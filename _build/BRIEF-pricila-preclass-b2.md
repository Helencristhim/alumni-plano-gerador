# BRIEF — Pre-class B2 da Pricila Adamo (uma aula por subagente)

Você autora o **Pre-class B2** (self-study, accordion) de UMA aula da aluna `pricila-adamo`
(B2, Travel English, Araras/SP, dentista em transição p/ aposentadoria, gênero f).
O IN CLASS já existe e é B2. Você NÃO toca no hub (`public/professor/pricila-adamo.html`)
nem nos standalones. Você só ADICIONA: `_build/pricila-adamo-aula{N}/preclass.html` +
os mp3 `public/audio/pricila-adamo/pc{N}_*`.

## Fonte do conteúdo (consistência obrigatória)
- Aulas 2–7: leia o standalone `public/professor/pricila-adamo-aula{N}.html` — pegue
  TEMA, GRAMÁTICA B2 (capítulo "The Code"/Grammar Discovery) e VOCAB (capítulo
  "Packing Words"/"Key Words", reveal cards).
- Aula 1: NÃO tem standalone (é inline no hub `public/professor/pricila-adamo.html`,
  slides com `data-lesson="1"`). Tema = Travel English / The Dream + Packing Words;
  gramática = Present Simple vs Present Perfect (extraia os slides data-lesson="1").

## Formato (MOLDE) — use estes como espelho de FORMATO, não de conteúdo:
`_build/pricila-adamo-aula{11,12,13}/preclass.html` (origin/main). É um único
`<div class="lesson-card" id="ex-lesson-{N}">` com header + `.lesson-body` contendo as
seções. NÃO inclua `<script>`/audioMap/`<html>` — é fragmento; o audioMap é montado
depois pela passada do hub. Áudio funciona via `speakText('Frase exata')`.

## REGRA 4 — 5 etapas OBRIGATÓRIAS (todas presentes, nesta ordem):
- **Stage 1.1 Vocab Cards** com `<div class="vocab-card-pc">` + `speakText('Word')` (botão Ouvir). B2 = 12–15 palavras. Cada card: word, def PT, exemplo EN. Use o VOCAB da aula.
- **Stage 1.2 Matching** `match-grid#match-l{N}` com `<select onchange="checkMatch(this)">` — opções **EMBARALHADAS** (REGRA 24), ordem diferente das palavras.
- **Stage 1.3 Grammar in Context** — texto narrativo curto usando a gramática (palavras em `<strong>`) + 3 `quiz-item` com `selectQuiz`.
- **Stage 1.4 Grammar Tip** — bilíngue EN+PT (parágrafo PT+EN + tabela da estrutura, afirm/neg/interrog). B2 ~30% bilíngue.
- **Stage 1.5 Fill-in-the-blank** — `blank-input` com `data-answer`/`data-hint`/`data-phrase` + `checkBlank` + `listenBlank`.
- **Stage 2 Order** (opcional mas recomendado): `order-container#order-l{N}`. SE usar `speakText('[order-l{N}]')`, DECLARE no `extra_audio` do config (senão fica mudo).
- **Stage 3 Pronúncia** — `speech-card` com `data-phrase` + `speakPhrase`/`startRecording`/`stopRecording` (4 frases).
- **Stage 4 Quiz Situacional** — 3 `quiz-item` `selectQuiz` (contexto viagem/vida real B2).
- **Stage 5 Free Production** — `think-card` com `think-question` + `startFreeRecording`/`stopFreeRecording` + `<div id="think-result-{N}">`.
- **Survival Card** ao final (5 frases `sp-en`/`sp-pt` + `speakText`).

Copie classes/atributos/onclicks EXATAMENTE do molde 11/12/13 (só troca o conteúdo e o N).
Use badges REGRA 6. Zero emoji, ícones SVG inline como no molde. American English.
⚠️ REGRA 22: não apresente como NOVO um vocab que a aula vizinha já ensina; alinhe-se ao vocab do standalone daquela aula.

## Config
Crie `_build/pricila-adamo-aula{N}/config.json` copiando o de aula 11
(`git show origin/main:_build/pricila-adamo-aula11/config.json`), trocando:
- `lesson.n` = N, `lesson.menu_num`/`menu_title`/`menu_desc`/`subtitle`/`title_tag` (tema da aula N)
- `stamps` (id N)
- SE houver order com áudio: adicione em `lesson.extra_audio`:
  `[{"key":"[order-l{N}]","file":"pc{N}_order_story.mp3","voice":"ellen","text":"<texto concatenado da história na ordem correta>"}]`
Mantenha slug/gender/characters (pricila=ellen, guest=arthur)/palette/header iguais.
(Só preclass.html + mp3 entram no commit; o config fica no build dir, pode commitar junto — é aditivo e não toca hub.)

## Áudio (pc{N}_*, Arthur/Ellen alternados automaticamente)
```
set -a && source /home/dan/dev/work/better/alumni-plano-gerador/.env.local && set +a
python3 _build/gen_preclass_audio.py _build/pricila-adamo-aula{N}/config.json
```
Vozes atribuídas iguais ao builder: 1–2 palavras=arthur; frases alternam ellen/arthur;
`data-voice` vence; "I'm Pricila"=ellen. Pula existentes. Gere até **0 missing**.

## Validação (gates bloqueantes)
```
python3 _build/validate_preclass.py _build/pricila-adamo-aula{N}/config.json   # 5 etapas + 0 audio missing
python3 -c "import esprima"  # se faltar: pip install esprima  (preclass é fragmento sem JS — pule se não houver <script>)
```
Contraste: o fragmento usa só classes/vars do design-system (como o molde) → 0 ilegíveis por construção; não invente cores inline de texto fora do molde.

## GOTCHAS
- Worktree: `git worktree add -b feat/pricila-preclass-b2-a{N} ../wt-pripc{N} origin/main`
  então **`git -C ../wt-pripc{N} sparse-checkout disable`** (senão os mp3/standalones somem do checkout).
- Trabalhe DENTRO do worktree `../wt-pripc{N}` (caminhos absolutos; cwd reseta entre Bash calls).
- mp3 são binários e há `.gitignore` — confirme que `git add public/audio/pricila-adamo/pc{N}_*.mp3` realmente adiciona (use `git add -f` se ignorado). `sparse-checkout disable` é o que faz entrarem.

## Commit (REGRA 19 — branch+PR+squash)
Adicione APENAS: `_build/pricila-adamo-aula{N}/preclass.html`, `_build/pricila-adamo-aula{N}/config.json`,
`_build/pricila-adamo-aula{N}/preclass_audio_manifest.json`, e `public/audio/pricila-adamo/pc{N}_*.mp3`.
NÃO toque hub nem standalones (confirme `git status` não lista pricila-adamo.html nem -aula{N}.html).
```
git push -u origin feat/pricila-preclass-b2-a{N}
gh pr create --title "Pricila Adamo — Pre-class B2 aula {N}" --body "..."
gh pr merge --squash --delete-branch
```
Confirme MERGED. Reporte: preclass criado? quantos pc{N}_ áudios? gates (5 etapas ok / 0 missing / contraste ok)? PR #. Bloqueios.
Co-author no commit: `Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>`
```
