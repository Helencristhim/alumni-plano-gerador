# Referencia FAAP — Padrao de Qualidade Pedagogica e UX

> Documento de referencia para o padrao de qualidade de exercicios interativos.
> Referenciado por: gerador de material

---

## Visao Geral

O projeto FAAP English Hub e a referencia de qualidade para exercicios
interativos da Alumni. Todo material gerado deve seguir o mesmo nivel
de polish, microcopy e estrutura pedagogica desse projeto.

---

## URLs de Referencia

- https://faap-english-hub.vercel.app/starter/future-me/careers/2
- https://faap-english-hub.vercel.app/starter/pop-culture/tv-shows/1

Essas paginas devem ser consultadas como benchmark visual e funcional
antes de implementar qualquer novo tipo de exercicio.

---

## 7 Tipos de Exercicio FAAP

### 1. Matching Dropdown

O aluno associa itens de duas colunas usando menus dropdown.

- Coluna esquerda: termo, frase ou imagem (fixo)
- Coluna direita: dropdown com opcoes para selecionar
- Todas as opcoes aparecem em todos os dropdowns (para evitar eliminacao)
- Feedback individual por par (nao espera completar todos)
- Uso: vocabulario, collocations, definicoes

### 2. Fill-in-the-blank Simples

O aluno digita a palavra ou expressao que completa a frase.

- Frase com lacuna claramente marcada (underline ou caixa)
- Aceita variacoes de grafia (ex: "colour" e "color")
- Aceita contrações (ex: "don't" e "do not")
- Nao diferencia maiusculas/minusculas
- Mostra resposta correta apos erro
- Uso: gramatica, vocabulario em contexto, preposicoes

### 3. Fill-in com Dica em Portugues

Variacao do fill-in onde a dica aparece em portugues abaixo da lacuna.

- Frase em ingles com lacuna
- Dica em portugues em texto menor, italico, abaixo da lacuna
- A dica e a traducao da palavra esperada (nao da frase inteira)
- Mesmo comportamento de aceitacao do tipo 2
- Uso: niveis iniciantes, vocabulario novo, reforco de traducao

### 4. Multipla Escolha (4 opcoes)

O aluno seleciona a resposta correta entre 4 alternativas.

- Enunciado claro em ingles (ou bilingue para iniciantes)
- Exatamente 4 opcoes (nunca 3, nunca 5)
- Opcoes de tamanho similar (para nao dar pista visual)
- Distratores plausíveis (erros comuns reais, nao opcoes absurdas)
- Ordem das opcoes aleatorizada a cada tentativa
- Feedback explica por que a correta e correta (nao so "errado")
- Uso: compreensao, gramatica, vocabulario, interpretacao

### 5. Ordering (Reordenar)

O aluno arrasta palavras ou frases para a ordem correta.

- Palavras/frases apresentadas embaralhadas
- Interface de drag-and-drop com areas numeradas
- Alternativa de toque (tap para selecionar, tap destino para colocar)
- Feedback mostra posicoes corretas e incorretas
- Uso: word order, sequencia logica, storytelling, instrucoes

### 6. Pronuncia Avaliada (Microfone)

O aluno grava a pronuncia de uma frase e recebe avaliacao automatica.

- Frase modelo exibida com audio de referencia (botao ouvir)
- Botao de gravacao grande e central
- Gravacao com limite de tempo (5-15 segundos)
- Avaliacao por fonema com destaque visual:
  - Verde: pronuncia correta
  - Amarelo: aceitavel mas pode melhorar
  - Vermelho: precisa de atencao
- Score geral de 0-100
- Opcao de regravar ilimitada
- Uso: palavras dificeis, frases funcionais, entonacao

### 7. Gravacao Livre — Think About It

O aluno grava uma resposta livre a uma pergunta aberta.

- Pergunta provocadora exibida em destaque
- Sem avaliacao automatica de corretude
- Gravacao de ate 60 segundos
- Playback disponivel para o aluno se ouvir
- Transcricao automatica exibida abaixo (para autoavaliacao)
- Professor recebe gravacao + transcricao para feedback posterior
- Uso: reflexao, opiniao, pratica de fluencia, confianca

---

## Microcopy Obrigatorio

Cada secao da aula deve ter microcopy padronizado. Exemplos:

### Introducao da aula
- Titulo: `"Lesson 3: Careers That Shape the Future"`
- Subtitulo: `"Let's explore vocabulary and ideas about modern careers."`

