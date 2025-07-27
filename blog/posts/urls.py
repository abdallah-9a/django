from django.urls import path
from . import views

urlpatterns = [
    path("", views.Home, name="home"),
    path("category/<int:category_id>/", views.CategoryDetails, name="category_details"),
    path("post/<int:pk>", views.PostDetails, name="post_details"),
    path("subscribe/<int:category_id>/", views.Subscribe, name="subscribe"),
    path("unsubscribe/<int:category_id>/", views.Unsubsribe, name="unsubscribe"),
    path("signup/",views.Signup.as_view(),name='signup'),
    path("administration",views.Admin,name='admin')
    
]
