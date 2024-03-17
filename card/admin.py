from django.contrib import admin
from django.contrib.auth.models import User
from .models import Card
from django.utils import timezone


class CardAdmin(admin.ModelAdmin):
    fields = ["image", "text", "lan", "creation_date", "modification_date", "upload_by_userName"]
    list_display = ["image", "lan", "text", "upload_by_userName", "modification_date", "creation_date"]
    def change_view(self, request, object_id, form_url='', extra_context=None):
        # Get the object instance
        obj = Card.objects.get(pk=object_id)
        # Pass the instance to the template context
        extra_context = extra_context or {}
        extra_context['instance'] = obj
        return super().change_view(request, object_id, form_url, extra_context=extra_context)      
       
    def get_form(self, request, obj=None, **kwargs):
            form = super().get_form(request, obj, **kwargs)
            if obj is None:  # Only fill the field for new instances
                form.base_fields['upload_by_userName'].initial = request.user.username
                form.base_fields['creation_date'].initial = timezone.now()
                form.base_fields['modification_date'].initial = timezone.now()
            return form    
    def save_model(self, request, obj, form, change):
        if not obj.upload_by_userName:
            obj.upload_by_userName = request.user.username
        super().save_model(request, obj, form, change)

# Register your models here.
admin.site.register(Card, CardAdmin)
