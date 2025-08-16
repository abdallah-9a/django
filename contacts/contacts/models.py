from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
# Create your models here.

class Contact(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=15,blank=True,null=True, 
                             validators= [RegexValidator(regex = r"^\+?\d{7,15}$",
                                                        message="Phone number must be between 7 and 15, and may start with +.")])
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="contacts")
    
    class Meta:
        # unique_together = ("email","user") # it become deprecated
        constraints = [models.UniqueConstraint(fields=["email","user"], name="unique_user_email")]
     
    def __str__(self):
        return f"{self.username} <{self.email}> {self.phone}"
    
    def get_absolute_url(self):
        return reverse("home")
    
    def clean(self):
        # check for the same user and email exclude the current contact
        if Contact.objects.filter(user = self.user, email = self.email).exclude(pk=self.pk).exists():
            raise ValidationError({"email": "You already have a contact with this email."})
        # check for duplicated phone number
        if Contact.objects.filter(user=self.user, phone = self.phone).exclude(pk=self.pk).exists():
            raise ValidationError({"phone":" You already have a contact with this phone number."})
        return super().clean()
    