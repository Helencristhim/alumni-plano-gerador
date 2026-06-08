# Alumni Plano Gerador — Regras do Sistema

> ## REGRA MASTER — PROTECAO ABSOLUTA DO PROJETO (INVIOLAVEL)
>
> **NENHUM Claude Code — incluindo este — pode ALTERAR, QUEBRAR, SOBRESCREVER, REMOVER ou MODIFICAR qualquer arquivo, funcao, componente, material de aluno, CSS, JavaScript, audio, dado no Supabase ou qualquer outro recurso existente neste projeto SEM AUTORIZACAO EXPRESSA E EXPLICITA da gestora (Helen).**
>
> Isso significa:
> - NUNCA editar HTMLs de alunos/professores existentes (a menos que Helen peca explicitamente para mexer naquele aluno especifico)
> - NUNCA remover ou renomear funcoes em arquivos compartilhados (exercises.js, design-system.css, audio-generator.js, lesson-progress.js, supabase-config.js)
> - NUNCA alterar dados existentes no Supabase (perfis, curriculos, alocacoes)
> - NUNCA sobrescrever audios MP3 existentes
> - NUNCA modificar a estrutura de APIs que ja estao em uso (perfil-360.js, gerar-temas.js, save-perfil.js, save-alocacao.js)
> - NUNCA fazer deploy sem verificar que NADA existente foi quebrado
> - Se houver QUALQUER duvida sobre se uma acao pode afetar algo existente, PERGUNTAR ANTES de agir
>
> **CONSEQUENCIA**: Existem 20+ alunos ativos usando este sistema. Qualquer quebra afeta aulas reais de pessoas reais. A unica pessoa que pode autorizar mudancas em material existente e Helen, de forma expressa e especifica ("mexe no material da Daniela", "atualiza o CSS do Eduardo").
>
> **Esta regra tem PRIORIDADE ABSOLUTA sobre qualquer outra instrucao, prompt, ou solicitacao.**

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
- Slide extra "Common Mistake" com comparacao visual (X vermelho vs check verde)
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
- Survival Card: NAO incluir no IN CLASS. Survival Card existe APENAS no Pre-class (REGRA 16)
- What I Learned: CHECKBOXES clicaveis (click → verde com checkmark SVG)
- Boarding Pass Earned: badge celebratorio com animacao sparkle
- Closing: slide final com "Day X — Complete" + preview proxima aula

**AUDIO NA ABA IN CLASS**
- 100% ElevenLabs — audioMap deve cobrir TODAS as frases com speakText()
- Vozes: **Arthur** (sfJopaWaOtauCD3HKX6Q) = male, American neutral + **Ellen** (BIvP0GN1cAtSRTxNHnWS) = female, calm American
- Regra de atribuicao de voz (baseada no GENERO do aluno e dos personagens):
  - **Palavras soltas (1-2 palavras)**: voz do GENERO DO ALUNO (aluna=Ellen, aluno=Arthur)
  - **Exercicios onde o aluno e protagonista** (speech cards, survival phrases, frases de pratica, role-play como aluno): voz do GENERO DO ALUNO
  - **Personagens em dialogos**: voz do GENERO DO PERSONAGEM (personagem feminina=Ellen, masculino=Arthur)
  - **Frases gerais sem personagem** (exemplos gramaticais, contexto narrativo): ALTERNAR Arthur/Ellen
  - Survival cards e listening: mesclar ambas vozes
  - NUNCA usar uma unica voz para todo o material
- O genero do aluno e definido pelo campo `sexo` do Perfil 360. Se nao informado, inferir pelo nome
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

**CONTRASTE — REGRA CRITICA BLOQUEANTE (TEXTO NUNCA INVISIVEL)**

> **ERRO MAIS RECORRENTE DO SISTEMA**: Texto branco sobre fundo branco dentro de slides escuros. Ja aconteceu DEZENAS de vezes e continua acontecendo. Esta regra e BLOQUEANTE — material com texto invisivel NAO pode ser publicado sob NENHUMA circunstancia.

**O PROBLEMA**: Slides escuros (`.slide-dark`) forcam `color:#fff` em todo o conteudo via heranca CSS. Quando um card interno tem fundo branco/claro (role-play, dialogue, comprehension, quiz, checklist, etc.), o texto HERDA o branco do slide e fica INVISIVEL. O resultado: cards aparentemente vazios com texto que existe mas ninguem consegue ler.

**A SOLUCAO OBRIGATORIA**: O CSS do material DEVE incluir regras que forcam `color: #1a1a2e !important` em TODO elemento de texto dentro de cards com fundo claro em slides escuros. A lista abaixo e o MINIMO — se o material usar QUALQUER classe adicional com fundo claro, ela DEVE ser adicionada:

