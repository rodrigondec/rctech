from django.urls import reverse
from django.test import TestCase

from core.models import Article
from core.factories import ArticleFactory


class ArticleIndexViewTests(TestCase):
    def test_no_articles(self):
        """
        If no arqicles exist, an appropriate message is displayed.
        """
        response = self.client.get(reverse('core:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Notícias não encontradas")
        self.assertQuerysetEqual(response.context['articles'], [])

    def test_articles(self):
        ArticleFactory.create_batch(3)
        self.assertEqual(3, Article.objects.count())

        response = self.client.get(reverse('core:index'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['articles']), 3)
        self.assertEqual(list(response.context['articles']), list(Article.objects.all()))

    def test_filter_articles(self):
        ArticleFactory(title='Minha noticia 1')
        ArticleFactory(title='Minha noticia 2')
        ArticleFactory(title='noticia 1')

        self.assertEqual(3, Article.objects.count())

        response = self.client.get(reverse('core:index'), data={'title': 'min'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Article.objects.filter(title__icontains='min').count(), 2)
        self.assertEqual(len(response.context['articles']), 2)
        self.assertEqual(list(response.context['articles']), list(Article.objects.filter(title__icontains='min')))
