from django.urls import path
from . import views

urlpatterns = [
    path("", views.ProjectsList.as_view(), name="home"),
    path("project-detail/<int:pk>/", views.ProjectDetail.as_view(),name="project_detail"),
    path("add/",views.ProjectCreate.as_view(),name="add_project"),
    path("edit/<int:pk>/",views.ProjectEdit.as_view(),name="edit_project"),
    path("delete/<int:pk>/",views.ProjectDelete.as_view(),name="delete_project"),
    
]
