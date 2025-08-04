from django.urls import path
from . import views


urlpatterns = [
    path("plans/", views.PlanList.as_view()),
    path("plans/<int:pk>/", views.PlanDetails.as_view()),
    path("plans/<int:pk>/tasks/", views.TaskList.as_view()),
]
