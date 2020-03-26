from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Item
from django.db.models import When, Case

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

def add_to_cart(request):
	if request.method == 'POST':
	   form = CartItemForm(request.POST)
	   if form.is_valid():
	      cart = Cart.add(item=form.cleaned_data['item'], quantity=form.cleaned_data['quantity'])
	      data = {"status": "success", "total": cart.total, "count": cart.count }
	      return HttpResponseRedirect(reverse('index'))
	return render(request, 'index_l.html', context)
#user items
def my_items(request):
	# want to only display user's objects -- need to fix
	items1 = Item.objects.all()
	#items1 = Item.objects.filter(owner=Case(
	#When request.user = Item.owner))
	context = {'items': items1}
	return render(request, 'my_items.html', context)


