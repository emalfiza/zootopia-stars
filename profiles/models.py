from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_street_address_1 = models.CharField(max_length=60, blank=False)
    user_street_address_2 = models.CharField(max_length=60, blank=False)
    user_city = models.CharField(max_length=40, blank=False)
    user_county = models.CharField(max_length=40, blank=False)
    user_country = models.CharField(max_length=40, blank=False)
    user_postcode = models.CharField(max_length=20, blank=False)
    user_phone_number = models.CharField(max_length=20, blank=False)

    def __str__(self):
        return self.user.username
