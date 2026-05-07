# CHECKLIST FINAL OBRIGATÓRIO — VALIDAÇÃO PRÉ-DEPLOY

> **REGRA ABSOLUTA:** Nenhum material pode ser entregue como "pronto" sem passar por TODOS
> os checks abaixo. Se QUALQUER check falhar, o material é REJEITADO e deve ser corrigido
> antes de novo deploy. Sem exceção.

---

## CHECK 1 — PORTUGUÊS E ACENTUAÇÃO

**O que verificar:**
- Todos os textos em português têm acentuação perfeita (ã, ç, é, í, ó, ú, â, ê, ô)
- Nenhuma palavra em português sem acento quando deveria ter
- Microcopy, traduções, hints, survival cards, explicações gramaticais

**Como verificar (automatizado):**
```bash
# Buscar palavras comuns que frequentemente perdem acento
grep -i "traducao\|comunicacao\|producao\|apresentacao\|informacao\|pronuncia\|exercicio\|pratica\|financas\|portugues\|ingles\|numero\|pagina\|tambem\|voce\|esta\|ate\|ai\|la\|ja\|nao\|sao" public/professor/{id}.html public/aluno/{id}.html
```

**Palavras que SEMPRE precisam de acento:**
tradução, comunicação, produção, apresentação, informação, pronúncia, exercício, prática, finanças, português, inglês, número, página, também, você, está, até, aí, lá, já, não, São

**Critério:** ZERO palavras em português sem acento correto.

---

## CHECK 2 — INGLÊS (ESCRITA E APLICAÇÕES)

**O que verificar:**
- Todo texto em inglês é gramaticalmente perfeito
- American English consistente (color, not colour; organize, not organise)
- Datas em formato americano (March 15th, not 15th March)
- Frases de exemplo fazem sentido no contexto profissional do aluno
- Instruções de exercícios em inglês são claras e corretas
- Sem mistura de British/American English

**Como verificar:**
```bash
# Buscar erros comuns de British English
grep -i "colour\|organise\|favourite\|centre\|realise\|recognise\|behaviour\|programme\b" public/professor/{id}.html public/aluno/{id}.html
```

**Critério:** ZERO erros gramaticais em inglês. American English 100%.

---

## CHECK 3 — NÍVEL x AULA (ADEQUAÇÃO CEFR)

**O que verificar:**
- Vocabulário compatível com o nível CEFR do aluno
- Estruturas gramaticais dentro do escopo do nível
- Tamanho das frases adequado ao nível
- Complexidade dos exercícios condizente
- Referência: `/docs/CEFR-ALUMNI.md`

**Critérios por nível:**

| Nível | Vocab/aula | Tamanho frase | Gramática permitida |
|-------|-----------|---------------|---------------------|
| A0 | 4-5 palavras | 2-4 palavras | Verb to be (aff only) |
| A1 | 5-7 palavras | 4-6 palavras | Present simple, to be, can |
| A2 | 6-8 palavras | 5-8 palavras | Past simple, present continuous |
| B1 | 7-9 palavras | 8-12 palavras | Present perfect, conditionals |
| B2 | 10-12 palavras | Parágrafos | All tenses, passive, reported |

**Verificação:** Comparar conteúdo proposto com tabela CEFR. Se exercícios estão abaixo do nível = material subutiliza o aluno. Se acima = material frustra.

---

## CHECK 4 — ÁUDIOS ELEVENLABS (OBRIGATÓRIO)

**REGRA:** Todo botão "Ouvir", todo `speakText()`, todo `speakPhrase()`, todo `data-phrase` DEVE ter um arquivo MP3 gerado pelo ElevenLabs. Web Speech API é APENAS fallback — NUNCA método principal.

