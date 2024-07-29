from django.db import models
from django.contrib.auth.models import User
from ..users.models import Pet


class Slot(models.Model):
    doctor = models.ForeignKey(User, on_delete=models.CASCADE)
    time = models.TimeField()

    objects = models.Manager()


class Appointment(models.Model):
    slot = models.ForeignKey(Slot, on_delete=models.CASCADE, default=None)
    date = models.DateField(default=None)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)


    objects = models.Manager()


