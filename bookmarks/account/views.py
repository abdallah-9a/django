from django.shortcuts import render, HttpResponse
from .forms import LoginForm, SignUpForm, UserEditForm, ProfileForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import Profile


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
    if request.method == "POST":
        user_form = SignUpForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data["password"])
            new_user.save()
            # create user profile 
            Profile.objects.create(user=new_user)
            context = {"new_user": new_user}
            return render(request, "registration/signup_done", context)
    user_form = SignUpForm()
    context = {"user_form": user_form}
    return render(request, "registration/signup.html", context)

@login_required
def Edit(request):
    if request.method == "POST":
        user_form = UserEditForm(instance= request.user, data = request.POST)
        profile_form = ProfileForm(instance=request.user.profile, data = request.POST, files = request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
    else:
         user_form = UserEditForm(instance=request.user)   
         profile_form = ProfileForm(instance=request.user.profile)
    context = {"user_form":user_form, "profile_form":profile_form}
    return render(request,"account/edit.html",context)
            