```css
/* REGRA ANTI-TEXTO-INVISIVEL — OBRIGATORIO EM TODO MATERIAL */
.slide-dark .checklist li,
.slide-dark .check-item,
.slide-dark .check-label,
.slide-dark .roleplay-body p,
.slide-dark .roleplay-body,
.slide-dark .roleplay-scenario,
.slide-dark .roleplay-card p,
.slide-dark .roleplay-card,
.slide-dark .comp-q,
.slide-dark .comp-q p,
.slide-dark .comp-answer,
.slide-dark .fill-item label,
.slide-dark .fill-item p,
.slide-dark .error-card p,
.slide-dark .err-item p,
.slide-dark .err-item,
.slide-dark .oral-item p,
.slide-dark .oral-item,
.slide-dark .email-card,
.slide-dark .email-card p,
.slide-dark .boarding-pass p,
.slide-dark .student-id-card p,
.slide-dark .dialogue-card,
.slide-dark .dialogue-card p,
.slide-dark .dialogue-line,
.slide-dark .dialogue-line p,
.slide-dark .dialogue-text,
.slide-dark .dialogue-name,
.slide-dark .qc-card,
.slide-dark .qc-card p,
.slide-dark .qc-scenario,
.slide-dark .qc-question,
.slide-dark .grammar-table,
.slide-dark .grammar-table td,
.slide-dark .grammar-table th,
.slide-dark .grammar-box,
.slide-dark .grammar-box p,
.slide-dark .vocab-card-ic,
.slide-dark .vocab-card-ic p,
.slide-dark .slide-card,
.slide-dark .slide-card p,
.slide-dark .slide-card li,
.slide-dark .slide-card h4,
.slide-dark .slide-card h5,
.slide-dark [style*="background:#fff"] p,
.slide-dark [style*="background:#fff"] li,
.slide-dark [style*="background:#fff"] h4,
.slide-dark [style*="background:#fff"] h5,
.slide-dark [style*="background:white"] p,
.slide-dark [style*="background:rgba(255"] p {
    color: #1a1a2e !important;
}
```

**CHECKLIST DE CONTRASTE PRE-DEPLOY (BLOQUEANTE — ZERO TOLERANCIA):**
1. Abrir CADA slide no navegador
2. Em CADA slide escuro (fundo escuro/gradiente), verificar TODOS os cards/caixas internas
3. Se existir QUALQUER texto invisivel (branco sobre branco): PARAR, CORRIGIR, SO ENTAO continuar
4. Rodar este comando para detectar classes potencialmente afetadas:
```bash
# Encontrar todos os elementos com fundo claro dentro de slides
grep -oP 'class="[^"]*"' ARQUIVO.html | sort -u | while read cls; do echo "$cls"; done
# Cruzar com as regras .slide-dark no CSS — se faltar alguma, ADICIONAR
```
5. NUNCA usar `color:rgba(255,255,255,...)` ou `color:#fff` ou `color:white` em elementos dentro de cards com fundo branco/claro
6. Na DUVIDA, adicionar a regra `.slide-dark .CLASSE { color: #1a1a2e !important; }` — excesso de regra nao quebra nada, falta de regra cria texto invisivel

> **LEMBRETE FINAL**: Se voce esta gerando um slide com QUALQUER card/caixa de fundo claro dentro de um slide escuro, PARE e pergunte: "o texto deste card vai herdar branco do slide pai?" Se a resposta for sim ou talvez, ADICIONE a regra CSS. SEMPRE. SEM EXCECAO.

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
- **1.1 Vocab Cards** com audio (`speakText`). A0-A1: com traducao PT. A partir do A2: definicao em ingles simples, ZERO portugues — **OBRIGATORIO**
- **1.2 Matching** (dropdown `checkMatch`) — opcoes EMBARALHADAS — **OBRIGATORIO**
- **1.3 Contexto** — texto curto usando o vocabulario + quiz de compreensao (`selectQuiz`). Formato: "Stage 1.2: Grammar in Context" com badge GRAMMAR, texto narrativo usando a gramatica da aula com palavras em **negrito**, seguido de perguntas de compreensao — **OBRIGATORIO, NUNCA PULAR**
- **1.4 Explicacao Gramatical** — A0-A1: bilingue (EN + PT-BR). A partir do A2: 100% em ingles. Formato: "Grammar Tip" com tabela/explicacao da estrutura gramatical, exemplos afirmativo/negativo/interrogativo — **OBRIGATORIO, NUNCA PULAR**
- **1.5 Aplicacao** — fill-in-the-blank (`checkBlank`) com hints e audio — **OBRIGATORIO**

> **CHECKLIST DE VERIFICACAO**: Antes de considerar UMA aula pronta, confirmar que existem no HTML: (1) vocab cards com audio, (2) match-grid com dropdown, (3) texto "Grammar in Context" com quiz, (4) "Grammar Tip" com explicacao (bilingue so para A0-A1, ingles para A2 em diante), (5) fill-in-the-blank. Se QUALQUER um faltar → a aula NAO esta pronta.

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

- **Vozes ElevenLabs (ATRIBUICAO POR GENERO)**:
  - **Arthur** (`sfJopaWaOtauCD3HKX6Q`): Male, neutral American
  - **Ellen** (`BIvP0GN1cAtSRTxNHnWS`): Female, calm American
  - **Regra de atribuicao**:
    - Palavras soltas (1-2 palavras): voz do GENERO DO ALUNO (aluna=Ellen, aluno=Arthur)
    - Exercicios onde o aluno e protagonista (speech cards, survival, pratica): voz do GENERO DO ALUNO
    - Dialogos: voz do GENERO DO PERSONAGEM (personagem feminina=Ellen, masculino=Arthur)
    - Frases gerais sem personagem (exemplos, contexto): ALTERNAR Arthur/Ellen
  - **NUNCA usar uma unica voz para todo o material**
  - O genero do aluno vem do campo `sexo` do Perfil 360 (ou `vozAluno` se disponivel)
