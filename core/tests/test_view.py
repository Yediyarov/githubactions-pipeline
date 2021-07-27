from django.test import TestCase, Client
from django.urls import reverse

class ViewTest(TestCase):

    def test_index_view(self):
        url = reverse('index')
        client = Client()
        response = client.get(url)
        self.assertEqual(response.status_code,200)

