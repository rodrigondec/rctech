from django.views.generic import ListView

from core.forms import ArticleForm
from core.models import Article


class HomeView(ListView):
    template_name = 'core/index.html'
    model = Article
    form_class = ArticleForm
    context_object_name = 'articles'
    paginate_by = 5

    def get_queryset(self):
        form = self.form_class(self.request.GET)
        if form.is_valid():
            articles = self.model.objects.filter(title__icontains=form.cleaned_data['title'])
        else:
            articles = self.model.objects.all()
        return articles
