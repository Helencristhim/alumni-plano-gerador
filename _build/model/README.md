# Pipeline do MODELO (aluna modelo Helen Mendes)

> **REGRA 20**: toda aula nova nasce daqui. Layout/CSS/JS vêm SEMPRE do shell da
> aluna modelo (`public/professor/helen-mendes-aula1.html` e hubs `helen-mendes.html`);
> o conteúdo vem do perfil 360 do aluno. NUNCA gerar CSS/JS do zero e NUNCA
> corrigir bug de layout num aluno individual — bug de layout se corrige NO MODELO
> e a correção chega aos próximos via builder. **Aulas passadas não são tocadas**
> (retrofit é fase 2, sob demanda, com OK da Helen).

## Fluxo por aula

```
1. Autorar conteúdo (do perfil 360):   _build/{slug}-aula{N}/slides.html (+preclass.html...)
2. Configurar:                          _build/{slug}-aula{N}/config.json (schema no build_from_model.py)
3. Buildar:                             python3 _build/model/build_from_model.py _build/{slug}-aula{N}/config.json
4. Gerar áudio:                         ELEVENLABS_API_KEY=... python3 _build/model/gen_audio.py _build/{slug}-aula{N}/config.json
4b. QUALIDADE DE ÁUDIO (GATE, bloqueante): python3 _build/model/check_audio_quality.py _build/{slug}-aula{N}/config.json
    Valida que CADA mp3 do manifest é um MP3 real (frames MPEG + duração ≥ 0.30s +
    tamanho ≥ 1.2KB). Pega áudio PODRE que gen_audio gravou de um corpo de erro/
    rate-limit/truncado da ElevenLabs (o gate de integridade do deploy só checa se o
    arquivo EXISTE, não se presta — incidente Fabiana). Se acusar podre: re-gere só
    esses com GEN_AUDIO_FORCE=1 e revalide até 0 podre.
5. Validar (GATE, bloqueante):          python3 _build/model/validate_lesson.py public/professor/{slug}-aula{N}.html public/aluno/{slug}-aula{N}.html
5b. PADROES IN CLASS (GATE):             python3 _build/model/check_inclass_patterns.py public/professor/{slug}-aula{N}.html
    Anti-regressao dos 2 bugs sistemicos: (1) Comprehension com .comp-question SEM a
    regra CSS de reveal (clicar nao revela — use .comp-q/.q-answer do modelo); (2)
    slide Common Mistake com .mistake-item cru (background inline) em vez de
    .mistake-wrong/.mistake-right. Sai != 0 se a aula nova reproduzir qualquer um.
6. Contraste computado (GATE):          python3 check_computed_contrast.py (headless; 0 ilegível obrigatório)
7. Hub: inserir _build/{slug}-aula{N}/hub_snippets.html no hub existente (modo "snippets")
   ou usar hub "new" no config (aluno novo, sem hub)
7b. ESTRUTURA DO HUB (GATE OBRIGATÓRIO após insert_hub):
                                        python3 _build/model/audit_hubs_struct.py --check public/professor/{slug}.html public/aluno/{slug}.html
    Pega vazamento de aba (ORPHAN/ESCAPE: Pre-class/Complementares renderizando fora
    da aba certa quando insert_hub fecha </div> de tab cedo demais), SLIDES_COMP,
    DIV_IMBAL, MENU_MIX, OLD_SHELL. Sai != 0 (bloqueia) se o hub tocado tiver defeito.
    Fix = mover o </div> de fechamento da aba de ANTES do 1º bloco-órfão para DEPOIS
    do último bloco da aba, até auditor limpo (0 ESCAPE/ORPHAN) e balanço de divs = 0.
8. PR → merge → deploy automático via GitHub (NUNCA vercel --prod)
```

## CI (trava física — roda sozinho em TODO PR que toca aula)

