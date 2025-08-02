from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)

    USERNAME_FIELD = "email"  # login by email
    REQUIRED_FIELDS = ["username"]  # required when creating superuser

    def __str__(self):
        return self.username
