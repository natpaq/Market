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
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from . import forms
from chat.forms import RoomForm
import string
#from django.utils.safestring import mark_safe
#import json


def index(request):
    return render(request, 'chat/index.html', {})
@login_required
def room(request, room_name):

    if request.method == 'GET':
        form = forms.RoomForm(request.GET or None)

        if all(i in string.ascii_letters + string.digits + '-.' for i in room_name):
            return render(request, 'chat/room.html', {'room_name': room_name,
            'username': request.user.username
            })

        return redirect("index")

    
