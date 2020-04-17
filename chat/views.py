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

from django.shortcuts import render, redirect
from . import forms
from chat.forms import RoomForm


def index(request):
    return render(request, 'chat/index.html', {})

def room(request, room_name):
    #form = RoomForm()
    #context = {}
    if request.method == 'GET':
        form = forms.RoomForm(request.GET or None)
        #if not form.fields[room_name]:
        #if room_name is None:
        if form.is_valid():
            #form.save()
        #if not context['room_name']:
    #return render(request, 'chat/index.html', {'form': form})
            return render(request, 'chat/room.html', {'room_name': room_name})
        # else:
        #   return redirect("index")
        #    return render(request, 'chat/index.html', {})
    else:
        return redirect("index")
        #return render(request, 'chat/index.html', {})
    #return render(request, 'chat/room.html', {'room_name': room_name})
    


# def index(request):
#     return render(request, 'chat/index.html', {})

# def room(request, room_name=None):
#     if request.method == 'POST':
#         form = forms.RoomForm(request.POST)
#         if form.is_valid():
#             if not room:
#                 form.save
#                 return render(request, 'chat/room.html', {
#                     'room_name': room_name
#                 })
#     else:
#         form = RoomForm()
#         return render(request, 'chat/index.html', {'form': form})  