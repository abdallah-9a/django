from django.shortcuts import render, HttpResponse
from .forms import LoginForm
from django.contrib.auth import authenticate, login

# Create your views here.


def Login(request):# Manually create login view function to understand process for login
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(
                request, username=cd["username"], password=cd["password"]
            )
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse("Login Successfully")
                else:
                    return HttpResponse("Disable Account")
            else:
                return HttpResponse("Invalid Login")
    form = LoginForm()
    context = {"form": form}
    return render(request, "account/login.html", context)
