from django.shortcuts import render,redirect
from .forms import SignUpForm
from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.urls import reverse_lazy

# Create your views here.

class SignUp(CreateView):
    model = User
    form_class = SignUpForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy("login")