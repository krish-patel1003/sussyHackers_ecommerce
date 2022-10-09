from dataclasses import fields
import django_filters

from .models import Product

class ProductFilter(django_filters.FilterSet):
    # product_category__name = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Product
        fields = ['product_name', 'product_brand', 'product_category']
    