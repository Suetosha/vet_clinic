from django.contrib import admin
from django import forms
from django.contrib.admin.widgets import AdminFileWidget
from django.db import models
from django.utils.html import format_html

from vet_apps.clinic.models import Slot
from django.contrib.auth.admin import UserAdmin
from vet_apps.users.models import CustomUser


@admin.register(CustomUser)
class UserAdmin(UserAdmin):
    pass
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





