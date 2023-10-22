from django.db import models
from django.contrib.auth.models import AbstractBaseUser, AbstractUser, UserManager


class User(AbstractUser):
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    username = models.CharField(max_length=200, unique=True)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email", "password"]

    objects = UserManager()

    def __str__(self):
        return self.username
