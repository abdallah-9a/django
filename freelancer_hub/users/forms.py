from django import forms 
from .models import Profile
from django.contrib.auth.forms import UserCreationForm
class SignUpForm(UserCreationForm):
    class Meta:
        model = Profile
        fields = ["first_name","last_name",
                      "username","email","password1","password2"]
    
    