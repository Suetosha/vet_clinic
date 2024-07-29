from django.contrib.auth.models import User
from django.forms import ModelForm, fields
from django import forms

from vet_apps.clinic.models import Appointment, Slot
from vet_apps.users.models import Pet


class AppointmentForm(ModelForm):

    date = fields.DateField(
        label='Дата',
        widget=forms.widgets.DateInput(attrs={'type': 'date', 'class': ' form-control'})
    )

    doctor = forms.ChoiceField(
        label='Врачи',
        choices=[(doctor.id, doctor.username) for doctor in User.objects.filter(groups__name='Doctor')],
        widget=forms.Select(attrs={'class': 'form-select'})
        )

    def __init__(self, *args, **kwargs):
        user_id = kwargs.pop('user_id', None)
        super().__init__(*args, **kwargs)
        if user_id:
            self.fields['pet'].choices = [(pet.id, pet.name) for pet in Pet.objects.filter(user_id=user_id)]
            self.fields['pet'].label = 'Питомец'
            self.fields['pet'].widget.attrs.update({'class': 'form-select'})

    class Meta:
        model = Appointment
        fields = ('pet',)


class SlotForm(ModelForm):
    def __init__(self, *args, **kwargs):
        doctor_id = kwargs.pop('doctor_id', None)
        free_slots = kwargs.pop('free_slots', None)
        super().__init__(*args, **kwargs)

        if doctor_id:
            self.fields['time'] = forms.ChoiceField(
                label='Время',
                choices=[(slot, slot) for slot in free_slots],
                widget=forms.Select(attrs={'class': 'form-select'})

            )

    class Meta:
        model = Slot
        fields = ('time',)

