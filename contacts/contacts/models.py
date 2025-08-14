from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Contact(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=15,blank=True,null=True) # Need to handle it allow only phones number
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="contacts")
    
    class Meta:
        unique_together = ("email","username")
    
    
    def __str__(self):
        return f"{self.username} <{self.email}>"
    