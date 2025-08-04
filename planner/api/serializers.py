from rest_framework.serializers import ModelSerializer
from plans.models import Plan, Task


class PlanSerializer(ModelSerializer):
    class Meta:
        model = Plan
        fields = "__all__"


class TaskSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = "___all__"
