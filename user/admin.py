from django.contrib import admin
from .models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'target_lan', 'grade', 'night_mode')

admin.site.register(UserProfile, UserProfileAdmin)