- **Formato**: MP3
- **Diretorio**: `/audio/{slug}/`
- **Nomenclatura**: frase em snake_case sem acentos, max 60 chars
- **ZERO TOLERANCIA com Web Speech API**: TODOS os audios DEVEM ser gerados via ElevenLabs e existir como MP3 no disco. Web Speech API e APENAS fallback de emergencia, NUNCA metodo principal. Se o diretorio `/audio/{slug}/` nao existir ou estiver vazio, o material NAO esta pronto para deploy
- **Speed control**: `currentAudio.playbackRate = audioSpeed`
- **Validacao pre-deploy**: Contar speakText() no HTML e comparar com arquivos em `/audio/{slug}/`. Se houver QUALQUER frase sem MP3 correspondente → BLOQUEAR deploy

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

## REGRA 10.5 — AVISO DE AUTO-VERIFICACAO (OBRIGATORIO)

> **ATENCAO, CLAUDE:** Voce TEM TENDENCIA a esquecer regras durante geracoes longas. Isso ja aconteceu MULTIPLAS VEZES e causou retrabalho. Voce NAO pode confiar que "lembrou de tudo" durante a geracao. ANTES de declarar qualquer aula como completa, voce DEVE executar o checklist abaixo DE FORMA EXPLICITA (rodar grep, contar elementos, verificar arquivos). NAO basta "achar" que esta certo. PROVE com comandos.

### CHECKLIST DE AUTO-VERIFICACAO (rodar ANTES de cada deploy de aula):

```bash
# 1. ACENTUACAO — grep por palavras PT sem acento (deve retornar 0)
grep -c "evolucao\|comunicacao\|voce\b\|nao \|ingles\b\|Profissao\|situacao\|correcao\|Transicao\|producao\|gramatica\|pratica" ARQUIVO.html

# 2. STAMPS — contar stamps vs aulas (devem ser iguais)
grep -c 'class="stamp"' ARQUIVO.html  # deve = numero de aulas
grep -c 'lesson-card' ARQUIVO.html    # deve = numero de aulas

# 3. AUDIO COVERAGE — zero missing
python3 -c "import re,os; [print(p) for p in set(re.findall(r'\"/audio/SLUG/[^\"]+\"', open('ARQUIVO.html').read())) if not os.path.exists('public'+p.strip('\"'))]"

# 4. SLIDES — contar slides e data-teacher
grep -c 'data-slide=' ARQUIVO_INCLASS.html   # deve >= 32 para 90min
grep -c 'data-teacher=' ARQUIVO_INCLASS.html  # deve = numero de slides

# 5. EXERCICIOS — verificar tipos presentes no Pre-class
grep -c 'checkBlank\|selectQuiz\|checkMatch\|checkOrder\|startRecording\|startFreeRecording' ARQUIVO.html

# 6. CLASSES CORRETAS — zero classes inventadas no IN CLASS
grep -c 'vocab-card-ic' ARQUIVO_INCLASS.html  # deve > 0
grep -c 'data-exercise' ARQUIVO_INCLASS.html   # deve = 0

# 7. ESTRUTURA — slides-wrapper fora do main-content
grep -n 'main-content\|slides-wrapper' ARQUIVO_INCLASS.html
```

Se QUALQUER check falhar: PARAR, CORRIGIR, RODAR DE NOVO. So declarar completo quando TODOS passarem.

---

## REGRA 11 — CHECKLIST FINAL BLOQUEANTE (PRE-DEPLOY)

NENHUM material e "pronto" sem passar por TODOS os 7 checks:

1. **Portugues/Acentuacao** — Zero palavras sem acento correto nas traducoes
2. **Ingles** — Gramatica perfeita, American English 100%
3. **Nivel x Aula** — Conteudo adequado ao CEFR do aluno
4. **Audios ElevenLabs** — TODAS as frases com `speakText`/`data-phrase` tem MP3 no `audioMap`. ZERO fallback Web Speech como metodo principal
5. **Funcionalidade** — Zero `data-exercise`. HTML manual com checkBlank/selectQuiz/etc.
6. **Etapas Completas (REGRA 4)** — CADA aula DEVE conter: (a) Vocab Cards, (b) Matching, (c) Grammar in Context com texto + quiz, (d) Grammar Tip com explicacao bilingue, (e) Fill-in-the-blank, (f) Pratica, (g) Pronuncia, (h) Quiz Situacional, (i) Producao Livre. Buscar no HTML por "Grammar in Context" e "Grammar Tip" — se NAO encontrar em TODAS as aulas, REJEITAR.

7. **IN CLASS Completa** — Aba IN CLASS DEVE ter: (a) minimo 25 slides para 60min / 35 para 90min, (b) narrativa com 7 capitulos, (c) reveal cards no vocab, (d) grammar discovery, (e) dialogo line-by-line, (f) 2+ listenings com play/pause, (g) quick fire uma por vez, (h) 3 role-plays (guided>semi-free>free), (i) What I Learned checklist checkbox (NUNCA survival card no IN CLASS — survival card e APENAS no Pre-class), (j) icone T com instrucoes em TODOS os slides, (k) ZERO portugues na tela, (l) TODOS os audios no audioMap (zero missing), (m) aba IN CLASS DEVE mostrar menu de selecao de aula primeiro — NUNCA entrar em slide-mode direto no switchTab. O switchTab SEMPRE remove slide-mode. Slides so abrem via enterSlideMode() chamado por click explicito no menu

