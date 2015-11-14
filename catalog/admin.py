from django.contrib import admin
from products.models import Catalog, Product, CatalogCategory, ProductDetail, ProductAttribute


admin.site.register(Catalog)
admin.site.register(Product)
admin.site.register(CatalogCategory)
admin.site.register(ProductDetail)
admin.site.register(ProductAttribute)
