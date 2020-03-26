from django import forms
from django.core.exceptions import ValidationError
from django.forms import ModelForm
from django.views.generic import CreateView
from item.models import Item

class SignUpForm(forms.Form):
	username = forms.CharField(max_length=100, error_messages={'required': 'You must enter a username'}
	)	
	password = forms.CharField()
	def clean(self):
		cleaned_data = super(SignUpForm, self).clean()

class LoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField()


class AddItemForm(ModelForm):
	class Meta:
		model = Item
		fields = ["image", "itemname", "descrip", "price", "inv_count",]
	def clean(self):
		cleaned_data = super(AddItemForm, self).clean()
