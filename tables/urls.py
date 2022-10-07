from django.urls import path, include
from tables.views import (
    ProductTableView,
    ProductHTMxTableView,
    ProductHTMxInfiniteTableView,
    ProductHTMxMultiColumTableView,
)

urlpatterns = [
    path("original/", ProductTableView.as_view(), name="products"),
    path("htmx/", ProductHTMxTableView.as_view(), name="products_htmx"),
    path(
        "multi-col-htmx/",
        ProductHTMxMultiColumTableView.as_view(),
        name="products_htmx_multicol",
    ),
    path(
        "infinite/",
        ProductHTMxInfiniteTableView.as_view(),
        name="products_htmx_infinite",
    ),
]
