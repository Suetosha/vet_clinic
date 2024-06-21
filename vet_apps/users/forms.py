from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from django.contrib.auth.models import User
from django.forms import ModelForm

from vet_apps.users.models import Pet


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='логин', widget=forms.TextInput(attrs={
        'class': "form-control", 'placeholder': "Введите имя пользователя"}))

    password = forms.CharField(label='пароль', widget=forms.PasswordInput(attrs={
        'class': "form-control", 'placeholder': "Введите пароль"}))

    class Meta:
        model = User
        fields = ['username', 'password']


class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={
        'class': "form-control", 'placeholder': "Введите имя пользователя"}))

    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={
        'class': "form-control", 'placeholder': "Введите пароль"}))

    password2 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={
        'class': "form-control", 'placeholder': "Повторите пароль"}))


class PetRegistrationForm(ModelForm):
    name = forms.CharField(label='Имя питомца', widget=forms.TextInput(attrs={
        'class': "form-control", 'placeholder': "Введите имя питомца", 'required': 'Нужно ввести имя питомца'}))

    pet_type = forms.ChoiceField(label='Вид питомца', choices=((1, 'Кошка'), (2, 'Собака')))

    breed = forms.CharField(label='Порода питомца', widget=forms.TextInput(attrs={
        'class': "form-control", 'placeholder': "Введите породу"}))

    age = forms.IntegerField(label='Возраст питомца', initial=1, widget=forms.NumberInput(attrs={
        'class': "form-control", 'placeholder': "Введите возраст питомца"}))

    #photo = forms.ImageField(label='Фото питомца')

    class Meta:
        model = Pet
        fields = ('name', 'pet_type', 'breed', 'age')


