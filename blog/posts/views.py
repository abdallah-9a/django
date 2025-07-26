from django.shortcuts import render, redirect
from .models import Post, Category
from django.views.generic import CreateView
from django.urls import reverse_lazy, reverse
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def Home(request):
    categories = Category.objects.all()
    context = {"categories": categories}
    return render(request, "blog/home.html", context)


def CategoryDetails(request, category_id):
    category = Category.objects.get(id=category_id)
    posts = category.posts.all()

    context = {"category": category, "posts": posts}
    return render(request, "blog/category_details.html", context)


def PostDetails(request, pk):
    post = Post.objects.get(id=pk)
    context = {"post": post}
    return render(request, "blog/post_details.html", context)


def Unsubsribe(request, category_id):
    category = Category.objects.get(id=category_id)
    category.subscribers.remove(request.user)
    return redirect("home")


def Subscribe(request, category_id):
    category = Category.objects.get(id=category_id)
    category.subscribers.add(request.user)
    return redirect("home")

class Signup(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "signup.html"