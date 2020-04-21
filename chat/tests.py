from django.test import TestCase, Client, SimpleTestCase
from views.py import index, room
from django.urls import reverse, resolve
# Create your tests here.
    
from channels.testing import WebsocketCommunicator
#import pytest

from chat.routing import application

#Test url routing
class TestUrls(SimpleTestCase):

##index
    def test_main(self):
        url = reverse('')
        self.assertEquals(resolve(url).func, main_chat)

class TestViews(TestCase):
##room
    def test_room(self):
        user = Client()
        #request or request.GET?
        url = render(request.GET, 'chat/room.html', {'room_name': 'test',
            'username': 'bob'
            })
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'room.html')

    def test_msg(self):
        response = HttpResponse()
        response["TestCustomHeader"] = "WebSocket CONNECT"
        self.assertEquals(response, response["TestCustomHeader"])
        

##login authen correct redirect
#Should class testURL =testInput

#test input field 
class TestInput(TestCase):

##invalid input -> index

##valid input -> proper room

#Test Websocket 
# class TestMWS(TestCase):

#Test 
# class TestMWS(TestCase):

# #Test room messages 
#class TestMsg(TestCase):
# ##test messages are viewable by everyone in the same room
#     def same_room(self):


# ##test if you are in a different room that you don't see 1's messages
#     def diff_room(self):
