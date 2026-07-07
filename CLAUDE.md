# Alumni Plano Gerador — Regras do Sistema

> **REGRA ZERO**: Este documento e AUTOCONTIDO. Voce NAO precisa ler nenhum arquivo de aluno existente como referencia. Tudo que voce precisa para gerar material perfeito esta aqui.

> **AVISO CRITICO**: TODAS as regras abaixo sao OBRIGATORIAS e INEGOCIAVEIS. Nenhuma etapa pode ser pulada, simplificada ou omitida por qualquer motivo — incluindo "simplificar", "adaptar ao nivel", "o aluno nao precisa", ou qualquer outra justificativa. Se uma regra diz DEVE, significa que a ausencia e um BUG que BLOQUEIA o deploy. O sistema NAO tem autonomia para decidir quais regras seguir — TODAS se aplicam, SEMPRE, para TODOS os alunos.

---

## ARQUITETURA DO PROJETO

```
alumni-plano-gerador/
├── public/
│   ├── professor/{slug}.html    ← Material do professor (4 abas: Planejamento, Pre-class, IN CLASS, Complementares)
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

1. **Professor tem 4 abas**: Planejamento, Pre-class, IN CLASS, Complementares
2. **Aluno tem 2 abas**: Pre-class, Complementares (conteudo IDENTICO ao professor)
3. Sempre criar o professor PRIMEIRO, depois extrair o aluno
4. NUNCA editar o aluno diretamente — sempre via professor
5. As 3 abas de conteudo devem ter: MESMO vocabulario, MESMA gramatica, MESMO tema
   - Pre-class PREPARA (primeiro contato do aluno, antes da aula)
   - IN CLASS ENTREGA (slides interativos Zoom — a aula acontece aqui, instrucoes ao professor via icone T)
   - Complementares REFORCAM (exposicao passiva fora de aula)

---

## REGRA 2 — ESTRUTURA DO ARQUIVO PROFESSOR (4 ABAS)

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

    <!-- Container principal (main-content) -->
    <div class="container main-content">
        <!-- Speed control -->
        <div class="speed-control">...</div>

        <!-- Tabs -->
        <div class="tabs">
            <button class="tab-btn active" onclick="switchTab('planning')">Planejamento</button>
            <button class="tab-btn" onclick="switchTab('exercises')">Pre-class</button>
            <button class="tab-btn" onclick="switchTab('inclass')">IN CLASS</button>
            <button class="tab-btn" onclick="switchTab('complementary')">Complementares</button>
        </div>

        <!-- 3 tab containers DENTRO do main-content -->
        <div class="tab-content active" id="tab-planning">...</div>
        <div class="tab-content" id="tab-exercises">...</div>
        <div class="tab-content" id="tab-inclass">
            <!-- APENAS o menu de selecao de aulas -->
        </div>
    </div><!-- /main-content FECHA AQUI -->

    <!-- ╔══════════════════════════════════════════════════════════════╗ -->
    <!-- ║  REGRA CRITICA: slides-wrapper DEVE ficar FORA do          ║ -->
    <!-- ║  main-content. O CSS faz body.slide-mode .main-content     ║ -->
    <!-- ║  { display:none }. Se slides-wrapper estiver DENTRO,       ║ -->
    <!-- ║  ele sera escondido junto e o IN CLASS NAO funciona.        ║ -->
    <!-- ╚══════════════════════════════════════════════════════════════╝ -->
    <div class="slides-wrapper" id="slidesWrapper">
        <!-- phase-bar, phase-labels, slides-container, nav-bar -->
        <!-- TODOS os slides ficam aqui -->
    </div>

    <div class="confetti-container" id="confettiContainer"></div>

    <!-- Complementares pode ficar em seu proprio main-content -->
    <div class="container main-content">
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

#### ABA 3 — IN CLASS (Experiencia de aula via Zoom — SLIDES INTERATIVOS)

> **ESTA ABA SUBSTITUI o antigo "Plano de Aula" e "Material do Professor"**. Tudo que o professor precisa esta aqui: o conteudo visual nos slides + as instrucoes via icone T.

> **PRINCIPIO CENTRAL**: A aba IN CLASS e a SALA DE AULA. E o que o professor compartilha na tela do Zoom. NAO e uma pagina com scroll — e uma APRESENTACAO de slides interativos. O aluno vive uma experiencia imersiva.

**FORMATO: SLIDES, NAO PAGINA**
- Sequencia de slides (100vh por slide), NAO pagina com scroll
- Navegacao: setas do teclado (esquerda/direita) + botoes na tela
- Contador de slides no canto: "7 / 30"
- Barra de progresso por capitulos no topo (clicavel)
- Transicoes fade 400ms
- Cada slide tem UM proposito, UM conceito
- Minimo 25-30 slides para 60 min, 35-45 para 90 min
- **MENU DE SELECAO OBRIGATORIO**: A aba IN CLASS NUNCA entra em slide-mode direto. Ao clicar na aba, mostra um menu com cards de cada aula disponivel. O usuario clica na aula desejada e SO ENTAO entra em slide-mode via `enterSlideMode()`. O `switchTab()` SEMPRE faz `document.body.classList.remove('slide-mode')` — NUNCA adiciona slide-mode

**SEPARACAO DE AULAS — REGRAS OBRIGATORIAS (slides multi-aula)**

Quando um material tem mais de 1 aula, os slides de TODAS as aulas ficam no mesmo `slides-wrapper`. Para que cada aula funcione de forma independente, TRES mecanismos sao OBRIGATORIOS:

1. **`data-lesson` em CADA slide**: Todo `<div class="slide">` DEVE ter `data-lesson="N"` indicando a qual aula pertence. Exemplo: `<div class="slide slide-dark" data-slide="28" data-lesson="2" data-phase="1">`. Isso permite auditoria estatica e agrupamento por aula.

2. **`lessonRanges` + filtragem JS**: O JavaScript DEVE conter:
   ```
   var lessonRanges = { 1: {start:1, end:27}, 2: {start:28, end:54}, ... };
   var currentLesson = 1;
   ```
   - `enterSlideMode(startSlide)` detecta a aula pelo startSlide e seta `currentLesson`
   - `changeSlide(dir)` respeita os bounds: `if (next < range.start || next > range.end) return;`
   - `updateNav()` mostra contador RELATIVO a aula ("01 / 27", nao "28 / 135") e esconde dots fora da aula

3. **Menu visual UNIFORME**: Todos os cards do seletor de aula DEVEM seguir o MESMO padrao HTML:
   ```html
   <div style="display:flex;align-items:center;gap:1rem;padding:1.2rem;background:rgba(255,255,255,.5);backdrop-filter:blur(8px);border:1px solid rgba(200,200,190,.5);border-radius:10px;cursor:pointer;transition:all .3s" onclick="enterSlideMode(N)">
     <div style="width:48px;height:48px;background:var(--accent);border-radius:8px;display:flex;align-items:center;justify-content:center;color:#fff;font-weight:700;font-size:1.1rem">01</div>
     <div><div style="font-weight:600;font-size:.95rem">Titulo da Aula</div><div style="font-size:.8rem;color:var(--text-dim)">Descricao -- 27 slides</div></div>
   </div>
   ```
   NUNCA misturar formatos (ex: uns com border-radius:8px e outros com 50%, uns com label "Lesson" e outros sem). Numero sempre com 2 digitos ("01", "02"... "10"). Icone SEMPRE quadrado arredondado (border-radius:8px), NUNCA circular.

**CHECKLIST PRE-DEPLOY (slides multi-aula)**:
- [ ] TODOS os slides tem `data-lesson="N"`?
- [ ] `lessonRanges` cobre TODAS as aulas?
- [ ] Setas do teclado param no limite de cada aula?
- [ ] Contador mostra numero relativo ("01/27"), nao absoluto ("28/135")?
- [ ] TODOS os cards do menu tem o MESMO formato HTML?

**NARRATIVA OBRIGATORIA**
- Toda aula segue uma HISTORIA com titulo e capitulos (ex: "Elaine's First Day in New York")
- 7 capitulos minimos: The Dream (warm-up) > Packing Words (vocab) > The Code (grammar) > Getting There (context) > Practice > Your Turn (production) > Wrap-up
- Slides de transicao entre capitulos com imagem de fundo + titulo

**VOCABULARIO — REVEAL CARDS**
- Grid 2x2 (4 cards por slide, 2 slides = 8 palavras)
- Card FECHADO mostra: icone SVG com gradiente tematico + definicao em INGLES como pista
- Ao CLICAR: revela palavra + definicao + frase de exemplo + botao Listen
- Icones sao SVG inline com gradiente de fundo (NUNCA fotos externas)
- Cada palavra tem cor unica no gradiente (ex: passaporte=azul marinho, emergencia=vermelho)
- Contador visual: "3 / 8 words revealed"

**GRAMATICA — DISCOVERY METHOD**
- NUNCA mostrar a regra primeiro
- Mostrar 3-4 exemplos com estrutura em destaque (cor accent)
- Pergunta: "What do the orange words have in common?"
- Botao "Reveal the Rule" → tabela gramatical com fade-in
- Slide extra "Common Mistake" com comparacao visual (X vermelho vs check verde). Classe `slide-light` (NUNCA slide-dark). Texto DIRETO no div (NUNCA dentro de `<p>` ou `<strong>` — o `display:flex` do `.mistake-item` espalha elementos inline). SVG 24x24 padrão Patricia. Explicação pedagógica em `<p>` EMBAIXO do mistake-card
- Slide de Grammar Practice com fill-in clicaveis (click → revela resposta)

**DIALOGO — LINE BY LINE**
- Dialogo aparece UMA troca por vez (botao "Next Line")
- Fundo escuro estilo cinema/legenda
- Avatar colorido por personagem (ex: Sarah=azul, aluna=terracotta)
- Vocabulario da aula em negrito cor accent
- Audio ElevenLabs por linha com `data-voice` no HTML: `data-voice="ellen"` para personagens femininos, `data-voice="arthur"` para masculinos
- O script de geracao de audio LE o `data-voice` de cada linha para gerar o MP3 com a voz correta automaticamente
- Slide extra de Dialogue Comprehension com 3 perguntas click-to-reveal

**LISTENING — SOUND-FIRST com PLAYER COMPLETO**
- Slide escuro com player de audio completo (NAO apenas botao play simples)
- Player OBRIGATORIO com: seekbar clicavel (barra de progresso), tempo atual/total, botao play/pause, botao voltar 5s, botao avancar 5s
- Controle de velocidade LOCAL ao slide: botoes 0.5x | 0.75x | 1x | 1.25x (independente do controle global do Pre-class)
- Audio toca PRIMEIRO, aluno ouve SEM texto. Perguntas de compreensao aparecem apos audio terminar (audio.ended)
- Audio deve ser MP3 UNICO por listening (nao sequencia de speakText calls). Gerar MP3 completo via ElevenLabs
- Minimo 2 listenings por aula (contextos diferentes)
- Cada slide de Listening E Dialogue tem controle de velocidade independente
- Implementacao: usar `data-src` no container do player apontando para o MP3, inicializar com `initPlayer(id)`, controlar via `togglePlayer(id)`, `skipAudio(id, seconds)`, `seekAudio(event, id)`, `setPlayerSpeed(id, speed)`

**ARTEFATOS REAIS**
- Minimo 1 artefato CSS por aula (boarding pass, hotel confirmation, email, menu, etc.)
- Construidos em HTML/CSS (NUNCA imagem) — com nome do aluno personalizado
- Base para comprehension questions

**QUICK FIRE — UMA PERGUNTA POR VEZ**
- Uma situacao completa por tela, em INGLES (A2+ = zero portugues)
- Botao "Show Answer" → revela → botao "Next Question"
- Score counter: "3 / 6"
- Confetti CSS ao completar todas
- Perguntas situacionais: "You arrive at the hotel. Tell the receptionist you booked a room."

**SPOT THE ERROR**
- Frases com erro em vermelho (line-through)
- Click → correcao em verde
- Score counter

**ROLE-PLAY — SITUATION CARDS**
- 3 niveis obrigatorios: Guided > Semi-free > Free (um slide cada)
- Card visual com gradiente CSS + icone SVG + cenario + keyword chips
- NUNCA fotos externas em role-play — sempre gradientes + SVG
- Keywords como chips com borda accent

**TEACHER CUE SYSTEM (icone "?" flutuante)**
- Cada slide tem icone "?" no canto superior direito
- Click → tooltip escuro com instrucao pro professor
- Click novamente → some
- Conteudo neutro (nunca gabaritos)

**WRAP-UP**
- Survival Card: slide escuro, 5 frases com botao Listen (audio ElevenLabs)
- What I Learned: CHECKBOXES clicaveis (click → verde com checkmark SVG)
- Boarding Pass Earned: badge celebratorio com animacao sparkle
- Closing: slide final com "Day X — Complete" + preview proxima aula

**AUDIO NA ABA IN CLASS**
- 100% ElevenLabs — audioMap deve cobrir TODAS as frases com speakText()
- Vozes: **Arthur** (sfJopaWaOtauCD3HKX6Q) = male, American neutral + **Ellen** (BIvP0GN1cAtSRTxNHnWS) = female, calm American
- Regra de alternancia:
  - Palavras soltas (1-2 palavras) = SEMPRE Arthur
  - Frases (3+ palavras) = ALTERNAR Arthur/Ellen a cada frase
  - Dialogos: Arthur para personagens MASCULINOS, Ellen para personagens FEMININOS (incluindo a propria aluna se for mulher)
  - Survival cards e listening: mesclar ambas vozes
  - NUNCA usar uma unica voz para todo o material
- Atribuicao automatica de voz em dialogos:
  - Todo elemento de dialogo DEVE ter `data-voice="arthur"` ou `data-voice="ellen"`
  - O nome do personagem define a voz: nomes femininos (Sarah, Maria, receptionist feminina) = `data-voice="ellen"`, nomes masculinos (David, John, waiter masculino) = `data-voice="arthur"`
  - O script de geracao de audio LE o atributo `data-voice` para saber qual voz ElevenLabs usar
  - Exemplo: `<div class="dialogue-line" data-voice="ellen">` gera MP3 com Ellen
  - Se o genero do personagem nao for obvio pelo nome, o material DEVE especificar (ex: "Receptionist — female" no Plano de Aula)
- Verificacao pre-deploy: script que compara speakText() calls vs audioMap — ZERO missing permitido
- Web Speech API e EMERGENCIA, nunca principal
- Botoes Listen: fundo solido accent, icone SVG volume + texto "Listen"

**VISUAL — REGRAS ABSOLUTAS**
- Zero emojis — TODOS os icones sao SVG inline (Lucide style)
- Zero imagens externas em cards/componentes — so em backgrounds full-screen (testados 200 OK com gradient overlay fallback)
- Font minimo 0.9rem corpo, 0.8rem labels (legibilidade Zoom)
- Dois tipos de botao: primary (filled accent) + secondary (outlined accent)
- Paleta unica por aluno
- Zero portugues na tela (A2+). Definicoes de vocabulario em INGLES simples

**ICONE T — INSTRUCOES AO PROFESSOR (SUBSTITUI O ANTIGO PLANO DE AULA)**
- NAO existe aba separada de Plano de Aula — tudo esta no icone T de cada slide
- O T DEVE conter para CADA slide: timing sugerido, instrucoes de como conduzir, CCQs quando aplicavel, obstacle alerts, dicas de pronuncia
- Homework: o professor diz ORALMENTE no ultimo slide (nunca aparece escrito na tela IN CLASS)
- O icone T e a UNICA forma do professor receber instrucoes durante a aula — deve ser COMPLETO e DETALHADO
- Cada instrucao e escrita em portugues (para o professor brasileiro)

#### ABA 4 — Complementares
- Media grid com cards de conteudo
- 3 recomendacoes por aula (serie/filme + podcast + YouTube)
- Cada media card tem: checkbox de conclusao, tipo, titulo, descricao, dica de uso
- Organizado por categorias tematicas relacionadas ao foco do aluno

---

## REGRA 3 — ESTRUTURA DO ARQUIVO ALUNO (2 ABAS)

O aluno recebe APENAS:
- **Aba 1: Pre-class** (identico a aba 2 do professor)
- **Aba 2: Complementares** (identico a aba 4 do professor)

Badge do header: `ALUNO` (em vez de `PROFESSOR VIEW`)

---

## REGRA 4 — 5 ETAPAS OBRIGATORIAS POR AULA (Pre-class)

> **ATENCAO**: Esta regra e INVIOLAVEL. TODAS as 5 etapas E TODAS as sub-etapas (1.1 a 1.5) DEVEM existir em CADA aula, para QUALQUER aluno, em QUALQUER nivel. Pular qualquer etapa (especialmente 1.3 e 1.4) e um BUG CRITICO que bloqueia deploy. NAO existe justificativa valida para omitir etapas — nem nivel iniciante, nem falta de tempo, nem "simplificacao". Se o aluno e A1, a gramatica sera simples (to be, present simple) mas DEVE ESTAR LA.

Cada aula no Pre-class DEVE conter estas 5 etapas, nesta ordem:

### Etapa 1: Vocabulario + Expressoes (TODAS as 5 sub-etapas obrigatorias)
- **1.1 Vocab Cards** com audio (`speakText`) + traducao — **OBRIGATORIO**
- **1.2 Matching** (dropdown `checkMatch`) — opcoes EMBARALHADAS — **OBRIGATORIO**
- **1.3 Contexto** — texto curto usando o vocabulario + quiz de compreensao (`selectQuiz`). Formato: "Stage 1.2: Grammar in Context" com badge GRAMMAR, texto narrativo usando a gramatica da aula com palavras em **negrito**, seguido de perguntas de compreensao — **OBRIGATORIO, NUNCA PULAR**
- **1.4 Explicacao Gramatical** — bilingue (EN + PT-BR). Formato: "Grammar Tip" com tabela/explicacao da estrutura gramatical, exemplos afirmativo/negativo/interrogativo, e traducao — **OBRIGATORIO, NUNCA PULAR**
- **1.5 Aplicacao** — fill-in-the-blank (`checkBlank`) com hints e audio — **OBRIGATORIO**

> **CHECKLIST DE VERIFICACAO**: Antes de considerar UMA aula pronta, confirmar que existem no HTML: (1) vocab cards com audio, (2) match-grid com dropdown, (3) texto "Grammar in Context" com quiz, (4) "Grammar Tip" com explicacao bilingue, (5) fill-in-the-blank. Se QUALQUER um faltar → a aula NAO esta pronta.

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

- **Vozes ElevenLabs (ALTERNANCIA OBRIGATORIA)**:
  - **Arthur** (`sfJopaWaOtauCD3HKX6Q`): Male, neutral American — usado para palavras soltas (1-2 palavras)
  - **Ellen** (`BIvP0GN1cAtSRTxNHnWS`): Female, calm American — usada para frases longas (3+ palavras), ALTERNANDO com Arthur
  - **Regra de alternancia**: Palavras soltas (1-2 palavras) = SEMPRE Arthur. Frases (3+ palavras) = ALTERNAR Arthur/Ellen a cada frase. Dialogos: voz masculina para personagens masculinos, voz feminina para personagens femininos
  - **NUNCA usar uma unica voz para todo o material** — a alternancia e OBRIGATORIA para naturalidade
- **Formato**: MP3
- **Diretorio**: `/audio/{slug}/`
- **Nomenclatura**: frase em snake_case sem acentos, max 60 chars
- **ZERO TOLERANCIA com Web Speech API**: TODOS os audios DEVEM ser gerados via ElevenLabs e existir como MP3 no disco. Web Speech API e APENAS fallback de emergencia, NUNCA metodo principal. Se o diretorio `/audio/{slug}/` nao existir ou estiver vazio, o material NAO esta pronto para deploy
- **Speed control**: `currentAudio.playbackRate = audioSpeed`
- **Validacao pre-deploy**: Contar speakText() no HTML e comparar com arquivos em `/audio/{slug}/`. Se houver QUALQUER frase sem MP3 correspondente → BLOQUEAR deploy

---

## REGRA 8 — PRONUNCIA (startRecording)

A funcao `startRecording` DEVE implementar:

1. **SpeechRecognition** (Web Speech API) com `lang='en-US'` — APENAS para o score word-by-word, que so existe em Chrome/Edge.
   - NUNCA bloquear a gravacao por falta de SpeechRecognition. Sem SR (Safari/Firefox/celular), `hasSR=false`: a gravacao (MediaRecorder) roda do mesmo jeito, o aluno se ouve no "Your Pronunciation", o audio sobe pro Supabase e o exercicio conta como feito (`.speech-result.show` + `updateProgress()`). So o score automatico e pulado. PROIBIDO o antigo `alert('Please use Google Chrome')` + `return`.
2. **MediaRecorder** para playback do audio gravado (SEMPRE roda, independente de SpeechRecognition)
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
8. **Persistencia da gravacao**:
   - Upload do blob para Supabase Storage: `{slug}/{phraseSlug}.{ext}` (bucket `recordings`, `upsert: true`)
   - URL publica salva em `card.dataset.recordingUrl` para restauracao
   - `saveState()` inclui a URL no campo `speech` (formato JSON)
   - Ao recarregar, `loadState()` restaura o botao de playback via `injectPronunciationBtn(card, url)`
9. **Botao "Your Pronunciation"**:
   - Aparece apos gravar, ao lado de Listen e Record
   - Toca o audio gravado pelo aluno (toggle play/pause)
   - Implementado via `injectPronunciationBtn(card, audioUrl)` — funcao separada, reutilizavel
   - Cor roxa (#7c3aed) para diferenciar dos botoes Listen (accent) e Record (vermelho)
10. **Mic error handling**: `.catch()` no `getUserMedia` remove classes recording/hidden e alerta o usuario

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
ttsSpeak(text)             — Fallback TTS via speechSynthesis (helper)
injectPronunciationBtn(card, url) — Injetar botao playback da gravacao do aluno
startFreeRecording(btn)    — Gravar sem comparacao + upload Supabase + marcar .recorded
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

NENHUM material e "pronto" sem passar por TODOS os 7 checks:

1. **Portugues/Acentuacao** — Zero palavras sem acento correto nas traducoes
2. **Ingles** — Gramatica perfeita, American English 100%
3. **Nivel x Aula** — Conteudo adequado ao CEFR do aluno
4. **Audios ElevenLabs** — TODAS as frases com `speakText`/`data-phrase` tem MP3 no `audioMap`. ZERO fallback Web Speech como metodo principal
5. **Funcionalidade** — Zero `data-exercise`. HTML manual com checkBlank/selectQuiz/etc.
6. **Etapas Completas (REGRA 4)** — CADA aula DEVE conter: (a) Vocab Cards, (b) Matching, (c) Grammar in Context com texto + quiz, (d) Grammar Tip com explicacao bilingue, (e) Fill-in-the-blank, (f) Pratica, (g) Pronuncia, (h) Quiz Situacional, (i) Producao Livre. Buscar no HTML por "Grammar in Context" e "Grammar Tip" — se NAO encontrar em TODAS as aulas, REJEITAR.

7. **IN CLASS Completa** — Aba IN CLASS DEVE ter: (a) minimo 25 slides para 60min / 35 para 90min, (b) narrativa com 7 capitulos, (c) reveal cards no vocab, (d) grammar discovery, (e) dialogo line-by-line, (f) 2+ listenings com play/pause, (g) quick fire uma por vez, (h) 3 role-plays (guided>semi-free>free), (i) survival card + checklist checkbox, (j) icone T com instrucoes em TODOS os slides, (k) ZERO portugues na tela, (l) TODOS os audios no audioMap (zero missing), (m) aba IN CLASS DEVE mostrar menu de selecao de aula primeiro — NUNCA entrar em slide-mode direto no switchTab. O switchTab SEMPRE remove slide-mode. Slides so abrem via enterSlideMode() chamado por click explicito no menu

8. **Separacao de Aulas (multi-aula)** — Se o material tem 2+ aulas: (a) TODOS os slides tem `data-lesson="N"`, (b) `lessonRanges` no JS cobre todas as aulas com start/end corretos, (c) `changeSlide()` respeita bounds da aula atual, (d) contador mostra numero relativo ("01/27" nao "28/135"), (e) TODOS os cards do menu IN CLASS tem formato HTML IDENTICO (mesmo border-radius, mesmo layout, mesmo padrao de numero 2 digitos "01"/"02"). NUNCA misturar estilos entre cards.

9. **Uniformidade Visual** — Componentes repetidos (cards de menu, lesson cards, exercise sections) DEVEM ter o MESMO HTML/CSS em TODAS as instancias. Se aula 1 usa border-radius:8px e font-weight:600, aula 5 DEVE usar o mesmo. Verificar: comparar o HTML do primeiro e ultimo item de cada componente repetido — devem ser identicos exceto pelo conteudo.

Se QUALQUER check falhar → REJEITAR → corrigir → re-validar → so entao deploy.

> **LEMBRETE**: O erro mais comum e pular as etapas 1.3 (Grammar in Context) e 1.4 (Grammar Tip) no Pre-class. Isso ja aconteceu antes e NAO pode se repetir. SEMPRE verificar.

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

## REGRA 18 — PROGRESS TRACKING + PERSISTENCIA COMPLETA

> O progresso do aluno NUNCA pode sumir. Tudo que o aluno faz no Pre-class fica salvo em localStorage (instantaneo) E no Supabase (nuvem, cross-device) via activity-sync.js. Ao recarregar a pagina ou abrir de outro dispositivo, o estado completo e restaurado.

### 18.1 — O QUE CONTA NO PROGRESSO (7 tipos de exercicio)

Cada lesson card (`#ex-lesson-{N}`) tem seu progresso calculado individualmente:

