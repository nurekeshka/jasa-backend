from django.views.generic import CreateView
from django.contrib.auth.views import LoginView

from django.urls import reverse_lazy

from .forms import CreationForm, LoginForm


class SignUp(CreateView):
    """This view is used to create a new user."""

    form_class = CreationForm
    success_url = reverse_lazy('events:index')


# https://stackoverflow.com/questions/53431476/django-how-to-implement-a-remember-me-radio-button-on-a-login-page
class UpdatedLoginView(LoginView):
    """This view implments some more features on LoginView"""

    form_class = LoginForm

    def get_initial(self):
        auth_data = self.request.session.get('remember_me', {})

        self.initial['username'] = auth_data.get('username', '')
        self.initial['password'] = auth_data.get('password', '')
        self.initial['remember_me'] = False

        return super(UpdatedLoginView, self).get_initial()

    def get_context_data(self, **kwargs):
        context = super(UpdatedLoginView, self).get_context_data(**kwargs)
        return context


    def form_valid(self, form):
        username = form.cleaned_data['username'].strip()
        password = form.cleaned_data['password'].strip()
        remember_me = form.cleaned_data['remember_me']

        current_session = self.request.session

        if remember_me:
            print(username, password, remember_me)
            current_session['remember_me'] = {
                'username': username,
                'password': password
            }
            current_session.set_expiry(1209600) # 2 weeks
            current_session.modified = True
    
        return super(UpdatedLoginView, self).form_valid(form)