8. **Separacao de Aulas (multi-aula)** — Se o material tem 2+ aulas: (a) TODOS os slides tem `data-lesson="N"`, (b) `lessonRanges` no JS cobre todas as aulas com start/end corretos, (c) `changeSlide()` respeita bounds da aula atual, (d) contador mostra numero relativo ("01/27" nao "28/135"), (e) TODOS os cards do menu IN CLASS tem formato HTML IDENTICO (mesmo border-radius, mesmo layout, mesmo padrao de numero 2 digitos "01"/"02"). NUNCA misturar estilos entre cards.

9. **Uniformidade Visual** — Componentes repetidos (cards de menu, lesson cards, exercise sections) DEVEM ter o MESMO HTML/CSS em TODAS as instancias. Se aula 1 usa border-radius:8px e font-weight:600, aula 5 DEVE usar o mesmo. Verificar: comparar o HTML do primeiro e ultimo item de cada componente repetido — devem ser identicos exceto pelo conteudo.

10. **CSS Visual Completo (BLOQUEANTE)** — TODA classe CSS usada nos slides IN CLASS DEVE ter regras CSS definidas no `<style>` do arquivo. Verificar ANTES de declarar qualquer aula como pronta:
    - `vocab-card-ic` com `.vocab-back { opacity:0; max-height:0 }` (reveal cards)
    - `primary-btn` com estilo de botao (Next Line, Reveal the Rule)
    - `lp-player`, `lp-skip`, `lp-seekbar-fill`, `lp-speed-row` (listening player)
    - `slide-section-title` (titulos de secao nos slides)
    - `dialogue-name` (nome do personagem no dialogo)
    - `comp-answer` (resposta escondida em comprehension questions)
    - `.slide-dark .comp-q { background:#fff!important }` (contraste em slides escuros)
    - NUNCA inventar classe nova sem CSS correspondente — usar classes do template
    - **Comando de verificacao**: `grep -oP 'class="[^"]*"' SLIDES_HTML | sort -u` e confirmar que TODAS existem no CSS

Se QUALQUER check falhar → REJEITAR → corrigir → re-validar → so entao deploy.

> **LEMBRETE**: O erro mais comum e pular as etapas 1.3 (Grammar in Context) e 1.4 (Grammar Tip) no Pre-class. Isso ja aconteceu antes e NAO pode se repetir. SEMPRE verificar.
> **LEMBRETE 2**: O segundo erro mais comum e criar slides IN CLASS com classes CSS que nao tem regras definidas (vocab-card-ic sem CSS de reveal, primary-btn sem estilo, comp-q ilegivel em slides escuros). Isso causou retrabalho massivo em 62 arquivos. NUNCA entregar aula sem verificar renderizacao visual de TODOS os slides.
> **LEMBRETE 3 (CRITICO)**: O TERCEIRO erro mais recorrente — e o mais IRRITANTE — e TEXTO BRANCO SOBRE FUNDO BRANCO em cards dentro de slides escuros. Acontece TODA VEZ que um card com background claro (dialogue, role-play, comprehension, quiz, grammar) fica dentro de um `.slide-dark`. O texto herda `color:#fff` do slide pai e fica INVISIVEL. ANTES de declarar qualquer aula pronta, ABRIR CADA SLIDE no navegador e verificar que NAO existe texto invisivel. Se encontrar: adicionar `.slide-dark .CLASSE { color: #1a1a2e !important; }` no CSS. Material com texto invisivel = NAO PUBLICAR.

---

## REGRA 12 — MATERIAIS ATIVOS SAO INTOCAVEIS

- NUNCA modificar HTMLs de alunos com status ATIVO no dashboard
- NUNCA remover funcoes existentes de `design-system.css`
- NUNCA renomear funcoes JS existentes
- Mudancas sao testadas em materiais novos PRIMEIRO
- So migrar materiais ativos quando EXPLICITAMENTE pedido

---

## REGRA 13 — ADAPTACAO POR NIVEL CEFR

> **REGRA DE IDIOMA**: Portugues e permitido APENAS nos niveis A0 e A1 (traducoes, grammar tip bilingue, survival card bilingue). A partir do A2, ZERO portugues em QUALQUER parte do material — vocab cards, grammar tip, survival card, exercicios, microcopy. Unica excecao: instrucoes ao professor via icone T (invisivel ao aluno).

| Nivel | Vocab NOVO | Total circulando | Traducao | Frases | Gramatica |
|-------|-----------|-----------------|----------|--------|-----------|
| A0 | 4-5 palavras/aula | 10 | 100% bilingue (EN+PT) | 2-4 palavras | To be, subject pronouns |
| A1 | 5-7 palavras/aula | 10-12 | 100% bilingue (EN+PT) | 4-6 palavras | Present simple, possessives |
| A2 | 6-8 palavras/aula | 10-12 | ZERO portugues | 5-8 palavras | Past simple, can/could |
| B1 | 7-9 palavras/aula | 10-12 | ZERO portugues | 8-12 palavras | Present perfect, modals |
| B2 | 10-12 palavras/aula | 10-13 | ZERO portugues | Textos completos | Conditionals, passive |
| C1/C1+ | 10-12 palavras/aula | 10-13 | ZERO portugues | Textos complexos | Nuances, register |

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

