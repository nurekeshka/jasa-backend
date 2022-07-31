# Generated by Django 2.2.19 on 2022-07-29 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TelegramUser',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True, verbose_name='User id')),
                ('username', models.CharField(blank=True, max_length=255, null=True, verbose_name='Username')),
                ('first_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='First name')),
                ('last_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Last name')),
            ],
            options={
                'verbose_name': 'Telegram user',
                'verbose_name_plural': 'Telegram users',
            },
        ),
    ]