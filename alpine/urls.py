from django.urls import path, include
from django.views.generic import TemplateView

from . import views
from .api import api

urlpatterns = [
    path("", TemplateView.as_view(template_name="alpine/v1.html"), name="home"),
    path("people/", views.people, name="people"),
    path("filter/", views.index, name="filter"),
    path("filter/bands/", views.bands, name="bands"),
    path("filter/api/", api.urls),
    path("accordion/", views.courses, name="accordion"),
    path("accordion/modules/", views.modules, name="modules"),
    path("accordion/university/", views.university, name="university"),
    path("accordion/university/course-list", views.course_list, name="course_list"),
]
