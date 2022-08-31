from django.views.generic import CreateView
from django.urls import reverse_lazy

from .forms import CreationForm


class SignUp(CreateView):
    """This view is used to create a new user."""

    form_class = CreationForm
    success_url = reverse_lazy('events:index')
