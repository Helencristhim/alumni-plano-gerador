# Alumni Plano Gerador — Regras do Sistema

> **REGRA ZERO**: Este documento e AUTOCONTIDO. Voce NAO precisa ler nenhum arquivo de aluno existente como referencia. Tudo que voce precisa para gerar material perfeito esta aqui.

---

## ARQUITETURA DO PROJETO

```
alumni-plano-gerador/
├── public/
│   ├── professor/{slug}.html    ← Material do professor (5 abas)
│   ├── aluno/{slug}.html        ← Material do aluno (2 abas, derivado do professor)
│   ├── audio/{slug}/            ← MP3s ElevenLabs
│   ├── styles/design-system.css ← Design system global
│   ├── lib/supabase-config.js   ← Supabase client
│   ├── dashboard.html           ← Painel de alunos
│   ├── index.html               ← Formulario de intake
│   └── perfil.html              ← Perfil 360
├── api/                         ← Serverless functions (Vercel)
├── docs/                        ← Documentacao pedagogica
└── vercel.json                  ← Config de deploy
```

---

## REGRA 1 — PROFESSOR E BASE, ALUNO E DERIVADO

1. **Professor tem 5 abas**: Planejamento, Pre-class, Plano de Aula, Material do Professor, Complementares
2. **Aluno tem 2 abas**: Pre-class, Complementares (conteudo IDENTICO ao professor)
3. Sempre criar o professor PRIMEIRO, depois extrair o aluno
4. NUNCA editar o aluno diretamente — sempre via professor
5. As 4 abas de conteudo devem ter: MESMO vocabulario, MESMA gramatica, MESMO tema
   - Pre-class PREPARA (primeiro contato do aluno)
   - Plano de Aula GUIA (roteiro para o professor)
   - Material Professor APROFUNDA (tela compartilhada na aula)
   - Complementares REFORCAM (exposicao passiva fora de aula)

---

## REGRA 2 — ESTRUTURA DO ARQUIVO PROFESSOR (5 ABAS)

### HTML base do professor:

```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Alumni — {Nome} — Professor</title>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=Cormorant+Garamond:wght@400;500;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="/styles/material.css">
    <style>
        /* Paleta UNICA deste aluno — NUNCA reusar entre alunos */
        :root {
            --accent: {COR_PRINCIPAL};      /* ex: #0d7377 */
            --accent-light: {COR_CLARA};    /* ex: #14919b */
            --accent-dim: rgba(..., 0.08);
            --accent-glow: rgba(..., 0.05);
            --black: #1a1a2e;
            --bg: #f5f5f0;
            --bg-card: #ffffff;
            --bg-elevated: #f0f0eb;
            --bg-input: #fafaf7;
            --border: #d4d4cc;
            --border-light: #c0c0b8;
            --white: #1a1a2e;
            --text: #2d2d3a;
            --text-mid: #4a4a5a;
            --text-dim: #5c5c6c;
            --success: #16a34a;
            --success-bg: rgba(22,163,74,0.08);
            --success-border: rgba(22,163,74,0.25);
            --danger: #dc2626;
            --danger-bg: rgba(220,38,38,0.08);
            --danger-border: rgba(220,38,38,0.25);
            --warn: #d97706;
            --warn-bg: rgba(217,119,6,0.08);
            --warn-border: rgba(217,119,6,0.25);
        }
    </style>
</head>
<body>
    <!-- Logo bar -->
    <div class="logo-bar">
        <img src="/assets/logo-alumni.png" alt="Alumni by Better">
        <span class="view-badge">PROFESSOR VIEW</span>
    </div>

    <!-- Hero header com imagem de fundo -->
    <div class="header" style="background-image:url(...)">
        <div class="header-overlay"></div>
        <div class="header-content">
            <div class="passport-badge">{PROGRAMA} — {N} Aulas</div>
            <h1>{NOME DO ALUNO}</h1>
            <p class="subtitle">{Descricao curta do programa}</p>
            <div class="student-info">
                <span>{Cidade}</span><span>{Nivel CEFR}</span>
                <span>{Profissao}</span><span>{Duracao}</span>
            </div>
            <div class="progress-bar">...</div>
            <div class="stamps-row"><!-- 5 stamps desbloqueados por progresso --></div>
        </div>
    </div>

    <!-- Container principal -->
    <div class="container">
        <!-- Speed control -->
        <div class="speed-control">
            <button class="speed-btn" onclick="setAudioSpeed(0.5,this)">0.5x</button>
            <button class="speed-btn" onclick="setAudioSpeed(0.75,this)">0.75x</button>
            <button class="speed-btn active" onclick="setAudioSpeed(1,this)">1x</button>
            <button class="speed-btn" onclick="setAudioSpeed(1.25,this)">1.25x</button>
        </div>

        <!-- Tabs -->
        <div class="tabs">
            <button class="tab-btn active" onclick="switchTab('planning')">Planejamento</button>
            <button class="tab-btn" onclick="switchTab('exercises')">Pre-class</button>
            <button class="tab-btn" onclick="switchTab('plan')">Plano de Aula</button>
            <button class="tab-btn" onclick="switchTab('teacher')">Material do Professor</button>
            <button class="tab-btn" onclick="switchTab('complementary')">Complementares</button>
        </div>

        <!-- 5 tab containers -->
        <div class="tab-content active" id="tab-planning">...</div>
        <div class="tab-content" id="tab-exercises">...</div>
        <div class="tab-content" id="tab-plan">...</div>
        <div class="tab-content" id="tab-teacher">...</div>
        <div class="tab-content" id="tab-complementary">...</div>
    </div>

    <script>
        // audioMap, switchTab, toggleLesson, speakText, speakPhrase,
        // checkBlank, checkMatch, selectQuiz, startRecording, etc.
    </script>
</body>
</html>
```

### Conteudo de cada aba:

