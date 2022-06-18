from django.db import models

from admin_users.addresses.models import Address

# Create your models here.


class User(models.Model):
    dni = models.IntegerField()
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    email = models.EmailField()
    address = models.ForeignKey(
        Address, blank=True, on_delete=models.CASCADE, null=True)
