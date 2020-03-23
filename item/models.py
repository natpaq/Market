from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

class Item(models.Model):
	owner = models.ForeignKey(User, on_delete=models.CASCADE)
	image = models.FileField(upload_to='images/', null=True, verbose_name="")
	itemname = models.CharField(max_length=100)
	descrip = models.CharField(max_length=1000)
	price = models.DecimalField(max_digits=10, decimal_places=2)
	inv_count = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100000000)])
	
