from django.contrib.auth.models import User
from django.forms import ModelForm, fields
from django import forms

from vet_apps.clinic.models import Appointment
from vet_apps.users.models import Pet


class AppointmentForm(ModelForm):
    date = fields.DateField(label='Дата', widget=forms.widgets.DateInput(attrs={'type': 'date'}))

    def __init__(self, *args, **kwargs):
        user_id = kwargs.pop('user_id', None)
        super().__init__(*args, **kwargs)
        if user_id:
            self.fields['pet'].choices = [(pet.id, pet.name) for pet in Pet.objects.filter(user_id=user_id)]
            self.fields['doctor'].choices = [(doctor.id, doctor.username) for doctor in
                                             User.objects.filter(groups__name='Doctor')]

    class Meta:
        model = Appointment
        fields = ('pet', 'doctor')


class SlotForm(ModelForm):
    time = forms.ChoiceField(label='Время', choices=[('17:00', '17:00'), ('15:30', '15:30'), ('16:00', '16:00')])

    class Meta:
        model = Appointment
        fields = ('time',)

