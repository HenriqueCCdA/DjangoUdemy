from django.views.generic import ListView

from core.models import Produto


class IndexListView(ListView):
    template_name = 'index.html'
    model = Produto
    paginate_by = 4
    ordering = '-id'
