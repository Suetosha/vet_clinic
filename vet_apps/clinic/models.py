from django.db import models
from django.conf import settings
from ..users.models import Pet


class Slot(models.Model):
    doctor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    time = models.TimeField()

    objects = models.Manager()

    def __str__(self):
        return f'{self.doctor} {self.time}'


class Appointment(models.Model):
    slot = models.ForeignKey(Slot, on_delete=models.CASCADE)
    date = models.DateField()
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    description = models.TextField()

    objects = models.Manager()