| Tipo | Selector total | Selector done | Quando conta |
|---|---|---|---|
| Vocab cards | `.vocab-card-pc` | `.vocab-card-pc.listened` | Aluno clicou Listen |
| Matching | `.match-row` | `.match-row.correct` | Resposta correta |
| Fill-in-blank | `.blank-input` | `.blank-input.correct` | Resposta correta |
| Quiz | `.quiz-item` | `.quiz-item` com `.quiz-option.correct` | Opcao correta |
| Speech | `.speech-card` | `.speech-card` com `.speech-result.show` | Qualquer tentativa (good/try-again/bad) |
| Ordering | `.order-container` (1 por container) | Todos `.order-item.correct-order` | Ordem correta |
| Think card | `.think-card` | `.think-card.recorded` | Aluno gravou |

**Calculo**: `totalDone / totalExercises * 100` = percentual por aula e geral

**Barras visuais**: `.mini-bar-fill[data-lesson-progress="N"]` (width) + `.mini-percent[data-lesson-pct="N"]` (texto)

**Stamps**: `#stampN` recebe `.earned` quando a aula atinge 100%

**IMPORTANTE**: `data-lesson-progress` e `data-lesson-pct` DEVEM ter o numero correto da aula (1, 2, 3... N). NUNCA todos com "1".

