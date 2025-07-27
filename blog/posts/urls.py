from django.urls import path
from . import views

urlpatterns = [
    path("", views.Home, name="home"),
    path("category/<int:category_id>/", views.CategoryDetails, name="category_details"),
    path("post/<int:pk>", views.PostDetails, name="post_details"),
    path("subscribe/<int:category_id>/", views.Subscribe, name="subscribe"),
    path("unsubscribe/<int:category_id>/", views.Unsubsribe, name="unsubscribe"),
    path("signup/",views.Signup.as_view(),name='signup'),
    path("manage",views.Admin,name='admin'),
    path("manage/posts",views.ManagePosts,name='manage_posts'),
    path("manage/post/edit/<int:pk>",views.EditPost.as_view(),name='edit_post'),
    path("manage/post/delete/<int:pk>",views.DeletePost.as_view(),name='delete_post'),
    path("manage/post/add",views.AddPost.as_view(),name='add_post'),
    
]
