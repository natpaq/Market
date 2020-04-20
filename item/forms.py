from django.forms import ModelForm
from django.views.generic import CreateView
from .models import Item, OrderItem, Address
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

class CheckoutForm(forms.Form):
	street_address = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'ex. Address Lane',
																				   'class':'form-control'}))
	city = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'ex. London', 'class':'form-control'}))
	state = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'ex. Ontario', 'class':'form-control'}))
	zip = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'ex. Q6R 2I9', 'class':'form-control'}))

	def clean(self):
		cleaned_data = super(CheckoutForm, self).clean()
