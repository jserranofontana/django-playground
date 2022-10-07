from django.http import HttpRequest
from django.shortcuts import render

from django_tables2 import SingleTableMixin
from django_filters.views import FilterView

from table.models import Product
from table.tables import ProductHTMxTable
from table.filters import ProductFilter


def index(request: HttpRequest):
    return render(request, "table/index.html", {})


class ProductHTMxTableView(SingleTableMixin, FilterView):
    table_class = ProductHTMxTable
    queryset = Product.objects.all()
    filterset_class = ProductFilter
    paginate_by = 15

    def get_template_names(self):
        if self.request.htmx:
            template_name = "table/partials/_product_table_partial.html"
        else:
            template_name = "table/product_table_htmx.html"

        return template_name
