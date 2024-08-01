import markdown
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.safestring import mark_safe


class CustomUser(AbstractUser):
    username = models.CharField(max_length=30, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    password = models.CharField(max_length=128)
    image = models.ImageField(upload_to="media/", default=None)
    description = models.TextField()


class Pet(models.Model):
    name = models.CharField(max_length=30)
    pet_type = models.CharField(max_length=30)
    breed = models.CharField(max_length=30)
    age = models.IntegerField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to="media/", default="media/pet_default.png")

    objects = models.Manager()





