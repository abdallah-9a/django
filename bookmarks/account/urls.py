from django.urls import path
from . import views
from django.contrib.auth import views as auth_views  # Take fully control

urlpatterns = [
    path("login", views.Login, name="login"),
]