### 18.2 — O QUE E SALVO (saveState)

O `saveState()` coleta o estado COMPLETO do DOM e salva em localStorage + Supabase:

```javascript
var s = {
  matches: [],        // "word|value" para cada .match-row.correct
  blanks: [],         // data-answer de cada .blank-input.correct
  quiz: [],           // texto (30 chars) de cada .quiz-option.correct
  speech: [],         // JSON string: {p: phrase, c: class, s: scoreText, words: [{w,s}], r: recordingUrl}
  mediaChecks: {},    // {mediaId: checked} para complementares
  checklists: {},     // {index: checked} para checklists
  vocabListened: [],  // texto da palavra de cada .vocab-card-pc.listened
  ordering: [],       // {id: containerId, order: [textos na ordem correta]}
  thinkRecorded: []   // JSON string: {q: questionText, r: recordingUrl}
};
```

### 18.3 — O QUE E RESTAURADO (loadState)

O `loadState()` reconstroi o estado visual completo:

- **Matches**: seleciona o dropdown, marca `.correct`, desabilita
- **Blanks**: preenche o input, marca `.correct`
- **Quiz**: marca a opcao correta com `.correct`
- **Speech**: reconstroi score + word-by-word (`.word-box.word-correct` / `.word-missing`) + injeta botao "Your Pronunciation" se houver URL de gravacao
- **Vocab listened**: marca `.listened` no card
- **Ordering**: REORDENA o DOM (move os `.order-item` para a posicao correta) e marca `.correct-order`
- **Think recorded**: marca `.recorded`, restaura `<audio>` player com URL do Supabase ou "Recording completed"
- **Media checks**: marca checkboxes e `.done`

