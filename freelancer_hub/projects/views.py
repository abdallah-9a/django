from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView,DeleteView
from .models import Project
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
# Create your views here.

class ProjectsList(ListView):
    model = Project
    context_object_name = "Projects"
    template_name = "projects/home.html"
    ordering = ["-status"]


class ProjectDetail(DetailView):
    model = Project
    context_object_name = "project"
    template_name = "projects/project_detail.html"
    

class ProjectEdit(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Project
    fields = ["title","description","budget","deadline","status"]
    template_name = "projects/project_edit.html"
    
    def test_func(self):
        return self.request.user.id == self.get_object().created_by.id

class ProjectDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Project
    success_url = reverse_lazy("home")
    template_name = "projects/project_delete.html"
    
    def test_func(self):
        return self.request.user.id == self.get_object().created_by.id