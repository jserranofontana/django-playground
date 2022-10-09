from django.urls import path, include
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path("", TemplateView.as_view(template_name="realworld/index.html"), name="home"),
]
