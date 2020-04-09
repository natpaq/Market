from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Item, OrderItem, Order
from django.db.models import When, Case
from django.utils import timezone
from django.contrib import messages
from . import forms


def add_item(request):
	context = {}
	if request.method == 'POST':
	   form = forms.AddItemForm(request.POST, request.FILES)
	   if form.is_valid():
	      item = form.save(commit=False)
	      item.owner = request.user
	      item.save()
	      return HttpResponseRedirect(reverse('my_items')) 	
	   context['form'] = form
	return render(request, 'list_item.html', context)

def my_items(request):
	items1 = Item.objects.all()
	context = {'items': items1}
	return render(request, 'my_items.html', context)

def my_cart(request):
        orderitems = OrderItem.objects.all()
        # do not throw an error if cart is empty
        try:
           order = Order.objects.get(user=request.user)
           context = {'orderitems' : orderitems, 'order' : order}
        except Order.DoesNotExist:
           context = {}
        return render(request, 'view_cart.html', context)


def add_to_cart(request, id):
	item = get_object_or_404(Item, id=id)
	order_item, created = OrderItem.objects.get_or_create(item=item, user=request.user, ordered=False)
	order_inital = Order.objects.filter(user=request.user, ordered=False)
	if order_inital.exists():
		order = order_inital[0]
		if order.items.filter(item__id=item.id).exists():
			order_item.quantity += 1
			order_item.save()
			messages.info(request, "This item has been updated in your cart!")
			return redirect(reverse('my_cart'))
		else:
			order.items.add(order_item)
			messages.info(request, "This item has been added to your cart!")
			return redirect(reverse('my_cart'))
	else:
		date = timezone.now()
		order = Order.objects.create(user=request.user, ordered_date=date)
		order.items.add(order_item)
		messages.info(request, "This item has been added to your cart!")
		return redirect(reverse('my_cart'))

def remove_from_cart(request, id):
	item = get_object_or_404(Item, id=id)
	order_inital = Order.objects.filter(user=request.user, ordered=False)
	if order_inital.exists():
		order = order_inital[0]
		if order.items.filter(item__id=item.id).exists():
			order_item = OrderItem.objects.filter(item=item, user=request.user, ordered=False)[0]
			if order_item.quantity > 1:
				order_item.quantity -= 1
				order_item.save()
			else:
				order.items.remove(order_item)
				order_item.delete()
			messages.info(request, "This item has been removed from your cart!")
			return redirect(reverse('my_cart'))
		else:
			messages.info(request, "This item was not in your cart!")
			return redirect(reverse('my_cart'))
	else:
		messages.info(request, "You do not have an active order!")
		return redirect(reverse('my_cart'))

#Work ON REWORKING!!!!!!!!!!!!!!!!!!!!!!!!!
def delete_from_cart(request, id):
	item = get_object_or_404(Item, id=id)
	order = Order.objects.filter(user=request.user, ordered=False)[0]
	order_item = OrderItem.objects.filter(item=item, user=request.user, ordered=False)[0]
	order.items.remove(order_item)
	order_item.delete()
	messages.info(request, "This item was removed from your cart.")
	return redirect(reverse('my_cart'))

def checkout(request):
	orderitems = OrderItem.objects.all()
        # do not throw an error if cart is empty
	try:
           order = Order.objects.get(user=request.user)
           context = {'orderitems' : orderitems, 'order' : order}
	except Order.DoesNotExist:
           context = {}
	return render(request, 'checkout.html', context)



