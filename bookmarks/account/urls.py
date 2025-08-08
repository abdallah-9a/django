from django.urls import path
from . import views
from django.contrib.auth import views as auth_views  # Take fully control

urlpatterns = [
    # path("login", views.Login, name="login"), previous url
    path("login", auth_views.LoginView.as_view(), name="login"),
    path("logout", auth_views.LogoutView.as_view(), name="logout"),
    path("password-change", auth_views.PasswordChangeView.as_view(),name = "password_change"),
    path("password-change/done", auth_views.PasswordChangeDoneView.as_view(),name = "password_change_done"),
    path("home",views.Home, name='home'),
]
