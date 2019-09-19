from unittest.mock import MagicMock, patch

from django.test import TestCase
from bs4 import BeautifulSoup

from core.scrapping import TecmundoScrapper
from core.models import Article
from core.factories import ArticleFactory


class TecmundoScrapperTests(TestCase):
    @patch('core.scrapping.request_page', return_value=MagicMock(content='<html><body>oi</body></html>'))
    def test_init(self, mocked_request_page):
        self.assertIsInstance(mocked_request_page, MagicMock)
        instance = TecmundoScrapper()
        self.assertIsInstance(instance.page, BeautifulSoup)
        mocked_request_page.assert_called_once_with('https://www.tecmundo.com.br/')

    @patch(
        'core.scrapping.request_page',
        return_value=MagicMock(
           content='<html><body><article><figure>img</figure><div><a>Article Tittle</a></div></article></body></html>')
    )
    def test_process(self, mocked_request_page):
        self.assertIsInstance(mocked_request_page, MagicMock)
        instance = TecmundoScrapper()
        self.assertIsInstance(instance.page, BeautifulSoup)

        self.assertEqual(Article.objects.count(), 0)
        instance.process()
        self.assertEqual(Article.objects.count(), 1)
        self.assertEqual(Article.objects.first().title, 'Article Tittle')

    @patch(
        'core.scrapping.request_page',
        return_value=MagicMock(
            content='<html><body><article><figure>img</figure><div><a>Article Tittle</a></div></article></body></html>')
    )
    def test_process_duplicated_article(self, mocked_request_page):
        self.assertIsInstance(mocked_request_page, MagicMock)
        instance = TecmundoScrapper()
        self.assertIsInstance(instance.page, BeautifulSoup)

        ArticleFactory(title='Article Tittle')

        self.assertEqual(Article.objects.count(), 1)
        instance.process()
        self.assertEqual(Article.objects.count(), 1)
        self.assertEqual(Article.objects.first().title, 'Article Tittle')
