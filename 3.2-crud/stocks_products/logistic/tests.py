from unittest import TestCase
from rest_framework.test import APIClient


class TestView(TestCase):
    def test_response(self):
        url = '/api/v1/test'
        client = APIClient()
        response = client.get(url, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, 'Запущена тестовая страница')
