# Diário de Bordo: Processo de Modelação do Portfólio

Este documento regista a evolução, as decisões e os erros corrigidos durante 
a fase de modelação da base de dados do projeto de Portfólio em Django.

## 1. Fotografias do DER e Apontamentos
O planeamento foi feito em papel e colocado no ficheiro docs_makingOf 
que tem uma pasta chamada imagens_papel. As imagens mostram todo o 
planeamento antes de passar para o código no computador:
* `docs_makingOf/imagens_papel/`

## 2. Evolução do Modelo e Correção de Erros

### Versão 1 (Rascunho Inicial)
* **Erro Identificado:** O primeiro rascunho deixava algumas entidades 
  (como as Formações) desconectadas do resto do modelo.
* **Correção:** Atualizei as relações para que todas as tabelas fizessem 
  parte da mesma rede. A `Licenciatura` passou a agregar todo o percurso 
  académico, enquanto as `Competencias` passaram a cruzar a informação 
  ganha tanto nos `Projetos` como nas `Formações`.

### Versão 2 (Ajuste de Relações)
* **Erro Identificado 1:** A relação inicial entre `Licenciatura` e `TFC` 
  era de 1:N. No entanto, no contexto do meu portfólio pessoal, a minha 
  licenciatura apenas me permite ter um TFC.
* **Correção 1:** Alterei para `OneToOneField`, garantindo que a minha 
  licenciatura culmina num único Trabalho Final de Curso.
* **Erro Identificado 2:** Faltavam atributos obrigatórios definidos nos 
  requisitos (imagens, links de repositório, datas).
* **Correção 2:** Adicionei `ImageField` para logos/imagens, `URLField` 
  para GitHub e páginas de docentes, e `DateField` para ordenação 
  cronológica das formações.

### Versão 3 (Implementação e Erros de Sintaxe)
* **Erro Identificado 3:** `IndentationError` durante a implementação. 
  O Python bloqueou as migrações porque o `models.py` tinha espaços 
  desalinhados.
* **Correção 3:** Realinhamento completo do bloco de código no `models.py` 
  com indentação correta (4 espaços por nível).
* **Erro Identificado 4:** No painel admin, o Django gerou nomes no plural 
  incorretos como "Unidade curriculars" e "Tfcs".
* **Correção 4:** Utilização de `class Meta` com `verbose_name_plural` 
  em português ("Unidades Curriculares", "TFCs").

### Versão 4 (Reestruturação das Apps)
* **Erro Identificado 5:** Inicialmente criei uma app separada para cada 
  entidade (licenciatura, docentes, tecnologias, etc.), semelhante ao 
  projeto de um colega. No entanto, após indicação, a abordagem correta 
  para este projeto é ter tudo dentro de uma única app `portfolio`.
* **Correção 5:** Apaguei todas as apps separadas e movi todos os modelos 
  para `portfolio/models.py`, atualizando o `settings.py` em conformidade.

### Versão 5 (Erros de Configuração)
* **Erro Identificado 6:** Ao tentar correr `python manage.py startapp`, 
  apareceu `Remove-Item: command not found` porque copiei um comando 
  PowerShell (Windows) num ambiente Linux (GitHub Codespaces).
* **Correção 6:** Utilizei o comando correto para Linux: `rm -rf`.

* **Erro Identificado 7:** `ModuleNotFoundError: No module named 'django'` 
  porque o Django não estava instalado no ambiente.
* **Correção 7:** Instalei com `pip install django pillow`.

* **Erro Identificado 8:** `ImportError` no `portfolio/admin.py` porque 
  estava a importar modelos que tinham sido removidos do `portfolio/models.py`.
* **Correção 8:** Limpei o `admin.py` e o `models.py` do portfolio antes 
  de criar as novas apps.

* **Erro Identificado 9:** `IndentationError: unexpected indent` no 
  `settings.py` porque o `INSTALLED_APPS` tinha um espaço extra no início.
* **Correção 9:** Removi o espaço e garantia que a variável estava 
  corretamente alinhada à margem esquerda.

## 3. Carregamento de Dados via JSON e API

