from datetime import datetime
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import TemplateView, CreateView
from utils.mixins import TitleMixin
from .forms import AppointmentForm, SlotForm
from .models import Appointment, Slot

from ..users.models import Pet, CustomUser


class HomeTemplateView(TitleMixin, TemplateView):
    template_name = "clinic/home.html"
    title = "Главная страница"


class DoctorsTemplateView(TitleMixin, TemplateView):
    template_name = "clinic/doctors.html"
    title = "О нас"

    def get_context_data(self, *args, **kwargs):
        context = super(DoctorsTemplateView, self).get_context_data(*args, **kwargs)
        context['doctors'] = [doctor for doctor in CustomUser.objects.filter(groups__name='Doctor')]
        return context


class DoctorInfoTemplateView(TitleMixin, TemplateView):
    template_name = "clinic/doctor_info.html"

    def get_context_data(self, *args, **kwargs):
        context = super(DoctorInfoTemplateView, self).get_context_data(*args, **kwargs)
        doctor = CustomUser.objects.get(id=kwargs['pk'])
        context['doctor'] = doctor
        context['title'] = f'{doctor.first_name} {doctor.last_name}'
        return context


class AppointmentCreateView(LoginRequiredMixin, TitleMixin, CreateView):
    template_name = 'clinic/appointment.html'
    title = 'Запись на прием'
    form_class = AppointmentForm
    model = Appointment, CustomUser

    def get_form_kwargs(self):
        kwargs = super(AppointmentCreateView, self).get_form_kwargs()
        kwargs['user_id'] = self.request.user.id
        return kwargs

    def post(self, request, *args, **kwargs):
        form = AppointmentForm(request.POST)

        if form.is_valid():
            request.session['pet_id'] = form.cleaned_data['pet'].id
            request.session['doctor_id'] = form.cleaned_data['doctor']
            request.session['date'] = form.cleaned_data['date'].strftime('%Y-%m-%d')
            request.session['description'] = form.cleaned_data['description']
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
    model = Appointment,  CustomUser

    def get_form_kwargs(self):
        kwargs = super(AppointmentSlotsCreateView, self).get_form_kwargs()
        kwargs['doctor_id'] = self.request.session['doctor_id']
        free_slots = self.request.session['free_slots']

        if free_slots:
            kwargs['free_slots'] = free_slots
        return kwargs

    def post(self, request, *args, **kwargs):
        form = SlotForm(request.POST)

        if form.is_valid():

            appointment = Appointment(
                slot=Slot.objects.get(time=form.cleaned_data['time'],
                                      doctor=CustomUser.objects.get(id=request.session['doctor_id'])),

                date=request.session['date'],
                pet=Pet.objects.get(id=request.session['pet_id']),
                description=request.session['description']
                )

            appointment.save()
            messages.success(request, 'Вы успешно записались на прием')
            return HttpResponseRedirect(reverse('users:profile'))


def get_free_slots(selected_date, doctor_id):
    selected_date = datetime.strptime(selected_date, '%Y-%m-%d').date()

    closed_slots = [app for app in Appointment.objects.filter(slot__doctor=doctor_id, date=selected_date)
                                                      .values_list('slot__time', flat=True)]

    free_slots = [time for time in Slot.objects.filter(doctor=doctor_id)
                                               .exclude(time__in=closed_slots)
                                               .values_list('time', flat=True)]

    return free_slots
