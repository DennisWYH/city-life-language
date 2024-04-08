# Generated by Django 5.0.3 on 2024-04-08 12:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('translator', '0005_alter_texttranslator_creation_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='texttranslator',
            name='creation_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 4, 8, 14, 41, 32, 665442), verbose_name='date created'),
        ),
        migrations.AlterField(
            model_name='texttranslator',
            name='modification_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 4, 8, 14, 41, 32, 665442), verbose_name='date modified'),
        ),
    ]
