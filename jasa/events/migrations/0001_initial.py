# Generated by Django 2.2.19 on 2022-07-30 12:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Event title')),
                ('description', models.TextField(verbose_name='Event description')),
                ('sign_up_url', models.URLField(verbose_name='Sign up URL')),
                ('photo', models.URLField(verbose_name='Event photo URL')),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='Event publish date')),
                ('start_date', models.DateTimeField(verbose_name='Event start date')),
                ('end_date', models.DateTimeField(verbose_name='Event end date')),
                ('address', models.CharField(max_length=255, verbose_name='Address')),
                ('longitude', models.FloatField(verbose_name='Longitude')),
                ('latitude', models.FloatField(verbose_name='Latitude')),
                ('organizer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to=settings.AUTH_USER_MODEL, verbose_name='Event organizer')),
            ],
            options={
                'verbose_name': 'Event',
                'verbose_name_plural': 'Events',
                'ordering': ['-pub_date'],
            },
        ),
    ]