from django.views.generic import CreateView
from django.urls import reverse_lazy


from .forms import CreationForm
from telegram.models import TelegramUser

class SignUp(CreateView):
    form_class = CreationForm

    success_url = reverse_lazy('users:login')
    template_name = 'users/signup.html'

    def form_valid(self, form):
        telegram_user = TelegramUser.objects.get(id=self.kwargs['user_id'])
        telegram_user.user = form.save()
        telegram_user.save()

        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        ctx = super(SignUp, self).get_context_data(**kwargs)
        ctx['user_id'] = self.kwargs['user_id']
        return ctx
