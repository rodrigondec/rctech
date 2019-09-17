from django.forms import ModelForm

from core.models import Article


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['title']
