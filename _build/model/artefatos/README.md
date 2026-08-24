# Artefatos normativos de INTERFACE

## `erica-professor-view.html`

**O que é.** O *Professor View* da Erica (*Business English for Restructuring & M&A*),
escrito pela Stephanie Vicente fora do sistema, em agosto/2026. Quatro aulas completas —
ESP, Listening, Grammar e Reading — com hub, syllabus, slides de IN CLASS e ficha de
evidências.

**Procedência.** É o HTML **real** da página, não o wrapper. O `.html` que o navegador salva
em `~/Downloads` é a moldura do claude.ai; o documento de verdade vem no diretório
`..._files/`, como `a_f6dO.html`. É esse arquivo que está aqui, byte a byte.

- SHA-256: `51d7bd416d75c2778c2f37977673b81b24b32c0dd15413d69d22298411baf00a`
- 377.418 bytes · 354 regras de CSS · 63 telas em 4 aulas
- Versionado no repo em **11/08/2026**

---

## `dante-kids-professor-view.html`

**O que é.** O *Professor View* do **Dante Blecker Gregory** (Kids · A2), escrito fora do
sistema em agosto/2026. Duas aulas completas — *Dragon Rider* e *My Lego City* — com
Planejamento, deck de IN CLASS e o percurso de POST-CLASS.

É a especificação do molde **`joaozinho`**, o modelo-aluno kids novo, na mesma relação que o
artefato da Erica tem com a `stephanie-vicente`:

| | adulto | kids |
|---|---|---|
| modelo atual | `helen-mendes` (anatomia `imersivo`) | `bento` (anatomia `imersivo`, pele kids) |
| modelo novo | `stephanie-vicente` (`guided-discovery`) | **`joaozinho`** (este artefato) |

**Procedência.** É o HTML **real** da página, não o wrapper — o `.html` que o navegador salva
em `~/Downloads` é a moldura do claude.ai, e o documento de verdade vem no diretório
`..._files/`, aqui como `a_002_dqUE.html`. Está no repo byte a byte.

- SHA-256: `dc20671678e3b7d121aa6dfd17eda88d78787b5e247746e0d19157f66c932460`
- 437.807 bytes · 1.076 regras de CSS · 20 telas em 2 aulas · 3 abas
- Versionado no repo em **13/08/2026**

### O que ele especifica que nenhuma anatomia de hoje tem

| | `imersivo` (o que o Dante tem no ar) | este artefato |
|---|---|---|
| abas | Planejamento · Pre-class · IN CLASS · Complementares | **Planejamento · In Class · Post-class** |
| deck | 29 telas em 7 capítulos | **10 telas em 6 stages** |
| espinha | The Cave · Dragon Words · Can It Fly? · Meet Storm · Dragon School · Your Turn · Wrap-Up | **Hello Time · Story Time · Say It Like This · Game Time · My Turn · Star Time** |
| eixo | 8 palavras de vocabulário | **1 chunk produtivo** (`He can fly, but he can't swim.`) + 6 ações que cabem nele |
| dever de casa | Complementares (mídia passiva) | **percurso auto-corrigido** (já portado — ver abaixo) |

Componentes próprios, medidos no deck (por aula): `flip-tile` 6 (vocab que vira),
`story-frame` 6 (a história em painéis), `star-card` 6 (recall do fecho), `unj-chip` 6
(montar a frase), `tscript-line` 13,5 (transcrição falante a falante), `gist-opt` 4,5,
`tf-b` 7,5, `conf-o` 9, `sc-obj` 10,5 (a cena clicável do jogo), `keyword-chip` 12.

### O emoji dele é slot de imagem, não decisão de arte

O deck tem 245 emojis e 2 imagens; o deck que está no ar tem 17 imagens da `assets/kids` e
2 emojis. Isso **não** é conflito com a direção "figura, não emoji": o próprio CSS do
artefato declara o que aquilo é —

```css
/* --- fallback de imagem --------------------------------------------------- */
.imgph { display:inline-flex; ... font-size:var(--ph-size,3.2rem); }
```

`.imgph` aparece 6 vezes por aula, sempre dentro de `.ft-img` (a frente do `flip-tile`) e de
`.st-art`. O emoji ali é **o placeholder de uma figura que não existia na página estática**.
Copiar o artefato e preencher esses slots pela biblioteca `public/assets/kids/` é obedecê-lo,
não divergir dele. Emoji fora de `.imgph` (o `😀 Great` do humor, o `🔊` do botão) é
tipografia da peça e copia-se como está.

### O POST-CLASS dele já está portado

`_build/dante-blecker-gregory-aula{1,2}/postclass.html` é **byte a byte** o `PV_POSTS` deste
artefato. O `.js` é o mesmo, com três correções documentadas no cabeçalho (o `imgFallback`
que não compilava em handler inline — REGRA 7.1; o espaço antes do ponto que quebrava a
chave do `audioMap`; o `restart()`) e mais a `AUDIO_PHRASES`, que o builder lê para gerar os
MP3. Ou seja: desta especificação, falta portar **o deck**.

