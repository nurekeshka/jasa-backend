from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from django.urls import reverse_lazy


from .forms import CreationForm
from telegram.models import TelegramUser


class SignUp(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy('events:index')

    def form_valid(self, form):
        print("Hello?")
        print(self.kwargs['user_id'])
        user_id = self.kwargs['user_id']
        telegram_user = TelegramUser.objects.get(id=user_id)
        telegram_user.user = form.save()
        telegram_user.save()

        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        ctx = super(SignUp, self).get_context_data(**kwargs)
        ctx['user_id'] = self.kwargs['user_id']
        return ctx


class Login(LoginView):
    def form_valid(self, form):
        user_id = self.kwargs['user_id']
        telegram_user = TelegramUser.objects.get(id=user_id)
        telegram_user.user = form.get_user()
        telegram_user.save()

        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        ctx = super(Login, self).get_context_data(**kwargs)
        ctx['user_id'] = self.kwargs['user_id']
        return ctx


class Logout(LogoutView):
    def dispatch(self, request, *args, **kwargs):
        user_id = self.kwargs['user_id']
        telegram_user = TelegramUser.objects.get(id=user_id)
        telegram_user.user = None
        telegram_user.save()

        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        ctx = super(Logout, self).get_context_data(**kwargs)
        ctx['user_id'] = self.kwargs['user_id']
        return ctx
