from django.contrib import admin
from .models import Product, ProductCategory

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'product_name',
        'product_category',
        'product_price',
        'product_image',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductCategory)
