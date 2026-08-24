# A fronteira do `private-black`

> **O molde é o `stephanie-vicente`.** O artefato do Marcos Mansour é a **especificação de
> interface** que se leva para dentro dele — não é o destino do trabalho, é de onde a forma
> vem. Quem reproduz para qualquer aluno é o molde. A mesma relação que já existe no
> sistema: molde `helen-mendes` ↔ anatomia `imersivo`; molde `stephanie-vicente` ↔ anatomia
> `private-black`, portada do artefato do Marcos.
>
> Correção do Dan, 24/08/2026:
>
> > *"o artefato do Marcos Mansur precisa ser levado pro molde stephanie pra só então o
> > molde ser capaz de reproduzir com qualquer aluno"*

> **O que este arquivo é.** A declaração do que o molde `stephanie-vicente`, na anatomia
> nova, herda do sistema atual e do que ele não herda. Ele existe porque a pergunta do Dan
> (24/08/2026) foi exatamente essa:
>
> > *"não quero o novo molde carregando erros e defeitos e problemas do molde helen-mendes,
> > apenas carregando as coisas acertadas (porém no padrão novo)"*

## Por onde o defeito viaja de verdade

Não é por morar no mesmo repositório. É por **cópia** e por **gate mal escopado**. Os três
casos são medidos, e todos os três são de autoria — aconteceriam igual num repo separado:

1. o molde `guided-discovery` nasceu **clonando** o shell da helen. Por isso existe o
   GATE 18 (`check_shell_drift.py`), que *força* os dois shells a não divergirem nas funções
   JS — proteção legítima entre clones, e cano de contaminação para quem não é clone;
2. o `anatomias.json` catalogou a **reescrita** (`ic-reveal`, `ic-blank`…) em vez das classes
   do artefato, e o GATE 20 passou a comparar a cópia consigo mesma: verde para sempre,
   medindo coerência interna e chamando isso de fidelidade;
3. o critério *"a classe existe no shell?"* respondeu SIM para tudo, porque o shell é clone e
   carrega até o CSS das peças que a anatomia não usa.

Por isso a fronteira aqui é de **código e de escopo**, não de repositório. Repo separado
duplicaria Supabase, senhas, dashboard, CI e pipeline de áudio — que divergiriam a partir do
primeiro dia, na camada onde divergir dói mais.

## O carimbo

Toda aula desta anatomia nasce com, no `<head>`:

```html
<meta name="alumni-anatomia" content="private-black">
```

É por ele que gate se escopa — nunca pelo caminho do arquivo, nunca por um sintoma que o
legado compartilha. O `scripts/gates.json` aceita escopo por `marcador`, e é essa a forma:

```json
"escopo": {"marcador": "alumni-anatomia=private-black"}
```

## O que o novo NÃO herda

| | Por quê |
|---|---|
| o shell (CSS/JS) da helen | o shell do `private-black` é **extraído do artefato do Marcos**, por remoção do conteúdo dele. Zero linha vinda do imersivo |
| GATE 18 (shell drift) | ele existe para CLONE. O `private-black` não é clone de ninguém — como a `story-quest` também não é, e por isso também está fora |
| o builder do imersivo | builder próprio (`scripts/black/`), não um `if model==` dentro do `build_from_model.py` |
| as regras de anatomia do `CLAUDE.md` | as 5 etapas do pre-class (REGRA 4), o piso de 25 slides, o survival card, os Complementares, o matching PT: **nada disso atravessa**. A anatomia é a dos documentos 00–06 |
| a contagem de etapas | o 00 §5 diz que não existe quantidade universal de oito; o P3 §2.1 manda a suíte **reprovar** número de etapas escrito no código. O N sai do registro da aula |

## O que o novo HERDA — e seria burrice reaprender

A doutrina que **atravessa** é a de integridade: ela não descreve a forma de um molde, descreve
o que quebra em qualquer navegador. Cada uma custou um incidente:

