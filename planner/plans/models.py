from django.db import models
from accounts.models import CustomUser
from django.urls import reverse,reverse_lazy
# Create your models here.


class Plan(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="plans",default=None)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("home", kwargs={"pk": self.pk})
    
class Task(models.Model):
    name = models.CharField(max_length=100)
    deadline = models.DateTimeField()
    plan = models.ForeignKey(Plan, related_name="tasks", on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse("home")
    

    def __str__(self):
        return self.name
