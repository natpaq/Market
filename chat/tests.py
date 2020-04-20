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
    def test_index(self):
        url = reverse('')
        self.assertEquals(resolve(url).func, index)

##room
    def test_room(self):
        user = self.user
        #request or request.GET?
        url = render(request.GET, 'chat/room.html', {'room_name': 'test',
            'username': 'bob'
            })
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'room.html')
#Should class testURL =testInput

#test input field 
class TestInput(TestCase):

##invalid input -> index

##valid input -> proper room

#Test Websocket 
class TestMsg(TestCase):
@pytest.mark.asyncio
    async def test_chat_consumer_connection():
        communicator = WebsocketCommunicator(application, '/ws/chat/test/')
        connected, subprotocol = await communicator.connect()
        assert connected
        await communicator.disconnect()

#Test room messages 
class TestMsg(TestCase):
##test messages are viewable by everyone in the same room
    def same_room(self):
        try:
            self._enter_chat_room('room_1')

            self._open_new_window()
            self._enter_chat_room('room_1')

            self._switch_to_window(0)
            self._post_message('hello')
            WebDriverWait(self.driver, 2).until(lambda _:
                'hello' in self._chat_log_value,
                'Message was not received by window 1 from window 1')
            self._switch_to_window(1)
            WebDriverWait(self.driver, 2).until(lambda _:
                'hello' in self._chat_log_value,
                'Message was not received by window 2 from window 1')
        finally:
            self._close_all_new_windows()

##test if you are in a different room that you don't see 1's messages
    def diff_room(self):
        try:
            self._enter_chat_room('room_1')

            self._open_new_window()
            self._enter_chat_room('room_2')

            self._switch_to_window(0)
            self._post_message('hello')
            WebDriverWait(self.driver, 2).until(lambda _:
                'hello' in self._chat_log_value,
                'Message was not received by window 1 from window 1')

            self._switch_to_window(1)
            self._post_message('world')
            WebDriverWait(self.driver, 2).until(lambda _:
                'world' in self._chat_log_value,
                'Message was not received by window 2 from window 2')
            self.assertTrue('hello' not in self._chat_log_value,
                'Message was improperly received by window 2 from window 1')
        finally:
            self._close_all_new_windows()