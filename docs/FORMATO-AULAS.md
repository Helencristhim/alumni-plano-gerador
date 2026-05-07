# Formato de Aulas Alumni — Padrão Definitivo

> Este documento define a estrutura OBRIGATÓRIA de exercícios e conteúdo
> para TODOS os materiais gerados. Nenhuma aula pode ser entregue sem
> seguir estas etapas na ordem descrita.

---

## PARTE 1 — PRE-CLASS (exercícios individuais do aluno)

O Pre-class é o material que o aluno faz ANTES da aula. Deve preparar vocabulário, gramática e pronúncia para que o tempo de aula seja maximizado em produção oral.

### Etapa 1.1 — Apresentação Inicial do Vocabulário (Matching)

Apresentação de vocabulário através de exercício de **matching** com 8 a 12 palavras. Pode mesclar palavras do vocabulário e expressões úteis relacionadas ao tema. O exercício deve ser todo em **inglês** (palavra em inglês → tradução em português).

**Regras:**
- Mínimo 8, máximo 12 palavras/expressões
- Incluir mix de palavras isoladas E expressões (ex: "IT Manager", "based in", "deal with")
- Opções EMBARALHADAS (resposta nunca na mesma posição)
- Palavras sempre com inicial MAIÚSCULA
- HTML: `checkMatch(this)` + `verifyAllMatches(id)`

---

### Etapa 1.2 — Apresentação de Gramática (Texto/Diálogo + Quiz)

A gramática é apresentada através de **elicitação**: um texto de até 15 linhas OU diálogo curto, seguido de perguntas focadas na aplicação da gramática. O aluno descobre a regra pelo contexto antes de receber a explicação.

**Regras:**
- Texto contextualizado no tema da aula e no universo profissional do aluno
- 3-5 perguntas de múltipla escolha sobre o uso da gramática NO texto
- Feedback automático (correto/incorreto em tempo real)
- HTML: `selectQuiz(this)` com `data-correct="true/false"`
- As perguntas testam COMPREENSÃO da estrutura, não tradução

---

### Etapa 1.3 — Explicação Gramatical (Bilíngue)

Texto explicativo de como a gramática funciona, com exemplos. **Sempre bilíngue**: explicação em inglês primeiro, depois em português.

**Regras:**
- Explicação clara e concisa (não acadêmica)
- Exemplos contextualizados no universo profissional do aluno
- Incluir "Business Tip" ou "Professional Tip" quando aplicável
- Referências: British Council, Cambridge Dictionary, BBC Learning English
- Formato: seção estática (não é exercício interativo)

---

### Etapa 1.4 — Aplicação da Gramática (Fill-in-the-Blanks)

O aluno aplica os conceitos gramaticais em 4-5 frases de fill-in-the-blanks.

**Regras:**
- 4-5 frases no mínimo
- O aluno DIGITA a resposta (não múltipla escolha)
- Se errar, tem acesso à resposta correta (feedback imediato)
- Frases contextualizadas no tema da aula
- HTML: `checkBlank(this)` com `data-answer` e `data-hint`

---

### Etapa 2 — Prática de Vocabulário (Fill-in com Word Cloud)

Prática com exercício de "complete as frases" contemplando TODAS as palavras e expressões da Etapa 1.1. Apresentar sempre a **nuvem de palavras embaralhadas** que serão utilizadas.

**Regras:**
- Uma frase para CADA palavra/expressão do vocabulário (8-12 frases)
- Nuvem de palavras visível acima do exercício
- Frases contextualizadas no universo profissional do aluno
- HTML: `checkBlank(this)` com word bank visível
- Gabarito no Teacher's Guide (não visível para o aluno)

---

### Etapa 3 — Treino de Pronúncia

Frases úteis com TODAS as palavras-chave do vocabulário, respeitando o contexto do tema. Com possibilidade de alteração de velocidade dos áudios: **0.25x, 0.5x e 1x**.

**Regras:**
- 5-8 frases usando as palavras-chave em contexto
- Cada frase tem botão "Ouvir" com áudio ElevenLabs
- Controle de velocidade (0.25x, 0.5x, 1x)
- Tradução em português abaixo de cada frase
- HTML: `speakPhrase(this)` + `startRecording(this)` + `stopRecording(this)`

**Feedback de pronúncia OBRIGATÓRIO (ver detalhes em REFERENCIA-FAAP.md):**
- Função `analyzeWords` com LCS + Levenshtein para comparação word-by-word
- Feedback visual: WORD-BY-WORD (esperado) + YOU SAID (falado) + Focus on (erros)
- Playback: MediaRecorder grava em paralelo, aluno pode se ouvir após análise
- Detecção de mimeType: `audio/mp4` (Safari) > `audio/webm` (Chrome)
- Regex: `/[^a-z0-9' ]/g` com espaço LITERAL. Split: `/ +/` com espaço LITERAL (nunca `\s`)

---

### Etapa 4 — Produção Controlada (Quiz de Situações)

