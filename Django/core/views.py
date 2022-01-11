from django.shortcuts import render


from core.models import Produto


def index(request):
    produtos = Produto.objects.all()
    context = {
        'curso': 'Progamação Web com Django Framework',
        'outro': 'Django é massa!',
        'produtos': produtos
    }
    return render(request, 'index.html', context)

def contato(request):
    return render(request, 'contato.html')

def produto(request, pk):
    prod = Produto.objects.get(id=pk)
    context = { 'produto': prod}

    return render(request, 'produto.html', context)
