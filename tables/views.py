from django.core.paginator import Paginator, EmptyPage

from django_tables2 import SingleTableView, SingleTableMixin
from django_filters.views import FilterView

from tables.models import Product
from tables.tables import (
    ProductTable,
    ProductHTMxTable,
    ProductHTMxInfiniteTable,
    ProductHTMxMultiColumnTable,
)
from tables.filters import ProductFilter, ProductUniversalFilter


class ProductTableView(SingleTableView):
    table_class = ProductTable
    queryset = Product.objects.all()
    template_name = "tables/product_table.html"
    paginate_by = 10


class ProductHTMxTableView(SingleTableMixin, FilterView):
    table_class = ProductHTMxTable
    queryset = Product.objects.all()
    filterset_class = ProductUniversalFilter
    paginate_by = 10

    def get_template_names(self):
        if self.request.htmx:
            template_name = "tables/partials/_product_table_partial.html"
        else:
            template_name = "tables/product_table_htmx.html"

        return template_name


class ProductHTMxInfiniteTableView(SingleTableMixin, FilterView):
    table_class = ProductHTMxInfiniteTable
    queryset = Product.objects.all()
    filterset_class = ProductUniversalFilter
    paginate_by = 10

    def get_template_names(self):
        if self.request.htmx:
            if "lazy" in self.request.GET:
                # Render only rows
                template_name = "tables/components/bootstrap_htmx_rows.html"
            else:
                # Render Full table
                template_name = "tables/partials/_product_table_partial.html"
        else:
            # Render full page
            template_name = "tables/product_table_htmx_infinite.html"

        return template_name


class CustomPaginator(Paginator):
    def validate_number(self, number):
        try:
            return super().validate_number(number)
        except EmptyPage:
            if int(number) > 1:
                # return the last page
                return self.num_pages
            elif int(number) < 1:
                # return the first page
                return 1
            else:
                raise


class ProductHTMxMultiColumTableView(SingleTableMixin, FilterView):
    table_class = ProductHTMxMultiColumnTable
    queryset = Product.objects.all()
    filterset_class = ProductFilter
    paginate_by = 10
    paginator_class = CustomPaginator

    def get_template_names(self):
        if self.request.htmx:
            template_name = "tables/partials/_product_table_partial.html"
        else:
            template_name = "tables/product_table_col_filter.html"

        return template_name
