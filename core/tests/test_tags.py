from unittest.mock import MagicMock

from django.test import TestCase

from core.templatetags.title_tags import param_replace


class TagsTests(TestCase):
    def test_without_data(self):
        request = MagicMock(GET=MagicMock(get=MagicMock(return_value=None)))
        context = {
            'request': request
        }
        data = param_replace(context, ex='test')
        self.assertEqual(data, 'ex=test')

    def test_without_data_and_empty_value(self):
        request = MagicMock(GET=MagicMock(get=MagicMock(return_value=None)))
        context = {
            'request': request
        }
        data = param_replace(context, ex='')
        self.assertEqual(data, '')

    def test_with_data_and_empty_value(self):
        request = MagicMock(GET=MagicMock(get=MagicMock(return_value='value')))
        context = {
            'request': request
        }
        data = param_replace(context, ex='')
        self.assertEqual(data, 'title=value')

    def test_with_data(self):
        request = MagicMock(GET=MagicMock(get=MagicMock(return_value='value')))
        context = {
            'request': request
        }
        data = param_replace(context, ex='test')
        self.assertTrue((data == 'title=value&ex=test') or data == 'ex=test&title=value')
