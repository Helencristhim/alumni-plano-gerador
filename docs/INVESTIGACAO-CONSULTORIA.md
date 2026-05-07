# Investigacao da Consultoria — O que a IA Analisa

> Documento de referencia tecnica para o pipeline de analise pedagogica.
> Referenciado por: `api/perfil-360.js`

---

## Visao Geral

A consultoria e o momento mais rico de dados que temos sobre o aluno.
Acontece ao vivo, com professor treinado, e gera tres camadas de informacao:
dados declarados (formulario), dados observados (transcricao) e dados inferidos
(cruzamento das duas camadas anteriores pelo modelo de IA).

A IA nao e um extrator de palavras-chave. E um analisador pedagogico senior
que cruza dados declarados + observados + inferidos para produzir um perfil
360 graus do aluno.

---

## O que a IA Recebe

### 1. Transcricao completa da consultoria

- Texto integral da sessao, incluindo falas do professor e do aluno.
- Trechos em ingles e em portugues sao mantidos no idioma original.
- Timestamps aproximados quando disponiveis (ajudam a medir hesitacao).
- A transcricao e a fonte primaria — tudo que o aluno de fato disse.

### 2. Observacoes estruturadas do professor

O professor preenche um formulario de observacao com os seguintes campos:

| Campo               | Descricao                                                        |
|---------------------|------------------------------------------------------------------|
| Tom geral           | Confiante, timido, ansioso, entusiasmado, neutro                 |
| Cadencia de fala    | Rapida, moderada, lenta, irregular                               |
| Energia             | Alta, media, baixa, oscilante                                    |
| Hesitacoes          | Frequentes, pontuais, raras, ausentes                            |
| Postura corporal    | Aberta, fechada, inquieta, relaxada                              |
| Momentos de animacao| Topicos ou perguntas que geraram entusiasmo visivel              |
| Momentos de travamento | Topicos ou perguntas onde o aluno travou, desviou ou encolheu |

### 3. Dados do formulario (declarados pelo gestor)

- Nivel declarado (A1-C2 ou descricao informal)
- Foco principal (business, viagem, academico, social, etc.)
- Perfil profissional (cargo, area, setor)
- Objetivos declarados (o que o gestor/aluno diz que quer)
- Historico de estudo (cursos anteriores, tempo estudando)
- Disponibilidade (horas por semana, preferencia de horario)
- Urgencia (prazo, evento, meta corporativa)

---

## A) Validacao dos Dados Declarados pelo Gestor

A IA compara cada dado declarado com a evidencia da transcricao e das
observacoes do professor. Para cada item, emite um selo de validacao:

| Selo | Significado | Acao                                                       |
|------|-------------|------------------------------------------------------------|
| 🟢   | Confirma    | Dado declarado e consistente com evidencia observada       |
| 🟡   | Ajusta      | Dado declarado e proximo mas precisa de refinamento        |
| 🟠   | Sinaliza    | Dado declarado tem divergencia relevante com a evidencia   |
| 🔴   | Contradiz   | Dado declarado contradiz diretamente a evidencia observada |

### Exemplos de validacao

- **Nivel declarado: Intermediario** — Se o aluno nao conseguiu formar frases
  simples no passado, o selo sera 🟠 ou 🔴 com sugestao de nivel real.
- **Foco: Business** — Se o aluno so falou de viagem e familia na consultoria,
  o selo sera 🟡 com nota sobre foco hibrido.
- **Perfil: Extrovertido** — Se as observacoes do professor indicam postura
  fechada e hesitacoes frequentes em ingles, o selo sera 🟠.

### Campos validados

1. Nivel de ingles (comparado com vocabulario e estruturas usadas)
2. Foco principal (comparado com topicos de energia na transcricao)
3. Perfil de personalidade (comparado com observacoes do professor)
4. Objetivos (comparados com urgencia e motivacao real)
5. Disponibilidade (comparada com rotina descrita na conversa)

---

## B) Captacao que So a Transcricao Revela

Esta secao extrai informacoes que nenhum formulario consegue capturar.

### B.1 Frases textuais ipsis litteris do aluno (3-5)

A IA seleciona de 3 a 5 frases exatas ditas pelo aluno que revelam
personalidade, motivacao, medo ou objetivo real. Essas frases sao usadas
depois na justificativa do programa e na promessa transformadora.

Exemplo: *"Eu travo quando tem gringo na call, mesmo sabendo o vocabulario"*

### B.2 Vocabulario em ingles que o aluno usa naturalmente

Palavras e expressoes em ingles que o aluno inseriu espontaneamente durante
a conversa em portugues. Isso revela o nivel real de absorcao do idioma,
independente do que foi declarado.

- Palavras isoladas (meeting, deadline, feedback)
- Expressoes compostas (follow up, to be honest)
- Jargao tecnico da area (deploy, sprint, compliance)
- Collocations corretas ou incorretas

### B.3 Frases em ingles que o aluno errou

Quando o aluno tentou falar em ingles e cometeu erros, esses erros sao
catalogados por tipo:

- Erros de estrutura (word order, subject-verb agreement)
- Erros de vocabulario (false friends, wrong word choice)
- Erros de pronuncia (anotados pelo professor)
- Erros de registro (formal vs informal inadequado)

### B.4 Padroes de fala em portugues

Como o aluno fala em portugues revela muito sobre como vai aprender ingles:

