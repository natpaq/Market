from django.test import TestCase, Client
from item.models import Item, OrderItem
from django.urls import reverse
from django.contrib.auth.models import User



class TestViews(TestCase):

    #Were going to test the signup page (get and post requests)
    def setUp(self):
        self.client = Client()
        self.main_url = reverse('signup')
        self.user = User.objects.create(username='Testuser')

    def test_project_GET(self):
        client = self.client
        response = client.get(self.main_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'signup.html')

    def test_project_POST(self):
        response = self.client.post(self.main_url, {'username': 'Test 123', 'password': "Password ;)"})
        self.assertEquals(response.status_code, 302)



