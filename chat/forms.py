from django import forms
from django.core.exceptions import ValidationError
from django.forms import ModelForm
from django.views.generic import CreateView

class RoomForm(forms.Form):
    room = forms.CharField(max_length=100, error_messages={'required': 'You mustt enter a room'})
    #
    #fields = ['room']
    def clean(self):
        # cleaned_data = super(RoomForm, self).clean()
        cleaned_data = self.cleaned_data.get('room_name')

        # if not is_valid(cleaned_data):
        #     raise forms.ValidationError('room required')
        # return cleaned_data