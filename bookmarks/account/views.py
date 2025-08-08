from django.shortcuts import render, HttpResponse
from .forms import LoginForm, SignUpForm
from django.contrib.auth import authenticate, login

# Create your views here.


# def Login(request):# From Scrach create login view function to understand process for login
#     if request.method == "POST":
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             cd = form.cleaned_data
#             user = authenticate(
#                 request, username=cd["username"], password=cd["password"]
#             )
#             if user is not None:
#                 if user.is_active:
#                     login(request, user)
#                     return HttpResponse("Login Successfully")
#                 else:
#                     return HttpResponse("Disable Account")
#             else:
#                 return HttpResponse("Invalid Login")
#     form = LoginForm()
#     context = {"form": form}
#     return render(request, "account/login.html", context)


def Home(request):
    return render(request, "base.html")


def SignUp(request):
    if request.methpd == "POST":
        user_form = SignUpForm(request.POST)
        if user_form.is_valid():
            user_form.save(commit=False)
            user_form.set_password(user_form.cleaned_data["password"])
            user_form.save()
            context = {"form": user_form}
            return render(request, "account/register_done", context)
    user_form = SignUpForm()
    context = {"form": user_form}
    return render(request, "account/register.html", context)
