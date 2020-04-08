from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.conf import settings
from django.shortcuts import reverse


class Item(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    itemname = models.CharField(max_length=100)
    descrip = models.CharField(max_length=1000)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inv_count = models.PositiveIntegerField()

    def get_add_to_cart_url(self):
        return reverse("add_to_cart", kwargs={'id': self.id})

    def get_remove_from_cart_url(self):
        return reverse("remove_from_cart", kwargs={'id': self.id})


def __str__(self):
    return self.owner + self.image + self.itemname + self.descrip + self.price + self.inv_count


class OrderItem(models.Model):
    item = models.OneToOneField(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.quantity} of {self.item.itemname}"

    def get_total_item_price(self):
        return self.quantity * self.item.price

class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    items = models.ManyToManyField(OrderItem)
    ordered_date = models.DateTimeField()
    address = models.ForeignKey('Address', on_delete=models.SET_NULL, blank=True, null=True)
    payment = models.ForeignKey('Payment', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.user.username

    def get_total(self):
        total = 0
        for order_item in self.items.all():
            total += order_item.get_total_item_price()
        return total

class Address(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    street_address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip = models.CharField(max_length=100)
    #contact = models.CharField(max_length=100)

    def __str__(self):
        return self.city

class Payment(models.Model):
    stripe_charge_id = models.CharField(max_length=50)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True)
    amount = models.FloatField()
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username + self.amount


