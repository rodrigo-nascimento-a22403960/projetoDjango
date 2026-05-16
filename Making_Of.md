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


  #  Implementação do CRUD (Projetos, Tecnologias, Competências, Formações)

## O Desafio
O objetivo desta fase foi implementar as operações CRUD (Create, Read, Update, Delete) para as várias entidades do portfólio, permitindo gerir o conteúdo da aplicação diretamente pelo browser, de forma protegida.

## Dificuldades Encontradas e Erros

* **Erro de Nomenclatura (TemplateDoesNotExist):** Deparei-me com um erro clássico do Django ao tentar renderizar a página de criação. O erro indicava que o ficheiro `portfolio/form.html` não existia. A causa foi uma pequena assimetria entre o nome do ficheiro físico (que criei como `forms.html`, no plural) e o nome que estava a ser chamado na função `render` no `views.py` (no singular). A correção rápida passou por uniformizar tudo no `views.py` usando o "Find and Replace" para `forms.html`.
* **Compreensão do Sistema de Rotas:** Inicialmente, gerou-se uma confusão em relação aos links nos botões, como `{% url 'projeto_editar' projeto.id %}`. Pensei que seria necessário criar um ficheiro HTML físico para cada ação de cada tabela. Rapidamente percebi que a tag `{% url %}` não procura ficheiros físicos, mas sim o `name` da rota definido no `urls.py`, o que redireciona dinamicamente para a View e Template corretos.
* **Botões "Invisíveis":** Ao adicionar os botões de Edição e Apagar no HTML, eles não apareceram no ecrã. Isto aconteceu por duas razões lógicas: primeiro, o código `{% if request.user.is_authenticated %}` estava a ocultar os botões porque a sessão não tinha login feito; segundo, como a base de dados ainda não tinha projetos registados, o ciclo `{% for %}` não rodava e não desenhava a estrutura.

## O que achei mais útil e Vantagens do Django

* **Reutilização de Templates:** Uma das maiores vantagens que encontrei foi não ter de escrever código repetido. Consegui usar exatamente o mesmo ficheiro `forms.html` (com a tag mágica `{{ form.as_p }}`) e o mesmo `confirmar_apagar.html` para os Projetos, Tecnologias, Competências e Formações. O Django tratou de adaptar o formulário à base de dados de forma automática.
* **Segurança Integrada:** O uso do decorador `@login_required` no `views.py` e da verificação `request.user.is_authenticated` nos templates HTML revelou-se uma forma super rápida e robusta de proteger a aplicação, garantindo que nenhum visitante comum consegue apagar ou editar o meu portfólio.

## O que não gostei (ou aspetos a melhorar)

* **Estilização Padrão dos Formulários:** Embora o `{{ form.as_p }}` seja incrivelmente útil para poupar tempo, o HTML gerado "cru" é esteticamente muito básico e pouco apelativo. 
* **Usabilidade dos campos ManyToMany:** Os campos de relação Muitos-para-Muitos (como associar várias Tecnologias a um Projeto) exigem que o utilizador mantenha a tecla `Ctrl` pressionada para selecionar várias opções no browser, o que não é muito intuitivo em termos de Experiência de Utilizador (UX). Requererá a aplicação de CSS, JavaScript ou ferramentas como o *Crispy Forms* numa fase posterior.

## 7. Autenticação Avançada, Link Mágico e Segurança de Grupos

### O Desafio
O objetivo foi implementar um sistema de "Passwordless Login" (Magic Link) via envio de emails reais e, simultaneamente, aplicar uma camada de segurança robusta no portfólio. A ideia era garantir que não basta ter uma conta no site para gerir os projetos; é necessário ter o nível de "Gestor".

### Dificuldades e Erros Corrigidos
* **Erro de Ambiente (GitHub Codespaces vs Localhost):** * **Problema:** Ao enviar o email com o Link Mágico, o Django gerava o URL como `http://localhost:8000/...`. Ao clicar no email fora do ambiente, a página dava erro "Não é possível aceder a esta página". Além disso, recebi erros `Forbidden (403) CSRF verification failed` e `DisallowedHost`. Isto aconteceu porque o GitHub Codespaces cria um túnel e baralha as origens confiáveis do Django.
  * **Correção:** Atualizei as variáveis `ALLOWED_HOSTS` e `CSRF_TRUSTED_ORIGINS` no `settings.py` para aceitar os domínios `.app.github.dev`. Para o Link Mágico, em vez de forçar o Django a adivinhar o link dinamicamente, hardcodei o domínio base do Codespaces no `views.py` exatamente como recomendado na documentação da disciplina.
* **Segurança Baseada em Grupos (Botões Invisíveis):**
  * **Problema:** Após ter o login a funcionar na perfeição, reparei que os botões "Criar Projeto" e "Editar" continuavam a não aparecer. 
  * **Correção:** Percebi que as views (`@user_passes_test(is_gestor)`) e os templates (`{% if grupo.name == 'gestor-portfolio' %}`) estavam a exigir uma permissão superior. Acedi ao painel de administração (`/admin`), criei o grupo `gestor-portfolio` e adicionei a minha conta `RodrigoNascimento` a esse grupo.

---

## 8. Criação da App "Artigos" (Blog e Interatividade)

### O Desafio
Criar uma app independente chamada `artigos` para publicar conteúdos sobre tecnologias e soft-skills. Esta app exigiu um sistema próprio de Registo de Utilizadores, permissões segmentadas por autoria (só o autor pode editar o seu artigo), Likes e Comentários.

### Decisões de Modelação e Lógica
* **Associação Automática de Autores:** Na View de registo (`registo_view`), adicionei lógica para que, assim que um utilizador se regista, o Django o coloque imediatamente no grupo `autores` usando `Group.objects.get_or_create(name='autores')`. A conta entra logo com login automático (`login(request, user)`).
* **Proteção de Edição Mútua:** Para evitar que o "Autor A" apague ou edite artigos do "Autor B", implementei uma verificação crítica na `artigo_editar`: `if artigo.autor != request.user: return HttpResponseForbidden(...)`.
* **Likes:** Em vez de criar uma tabela complexa para guardar quem deu like, adicionei um simples campo `likes = models.IntegerField(default=0)` no modelo `Artigo`, permitindo que mesmo utilizadores anónimos (sem login) possam gostar das publicações.
* **Comentários Relacionais:** Criei o modelo `Comentario` associado ao `Artigo` por `ForeignKey`. No template `detalhe.html`, a caixa de texto para comentar está protegida por um `{% if request.user.is_authenticated %}`. Visitantes anónimos vêem os comentários, mas não podem escrever.

### Erros Identificados na App Artigos
* **Erro Estrutural de Ciclos no HTML:** * **Problema:** Erro `NoReverseMatch with arguments '('',)' not found`. Ocorreu quando tentei reciclar o código dos botões de Editar/Apagar para as Competências e Formações.
  * **Correção:** O erro indicava que o ID estava vazio. Percebi que estava a colocar os botões fora do ciclo `{% for %}`, onde a variável ainda não existia. Movi-os para dentro do ciclo e funcionou perfeitamente.
* **Erro de Navegação Ausente:**
  * **Problema:** Ao testar a app, recebi `NoReverseMatch for 'artigos_lista'`.
  * **Correção:** A rota principal da lista de artigos estava comentada (inativa) no `artigos/urls.py`. Ao ativar a linha, o link no menu de navegação do Portfólio conseguiu finalmente mapear a página corretamente.