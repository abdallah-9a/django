from django.db import models
from users.models import Profile
from django.urls import reverse
# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    budget = models.DecimalField(max_digits= 5,decimal_places=2)
    created_by = models.ForeignKey(Profile,related_name="projects", on_delete=models.CASCADE)
    deadline = models.DateField()
    status = models.BooleanField(default=True) # True for open, False for closed
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def get_absolute_url(self):
        return reverse("project_detail", kwargs={"pk": self.pk})
    
    def __str__(self):
        return self.title