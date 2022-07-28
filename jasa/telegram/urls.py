from django.urls import path

from jasa.settings import BOT_TOKEN
from . import views


app_name = 'telegram'

urlpatterns = [
    path('/', views.webhook, name='webhook'),
    path(f'/{BOT_TOKEN}', views.process_updates, name='process_updates')
]
