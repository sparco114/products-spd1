import django.utils.timezone
from django.db import models
from django.contrib.auth.models import User

from emails.models import Email
from products.models import Product


class SalesOrder(models.Model):
    amount = models.IntegerField()
    description = models.CharField(max_length=255)
    price = models.IntegerField(null=True)
    date = models.DateField(default=django.utils.timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    products = models.ManyToManyField(Product)
    email = models.OneToOneField(Email, null=True, on_delete=models.SET_NULL)

