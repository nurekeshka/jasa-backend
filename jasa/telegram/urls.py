from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from jasa.settings import BOT_TOKEN
from . import views


app_name = 'telegram'

urlpatterns = [
    path(
        '',
        views.set_webhook,
        name='setup_webhook',
    ),
    path(
        f'{BOT_TOKEN}/', 
        csrf_exempt(views.Process_updates.as_view()), 
        name='process_updates'
    )
]
