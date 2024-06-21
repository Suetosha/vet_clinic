from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponse
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView

from utils.mixins import TitleMixin
from vet_apps.users.forms import UserLoginForm, UserRegistrationForm, PetRegistrationForm
from vet_apps.users.models import Pet


class UserLoginView(TitleMixin, LoginView):
    template_name = 'users/login.html'
    form_class = UserLoginForm
    title = 'Авторизация'


class UserRegistrationView(TitleMixin, SuccessMessageMixin, CreateView):
    template_name = 'users/registration.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('users:login')
    success_message = 'Вы успешно зарегистрировались'
    title = 'Регистрация'


class UserProfileView(TitleMixin, TemplateView):
    template_name = 'users/profile.html'
    title = 'Профиль'
    model = User

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context['pets'] = Pet.objects.filter(user=request.user)
        return self.render_to_response(context)


class PetCreateView(TitleMixin, CreateView):
    template_name = 'users/pets/create.html'
    title = 'Добавление питомца'
    model = Pet
    form_class = PetRegistrationForm

    def get_success_url(self):
        return reverse('users:profile')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class PetProfileView(TitleMixin, UpdateView):
    template_name = 'users/pets/profile.html'
    title = f'Профиль питомца'
    model = Pet
    form_class = PetRegistrationForm

    def get_success_url(self):
        return reverse_lazy('users:profile')


