from django.db import models
from django.contrib.auth.models import User

class Artigo(models.Model):
    titulo = models.CharField(max_length=200) # Adicionado para dar nome ao artigo
    texto = models.TextField()
    fotografia = models.ImageField(upload_to='artigos/', blank=True, null=True)
    link_externo = models.URLField(blank=True, null=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    
    # Como "qualquer pessoa" pode dar like, um contador numérico é a forma mais simples
    likes = models.IntegerField(default=0) 

    def __str__(self):
        return self.titulo


class Comentario(models.Model):
    # Relaciona o comentário ao artigo específico (related_name ajuda a listar depois)
    artigo = models.ForeignKey(Artigo, on_delete=models.CASCADE, related_name='comentarios')
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    texto = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comentário de {self.autor.username} em {self.artigo.titulo}"