### TFCs
O ficheiro JSON dos TFCs foi analisado e verificou-se que continha campos 
adicionais não previstos no modelo inicial: `link_pdf`, `imagem`, 
`palavras_chave`, `areas`, `tecnologias_usadas` e `rating`. O modelo foi 
atualizado para incluir estes campos e foi criado o script 
`data/carrega_tfcs.py` para automatizar o carregamento via ORM Django.

* **Erro Identificado:** Ao correr o script, apareceu 
  `NameError: name 'requests' is not defined` porque o ficheiro 
  `carrega_tfcs.py` tinha o conteúdo errado (tinha o código do 
  `download_curso.py`).
* **Correção:** Substituição do conteúdo pelo loader correto.

* **Erro Identificado 2:** `ModuleNotFoundError: No module named 'project'` 
  ao correr os scripts de carregamento.
* **Correção 2:** Adição de `sys.path.insert(0, ...)` no início dos 
  scripts para que o Python encontre o módulo `project`.

### Curso e Unidades Curriculares
Utilizei a API pública da Lusófona para descarregar os dados do curso LEI 
(código 260) e de cada Unidade Curricular. O script `data/download_curso.py` 
faz o download dos JSONs para a pasta `files/`. O script 
`data/carrega_curso.py` lê esses JSONs e carrega os dados na base de dados 
usando o ORM Django. Os dados carregados incluem: nome, código, ano 
curricular, ECTS, natureza, objetivos, apresentação, metodologia, 
programa, bibliografia e avaliação.

## 4. Justificação das Decisões de Modelação

**1. Licenciatura** — Base de tudo. `CASCADE` nas UCs garante que não 
ficam dados órfãos. `PositiveIntegerField` para ECTS e duração bloqueia 
valores negativos automaticamente.

**2. Docente** — Entidade separada em vez de campo de texto, resolve a 
relação N:M real (um professor dá várias UCs, uma UC tem vários professores). 
`URLField` para ligar à página oficial na Lusófona.

**3. Unidade Curricular** — `ForeignKey` para Licenciatura (1:N). 
`ImageField` para o Frontend mostrar cartões visuais por disciplina. 
Campos detalhados da API (objetivos, metodologia, programa, bibliografia) 
enriquecem o portfólio.

**4. Projeto** — Tabela que cruza mais dados: liga à UC (1:N), Tecnologias 
(N:M) e Competências (N:M). GitHub obrigatório pois é a primeira coisa 
que um recrutador quer ver.

**5. Tecnologia** — Entidade separada ligada por N:M evita repetição 
("Python" escrito uma vez, ligado a vários projetos). `nivel_preferencia` 
permite ordenar a stack favorita no topo.

**6. TFC** — `destaque` booleano funciona como "interruptor" para afixar 
o TFC na página principal via Admin.

**7. Competência** — Liga N:M a Projetos. `tipo` permite separar 
Hard Skills de Soft Skills no currículo digital.

**8. Formação** — `DateField` com `ordering = ['-data_inicio']` ordena 
automaticamente do mais recente para o mais antigo.

**9. Making Of** — Auto-documentação do processo. Campos `decisoes`, 
`erros_correcoes` e `uso_ia` garantem transparência técnica e cumprem 
os critérios de avaliação.

## 5. Implementação de Views e Templates

Para cada entidade foi criada uma view, um template HTML e uma URL:
* `portfolio/views.py` — funções para listar cada entidade
* `portfolio/templates/portfolio/` — templates HTML com `base.html` 
  como layout comum
* `portfolio/urls.py` — rotas para cada página
* `portfolio/static/portfolio/styles.css` — estilização comum

O mesmo processo foi seguido para a app `escola`, que serviu como 
exercício prático antes de aplicar ao portfólio.

## 6. Uso de Inteligência Artificial

Durante este processo utilizei IA (Claude da Anthropic) como 
peer-programmer e tutor. A IA foi utilizada para:
* Debug de erros de configuração e sintaxe
* Correção de comandos errados (PowerShell vs Linux)
* Criação dos scripts de carregamento de dados JSON
* Estruturação dos modelos Django
* Criação de views, templates e URLs
* Todas as decisões finais de modelação foram tomadas por mim, 
  com a IA a servir de suporte técnico