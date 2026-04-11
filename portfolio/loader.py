import json
from portfolio.models import TFC, Licenciatura

# Apagar TFCs antigos para evitar duplicados caso corras o script mais de uma vez
TFC.objects.all().delete()

# Abrir o ficheiro JSON que acabaste de colar
with open('portfolio/json/tfcs_2025.json', encoding='utf-8') as f:
    tfcs = json.load(f)

    for item in tfcs:
        # 1. Lidar com a Licenciatura (O JSON só dá o nome da licenciatura)
        nome_licenciatura = item['licenciaturas']
        if not nome_licenciatura: # Se vier vazio no JSON
            nome_licenciatura = "Não Especificada"

        # Procura a Licenciatura. Se não existir, cria uma automaticamente!
        licenciatura_obj, created = Licenciatura.objects.get_or_create(
            nome=nome_licenciatura,
            defaults={
                'sigla': 'N/A',
                'descricao': 'Criada via script de importação',
                'duracao_anos': 3,
                'ects_total': 180
            }
        )

        # 2. Criar o TFC
        TFC.objects.create(
            titulo=item['titulo'],
            autor=item['autores'] if item['autores'] else "Autor Desconhecido",
            resumo=item['sumario'],
            ano=2024, # Como o JSON não tem ano, definimos 2024 por defeito
            licenciatura=licenciatura_obj,
            link_pdf=item['link_pdf'],
            imagem_url=item['imagem']
        )

print("✅ Todos os TFCs foram importados com sucesso!")