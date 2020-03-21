from django import forms
from django.core.exceptions import ValidationError

class SignUpForm(forms.Form):
	username = forms.CharField(max_length=100, error_messages={'required': 'You must enter a username'}
	)	
	password = forms.CharField()
	def clean(self):
		cleaned_data = super(SignUpForm, self).clean()

class LoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField()
