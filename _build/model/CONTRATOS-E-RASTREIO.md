# Contratos Universais & Rastreio Modelo↔Aula

> **O que é.** O gerador tem >1 modelo (Adulto, Kids em construção, Teens depois). Todos
> nascem do mesmo lugar e têm de honrar um mesmo conjunto de garantias, cada uma travada
> por um gate. Este documento é a **fonte única da verdade** desses contratos + de como
> uma correção viaja entre aula e modelo. Ver também o Catálogo (`public/catalogo.html`).

---

## 1. Contratos Universais

O que **TODO modelo** (Adulto/Kids/Teens/…) é obrigado a honrar, em **toda aula**, nos
**dois papéis** (professor + aluno). O *visual* muda por modelo; a **classe-mecanismo que o
gate enxerga é invariante**. Regra de ouro: **shell novo REUSA a classe-mecanismo, ou
generaliza o gate ANTES** — nunca se pula o gate.

| # | Contrato | Classe/estrutura invariante | Gate | No `main`? |
|---|---|---|---|---|
| 1 | **Slide de conclusão acende o card** | `.check-grid[data-lesson]` + `.check-item onclick="toggleCheck"` + checkmark reage a `.checked` | `check_wrapup_checklist` + `check_persistence_wiring` (STUDENT_SLUG/lesson-progress.js) | ✅ |
| 2 | **Rolagem do slide** (página nunca trava) | `.slide > .slide-inner { …; overflow-y:auto }` — inclusive espelho aluno | `validate_lesson` (regressão fix #1074) | ✅ |
| 3 | **Tarefa ANTES / checagem DEPOIS** | slide `data-task-for` antes de diálogo/leitura | `check_task_before_exposure` | ✅ |
| 4 | **Perguntas visíveis ANTES do play** | `.comp-questions` nunca nasce `display:none` | `validate_lesson` ("PERGUNTA ESCONDIDA") | ✅ |
| 5 | **Áudio 100% ElevenLabs** | todo `speakText`/`data-phrase` tem MP3 no `audioMap` | `validate_lesson` (audioMap) + `check_audio_quality` | ✅ |
| 6 | **Botões compilam** (handler não morre) | handler inline compila no V8; texto no `data-*`, nunca na string JS (REGRA 7.1) | `check_inline_js.mjs` (GATE 7) + `check_handlers_exist` | ✅ |
| 7 | **Voz por personagem** | `data-voice` em toda `dialogue-line`; 1 voz/personagem | `validate_lesson` + cross-check do manifest | ✅ |
| 8 | **Contraste legível** | nenhum texto ilegível (claro E escuro) | `check_contrast.py` (GATE 2) | ✅ |
| 9 | **Complementares: link DIRETO** | cada `media-card` tem `<a href>` ao recurso exato, sem busca/placeholder (REGRA 17) | `validate_lesson` (anti-busca) | ✅ |
| 10 | **Complementares: sem conteúdo PAGO** | sem businessenglishpod/eslpod/englishclass101/hbr | `check_forbidden_patterns` (padrão pago) | ✅ *(fechado 22/07)* |
| 11 | **Idioma por nível** (a maior variação) | A0/A1 bilíngue; **A2+ zero PT** na tela | `validate_lesson` (pt_na_tela por nível) | ✅ |
| 12 | **Hub inteiro, não só IN CLASS** | Planejamento+Pre-class+IN CLASS+Complementares; prof E aluno | `validate_lesson` + `audit_hubs_struct` rodam nos 2 arquivos | ✅ |

> **Como um modelo novo entra:** o shell dele começa dos ossos estruturais do Adulto
> (mesmas classes-mecanismo acima), muda só a pele (CSS/ilustração/tom). Assim os 12 gates
> valem de graça. Se um contrato precisar de estrutura diferente, **primeiro** se generaliza
> o gate (pra reconhecer as duas formas), **depois** se muda o shell. Nunca o inverso.

---

## 2. Rastreio bidirecional (aula ↔ modelo)

O modelo é a **fonte única da verdade**. Uma correção viaja nos dois sentidos — com escopo
e controle, pra respeitar a REGRA 30 ("aula já dada não se mexe sem ordem").

### ↑ Sobe: conserto num aluno → vira modelo + gate
Achou um defeito consertável numa aula de aluno? O conserto **não pára no aluno**:
1. corrige-se o **shell do modelo** (pra a próxima aula já nascer certa);
2. cria-se/estende-se um **gate** que trava a regressão (senão volta — foi o Walyson);
3. confirma-se o gate **no CI e no main** (senão é lacuna — foi o gate de links pagos, que
   ficou 1 mês numa branch sem mergear).

"*Conserto só fica se estiver no molde + gate + CI.*" Sem os três, é sorte, não garantia.

### ↓ Desce: conserto no modelo → reflete SÓ nas aulas daquele modelo
| | Aulas **futuras** | Aulas **existentes** |
|---|---|---|
| Modelo → aulas | **automático** (o builder já emite certo) | **retrofit ESCOPADO**: só as aulas daquele modelo, sob comando explícito, verificado por gate — **nunca** varredura gulosa no repo (quase reescreveu 2.182 arquivos errados uma vez) |

O "**APENAS as aulas que herdaram o modelo**" exige saber a proveniência de cada aula — ver §3.
Um conserto no Modelo Kids **nunca** pode tocar uma aula do Adulto (estrutura diferente).

---

## 3. Etiqueta de proveniência (o que torna o §2 possível)

Toda aula gerada nasce declarando de qual **modelo** e **nível** herdou — no `<head>` de
professor E aluno:

```html
<meta name="alumni-model" content="adulto">
<meta name="alumni-level" content="A2">
```

- **Quem emite:** o builder, em `base_swaps()` (`build_from_model.py`) — passa por TODA aula
  (standalone + hub, prof + aluno). O autor do conteúdo não escreve nada; é impossível
  esquecer. `model` vem de `config.json` (`"model"`, default `"adulto"`); `level` vem de
  `"level"` ou do 1º item do `header` (o CEFR). Idempotente.
- **Pra que serve:**
  - **retrofit escopado** — "aplicar em todas as aulas do Modelo Kids" filtra por `alumni-model=kids` e não vaza pro Adulto;
  - **catálogo** — sabe quais aulas pertencem a cada modelo/nível;
  - **auditoria** — o rastreio §2 fica verificável (quem herdou o quê).

> Aulas legadas (geradas antes desta etiqueta) não têm o `<meta>`. Isso é esperado: elas
> ficam como estão (REGRA 30). Um retrofit escopado que as toque, por ordem explícita,
> aproveita pra carimbar a etiqueta.
