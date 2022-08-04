# Generated by Django 2.2.19 on 2022-08-03 03:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('telegram', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='telegramuser',
            old_name='id',
            new_name='telegram_id',
        ),
        migrations.AddField(
            model_name='telegramuser',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL, verbose_name='User account'),
        ),
    ]
