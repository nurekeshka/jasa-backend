from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404

from .forms import CreationForm
from telegram.models import TelegramUser


class SignUp(CreateView):
    form_class = CreationForm
    template_name='users/signup.html'
    success_url = reverse_lazy('events:index')

    def form_valid(self, form):
        user_id = self.kwargs.get('user_id', '')

        if user_id:
            tg_user = get_object_or_404(TelegramUser, id=user_id)
            tg_user.user = form.save()
            tg_user.save()

        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        ctx = super(SignUp, self).get_context_data(**kwargs)
        ctx['user_id'] = self.kwargs.get('user_id', '')
        return ctx


class Login(LoginView):
    template_name='users/login.html'
    success_url = reverse_lazy('events:index')

    def form_valid(self, form):
        user_id = self.kwargs.get('user_id', '')

        if user_id:
            tg_user = get_object_or_404(TelegramUser, id=user_id)
            tg_user.user = form.get_user()
            tg_user.save()

        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        ctx = super(Login, self).get_context_data(**kwargs)
        ctx['user_id'] = self.kwargs.get('user_id', '')
        return ctx


class Logout(LogoutView):
    template_name='users/logout.html'

    def dispatch(self, request, *args, **kwargs):
        user_id = self.kwargs.get('user_id', '')

        if user_id:
            tg_user = get_object_or_404(TelegramUser, id=user_id)
            tg_user.user = None
            tg_user.save()

        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        ctx = super(Logout, self).get_context_data(**kwargs)
        ctx['user_id'] = self.kwargs.get('user_id', '')
        return ctx