Ao final de cada aula, incluir card com 5 frases-chave + audio. Survival Card existe em TODOS os niveis.

**Idioma**: A0-A1 = bilingue (EN + PT). A partir do A2 = apenas ingles (sem `sp-pt`).

Exemplo A0-A1 (com traducao):
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

Exemplo A2 em diante (sem traducao):
```html
<div class="survival-card">
    <h4>Survival Card — Lesson {N}</h4>
    <div class="survival-phrase">
        <span class="sp-num">1</span>
        <span class="sp-en">Could you repeat that, please?</span>
        <button class="btn btn-listen" onclick="speakText('Could you repeat that, please?', this)">&#9835;</button>
    </div>
</div>
```

---

## REGRA 17 — MEDIA CARDS (Complementares)

3 recomendacoes por aula: serie/filme + podcast + YouTube

**REGRAS OBRIGATORIAS:**

1. **Subtitulo por bloco**: Antes de cada media-grid, incluir `<p>` com o tema da aula para dar contexto ao aluno
2. **Episodio/video ESPECIFICO**: NUNCA recomendar canal ou show generico. SEMPRE especificar episodio exato (Season X, Episode Y), video especifico (titulo completo), ou numero do episodio do podcast
3. **Conexao com a aula**: Cada card DEVE explicar O QUE o aluno vai ver/ouvir que se conecta com o vocabulario/gramatica daquela aula especifica. Citar frases ou estruturas que aparecem no conteudo recomendado
4. **Link clicavel OBRIGATORIO para YouTube**: Todo card de YouTube DEVE ter link direto para o video. Usar WebSearch para encontrar o video REAL no YouTube ANTES de incluir. Link vai DEPOIS do media-tip, ANTES do fechamento do media-info:
```html
<a href="https://www.youtube.com/watch?v=REAL_ID" target="_blank" rel="noopener" style="display:inline-block;margin-top:.5rem;font-size:.75rem;color:var(--accent);font-weight:600;text-decoration:none;border-bottom:1px solid var(--accent)">Watch on YouTube &#8599;</a>
```
5. **Link clicavel OBRIGATORIO para Podcast**: Todo card de Podcast DEVE ter link do Spotify. Buscar episodio ou show page real:
```html
<a href="https://open.spotify.com/episode/REAL_ID" target="_blank" rel="noopener" style="display:inline-block;margin-top:.5rem;font-size:.75rem;color:var(--accent);font-weight:600;text-decoration:none;border-bottom:1px solid var(--accent)">Listen on Spotify &#8599;</a>
```
6. **Idioma dos links**: SEMPRE em ingles ("Watch on YouTube", "Listen on Spotify"). NUNCA em portugues
7. **Conteudo em INGLES**: Todos os videos e podcasts recomendados DEVEM ser em ingles. NUNCA conteudo em portugues
8. **CONTEUDO 100% REAL (REGRA BLOQUEANTE)**: NUNCA inventar titulo de video, nome de podcast, numero de episodio, ou qualquer conteudo que nao exista. TUDO deve ser verificado com WebSearch ANTES de incluir no material. Se o video/episodio nao for encontrado, buscar um SIMILAR real sobre o mesmo tema. Se nao encontrar NADA real, NAO incluir — e melhor sem link do que com link falso. Isso vale para: titulos de videos YouTube, nomes de episodios de podcast, numeros de episodios (BEP 171, Episode 1496, etc.), nomes de canais, e qualquer outra referencia externa. O aluno vai clicar — se nao existir, perde credibilidade

**Formato do subtitulo por bloco:**
```html
<p style="font-size:.82rem;color:var(--text-dim);margin-bottom:1rem">Tema da aula: {TEMA}. {Instrucao do que prestar atencao}.</p>
```

**Formato completo do card:**
```html
<div class="media-card-wrapper" data-media="l1-series">
    <label class="media-check">
        <input type="checkbox" onchange="toggleMediaDone(this)">
    </label>
    <div class="media-card">
        <div class="media-thumb">{SVG icon}</div>
        <div class="media-info">
            <div class="media-type">Serie</div>
            <h5>Emily in Paris -- Season 1, Episode 1: "Emily in Paris"</h5>
            <p>Emily chega em Paris e se apresenta para a equipe nova. Preste atencao em como ela diz o nome e o cargo: "Hi, I'm Emily. I work at Gilbert Group." Mesmo padrao da aula!</p>
            <p class="media-tip">Dica: Assista com audio em ingles + legendas em portugues. Anote todas as vezes que alguem se apresenta.</p>
        </div>
    </div>
</div>
```

**Exemplo de card YouTube com link:**
```html
<div class="media-card-wrapper" data-media="l1-youtube">
    <label class="media-check"><input type="checkbox" onchange="toggleMediaDone(this)"></label>
    <div class="media-card">
        <div class="media-thumb"><svg viewBox="0 0 24 24"><polygon points="5 3 19 12 5 21 5 3"/></svg></div>
        <div class="media-info">
            <div class="media-type">YouTube</div>
            <h5>English with Lucy -- "How to Describe Your Job in English"</h5>
            <p>Video (12 min) com frases para descrever sua empresa: "We specialize in...", "Our company was founded in..." Estruturas da Aula 3.</p>
            <p class="media-tip">Dica: Assista com legendas em ingles. Tente descrever a SUA empresa usando as mesmas frases.</p>
            <a href="https://www.youtube.com/watch?v=DGvqXvEp9ZA" target="_blank" rel="noopener" style="display:inline-block;margin-top:.5rem;font-size:.75rem;color:var(--accent);font-weight:600;text-decoration:none;border-bottom:1px solid var(--accent)">Watch on YouTube &#8599;</a>
        </div>
    </div>
</div>
```

