from django.urls import path
from . import views

urlpatterns = [
    # path("", views.Home, name = "home"),
    path("",views.Home.as_view(), name='home'),
    path("add",views.AddContact.as_view(),name="add_contact"),
    path("edit/<int:pk>",views.EditContact.as_view(),name="edit_contact"),
    path("delete/<int:pk>",views.DeleteContact.as_view(),name="delete_contact"),
]
