from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from . import forms
from django.shortcuts import get_list_or_404, get_object_or_404
from django.contrib import messages

from item.forms import OrderItemForm
from item.models import Item, OrderItem, Order
from item.views import add_to_cart, remove_from_cart, my_cart, payment


def index(request):
    items1 = Item.objects.all()
    context = {'items': items1}
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = OrderItemForm(request.POST)
            if form.is_valid():
                order_item = OrderItem.objects.create(form.cleaned_data['item'], form.cleaned_data['quantity'])
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
                form.add_error('password', 'Username and password combination is invalid!')
        context['form'] = form
    return render(request, 'login.html', context)


def do_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def item_update(request, id):
    post = get_object_or_404(Item, id=id)
    if request.method == "POST":
        form = forms.AddItemForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return HttpResponseRedirect(reverse('my_items'))
    else:
        form = forms.AddItemForm(instance=post)
    context = {'form': form}
    context['item'] = post
    return render(request, "edit_item.html", context)


def item_delete(request, id):
    post = get_object_or_404(Item, id=id)
    post.delete()
    messages.info(request, "This item has been deleted!")
    return redirect(reverse("index"))
