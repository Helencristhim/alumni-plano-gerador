# Syllabus — Bloco 1 (aulas 1–5) — `mock-rodizio-tiago`

> Currículo do experimento de **rodízio de frameworks**. Perfil da persona em
> `PERFIL-360.md`. O rodízio está declarado em `public/data/frameworks.json` (`rodizios[]`) e
> é conferido aula a aula pelo **GATE 11**.

## 1. O ciclo

```
aula 1 → PPP            aula 4 → PPP
aula 2 → Communicative  aula 5 → Communicative
aula 3 → Task-Based     (aula 6 voltaria a Task-Based)
```

Framework da aula N = `ciclo[(N - 1) % 3]`. É posição, não escolha caso a caso — foi a
decisão do Dan em 30/07/2026, e é o que permite escalar para 20/48 aulas sem alguém ter de
decidir método a método.

## 2. As 5 aulas

| # | Framework | Título | Skill receptiva principal | O que o aluno sai sabendo fazer |
|---|---|---|---|---|
| 1 | PPP | **The Update Nobody Read** | Reading | Dar um status update falado, na ordem certa |
| 2 | Communicative | **What They Actually Need** | Listening | Extrair o pedido real de quem não o formula bem |
| 3 | Task-Based | **Two Suppliers, One Slot** | Reading (2 cotações) | Recomendar entre duas opções e sustentar a escolha |
| 4 | PPP | **Before It Becomes a Problem** | Listening | Sinalizar risco cedo e pedir decisão com prazo |
| 5 | Communicative | **The Meeting That Ends On Time** | Listening | Conduzir uma reunião curta e fechar quem-faz-o-quê |

**Skill receptiva alterna** (R · L · R · L · L → ver §5): exigência do V4-SPEC para o PPP
(§2, skill-load management) e boa prática para os outros dois. Como o aluno lê muito melhor
do que ouve, o bloco pesa deliberadamente para o listening na segunda metade.

## 3. Linguagem-alvo e vocabulário (REGRA 22 — nada repete como novidade)

> Escrito ANTES de gerar e **corrigido depois** para bater com o que as cinco aulas de fato
> ensinam — o syllabus é o mapa, e mapa que diverge do território não serve para nada. As
> aulas de framework **Communicative** ensinam LINHAS funcionais nos vocab cards, não
> palavras soltas: é o que o método pede (chunks extraídos do input), e é o que está lá.

### Aula 1 — PPP — *The Update Nobody Read* — 13 slides · Reading
- **Funcional:** `We're on track for…` · `We're running about X behind` · `The blocker is…` ·
  `What I need from you is…` · `By Friday we'll have…`
- **Vocab (8):** update · on track · behind schedule · blocker · lead time · batch ·
  shipment · sign-off
- **Input:** o texto "Four hundred words nobody read" — a coordenadora cujo relatório
  completo nunca chegava a ninguém.

### Aula 2 — Communicative — *What They Actually Need* — 9 slides · Listening
- **Funcional / vocab cards (8):** `Before I confirm, can I check one thing?` ·
  `Can I ask what's driving this?` · `What happens if we don't?` · `Just to be clear…` ·
  `Do you mean X or Y?` · `So what you need is…` · `Would it help if…?` ·
  `I'll confirm by Thursday.`
- **Task:** a professora é a compradora do cliente e pede uma coisa querendo outra (peça mais
  fina, quando o problema é o peso da caixa). O aluno tem de sair da call com o requisito
  real. *Information gap por PAPEL* — a assimetria é de posição, não de conhecimento, e o
  motivo sai em três camadas, só se ele perguntar.
- **Callback da 1:** o warm-up abre com o update de 60s que ele gravou de homework.

### Aula 3 — Task-Based — *Two Suppliers, One Slot* — 9 slides · Reading
- **Funcional (exposta antes, ENSINADA só depois — é a inversão do TBL):**
  `A is cheaper, but…` · `The main trade-off is…` · `I'd go with…` · `What worries me is…` ·
  `If we go with A, we…`
- **Vocab (10):** quote · unit price · minimum order · capacity · certification · penalty
  clause · trade-off · downside · track record · to commit
- **Task Cycle:** (1) ler duas cotações e decidir; (2) defender a decisão para a professora,
  que assume a posição contrária. **Focus on Form diferido** sobre o que ele produziu:
  comparativos e hedging.
- **Callback da 2:** a decisão depende do requisito que ele extraiu na aula 2.

### Aula 4 — PPP — *Before It Becomes a Problem* — 13 slides · Listening
- **Funcional (as 4 partes de um alerta):** `Heads-up:…` · `There's a risk that…` ·
  `Unless we…, we'll…` · `The impact would be…` · `I need a decision by…`
