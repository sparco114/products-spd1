import django.utils.timezone
from django.db import models


class SalesOrder(models.Model):
    amount = models.IntegerField()
    description = models.CharField(max_length=255)
    price = models.IntegerField(default=0)
    date = models.DateField(default=django.utils.timezone.now)
