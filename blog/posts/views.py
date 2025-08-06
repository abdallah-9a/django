from django.shortcuts import render, redirect
from .models import Post, Category, Comment, ForbiddenWords
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.contrib.auth.forms import UserCreationForm
from django.core.paginator import Paginator
from .forms import CommentForm, ForbiddensForm, CustomUserCreationForm
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.template.loader import render_to_string
from django.utils.html import strip_tags


# Create your views here.
def Home(request):
    categories = Category.objects.all()
    posts = Post.objects.order_by("-publish_date")  # '-' sign for descending order
    paginator = Paginator(posts, 5)  # 5 posts per page
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {"categories": categories, "page_obj": page_obj}
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
            return redirect("post_details", pk=post.pk)
    tags = post.tages.values_list("id", flat=True)
    similar_posts = Post.objects.filter(tages__in=tags).exclude(
        id=post.id
    )  # excluding the current post
    context = {"post": post, "form": form, "similar_posts": similar_posts}
    return render(request, "blog/post_details.html", context)


def LikePost(request, pk):
    post = Post.objects.get(id=pk)
    if request.method == "POST":
        if request.user in post.dislikes.all():
            post.dislikes.remove(request.user)
            post.likes.add(request.user)
        elif request.user in post.likes.all():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

    return redirect("post_details", pk=post.id)


def DislikePost(request, pk):
    post = Post.objects.get(id=pk)
    if request.method == "POST":
        if request.user in post.likes.all():
            post.likes.remove(request.user)
            post.dislikes.add(request.user)
        elif request.user in post.dislikes.all():
            post.dislikes.remove(request.user)
        else:
            post.dislikes.add(request.user)
    if post.dislikes.count() == 10:  # Auto Delete after 10 Dislikes
        post.delete()
        return redirect("home")
    return redirect("post_details", pk=post.id)


def Unsubsribe(request, category_id):
    category = Category.objects.get(id=category_id)

    if category.is_subscribed(request.user):
        category.subscribers.remove(request.user)
        messages.success(request, f"Successfully unsubscribed from {category.name}.")

    return redirect("home")


def Subscribe(request, category_id):
    category = Category.objects.get(id=category_id)

    # Check if user is already subscribed
    if not category.is_subscribed(request.user):
        category.subscribers.add(request.user)

        # Send confirmation email
        try:
            # Check if user has an email address
            if not request.user.email:
                messages.success(
                    request, f"Successfully subscribed to {category.name}!"
                )
                messages.warning(
                    request,
                    "No email address found. Please update your profile to receive email notifications.",
                )
                return redirect("home")

            subject = f"Subscription Confirmation - {category.name}"

            # Render HTML email template
            html_message = render_to_string(
                "emails/subscription_confirmation.html",
                {
                    "user": request.user,
                    "category": category,
                },
            )

            # Create plain text version
            plain_message = strip_tags(html_message)

            from_email = settings.DEFAULT_FROM_EMAIL
            recipient_list = [request.user.email]

            send_mail(
                subject=subject,
                message=plain_message,
                from_email=from_email,
                recipient_list=recipient_list,
                html_message=html_message,
                fail_silently=False,
            )

            messages.success(
                request,
                f"Successfully subscribed to {category.name}! A confirmation email has been sent to {request.user.email}.",
            )
        except Exception as e:
            # Still subscribe the user even if email fails
            messages.success(request, f"Successfully subscribed to {category.name}!")
            messages.warning(request, f"Email confirmation could not be sent: {str(e)}")
    else:
        messages.info(request, f"You are already subscribed to {category.name}.")

    return redirect("home")


def PostsWithTags(request, tag):
    posts = Post.objects.filter(tages__name__icontains=tag)
    context = {"posts": posts, "tag": tag}
    return render(request, "blog/posts_list.html", context)


class Signup(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "signup.html"


def Admin(request):
    return render(request, "administration/admin.html")


def ManagePosts(request):
    posts = Post.objects.all()
    context = {"posts": posts}
    return render(request, "administration/manage_posts.html", context)


class EditPost(UpdateView):
    model = Post
    fields = ["title", "category", "content", "tages", "pic"]
    template_name = "administration/edit_post.html"


class DeletePost(DeleteView):
    model = Post
    template_name = "administration/delete_post.html"
    success_url = reverse_lazy("manage_posts")


class AddPost(CreateView):
    model = Post
    fields = ["title", "category", "content", "author", "tages", "pic"]
    template_name = "administration/add_post.html"


def ManageUsers(request):
    users = User.objects.all()
    context = {"users": users}
    return render(request, "administration/manage_users.html", context)


def PromoteUser(request, user_id):
    user = User.objects.get(id=user_id)
    user.is_superuser = True
    user.save()
    return redirect("manage_users")


def ManageCategories(request):
    categories = Category.objects.all()
    context = {"categories": categories}
    return render(request, "administration/manage_categories.html", context)


class AddCategory(CreateView):
    model = Category
    fields = [
        "name",
    ]
    template_name = "administration/add_category.html"


class EditCategory(UpdateView):
    model = Category
    fields = [
        "name",
    ]
    template_name = "administration/edit_category.html"


class DeleteCategory(DeleteView):
    model = Category
    success_url = reverse_lazy("manage_categories")
    template_name = "administration/delete_category.html"


def ManageForbiddenWords(request):
    forbidden_words = ForbiddenWords.objects.all()
    form = ForbiddensForm
    if request.method == "POST":
        form = ForbiddensForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("manage_forbiddens")
    context = {"words": forbidden_words, "form": form}
    return render(request, "administration/manage_forbiddens.html", context)


def DelteForbidden(request, id):
    word = ForbiddenWords.objects.get(id=id)
    word.delete()
    return redirect("manage_forbiddens")
