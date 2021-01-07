from django.test import TestCase
from django.core.urlresolvers import reverse
from .forms import *
from .views import *

class MushroomTest(TestCase):
    def test_valid_MessageForm(self):
        data = {'name': "name@gmail.com", 'subject': "subject", 'message': "message"}
        form = MessageForm(data = data)
        self.assertTrue(form.is_valid())

        data = {'name': "name@hotmail.com", 'subject': "subject", 'message': "message"}
        form = MessageForm(data = data)
        self.assertTrue(form.is_valid())

        data = {'name': "name@gmail.com", 'subject': "abcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcde", 'message': "message"}
        form = MessageForm(data = data)
        self.assertTrue(form.is_valid())

    def test_invalid_MessageForm(self):
        data = {'name': "", 'subject': "", 'message': ""}
        form = MessageForm(data = data)
        self.assertFalse(form.is_valid())

        data = {'name': "", 'subject': "subject", 'message': ""}
        form = MessageForm(data = data)
        self.assertFalse(form.is_valid())

        data = {'name': "", 'subject': "", 'message': "message"}
        form = MessageForm(data = data)
        self.assertFalse(form.is_valid())

        data = {'name': "", 'subject': "subject", 'message': "message"}
        form = MessageForm(data = data)
        self.assertFalse(form.is_valid())

        data = {'name': "name", 'subject': "subject", 'message': "message"}
        form = MessageForm(data = data)
        self.assertFalse(form.is_valid())

        data = {'name': "name@gmail.com", 'subject': "", 'message': ""}
        form = MessageForm(data = data)
        self.assertFalse(form.is_valid())

        data = {'name': "name@gmail.com", 'subject': "subject", 'message': ""}
        form = MessageForm(data = data)
        self.assertFalse(form.is_valid())

        data = {'name': "name@gmail.com", 'subject': "", 'message': "message"}
        form = MessageForm(data = data)
        self.assertFalse(form.is_valid())

        data = {'name': "name@gmail.com", 'subject': "abcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdeabcdea", 'message': "message"}
        form = MessageForm(data = data)
        self.assertFalse(form.is_valid())

    def test_home_view(self):
        url = reverse("home")
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)

    def test_SendEmail_view(self):
        url = reverse("SendEmail")
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)