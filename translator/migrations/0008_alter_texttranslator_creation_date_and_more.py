# Generated by Django 5.0.3 on 2024-04-09 17:18

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0017_alter_card_lan'),
        ('translator', '0007_alter_texttranslator_creation_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='texttranslator',
            name='creation_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 4, 9, 19, 18, 10, 522135), verbose_name='date created'),
        ),
        migrations.AlterField(
            model_name='texttranslator',
            name='modification_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2024, 4, 9, 19, 18, 10, 522135), verbose_name='date modified'),
        ),
        migrations.CreateModel(
            name='TextTokenizer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tokens', models.JSONField(blank=True, default=list)),
                ('creation_date', models.DateTimeField(blank=True, default=datetime.datetime(2024, 4, 9, 19, 18, 10, 522936), verbose_name='date created')),
                ('modification_date', models.DateTimeField(blank=True, default=datetime.datetime(2024, 4, 9, 19, 18, 10, 522936), verbose_name='date modified')),
                ('card', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='tokens', to='card.card')),
            ],
        ),
    ]