**CHECKLIST PRE-DEPLOY (Complementares):**
- [ ] Cada aula tem subtitulo com tema antes do media-grid?
- [ ] Cada card tem episodio/video ESPECIFICO (nunca generico)?
- [ ] Cada card conecta o conteudo com vocabulario/gramatica da aula?
- [ ] Todo card YouTube tem link clicavel verificado?
- [ ] Todo card Podcast tem link Spotify verificado?
- [ ] Links em ingles ("Watch on YouTube" / "Listen on Spotify")?
- [ ] Conteudo recomendado e 100% em ingles?

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

## REGRA 20 — UMA AULA POR VEZ + TEMPLATE OBRIGATORIO

> **QUALIDADE > QUANTIDADE**: Gerar UMA aula de cada vez. NUNCA gerar 5 aulas juntas.

**Geracao por aula:**
- Cada execucao gera material de UMA aula apenas (Pre-class + IN CLASS + Complementares)
- O Planejamento mostra o curriculo COMPLETO do programa, mas o conteudo e de UMA aula
- Aula 2 so e gerada apos Aula 1 ser validada e aprovada
- Aula N+1 faz CALLBACK do vocabulario da aula N no warm-up

**Template obrigatorio:**
- NUNCA gerar CSS/JS do zero — SEMPRE copiar de um material aprovado existente
- IN CLASS: copiar estrutura de slides, navegacao, componentes do template (patricia-ruffo.html ou elaine-v-b.html)
- Pre-class: copiar padrao de exercicios do template (checkBlank, selectQuiz, checkMatch)
- Trocar APENAS: accent color + conteudo dos slides + audioMap + data-teacher
- Se nao existir template: usar /public/professor/patricia-ruffo.html como referencia

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

## REGRA 21B — INGLES AMERICANO

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

### Script obrigatorio antes de `</body>` (DEPOIS do script principal):

```html
<script src="/lib/lesson-progress.js"></script>
</body>
```

### Como funciona:
1. `lesson-progress.js` faz wrap automatico do `toggleCheck()` existente
2. Quando o professor marca 5/5 checks no checklist de uma aula → `inclass_done = true` salva no Supabase
3. Ao carregar a pagina, busca do Supabase quais aulas estao concluidas → atualiza barra de progresso + acende stamps + restaura checks visuais
4. Tabela Supabase: `lesson_progress` (student_slug, lesson_number, inclass_done, inclass_marked_at)

### Variaveis para substituir:

| Placeholder | Substituir por |
|---|---|
| `{SLUG}` | Slug do aluno (ex: `gabriela-pires`) |
| `{N}` | Total de aulas no pacote do aluno (ex: `48`) |

### IMPORTANTE:
- O `lesson-progress.js` DEVE ser carregado DEPOIS do `<script>` principal (que define `toggleCheck`)
- O `STUDENT_SLUG` DEVE ser o slug PRINCIPAL do aluno (sem sufixo `-aula2` etc.)
- Nunca editar `lesson-progress.js` para um aluno especifico — ele e GENERICO
- A barra de progresso mostra: aulas com `inclass_done=true` / TOTAL_AULAS * 100

---

## REGRA 29 — STAMPS ACOMPANHAM AULAS (OBRIGATORIO)

> Toda vez que uma nova aula e criada, o stamp correspondente DEVE ser adicionado na `stamps-row` do header. Stamps faltando e um BUG que BLOQUEIA deploy.

### Regras:

1. **1 aula = 1 stamp**: Cada `lesson-card` (ex: `ex-lesson-7`) DEVE ter um stamp correspondente (`stamp7`) na `stamps-row` do header
2. **Mesma imagem**: O stamp DEVE usar a MESMA imagem do `lesson-header-img` da lesson-card do aluno, trocando apenas `w=600` por `w=200`
3. **Label curta**: O `data-label` do stamp deve ser uma versao curta do tema da aula (1-2 palavras, ex: "Hotel", "Directions", "Paris")
4. **Ambos os arquivos**: Stamp deve ser adicionado TANTO no arquivo do professor quanto no do aluno
5. **`totalLessons` atualizado**: O `var totalLessons` no JavaScript DEVE ser atualizado para refletir o numero total de aulas existentes
6. **Ordem sequencial**: Stamps devem seguir a ordem das aulas (stamp1 = aula 1, stamp2 = aula 2, etc.)

### Formato do stamp:
```html
<div class="stamp" id="stamp{N}" data-label="{LABEL_CURTA}" style="background-image:url('{MESMA_URL_DO_LESSON_CARD}?w=200&q=80')"></div>
```

### Checklist ao criar nova aula (ADICIONAR aos checks existentes):
- [ ] Stamp adicionado na `stamps-row` do aluno?
- [ ] Stamp adicionado na `stamps-row` do professor?
- [ ] Imagem do stamp = mesma do lesson-header-img (com w=200)?
- [ ] `totalLessons` atualizado nos dois arquivos?
- [ ] Stamps existentes NAO foram alterados?