### Instrucao de exercicio
- Matching: `"Match each word to its definition."`
- Fill-in: `"Complete the sentence with the correct word."`
- Fill-in com dica: `"Complete with the correct word. The hint is in Portuguese."`
- Multipla escolha: `"Choose the best option."`
- Ordering: `"Put the words in the correct order."`
- Pronuncia: `"Listen, then record yourself saying the phrase."`
- Think about it: `"Think about it. Record your answer."`

### Feedback de acerto
- `"Nice job!"` ou `"Boa!"` (alternados)
- `"That's correct!"` ou `"Exactly!"`
- `"Well done!"` ou `"Perfect!"`

### Feedback de erro
- `"Not quite. The correct answer is [X]."`
- `"Almost! Try again."` (quando ha segunda tentativa)
- `"Quase. A resposta certa e [X]."`

### Transicao entre secoes
- `"Great! Let's move on."` ou `"Now let's practice."`
- `"Ready for the next one?"` ou `"Keep going!"`

### Conclusao
- `"You completed this lesson! Here's your summary."`
- `"Parabens! Voce concluiu esta aula."`

---

## Estrutura Obrigatoria de Cada Aula

Toda aula gerada deve conter estes 11 elementos, nesta ordem:

1. **Header** — Numero da aula, titulo, icone tematico
2. **Warm-up** — Pergunta aberta em portugues para ativar contexto (30s)
3. **Vocabulary** — 5-8 palavras/expressoes com audio, definicao, exemplo
4. **Vocabulary Practice** — 2-3 exercicios usando o vocabulario apresentado
5. **Context** — Texto curto (80-150 palavras) usando o vocabulario em contexto
6. **Comprehension** — 2-3 exercicios sobre o texto de contexto
7. **Grammar Spotlight** — Ponto gramatical em destaque com exemplos claros
8. **Grammar Practice** — 2-3 exercicios sobre o ponto gramatical
9. **Pronunciation** — 2-3 frases para gravacao com audio modelo
10. **Think About It** — Gravacao livre com pergunta provocadora
11. **Wrap-up** — Resumo visual do que foi aprendido + mensagem motivacional

---

## Microinteracoes Obrigatorias

### Acerto
- Cor: verde (`#22c55e`)
- Icone: check (Lucide `check-circle`)
- Texto: `"Boa!"` ou `"Nice job!"`
- Animacao: fade in 200ms + leve scale up
- Som: feedback positivo sutil (opcional)

### Erro
- Cor: vermelho (`#ef4444`)
- Icone: X (Lucide `x-circle`)
- Texto: `"Quase."` ou `"Not quite."`
- Animacao: shake horizontal (3 ciclos, 150ms total)
- Exibe resposta correta apos 500ms
- Som: feedback neutro sutil (opcional, nunca punitivo)

### Estados de transicao
- Entre exercicios: fade out 200ms + fade in 200ms
- Progresso: barra no topo atualiza com ease-out 300ms
- Scroll automatico para proximo exercicio apos feedback

---

## Principios de Design FAAP

1. **Clareza acima de tudo** — O aluno nunca deve ter duvida sobre o que fazer
2. **Bilingue quando necessario** — Instrucoes em ingles, dicas em portugues
3. **Feedback imediato** — Nunca mais que 200ms entre acao e resposta
4. **Progresso visivel** — O aluno sempre sabe onde esta e quanto falta
5. **Mobile first** — Todo exercicio funciona perfeitamente em tela pequena
6. **Acessivel** — Navegavel por teclado, leitores de tela, contraste adequado
7. **Bonito** — Design limpo, espacado, tipografia legivel, cores consistentes

---

## Padrão Obrigatório de Exercícios — HTML Manual (NÃO-NEGOCIÁVEL)

### Contexto e Decisão Arquitetural

O exercises.js possui DOIS sistemas de exercícios:

1. **Sistema `data-exercise`** (auto-init via `createElement` + `innerHTML`) — **PROIBIDO USAR**
2. **Sistema HTML manual** (funções fallback: `checkBlank`, `selectQuiz`, etc.) — **OBRIGATÓRIO**

O sistema `data-exercise` gera HTML dinamicamente via `innerHTML` com JavaScript inline em atributos `onclick`. Isso causa bugs críticos:
- SVG icons contêm `<` e `>` que quebram o parser HTML dentro de atributos
- Código JS aparece como texto visível nos exercícios
- Botões "Verificar" não funcionam
- Exercícios de pronúncia mostram código cru

O sistema HTML manual usa funções simples chamadas diretamente do HTML. **Funciona em todos os browsers, todos os alunos, sem exceção.**

