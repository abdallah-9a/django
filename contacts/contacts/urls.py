from django.urls import path
from . import views

urlpatterns = [
    path("", views.Home, name = "home"),
    path("add",views.AddContact.as_view(),name="add_contact"),
]
