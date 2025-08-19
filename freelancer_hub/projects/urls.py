from django.urls import path
from . import views

urlpatterns = [
    path("", views.ProjectsList.as_view(), name="home"),
    
]
