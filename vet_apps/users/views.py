from django.contrib import messages
from django.contrib.auth.models import Group, User
from django.http import HttpResponseRedirect, HttpResponseBadRequest
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from utils.mixins import TitleMixin, GroupRequiredMixin

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

    def post(self, request, *args, **kwargs):
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            owner_group = Group.objects.get(name='Owner')
            user.groups.add(owner_group)
            messages.success(request, 'Вы успешно зарегистрировались')
            return HttpResponseRedirect(reverse_lazy('users:login'))
        else:
            return HttpResponseBadRequest("Некорректные данные")


class UserProfileView(TitleMixin, GroupRequiredMixin, TemplateView):
    group_required = 'Owner'
    template_name = 'users/profile.html'
    title = 'Профиль'
    model = User


class DoctorProfileView(TitleMixin, GroupRequiredMixin, TemplateView):
    group_required = 'Doctor'
    template_name = 'users/doctors/profile.html'
    title = 'Профиль врача'
    model = User


class PetCreateView(TitleMixin, SuccessMessageMixin, CreateView):
    template_name = 'users/pets/create.html'
    title = 'Добавление питомца'
    model = Pet
    form_class = PetRegistrationForm
    success_message = 'Вы успешно добавили питомца'

    def get_success_url(self):
        return reverse('users:profile')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class PetProfileView(TitleMixin, SuccessMessageMixin, UpdateView):
    template_name = 'users/pets/profile.html'
    title = 'Профиль питомца'
    model = Pet
    form_class = PetRegistrationForm
    success_message = 'Данные о питомце обновлены'

    def get_success_url(self, *args, **kwargs):
        return reverse_lazy(f'users:pet_profile', args=[self.object.pk])


class PetDeleteView(TitleMixin, DeleteView):
    model = Pet
    template_name = 'users/pets/delete.html'
    success_url = reverse_lazy('users:profile')
    title = 'Удаление профиля питомца'
