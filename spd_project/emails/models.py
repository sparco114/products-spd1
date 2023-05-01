from django.db import models


class Email(models.Model):
    email_address = models.EmailField(max_length=255)
