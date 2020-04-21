from django import forms
from django.core.exceptions import ValidationError
from django.forms import ModelForm
from django.views.generic import CreateView
from django.core.validators import RegexValidator

class RoomForm(forms.Form):

    room_name = forms.CharField(max_length=100, error_messages={'required': 'You must enter a room'})