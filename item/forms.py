from django.forms import ModelForm
from django.views.generic import CreateView
from .models import Item
from django.core.exceptions import ValidationError

class AddItemForm(ModelForm):
	class Meta:
		model = Item
		fields = ["image", "itemname", "descrip", "price", "inv_count",]
	def clean(self):
		cleaned_data = super(AddItemForm, self).clean()