**Como verificar (automatizado):**
```bash
node -e "
const fs = require('fs');
const path = require('path');
const file = 'public/professor/{id}.html';  // ou aluno
const html = fs.readFileSync(file, 'utf8');

// 1. Verificar audioMap entries com arquivos
const match = html.match(/var audioMap = ({[\s\S]*?});/);
const map = match ? JSON.parse(match[1]) : {};
let mapMissing = 0;
Object.entries(map).forEach(([text, relPath]) => {
  if (!fs.existsSync(path.join('public', relPath))) mapMissing++;
});

// 2. Verificar speakText calls sem audioMap
const speaks = [...html.matchAll(/speakText\('([^']+)'/g)];
const phrases = [...html.matchAll(/data-phrase=\"([^\"]+)\"/g)];
let unmapped = 0;
speaks.forEach(m => { if (!map[m[1]]) unmapped++; });
phrases.forEach(m => { if (!map[m[1]]) unmapped++; });

console.log('AudioMap entries sem MP3:', mapMissing);
console.log('speakText/data-phrase sem audioMap:', unmapped);
if (mapMissing > 0 || unmapped > 0) {
  console.log('FALHOU — gerar áudios antes do deploy');
  process.exit(1);
}
console.log('PASSOU — todos os áudios cobertos');
"
```

**Critério:** ZERO frases sem MP3 ElevenLabs. Se o check falhar, rodar o script de geração de áudio antes do deploy.

**Fluxo obrigatório:**
1. Gerar HTML com audioMap
2. Extrair TODAS as frases usadas em speakText/data-phrase
3. Gerar MP3 para cada frase via ElevenLabs API
4. Atualizar audioMap no HTML com os paths corretos
5. Verificar que TODOS os MP3 existem
6. SÓ ENTÃO fazer deploy

---

## CHECK 5 — FUNCIONALIDADE DOS EXERCÍCIOS

**O que verificar:**
- Matching: selecionar opção → feedback verde/vermelho imediato
- Fill-in-the-blank: digitar resposta + clicar Check → validação funciona
- Multiple choice: clicar opção → marca correto/errado
- Ordering: setas funcionam, Check Order valida
- Pronunciation: botão Ouvir toca áudio, Gravar ativa microfone
- Think About It: Gravar funciona, Parar salva, Ouvir reproduz
- Survival Card: botões de áudio tocam

**Como verificar (automatizado — check de integridade):**
```bash
node -e "
const fs = require('fs');
const file = 'public/professor/{id}.html';
const html = fs.readFileSync(file, 'utf8');

// Verificar que NÃO tem data-exercise (padrão quebrado)
const dataEx = (html.match(/data-exercise=/g) || []).length;
if (dataEx > 0) { console.log('FALHOU: ' + dataEx + ' data-exercise encontrados (usar HTML manual)'); process.exit(1); }

// Verificar funções essenciais presentes
const funcs = ['checkBlank','selectQuiz','checkMatch','verifyAllMatches','checkOrder','startRecording','speakPhrase','startFreeRecording'];
funcs.forEach(f => {
  const count = (html.match(new RegExp(f, 'g')) || []).length;
  if (count === 0) console.log('AVISO: ' + f + ' não encontrado no HTML');
});

// Verificar que exercícios existem
const matching = (html.match(/match-grid/g) || []).length;
const fillin = (html.match(/checkBlank/g) || []).length;
const quiz = (html.match(/selectQuiz/g) || []).length;
const order = (html.match(/order-container/g) || []).length;
const speech = (html.match(/speech-card/g) || []).length;

console.log('Matching grids:', matching);
console.log('Fill-in checks:', fillin);
console.log('Quiz options:', quiz);
console.log('Order containers:', order);
console.log('Speech cards:', speech);
console.log(dataEx === 0 ? 'PASSOU — HTML manual correto' : 'FALHOU');
"
```

**Critério:** ZERO `data-exercise` no HTML. Todas as funções fallback presentes. Todos os tipos de exercício existem.

---

## SCRIPT DE VALIDAÇÃO COMPLETA

Rodar ANTES de qualquer deploy:

```bash
node scripts/validate-material.js --professor public/professor/{id}.html --aluno public/aluno/{id}.html
```

Este script executa os 5 checks automaticamente e retorna PASS/FAIL para cada um.

---

## RESUMO

| Check | O que | Critério | Bloqueante |
|-------|-------|----------|------------|
| 1. Português | Acentuação perfeita | Zero erros | SIM |
| 2. Inglês | Gramática + American English | Zero erros | SIM |
| 3. Nível | Conteúdo adequado ao CEFR | Dentro do nível | SIM |
| 4. Áudios | Todos via ElevenLabs | Zero frases sem MP3 | SIM |
| 5. Funcionalidade | Exercícios funcionam | Zero quebrados | SIM |

**Todos os 5 checks são BLOQUEANTES. Material com qualquer falha NÃO é "pronto".**
