# Diário de Bordo: Processo de Modelação do Portfólio

Este documento regista a evolução, as decisões e os erros corrigidos durante a fase de modelação da base de dados do projeto de Portfólio em Django

## 1. Fotografias do DER e Apontamentos
 O planemaneto foi feito em papel e colocado no ficheiro dock_makingOf que tem uma pasta chamda imagens_papel. As imagens mostram todo o planemante antes de passar para o codigo no computador, diretorio:
* `docs_makingOf/imagens_papel/`


## 2. Evolução do Modelo e Correção de Erros

Vou descrever entao erros e correçoes ao longo deste processo no papel

* **Versão 1 (Rascunho Inicial):**

* **Versão 1 (Rascunho Inicial):**
  * **Erro Identificado:** Reparei que o primeiro rascunho deixava algumas entidades (como as Formações e os Interesses) desconectadas do resto do modelo, o que iria dificultar o cruzamento de dados na aplicação.
  * **Correção:** Atualizei as relações no diagrama para que todas as tabelas fizessem parte da mesma rede. A `Licenciatura` passou a agregar todo o percurso académico, enquanto as `Competencias` passaram a cruzar a informação ganha tanto nos `Projetos` como nas `Formações`.


* **Versão 2 (Ajuste de Relações e Guião):**
  * **Erro Identificado 1:** A relação inicial planeada entre `Licenciatura` e `TFC` era de 1:N (um curso tem muitos TFCs). No entanto, num contexto de portfólio pessoal, isto estava incorreto a meu ver porque a minha licenciatura apenas me permite ter um TFC.
  * **Correção 1:** Alterei a modelação no Django para um `OneToOneField`, garantindo que, no meu percurso, a minha licenciatura culmina num único Trabalho Final de Curso.
  * **Erro Identificado 2:** Faltavam atributos obrigatórios definidos nos requisitos (ex: imagens, links de repositório, datas).
  * **Correção 2:** Adicionei campos rigorosos (`ImageField` para logos/imagens, `URLField` para o GitHub oficial e páginas docentes, e `DateField` para ordenação cronológica das formações).

## 3. Justificação das Decisões de Modelação

Abaixo explico as decisões técnicas para a construção de cada tabela, focadas em manter a base de dados limpa e pronta para o Frontend:

**1. Licenciatura**
* *Porquê Raiz?:* Defini a Licenciatura como a base de tudo. Usar `CASCADE` nas UCs garante que não ficam dados "órfãos" na base de dados se o curso for apagado.
* *Controlo de Dados:* Os ECTS e a duração usam `PositiveIntegerField` para a base de dados bloquear automaticamente qualquer tentativa de inserir valores negativos.

**2. Docente**
* *Tabela Independente:* Criei uma entidade separada em vez de apenas um campo de texto na UC. Isto resolve o problema real da relação N:M (um professor dá várias cadeiras, uma cadeira tem vários professores).
* *Links Práticos:* O `URLField` serve para ligar diretamente à página oficial do professor na faculdade, facilitando o acesso a quem vir o portfólio.

**3. Unidade Curricular (UC)**
* *Ligação ao Curso:* Usa uma `ForeignKey` para a Licenciatura (relação 1:N) para o sistema saber exatamente a que curso a cadeira pertence.
* *Interface Visual:* O campo `ImageField` foi adicionado para que o Frontend possa mostrar cartões com imagens por disciplina, em vez de listas de texto aborrecidas.

**4. Projeto**
* *O Centro Prático:* É a tabela que cruza mais dados. Liga à UC (1:N), Tecnologias (N:M) e Competências (N:M) para mostrar de forma automática o que fiz, onde fiz e o que aprendi.
* *GitHub Obrigatório:* O link do repositório (`URLField`) é obrigatório porque o código-fonte é a primeira coisa que um recrutador vai querer ver.

**5. Tecnologia**
* *Sem Repetições:* Entidade separada ligada por N:M. Assim escrevo "Python" apenas uma vez e ligo aos vários projetos onde o usei, poupando espaço na base de dados (normalização).
* *Filtros Futuros:* O campo `nivel_preferencia` vai servir para eu conseguir ordenar as tecnologias e colocar as minhas "stacks" favoritas no topo do site.

**6. TFC (Trabalho Final de Curso)**
* *Regra de Negócio:* Usei o `OneToOneField` com a Licenciatura. O meu curso culmina num único TFC, logo a base de dados tem de proibir que se associem dois projetos finais à mesma licenciatura.
* *Destaque no Site:* O campo booleano `destaque` funciona como um "interruptor" para eu conseguir afixar o TFC na página principal do portfólio através do Admin.

**7. Competência**
* *Cruzamento de Dados:* Liga-se em N:M aos Projetos e Formações. É a prova em base de dados de que as minhas "skills" vêm tanto da faculdade como de cursos extra.
* *Organização Visual:* O campo `tipo` permite-me criar secções diferentes (ex: separar Hard Skills de Soft Skills) no currículo digital.

**8. Formação**
* *Fator Tempo:* Usei `DateField` para o início e fim. Ter datas reais permite pedir ao Django que ordene os cursos do mais recente para o mais antigo de forma automática (`order_by`).
* *Ligação à Prática:* A relação direta com as Competências serve para justificar o valor prático da formação que tirei.

**9. Interesse**
* *Focado na Tecnologia:* Em vez de hobbies soltos num texto, os interesses ligam-se diretamente às Tecnologias (N:M) que quero aprender no futuro.
* *Métrica:* O `nivel_interesse` foi pensado para eu futuramente poder criar barras de progresso ou gráficos visuais na interface.

**10. Making Of**
* *Auto-documentação:* Tem uma `ForeignKey` para o Projeto. Como o meu portfólio final é, em si, um projeto Django, eu documento os passos da construção do site diretamente na sua própria base de dados.
* *Registo Honesto:* Campos como `erro_encontrado` e `uso_ia` servem para garantir transparência técnica e cumprir os critérios da avaliação contínua.

## 4. Uso de IA (Inteligência Artificial)
Durante este processo de modelação, utilizei a Inteligência Artificial (Gemini) como um *peer-programmer* e tutor. A IA não gerou a ideia do meu percurso, mas foi fundamental para:
* Validar a normalização do meu diagrama conceptual.
* Sugerir o mapeamento ótimo para o ORM do Django 
* Apoiar no debug dos comandos Git e na estruturação dos tipos de dados exigidos pelo guião da disciplina
* E tambem para me ajudar a escrever 