### REGRA ABSOLUTA

> **NUNCA usar `<div data-exercise="...">`.**
> **SEMPRE escrever HTML manual com as funções fallback.**
> Referência de implementação: `/public/professor/daniela-feitoza.html`

---

### 1. Matching Dropdown — `checkMatch()` + `verifyAllMatches()`

```html
<div class="exercise-section">
    <h4>V1. Match the words <span class="badge badge-vocab">Vocabulary</span></h4>
    <p class="microcopy">Selecione a tradução correta para cada palavra.</p>
    <div class="match-grid" id="match-l1">
        <div class="match-row" data-answer="nome">
            <span class="match-word">name</span>
            <select onchange="checkMatch(this)">
                <option value="">Select...</option>
                <option value="idade">idade</option>
                <option value="nome">nome</option>
                <option value="cidade">cidade</option>
            </select>
        </div>
        <!-- mais rows com opções EMBARALHADAS -->
    </div>
    <button class="verify-all-btn" onclick="verifyAllMatches('match-l1')">Check Answers</button>
</div>
```

**Regras:**
- **Palavras SEMPRE com inicial maiúscula** nos vocab cards e matching (Finance, Company, Based In)
- **Traduções SEMPRE com inicial maiúscula** (Finanças, Empresa, Sediado Em)
- ID único por aula: `match-l1`, `match-l2`, etc.
- `data-answer` = tradução correta
- Opções embaralhadas (NUNCA resposta na mesma posição)
- `onchange="checkMatch(this)"` valida individualmente
- `verifyAllMatches(id)` valida todos de uma vez

---

### 2. Fill-in-the-Blank — `checkBlank()` + `listenBlank()`

```html
<div class="exercise-section">
    <h4>V2. Complete with the correct word <span class="badge badge-practice">Practice</span></h4>
    <p class="microcopy">Preencha com a palavra certa. Use a dica se precisar.</p>
    <div class="fill-blank-item">
        <div class="fill-blank-sentence">
            "My <input class="blank-input"
                data-answer="name"
                data-hint="Hint: what people call you"
                data-phrase="My name is Maísa."
                placeholder="___"> is Maísa."
        </div>
        <div class="hint-text">Hint: what people call you</div>
        <button class="btn check-btn" onclick="checkBlank(this)">Check</button>
        <button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button>
    </div>
</div>
```

**Regras:**
- `data-answer` = resposta correta (case-insensitive, aceita contrações)
- `data-hint` = dica em INGLÊS (nunca português)
- `data-phrase` = frase completa para áudio
- `data-alt` = resposta alternativa aceita (opcional)
- `checkBlank(this)` valida e mostra feedback
- `listenBlank(this)` toca o áudio da frase completa

---

### 3. Múltipla Escolha — `selectQuiz()`

```html
<div class="exercise-section">
    <h4>P1. Choose the best answer <span class="badge badge-quiz">Quiz</span></h4>
    <div class="quiz-item">
        <div class="quiz-question">How do you say 'Eu trabalho em finanças' in English?</div>
        <div class="quiz-options">
            <div class="quiz-option" tabindex="0" role="button" onclick="selectQuiz(this)" data-correct="true">
                <span class="option-letter">A</span> I work in finance.
            </div>
            <div class="quiz-option" tabindex="0" role="button" onclick="selectQuiz(this)" data-correct="false">
                <span class="option-letter">B</span> I works in finance.
            </div>
            <div class="quiz-option" tabindex="0" role="button" onclick="selectQuiz(this)" data-correct="false">
                <span class="option-letter">C</span> I working in finance.
            </div>
            <div class="quiz-option" tabindex="0" role="button" onclick="selectQuiz(this)" data-correct="false">
                <span class="option-letter">D</span> I am work in finance.
            </div>
        </div>
    </div>
</div>
```

**Regras:**
- Exatamente 4 opções (A/B/C/D)
- `data-correct="true"` na resposta certa, `"false"` nas erradas
- `tabindex="0"` e `role="button"` para acessibilidade
- Distratores plausíveis (erros comuns reais)
- `selectQuiz(this)` marca correto/errado com feedback visual

---

### 4. Ordering — `selectOrderItem()` + `checkOrder()` + `moveItem()`

