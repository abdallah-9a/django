from django.shortcuts import render
from .models import Plan, Task

# Create your views here.


def Home(request):
    user = request.user
    plans = user.plans.all()
    context = {"plans": plans}
    return render(request, "plans/home.html", context)
