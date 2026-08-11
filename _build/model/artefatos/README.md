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
