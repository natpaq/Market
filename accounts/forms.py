from django import forms
from django.core.exceptions import ValidationError

class SignUpForm(forms.Form):

	def clean(self):
		cleaned_data = super(SignUpForm, self).clean()

class LoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField()
