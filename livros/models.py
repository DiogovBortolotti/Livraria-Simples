from django.db import models

# Create your models here.

class Livros(models.Model):
    id = models.AutoField(primary_key=True)    
    titulo = models.CharField(max_length=255)
    autor = models.CharField(max_length=255)
    ano_lancamento = models.IntegerField()
    status = models.CharField(max_length=20, choices=[("bom", "Bom"), ("execelente", "Execelente"), ("ruim", "Ruim")])
    paginas = models.IntegerField()
    publicado = models.CharField(max_length=255)
    criado_em = models.DateTimeField(auto_now_add=True)