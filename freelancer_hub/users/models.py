from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse

# Create your models here.


class Profile(AbstractUser):
    email = models.EmailField(unique=True)
    avatar = models.ImageField(upload_to="avatars/", blank=True, null=True)
    resume = models.FileField(upload_to="resumes/", blank=True, null=True)
    bio = models.TextField(null=True, blank=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    location = models.CharField(max_length=120, blank=True, null=True)

    def get_absolute_url(self):
        return reverse("profile_details", kwargs={"pk": self.pk})