### 18.4 — GRAVACOES (Supabase Storage)

Toda gravacao (speech + free record) faz upload para Supabase Storage:

- **Bucket**: `recordings`
- **Path speech**: `{slug}/{phraseSlug}.{ext}` (ext = mp4 ou webm)
- **Path think**: `{slug}/{thinkResultId}.{ext}`
- **Upsert**: `true` (regravar sobrescreve a anterior)
- **URL publica** salva em `card.dataset.recordingUrl` e no estado (speech.r ou thinkRecorded.r)

### 18.5 — CSS OBRIGATORIO

Todo material DEVE ter estes estilos para o tracking funcionar visualmente:

```css
.vocab-card-pc.listened{border-color:var(--success);background:rgba(22,163,74,0.06)}
.vocab-card-pc.listened .audio-btn{background:var(--success);border-color:var(--success)}
.btn-your-pronunciation{display:inline-flex;align-items:center;gap:5px;padding:.55rem 1.2rem;font:600 .82rem/1.4 -apple-system,BlinkMacSystemFont,"Inter",sans-serif;color:#fff;background:#7c3aed;border:2px solid #7c3aed;border-radius:8px;cursor:pointer;transition:all 150ms ease;white-space:nowrap}
.btn-your-pronunciation:hover{background:#6d28d9;border-color:#6d28d9}
```

---

## REGRA 19 — DEPLOY VIA GIT (NUNCA vercel --prod, SEMPRE via branch + PR)

Deploy de producao acontece AUTOMATICAMENTE via GitHub: branch → PR → merge no main → Vercel deploya.
**PROIBIDO rodar `vercel --prod` local** — deploya o checkout LOCAL por cima da producao e ja
sobrescreveu material no ar (incidente de 11/06/2026: hubs e controle perderam dados).

### BRANCHING OBRIGATORIO (dois devs no mesmo repo)

Helen e Danilo trabalham no mesmo repositorio. Para NUNCA sobrescrever o trabalho um do outro:

1. **NUNCA commitar direto no `main`**. O branch `main` e protegido.
2. **SEMPRE criar uma branch** antes de qualquer mudanca:
   - Padrao: `feat/{slug}-aula{N}` (ex: `feat/tania-rosa-aula9`)
   - Para fixes: `fix/{descricao-curta}` (ex: `fix/contrast-guard-slides`)
   - Para docs/config: `chore/{descricao}` (ex: `chore/update-regras`)
3. **Fluxo automatico que o Claude Code DEVE seguir**:
   ```
   git checkout main
   git pull origin main
   git checkout -b feat/{slug}-aula{N}
   # ... fazer todas as mudancas, commits, gerar audios ...
   git push -u origin feat/{slug}-aula{N}
   gh pr create --title "..." --body "..."
   gh pr merge --squash --delete-branch
   ```
4. **NUNCA fazer `git push origin main` direto** — o GitHub vai rejeitar.
5. Se estiver no `main` e precisar editar arquivos: criar branch ANTES da primeira edicao.
6. Apos merge: smoke-testar o site live comparando com o git.

---

## REGRA 20 — UMA AULA POR VEZ + TEMPLATE OBRIGATORIO

> **QUALIDADE > QUANTIDADE**: Gerar UMA aula de cada vez. NUNCA gerar 5 aulas juntas.

**Geracao por aula:**
- Cada execucao gera material de UMA aula apenas (Pre-class + IN CLASS + Complementares)
- O Planejamento mostra o curriculo COMPLETO do programa, mas o conteudo e de UMA aula
- Aula 2 so e gerada apos Aula 1 ser validada e aprovada
- Aula N+1 faz CALLBACK do vocabulario da aula N no warm-up

**Template obrigatorio = ALUNA MODELO (helen-mendes):**
- NUNCA gerar CSS/JS do zero. A fonte unica de layout e a aluna modelo:
  `public/professor/helen-mendes-aula1.html` (standalone) e `helen-mendes.html` (hubs prof/aluno)
- Gerar via builder: `python3 _build/model/build_from_model.py _build/{slug}-aula{N}/config.json`
  (fluxo completo, schema do config e gates em `_build/model/README.md`)
- O shell do modelo ja carrega TODOS os fixes globais (EXIT/Escape/player de listening/
  revealError/contrast-guard/nav-bar flex/3a cor guest). Builder troca APENAS:
  slug + paleta + header (perfil 360) + personagens + conteudo + audioMap
- LAYOUT vem do modelo; CONTEUDO vem do perfil 360 do aluno. Sempre.
- Bug de layout NUNCA se corrige num aluno individual: corrige-se NO MODELO (helen-mendes),
  e a correcao chega as proximas aulas via builder. Aulas ja publicadas NAO sao tocadas
  (retrofit = fase 2, sob demanda, com OK explicito)
- Exercicio de tipo NOVO (outro nivel/idade/formato) entra PRIMEIRO no modelo
  (HTML + JS + regra no validador), valida, e so entao vai pra aluno real
- patricia-ruffo/elaine-v-b sao templates LEGADOS — nao usar em geracao nova

**NUNCA contornar o builder (REGRA BLOQUEANTE):**
- Se o builder falhar (assert, erro de parsing, arquivo faltando): CORRIGIR O BUILDER, nunca contornar
- PROIBIDO usar `hub: "none"` e montar o hub manualmente via scripts Python ou copy/paste
- PROIBIDO copiar o standalone como base do hub — standalone tem CSS de slides, hub tem CSS de Pre-class. Sao arquivos DIFERENTES com CSS DIFERENTE
- PROIBIDO injetar CSS/JS/audioMap manualmente com scripts ad-hoc — o builder faz isso corretamente
- Se um assert falhar, a correcao e no arquivo `_build/model/build_from_model.py`, NAO no output
- Incidente: hub do Walyson saiu com CSS quebrado, tabs duplicadas e audioMap fora do bloco JS porque o builder foi contornado com `hub: "none"` + scripts manuais. Custou 3 PRs de correcao