```html
<div class="exercise-section">
    <h4>P2. Put in order <span class="badge badge-order">Practice</span></h4>
    <p class="microcopy">Organize as palavras na ordem correta.</p>
    <div class="order-container" id="order-l1">
        <div class="order-item" draggable="true" data-order="3"
             onclick="selectOrderItem(this,'order-l1')">
            <span class="order-num">?</span>
            <span class="order-text">is</span>
            <span class="order-arrows">
                <button class="arrow-btn" onclick="event.stopPropagation();moveItem(this,-1,'order-l1')">&#9650;</button>
                <button class="arrow-btn" onclick="event.stopPropagation();moveItem(this,1,'order-l1')">&#9660;</button>
            </span>
        </div>
        <!-- itens embaralhados, data-order = posição correta -->
    </div>
    <button class="btn check-btn" onclick="checkOrder('order-l1')" style="margin-top:1rem;">Check Order</button>
</div>
```

**Regras:**
- ID único: `order-l1`, `order-l2`, etc.
- `data-order` = posição correta (1-based)
- Itens apresentados EMBARALHADOS (ordem no HTML ≠ data-order)
- Suporta drag-and-drop E setas (mobile-friendly)
- `event.stopPropagation()` nos botões de seta

---

### 5. Pronúncia — `speakPhrase()` + `startRecording()` + `stopRecording()`

```html
<div class="exercise-section">
    <h4>S1. Read aloud <span class="badge badge-speak">Speaking</span></h4>
    <p class="microcopy">Ouça a frase, depois grave você falando.</p>
    <div class="speech-card" data-phrase="My name is Maisa. I work in finance.">
        <div class="speech-phrase">My name is Maísa. I work in finance.</div>
        <div class="speech-translation">Meu nome é Maísa. Eu trabalho em finanças.</div>
        <div class="speech-controls">
            <button class="btn btn-listen" onclick="speakPhrase(this)">&#9654; Ouvir</button>
            <button class="btn btn-record" onclick="startRecording(this)">&#9679; Gravar</button>
            <button class="btn btn-stop" onclick="stopRecording(this)">&#9632; Parar</button>
        </div>
        <div class="speech-result"></div>
    </div>
</div>
```

**Regras de HTML:**
- `data-phrase` = texto SEM acentos para comparação de pronúncia (Maisa, não Maísa)
- `.speech-phrase` = texto visual COM acentos para o aluno ler
- `.speech-translation` = tradução em português
- `speakPhrase(this)` toca áudio via audioMap ou Web Speech API
- `startRecording(this)` inicia gravação + reconhecimento + feedback
- `.speech-result` recebe o feedback visual detalhado

**Regras de implementação da função `startRecording` (NÃO-NEGOCIÁVEL):**

O `startRecording` deve OBRIGATORIAMENTE implementar:

1. **Função `analyzeWords(targetStr, spokenStr)`** — Algoritmo LCS (Longest Common Subsequence) que compara palavra por palavra com tolerância via Levenshtein distance (≤1 edit = aceita). Retorna `{ expected, spoken, wrongWords, score }`.

