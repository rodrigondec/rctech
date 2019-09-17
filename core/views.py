from django.views.generic import ListView

from core.models import Article


class HomeView(ListView):
    template_name = 'core/index.html'
    model = Article
    context_object_name = 'articles'
    paginate_by = 5
