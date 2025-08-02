from django.urls import path
from . import views

urlpatterns = [
    path("", views.Home, name="home"),
    path("add/<int:plan_id>/", views.AddTask.as_view(), name="add_task"),
    path("add/", views.AddPlan.as_view(), name="add_plan"),
]
