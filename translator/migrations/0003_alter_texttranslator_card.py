# Generated by Django 5.0.3 on 2024-04-06 11:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0014_card_comment'),
        ('translator', '0002_alter_texttranslator_tokens_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='texttranslator',
            name='card',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='translations', to='card.card'),
        ),
    ]
