from django.test import TestCase

from core.utils import request_page


class UtilsTests(TestCase):
    def test_request_page(self):
        url = 'https://www.google.com.br/'
        response = request_page(url)
        self.assertEqual(response.status_code, 200)
