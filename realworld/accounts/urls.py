from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path(
        "",
        TemplateView.as_view(template_name="realworld/accounts.html"),
        name="accounts",
    ),
    path("register/", views.register, name="register"),
    path(
        "login/",
        LoginView.as_view(template_name="realworld/registration/login.html"),
        name="login",
    ),
    path("logout/", LogoutView.as_view(next_page="/realworld/"), name="logout"),
    path("settings/", views.settings, name="settings"),
    path("check-email/", views.check_email, name="check_email"),
    path("profile/<int:user_id>/", views.profile, name="profile"),
    path("profile/follow/<int:user_id>/", views.follow, name="follow"),
]
