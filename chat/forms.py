from django import forms
from django.core.exceptions import ValidationError
from django.forms import ModelForm
from django.views.generic import CreateView
from django.core.validators import RegexValidator
alphanumeric = RegexValidator(r'^[0-9a-zA-Z\-.]*$', 'Only alphanumeric characters are allowed.')
class RoomForm(forms.Form):

    room_name = forms.CharField(max_length=100, validators=[alphanumeric], error_messages={'required': 'You must enter a room'})

    #fields = ['room']
    # def clean(self):
    # #    cleaned_data = super(RoomForm, self).clean()
    #     cleaned_data = self.cleaned_data.get('room_name')
    #     return cleaned_data

        # if not is_valid(cleaned_data):
        #     raise forms.ValidationError('room required')
        # return cleaned_data