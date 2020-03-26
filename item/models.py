from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class Item(models.Model):
	owner = models.ForeignKey(User, on_delete=models.CASCADE)
	image = models.ImageField(upload_to='images/')
	itemname = models.CharField(max_length=100)
	descrip = models.CharField(max_length=1000)
	price = models.DecimalField(max_digits=10, decimal_places=2)
	inv_count = models.PositiveIntegerField()

def __str__(self):
        return self.owner + self.image + self.itemname + self.descrip + self.price + self.inv_count
	

class OrderItem(models.Model):
	item = models.OneToOneField(Item, on_delete=models.CASCADE)
	quantity = models.PositiveIntegerField(default=0)
	
	def __str__(self):
		return self.item 
	