`.github/workflows/validate-lessons.yml`: arquivo de aula NOVO passa por
`validate_lesson.py` (estrutura + vozes por personagem + wiring de persistência
REGRA 28: sem activity-sync.js/supabase/STUDENT_SLUG a gravação do aluno some ao
atualizar a página) + `check_contrast.py`
(contraste computado, slides claros E escuros; gradiente/foto são pulados — o
contrast-guard cobre em runtime). Arquivo MODIFICADO passa por
`check_no_regression.py` (ex-lesson/stamp/slide não pode sumir; arquivo não pode
encolher >10% — classe do incidente 6cd5b3b9). HUBs tocados (novos E modificados)
passam por `audit_hubs_struct.py --check` (GATE 4 — vazamento de aba ORPHAN/ESCAPE/
SLIDES_COMP/DIV_IMBAL/MENU_MIX + shell pré-modelo OLD_SHELL; bloqueia o PR se algum
hub modificado renderizar Pre-class/Complementares fora da aba certa — classe do
incidente Tânia/tuca-dias). Ninguém precisa lembrar de rodar
gate local: o PR não mergeia vermelho.

## Áudio de listening = MONÓLOGO

Listening é 1 MP3 com 1 voz. Por isso o texto de listening DEVE ser monólogo
(aviso, recado, narração). Conversa de 2+ pessoas vai SEMPRE pro diálogo
line-by-line com `data-voice` por fala (o validador trava voz repetida).
NUNCA escrever um diálogo dentro de um listening.

## O que o shell do modelo garante de graça

EXIT→exitSlideMode() · handler de Escape fora de `<script src>` · listening = MP3 único
com player completo (mpToggle/mpSeek/mpSkip/mpSpeed) · revealError dinâmico · prefixo de
áudio a{N}_/pc_ · contrast-guard.js · nav-bar flex dentro do slides-wrapper (fix e615c853)
· 3ª cor de diálogo `.guest` · bloco de contraste slide-dark dos diálogos.

## Vozes (voices.json)

Só **arthur** e **ellen** existem na conta ElevenLabs (REGRA 35 — Ash/Kristen NÃO existem).
Regras bloqueantes do validador:
- toda `dialogue-line` tem `data-voice`
- 1 voz consistente por personagem no arquivo inteiro
- personagens distintos no MESMO diálogo = vozes distintas
- diálogo com mais falantes que vozes disponíveis = ERRO (reescrever ou adicionar voz)
- cross-check: o MP3 de cada fala (audio_manifest.json) foi gerado com a voz do `data-voice`

## Exercício novo (nível/idade/tipo de aula diferente)

Um tipo de exercício que ainda não existe entra PRIMEIRO no modelo (HTML+JS+regra no
validador), valida, e só então é usado em aluna(o) real. O validador pega estrutura
quebrada: handler `onclick` sem função correspondente, `<div>` desbalanceado, wildcard
de contraste, `data-exercise`, áudio sem MP3.

## Blocos B2 do IN CLASS (aditivo)

Blocos de exercício prontos pra aulas B2 (leitura/gist/true-false/advice modais...),
portados de `artefato-b2-exercicios.html`. CSS+JS já vivem no shell do modelo
(classes `.ic-*`; handlers `icPickGist`/`icRevealTf`/`icToggleAnswer`). O builder
emite o HTML a partir do config — tipos antigos seguem idênticos.

**Como usar:** no `slides.html`, ponha um placeholder onde os blocos entram:
```html
<div class="slide slide-light" data-slide="5" data-phase="3" data-teacher="...">
  <div class="slide-inner">
    <h2 class="slide-heading">Read for the <span class="accent">main idea</span></h2>
    <!--IC-BLOCKS:reading-->
  </div>
</div>
```
e declare os blocos no config em `lesson.inclass_blocks` (chave = nome do placeholder):
```json
"inclass_blocks": {
  "reading": [
    {"kind":"reading","rtitle":"...","paras":["..."],"source":"...","link":"..."},
    {"kind":"gist","prompt":"Best title?","choices":[["a","...",false],["b","...",true]]},
    {"kind":"tf","items":[["statement","t","justification"], ...]}
  ]
}
```
Schema completo de cada `kind` (gist, tf, answer, reading, matching, gapfill, modals,
rephrase, scenarios, questions/guiding/analyse, lf, vocabnote/followup/bank) está no
cabeçalho de `build_from_model.py` (função `render_block`). Interativos: **gist**
(clicar a ideia certa), **tf** (revelar verdict+justificativa) e **answer** (accordion
"Reveal answer key") — todos toggle (REGRA 27.E) e teacher-led (NÃO entram na barra de
progresso do Pre-class; updateProgress intocado). Aula sem placeholder = build
byte-a-byte idêntico ao de antes (no-op).
