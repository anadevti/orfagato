from django.shortcuts import render
from .models import Gato, Interessado
from .forms import AdocaoForm

# Create your views here.

def home(request):
    return render(request, 'landing/home.html')

def sobre(request):
    return render(request, 'landing/sobre.html')


def adocao_view(request):
    # Busca todos os gatinhos cadastrados no banco de dados
    gatos = Gato.objects.all()

    if request.method == 'POST':
        form = AdocaoForm(request.POST)
        if form.is_valid():
            # Crie uma instância do modelo Interessado com os dados do formulário
            Interessado.objects.create(
                nome=form.cleaned_data['nome'],
                idade=form.cleaned_data['idade'],
                trabalha=form.cleaned_data['trabalha'],
                tem_outros_pets=form.cleaned_data['tem_outros_pets'],
                vacinados=form.cleaned_data['vacinados'],
                testou_fiv_felv=form.cleaned_data['testou_fiv_felv'],
                mora=form.cleaned_data['mora'],
                janelas_teladas=form.cleaned_data['janelas_teladas'],
                mora_com_outros=form.cleaned_data['mora_com_outros'],
                concordam_adocao=form.cleaned_data['concordam_adocao'],
                numero_contato=form.cleaned_data['numero_contato']
            )
            # Redirecione para uma página de agradecimento
            return render(request, 'landing/obrigado.html')
    else:
        form = AdocaoForm()

    # Passa os gatos e o formulário para o template
    return render(request, 'landing/adocao_form.html', {'form': form, 'gatos': gatos})




def contato(request):
    return render(request, 'landing/contato.html')