**Validacao obrigatoria (gates bloqueantes, antes do PR):**
- `python3 _build/model/validate_lesson.py public/professor/{slug}-aula{N}.html public/aluno/{slug}-aula{N}.html`
- `python3 _build/model/check_vocab_progression.py public/professor/{slug}.html` — REGRA 22:
  nenhuma palavra (vocab card) ensinada como NOVA em 2+ aulas do aluno. Aula de revisao/checkpoint
  que reusa vocab de proposito = adicionar as palavras na whitelist `_build/model/vocab_allow_repeat.json`
- `python3 _build/model/check_preclass_coherence.py public/professor/{slug}.html` — REGRA 29:
  o Pre-class (bloco ex-lesson-N do hub) PREVIEWA a aula IN CLASS (mesmo tema/gramatica/vocab).
  Falha se o Pre-class for de outra aula (vocab disjunto do da aula)
- Contraste computado headless: 0 textos ilegiveis (check_computed_contrast)
- VOZES POR PERSONAGEM (bloqueante): toda dialogue-line tem data-voice; 1 voz consistente
  por personagem; personagens distintos no MESMO dialogo = vozes DISTINTAS; dialogo com
  mais falantes que vozes disponiveis (_build/model/voices.json) = ERRO; o validador
  cruza o audio_manifest.json pra garantir que cada MP3 foi gerado com a voz declarada

**Audio OBRIGATORIO em TODA aula:**
- TODAS as frases com speakText() DEVEM ter MP3 no audioMap ANTES do deploy
- Script de geracao de audio roda DEPOIS do HTML, populando o audioMap
- Verificacao pre-deploy: comparar speakText() calls vs audioMap — ZERO missing
- Se audioMap estiver vazio ou incompleto: NAO fazer deploy

**Checklist por aula (BLOQUEANTE):**
1. Pre-class tem as 5 etapas obrigatorias (REGRA 4)?
2. IN CLASS tem minimo 25 slides com todos os componentes?
3. Icone T tem instrucoes em TODOS os slides?
4. ZERO portugues na tela IN CLASS?
5. audioMap cobre 100% dos speakText()?
6. Vozes Arthur/Ellen alternadas corretamente (feminino=Ellen, masculino=Arthur)?
7. ZERO emojis, ZERO imagens externas quebradas?
8. Complementares tem 3 recomendacoes?
Se QUALQUER item falhar → NAO fazer deploy → corrigir → re-validar.

---

## REGRA 21 — NUNCA ALTERAR MATERIAIS ATIVOS

Materiais de alunos com status ATIVO no dashboard NUNCA podem ser alterados sem pedido EXPLICITO.
Melhorias sao testadas em materiais novos PRIMEIRO.
So migrar materiais ativos quando EXPLICITAMENTE pedido.
Melhorias sao testadas em materiais novos primeiro.

---

## REGRA 21 — INGLES AMERICANO

Todo conteudo em ingles deve seguir American English: spelling, vocabulary, pronunciation.
- "color" (nao "colour"), "organize" (nao "organise"), "apartment" (nao "flat")

### Teacher vs Professor — USO CORRETO

| Termo | Significado | Contexto |
|-------|------------|----------|
| **Teacher** | Termo GERAL para quem ensina | Escolas, cursos livres, aulas particulares, ensino fundamental/medio. Ex: "English teacher", "math teacher" |
| **Professor** | Titulo ACADEMICO especifico | Ensino superior (universidades/faculdades), docentes com mestrado/doutorado, cargos de pesquisa. Ex: "Professor Crawford teaches constitutional law at Georgetown" |

**Regras para o material Alumni:**
- Personagens que ENSINAM INGLES = **teacher** (Helen e a equipe Alumni sao teachers)
- Personagens em UNIVERSIDADES = **professor** (Professor Crawford, Professor Torres)
- Na aba Planejamento e data-teacher = ok usar "professor" em portugues (instrucoes internas)
- Na tela IN CLASS = "Professor" so como titulo academico EN seguido de nome proprio
- NUNCA usar "professor" como traducao generica de "teacher" na tela IN CLASS

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

## REGRA 25 — MOBILE-FIRST + UI/UX PRO MAX

Todo material e pagina do sistema deve ser responsivo e funcional em celular. Touch targets minimos de 44x44px. Ordering deve ter botoes de seta alem de drag-and-drop.

**UI/UX Pro Max OBRIGATORIO em TODA pagina criada ou modificada:**
- Contraste WCAG AA minimo (4.5:1) para todo texto
- Focus states visiveis (outline 3px) em TODOS os elementos interativos (botoes, links, cards clicaveis)
- `aria-label` em botoes com icone (sem texto visivel)
- `prefers-reduced-motion`: desativar animacoes para usuarios que preferem
- `cursor-pointer` em todos os elementos clicaveis
- Hover states com transicoes suaves (150-300ms)
- Responsivo em 375px, 768px, 1024px, 1440px
- Zero emojis — TODOS os icones sao SVG inline
- Tipografia consistente: Inter (corpo) + Cormorant Garamond (titulos)
- Paleta Alumni: navy #003080, red #d70c0c, bg #f5f5f0, success #16a34a, danger #dc2626

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
        currentAudio.play().catch(function() { ttsSpeak(cleanText); });
    } else { ttsSpeak(cleanText); }
    if (btn) { var vc = btn.closest('.vocab-card-pc'); if (vc && !vc.classList.contains('listened')) { vc.classList.add('listened'); updateProgress(); } }
}

function ttsSpeak(text) {
    if ('speechSynthesis' in window) { window.speechSynthesis.cancel(); var u = new SpeechSynthesisUtterance(text); u.lang = 'en-US'; u.rate = audioSpeed * 0.85; u.pitch = 1; window.speechSynthesis.speak(u); }
}

function speakPhrase(btn) {
    var card = btn.closest('.speech-card');
    if (card) speakText(card.dataset.phrase, btn);
}

// ===== YOUR PRONUNCIATION BUTTON =====
function injectPronunciationBtn(card, audioUrl) {
    var old = card.querySelector('.btn-your-pronunciation'); if (old) old.remove();
    var playBtn = document.createElement('button');
    playBtn.className = 'btn btn-your-pronunciation';
    playBtn.innerHTML = '&#9654; Your Pronunciation';
    playBtn.onclick = function(e) { e.preventDefault();
        if (playBtn.dataset.playing === 'true') {
            var a = card.querySelector('.your-pron-audio'); if (a) { a.pause(); a.remove(); }
            playBtn.innerHTML = '&#9654; Your Pronunciation'; playBtn.dataset.playing = 'false'; return;
        }
        var audio = new Audio(audioUrl); audio.className = 'your-pron-audio'; audio.style.display = 'none';
        card.appendChild(audio); playBtn.innerHTML = '&#9632; Playing...'; playBtn.dataset.playing = 'true';
        audio.play();
        audio.onended = function() { playBtn.innerHTML = '&#9654; Your Pronunciation'; playBtn.dataset.playing = 'false'; audio.remove(); };
        audio.onerror = function() { playBtn.innerHTML = '&#9654; Your Pronunciation'; playBtn.dataset.playing = 'false'; audio.remove(); };
    };
    var controls = card.querySelector('.speech-controls');
    if (controls) controls.appendChild(playBtn);
}

// ===== SPEECH RECOGNITION =====
var activeRecognition = null;

