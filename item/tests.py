from django.test import TestCase, Client, SimpleTestCase
from item.forms import AddItemForm
from django.urls import reverse, resolve
from item.views import checkout, payment
from item.models import Item

class TestForms(SimpleTestCase):
    #Test if the form accepts everything even if just the image is not input into the form properly
    def test_AddItemForm_valid_image(self):
        form = AddItemForm(data={
            'image': '',
            'itemname': 'Testing Item',
            'descrip': 'This is just a test',
            'price': 10.99,
            'inv_count': 10
        })

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)


#Make sure the urls are routing the proper views
class TestUrls(SimpleTestCase):
    def test_urls(self):
        url = reverse('checkout')
        self.assertEquals(resolve(url).func, checkout)

    def test_urls_2(self):
        url = reverse('payment')
        self.assertEquals(resolve(url).func, payment)


