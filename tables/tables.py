import django_tables2 as tables

from tables.models import Product


class ProductTable(tables.Table):
    class Meta:
        model = Product
        template_name = "django_tables2/bootstrap4.html"


class ProductHTMxTable(tables.Table):
    class Meta:
        model = Product
        template_name = "tables/components/bootstrap_htmx_full.html"


class ProductHTMxInfiniteTable(tables.Table):
    class Meta:
        model = Product
        template_name = "tables/components/bootstrap_htmx_infinite.html"


class ProductHTMxMultiColumnTable(tables.Table):
    class Meta:
        model = Product
        show_header = False
        template_name = "tables/components/bootstrap_col_filter.html"
