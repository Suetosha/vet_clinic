from django.db import models
from django.contrib.auth.models import User
from ..users.models import Pet


class Appointment(models.Model):
    date_time = models.DateTimeField()
    doctor = models.ForeignKey(User, on_delete=models.CASCADE)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)

    objects = models.Manager()

