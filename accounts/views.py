from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from . import forms
from item.models import Item
from django.shortcuts import get_list_or_404, get_object_or_404

from item.forms import OrderItemForm
from item.models import Item, OrderItem, Order

def index(request):
   items1 = Item.objects.all()
   context = {'items': items1}
   if request.user.is_authenticated:
      if request.method == 'POST':
         form = OrderItemForm(request.POST)
         if form.is_valid():
            #order_item = form.save()
            order_item = OrderItem.objects.create(form.cleaned_data['item'], form.cleaned_data['quantity'])
            #order_item.save()
            return HttpResponseRedirect(reverse('index'))
      return render(request, 'index_l.html', context)
   return render(request, 'index.html', context)


def signup(request):
    context = {}
    if request.method == 'POST':
        form = forms.SignUpForm(request.POST)
        if form.is_valid():
            try:
                # password hashing is taken care of
                user = User.objects.create_user(form.cleaned_data['username'], password=form.cleaned_data['password'])
                return HttpResponseRedirect(reverse('login'))
            # display error in form
            except IntegrityError:
                form.add_error('username', 'Username already exists!')
        # display form again
        context['form'] = form
    return render(request, 'signup.html', context)


def do_login(request):
    context = {}
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                # stores session of logged in user
                login(request, user)
                if 'next' in request.GET:
                    return HttpResponseRedirect(request.GET['next'])
                return HttpResponseRedirect(reverse('index'))
            else:
                form.add_error(None, 'Unable to log in')
        context['form'] = form
    return render(request, 'login.html', context)


def do_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def item_update(request, id):
    post = get_object_or_404(Item, id=id)
    if request.method == "POST":
        form = forms.AddItemForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return HttpResponseRedirect(reverse('my_items'))
    else:
        form = forms.AddItemForm(instance=post)
    context = {'form': form}
    return render(request, "list_item.html", context)

