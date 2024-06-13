from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from utils.mixins import TitleMixin
from django.contrib.messages.views import SuccessMessageMixin


class HomeTemplateView(TitleMixin, TemplateView):
    template_name = "clinic/home.html"
    title = "Главная страница"


class AboutUsTemplateView(TitleMixin, TemplateView):
    template_name = "clinic/about.html"
    title = "О нас"


class AppointmentTemplateView(LoginRequiredMixin, TitleMixin, TemplateView):
    template_name = 'clinic/appointment.html'
    title = 'Запись к врачу'