- **Vocab (8):** heads-up · risk · impact · contingency · to escalate · to flag ·
  bottleneck · downtime
- **Skill:** Listening principal (o oposto da aula 1, que foi Reading) — um recado gravado no
  chão de fábrica, difícil de propósito, que é onde ele mais sofre. O recado tem só as duas
  primeiras partes do alerta, e o exercício é completar as outras duas.
- **Callback da 3:** o risco nasce do fornecedor que ele escolheu na aula 3.

### Aula 5 — Communicative — *The Meeting That Ends On Time* — 9 slides · Listening
- **Funcional / vocab cards (8):** `We have ten minutes` · `Can I stop you there?` ·
  `Let's park that for now` · `That's a separate conversation` · `Who owns this?` ·
  `Let's put a date on that` · `To recap` · `We're at time`
- **Task:** conduzir 10 minutos de reunião com 3 pontos, com a professora como participante
  que diverge e traz assunto fora de pauta. Cada item sai com dono e data, ou parqueado.
  Segunda task (`project`): a ata falada em 90 segundos.
- **Callback da 4:** o primeiro ponto da pauta é a decisão que ele pediu na aula 4.

## 4. Como as aulas se conectam (por que este bloco é UM curso, não 5 aulas soltas)

Uma história única, em cinco tempos, com o mesmo elenco (o cliente Michael, a compradora
Denise, o fornecedor):

```
aula 1  ele REPORTA o que está acontecendo
   ↓ o cliente responde pedindo algo que não é o que precisa
aula 2  ele DESCOBRE o pedido real
   ↓ atender ao pedido real exige trocar de fornecedor
aula 3  ele RECOMENDA e defende a escolha
   ↓ a escolha traz um risco novo
aula 4  ele SINALIZA o risco e pede decisão
   ↓ a decisão precisa de uma reunião
aula 5  ele CONDUZ a reunião e fecha
```

Cada aula abre com callback do vocabulário da anterior (REGRA 20) e a linguagem funcional se
acumula: na aula 5 ele ainda precisa do update da aula 1 para abrir a pauta.

## 5. Alternância de skill e de método (a grade do experimento)

| Aula | Framework | Skill principal | Gramática | Produção final |
|---|---|---|---|---|
| 1 | PPP | Reading | implícita | Production + Discussion |
| 2 | Communicative | Listening | sai do uso | Communicative Task (25–30 min) |
| 3 | Task-Based | Reading | **diferida** (Focus on Form no fim) | Task Cycle (2 tasks) |
| 4 | PPP | Listening | implícita | Production + Discussion |
| 5 | Communicative | Listening | sai do uso | Communicative Task |

**Nenhuma das três traz gramática explícita** — nenhum destes frameworks a admite (é o que
os GATES 12/13/14 barram). Para o aluno isso é o oposto do Imersivo, onde a regra é
descoberta e mostrada numa tabela. É o ponto mais visível do experimento e o que o Dan
precisa julgar: **um B1 que traduz do português aguenta 5 aulas sem uma tabela sequer?**

## 5.1 O que o rodízio produziu de fato (medido, 30/07/2026)

**A pré-aula é onde a diferença mais aparece** — e ela não foi decidida aula a aula: cada
framework traz a sua, e o ciclo a distribui.

| Aula | Framework | Desenho do Pre-class | O que fica de fora, de propósito |
|---|---|---|---|
| 1 | PPP | **Flipped** — glossário + texto + check + fill + speech + think | nada: no PPP o input vai antes |
| 2 | Communicative | **Ensaio + coleta** — linhas, gravação, 2 casos reais dele | o áudio da aula (é o núcleo receptivo) |
| 3 | Task-Based | **Priming + noticing** — texto, 12 linhas para observar, 2 casos | qualquer exercício de FORMA (viraria PPP) |
| 4 | PPP | **Flipped** de novo | o áudio (aqui a skill principal é Listening) |
| 5 | Communicative | **Ensaio + coleta** de novo | o áudio da aula |

Outros números: 13 · 9 · 9 · 13 · 9 slides · 72 MP3 ElevenLabs, 0 podres · 5 PRs, um por
aula, todos mergeados no verde (REGRA 32).

**O que o ciclo NÃO trivializou:** repetir o framework não repetiu a aula. As duas de PPP
diferem na skill (Reading → Listening) e as duas de Communicative diferem no papel do aluno
(responder → conduzir). O que se repete é a FORMA; o syllabus decide o resto.

## 6. O que este bloco NÃO cobre (transparência)

Escrita (o e-mail que ele manda todo dia), apresentação formal e small talk. Cabem no
bloco 2 — o bloco 1 é inteiro sobre **falar sob pressão em call**, que é onde a dor está.