function startRecording(btn) {
    var SR = window.SpeechRecognition || window.webkitSpeechRecognition;
    var hasSR = !!SR; // Chrome/Edge tem SpeechRecognition (score word-by-word). Safari/Firefox/mobile nao — caem no fallback audio-only.
    var card = btn.closest('.speech-card');
    var target = card.dataset.phrase.toLowerCase().replace(/[^a-z0-9' ]/g, '');
    var resultDiv = card.querySelector('.speech-result');
    var stopBtn = card.querySelector('.btn-stop');
    if (btn.classList.contains('recording')) return;
    btn.classList.add('recording', 'hidden');
    stopBtn.classList.add('visible');

    var mediaRec = null, mediaChunks = [], mediaStream = null, recDone = false;
    navigator.mediaDevices.getUserMedia({ audio: true }).then(function(stream) {
        mediaStream = stream;
        var mimeType = MediaRecorder.isTypeSupported('audio/mp4') ? 'audio/mp4' : MediaRecorder.isTypeSupported('audio/webm;codecs=opus') ? 'audio/webm;codecs=opus' : '';
        mediaRec = mimeType ? new MediaRecorder(stream, { mimeType: mimeType }) : new MediaRecorder(stream);
        mediaChunks = [];
        mediaRec.ondataavailable = function(e) { if (e.data.size > 0) mediaChunks.push(e.data); };
        mediaRec.onstop = function() {
            if (recDone) return; recDone = true;
            stream.getTracks().forEach(function(t) { t.stop(); });
            if (mediaChunks.length > 0) {
                var blob = new Blob(mediaChunks, { type: mediaRec.mimeType });
                var audioUrl = URL.createObjectURL(blob);
                injectPronunciationBtn(card, audioUrl);
                // Fallback audio-only (sem SpeechRecognition): marca o exercicio como feito e mostra "Recording saved"
                if (!hasSR) {
                    resultDiv.classList.add('show', 'good'); resultDiv.classList.remove('try-again', 'bad');
                    resultDiv.innerHTML = '<strong>&#10003; Recording saved</strong> — listen back with "Your Pronunciation".';
                    if (typeof updateProgress === 'function') updateProgress();
                    finish();
                }
                // Upload to Supabase Storage for persistence
                var phraseSlug = card.dataset.phrase.toLowerCase().replace(/[^a-z0-9]/g, '_').substring(0, 50);
                var slug = window.STUDENT_SLUG || 'unknown';
                var ext = blob.type.indexOf('mp4') !== -1 ? 'mp4' : 'webm';
                var filePath = slug + '/' + phraseSlug + '.' + ext;
                if (typeof sb !== 'undefined') {
                    sb.storage.from('recordings').upload(filePath, blob, { contentType: blob.type, upsert: true }).then(function(res) {
                        if (!res.error) {
                            var pubUrl = sb.storage.from('recordings').getPublicUrl(filePath).data.publicUrl;
                            card.dataset.recordingUrl = pubUrl;
                            if (typeof saveState === 'function') saveState();
                        }
                    });
                }
            }
        };
        mediaRec.start(100);

        var ended = false;
        function finish() {
            if (ended) return; ended = true;
            btn.classList.remove('recording', 'hidden'); stopBtn.classList.remove('visible'); activeRecognition = null;
            setTimeout(function() { if (mediaRec && mediaRec.state === 'recording') mediaRec.stop(); }, 200);
        }
        if (hasSR) {
        var r = new SR();
        r.lang = 'en-US'; r.interimResults = false; r.maxAlternatives = 3; r.continuous = true;
        activeRecognition = { recognition: r, btn: btn, stopBtn: stopBtn, card: card, mediaRec: mediaRec };
        r.start();
        r.onresult = function(event) {
            var best = event.results[event.results.length - 1][0].transcript.toLowerCase().replace(/[^a-z0-9' ]/g, '');
            var analysis = analyzeWords(target, best);
            var totalWords = analysis.expected.length;
            var correctWords = analysis.expected.filter(function(w) { return w.status === 'correct'; }).length;
            resultDiv.classList.add('show'); resultDiv.classList.remove('good', 'try-again', 'bad');
            var html = '';
            if (analysis.score >= 0.8) { resultDiv.classList.add('good'); html += '<strong>Score: ' + correctWords + '/' + totalWords + '</strong> — Excellent!'; updateProgress(); }
            else if (analysis.score >= 0.5) { resultDiv.classList.add('try-again'); html += '<strong>Score: ' + correctWords + '/' + totalWords + '</strong> — Almost there!'; }
            else { resultDiv.classList.add('bad'); html += '<strong>Score: ' + correctWords + '/' + totalWords + '</strong> — Keep practicing!'; }
            html += '<div class="word-comparison"><div class="comp-label">Word-by-word:</div><div class="comp-words">';
            analysis.expected.forEach(function(w) { html += '<span class="word-box word-' + (w.status === 'correct' ? 'correct' : 'missing') + '">' + w.word + '</span>'; });
            html += '</div></div>';
            resultDiv.innerHTML = html;
            finish();
        };
        r.onerror = function() { finish(); resultDiv.classList.add('show', 'try-again'); resultDiv.innerHTML = 'Could not hear you. Check your microphone.'; };
        r.onend = function() { finish(); };
        setTimeout(function() { if (!ended) { try { r.stop(); } catch(e) {} finish(); } }, 30000);
        } else {
        activeRecognition = { recognition: null, btn: btn, stopBtn: stopBtn, card: card, mediaRec: mediaRec };
        setTimeout(function() { if (!ended) finish(); }, 30000);
        }
    }).catch(function() { btn.classList.remove('recording', 'hidden'); stopBtn.classList.remove('visible'); alert('Could not access microphone.'); });
}

function stopRecording(stopBtn) {
    if (activeRecognition) {
        try { activeRecognition.recognition.stop(); } catch(e) {}
        if (activeRecognition.mediaRec && activeRecognition.mediaRec.state === 'recording') {
            try { activeRecognition.mediaRec.stop(); } catch(e) {}
        }
    }
}

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
            if (resultDiv) resultDiv.innerHTML = '<audio controls src="' + url + '" style="width:100%;margin-top:0.5rem;"></audio><p style="font-size:0.72rem;color:var(--success);margin-top:0.3rem;">Recording saved!</p>';
            thinkCard.classList.add('recorded');
            updateProgress();
            stream.getTracks().forEach(function(t) { t.stop(); });
            // Upload to Supabase Storage
            var slug = window.STUDENT_SLUG || 'unknown';
            var thinkId = resultDiv.id || 'think-free';
            var ext = blob.type.indexOf('mp4') !== -1 ? 'mp4' : 'webm';
            var filePath = slug + '/' + thinkId + '.' + ext;
            if (typeof sb !== 'undefined') {
                sb.storage.from('recordings').upload(filePath, blob, { contentType: blob.type, upsert: true }).then(function(res) {
                    if (!res.error) {
                        var pubUrl = sb.storage.from('recordings').getPublicUrl(filePath).data.publicUrl;
                        thinkCard.dataset.recordingUrl = pubUrl;
                        if (typeof saveState === 'function') saveState();
                    }
                });
            }
        };
        freeRecorder.start(100);
        btn.classList.add('hidden');
        stopBtn.classList.add('visible');
    }).catch(function() { alert('Could not access microphone.'); });
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
    var totalAllDone = 0, totalAllEx = 0;
    for (var l = 1; l <= totalLessons; l++) {
        var card = document.getElementById('ex-lesson-' + l);
        if (!card) continue;
        var total = 0, done = 0;
        total += card.querySelectorAll('.vocab-card-pc').length;
        done += card.querySelectorAll('.vocab-card-pc.listened').length;
        total += card.querySelectorAll('.match-row').length;
        done += card.querySelectorAll('.match-row.correct').length;
        total += card.querySelectorAll('.blank-input').length;
        done += card.querySelectorAll('.blank-input.correct').length;
        var quizItems = card.querySelectorAll('.quiz-item');
        total += quizItems.length;
        quizItems.forEach(function(qi) { if (qi.querySelector('.quiz-option.correct')) done++; });
        var speechCards = card.querySelectorAll('.speech-card');
        total += speechCards.length;
        speechCards.forEach(function(sc) { if (sc.querySelector('.speech-result.show')) done++; });
        card.querySelectorAll('.order-container').forEach(function(oc) {
            var items = oc.querySelectorAll('.order-item');
            total += 1;
            if (items.length > 0 && items.length === oc.querySelectorAll('.order-item.correct-order').length) done++;
        });
        var thinkCards = card.querySelectorAll('.think-card');
        total += thinkCards.length;
        thinkCards.forEach(function(tc) { if (tc.classList.contains('recorded')) done++; });
        var pct = total > 0 ? Math.round(done / total * 100) : 0;
        var fill = document.querySelector('.mini-bar-fill[data-lesson-progress="' + l + '"]');
        if (fill) fill.style.width = pct + '%';
        var pctEl = document.querySelector('.mini-percent[data-lesson-pct="' + l + '"]');
        if (pctEl) pctEl.textContent = pct + '%';
        var stampEl = document.getElementById('stamp' + l);
        if (stampEl) { if (pct === 100) stampEl.classList.add('earned'); else stampEl.classList.remove('earned'); }
        totalAllDone += done; totalAllEx += total;
    }
    var overallPct = totalAllEx > 0 ? Math.round(totalAllDone / totalAllEx * 100) : 0;
    var pb = document.getElementById('progressBar');
    var pp = document.getElementById('progressPercent');
    if (pb) pb.style.width = overallPct + '%';
    if (pp) pp.textContent = overallPct + '%';
    var celCard = document.getElementById('celebrationCard');
    if (celCard) celCard.style.display = overallPct === 100 ? 'block' : 'none';
    try { localStorage.setItem('alumni-progress-{SLUG}', JSON.stringify({ concluidas: totalAllDone, total: totalAllEx })); } catch(e) {}
    saveState();
}

