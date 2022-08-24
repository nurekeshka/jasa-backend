from django.urls import path

from . import views


app_name = 'users'

urlpatterns = [
    path('login/', views.Login.as_view(), name='login'),
    path('login/<int:user_id>/', views.Login.as_view(), name='tg-login'),

    path('signup/', views.SignUp.as_view(), name='signup'),
    path('signup/<int:user_id>/', views.SignUp.as_view(), name='tg-signup'),

    path('logout/', views.Logout.as_view(), name='logout'),
    path('logout/<int:user_id>/', views.Logout.as_view(), name='tg-logout'),
] 