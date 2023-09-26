from django.contrib import admin

from products.models import Product, ProductCategory, ProductPrice


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(ProductPrice)
class ProductCategoryAdmin(admin.ModelAdmin):
    pass
