from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from django import forms


User = get_user_model()


class CreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email')


class LoginForm(AuthenticationForm):
    """Custom LoginForm to add a 'remember me' checkbox"""

    username = forms.CharField(
        label='',
        max_length=30,
        widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Username'}
        )
    )
    password = forms.CharField(
        label='',
        max_length=30,
        widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Password'},
            render_value=True
        )
    )
    remember_me = forms.BooleanField(
        label='Remember me',
        required=False,
        initial=False,
        widget=forms.CheckboxInput()
    )
