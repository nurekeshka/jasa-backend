from django.urls import path

from . import views


app_name = 'users'

urlpatterns = [
    path(
        'signup/<int:user_id>/',
        views.SignUp.as_view(template_name='users/signup.html'),
        name='signup'
    ),
    path(
        'logout/<int:user_id>/', 
        views.Logout.as_view(template_name='users/logout.html'), 
        name='logout'
    ),
    path(
        'login/<int:user_id>/',
        views.Login.as_view(template_name='users/login.html'),
        name='login'
    ),
] 