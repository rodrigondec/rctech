from unittest.mock import MagicMock, patch

from django.test import TestCase
from bs4 import BeautifulSoup

from core.scrapping import PortalScrapper


class PortalScrapperTests(TestCase):
    def test_init_error(self):
        self.assertRaises(TypeError, PortalScrapper)

    @patch('core.scrapping.request_page', return_value=MagicMock(content='<html><body>oi</body></html>'))
    def test_load_soup(self, mocked_request_page):
        self.assertIsInstance(mocked_request_page, MagicMock)
        mock = MagicMock(url='http://www.google.com.br/', load_soup=PortalScrapper.load_soup)
        mock.load_soup(mock)
        self.assertIsInstance(mock.page, BeautifulSoup)
        mocked_request_page.assert_called_once_with('http://www.google.com.br/')
