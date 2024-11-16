from django.db import models

class Gato(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.PositiveIntegerField()  # Idade em anos
    sexo = models.CharField(max_length=10, choices=[('Macho', 'Macho'), ('Fêmea', 'Fêmea')])
    castrado = models.BooleanField(default=False)
    fiv_felv = models.CharField(max_length=10, choices=[('Positivo', 'Positivo'), ('Negativo', 'Negativo')])
    vacinado = models.BooleanField(default=False)
    imagem = models.ImageField(upload_to='gatos/', blank=True, null=True)
    descricao = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nome
