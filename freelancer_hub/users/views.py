from django.shortcuts import render
from django.views.generic import CreateView, DetailView, UpdateView
from .models import Profile
from .forms import SignUpForm
from django.urls import reverse_lazy

# Create your views here.


class SignUp(CreateView):
    form_class = SignUpForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy("login")


class ProfileDetail(DetailView):
    model = Profile
    context_object_name = "profile"
    template_name = "users/profile_detail.html"


class ProfileEdit(UpdateView):
    model = Profile
    fields = ["avatar", "bio", "phone_number", "location", "first_name", "last_name"]
    template_name = "users/profile_edit.html"
