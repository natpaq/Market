from django.forms import ModelForm
from .models import Item
from django.core.exceptions import ValidationError

class AddItemForm(ModelForm):
	class Meta:
		model = Item
		fields = ["owner", "image", "itemname", "descrip", "price", "inv_count"]
