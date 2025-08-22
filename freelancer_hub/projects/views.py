from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, DetailView,CreateView,UpdateView,DeleteView, View
from .models import Project, Category
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
# Create your views here.

class ProjectsList(ListView):
    model = Project
    context_object_name = "Projects"
    template_name = "projects/home.html"
    ordering = ["-status","-created_at"]
    paginate_by = 9
    
    def get_queryset(self):
        qs = super().get_queryset()
        
        # to apply to other's projects not yours
        if self.request.user.is_authenticated:
            qs = qs.exclude(created_by = self.request.user).order_by("-status","-created_at")
        
        # filter by category
        category_slug = self.request.GET.get("category")
        if category_slug:
            qs = qs.filter(category__slug = category_slug)
            
        return qs
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        
        context["categories"] = Category.objects.all()
        context["selected_category"] = self.request.GET.get("category")
        
        return context
    

class ProjectDetail(DetailView):
    model = Project
    context_object_name = "project"
    template_name = "projects/project_detail.html"
    

class ProjectCreate(LoginRequiredMixin,CreateView):
    model = Project
    fields = ["title","description","budget","deadline"]
    template_name = "projects/project_add.html"
    
    def form_valid(self, form):
        form.instance.created_by = self.request.user # assign current user 
        return super().form_valid(form)

    
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

class CloseProject(LoginRequiredMixin, UserPassesTestMixin,View):
    
    def post(self, request, pk):
        project = get_object_or_404(Project, pk=pk)
        project.status = False
        project.save()
        return redirect("project_detail", pk=pk)
    
    def test_func(self):
        project = get_object_or_404(Project, pk = self.kwargs["pk"])
        return self.request.user == project.created_by
    
    