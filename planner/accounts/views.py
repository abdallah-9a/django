from django.shortcuts import render
from .forms import SignUpForm
from .models import CustomUser
from django.views.generic import CreateView
from django.urls import reverse_lazy

# Create your views here.


class SignUp(CreateView):
    model = CustomUser
    form_class = SignUpForm
    template_name = "registration/signup.html"
    success_url = reverse_lazy("login")
