from django.db import models
from profiles.models import Customer
from store.models import Product

# Create your models here.


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False, null=True, blank=False)
    transaction_id = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.id)


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.quantity}-{self.product}'


class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)
    order_full_name = models.CharField(max_length=50, null=False, blank=False)
    order_email = models.EmailField(max_length=254, null=False, blank=False, default='')
    order_phone_number = models.CharField(max_length=15, null=False, blank=False)
    order_street_address_1 = models.CharField(max_length=60, blank=False)
    order_street_address_2 = models.CharField(max_length=60, blank=False)
    order_city = models.CharField(max_length=40, blank=False)
    order_county = models.CharField(max_length=40, blank=False)
    order_country = models.CharField(max_length=40, blank=False)
    order_postcode = models.CharField(max_length=10, blank=False)

    def __str__(self):
        return f'{self.order_full_name}-{self.order_postcode}'