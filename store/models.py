from django.db import models

# Create your models here.


class ProductCategory(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    category_name = models.TextField(max_length=50)

    def __str__(self):
        return self.category_name


class Product(models.Model):

    class Meta:
        verbose_name_plural = 'Products'

    product_category = models.ForeignKey('ProductCategory', null=True, blank=True, on_delete=models.SET_NULL)
    product_name = models.CharField(max_length=100)
    product_price = models.DecimalField(max_digits=6, decimal_places=2)
    product_description = models.TextField(max_length=300)
    product_image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.product_name
