from django.db import models
from users.models import Profile
from django.urls import reverse
from django.utils.text import slugify
# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    budget = models.DecimalField(max_digits= 5,decimal_places=2)
    created_by = models.ForeignKey(Profile,related_name="projects", on_delete=models.CASCADE)
    category = models.ForeignKey("Category",on_delete=models.SET_NULL,blank=True,null=True,related_name="projects")
    deadline = models.DateField()
    status = models.BooleanField(default=True) # True for open, False for closed
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    skills = models.ManyToManyField("Skill", related_name="projects")
    
    def get_absolute_url(self):
        return reverse("project_detail", kwargs={"pk": self.pk})
    
    def __str__(self):
        return self.title
    
class Category(models.Model):
    name = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=150, unique=True)
    skills = models.ManyToManyField("Skill",blank=True, related_name="categories")
    description = models.TextField(blank = True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ["name"]
    
    def save(self,*args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name
    

class Skill(models.Model):
    name = models.CharField(max_length=100,unique=True)
    slug = models.SlugField(max_length=150,unique=True,blank=True,null=True)
    
    def save(self,*args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name