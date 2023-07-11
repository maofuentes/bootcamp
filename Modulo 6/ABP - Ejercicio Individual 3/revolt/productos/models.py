from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    telefono = models.CharField(max_length=15, blank=True)
    direccion = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return self.username