// ===== STATE PERSISTENCE =====
// SUBSTITUIR: '{SLUG}-professor' ou '{SLUG}-aluno' conforme o arquivo
function saveState() {
    var s = { matches: [], blanks: [], quiz: [], speech: [], mediaChecks: {}, checklists: {}, vocabListened: [], ordering: [], thinkRecorded: [] };
    document.querySelectorAll('.media-card-wrapper').forEach(function(w) { var id = w.dataset.media; var cb = w.querySelector('input[type="checkbox"]'); if (id && cb) s.mediaChecks[id] = cb.checked; });
    document.querySelectorAll('.match-row.correct select').forEach(function(sel) { s.matches.push(sel.closest('.match-row').querySelector('.match-word').textContent + '|' + sel.value); });
    document.querySelectorAll('.blank-input.correct').forEach(function(e) { s.blanks.push(e.dataset.answer); });
    document.querySelectorAll('.quiz-option.correct').forEach(function(e) { s.quiz.push(e.textContent.trim().substring(0, 30)); });
    document.querySelectorAll('.speech-result.show').forEach(function(e) {
        var sc = e.closest('.speech-card');
        if (sc && sc.dataset.phrase) {
            var cls = e.classList.contains('good') ? 'good' : e.classList.contains('try-again') ? 'try-again' : 'bad';
            var strong = e.querySelector('strong'); var scoreTxt = strong ? strong.textContent : 'Done';
            var words = []; e.querySelectorAll('.word-box').forEach(function(wb) { words.push({ w: wb.textContent, s: wb.classList.contains('word-correct') ? 'c' : 'm' }); });
            var recUrl = sc.dataset.recordingUrl || '';
            s.speech.push(JSON.stringify({ p: sc.dataset.phrase, c: cls, s: scoreTxt, words: words, r: recUrl }));
        }
    });
    document.querySelectorAll('.checklist input[type="checkbox"]').forEach(function(cb, i) { s.checklists[i] = cb.checked; });
    document.querySelectorAll('.vocab-card-pc.listened').forEach(function(vc) { var w = vc.querySelector('.vocab-card-word'); if (w) s.vocabListened.push(w.textContent); });
    document.querySelectorAll('.order-container').forEach(function(oc) {
        var items = oc.querySelectorAll('.order-item'); var correct = oc.querySelectorAll('.order-item.correct-order');
        if (items.length > 0 && items.length === correct.length) {
            var id = oc.id || ''; var order = [];
            items.forEach(function(it) { order.push(it.querySelector('.order-text').textContent); });
            s.ordering.push({ id: id, order: order });
        }
    });
    document.querySelectorAll('.think-card.recorded').forEach(function(tc) {
        var q = tc.querySelector('.think-question');
        if (q) { var recUrl = tc.dataset.recordingUrl || ''; s.thinkRecorded.push(JSON.stringify({ q: q.textContent.trim().substring(0, 40), r: recUrl })); }
    });
    localStorage.setItem('{SLUG}-professor', JSON.stringify(s));
}

