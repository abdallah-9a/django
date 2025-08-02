from django.shortcuts import render
from .models import Plan, Task
from django.views.generic import CreateView, UpdateView, DeleteView

# Create your views here.


def Home(request):
    user = request.user
    plans = user.plans.all()
    context = {"plans": plans}
    return render(request, "plans/home.html", context)


class AddTask(CreateView):
    model = Task
    fields = ["name", "deadline"]
    template_name = "plans/add_task.html"

    def form_valid(self, form):
        plan_id = self.kwargs.get("plan_id")
        form.instance.plan = Plan.objects.get(id=plan_id)
        return super().form_valid(form)


class AddPlan(CreateView):
    model = Plan
    fields = [
        "name",
    ]
    template_name = "plans/add_plan.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


def PlanDetails(request, plan_id):
    plan = Plan.objects.get(id=plan_id)
    context = {"plan": plan}
    return render(request, "plans/plan_details.html", context)
