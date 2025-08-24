from django import forms
from .models import Project
from django.utils.timezone import now

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ["title","description","category","skills","budget","deadline"]
    
    def clean_deadline(self):
        deadline = self.cleaned_data["deadline"]
        if deadline < now().date():
            raise forms.ValidationError("Deadline Can not be before today")
        
        return deadline
    