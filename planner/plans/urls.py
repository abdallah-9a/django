from django.urls import path
from . import views

urlpatterns = [
    path("", views.Home, name="home"),
    path("plan/<int:pk>/", views.PlanDetails, name="plan_details"),
    path("plan/add", views.AddPlan.as_view(), name="add_plan"),
    path("plan/delete/<int:pk>/", views.DeletePlan.as_view(), name="delete_plan"),
    path("plan/task/add/<int:plan_id>/", views.AddTask.as_view(), name="add_task"),
    path("plan/task/delete/<int:pk>/", views.DeleteTask.as_view(), name="delete_task"),
]
