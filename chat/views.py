# from django.contrib.auth.decorators import login_required
# from django.shortcuts import render
# from django.utils.safestring import mark_safe
# import json

# def index(request):
#     return render(request, 'chat/index.html', {})

# @login_required
# def room(request, room_name):
#     return render(request, 'chat/room.html', {
#         'room_name_json': mark_safe(json.dumps(room_name)),
#         'username': mark_safe(json.dumps(request.user.username)),
#     })

#from django.shortcuts import render
#from .forms import RoomForm

#def index(request):
#    return render(request, 'chat/index.html', {})

#def room(request, room_name=None):
#    return render(request, 'chat/room.html', {
#        'room_name': room_name
#    })
from django.shortcuts import render, redirect
from . import forms
from chat.forms import RoomForm
import string


def index(request):
    return render(request, 'chat/index.html', {})

def room(request, room_name):
    #form = RoomForm()
    #context = {}
    if request.method == 'GET':
        form = forms.RoomForm(request.GET or None)
        #if not form.fields[room_name]:
        # print(room_name)
        # print(form.is_valid())
        # print(form)
        # print(form.errors)
        # print(request.GET)
        #if not room_name:
        #if form.is_valid():
            #form.save()
            #if not context['room_name']:
         #return render(request, 'chat/index.html', {'form': form})
            #print(room_name)
        # bool i_val = False
        # i in string.ascii_letters + string.digits + '-.' for i in room_name:
        #     i_val = True
        #if form.is_valid() and room_name != ' ':
        if room_name != ' ':
            return render(request, 'chat/room.html', {'room_name': room_name})
        # else:
        #   return redirect("index")
        #    return render(request, 'chat/index.html', {})
        else:
            #print(form.errors)
            return redirect("index")
        #return render(request, 'chat/index.html', {})
    return render(request, 'chat/room.html', {'room_name': room_name})
    