---

## `marcos-private-black.html`

**O que é.** O material do **Marcos Mansour** (*Business English Program* · B1 · ciclo 2),
escrito fora do sistema em agosto/2026, já sob o pacote normativo novo — os documentos
**00–06**, a **Série P** (P1/P2/P3), os **Adendos 01 e 02** e o **Anexo P-A**
(`docs/private-black/`). Duas aulas completas do bloco 1 — 19 *Listening into Interaction*
e 20 *Reading into Speaking* —, cada uma com 10 telas e 8 etapas.

É a especificação da anatomia **`private-black`**, e **substitui o artefato da Erica** como
fonte de interface do molde adulto novo: o da Erica veio do doc set anterior e não conhece
`data-view`, aba Feedback, Post-class, Back to top, transcript, Stop no player nem a janela
do Teacher's Guide.

**Procedência.** É o HTML **real** da página, não o wrapper. O `.html` salvo em
`~/Downloads` é a moldura do claude.ai; o documento vem no diretório `..._files/`, como
`a_002_jqsA.html`. Está aqui byte a byte.

- SHA-256: `b3957620ccf8e2b051c1b2324b92abb79d8a5c8ace6f055a6947204e277d8d0f`
- 620.031 bytes · ~658 regras de CSS · 20 telas em 2 aulas · 6 abas · 187 funções JS
- 105 KB de CSS · 172 KB de JS (**32% em comentário**, que carrega a regra e o incidente)
- Versionado no repo em **24/08/2026**

### O que ele especifica que a anatomia de hoje não tem

| | `guided-discovery` (stephanie, hoje) | este artefato (`private-black`) |
|---|---|---|
| abas | Planejamento · Syllabus · Pre-class · In Class · Evidências | **Perfil/Planning · Planejamento · Pre-class · In-class · Feedback · Post-class** |
| visões | dois arquivos (professor / aluno) | `data-view` no mesmo arquivo — **e é aqui que divergimos de propósito, ver abaixo** |
| registro | paleta + header trocados pelo builder | **`ARTEFATO` · `ALUNO` · `CICLO` · `LESSONS` · `GUIDE`**, e a tela repintada por `data-lf` |
| etapas | `data-phase`, 7–8 fixas no gate | `stages[{n,min}]` **no registro**, quantidade livre, minutos fechando 55 |
| Teacher's Guide | só a nota local (`data-teacher`) | nota local **+ guia de 14 campos**, em janela própria (`?mode=teacher-guide&lesson=N`) |
| pre-class | as 5 etapas legadas do imersivo | **6 atividades reais**, cada uma com answer key próprio de 4 campos |
| post-class | não existe (Complementares saiu) | **5 componentes funcionais**, sem exercício e sem obrigatoriedade |
| player | play/pause + ±5s | **Play/Pause + Stop separado**, mesmo componente em todo áudio, com estado em texto |
| transcript | opt-in por config | **em todo áudio do in-class**, nascendo fechado (Adendo 01 §4) |
| ciclo | aulas 1..N | **`CICLO.primeira`** — o Marcos é ciclo 2, e as aulas se chamam 19 a 38 |

### Onde ele é protótipo, e por quê

O artefato roda no claude.ai: não tem servidor. Por isso o áudio é síntese do navegador,
**declarada uma vez** como provisória (P1 §0), e a persistência é `localStorage`. Isso não
é defeito nem conflito — é ausência, e a produção acrescenta as camadas por cima sem mudar
a forma: ElevenLabs pelo pipeline com manifesto (`transcript_hash`, `checksum`,
`qa_status`), Supabase no lugar do `localStorage`, e a janela do guia provada na URL real
(o sandbox do claude.ai não tem `allow-popups`, e isso é limitação do host, não da solução).

### A ÚNICA divergência deliberada: o arquivo do aluno

O P1 §1 pede **um** artefato com alternador *Visão professor · Visão aluno*, e é o que este
faz. Nós vamos emitir **dois arquivos**. Ordem do Dan, 24/08/2026:

> *"o aluno não ve o que não é dele"*

No arquivo único, o conteúdo do professor continua no DOM: um clique no alternador — sem
precisar de código-fonte — e o aluno lê os gabaritos das 6 atividades antes de fazê-las
(matando o diagnóstico que a aula existe para produzir) e as hipóteses escritas sobre as
dificuldades dele, que o doc 04 §7.1 proíbe que cheguem ao aluno. O P3 §3 já diz que
`display:none` não é separação — ela é de armazenamento e de árvore acessível. E o link do
aluno é público: arquivo estático na Vercel, com os códigos de acesso desligados.

Então o builder emite o espelho do aluno **sem** `data-teacher`, **sem** os painéis `ak`,
**sem** `var GUIDE` e **sem** o estado do ciclo. Removidos, não escondidos. O `data-view`
continua existindo — no arquivo do professor, como pré-visualização dele.

