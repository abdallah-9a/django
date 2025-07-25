from django.urls import path
from . import views

urlpatterns = [
    path("", views.Home, name="home"),
    path("category/<int:category_id>/", views.CategoryDetails, name="category_details"),
    path("post/<int:pk>", views.PostDetails, name="post_details"),
]
