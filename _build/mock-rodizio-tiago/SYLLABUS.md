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

### Aula 1 — PPP — *The Update Nobody Read*
- **Funcional:** `We're on track for…` · `We're running about X behind` · `The blocker is…` ·
  `What I need from you is…` · `By Friday we'll have…`
- **Vocab (10):** update · on track · behind schedule · blocker · milestone · lead time ·
  batch · shipment · rework · sign-off
- **Artefato:** o e-mail de status que ninguém leu (HTML/CSS), base do gist.

### Aula 2 — Communicative — *What They Actually Need*
- **Funcional:** `Just to be clear…` · `Do you mean X or Y?` · `So what you need is…` ·
  `Can I check one thing?` · `Let me repeat that back to you.`
- **Vocab (10):** requirement · assumption · scope · deadline vs. target date · spec ·
  clarify · confirm · misunderstanding · follow-up · workaround
- **Task:** a professora é a compradora do cliente e pede uma coisa querendo outra. O aluno
  tem de sair da call com o requisito real escrito. *Information gap por PAPEL* — a
  assimetria é de posição, não de conhecimento.
- **Callback da 1:** o update da aula 1 é o que abre a call.

### Aula 3 — Task-Based — *Two Suppliers, One Slot*
- **Funcional (exposta antes, ENSINADA só depois — é a inversão do TBL):**
  `A is cheaper, but…` · `The main trade-off is…` · `I'd go with…` · `What worries me is…` ·
  `If we go with A, we…`
- **Vocab (10):** quote · unit price · minimum order · capacity · certification · penalty
  clause · trade-off · downside · track record · to commit
- **Task Cycle:** (1) ler duas cotações e decidir; (2) defender a decisão para a professora,
  que assume a posição contrária. **Focus on Form diferido** sobre o que ele produziu:
  comparativos e hedging.
- **Callback da 2:** a decisão depende do requisito que ele extraiu na aula 2.

### Aula 4 — PPP — *Before It Becomes a Problem*
- **Funcional:** `Heads-up:…` · `There's a risk that…` · `Unless we…, we'll…` ·
  `I need a decision by…` · `The impact would be…`
- **Vocab (10):** heads-up · risk · impact · contingency · to escalate · to flag ·
  bottleneck · downtime · buffer · to postpone
- **Skill:** Listening principal (o oposto da aula 1, que foi Reading) — uma call ruim, com
  ruído, que é onde ele mais sofre.
- **Callback da 3:** o risco que ele sinaliza nasce do fornecedor que escolheu na aula 3.

### Aula 5 — Communicative — *The Meeting That Ends On Time*
- **Funcional:** `Let's park that for now.` · `Can we agree on…?` · `Who owns this?` ·
  `To recap:…` · `Anything else before we close?`
- **Vocab (10):** agenda · action item · owner · to park · to recap · minutes · next steps ·
  to wrap up · off-topic · deadline extension
- **Task:** conduzir 10 minutos de reunião com 3 pontos, com a professora como participante
  que foge do assunto. Fechar com action items nomeados.
- **Callback da 4:** um dos 3 pontos da pauta é a decisão que ele pediu na aula 4.

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

## 6. O que este bloco NÃO cobre (transparência)

Escrita (o e-mail que ele manda todo dia), apresentação formal e small talk. Cabem no
bloco 2 — o bloco 1 é inteiro sobre **falar sob pressão em call**, que é onde a dor está.
