from django.contrib import messages
from django.shortcuts import render

from core.forms import ContatoForm
# Create your views here.

def index(request):
    return render(request, 'index.html')

def contato(request):
    form = ContatoForm(request.POST or None)

    if str(request.method) == 'POST':
        if form.is_valid():
            form.send_mail()

            messages.success(request, 'E-mail enviado com sucesso!')

            form = ContatoForm()

        else:
            messages.error(request, 'Erro ao envia e-mail')

    context = {
        'form': form
    }

    return render(request, 'contato.html', context)

def produto(request):
    return render(request, 'produto.html')
