from django.shortcuts import render
from .models import Post, Category


# Create your views here.
def Home(request):
    categories = Category.objects.all()
    context = {"categories": categories}
    return render(request, "blog/home.html", context)
