# Generated by Django 5.0.3 on 2024-03-10 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0005_alter_card_modification_date_alter_card_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='image_source',
            field=models.ImageField(upload_to='', verbose_name='source_image'),
        ),
    ]
