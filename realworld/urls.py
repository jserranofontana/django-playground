from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path("", TemplateView.as_view(template_name="realworld/index.html"), name="home"),
    path("accounts/", include(("realworld.accounts.urls"))),
]