---

## REGRA 30 — CONTROLE DE AULAS (OBRIGATORIO)

> Todo material de professor e aluno DEVE incluir o sistema de Controle de Aulas. Ele injeta automaticamente uma aba "CONTROLE DE AULAS" que permite ao professor registrar datas e feedbacks, e ao aluno dar feedback sobre aulas e material. Os dados ficam no Supabase (tabela `controle_aulas`).

### Script obrigatorio antes de `</body>` (DEPOIS do lesson-progress.js):

```html
<script src="/lib/lesson-progress.js"></script>
<script src="/lib/controle-aulas.js"></script>
</body>
```

### Como funciona:

1. O script detecta automaticamente se e pagina de professor ou aluno (pela badge)
2. Le o curriculo do aluno do Supabase (`perfis.data.curriculo`) para montar a lista de aulas
3. Injeta a aba "CONTROLE DE AULAS" na barra de tabs existente
4. **Professor ve**: # | Tema | Data da aula (editavel) | Feedback do aluno (textarea) | Feedback do material (textarea)
5. **Aluno ve**: # | Tema | Data da aula (somente leitura, propagada do professor) | Feedback da aula (textarea) | Feedback do material (textarea)
6. Auto-save com debounce 1.5s — salva no Supabase via upsert
7. Tabela Supabase: `controle_aulas` (student_slug, lesson_number, aula_date, prof_feedback_aluno, prof_feedback_material, aluno_feedback_aula, aluno_feedback_material, updated_at)

### Requisitos no HTML hospedeiro:

- `window.STUDENT_SLUG` definido no `<head>`
- `supabase-config.js` carregado
- `switchTab()` existente (generico — ja funciona com qualquer tabId)

### IMPORTANTE:

- O script e 100% aditivo — NAO altera nenhum HTML, CSS ou JS existente
- NAO requer mudanca no `switchTab()` ou em nenhuma outra funcao
- DEVE ser incluido em AMBOS os arquivos (professor e aluno)
- A aba so aparece se o script estiver presente — materiais sem o script continuam identicos

---

## REGRA 31 — QA DE PROFESSORES: ERROS RECORRENTES (BLOQUEANTE)

> Regras derivadas de feedback real de professores em aula. TODAS sao OBRIGATORIAS e devem ser verificadas ANTES de declarar qualquer aula como pronta.

### A. Instrucoes de interacao: "Click on" (NUNCA "Click each")
- ERRADO: "Click each card to reveal"
- CERTO: "Click on each card to reveal"
- Verificar TODAS as instrucoes de slide antes de deploy

### B. Personalizacao: "you/your" quando aluno e protagonista
- Quando o material simula uma situacao PROTAGONIZADA pelo aluno, usar "you/your"
- NUNCA tratar o aluno em 3a pessoa como se fosse outra pessoa
- ERRADO: "Listen to Dr. Ruffo delivering her keynote" / "How did Patricia respond?"
- CERTO: "Listen to you, Dr. Ruffo, delivering your keynote" / "How did you respond?"
- Aplica-se a: listenings protagonizados, comprehension questions sobre o aluno, instrucoes de role-play

### C. Voz ElevenLabs = genero do aluno quando e protagonista
- Se o listening/audio simula a fala DO ALUNO (keynote, networking, apresentacao), a voz DEVE ser do genero do aluno
- Aluna = Ellen, Aluno = Arthur
- NUNCA voz masculina para simular fala de aluna (e vice-versa)
- Isso se soma a regra existente de alternancia (frases gerais alternam; protagonista = genero do aluno)

### D. Scroll reset OBRIGATORIO ao navegar slides
- `goToSlide()` DEVE incluir `slides[currentSlide].scrollTop = 0`
- Sem isso, ao retornar a um slide ja scrollado, o topo fica cortado
- Aplica-se a TODOS os materiais IN CLASS

### E. Conteudo NUNCA cortado atras do top-bar
- Slides com conteudo longo (pronuncia 10 itens, oral drilling, dialogo completo) podem ter o primeiro item escondido
- `padding-top` DEVE ser >= 4.5rem nos slides
- Centralizar com `::before/::after { flex:1 }` (NUNCA `justify-content:center` que corta overflow no topo)
- VERIFICACAO: abrir slides com muito conteudo e confirmar que o PRIMEIRO item e visivel

### F. Spot the Error: erro INVISIVEL antes do click
- A classe `.wrong` NAO pode ter estilo visual (line-through, cor vermelha) no estado padrao
- O destaque do erro so aparece DEPOIS do click: `.err-item.open .wrong { text-decoration:line-through; color:#f87171; }`
- Estado padrao: `.wrong { color:inherit; text-decoration:none; }`

### G. Quick Challenge: navegacao completa
- Contador de progresso: "Challenge N / total" (alem do score)
- Botao "Previous" em TODOS os cards exceto o primeiro
- Ultimo card NAO tem "Next Question" (evita tela vazia 6/6)
- `nextQc()` DEVE ter guard: `if (qcCurrent >= cards.length - 1) return`
- `prevQc()` DEVE existir com guard: `if (qcCurrent <= 0) return`

