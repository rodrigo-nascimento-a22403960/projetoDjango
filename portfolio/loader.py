import json
from portfolio.models import TFC, Licenciatura

# 1. Limpar dados antigos para evitar duplicados
TFC.objects.all().delete()

# 2. Abrir o ficheiro JSON (caminho atualizado para a pasta data)
with open('portfolio/data/tfcs_2025.json', encoding='utf-8') as f:
    tfcs = json.load(f)

    for item in tfcs:
        # Lidar com a Licenciatura
        nome_licenciatura = item.get('licenciaturas', "Não Especificada")
        if not nome_licenciatura:
            nome_licenciatura = "Não Especificada"

        # get_or_create: Procura ou cria se não existir
        licenciatura_obj, created = Licenciatura.objects.get_or_create(
            nome=nome_licenciatura,
            defaults={
                'sigla': 'N/A',
                'descricao': 'Importado via script',
                'duracao_anos': 3,
                'ects_total': 180
            }
        )

        # Criar o objeto TFC
        TFC.objects.create(
            titulo=item['titulo'],
            autor=item.get('autores', "Autor Desconhecido"),
            resumo=item.get('sumario', "Sem resumo disponível"),
            ano=2024,
            licenciatura=licenciatura_obj,
            link_pdf=item.get('link_pdf', ""),
            imagem_url=item.get('imagem', "")
        )

print("✅ Todos os TFCs foram importados com sucesso!")