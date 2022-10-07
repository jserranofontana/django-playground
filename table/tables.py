# table/tables.py
import django_tables2 as tables
from table.models import Product


class ProductHTMxTable(tables.Table):
    class Meta:
        model = Product
        template_name = "table/components/bootstrap_htmx.html"
