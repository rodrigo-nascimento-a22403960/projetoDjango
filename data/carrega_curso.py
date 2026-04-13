import os
import django
import json

import sys
sys.path.insert(0, '/workspaces/projetoDjango')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from licenciatura.models import Licenciatura, UnidadeCurricular

# Apaga dados antigos
UnidadeCurricular.objects.all().delete()
Licenciatura.objects.all().delete()

# Lê o ficheiro principal do curso
with open('files/ULHT260-PT.json', encoding='utf-8') as f:
    curso = json.load(f)

# Cria a Licenciatura com dados reais do JSON
lei = Licenciatura.objects.create(
    nome=curso.get('courseName', 'Engenharia Informática'),
    sigla='LEI',
    descricao=curso.get('courseDescription', 'Licenciatura em Engenharia Informática da Universidade Lusófona'),
    duracao_anos=3,
    ects_total=180,
)

# Mapear semestre a partir do courseFlatPlan
semestre_map = {}
for uc_info in curso['courseFlatPlan']:
    codigo = uc_info['curricularIUnitReadableCode']
    semestre_map[codigo] = uc_info.get('curricularSemester', 1)

# Para cada UC no plano curricular
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
        semestre=semestre_map.get(codigo, 1),
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
    print(f"✓ {uc.get('curricularUnitName', codigo)}")

print(f"\nTotal: {UnidadeCurricular.objects.count()} UCs carregadas!")