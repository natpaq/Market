from django.forms import ModelForm
from django.views.generic import CreateView
from .models import Item, OrderItem
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django import forms

class AddItemForm(ModelForm):
	class Meta:
		model = Item
		fields = ["image", "itemname", "descrip", "price", "inv_count",]
	def clean(self):
		cleaned_data = super(AddItemForm, self).clean()

class OrderItemForm(ModelForm):
	class Meta:
		model = OrderItem
		fields = ["item", "quantity",]

	def clean(self):
		cleaned_data = super(OrderItemForm, self).clean()
