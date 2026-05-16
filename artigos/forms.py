from django import forms
from .models import Artigo, Comentario

class ArtigoForm(forms.ModelForm):
    class Meta:
        model = Artigo
        # Repara que não colocamos aqui o 'autor' nem os 'likes', 
        # porque isso é preenchido automaticamente por trás das cortinas!
        fields = ['titulo', 'texto', 'fotografia', 'link_externo']

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['texto']
        labels = {'texto': 'O teu comentário'}