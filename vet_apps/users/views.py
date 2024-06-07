from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView

from utils.mixins import TitleMixin


class UserLoginView(TitleMixin, LoginView):
    template_name = 'users/login.html'
    title = 'Авторизация'


class UserRegistrationForm(TitleMixin, CreateView):
    template_name = 'users/registration.html'
    title = 'Регистрация'




