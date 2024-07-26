from django.contrib import admin
from django.contrib.auth.models import User
from django import forms
from django.forms import ChoiceField
from vet_apps.clinic.models import Slot


class DoctorSlotsAdminForm(forms.ModelForm):
    doctor = forms.ChoiceField(choices=[(doctor, doctor.username) for doctor in
                                        User.objects.filter(groups__name='Doctor')])

    class Meta:
        model = Slot
        fields = ('doctor', 'time')


@admin.register(Slot)
class DoctorSlotsAdmin(admin.ModelAdmin):
    pass


