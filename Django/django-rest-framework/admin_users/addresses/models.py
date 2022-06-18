from django.db import models

# Create your models here.


class Address(models.Model):
    street: models.CharField(max_length=255)
    nro: models.IntegerField()
    city: models.CharField(max_length=255)