#### ABA 1 — Planejamento
- Grid de informacoes do aluno (nome, idade, cidade, profissao, nivel, foco, frequencia, total aulas)
- Journey Box: narrativa de transformacao ("De: X" → "Para: Y")
- Promise Box: promessa transformadora do programa
- Grid Forcas/Fraquezas: analise pedagogica
- Tabela curricular: TODAS as aulas com colunas (#, Tema, Foco Linguistico, Atividade Principal, Homework)
- Cards de metodologia (5 abordagens)
- Mapa de personalidade (7 eixos)

#### ABA 2 — Pre-class (Exercicios individuais do aluno)
- Welcome card (onboarding, 5 frases de emergencia com audio)
- N lesson cards colapsaveis (1 por aula, ate 5 por bloco)
- Cada lesson card contem as 5 etapas obrigatorias (ver REGRA 4)
- Survival card ao final de cada aula (5 frases-chave com audio)
- Celebration card (exibido ao atingir 100%)

#### ABA 3 — Plano de Aula (Roteiro do professor)
- Lesson cards colapsaveis
- Tabela PPP com colunas: Tempo, Fase, Atividade Detalhada
- Fases: WARM-UP → VOCAB DEEP-DIVE → CONTEXT/DIALOGUE → GRAMMAR + CCQs → CONTROLLED PRACTICE → SEMI-FREE PRACTICE → FREE PRODUCTION → WRAP-UP
- CCQ Box: perguntas de verificacao conceitual
- Obstacle Alerts: 3 alertas pedagogicos com solucoes
- Teacher Tips: orientacoes de pronuncia com IPA
- Homework Box: 3 tarefas por aula
- Duracao padrao: 90 minutos (exceto criancas 5-12: 30 min)

#### ABA 4 — Material do Professor (Tela compartilhada)
- Material SEM traducoes (somente ingles na tela)
- Vocabulario com exemplos + audio
- Dialogos rotulados por personagem
- Grammar Focus em formato tabela
- Oral Drilling (situacoes numeradas)
- Listening Comprehension
- Sentence Building
- Role-Play Scenarios

#### ABA 5 — Complementares
- Media grid com cards de conteudo
- 3 recomendacoes por aula (serie/filme + podcast + YouTube)
- Cada media card tem: checkbox de conclusao, tipo, titulo, descricao, dica de uso
- Organizado por categorias tematicas relacionadas ao foco do aluno

---

## REGRA 3 — ESTRUTURA DO ARQUIVO ALUNO (2 ABAS)

O aluno recebe APENAS:
- **Aba 1: Pre-class** (identico a aba 2 do professor)
- **Aba 2: Complementares** (identico a aba 5 do professor)

Badge do header: `ALUNO` (em vez de `PROFESSOR VIEW`)

---

## REGRA 4 — 5 ETAPAS OBRIGATORIAS POR AULA (Pre-class)

Cada aula no Pre-class DEVE conter estas 5 etapas, nesta ordem:

### Etapa 1: Vocabulario + Expressoes
- **1.1 Vocab Cards** com audio (`speakText`) + traducao
- **1.2 Matching** (dropdown `checkMatch`) — opcoes EMBARALHADAS
- **1.3 Contexto** — texto curto usando o vocabulario + quiz de compreensao (`selectQuiz`)
- **1.4 Explicacao Gramatical** — bilingue (EN + PT-BR)
- **1.5 Aplicacao** — fill-in-the-blank (`checkBlank`) com hints e audio

### Etapa 2: Pratica de Vocabulario
- Word cloud com fill-in-the-blank avancado
- Ou ordering (`checkOrder`)

### Etapa 3: Pronuncia
- Speech cards com `speakPhrase` + `startRecording` + `stopRecording`
- Feedback word-by-word obrigatorio (ver REGRA 8)

### Etapa 4: Quiz Situacional
- Multiple choice (`selectQuiz`) com contextos profissionais/pessoais do aluno

### Etapa 5: Producao Livre
- Think card com prompt de reflexao
- Sugestao de resposta com comparacao
- Gravacao livre (`startFreeRecording` / `stopFreeRecording`)

---

## REGRA 5 — EXERCICIOS: SEMPRE HTML MANUAL, NUNCA data-exercise

**PROIBIDO**: `<div data-exercise="matching">` ou qualquer atributo `data-exercise`

**OBRIGATORIO**: HTML manual com funcoes inline. Tipos de exercicio:

### A. Matching (dropdown)
```html
<div class="match-grid" id="match-l1">
    <div class="match-row" data-answer="apresentacao">
        <span class="match-word">introduction</span>
        <select onchange="checkMatch(this)">
            <option value="">Select...</option>
            <option value="gerenciar">gerenciar</option>
            <option value="apresentacao">apresentacao</option>
        </select>
    </div>
</div>
<button class="verify-all-btn" onclick="verifyAllMatches('match-l1')">Check Answers</button>
```

### B. Fill-in-the-blank
```html
<div class="fill-blank-item">
    <div class="fill-blank-sentence">
        "Let me give you a quick
        <input class="blank-input"
               data-answer="introduction"
               data-hint="Hint: formal presentation"
               data-phrase="Let me give you a quick introduction about myself."
               placeholder="___">
        about myself."
    </div>
    <button class="check-btn" onclick="checkBlank(this)">Check</button>
    <button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button>
</div>
```

### C. Quiz (multiple choice)
```html
<div class="quiz-item">
    <div class="quiz-question">What would you say at a conference?</div>
    <div class="quiz-options">
        <div class="quiz-option" onclick="selectQuiz(this)" data-correct="false">
            <span class="option-letter">A</span> "I do computer things."
        </div>
        <div class="quiz-option" onclick="selectQuiz(this)" data-correct="true">
            <span class="option-letter">B</span> "I'm an IT Manager..."
        </div>
    </div>
</div>
```

### D. Ordering
```html
<div class="order-container" id="order-l1">
    <div class="order-item" draggable="true" data-order="1" onclick="selectOrderItem(this,'order-l1')">
        <span class="order-num">?</span>
        <span class="order-text">"Hi, I'm Daniela."</span>
        <span class="order-arrows">
            <button class="arrow-btn" onclick="moveItem(this,-1,'order-l1')">&#9650;</button>
            <button class="arrow-btn" onclick="moveItem(this,1,'order-l1')">&#9660;</button>
        </span>
    </div>
</div>
<button class="verify-all-btn" onclick="checkOrder('order-l1')">Check Order</button>
```

### E. Pronuncia (speech card)
```html
<div class="speech-card" data-phrase="Hi, I'm Daniela. Nice to meet you.">
    <div class="speech-phrase">Hi, I'm Daniela. Nice to meet you.</div>
    <div class="speech-translation">Oi, eu sou a Daniela. Prazer.</div>
    <div class="speech-controls">
        <button class="btn btn-listen" onclick="speakPhrase(this)">&#9654; Ouvir</button>
        <button class="btn btn-record" onclick="startRecording(this)">&#9679; Gravar</button>
        <button class="btn btn-stop" onclick="stopRecording(this)">&#9632; Parar</button>
    </div>
    <div class="speech-result"></div>
</div>
```

### F. Think (reflexao + gravacao livre)
```html
<div class="think-card">
    <div class="think-question">Imagine you are at a conference...</div>
    <div class="speech-controls">
        <button class="btn btn-record" onclick="startFreeRecording(this)">&#9679; Gravar Livre</button>
        <button class="btn btn-stop" onclick="stopFreeRecording(this)">&#9632; Parar</button>
    </div>
    <div id="think-result-1"></div>
</div>
```

---

## REGRA 6 — BADGES POR TIPO DE EXERCICIO

```html
<span class="badge badge-vocab">Vocabulary</span>
<span class="badge badge-practice">Practice</span>
<span class="badge badge-speak">Speaking</span>
<span class="badge badge-quiz">Quiz</span>
<span class="badge badge-order">Order</span>
<span class="badge badge-think">Reflection</span>
<span class="badge badge-media">Media</span>
```

---

## REGRA 7 — AUDIO MAP + ELEVENLABS

Cada arquivo deve ter um `audioMap` no `<script>` mapeando frases para MP3:

```javascript
const audioMap = {
    "Hi, I am Daniela. Nice to meet you.": "/audio/daniela-feitoza/hi_i_am_daniela_nice_to_meet_you.mp3",
    "I manage the IT department.": "/audio/daniela-feitoza/i_manage_the_it_department.mp3",
    // ... TODAS as frases com speakText/data-phrase
};
```

- **Voz**: Arthur (American English) via ElevenLabs
- **Formato**: MP3
- **Diretorio**: `/audio/{slug}/`
- **Nomenclatura**: frase em snake_case sem acentos, max 60 chars
- **Fallback**: Web Speech API (speechSynthesis) APENAS como fallback, NUNCA como metodo principal
- **Speed control**: `currentAudio.playbackRate = audioSpeed`

---

## REGRA 8 — PRONUNCIA (startRecording)

A funcao `startRecording` DEVE implementar:

1. **SpeechRecognition** (Web Speech API) com `lang='en-US'`
2. **MediaRecorder** para playback do audio gravado
   - Iniciar DENTRO de `getUserMedia().then()`
   - `mimeType`: testar `audio/mp4` primeiro (Safari), depois `audio/webm;codecs=opus` (Chrome)
   - `start(100)` para chunks frequentes
   - Blob criado NO callback `onstop` (nunca antes)
3. **`analyzeWords(targetStr, spokenStr)`** obrigatorio:
   - LCS (Longest Common Subsequence) + Levenshtein distance
   - Tolerancia: <=1 edit distance para palavras >3 chars
   - Score = matched_words / total_target_words
4. **Feedback visual word-by-word**:
   - `.word-correct` (verde) — palavra acertada
   - `.word-wrong` (vermelho, line-through) — palavra errada
   - `.word-missing` (laranja, italico) — palavra faltante
   - `.word-extra` (cinza) — palavra extra falada
5. **Resultado**:
   - `>=80%`: `.speech-result.good` (verde)
   - `50-80%`: `.speech-result.try-again` (laranja)
   - `<50%`: `.speech-result.bad` (vermelho)
   - "Focus on: [palavras erradas]"
6. **REGEX**: `/[^a-z0-9' ]/g` com espaco LITERAL (NUNCA `\s`)
7. **SPLIT**: `.split(/ +/)` com espaco LITERAL (NUNCA `/\s+/`)

---

## REGRA 9 — JAVASCRIPT OBRIGATORIO

Toda pagina de material DEVE incluir estas funcoes no `<script>`:

```
switchTab(tabId)           — Alternar entre abas
toggleLesson(header)       — Expandir/colapsar lesson card
setAudioSpeed(speed, btn)  — Mudar velocidade de audio
speakText(text, btn)       — Tocar audio do audioMap ou TTS fallback
speakPhrase(btn)           — Tocar audio do data-phrase do card pai
listenBlank(btn)           — Tocar audio do data-phrase do input pai
listenAllVocab(btn)        — Tocar todos os vocab cards sequencialmente
checkMatch(select)         — Validar matching individual
verifyAllMatches(gridId)   — Validar todos os matches de um grid
checkBlank(btn)            — Validar fill-in-the-blank
selectQuiz(option)         — Selecionar opcao de quiz
selectOrderItem(item, id)  — Selecionar item de ordering
checkOrder(containerId)    — Validar ordering
moveItem(btn, dir, id)     — Mover item para cima/baixo
startRecording(btn)        — Iniciar speech recognition + MediaRecorder
stopRecording(stopBtn)     — Parar recording
analyzeWords(target, spoken) — Comparar palavras (LCS)
wordsMatch(a, b)           — Comparar 2 palavras (fuzzy)
levenshtein(a, b)          — Edit distance
startFreeRecording(btn)    — Gravar sem comparacao
stopFreeRecording(stopBtn) — Parar gravacao livre
updateProgress()           — Calcular progresso por aula e geral
saveState()                — Salvar estado em localStorage
loadState()                — Restaurar estado do localStorage
toggleMediaDone(checkbox)  — Marcar media como assistida
```

---

## REGRA 10 — PALETA DE CORES UNICA POR ALUNO

Cada aluno DEVE ter uma paleta de cores DIFERENTE. Definida no `:root` do arquivo.

Exemplos:
- Daniela (Professional): `--accent: #0d7377` (teal)
- Maisa (Business): `--accent: #946B2D` (dourado)
- Zilaudio (Travel): tema escuro com dourado

Cores fixas Alumni (usadas em TODOS): `#003080` (azul), `#d70c0c` (vermelho), `#f5f5f0` (fundo)

---

## REGRA 11 — CHECKLIST FINAL BLOQUEANTE (PRE-DEPLOY)

NENHUM material e "pronto" sem passar por TODOS os 5 checks:

1. **Portugues/Acentuacao** — Zero palavras sem acento correto nas traducoes
2. **Ingles** — Gramatica perfeita, American English 100%
3. **Nivel x Aula** — Conteudo adequado ao CEFR do aluno
4. **Audios ElevenLabs** — TODAS as frases com `speakText`/`data-phrase` tem MP3 no `audioMap`. ZERO fallback Web Speech como metodo principal
5. **Funcionalidade** — Zero `data-exercise`. HTML manual com checkBlank/selectQuiz/etc.

Se QUALQUER check falhar → REJEITAR → corrigir → re-validar → so entao deploy.

---

## REGRA 12 — MATERIAIS ATIVOS SAO INTOCAVEIS

- NUNCA modificar HTMLs de alunos com status ATIVO no dashboard
- NUNCA remover funcoes existentes de `design-system.css`
- NUNCA renomear funcoes JS existentes
- Mudancas sao testadas em materiais novos PRIMEIRO
- So migrar materiais ativos quando EXPLICITAMENTE pedido

---

## REGRA 13 — ADAPTACAO POR NIVEL CEFR

| Nivel | Vocabulario | Traducao | Frases | Gramatica |
|-------|------------|----------|--------|-----------|
| A0-A1 | 5-7 palavras/aula | 100% bilingue | 3-5 palavras | Presente simples, to be |
| A2 | 8-10 palavras/aula | 80% bilingue | 5-7 palavras | Past simple, can/could |
| B1 | 10-12 palavras/aula | 50% bilingue | 7-10 palavras | Present perfect, modals |
| B2 | 12-15 palavras/aula | 30% bilingue | 10-15 palavras | Conditionals, passive |
| C1+ | 15-20 palavras/aula | Minimo | Complexas | Nuances, register |

---

## REGRA 14 — ADAPTACAO POR IDADE

| Idade | Duracao | Tom | Exercicios |
|-------|---------|-----|------------|
| 5-12 | 30 min | Ludico, visual | Jogos, cores, imagens |
| 13-17 | 45-60 min | Dinamico, pop culture | Memes, series, musica |
| 18-30 | 60-90 min | Profissional direto | Cases, situacoes reais |
| 31-50 | 60-90 min | Respeitoso, pratico | Contexto de trabalho |
| 50+ | 60-90 min | Calmo, paciente | Repeticao, ritmo lento |

---

## REGRA 15 — LESSON CARD (ACCORDION)

```html
<div class="lesson-card" id="ex-lesson-1">
    <div class="lesson-header" onclick="toggleLesson(this)">
        <div class="lesson-header-img" style="background-image:url(...)"></div>
        <div class="lesson-header-content">
            <div class="lesson-number">Aula 01 — Pre-class</div>
            <h3>{Titulo da aula}</h3>
            <div class="lesson-desc">{Descricao}</div>
            <div class="lesson-progress-mini">
                <div class="mini-bar"><div class="mini-bar-fill" data-lesson-progress="1" style="width:0%"></div></div>
                <span class="mini-percent" data-lesson-pct="1">0%</span>
            </div>
        </div>
        <div class="expand-icon">&#9660;</div>
    </div>
    <div class="lesson-body">
        <!-- Etapas 1-5 aqui (exercicios) -->
        <!-- Survival card ao final -->
    </div>
</div>
```

---

## REGRA 16 — SURVIVAL CARD

Ao final de cada aula, incluir card com 5 frases-chave + audio:

```html
<div class="survival-card">
    <h4>Survival Card — Lesson {N}</h4>
    <div class="survival-phrase">
        <span class="sp-num">1</span>
        <span class="sp-en">Hi, I'm Daniela. Nice to meet you.</span>
        <span class="sp-pt">Oi, sou a Daniela. Prazer.</span>
        <button class="btn btn-listen" onclick="speakText('Hi, I am Daniela. Nice to meet you.', this)">&#9835;</button>
    </div>
</div>
```

---

## REGRA 17 — MEDIA CARDS (Complementares)

3 recomendacoes por aula: serie/filme + podcast + YouTube

```html
<div class="media-card-wrapper" data-media="l1-series">
    <label class="media-check">
        <input type="checkbox" onchange="toggleMediaDone(this)">
    </label>
    <div class="media-card">
        <div class="media-thumb">{emoji}</div>
        <div class="media-info">
            <div class="media-type">Serie</div>
            <h5>Suits — Season 1, Episode 1</h5>
            <p>Descricao e por que assistir</p>
            <p class="media-tip">Dica: assista com legenda em ingles</p>
        </div>
    </div>
</div>
```

---

## REGRA 18 — PROGRESS TRACKING

- Contar exercicios corretos por aula (blanks, quizzes, matches, speech, orders)
- Calcular % por aula e % geral
- Atualizar barras de progresso + stamps
- Salvar em `localStorage` com chave `alumni-progress-{slug}`
- Exibir celebration card ao atingir 100%

---

## REGRA 19 — DEPLOY AUTOMATICO

Apos qualquer mudanca de codigo, rodar `npx vercel --prod --yes` automaticamente.
NAO perguntar "quer que eu faca deploy?" — apenas faca.

---

## REGRA 20 — NUNCA ALTERAR MATERIAIS ATIVOS

Materiais de alunos com status ATIVO no dashboard NUNCA podem ser alterados sem pedido EXPLICITO.
Melhorias sao testadas em materiais novos primeiro.

---

## REGRA 21 — INGLES AMERICANO

Todo conteudo em ingles deve seguir American English: spelling, vocabulary, pronunciation.
- "color" (nao "colour"), "organize" (nao "organise"), "apartment" (nao "flat")

---

## REGRA 22 — VOCABULARIO NAO REPETE

Palavras/expressoes ensinadas como conteudo NOVO em uma aula NUNCA aparecem como conteudo novo em aulas posteriores. Podem ser REVISADAS, mas nao apresentadas como novidade.

---

## REGRA 23 — CCQs OBRIGATORIOS

Concept Checking Questions devem estar ESCRITAS no material do professor (Plano de Aula), nao apenas mencionadas. Formato: pergunta + resposta esperada.

---

## REGRA 24 — MATCHING EMBARALHADO

As opcoes do dropdown de matching DEVEM estar em ordem DIFERENTE da ordem das palavras. NUNCA na mesma posicao.

---

## REGRA 25 — MOBILE-FIRST

Todo material deve ser responsivo e funcional em celular. Touch targets minimos de 44x44px. Ordering deve ter botoes de seta alem de drag-and-drop.

---

## REGRA 26 — JAVASCRIPT COMPLETO (COPIAR INTEGRALMENTE)

> **CRITICO**: O bloco abaixo DEVE ser copiado INTEGRALMENTE para todo material gerado. NAO reinventar, NAO simplificar, NAO omitir funcoes. Trocar apenas: o audioMap (frases do aluno), o slug no localStorage/IndexedDB, e o numero de totalLessons.

```javascript
// ===== TAB SWITCHING =====
function switchTab(tabId) {
    document.querySelectorAll('.tab-content').forEach(t => t.classList.remove('active'));
    document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
    document.getElementById('tab-' + tabId).classList.add('active');
    event.currentTarget.classList.add('active');
    window.scrollTo({ top: 0, behavior: 'smooth' });
}

// ===== LESSON EXPAND/COLLAPSE =====
function toggleLesson(header) { header.parentElement.classList.toggle('open'); }

// ===== AUDIO MAP (SUBSTITUIR com frases do aluno) =====
const audioMap = {
    // "Frase exata": "/audio/{slug}/nome_do_arquivo.mp3",
};

// ===== SPEAK TEXT (Audio + Fallback TTS) =====
let currentAudio = null;
let audioSpeed = parseFloat(localStorage.getItem('alumni-audio-speed') || '1');

function setAudioSpeed(speed, btn) {
    audioSpeed = speed;
    localStorage.setItem('alumni-audio-speed', speed);
    document.querySelectorAll('.speed-btn').forEach(function(b) {
        b.style.background = 'var(--bg-card)'; b.style.color = 'var(--text)';
        b.style.borderColor = 'var(--border)'; b.style.fontWeight = '400';
    });
    btn.style.background = 'var(--accent)'; btn.style.color = '#fff';
    btn.style.borderColor = 'var(--accent)'; btn.style.fontWeight = '600';
}

document.addEventListener('DOMContentLoaded', function() {
    var saved = parseFloat(localStorage.getItem('alumni-audio-speed') || '1');
    var btn = document.querySelector('.speed-btn[data-speed="' + saved + '"]');
    if (btn) setAudioSpeed(saved, btn);
});

function speakText(text, btn) {
    if (currentAudio) { currentAudio.pause(); currentAudio.currentTime = 0; }
    var cleanText = text.replace(/\\'/g, "'");
    var file = audioMap[cleanText] || audioMap[cleanText.replace(/\.$/, '')] || audioMap[cleanText + '.'];
    if (file) {
        currentAudio = new Audio(file);
        currentAudio.playbackRate = audioSpeed;
        currentAudio.play().catch(function() {
            if ("speechSynthesis" in window) {
                window.speechSynthesis.cancel();
                var u = new SpeechSynthesisUtterance(cleanText);
                u.lang = "en-US"; u.rate = audioSpeed * 0.85; u.pitch = 1;
                window.speechSynthesis.speak(u);
            }
        });
    } else {
        if ("speechSynthesis" in window) {
            window.speechSynthesis.cancel();
            var u = new SpeechSynthesisUtterance(cleanText);
            u.lang = "en-US"; u.rate = audioSpeed * 0.85; u.pitch = 1;
            window.speechSynthesis.speak(u);
        }
    }
}

function speakPhrase(btn) {
    var card = btn.closest('.speech-card');
    if (card) speakText(card.dataset.phrase, btn);
}

// ===== SPEECH RECOGNITION =====
var activeRecognition = null;

function startRecording(btn) {
    var SR = window.SpeechRecognition || window.webkitSpeechRecognition;
    if (!SR) { alert('Please use Google Chrome for voice recognition.'); return; }
    var card = btn.closest('.speech-card');
    var target = card.dataset.phrase.toLowerCase().replace(/[^a-z0-9' ]/g, '');
    var resultDiv = card.querySelector('.speech-result');
    var stopBtn = card.querySelector('.btn-stop');
    if (btn.classList.contains('recording')) return;
    btn.classList.add('recording', 'hidden');
    stopBtn.classList.add('visible');
    var r = new SR();
    r.lang = 'en-US'; r.interimResults = false; r.maxAlternatives = 3; r.continuous = true;
    activeRecognition = { recognition: r, btn: btn, stopBtn: stopBtn, card: card };
    r.start();
    function resetButtons() { btn.classList.remove('recording', 'hidden'); stopBtn.classList.remove('visible'); activeRecognition = null; }
    r.onresult = function(event) {
        var best = event.results[event.results.length - 1][0].transcript.toLowerCase().replace(/[^a-z0-9' ]/g, '');
        var analysis = analyzeWords(target, best);
        var totalWords = analysis.expected.length;
        var correctWords = analysis.expected.filter(function(w) { return w.status === 'correct'; }).length;
        resultDiv.classList.add('show'); resultDiv.classList.remove('good', 'try-again', 'bad');
        var html = '';
        if (analysis.score >= 0.8) { resultDiv.classList.add('good'); html += '<strong>Score: ' + correctWords + '/' + totalWords + '</strong> &mdash; Excellent!'; updateProgress(); }
        else if (analysis.score >= 0.5) { resultDiv.classList.add('try-again'); html += '<strong>Score: ' + correctWords + '/' + totalWords + '</strong> &mdash; Almost there!'; }
        else { resultDiv.classList.add('bad'); html += '<strong>Score: ' + correctWords + '/' + totalWords + '</strong> &mdash; Keep practicing!'; }
        html += '<div class="word-comparison"><div class="comp-label">Word-by-word:</div><div class="comp-words">';
        analysis.expected.forEach(function(w) { html += '<span class="word-box word-' + (w.status === 'correct' ? 'correct' : 'missing') + '"><span class="word-icon">' + (w.status === 'correct' ? '&#10003;' : '&#10007;') + '</span> ' + w.word + '</span>'; });
        html += '</div><div class="comp-label">You said:</div><div class="comp-words">';
        analysis.spoken.forEach(function(w) {
            var cls = w.status === 'correct' ? 'correct' : w.status === 'extra' ? 'extra' : 'wrong';
            var icon = w.status === 'correct' ? '&#10003;' : w.status === 'extra' ? '~' : '&#10007;';
            html += '<span class="word-box word-' + cls + '"><span class="word-icon">' + icon + '</span> ' + w.word + '</span>';
        });
        html += '</div>';
        if (analysis.wrongWords.length > 0) {
            html += '<div class="speech-suggestion"><strong>Focus on:</strong> ';
            html += analysis.wrongWords.map(function(w) { return '"<strong>' + w.expected + '</strong>"' + (w.got ? ' (you said "' + w.got + '")' : ''); }).join(' &middot; ');
            html += '</div>';
        }
        html += '</div>';
        resultDiv.innerHTML = html;
        resetButtons();
    };
    r.onerror = function() { resetButtons(); resultDiv.classList.add('show', 'try-again'); resultDiv.innerHTML = 'Could not hear you. Check your microphone.'; };
    r.onend = function() { resetButtons(); };
    setTimeout(function() { if (btn.classList.contains('recording')) { r.stop(); resetButtons(); } }, 30000);
}

function stopRecording(stopBtn) { if (activeRecognition) activeRecognition.recognition.stop(); }

// ===== WORD ANALYSIS (LCS + Levenshtein) =====
function analyzeWords(targetStr, spokenStr) {
    var tw = targetStr.split(/ +/).filter(function(w) { return w; });
    var sw = spokenStr.split(/ +/).filter(function(w) { return w; });
    var m = tw.length, n = sw.length;
    var dp = Array.from({ length: m + 1 }, function() { return Array(n + 1).fill(0); });
    for (var i = 1; i <= m; i++) for (var j = 1; j <= n; j++) dp[i][j] = wordsMatch(tw[i-1], sw[j-1]) ? dp[i-1][j-1] + 1 : Math.max(dp[i-1][j], dp[i][j-1]);
    var mt = new Set(), ms = new Set(); var i = m, j = n;
    while (i > 0 && j > 0) { if (wordsMatch(tw[i-1], sw[j-1])) { mt.add(i-1); ms.add(j-1); i--; j--; } else if (dp[i-1][j] > dp[i][j-1]) i--; else j--; }
    var expected = tw.map(function(w, i) { return { word: w, status: mt.has(i) ? 'correct' : 'missing' }; });
    var spoken = sw.map(function(w, i) { return { word: w, status: ms.has(i) ? 'correct' : 'wrong' }; });
    var wrongWords = [], missedTW = tw.filter(function(_, i) { return !mt.has(i); }), wrongSW = sw.filter(function(_, i) { return !ms.has(i); });
    missedTW.forEach(function(t, i) { wrongWords.push({ expected: t, got: wrongSW[i] || null }); });
    wrongSW.slice(missedTW.length).forEach(function(s) { spoken.forEach(function(sp) { if (sp.word === s && sp.status === 'wrong') sp.status = 'extra'; }); });
    return { expected: expected, spoken: spoken, wrongWords: wrongWords, score: mt.size / Math.max(m, 1) };
}

function wordsMatch(a, b) { if (a === b) return true; var ca = a.replace(/'/g, ''), cb = b.replace(/'/g, ''); if (ca === cb) return true; if (a.length > 3 && b.length > 3 && levenshtein(a, b) <= 1) return true; return false; }
function levenshtein(a, b) { var m = []; for (var i = 0; i <= b.length; i++) m[i] = [i]; for (var j = 0; j <= a.length; j++) m[0][j] = j; for (var i = 1; i <= b.length; i++) for (var j = 1; j <= a.length; j++) m[i][j] = b[i-1] === a[j-1] ? m[i-1][j-1] : Math.min(m[i-1][j-1] + 1, m[i][j-1] + 1, m[i-1][j] + 1); return m[b.length][a.length]; }

// ===== FILL-IN-THE-BLANK =====
function checkBlank(btn) {
    var item = btn.closest('.fill-blank-item'), input = item.querySelector('.blank-input');
    input.classList.remove('correct', 'wrong');
    var answer = input.dataset.answer.toLowerCase().trim();
    var altAnswer = input.dataset.alt ? input.dataset.alt.toLowerCase().trim() : null;
    var value = input.value.toLowerCase().trim();
    var hintEl = item.querySelector('.blank-hint-feedback');
    if (hintEl) hintEl.classList.remove('visible');
    if (value === answer || (altAnswer && value === altAnswer)) {
        input.classList.add('correct');
        if (hintEl) hintEl.classList.remove('visible');
        updateProgress();
    } else {
        input.classList.add('wrong');
        if (input.dataset.hint) {
            if (!hintEl) { hintEl = document.createElement('div'); hintEl.className = 'blank-hint-feedback'; item.appendChild(hintEl); }
            hintEl.textContent = input.dataset.hint; hintEl.classList.add('visible');
        }
        setTimeout(function() { input.classList.remove('wrong'); }, 1500);
    }
}

function listenBlank(btn) {
    var item = btn.closest('.fill-blank-item'), input = item.querySelector('.blank-input');
    if (input.dataset.phrase) speakText(input.dataset.phrase, btn);
}

// ===== QUIZ =====
function selectQuiz(o) {
    var p = o.closest('.quiz-options'); if (p.querySelector('.correct')) return;
    if (o.dataset.correct === 'true') { o.classList.add('correct'); updateProgress(); }
    else { o.classList.add('wrong'); setTimeout(function() { o.classList.remove('wrong'); }, 800); }
}

// ===== ORDER EXERCISE =====
var orderSelection = {};
function selectOrderItem(item, containerId) {
    if (item.classList.contains('correct-order')) return;
    if (!orderSelection[containerId]) orderSelection[containerId] = [];
    var idx = orderSelection[containerId].indexOf(item);
    if (idx > -1) { orderSelection[containerId].splice(idx, 1); item.querySelector('.order-num').textContent = '?'; item.style.borderColor = ''; }
    else { orderSelection[containerId].push(item); item.querySelector('.order-num').textContent = orderSelection[containerId].length; item.style.borderColor = 'var(--accent)'; }
}

function checkOrder(containerId) {
    var container = document.getElementById(containerId);
    var items = container.querySelectorAll('.order-item');
    var selected = orderSelection[containerId] || [];
    if (selected.length !== items.length) { alert('Select all items in the correct order.'); return; }
    var allCorrect = true;
    selected.forEach(function(item, idx) {
        if (parseInt(item.dataset.order) === idx + 1) { item.classList.add('correct-order'); item.querySelector('.order-num').textContent = idx + 1; }
        else { allCorrect = false; item.style.borderColor = 'var(--danger)'; item.classList.add('wrong'); setTimeout(function() { item.classList.remove('wrong'); item.style.borderColor = ''; item.querySelector('.order-num').textContent = '?'; }, 1000); }
    });
    if (!allCorrect) orderSelection[containerId] = [];
    else updateProgress();
}

function moveItem(btn, direction, containerId) {
    var item = btn.closest('.order-item');
    var container = document.getElementById(containerId);
    var items = Array.from(container.querySelectorAll('.order-item'));
    var idx = items.indexOf(item);
    if (direction === -1 && idx > 0) container.insertBefore(item, items[idx - 1]);
    else if (direction === 1 && idx < items.length - 1) container.insertBefore(items[idx + 1], item);
}

// ===== DRAG AND DROP =====
var draggedItem = null;
document.querySelectorAll('.order-container').forEach(function(container) {
    container.addEventListener('dragstart', function(e) { var item = e.target.closest('.order-item'); if (!item || item.classList.contains('correct-order')) return; draggedItem = item; item.classList.add('dragging'); e.dataTransfer.effectAllowed = 'move'; });
    container.addEventListener('dragend', function(e) { var item = e.target.closest('.order-item'); if (item) item.classList.remove('dragging'); container.querySelectorAll('.order-item').forEach(function(i) { i.classList.remove('drag-over'); }); draggedItem = null; });
    container.addEventListener('dragover', function(e) { e.preventDefault(); e.dataTransfer.dropEffect = 'move'; var target = e.target.closest('.order-item'); if (target && target !== draggedItem) { container.querySelectorAll('.order-item').forEach(function(i) { i.classList.remove('drag-over'); }); target.classList.add('drag-over'); } });
    container.addEventListener('drop', function(e) { e.preventDefault(); var target = e.target.closest('.order-item'); if (target && draggedItem && target !== draggedItem) { var items = Array.from(container.querySelectorAll('.order-item')); if (items.indexOf(draggedItem) < items.indexOf(target)) container.insertBefore(draggedItem, target.nextSibling); else container.insertBefore(draggedItem, target); } container.querySelectorAll('.order-item').forEach(function(i) { i.classList.remove('drag-over'); }); });
});

// ===== FREE RECORDING =====
var freeRecorder = null;
var freeChunks = [];
function startFreeRecording(btn) {
    var stopBtn = btn.parentElement.querySelector('.btn-stop');
    navigator.mediaDevices.getUserMedia({ audio: true }).then(function(stream) {
        var mimeType = MediaRecorder.isTypeSupported('audio/mp4') ? 'audio/mp4' : MediaRecorder.isTypeSupported('audio/webm;codecs=opus') ? 'audio/webm;codecs=opus' : '';
        freeRecorder = mimeType ? new MediaRecorder(stream, { mimeType: mimeType }) : new MediaRecorder(stream);
        freeChunks = [];
        freeRecorder.ondataavailable = function(e) { if (e.data.size > 0) freeChunks.push(e.data); };
        freeRecorder.onstop = function() {
            var blob = new Blob(freeChunks, { type: freeRecorder.mimeType });
            var url = URL.createObjectURL(blob);
            var thinkCard = btn.closest('.think-card');
            var resultDiv = thinkCard.querySelector('[id^="think-result"]');
            if (resultDiv) resultDiv.innerHTML = '<audio controls src="' + url + '" style="width:100%;margin-top:0.5rem;"></audio><p style="font-size:0.72rem;color:var(--success);margin-top:0.3rem;">Gravacao salva!</p>';
            stream.getTracks().forEach(function(t) { t.stop(); });
        };
        freeRecorder.start(100);
        btn.classList.add('hidden');
        stopBtn.classList.add('visible');
    }).catch(function() { alert('Nao foi possivel acessar o microfone.'); });
}

function stopFreeRecording(stopBtn) {
    if (freeRecorder && freeRecorder.state === 'recording') freeRecorder.stop();
    var recordBtn = stopBtn.parentElement.querySelector('.btn-record');
    recordBtn.classList.remove('hidden');
    stopBtn.classList.remove('visible');
}

// ===== CHECKLIST =====
function toggleChecklist(cb) {
    var li = cb.closest('li');
    if (cb.checked) li.classList.add('checked'); else li.classList.remove('checked');
    updateProgress();
}

// ===== PROGRESS TRACKING =====
// SUBSTITUIR: totalLessons pelo numero de aulas do bloco
// SUBSTITUIR: slug no localStorage.setItem
function updateProgress() {
    var totalLessons = 5; // ← AJUSTAR por aluno
    var completedLessons = 0;
    for (var l = 1; l <= totalLessons; l++) {
        var cl = document.getElementById('checklist-' + l);
        if (!cl) continue;
        var allChecks = cl.querySelectorAll('input[type="checkbox"]');
        var checkedChecks = cl.querySelectorAll('input[type="checkbox"]:checked');
        var lessonPct = allChecks.length > 0 ? Math.round(checkedChecks.length / allChecks.length * 100) : 0;
        var bar = document.querySelector('[data-lesson-progress="' + l + '"]');
        var lbl = document.querySelector('[data-lesson-pct="' + l + '"]');
        if (bar) bar.style.width = lessonPct + '%';
        if (lbl) lbl.textContent = lessonPct + '%';
        var stampEl = document.getElementById('stamp' + l);
        if (stampEl) { if (lessonPct === 100) stampEl.classList.add('earned'); else stampEl.classList.remove('earned'); }
        if (allChecks.length > 0 && checkedChecks.length === allChecks.length) completedLessons++;
    }
    var overallPct = Math.round(completedLessons / totalLessons * 100);
    var pb = document.getElementById('progressBar');
    var pp = document.getElementById('progressPercent');
    if (pb) pb.style.width = overallPct + '%';
    if (pp) pp.textContent = overallPct + '%';
    var celCard = document.getElementById('celebrationCard');
    if (celCard) celCard.style.display = overallPct === 100 ? 'block' : 'none';
    try { localStorage.setItem('alumni-progress-{SLUG}', JSON.stringify({ concluidas: completedLessons, total: totalLessons })); } catch(e) {}
    saveState();
}

// ===== STATE PERSISTENCE =====
// SUBSTITUIR: '{SLUG}-professor' ou '{SLUG}-aluno' conforme o arquivo
function saveState() {
    var s = { dropdowns: [], blanks: [], quiz: [], speech: [], checklists: {}, mediaChecks: {}, matches: [] };
    document.querySelectorAll('.media-card-wrapper').forEach(function(w) { var id = w.dataset.media; var cb = w.querySelector('input[type="checkbox"]'); if (id && cb) s.mediaChecks[id] = cb.checked; });
    document.querySelectorAll('.match-row.correct select').forEach(function(sel) { s.matches.push(sel.closest('.match-row').querySelector('.match-word').textContent + '|' + sel.value); });
    document.querySelectorAll('.blank-input.correct').forEach(function(e) { s.blanks.push(e.dataset.answer); });
    document.querySelectorAll('.quiz-option.correct').forEach(function(e) { s.quiz.push(e.textContent.trim().substring(0, 30)); });
    document.querySelectorAll('.speech-result.good').forEach(function(e) { s.speech.push(e.closest('.speech-card').dataset.phrase); });
    document.querySelectorAll('.checklist input[type="checkbox"]').forEach(function(cb, i) { s.checklists[i] = cb.checked; });
    localStorage.setItem('{SLUG}-professor', JSON.stringify(s));
}

function loadState() {
    var r = localStorage.getItem('{SLUG}-professor'); if (!r) return;
    var s = JSON.parse(r);
    if (s.matches) s.matches.forEach(function(d) { var parts = d.split('|'); var word = parts[0]; var val = parts[1]; document.querySelectorAll('.match-row').forEach(function(row) { if (row.querySelector('.match-word').textContent === word) { var sel = row.querySelector('select'); sel.value = val; row.classList.add('correct'); sel.disabled = true; } }); });
    if (s.blanks) s.blanks.forEach(function(a) { document.querySelectorAll('.blank-input[data-answer="' + a + '"]').forEach(function(e) { e.value = a; e.classList.add('correct'); }); });
    if (s.quiz) s.quiz.forEach(function(t) { document.querySelectorAll('.quiz-option[data-correct="true"]').forEach(function(e) { if (e.textContent.trim().substring(0, 30) === t) e.classList.add('correct'); }); });
    if (s.checklists) { document.querySelectorAll('.checklist input[type="checkbox"]').forEach(function(cb, i) { if (s.checklists[i]) { cb.checked = true; cb.closest('li').classList.add('checked'); } }); }
    if (s.mediaChecks) { document.querySelectorAll('.media-card-wrapper').forEach(function(w) { var id = w.dataset.media; var cb = w.querySelector('input[type="checkbox"]'); if (id && cb && s.mediaChecks[id]) { cb.checked = true; w.classList.add('done'); } }); }
    updateProgress();
}

function resetProgress() { if (confirm('Resetar todo o progresso?')) { localStorage.removeItem('{SLUG}-professor'); location.reload(); } }

// ===== LISTEN ALL VOCAB =====
function listenAllVocab(btn) {
    var section = btn.closest('.exercise-section') || btn.closest('.teacher-section');
    var audioBtns = section.querySelectorAll('.vocab-card .audio-btn');
    var i = 0;
    function playNext() { if (i < audioBtns.length) { audioBtns[i].click(); i++; setTimeout(playNext, 2500); } }
    playNext();
}

// ===== VERIFY ALL MATCHES =====
function verifyAllMatches(gridId) {
    var grid = document.getElementById(gridId);
    var rows = grid.querySelectorAll('.match-row');
    rows.forEach(function(row) {
        var select = row.querySelector('select');
        var answer = row.dataset.answer;
        row.classList.remove('correct', 'wrong');
        if (select.value === answer) { row.classList.add('correct'); }
        else if (select.value !== '') { row.classList.add('wrong'); setTimeout(function() { row.classList.remove('wrong'); }, 1800); }
    });
    updateProgress();
}

function checkMatch(select) {
    var row = select.closest('.match-row');
    var answer = row.dataset.answer;
    row.classList.remove('correct', 'wrong');
    if (select.value === answer) { row.classList.add('correct'); select.disabled = true; updateProgress(); }
    else if (select.value !== '') { row.classList.add('wrong'); setTimeout(function() { row.classList.remove('wrong'); select.value = ''; }, 1000); }
}

// ===== MEDIA CHECKBOXES =====
function toggleMediaDone(checkbox) {
    var wrapper = checkbox.closest('.media-card-wrapper');
    wrapper.classList.toggle('done', checkbox.checked);
    saveState();
}

// ===== INIT =====
loadState();

// Accessibility
document.querySelectorAll('.match-row select').forEach(function(sel) {
    var word = sel.closest('.match-row').querySelector('.match-word');
    if (word) sel.setAttribute('aria-label', 'Translation of ' + word.textContent);
});
```

### Variaveis para substituir ao gerar material:

| Placeholder | Substituir por |
|---|---|
| `{SLUG}` | Slug do aluno (ex: `daniela-feitoza`) |
| `audioMap = {}` | Mapa completo de frases → MP3 |
| `totalLessons = 5` | Numero de aulas do bloco |
| `'{SLUG}-professor'` | Chave localStorage (ex: `daniela-feitoza-professor` ou `daniela-feitoza-aluno`) |
