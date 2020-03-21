from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from . import forms

def signup(request):
   context = {}
   if request.method == 'POST':
      form = forms.SignUpForm(request.POST)
      if form.is_valid():
            try:
               user = User.objects.create_user(form.cleaned_data['username'], password=form.cleaned_data['password'])
               return HttpResponseRedirect(reverse('login'))
            except IntegrityError:
            	form.add_error('username', 'Username already exists!')
      context['form'] = form
   return render(request, 'signup.html', context)

def do_login(request):
   context = {}
   if request.method == 'POST':
      form = forms.LoginForm(request.POST)
      if form.is_valid():
         user = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password'])
         if user is not None:
            login(request, user)
            if 'next' in request.GET:
               return HttpResponseRedirect(request.GET['next'])
            return
         else:
            form.add_error(None, 'Unable to log in')
      context['form'] = form
   return render(request, 'login.html', context)

def do_logout(request):
   logout(request)
   return HttpResponseRedirect(reverse('login'))
