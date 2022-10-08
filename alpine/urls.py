from django.urls import path, include
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path("", TemplateView.as_view(template_name="alpine/v1.html"), name="home"),
    path("people/", views.people, name="people"),
    path("filter/", views.index, name="filter"),
    path("filter/bands/", views.bands, name="bands"),
]
