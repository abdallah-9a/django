from django.urls import path
from . import views
from django.contrib.auth import views as auth_views  # Take fully control
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path("login", views.Login, name="login"), previous url
    path("home",views.Home, name='home'),
    # Login\Logout urls
    path("login", auth_views.LoginView.as_view(), name="login"),
    path("logout", auth_views.LogoutView.as_view(), name="logout"),
    # Change Password urls
    path("password-change", auth_views.PasswordChangeView.as_view(),name = "password_change"),
    path("password-change/done", auth_views.PasswordChangeDoneView.as_view(),name = "password_change_done"),
    # Reset Password urls
    path("password-reset", auth_views.PasswordResetView.as_view(), name= "password_reset"),
    path("password-reset/done", auth_views.PasswordResetDoneView.as_view(), name = "password_reset_done"),
    path("password-reset/<uidb64>/<token>", auth_views.PasswordResetConfirmView.as_view(), name = "password_reset_confirm"),
    path("password-reset/complete", auth_views.PasswordResetCompleteView.as_view(), name= "password_reset_complete"),
    # SignUp
    path("signup", views.SignUp, name="signup"),
    path("edit", views.Edit, name="edit_user")
]


if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)