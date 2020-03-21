from django.shortcuts import render
from django.db import IntegrityError
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from . import forms

def signup(request):
   if request.method == 'POST':
      form = UserCreationForm(request.POST)
      if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('home')
   else:
      form = UserCreationForm()
   return render(request, 'signup.html', {'form' : form})

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
