from django.shortcuts import render
from plans.models import Plan, Task
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from .serializers import PlanSerializer, TaskSerializer

# Create your views here.


class PlanList(ListAPIView):
    serializer_class = PlanSerializer

    def get_queryset(self):
        return Plan.objects.filter(user=self.request.user)


class PlanDetails(RetrieveUpdateDestroyAPIView):
    serializer_class = PlanSerializer

    def get_queryset(self):
        return Plan.objects.filter(user=self.request.user, id=self.kwargs["pk"])


class TaskList(ListAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        plan = Plan.objects.get(user=self.request.user, id=self.kwargs["pk"])
        return plan.tasks.all()
