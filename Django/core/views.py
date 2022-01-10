from django.shortcuts import render


def index(request):
    context = {
        'curso': 'Progamação Web com Django Framework',
        'outro': 'Django é massa!'
    }
    return render(request, 'index.html', context)

def contato(request):
    return render(request, 'contato.html')
