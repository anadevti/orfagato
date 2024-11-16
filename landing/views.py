from django.shortcuts import render
from .forms import AdocaoForm
from .models import Gato

# Create your views here.

def home(request):
    return render(request, 'landing/home.html')

def sobre(request):
    return render(request, 'landing/sobre.html')

def adocao_view(request):
    gatos = Gato.objects.all()
    if request.method == 'POST':
        form = AdocaoForm(request.POST)
        if form.is_valid():
            # Aqui você pode processar os dados (salvar em banco ou enviar por e-mail)
            return render(request, 'landing/obrigado.html')  # Página de agradecimento
    else:
        form = AdocaoForm()

    # Combine os contextos em um único dicionário
    context = {
        'form': form,
        'gatos': gatos,
    }
    return render(request, 'landing/adocao.html', context)


def contato(request):
    return render(request, 'landing/contato.html')