from django.db import models

class Gato(models.Model):
    SEXO_CHOICES = [
        ('Macho', 'Macho'),
        ('Fêmea', 'Fêmea'),
    ]

    FIV_FELV_CHOICES = [
        ('Positivo', 'Positivo'),
        ('Negativo', 'Negativo'),
    ]

    nome = models.CharField(max_length=100, verbose_name="Nome do Gato")
    idade = models.PositiveIntegerField(verbose_name="Idade em anos")  # Idade do gato
    sexo = models.CharField(max_length=10, choices=SEXO_CHOICES, verbose_name="Sexo")
    castrado = models.BooleanField(default=False, verbose_name="Castrado")  # Sim ou não
    fiv_felv = models.CharField(max_length=10, choices=FIV_FELV_CHOICES, verbose_name="Status FIV/FELV")
    vacinado = models.BooleanField(default=False, verbose_name="Vacinado")  # Sim ou não
    imagem = models.ImageField(upload_to='gatos/', blank=True, null=True, verbose_name="Imagem do Gato")  # Upload de imagens
    descricao = models.TextField(blank=True, null=True, verbose_name="Descrição ou Observações")  # Texto descritivo opcional

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Gato"
        verbose_name_plural = "Gatos"
        ordering = ['nome']  # Ordenação por nome

class Interessado(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.PositiveIntegerField()
    trabalha = models.CharField(max_length=3, choices=[('sim', 'Sim'), ('nao', 'Não')])
    tem_outros_pets = models.CharField(max_length=3, choices=[('sim', 'Sim'), ('nao', 'Não')])
    vacinados = models.CharField(max_length=3, choices=[('sim', 'Sim'), ('nao', 'Não')])
    testou_fiv_felv = models.CharField(max_length=10, choices=[('sim', 'Sim'), ('nao', 'Não'), ('nao_aplica', 'Não se aplica')])
    mora = models.CharField(max_length=15, choices=[('casa', 'Casa'), ('apartamento', 'Apartamento')])
    janelas_teladas = models.CharField(max_length=3, choices=[('sim', 'Sim'), ('nao', 'Não')])
    mora_com_outros = models.CharField(max_length=3, choices=[('sim', 'Sim'), ('nao', 'Não')])
    concordam_adocao = models.CharField(max_length=3, choices=[('sim', 'Sim'), ('nao', 'Não')])
    numero_contato = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.nome} ({self.idade} anos)"