function loadState() {
    var r = localStorage.getItem('{SLUG}-professor'); if (!r) return;
    var s = JSON.parse(r);
    if (s.matches) s.matches.forEach(function(d) { var parts = d.split('|'); var word = parts[0]; var val = parts[1]; document.querySelectorAll('.match-row').forEach(function(row) { if (row.querySelector('.match-word').textContent === word) { var sel = row.querySelector('select'); sel.value = val; row.classList.add('correct'); } }); });
    if (s.blanks) s.blanks.forEach(function(a) { document.querySelectorAll('.blank-input[data-answer="' + a + '"]').forEach(function(e) { e.value = a; e.classList.add('correct'); }); });
    if (s.quiz) s.quiz.forEach(function(t) { document.querySelectorAll('.quiz-option[data-correct="true"]').forEach(function(e) { if (e.textContent.trim().substring(0, 30) === t) e.classList.add('correct'); }); });
    if (s.speech) s.speech.forEach(function(d) {
        var phrase, cls, scoreTxt, words, recUrl;
        try { var obj = JSON.parse(d); phrase = obj.p; cls = obj.c; scoreTxt = obj.s; words = obj.words || []; recUrl = obj.r || ''; }
        catch(e) { phrase = d; cls = 'good'; scoreTxt = 'Done'; words = []; recUrl = ''; }
        document.querySelectorAll('.speech-card').forEach(function(sc) {
            if (sc.dataset.phrase === phrase) {
                var rd = sc.querySelector('.speech-result');
                if (rd) {
                    rd.classList.add('show', cls);
                    var html = '<strong>' + scoreTxt + '</strong>' + (words.length > 0 ? (' — ' + (cls === 'good' ? 'Excellent!' : cls === 'try-again' ? 'Almost there!' : 'Keep practicing!')) : '');
                    if (words.length > 0) {
                        html += '<div class="word-comparison"><div class="comp-label">Word-by-word:</div><div class="comp-words">';
                        words.forEach(function(w) { html += '<span class="word-box word-' + (w.s === 'c' ? 'correct' : 'missing') + '">' + w.w + '</span>'; });
                        html += '</div></div>';
                    }
                    rd.innerHTML = html;
                }
                if (recUrl) { sc.dataset.recordingUrl = recUrl; injectPronunciationBtn(sc, recUrl); }
            }
        });
    });
    if (s.checklists) { document.querySelectorAll('.checklist input[type="checkbox"]').forEach(function(cb, i) { if (s.checklists[i]) { cb.checked = true; cb.closest('li').classList.add('checked'); } }); }
    if (s.mediaChecks) { document.querySelectorAll('.media-card-wrapper').forEach(function(w) { var id = w.dataset.media; var cb = w.querySelector('input[type="checkbox"]'); if (id && cb && s.mediaChecks[id]) { cb.checked = true; w.classList.add('done'); } }); }
    if (s.vocabListened) { s.vocabListened.forEach(function(word) { document.querySelectorAll('.vocab-card-pc').forEach(function(vc) { var w = vc.querySelector('.vocab-card-word'); if (w && w.textContent === word) vc.classList.add('listened'); }); }); }
    if (s.ordering) { s.ordering.forEach(function(o) {
        var id = typeof o === 'string' ? o : o.id; var savedOrder = typeof o === 'object' ? o.order : null;
        var oc = id ? document.getElementById(id) : null; if (!oc) return;
        if (savedOrder && savedOrder.length > 0) { var items = Array.from(oc.querySelectorAll('.order-item')); savedOrder.forEach(function(txt) { for (var i = 0; i < items.length; i++) { var t = items[i].querySelector('.order-text'); if (t && t.textContent === txt) { oc.appendChild(items[i]); break; } } }); }
        oc.querySelectorAll('.order-item').forEach(function(it, i) { it.classList.add('correct-order'); it.querySelector('.order-num').textContent = i + 1; it.style.borderColor = 'var(--success)'; });
    }); }
    if (s.thinkRecorded) { s.thinkRecorded.forEach(function(d) {
        var qTxt, recUrl; try { var obj = JSON.parse(d); qTxt = obj.q; recUrl = obj.r || ''; } catch(e) { qTxt = d; recUrl = ''; }
        document.querySelectorAll('.think-card').forEach(function(tc) {
            var qEl = tc.querySelector('.think-question');
            if (qEl && qEl.textContent.trim().substring(0, 40) === qTxt) {
                tc.classList.add('recorded'); tc.dataset.recordingUrl = recUrl;
                var rd = tc.querySelector('[id^="think-result"]');
                if (rd) { if (recUrl) { rd.innerHTML = '<audio controls src="' + recUrl + '" style="width:100%;margin-top:0.5rem;"></audio><p style="font-size:.72rem;color:var(--success);margin-top:.3rem;">&#10003; Recording saved</p>'; } else { rd.innerHTML = '<p style="font-size:.82rem;color:var(--success);font-weight:500;">&#10003; Recording completed</p>'; } }
            }
        });
    }); }
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
    if (select.value === answer) { row.classList.add('correct'); updateProgress(); } // NUNCA disabled: dropdown segue trocavel (REGRA UX)
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
| `window.STUDENT_SLUG` | Definido no `<head>`: `window.STUDENT_SLUG='{SLUG}'` |
| `sb` (Supabase client) | Disponivel via `/lib/supabase-config.js` carregado ANTES |

---

## REGRA 27 — DESIGN PEDAGOGICO DE SLIDES (IN CLASS)

> Regras derivadas de feedback real de professores em aula. TODAS sao OBRIGATORIAS para novos materiais.

### A. Saudacoes naturais NUNCA no slide
- Cumprimentos como "Hi [aluno]! How are you today?" acontecem ao vivo, organicamente
- NUNCA incluir saudacao inicial scriptada no warm-up — a professora ja vai ter feito isso
- O primeiro prompt do slide deve ir direto ao conteudo (ex: "In one word: what excites you most about...?")

### B. Transicoes entre temas precisam de ponte
- NUNCA pular de um tema para outro sem pergunta-bridge
- Se o slide fala de "Paris 2027" e depois vai para "favorite series", incluir uma pergunta intermediaria que conecte os dois (ex: "What do you know about French culture?" antes de perguntar sobre series)
- A sequencia logica deve ser: tema A → ponte A→B → tema B

### C. Zero redundancia contextual
- Se a aula inteira e em ingles, NUNCA escrever "in English" na instrucao
- Se o aluno ja esta praticando, NUNCA escrever "Time to Practice" — usar "More Practice"
- Se o aluno ja esta participando, NUNCA escrever "Your Turn" como se fosse a primeira vez — contextualizar com subtitulo (ex: "From guided to free — show what you learned")
- Regra geral: nao dizer o que ja e obvio pelo contexto

### D. Linguagem situacional realista
- Frases de dialogo e cenarios devem refletir o que alguem REALMENTE diria naquele contexto
- Num aeroporto: "What's your name?" (nao "Who are you?")
- Num hotel: "Do you have a reservation?" (nao "Are you staying here?")
- Sempre validar: "Uma pessoa real falaria isso nessa situacao?"

### E. Elementos interativos DEVEM ser toggle
- Vocab reveal cards: clicar abre, clicar de novo FECHA (classList.toggle, nao classList.add)
- Se a professora clica sem querer, DEVE conseguir fechar imediatamente
- Aplica-se a: vocab cards, hint cards, qualquer elemento que revela resposta
- NUNCA usar one-way reveal em elementos que a professora controla durante a aula

### F. Comprehension testa o OUTRO, nao o aluno
- Perguntas de "Did you understand?" apos dialogo devem ser sobre o INTERLOCUTOR (Sarah, receptionist, etc.)
- NUNCA pedir ao aluno que fale de si mesmo na 3a pessoa (ex: "How old is Gabriela?" para a propria Gabriela = confuso)
- Perguntas devem verificar compreensao do que o OUTRO disse no dialogo
- Formato ideal: "Where is [personagem] from?", "Does [personagem] like X?", "What does [personagem] do?"
- Numero de perguntas = numero de informacoes CONCRETAS sobre o interlocutor no dialogo (nao inventar)

### G. Keywords devem ser produziveis
- Keywords em role-play semi-free devem ser palavras/valores que o aluno ENCAIXA na frase
- ERRADO: `age` (ninguem fala "My age is...") → CERTO: `16` (induz "I am 16 years old")
- ERRADO: `city` (ninguem fala "My city is...") → CERTO: `São Paulo` (induz "I am from São Paulo")
- CERTO: `name` (induz "My name is...")  — funciona porque a palavra e usada naturalmente
- Teste: se a keyword NAO aparece literalmente na frase que o aluno diria, trocar pelo valor concreto

### H. Zero redundancia lexical em keywords
- NUNCA usar "favorite hobby" — hobby ja implica que e favorito
- NUNCA duplicar conceitos com adjetivos desnecessarios
- Cada keyword deve ser UMA informacao unica e necessaria

---

## REGRA 28 — LESSON PROGRESS TRACKING (SUPABASE)

> Todo material de aluno DEVE incluir o sistema de progresso via Supabase. Quando o professor marca os 5 checks do "What I Learned" no final de cada aula IN CLASS, a aula e registrada como concluida no Supabase. A barra de avanco e os stamps atualizam automaticamente em AMBAS as paginas (professor e aluno).

### Scripts obrigatorios no `<head>`:

```html
<script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2/dist/umd/supabase.min.js"></script>
<script src="/lib/supabase-config.js"></script>
<script>window.STUDENT_SLUG='{SLUG}';window.TOTAL_AULAS={N};</script>
```

### 3 scripts obrigatorios antes de `</body>` (DEPOIS do script principal, NESTA ORDEM):

```html
<script src="/lib/lesson-progress.js"></script>
<script src="/lib/controle-aulas.js"></script>
<script src="/lib/activity-sync.js"></script>
</body>
```

**ORDEM IMPORTA**: lesson-progress → controle-aulas → activity-sync. O activity-sync DEVE ser o ULTIMO porque faz wrap de `saveState()` e `updateProgress()` que ja devem existir.

### O que cada script faz:

| Script | Funcao | Tabela Supabase |
|---|---|---|
| `lesson-progress.js` | Progresso GLOBAL: stamps + barra do header. Wrap do `toggleCheck()` → salva `inclass_done` quando 5/5 checks marcados | `lesson_progress` |
| `controle-aulas.js` | Injeta aba "Controle de Aulas" com datas, feedback professor/aluno. Auto-save debounce 1.5s | `controle_aulas` |
| `activity-sync.js` | **O MAIS IMPORTANTE**: sync localStorage↔Supabase de TODOS os exercicios (matching, fill-in, quiz, speech, ordering, think, mediaChecks dos Complementares). Cross-device. Upload gravacoes. Botao Reset (so aluno). Debounce 2s + auto-save 30s + beforeunload keepalive | `student_activity` + Storage `recordings` |

### Como funciona:
1. `lesson-progress.js` faz wrap do `toggleCheck()` existente
2. Quando o professor marca 5/5 checks no checklist → `inclass_done = true` no Supabase
3. Ao carregar, busca do Supabase quais aulas concluidas → atualiza barra + stamps
4. `activity-sync.js` faz wrap de `saveState()` — check nos Complementares (`toggleMediaDone`) salva em localStorage E Supabase
5. Tabelas: `lesson_progress`, `controle_aulas`, `student_activity`

### Variaveis para substituir:

| Placeholder | Substituir por |
|---|---|
| `{SLUG}` | Slug do aluno (ex: `gabriela-pires`) |
| `{N}` | Total de aulas no pacote do aluno (ex: `48`) |

### IMPORTANTE:
- Os 3 scripts DEVEM ser carregados DEPOIS do `<script>` principal (que define `toggleCheck`, `saveState`, `updateProgress`)
- O `STUDENT_SLUG` DEVE ser o slug PRINCIPAL do aluno (sem sufixo `-aula2` etc.)
- Nunca editar esses scripts para um aluno especifico — sao GENERICOS
- Sem `activity-sync.js`, checks dos Complementares salvam APENAS em localStorage (perde ao limpar cache). COM ele, salva no Supabase = permanente + cross-device
- **TOTAL**: 5 scripts por material = 2 no head (supabase.min.js + supabase-config.js) + 3 antes do body (lesson-progress + controle-aulas + activity-sync)
- A barra de progresso mostra: aulas com `inclass_done=true` / TOTAL_AULAS * 100

---

## REGRA 29 — COERENCIA DAS 4 ABAS (Pre-class PREVIEWA a aula)

> Reforca a REGRA 1.5. Uma aula e UMA so: as 4 abas (Planejamento, Pre-class, IN CLASS,
> Complementares) falam da MESMA aula — MESMO tema, MESMA gramatica, MESMO vocab. O
> Pre-class do hub (bloco `id="ex-lesson-N"` em `{slug}.html`) PREVIEWA exatamente a aula
> IN CLASS standalone (`{slug}-aulaN.html`): mesmo titulo, mesma gramatica, e o vocab do
> Pre-class e o MESMO vocab que a aula ensina. NUNCA o Pre-class de uma aula com tema/vocab
> de OUTRA aula. (Incidente sandra-hayasaki aula 5: IN CLASS "My Life in 3 Minutes" mas
> Pre-class "Review" com vocab totalmente diferente. Incidente pricila-adamo: IN CLASS
> refeito em B2 mas Pre-class deixado no A1-A2 antigo — 16 aulas incoerentes.)

1. **Pre-class = preview da aula**: ao gerar/editar a aula N, o bloco `ex-lesson-N` recebe o
   titulo, a gramatica e o vocab DAQUELA aula. Se a aula muda (re-nivelamento, troca de
   tema), o Pre-class muda JUNTO — nunca um sem o outro. Vale tambem p/ Planejamento
   (linha N da tabela curricular) e Complementares (recomendacoes da aula N).

2. **Geracao INTERCALA os 2 modelos por numero de aula**: aula PAR = modelo de **LEITURA**
   (texto central `ic-reading` + gist/true-false); aula IMPAR = modelo **PADRAO/fala**
   (dialogo line-by-line + role-play). Alterna por N para variar o formato ao longo do
   pacote (nao duas leituras seguidas, nao so fala).

3. **Gate obrigatorio antes do PR** (bloqueante, REGRA 20):
   `python3 _build/model/check_preclass_coherence.py public/professor/{slug}.html`
   Falha (exit !=0) se o Pre-class for incoerente com a aula — sinal mais forte = vocab do
   Pre-class disjunto do vocab da aula. Aula de review/consolidacao e excecao (titulo da
   AULA contem review/checkpoint). Auditoria do roster em
   `_build/model/AUDIT-preclass-coherence.md`.