Quiz com até 5 perguntas situacionais, usando situações do contexto profissional do aluno e vocabulário previamente trabalhado.

**Regras:**
- 5 perguntas de múltipla escolha (A/B/C/D)
- Cada pergunta apresenta uma SITUAÇÃO profissional realista
- O aluno escolhe a resposta mais adequada
- Testar uso correto de vocabulário + gramática em contexto
- HTML: `selectQuiz(this)` com `data-correct`

---

### Etapa 5 — Produção Livre (Roleplay com Gravação)

O aluno pratica respondendo perguntas de um diálogo contextualizado. Pode gravar suas respostas e, ao finalizar, comparar com a resposta sugerida.

**Regras:**
- Diálogo de 3-5 turnos com interlocutor fictício
- Cada turno do interlocutor é dado (texto + áudio)
- O aluno grava sua resposta
- Após gravar, aparece a "Resposta Sugerida" com áudio para comparação
- Inclui explicação breve de "Por que funciona"
- HTML: `startFreeRecording(this)` + speech-card com sugestão

---

## PARTE 2 — IN-CLASS (Material do Professor para tela compartilhada)

O Material do Professor é o conteúdo exibido na tela durante a aula via Zoom/Meet. O professor segue este material enquanto conduz a aula.

### Etapa 1 — Warm-up (5-10 min)

3-5 perguntas abertas relacionadas ao tema. NÃO é teste — é conversa que prepara o cérebro. Não precisa de áudio (professor lê as perguntas).

**Regras:**
- 3-5 perguntas abertas em inglês
- Relacionadas ao tema da aula
- Tom casual e acolhedor
- SEM exercício interativo (é conversa oral)
- Perguntas na tela para o professor usar como guia visual

---

### Etapa 2 — Vocabulário e Gramática (25-30 min)

Apresentar conteúdo novo baseado no pre-class, contextualizado no tema.

#### 2a. Pre-teach (5 min)
- Selecionar até 6 palavras-chave do pre-class (as mais desafiadoras para o nível)
- Flashcards, imagens ou matching com significado em INGLÊS
- Palavras com inicial MAIÚSCULA

#### 2b. Aplicação (5 min)
- Fill-in-the-blanks com word bank (nuvem de palavras embaralhadas)
- 5-6 frases contextualizadas
- DIFERENTES das frases do pre-class (mesmo vocabulário, frases novas)

#### 2c. Teach — Conteúdo Principal (10-15 min)
- Texto, diálogo ou vídeo diretamente relacionado à gramática do pre-class
- Sequência de perguntas:
  - **Step 1:** 1 pergunta geral sobre o conteúdo ("Who are the people?")
  - **Step 2:** 1 pergunta específica de gramática + 3 perguntas gerais
  - **Step 3:** Até 3 exercícios de fixação gramatical (matching, fill-in, sorting)

---

### Etapa 3 — Produção Menos Controlada (15-20 min)

Scaffolding: fornecer estruturas e vocabulário, mas permitir complementação livre. O aluno trabalha indiretamente com as estruturas.

**Formatos possíveis:**
- Completar texto sobre si mesmo/colega (Create Your Story)
- Adaptar diálogo modelo com informações pessoais
- Preencher formulário/e-mail com dados reais
- Descrever imagem usando vocabulário da aula

---

### Etapa 4 — Produção Livre (15-20 min)

Até 3 cenários sem apoio do material: role-play, debate, apresentação curta, storytelling. O aluno performa seguindo as estruturas sem interferência.

**Regras:**
- Instruções claras do cenário na tela
- Possibilidades de resposta, scripts e informações no **Teacher's Guide APENAS**
- NÃO expor respostas esperadas para o aluno
- Professor anota erros para correção posterior (delayed feedback)

---

### Etapa 5 — Wrap-up (5 min)

- Checklist "O que eu aprendi" (8+ itens em primeira pessoa)
- Survival Card progressivo
- Homework
- Reforço positivo

---

## Validação Antes do Deploy

- [ ] Pre-class tem todas as 5 etapas (1.1 matching, 1.2 grammar quiz, 1.3 explicação, 1.4 fill-in, 2 word cloud, 3 pronúncia, 4 quiz situacional, 5 roleplay)
- [ ] In-class tem todas as 4 etapas (warm-up, vocab+grammar, produção controlada, produção livre)
- [ ] Matching tem 8-12 palavras/expressões
- [ ] Fill-in da Etapa 2 usa TODAS as palavras do matching
- [ ] Quiz situacional tem 5 perguntas
- [ ] Pronúncia tem 5-8 frases com controle de velocidade
- [ ] Produção livre tem 3-5 turnos de diálogo com gravação
- [ ] Palavras de vocabulário com inicial MAIÚSCULA
- [ ] Material do Professor tem exercícios DIFERENTES do Pre-class
- [ ] Teacher's Guide tem respostas esperadas (não visível ao aluno)
