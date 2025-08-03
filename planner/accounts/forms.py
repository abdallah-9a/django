from django import forms
from accounts.models import CustomUser
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ["username", "email", "password1", "password2"]