- Palavras de muleta ("tipo", "ne", "basicamente", "enfim")
- Regionalismos (sotaque, expressoes locais)
- Tom predominante (formal, coloquial, tecnico, narrativo)
- Complexidade das frases (simples, compostas, subordinadas)

### B.5 Topicos de energia vs obrigacao

| Alta energia (interesse genuino)     | Baixa energia (obrigacao)              |
|--------------------------------------|----------------------------------------|
| Topicos onde o aluno se anima        | Topicos onde o aluno responde no minimo|
| Fala mais rapido, ri, dá exemplos    | Respostas curtas, desvia, muda assunto |
| Inclina pra frente, gesticula        | Postura recuada, olha pro lado         |

---

## C) Inferencia Baseada em Observacoes do Professor

Cruzando as observacoes do professor com a transcricao, a IA infere:

### C.1 Tolerancia a erro real

Nao o que o aluno diz ("erro faz parte do aprendizado") mas como ele
de fato reage ao errar durante a consultoria. Classificacao:

- **Alta:** Ri do erro, se corrige, segue em frente
- **Media:** Pausa brevemente, pede confirmacao, continua
- **Baixa:** Para de falar, muda pra portugues, pede desculpa
- **Muito baixa:** Evita arriscar, so fala o que tem certeza

### C.2 Estilo de aprendizagem real

- **Analitico:** Quer regras, tabelas, logica gramatical
- **Comunicativo:** Quer conversar, errar, improvisar
- **Visual:** Responde melhor a exemplos escritos, quadros
- **Auditivo:** Responde melhor a frases faladas, musica, podcasts
- **Cinestesico:** Precisa de roleplay, simulacao, movimento

### C.3 Energia preferida

- **Alta intensidade:** Gosta de desafio, pressao positiva, ritmo rapido
- **Moderada:** Gosta de equilibrio entre desafio e conforto
- **Baixa intensidade:** Precisa de ambiente seguro, ritmo calmo, encorajamento

### C.4 Postura emocional sobre ingles

- **Positiva:** Ve ingles como oportunidade, investe com vontade
- **Neutra:** Ve ingles como necessidade pratica, sem emocao forte
- **Ansiosa:** Quer aprender mas tem medo de errar, julgamento
- **Resistente:** Estuda por obrigacao externa, resistencia interna
- **Traumatizada:** Experiencias negativas anteriores, bloqueio emocional

---

## D) Analise Pedagogica que Requer Expertise Senior

A partir de todas as camadas anteriores, a IA produz:

### D.1 Resumo executivo

Paragrafo unico (3-5 frases) que sintetiza quem e o aluno, o que precisa
e qual a melhor abordagem. Escrito para o coordenador pedagogico.

### D.2 Mapa de personalidade (7 eixos)

Cada eixo e uma escala de 1 a 10:

1. **Extroversao** (1 = introvertido, 10 = extrovertido)
2. **Abertura a erro** (1 = perfeccionista, 10 = experimentador)
3. **Autonomia** (1 = guiado, 10 = autodidata)
4. **Formalidade** (1 = casual, 10 = corporativo)
5. **Velocidade** (1 = lento e profundo, 10 = rapido e amplo)
6. **Emocionalidade** (1 = racional, 10 = emocional)
7. **Motivacao** (1 = extrinseca/obrigacao, 10 = intrinseca/desejo)

### D.3 Forcas e melhorias

- **Forcas:** 3-5 pontos fortes observados (ex: vocabulario tecnico solido)
- **Melhorias:** 3-5 gaps prioritarios (ex: estrutura de frases no passado)

### D.4 Necessidades pedagogicas (8 sub-campos)

1. **Gramatica prioritaria** — Estruturas que precisam de atencao imediata
2. **Vocabulario foco** — Areas lexicas essenciais para o objetivo
3. **Pronuncia** — Sons, ritmo, entonacao que precisam de trabalho
4. **Listening** — Tipo de audio que o aluno precisa treinar
5. **Speaking** — Situacoes de fala que precisam de simulacao
6. **Reading** — Generos textuais relevantes para o contexto
7. **Writing** — Tipos de texto que o aluno precisa produzir
8. **Soft skills em ingles** — Apresentacao, negociacao, small talk, etc.

### D.5 Indicacao de professor

Perfil ideal do professor para este aluno:
- Energia compativel
- Estilo de correcao adequado
- Background profissional relevante
- Genero/idade (quando relevante para conforto do aluno)

### D.6 Justificativa do programa

Texto de 2-3 paragrafos explicando por que o programa recomendado e o
ideal para este aluno, usando evidencias da consultoria (incluindo frases
ipsis litteris da secao B.1).

### D.7 Promessa transformadora

Frase unica, concreta, mensuravel, que descreve o resultado esperado
ao final do programa. Exemplo: *"Em 6 meses, voce vai liderar reunioes
em ingles sem precisar de script."*

---

## Principio Fundamental

> A IA NAO e extrator de palavras. E analisador pedagogico senior que
> cruza dados declarados + observados + inferidos para produzir um
> diagnostico completo, humano e acionavel.

A qualidade do plano depende diretamente da qualidade desta analise.
Cada campo existe por um motivo pedagogico. Nenhum campo e decorativo.

---

## Referencias Tecnicas

- Endpoint: `api/perfil-360.js`
- Input: JSON com transcricao, observacoes, formulario
- Output: JSON com todas as secoes acima preenchidas
- Modelo: GPT-4 com prompt pedagogico especializado
- Tempo medio de processamento: 15-30 segundos
