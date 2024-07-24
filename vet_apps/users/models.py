from django.contrib.auth.models import User
from django.db import models


class Pet(models.Model):
    name = models.CharField(max_length=30)
    pet_type = models.CharField(max_length=30)
    breed = models.CharField(max_length=30)
    age = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to="media/", default="media/pet_default.png")

    objects = models.Manager()





