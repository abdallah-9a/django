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
