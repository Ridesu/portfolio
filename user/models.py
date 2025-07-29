from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)
    email = models.EmailField(max_length=255, unique=True)
    role = models.CharField(max_length=150)
    firstname = models.CharField(max_length=255, blank=True)
    lastname= models.CharField(max_length=255, blank=True)

