from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from django.contrib.auth.models import User


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='логин', widget=forms.TextInput(attrs={
        'class': "form-control", 'placeholder': "Введите имя пользователя"}))

    password = forms.CharField(label='пароль', widget=forms.PasswordInput(attrs={
        'class': "form-control", 'placeholder': "Введите пароль"}))

    class Meta:
        model = User
        fields = ['username', 'password']


class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(label='логин', widget=forms.TextInput(attrs={
        'class': "form-control", 'placeholder': "Введите имя пользователя"}))

    password1 = forms.CharField(label='пароль', widget=forms.PasswordInput(attrs={
        'class': "form-control", 'placeholder': "Введите пароль"}))

    password2 = forms.CharField(label='пароль', widget=forms.PasswordInput(attrs={
        'class': "form-control", 'placeholder': "Повторите пароль"}))