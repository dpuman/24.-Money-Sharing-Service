from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Customer(models.Model):
    name = models.OneToOneField(User, on_delete=models.CASCADE)
    date_registered = models.DateTimeField(
        auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.name.username


class Account(models.Model):
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE)
    balance = models.FloatField(null=True, blank=True)
    date_opened = models.DateTimeField(
        auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.customer.name


class Transection(models.Model):
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    amount = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.customer.name
