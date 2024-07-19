from datetime import datetime
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import TemplateView, CreateView
from utils.mixins import TitleMixin
from .forms import AppointmentForm, SlotForm
from .models import Appointment

from ..users.models import Pet


class HomeTemplateView(TitleMixin, TemplateView):
    template_name = "clinic/home.html"
    title = "Главная страница"


class AboutUsTemplateView(TitleMixin, TemplateView):
    template_name = "clinic/about.html"
    title = "О нас"


class AppointmentCreateView(LoginRequiredMixin, TitleMixin, CreateView):
    template_name = 'clinic/appointment.html'
    title = 'Запись на прием'
    form_class = AppointmentForm
    model = Appointment, User

    def get_form_kwargs(self):
        kwargs = super(AppointmentCreateView, self).get_form_kwargs()
        kwargs['user_id'] = self.request.user.id
        return kwargs

    def post(self, request, *args, **kwargs):
        form = AppointmentForm(request.POST)
        if form.is_valid():
            request.session['pet_id'] = form.cleaned_data['pet'].id
            request.session['doctor_id'] = form.cleaned_data['doctor'].id
            request.session['date'] = form.cleaned_data['date'].strftime('%Y-%m-%d')
            return HttpResponseRedirect(reverse('clinic:appointment_slots'))


class AppointmentSlotsCreateView(LoginRequiredMixin, TitleMixin, CreateView):
    template_name = 'clinic/appointment_slots.html'
    title = 'Запись на прием - выберите время'
    form_class = SlotForm
    model = Appointment, User

    def post(self, request, *args, **kwargs):
        form = SlotForm(request.POST)
        if form.is_valid():
            date_time = datetime.strptime(request.session['date'] + ' ' + form.cleaned_data['time'], "%Y-%m-%d %H:%M")

            app = Appointment(
                date_time=date_time,
                doctor=User.objects.get(id=request.session['doctor_id']),
                user=request.user,
                pet=Pet.objects.get(id=request.session['pet_id'])
            )

            app.save()
            return HttpResponseRedirect(reverse('clinic:home'))
