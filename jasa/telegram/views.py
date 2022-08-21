from django.http import HttpResponse, JsonResponse
from django.views import View
from telebot import types

from .bot import bot
from jasa.settings import DOMAIN, BOT_TOKEN


def set_webhook(request):
    """Set the webhook."""
    bot.remove_webhook()
    bot.set_webhook(url=f'{DOMAIN}/{BOT_TOKEN}/')
    return HttpResponse('OK', status=200)


class Process_updates(View):
    """Receive requests from telegram API."""

    def get(self, request, *args, **kwargs):
        return HttpResponse('Бот запусчен и работает.')
 
    def post(self, request, *args, **kwargs):
        json_str = request.body.decode('UTF-8')
        update = types.Update.de_json(json_str)
        bot.process_new_updates([update])
 
        return JsonResponse({'code': 200})
