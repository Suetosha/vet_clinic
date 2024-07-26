import json
from datetime import datetime
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import TemplateView, CreateView, ListView
from utils.mixins import TitleMixin
from .forms import AppointmentForm, SlotForm
from .models import Appointment, Slot

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
            free_slots = get_free_slots(request.session['date'], request.session['doctor_id'])

            if free_slots:
                request.session['free_slots'] = [time.strftime('%H:%M') for time in free_slots]
                return HttpResponseRedirect(reverse('clinic:appointment_slots'))
            else:
                messages.error(request, 'К сожалению, на данную дату не осталось мест')
                return HttpResponseRedirect(reverse('clinic:appointment'))


class AppointmentSlotsCreateView(LoginRequiredMixin, TitleMixin, SuccessMessageMixin, CreateView):
    template_name = 'clinic/appointment_slots.html'
    title = 'Запись на прием - выберите время'
    form_class = SlotForm
    model = Appointment,  User

    def get_form_kwargs(self):
        kwargs = super(AppointmentSlotsCreateView, self).get_form_kwargs()
        kwargs['doctor_id'] = self.request.session['doctor_id']
        kwargs['date'] = self.request.session['date']
        free_slots = self.request.session['free_slots']

        if free_slots:
            kwargs['free_slots'] = free_slots
        return kwargs

    def post(self, request, *args, **kwargs):
        form = SlotForm(request.POST)
        if form.is_valid():
            date, time = datetime.strptime(request.session['date'], "%Y-%m-%d"), form.cleaned_data['time']
            date_time = datetime.combine(date, time)

            appointment = Appointment(
                date_time=date_time,
                doctor=User.objects.get(id=request.session['doctor_id']),
                pet=Pet.objects.get(id=request.session['pet_id'])
            )

            appointment.save()
            messages.success(request, 'Вы успешно записались на прием')
            return HttpResponseRedirect(reverse('users:profile'))


def get_free_slots(selected_date, doctor_id):
    selected_date = datetime.strptime(selected_date, '%Y-%m-%d').date()
    all_times = [time for time in Slot.objects.filter(doctor=doctor_id)
                                              .values_list('time', flat=True)]

    closed_slots = [app for app in Appointment.objects.filter(doctor=doctor_id)
                                                      .values_list('date_time', flat=True)]

    filtered_closed_slots = list(filter(lambda dt: dt.date() == selected_date, closed_slots))
    closed_time = list(map(lambda dt: dt.time(), filtered_closed_slots))
    free_slots = []

    for time in all_times:
        if time not in closed_time:
            free_slots.append(time)

    return free_slots
