from django.urls import path
from . import views


urlpatterns = [
    path("", views.PlanList.as_view()),
    path("<int:id>/", views.PlanDetails.as_view()),
]