2. **Função `wordsMatch(a, b)`** — Compara palavras considerando contrações (I'm = im) e tolerância Levenshtein.

3. **Feedback visual word-by-word obrigatório:**
   - **WORD-BY-WORD:** cada palavra ESPERADA com ✓ verde (correct) ou ✗ vermelho (missing)
   - **YOU SAID:** cada palavra FALADA com ✓ verde (correct), ✗ vermelho (wrong), ou ~ roxo (extra)
   - **Focus on:** lista das palavras erradas com "(you said X)" mostrando o que o aluno disse

4. **Playback da gravação do aluno:**
   - Usar `MediaRecorder` em PARALELO ao `SpeechRecognition`
   - MediaRecorder inicia PRIMEIRO, SpeechRecognition inicia DENTRO do callback `getUserMedia.then()`
   - Detectar mimeType suportado: `audio/mp4` (Safari) > `audio/webm;codecs=opus` (Chrome) > `audio/webm` > `audio/ogg`
   - Usar `start(100)` para coletar chunks a cada 100ms
   - Após resultado do SpeechRecognition, parar MediaRecorder via `onstop` callback
   - Inserir `<audio controls>` com blob URL no slot reservado APÓS `onstop` (nunca antes)
   - Seção "YOUR RECORDING:" com player para o aluno se ouvir

5. **Regex de limpeza:** usar `/[^a-z0-9' ]/g` com ESPAÇO LITERAL (nunca `\s` que pode ser corrompido por Node.js ao escrever arquivos)

6. **Split de palavras:** usar `.split(/ +/)` com ESPAÇO LITERAL (nunca `/\s+/` que vira `/s+/` quando escrito por Node.js)

7. **CSS obrigatório:**
   - `.speech-result`, `.speech-result.show`, `.speech-result.good/.try-again/.bad`
   - `.word-comparison`, `.comp-label`, `.comp-words`
   - `.word-box`, `.word-box.word-correct`, `.word-box.word-missing`, `.word-box.word-wrong`, `.word-box.word-extra`
   - `.word-box .word-icon`
   - `.speech-suggestion`

**Referência de implementação funcional:** `/public/professor/daniela-feitoza.html` (usa `analyzeWords` + word-by-word completo)

**ERROS CONHECIDOS que NUNCA podem ocorrer:**
- `split(/s+/)` em vez de `split(/ +/)` → junta palavras no "s" (bug: Score 0/2 em frase de 8 palavras)
- `audio/webm` em Safari → Error no player (Safari só aceita `audio/mp4`)
- Criar blob ANTES do `MediaRecorder.onstop` → áudio vazio ou Error
- `innerHTML` do áudio ANTES do blob estar pronto → Error no player

---

### 6. Think About It — `startFreeRecording()` + `stopFreeRecording()`

```html
<div class="exercise-section">
    <h4>T1. Think and respond <span class="badge badge-think">Reflection</span></h4>
    <div class="think-card">
        <div class="think-question" style="margin-bottom:1rem;">
            Think about why you decided to learn English. What changed?
        </div>
        <div class="speech-controls">
            <button class="btn btn-record" onclick="startFreeRecording(this)">&#9679; Gravar Livre</button>
            <button class="btn btn-stop" onclick="stopFreeRecording(this)">&#9632; Parar</button>
        </div>
        <div id="think-result-l1" style="margin-top:0.5rem;"></div>
    </div>
</div>
```

**Regras:**
- Sem avaliação automática (é reflexão, não teste)
- ID único para resultado: `think-result-l1`, `think-result-l2`, etc.
- Gravação salva localmente no dispositivo do aluno
- Pode incluir "Sugestão de resposta" com speech-card para comparação (opcional)

---

### 7. Survival Card — `speakText()`

```html
<div class="survival-card">
    <h4>Survival Card &mdash; Lesson 1</h4>
    <div class="survival-phrase">
        <span class="sp-num">1</span>
        <span class="sp-en">My name is Maísa.</span>
        <span class="sp-pt">Meu nome é Maísa.</span>
        <button class="btn btn-listen" onclick="speakText('My name is Maisa.', this)" style="flex-shrink:0;">&#9654;</button>
    </div>
    <!-- mais frases -->
</div>
```

**Regras:**
- `speakText(texto, botao)` — texto SEM acentos para compatibilidade com audioMap
- Progressivo: aula N inclui frases das aulas anteriores
- Formato: número + inglês + português + botão ouvir

---

### Checklist de Validação (antes de QUALQUER deploy)

- [ ] Zero `<div data-exercise="...">` no HTML (grep e confirmar 0 resultados)
- [ ] Todo matching usa `checkMatch(this)` + `verifyAllMatches(id)`
- [ ] Todo fill-in usa `checkBlank(this)` + `listenBlank(this)`
- [ ] Todo quiz usa `selectQuiz(this)` com `data-correct="true/false"`
- [ ] Todo ordering usa `selectOrderItem` + `checkOrder` + `moveItem`
- [ ] Toda pronúncia usa `speakPhrase` + `startRecording` + `stopRecording`
- [ ] Todo think-about-it usa `startFreeRecording` + `stopFreeRecording`
- [ ] IDs únicos por aula (match-l1, order-l1, think-result-l1)
- [ ] Opções de matching EMBARALHADAS
- [ ] Itens de ordering EMBARALHADOS (data-order ≠ posição no HTML)
- [ ] Hints em INGLÊS (nunca português)
- [ ] Acentos perfeitos no texto visível (Maísa, São Paulo, finanças)
- [ ] Texto sem acentos no data-phrase e speakText (Maisa, Sao Paulo)

---

## Referencias Tecnicas

- Framework: HTML estático + Vanilla JS (funções fallback em exercises.js)
- Estilos: design-system.css (Liquid Glass) + CSS inline para accent colors
- Audio: ElevenLabs API build-time (ver `docs/INTEGRACAO-ELEVENLABS.md`)
- Icones: Lucide SVG inline (nunca emojis) — apenas em JavaScript, NUNCA em atributos HTML
- Fonte: Montserrat/Inter (corpo) + Cormorant Garamond (títulos)
- Referência de implementação: `/public/professor/daniela-feitoza.html`
