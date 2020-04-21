from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from . import forms
from chat.forms import RoomForm
import string
#from django.utils.safestring import mark_safe
#import json


def main_chat(request):
    return render(request, 'chat/index.html', {})

@login_required
def room(request, room_name):

    if request.method == 'GET':
        form = forms.RoomForm(request.GET or None)

        if not room_name:
            return redirect('main_chat')

        if all(i in string.ascii_letters + string.digits + '-.' for i in room_name):
            return render(request, 'chat/room.html', {'room_name': room_name,
            'username': request.user.username
            })

        return redirect('main_chat')

    
