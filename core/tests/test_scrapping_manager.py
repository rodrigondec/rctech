from unittest.mock import MagicMock, patch

from django.test import TestCase

from core.scrapping import ScrappingManager


class ScrappingManagerTests(TestCase):
    @patch.object(ScrappingManager, 'SCRAPPERS', [MagicMock])
    def test_init(self):
        manager = ScrappingManager()
        self.assertEqual(len(manager.scrappers), 1)

    @patch.object(ScrappingManager, 'SCRAPPERS', [MagicMock])
    def test_process(self):
        manager = ScrappingManager()
        self.assertEqual(len(manager.scrappers), 1)

        manager.process()
        manager.scrappers[0].process.assert_called_once()
