from django import forms
from django.db.models import IntegerField


class AdocaoForm(forms.Form):
    nome = forms.CharField(label="Qual seu nome?", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    idade = forms.IntegerField(label="Sua idade?", widget=forms.NumberInput(attrs={'class': 'form-control'}))
    numero_contato = forms.CharField(
        label="Qual seu número para entrarmos em contato?",
        max_length=15,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex.: +55 11 12345-4321'})
    )
    trabalha = forms.ChoiceField(
        label="Trabalha?",
        choices=[('sim', 'Sim'), ('nao', 'Não')],
        widget=forms.RadioSelect
    )
    tem_outros_pets = forms.ChoiceField(
        label="Tem outros pets?",
        choices=[('sim', 'Sim'), ('nao', 'Não')],
        widget=forms.RadioSelect
    )
    vacinados = forms.ChoiceField(
        label="Estão vacinados?",
        choices=[('sim', 'Sim'), ('nao', 'Não')],
        widget=forms.RadioSelect
    )
    testou_fiv_felv = forms.ChoiceField(
        label="Se forem gatos, testou para FIV/FELV?",
        choices=[('sim', 'Sim'), ('nao', 'Não'), ('nao_aplica', 'Não se aplica')],
        widget=forms.RadioSelect
    )
    mora = forms.ChoiceField(
        label="Mora em casa ou apartamento?",
        choices=[('casa', 'Casa'), ('apartamento', 'Apartamento')],
        widget=forms.RadioSelect
    )
    janelas_teladas = forms.ChoiceField(
        label="A casa/ap tem as janelas teladas?",
        choices=[('sim', 'Sim'), ('nao', 'Não')],
        widget=forms.RadioSelect
    )
    mora_com_outros = forms.ChoiceField(
        label="Mora com outras pessoas?",
        choices=[('sim', 'Sim'), ('nao', 'Não')],
        widget=forms.RadioSelect
    )
    concordam_adocao = forms.ChoiceField(
        label="As pessoas com que mora concordam com a adoção do gatinho?",
        choices=[('sim', 'Sim'), ('nao', 'Não')],
        widget=forms.RadioSelect
    )