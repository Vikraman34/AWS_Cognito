from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('home', views.home, name='home'),
    path('change_password', views.change_password, name='change_password'),
    path('forgot_password1', views.forgot_password1, name='forgot_password1'),
    path('forgot_password2', views.forgot_password2, name='forgot_password2'),
    path('sign_up1', views.sign_up1, name='sign_up1'),
    path('sign_up2', views.sign_up2, name='sign_up2')
]