from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Item

from . import forms

# user must be logged in to be able to access view
# @login_required
def add_item(request):
	context = {}
	if request.method == 'POST':
	   form = forms.AddItemForm(request.POST, request.FILES)
	   if form.is_valid():
	      item = form.save(commit=False)
	      item.owner = request.user
	      item.save()
	      return HttpResponseRedirect(reverse('index')) 	
	   context['form'] = form
	return render(request, 'list_item.html', context)
