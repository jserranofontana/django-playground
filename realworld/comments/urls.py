from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path(
        "",
        TemplateView.as_view(template_name="realworld/comments.html"),
        name="comments",
    ),
    path(
        "add/<int:article_id>/",
        views.add_comment,
        name="add_comment",
    ),
    path(
        "edit/<int:comment_id>/",
        views.edit_comment,
        name="edit_comment",
    ),
    path(
        "delete/<int:comment_id>/",
        views.delete_comment,
        name="delete_comment",
    ),
]