A divergência está **declarada** (P1 §21 manda declarar, nunca resolver em silêncio) e é
para ser levada à Stephanie, não decidida por nós de novo.

---

## A HIERARQUIA: o artefato manda, a documentação explica

Palavras do Dan, 11/08/2026:

> *"SE AS AULAS NÃO ESTÃO IDÊNTICAS AO ARTEFATO, NO QUESITO INTERFACE, ENTÃO ESTÁ ERRADO"*
>
> *"pq que eu colocaria esse artefato se não fosse pra vc imitar ele?"*
>
> *"o artefato é o state-of-art do que vamos fazer, a documentação é a especificação caso o
> artefato não seja suficiente pra vc entender o que estamos fazendo"*

1. **O ARTEFATO É O QUE VAMOS FAZER.** Interface, componentes, estrutura, comportamento,
   densidade. É dele que se **copia**, classe por classe: mesmos nomes, mesmo CSS, mesmo
   HTML. Não é referência inspiracional, não é ponto de partida para reinterpretação.
2. **A documentação** (`docs/NORMATIVO-planejamento-aulas-2026-08.md` e
   `docs/NORMATIVO-arquitetura-frameworks-2026-08.md`) entra **quando o artefato não basta
   para entender**: a função de cada etapa, a arquitetura do ciclo, o porquê. Ela **explica**
   o artefato — não o corrige.

> **A doutrina NÃO é veto ao artefato.** Se algo do artefato parecer contrariar uma regra, a
> primeira hipótese é que a regra foi lida errado, não que o artefato está errado. Divergência
> que você não consiga resolver copiando: **pergunte ao Dan**, não invente exceção.

### O que o material de produção acrescenta POR CIMA (isto não é conflito, é ausência)

O artefato é uma página estática do claude.ai. Ele não tem servidor — por isso não tem certas
camadas. Elas entram **sobre** a forma dele, sem alterá-la:

| camada | como entra | regra |
|---|---|---|
| **Áudio** | onde o artefato toca som, o material usa o MP3 do `audioMap` (ElevenLabs) — mesmo botão, mesmo lugar, mesmo comportamento visual | REGRA 7 |
| **Persistência** | `saveState`/`loadState`, activity-sync e os 3 scripts do rodapé entram sem mudar um pixel | REGRA 28 |
| **Texto no atributo** | `data-speak="..."` em vez de texto dentro da string JS do handler: é forma de escrever, invisível na interface | REGRA 7.1 |
| **Idioma** | zero PT na tela em A2+ é o idioma do CONTEÚDO; o artefato da Erica já é todo em inglês | REGRA 13 |
| **Paleta por aluno** | o artefato é a página de UMA aluna e fixa as cores; o shell é a mesma forma parametrizada | REGRA 10 |

**Sobre a paleta**, em detalhe, porque é a única que toca o CSS: o artefato define
`--mint: #7BEFB2`, o acento sobre fundo escuro. O shell define `--mint` com o literal do
`accent-light` do modelo, que o `base_swaps()` do builder já troca pelo do aluno. Resultado: o
CSS do artefato entra **verbatim** (com `var(--mint)`) e cada aluno mantém a paleta própria.
Nenhuma regra de CSS foi editada para isso.

**Exceção conhecida hoje, fora do CSS:** o *readout* de etapa na nav-bar diz
`Stage 3 / 8 · …` em inglês; no artefato era `Etapa 3 · …`. A nav-bar sobrevive no espelho do
aluno, e português ali é FAIL do validador (REGRA 13).

---

## Por que isto está no repo, e não em `~/Downloads`

Porque em 07/08/2026 decidiu-se o contrário — que *"o artefato não é mais consultado: a fonte
é o inventário"* — e o resultado foi a divergência que este arquivo agora existe para impedir:
o inventário catalogou a **reescrita** (as classes `ic-*`), e o GATE 20 passou a comparar a
cópia consigo mesma. Medido em 11/08/2026, por aula:

| peça do artefato | uso no artefato | no molde |
|---|---|---|
| `callout` (a mais usada) | 23,8 /aula | **0** |
| `tbl-wrap` | 10,2 /aula | **0** |
| `quiz-option` | 6,8 /aula | **0** |
| `rule-box` | 6,0 /aula | **0** |
| `blank-input` | 26,8 /aula | 3,5 (como `ic-blank`) |
| `reveal-item` | 7,5 /aula | 2,2 (como `ic-reveal`) |

Um arquivo fora do repo não entra no CI, não tem hash, e some quando alguém limpa a pasta de
downloads. Aqui ele é comparável por gate (`scripts/check_artefato_paridade.py`, GATE 21).

## Quem lê este arquivo

- `scripts/check_artefato_paridade.py` — o gate de paridade de interface (GATE 21)
- `_build/model/anatomias.json` — o inventário, que declara as classes **do artefato**
- quem for portar peça nova: a fonte do CSS e do HTML é **este arquivo**, não a memória