| Gate | O que ele impede |
|---|---|
| 7 · `check_inline_js.mjs` | handler que não compila no V8 — 324 botões mortos em 48 arquivos, vivos por 23 dias |
| 2 · contraste computado | texto ilegível medido sobre a superfície composta, não sobre o fundo nominal |
| 28 · `check_reveal_clica.py` | reveal que não revela — 130 slides com o botão trocando de texto e a regra nunca aparecendo |
| 31 · `check_reset_completo.py` | Reset que não zera tudo o que conta progresso |
| 29 · `check_recording_paths.py` | gravação do aluno sobrescrita pela do professor |
| 30 · `check_score_align.mjs` | score marcando errado quem falou certo |
| 8 · `check_legacy_baseline.py` | arquivo novo nasce com baseline vazio: tolerância zero, de graça |

E a infraestrutura inteira: Supabase, dashboard, senhas, `merge_aula.py`, CI, pipeline
ElevenLabs com a credencial fora do repo.

## Onde cada coisa mora

| | Caminho |
|---|---|
| documentos normativos | `docs/private-black/` |
| especificação de interface | `_build/model/artefatos/marcos-private-black.html` |
| shell | `_build/model/shells/black.html` *(Fase 1)* |
| builder e gates próprios | `scripts/black/` |
| config das aulas | `_build/black/{slug}/` *(Fase 3)* |
| o molde | `public/professor/stephanie-vicente*.html` — a aluna-modelo, re-emitida na anatomia nova na Fase 4 |
| material publicado | `public/professor/{slug}.html` · `public/aluno/{slug}.html` — **a convenção não muda**, porque mudá-la quebraria dashboard, senhas e links por zero ganho. O escopo se lê no carimbo |

## O que o aluno recebe

**Dois arquivos.** Ordem do Dan, 24/08/2026: *"o aluno não ve o que não é dele"*. O espelho do
aluno sai **sem** `data-teacher`, **sem** os painéis `ak`, **sem** `var GUIDE` e **sem** o
estado do ciclo — removidos, não escondidos por CSS.

Isto **diverge** do P1 §1, que pede um artefato único com alternador de visão, e a divergência
está declarada (P1 §21) em `_build/model/artefatos/README.md`. Motivo: o link do aluno é
público — arquivo estático, códigos de acesso desligados — e no arquivo único basta clicar no
alternador para ler os gabaritos antes de fazer o pre-class e as hipóteses escritas sobre as
próprias dificuldades.

## As fases

| | Entrega | Prova |
|---|---|---|
| **0** *(esta)* | documentos no repo · artefato congelado · fronteira declarada · GATE 18 fora | GATE 17 aceita a anatomia; nenhum gate do imersivo casa com o carimbo |
| 1 | `shells/black.html`, extraído do artefato | boot no Chromium: console limpo e componentes construídos (P3 §1.1) |
| 2 | `anatomias.json` com as classes **do artefato do Marcos**; GATE 20/21 reapontados | uma classe `ic-*` nova reprova |
| 3 | `scripts/black/build_black.py` + schema do config | asserts de build: minutos fecham, 6 atividades, 14 campos do guia |
| 4 | **o molde `stephanie-vicente` re-emitido na anatomia nova** — é aqui que o artefato chega ao molde | a estrutura gerada bate com a do artefato |
| 5 | a suíte P3 (navegador + mutação + canário) | cada gate reprova a própria mutação |
| 6 | produção: ElevenLabs, Supabase, guia na URL real | só quando for testar em aluno |

## Duas perguntas abertas para a Stephanie

1. **Oito etapas, ou sem número?** O 03 §5 descreve os quatro frameworks com oito etapas; o
   00 §5 diz que não existe quantidade universal. Pela precedência do 00, o gate **não** cobra
   número — cobra que as etapas do registro sejam as da tela, na ordem, e que os minutos
   fechem os 55. Precisa de confirmação antes da Fase 5.
2. **O arquivo do aluno**, acima — a divergência declarada em relação ao P1 §1.
