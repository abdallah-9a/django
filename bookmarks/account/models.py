from django.db import models
from django.conf import settings

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    birthdate = models.DateField(blank=True, null=True)
    # Unable to use imagefield because can't install pillow package to validate format and demesions
    # photo = models.ImageField(upload_to="") 
    photo = models.FileField(upload_to="photos/", blank=True) 
    def __str__(self):
        return self.user.username