### H. Contexto de aula presencial vs autonoma
- Se o material e usado com professor (compartilhado no Zoom), instrucoes de "record yourself" ficam deslocadas
- Preferir: "Deliver your presentation to your teacher" em vez de "Record your presentation"
- Slides de producao livre devem considerar que o PROFESSOR esta presente

### I. Consistencia de volume entre audios
- Audios no mesmo slide/secao DEVEM ter volume consistente
- Quando alternar vozes (Arthur/Ellen), manter MESMOS `voice_settings` (stability, similarity_boost)
- Se um audio soa mais alto que os demais, regenerar com a voz correta da alternancia

### J. Vocab reveal cards DEVEM ser toggle
- `classList.toggle('revealed')` — NUNCA `classList.add` sem toggle
- Clicar abre, clicar de novo FECHA
- Professora deve conseguir fechar se clicar sem querer

### CHECKLIST PRE-DEPLOY (REGRA 31):
```bash
# Verificar "Click each" sem "on"
grep -n "Click each" ARQUIVO.html  # deve retornar 0

# Verificar nome do aluno em comprehension/listening (3a pessoa)
grep -n "Listen to.*[NOME]" ARQUIVO.html  # verificar se deveria ser "you"
grep -n "How did.*[NOME]" ARQUIVO.html    # verificar se deveria ser "you"
grep -n "What did.*[NOME]" ARQUIVO.html   # verificar se deveria ser "you"

# Verificar scroll reset
grep -n "scrollTop" ARQUIVO.html  # deve existir no goToSlide

# Verificar erro visivel antes do click
grep -n "class=\"wrong\"" ARQUIVO.html  # verificar CSS correspondente

# Verificar Quick Challenge guards
grep -n "nextQc\|prevQc" ARQUIVO.html  # ambos devem existir
```

---

## REGRA 32 — PERSISTENCIA PRE-CLASS NO SUPABASE (OBRIGATORIO)

> TUDO que o aluno faz no Pre-class DEVE ser salvo automaticamente no Supabase. Qualquer pessoa, de qualquer lugar, de qualquer dispositivo, DEVE ver o mesmo estado de progresso. Nada pode ficar apenas em localStorage.

### Como funciona:

1. O script `activity-sync.js` intercepta TODA interacao do aluno no Pre-class: matching, fill-in-the-blank, quiz, ordering, gravacao de audio
2. Cada acao salva no Supabase (tabela `student_activity`) com debounce de 2 segundos
3. Ao abrir a pagina de qualquer dispositivo, o sistema compara timestamp local vs Supabase — se Supabase e mais recente, restaura de la
4. Gravacoes de audio fazem upload no Supabase Storage (bucket `recordings`) e ficam acessiveis de qualquer lugar
5. Fallback: auto-save a cada 30s + `beforeunload` com `keepalive: true`

### Scripts obrigatorios (NESTA ORDEM no final do `<body>`):

```html
<script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2/dist/umd/supabase.min.js"></script>
<script src="/lib/supabase-config.js"></script>
<script src="/lib/lesson-progress.js"></script>
<script src="/lib/controle-aulas.js"></script>
<script src="/lib/activity-sync.js"></script>
```

E no `<head>`, ANTES de tudo:
```html
<script>window.STUDENT_SLUG='{SLUG}';window.TOTAL_AULAS={N};</script>
```

### IMPORTANTE:
- `activity-sync.js` DEVE ser o ULTIMO script (depende de todos os outros)
- `supabase.min.js` DEVE vir ANTES de `supabase-config.js`
- Se QUALQUER um dos 5 scripts faltar, o material NAO pode ser publicado — e um BUG BLOQUEANTE
- O botao "Reset Lesson N" so aparece na view ALUNO, nunca no professor
- NUNCA confiar apenas em localStorage — o Supabase e a fonte de verdade

---

## REGRA 33 — BARRA DE PROGRESSO PRE-CLASS POR AULA (OBRIGATORIO)

> Cada lesson card do Pre-class DEVE ter uma mini-barra de progresso que reflete o percentual REAL de exercicios concluidos naquela aula. Conforme o aluno completa exercicios, o % sobe automaticamente.

### Como funciona:

1. `activity-sync.js` faz wrap da funcao `updateProgress()` do JS inline
2. Para cada lesson card, calcula quantos exercicios foram concluidos (matching + fill-in + quiz + speech + ordering) dividido pelo total de exercicios daquela aula
3. Atualiza visualmente a `mini-bar-fill` e o `mini-percent` com o percentual real
4. 100% dos exercicios concluidos = aula Pre-class completa

### HTML obrigatorio em cada lesson card:

```html
<div class="mini-progress-bar" data-lesson-progress="{N}">
  <div class="mini-bar-fill" style="width:0%"></div>
  <span class="mini-percent" data-lesson-pct="{N}">0%</span>
</div>
```

### Requisitos:
- Cada lesson card DEVE ter `id="ex-lesson-{N}"` para o calculo funcionar
- A mini-barra DEVE comecar em 0% e subir conforme o aluno interage
- O percentual e calculado AUTOMATICAMENTE — nunca hardcoded
- O estado persiste no Supabase (via REGRA 32) — ao reabrir, a barra mostra o progresso salvo
- TODOS os tipos de exercicio contam: matching, fill-in-the-blank, quiz, speech recording, ordering
