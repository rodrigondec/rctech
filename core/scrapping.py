import logging
from abc import ABC, abstractmethod

from bs4 import BeautifulSoup

from core.utils import request_page
from core.models import Article


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
        raise NotImplementedError('Cannot call method from abstract class')


class TecmundoScrapper(PortalScrapper):
    def __init__(self):
        logging.info(f'{self.__class__.__name__} inicializando...')
        super(TecmundoScrapper, self).__init__('https://www.tecmundo.com.br/')

    def process(self):
        logging.info(f'{self.__class__.__name__} processando...')
        logging.info(f'{self.__class__.__name__} pegando todos os artigos da página...')
        article_tags = self.page_data.find_all('article')
        logging.info(f'{self.__class__.__name__} {len(article_tags)} artigos identificados!')
        for article_tag in article_tags:
            figure = article_tag.find('figure')
            div = figure.nextSibling
            a = div.find('a')
            article, created = Article.objects.get_or_create(title=a.text.strip())
            if created:
                logging.info(f'{self.__class__.__name__} artigo "{article.title}" cadastrado!')
            else:
                logging.info(f'{self.__class__.__name__} artigo "{article.title}" já estava cadastrado no sistema!')


class ScrappingManager(object):
    SCRAPPERS = [TecmundoScrapper]

    def __init__(self):
        logging.info(f'{self.__class__.__name__} inicializando...')
        self.scrappers = []
        self.initialize_scrappers()

    def initialize_scrappers(self):
        logging.info(f'{self.__class__.__name__} instanciando scrappers...')
        for scrapper_cls in self.SCRAPPERS:
            scrapper = scrapper_cls()
            assert isinstance(scrapper, PortalScrapper)
            self.scrappers.append(scrapper)

    def process(self):
        logging.info(f'{self.__class__.__name__} processando scrappers...')
        for scrapper in self.scrappers:
            scrapper.process()
