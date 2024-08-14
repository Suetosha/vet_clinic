from django.contrib import admin

from vet_apps.clinic.models import Slot, Appointment
from django.contrib.auth.admin import UserAdmin
from vet_apps.users.models import CustomUser


@admin.register(CustomUser)
class UserAdmin(UserAdmin):
    list_display = ('username', 'first_name', 'last_name', 'image')
    fieldsets = [
        (
            None,
            {
                "fields": ('username', 'first_name', 'last_name', 'groups', 'password', 'image', 'description'),
            },
        ),
    ]


@admin.register(Slot)
class DoctorSlotsAdmin(admin.ModelAdmin):
    pass


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('slot', 'date', 'pet', 'description')







