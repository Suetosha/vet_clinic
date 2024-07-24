from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from django.contrib.auth.models import User
from django.forms import ModelForm, FileInput

from vet_apps.users.models import Pet


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='логин', widget=forms.TextInput(attrs={
        'class': "form-control", 'placeholder': "Введите имя пользователя"}))

    password = forms.CharField(label='пароль', widget=forms.PasswordInput(attrs={
        'class': "form-control", 'placeholder': "Введите пароль"}))


class UserRegistrationForm(UserCreationForm):

    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={
        'class': "form-control", 'placeholder': "Введите имя пользователя"}))

    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={
        'class': "form-control", 'placeholder': "Введите пароль"}))

    password2 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={
        'class': "form-control", 'placeholder': "Повторите пароль"}))

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')


class PetRegistrationForm(ModelForm):
    name = forms.CharField(label='Имя', widget=forms.TextInput(attrs={
        'class': "form-control", 'placeholder': "Введите имя питомца", 'required': 'Нужно ввести имя питомца'}))

    pet_type = forms.ChoiceField(label='Вид', choices=((1, 'Кошка'), (2, 'Собака')),
                                 widget=forms.Select(attrs={'class': "btn btn-secondary dropdown-toggle"}))

    breed = forms.CharField(label='Порода', widget=forms.TextInput(attrs={
        'class': "form-control", 'placeholder': "Введите породу"}))

    age = forms.IntegerField(label='Возраст', initial=1, widget=forms.NumberInput(attrs={
        'class': "form-control", 'placeholder': "Введите возраст питомца"}))

    photo = forms.ImageField(label='Фото', required=False, widget=FileInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Pet
        fields = ('name', 'pet_type', 'breed', 'age', 'photo')


