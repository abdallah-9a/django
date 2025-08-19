from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Project

# Create your views here.

class ProjectsList(ListView):
    model = Project
    context_object_name = "Projects"
    template_name = "projects/home.html"


