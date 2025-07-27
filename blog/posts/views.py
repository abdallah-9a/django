from django.shortcuts import render, redirect
from .models import Post, Category, Comment
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.contrib.auth.forms import UserCreationForm
from django.core.paginator import Paginator
from .forms import CommentForm
from django.contrib.auth.models import User
# Create your views here.
def Home(request):
    categories = Category.objects.all()
    posts = Post.objects.order_by("-publish_date") # '-' sign for descending order
    paginator = Paginator(posts,5) # 5 posts per page 
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {"categories": categories, 'page_obj':page_obj}
    return render(request, "blog/home.html", context)


def CategoryDetails(request, category_id):
    category = Category.objects.get(id=category_id)
    posts = category.posts.all()

    context = {"category": category, "posts": posts}
    return render(request, "blog/category_details.html", context)


def PostDetails(request, pk):
    post = Post.objects.get(id=pk)
    comments = post.comments.all()
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect("post_details",pk = post.pk)
    context = {"post": post, "form":form}
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
    
    
def Admin(request):
    return render(request,"administration/admin.html")

def ManagePosts(request):
    posts = Post.objects.all()
    context = {"posts":posts}
    return render(request,"administration/manage_posts.html",context)

class EditPost(UpdateView):
    model = Post
    fields = ["title","category","content","tages","pic"]
    template_name = "administration/edit_post.html"
    
class DeletePost(DeleteView):
    model = Post
    template_name = "administration/delete_post.html"
    success_url = reverse_lazy("manage_posts")
    

class AddPost(CreateView):
    model=Post
    fields = "__all__"
    template_name = "administration/add_post.html"
    
    
def ManageUsers(request):
    users = User.objects.all()
    context = {"users": users}
    return render(request, "administration/manage_users.html",context)

def PromoteUser(request, user_id):
    user = User.objects.get(id = user_id)
    user.is_superuser = True
    user.save()
    return redirect("manage_users")