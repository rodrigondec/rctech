import logging
from abc import ABC, abstractmethod

from bs4 import BeautifulSoup

from core.utils import request_page


logging.basicConfig(level=logging.INFO)


class PortalScrapper(ABC):
    def __init__(self, url=None):
        self.url = url
        self.page = None
        self.page_data = None
        self.load_soup()

    def load_soup(self):
        logging.info(f'{self.__class__.__name__} requisitando a página {self.url}...')
        self.page = request_page(self.url)
        self.page_data = BeautifulSoup(self.page.content, 'html.parser')

    @abstractmethod
    def process(self):
        raise NotImplemented('Cannot call method from abstract class')
