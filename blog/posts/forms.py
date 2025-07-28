from django import forms 
from .models import Post, Comment, ForbiddenWords


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content',]

class ForbiddensForm(forms.ModelForm):
    class Meta:
        model = ForbiddenWords
        fields =["word",]