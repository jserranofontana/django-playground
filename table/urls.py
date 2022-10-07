from django.urls import path, include

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("product_htmx", views.ProductHTMxTableView.as_view(), name="product_htmx"),
]
