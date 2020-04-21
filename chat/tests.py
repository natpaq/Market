import unittest
from django.test import SimpleTestCase
from chat.views import main_chat, room
from django.urls import reverse, resolve

# Create your tests here.

#Test url routing
#class ChatUrls(SimpleTestCase):

##index
#     def test_main(self):
#         this_url = reverse('main_chat')
#         self.assertEquals(resolve(this_url).func, main_chat)

# class ChatViews(unittest.TestCase):
# ##room
#     @classmethod
#     def setUp(self):
#         c = Client()
#         url = reverse('room')
    
#     def get_request(self):
#         c = Client()
#         r = c.get(url, {'room_name': 'test', 'username': 'bob' })
#         self.assertEquals(r.status_code, 200)
#         self.assertTemplateUsed(r, 'room.html')


#test input field 

##invalid input -> index

##valid input -> proper room

#Test Websocket 
#REMOVE THIS CLASS bC PYTEST AND IMPORT USAGE  
# class WSTest(TestCase):
# @pytest.mark.asyncio
#     async def ConsConn():
#         con = WebsocketCommunicator(application, '/ws/chat/this/')
#         connected, subprotocol = await con.connect()
#         assert connected
#         await con.disconnect()
#Test 
# #Test room messages 
#class MsgTest(TestCase):
# ##test messages are viewable by everyone in the same room
#     def same_room(self):


# ##test if you are in a different room that you don't see 1's messages
#     def diff_room(self):
