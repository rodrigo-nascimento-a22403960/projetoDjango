import os
import django
import json

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from tfcs.models import TFC

# Apaga dados antigos
TFC.objects.all().delete()

with open('data/tfcs_2025_.json', encoding='utf-8') as f:
    tfcs = json.load(f)

for tfc in tfcs:
    TFC.objects.create(
        titulo=tfc.get('titulo', ''),
        autores=tfc.get('autores', ''),
        orientadores=tfc.get('orientadores', ''),
        licenciaturas=tfc.get('licenciaturas', ''),
        sumario=tfc.get('sumario', ''),
        link_pdf=tfc.get('link_pdf', ''),
        imagem=tfc.get('imagem', ''),
        palavras_chave=tfc.get('palavras_chave', ''),
        areas=tfc.get('areas', ''),
        tecnologias_usadas=tfc.get('tecnologias_usadas', ''),
        rating=tfc.get('rating', 0),
    )

print(f"{TFC.objects.count()} TFCs carregados com sucesso!")