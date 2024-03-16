# Generated by Django 5.0.3 on 2024-03-09 13:58

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lan_origin', models.CharField(choices=[('NL', 'Dutch'), ('EN', 'English'), ('CN', 'Chinese')], max_length=2)),
                ('creation_date', models.DateTimeField(verbose_name='date created')),
                ('modification_date', models.DateTimeField(verbose_name='date modified')),
                ('upload_by_userId', models.BigIntegerField(verbose_name='upload by userId')),
                ('image_source', models.ImageField(upload_to='cardImages/', verbose_name='source_image')),
            ],
        ),
        migrations.CreateModel(
            name='CardAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_text', models.CharField(choices=[('FL', 'flash'), ('DN', 'done'), ('PA', 'pass'), ('RE', 'repeat')], max_length=2)),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='card.card')),
            ],
        ),
        migrations.CreateModel(
            name='UserCardAnswer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='card.cardanswer')),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='card.card')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]
