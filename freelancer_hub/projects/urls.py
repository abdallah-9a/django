from django.urls import path
from . import views

urlpatterns = [
    path("", views.ProjectsList.as_view(), name="home"),
    path("project-detail/<int:pk>/", views.ProjectDetail.as_view(),name="project_detail"),
    
]
