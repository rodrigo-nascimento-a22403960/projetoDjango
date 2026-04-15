import os
import sys
import django
import json

# Adiciona a pasta raiz do projeto ao path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()



from portfolio.models import Licenciatura, UnidadeCurricular

UnidadeCurricular.objects.all().delete()
Licenciatura.objects.all().delete()

lei = Licenciatura.objects.create(
    nome='Engenharia Informática',
    sigla='LEI',
    descricao='Licenciatura em Engenharia Informática da Universidade Lusófona',
    duracao_anos=3,
    ects_total=180,
)

with open('files/ULHT260-PT.json', encoding='utf-8') as f:
    curso = json.load(f)

for uc_info in curso['courseFlatPlan']:
    codigo = uc_info['curricularIUnitReadableCode']
    ficheiro = f"files/{codigo}-PT.json"

    if not os.path.exists(ficheiro):
        print(f"Ficheiro não encontrado: {ficheiro}")
        continue

    with open(ficheiro, encoding='utf-8') as f:
        uc = json.load(f)

    UnidadeCurricular.objects.create(
        nome=uc.get('curricularUnitName', ''),
        codigo=codigo,
        ano_curricular=uc.get('curricularYear', 1),
        ects=uc.get('ects', 0),
        natureza=uc.get('nature', ''),
        objetivos=uc.get('objectives', ''),
        apresentacao=uc.get('presentation', ''),
        metodologia=uc.get('methodology', ''),
        programa=uc.get('programme', ''),
        bibliografia=uc.get('bibliography', ''),
        avaliacao=uc.get('avaliacao', ''),
        licenciatura=lei,
    )
   

