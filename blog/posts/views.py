from django.shortcuts import render
from .models import Post, Category


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
