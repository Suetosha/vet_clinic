from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from utils.mixins import TitleMixin


class HomeTemplateView(TitleMixin, TemplateView):
    template_name = "clinic/home.html"
    title = "Главная страница"


class AboutUsTemplateView(TitleMixin, TemplateView):
    template_name = "clinic/about.html"
    title = "О нас"


# @login_required()
class AppointmentTemplateView(TitleMixin, TemplateView):
    template_name = 'clinic/appointment.html'
    title = 'Запись к врачу'
