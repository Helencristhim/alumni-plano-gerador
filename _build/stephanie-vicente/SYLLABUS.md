# Syllabus provisório — Stephanie Vicente (molde adulto oficial)

> **Provisório até o checkpoint da aula 4.** O perfil inicial é uma hipótese pedagógica: as
> aulas 1–4 ensinam **e** diagnosticam, e o que sair delas confirma, ajusta ou reconfigura as
> aulas 5–20. Produzir as 5–20 antes do checkpoint é decidir antes de saber.

**Ciclo:** 20 aulas · 5 blocos · 4 modalidades por bloco · **B1** · 60 min nominais
(55 de percurso essencial + 5 de margem).

## A rotação

As quatro modalidades giram em cada bloco.

- **Bloco 1: Reading → Listening → Grammar → ESP. Ordem FIXA.** Não é escolha nossa: a
  apresentação normativa de agosto/2026 fixa exatamente esta sequência no slide 5 e a marca
  **"Ação Obrigatória"** (transcrição em `docs/NORMATIVO-arquitetura-frameworks-2026-08.md`).
  Ela também se sustenta sozinha: o **Reading entrega conteúdo e evidência antes de a aluna
  ser cobrada em produção**, e o **ESP fecha o bloco integrando** o que as três primeiras
  alimentaram — colado no checkpoint da aula 4, que lê as quatro juntas.
- **Blocos 2 a 5: ordem variável.** É o que o `.docx` normativo diz (§3, *"com ordem
  variável"*). A ordem de cada bloco se decide pelo estado pedagógico e se **declara** em
  `rodizios[]` de `public/data/frameworks.json` antes de o bloco ser gerado. Aqui o ESP
  fecha, porque ali ele deixa de ser sonda e vira integração.

> **Revisão registrada (11/08/2026).** Até esta data o bloco 1 **abria com ESP**, pelo
> argumento de que a etapa 2 dele (*Initial attempt*) pede produção sem apoio nenhum e é o
> melhor instrumento diagnóstico de uma abertura de ciclo. O argumento não foi refutado — foi
> **subordinado ao documento**: os dois normativos divergem (o `.docx` diz "ordem variável", a
> apresentação fixa o bloco 1), e o Dan decidiu que vale a apresentação. O ESP continua sendo
> a sonda sem apoio; ela agora acontece na aula 4, imediatamente antes do checkpoint. O
> histórico da ordem anterior está em `rodizios[0].historico` do `frameworks.json`.

| Bloco | Título de trabalho | Função | Apoio |
|---|---|---|---|
| **1 · Build** (1–4) | O que eu vi na aula | Ensinar e diagnosticar ao mesmo tempo. Testa H1–H3. | Alto |
| **2 · Explore** (5–8) | O que foi realmente dito | Ampliar exposição a variação, precisão e ambiguidade. | Alto–moderado |
| **3 · Organize** (9–12) | Ocupar espaço na conversa | Sistematizar gestão de turno, discurso longo e escrita. | Moderado |
| **4 · Challenge** (13–16) | Sustentar a recomendação | Contestação e imprevisibilidade, com apoio seletivo. | Seletivo |
| **5 · Transfer** (17–20) | Conduzir | Situação nova, apoio mínimo, produto final. | Mínimo adequado |

---

## Bloco 1 · Build — O que eu vi na aula

| # | Modalidade | Situação | Produto / evidência |
|---|---|---|---|
| 1 | **Reading** · R1 | O plano de aula contra o syllabus do curso | Briefing de 3 min para a coordenadora, com a divergência apontada e atribuída |
| 2 | **Listening** · L1 | Call de três pessoas sobre a adoção de um material | Retomar a call: quem defendeu o quê, e uma pergunta de esclarecimento |
| 3 | **Grammar** · G1 | Descrever a cena × avaliar a cena | Cinco momentos de aula relatados: o que estava acontecendo, o que aconteceu, o que se recomenda |
| 4 | **ESP** · E1 | Dar a devolutiva de uma observação de aula a um professor estrangeiro | Devolutiva completa + resposta a duas objeções + segunda rodada com uma premissa nova |

**Aula 1 — Reading: Duas fontes que deveriam concordar** · *Objetivo:* localizar três
divergências entre o plano de aula e o syllabus, e atribuir cada afirmação à sua fonte.
· *Funcional:* `The syllabus says X, but the plan has Y.` · `These two don't line up on…`
· *Foco:* referência coesiva e linguagem de discrepância. · *Diagnóstico:* **abre o bloco com
evidência de compreensão de texto denso e de atribuição de fonte** — o critério 4 do ciclo é
medido aqui pela primeira vez. Entrega, de saída, o conteúdo e o vocabulário de trabalho que
as três aulas seguintes reaproveitam.

**Aula 2 — Listening: A call sobre o material** · *Objetivo:* acompanhar três vozes sem
transcript e identificar quem defende o quê. · *Funcional:* `Sorry, could I just check —
did you say…?` · `So if I understood, you'd rather…` · *Foco:* identificar posição e
recuperar uma lista dita uma vez só. · *Diagnóstico:* **H2** — com apoio escrito à mão, ela
escuta ou lê?

**Aula 3 — Grammar: A cena e o veredito** · *Objetivo:* separar o que **estava acontecendo**
do que **aconteceu**, e a descrição da recomendação. · *Funcional:* `The students were
working in pairs when…` · `You could try…` · `It might help if…` · *Foco:* past continuous ×
past simple por função narrativa; modais de recomendação. · *Diagnóstico:* a **etapa 2 é
diagnóstica** e produz, sem apoio, a descrição de três cenas — primeira evidência de **H3**
(o contínuo escapa sob carga?) e de **H1** (a recomendação sai como `you have to`?).
· *Relação com a aula 4:* aqui se trabalha o **efeito** da escolha sobre quem recebe; lá a
mesma escolha é cobrada numa devolutiva inteira, sem apoio.

**Aula 4 — ESP: A devolutiva** · *Objetivo:* dar retorno de observação de modo que o professor
possa discordar. · *Funcional:* `What I noticed was…` · `One thing you might try is…` ·
`How did that feel from where you were?` · *Foco:* mitigação como recurso, não como objeto de
estudo. · *Diagnóstico:* a **etapa 2 (Initial attempt) pede produção sem apoio nenhum** — é a
sonda mais limpa do bloco, e ela cai **imediatamente antes do checkpoint**, que cruza esta
evidência com a da aula 3. Fecha H1, H2 e H3. · **Pre-class sem conteúdo de ensino, por
desenho** — a etapa 2 exige produção sem apoio, e um pre-class que ensine transforma a
tentativa em repetição do material. **A ausência é propriedade do framework ESP, não da
posição 1:** ela viajou com ele quando a ordem mudou. As aulas 1, 2 e 3 têm pre-class normal.

> **Checkpoint — aula 4.** Validar nível por habilidade, decidir H1–H3, confirmar adequação
> dos contextos e definir se as aulas 5–20 são confirmadas, ajustadas ou reconfiguradas.

---

## Bloco 2 · Explore — O que foi realmente dito

| # | Modalidade | Situação | Produto / evidência |
|---|---|---|---|
| 5 | Listening · L2 | Datas, cargas horárias e condições ditas rápido | Seis dados críticos recuperados + dois lidos de volta |
| 6 | Grammar · G2 | O que foi combinado × o que foi sugerido | Cinco falas ambíguas reformuladas, com o efeito justificado |
| 7 | Reading · R2 | A ementa da editora contra o e-mail do representante | Três divergências + a pergunta que vai para a call |
| 8 | **ESP** · E2 | Abrir a call e levantar o ponto difícil sem criar atrito | Abertura + a divergência em três formulações de dureza crescente |

## Bloco 3 · Organize — Ocupar espaço na conversa

| # | Modalidade | Situação | Produto / evidência |
|---|---|---|---|
| 9 | Listening · L3 | Quem fala quando, numa reunião de quatro pessoas | Grade de turnos + três entradas próprias numa discussão nova |
| 10 | Grammar · G3 | O que se pode afirmar, sugerir e não prometer | Seis afirmações recalibradas por grau de compromisso |
| 11 | Reading · R3 | A história de uma mudança de método, em fontes fora de ordem | Apresentação estruturada de 4 min + perguntas imprevistas |
| 12 | **ESP** · E3 | O resumo escrito da reunião, no tempo real de trabalho | E-mail cronometrado + segunda versão |

## Bloco 4 · Challenge — Sustentar a recomendação

| # | Modalidade | Situação | Produto / evidência |
|---|---|---|---|
| 13 | Listening · L4 | O professor que discorda sem dizer que discorda | Mediação do desacordo + retask com a inferência corrigida |
| 14 | Grammar · G4 | Precisão quando não há tempo para pensar | Seis respostas de 45 s + segunda versão de duas |
| 15 | Reading · R4 | A proposta da editora: premissas, riscos e omissões | Recomendação de 3 min defendida contra duas objeções |
| 16 | **ESP** · E4 | Defender a recomendação quando a premissa muda no meio | Conversa de 10 min com duas alterações não anunciadas |

## Bloco 5 · Transfer — Conduzir

| # | Modalidade | Situação | Produto / evidência |
|---|---|---|---|
| 17 | Listening · L5 | Oito minutos de formação, e o report interno | Mapa de tópicos + report oral de 3 min |
| 18 | Grammar · G5 | A história inteira de uma mudança | Narrativa de 5 min: o que houve, o que teria sido, o que ainda depende |
| 19 | Reading · R5 | Duas avaliações divergentes, uma recomendação | Recomendação de 4 min + defesa sob objeção |
| 20 | **ESP** · E5 | A devolutiva inteira — produto final do ciclo | Simulação de 14 min + plano de transferência |

---

## Reciclagem da linguagem prioritária

Não se ensina uma vez. Reaparece em contexto e tarefa diferentes:

| Linguagem | Introduzida | Reciclada em | Cobrada em |
|---|---|---|---|
| Atribuição de fonte | Aula 1 | 7, 11, 15 | 19, 20 |
| Cena × veredito (contínuo × simples) | Aula 3 | 5, 11, 14 | 18, 20 |
| Mitigação de recomendação | Aula 3 · cobrada inteira em 4 | 6, 10, 13 | 16, 20 |
| Gestão de turno e reparo | Aula 9 | 13, 16, 17 | 20 |

## As mecânicas — o que a anatomia tem, medido no artefato

O inventário saiu das Diretrizes §4 cruzado com o que o artefato de referência **de fato
contém**. Duas mecânicas que este syllabus prometia numa versão anterior — *ordering* e
*information gap* — **não existem na anatomia** e foram retiradas: eram invenção minha, não
do modelo. Duas outras estavam no artefato e faltavam aqui:

| mecânica | estado |
|---|---|
| matching · multiple choice · fill in the blanks · true/false · rephrasing · case/decision · role-play · replay/retask | já existiam no builder |
| **sorting** | portada do artefato (classificação em colunas) |
| **call player** | portada — a call é uma sequência de turnos com voz por personagem e recorte por segmento |
| **autoavaliação de confiança** | portada — fecha as quatro aulas do artefato; registra percepção, não aprendizagem |
| ~~ordering~~ · ~~information gap~~ | **não existem no artefato** — retiradas |

## O que NÃO é regra fixa neste ciclo

Nenhuma aula tem etapa autônoma de vocabulário, banco obrigatório de palavras, número fixo de
perguntas, dois slides por etapa, ou fechamento por recordação de palavras. **O número de
slides deriva do orçamento de minutos**, não de um piso. O apoio lexical varia por bloco:
repertório e prompts nos blocos 1–2, critérios nos blocos 3–4, apoio mínimo ou posterior no
bloco 5. O fechamento de cada aula é feedback aplicado, nova tentativa ou plano de
transferência.

## Governança

O horizonte pedagógico é sempre de 20 aulas. O pacote contratado determina quantas podem ser
produzidas — não redefine a lógica curricular. Se o pacote terminar antes da aula 20, emitir
relatório parcial e preservar o estado para continuidade.

> Isto **não é regra deste aluno**: é do programa, e por isso deixou de morar só aqui. A
> fonte declarada — com o que fazer quando o pacote é maior (96, 48) ou menor (15, 10) que o
> ciclo, e com as **três rotas depois da aula 20** (novo ciclo no mesmo nível · módulo
> intermediário · próximo nível, cada uma com seu critério) — é
> **`_build/model/ciclo.json`**, seções `governanca_ciclo_x_pacote` e `rotas_pos_ciclo`.
> Ali também vivem a **progressão A1–C1 por operação cognitiva**, os **10 campos obrigatórios
> de cada aula do syllabus**, o **microciclo de Guided Discovery em 6 operações** e a
> **cadência de lotes e checkpoints**.

**Este molde produz apenas o bloco 1.** As aulas 5–20 exigem o checkpoint da aula 4, que exige
uma aluna real observada por um professor. Molde não tem isso — e é por isso que o bloco 1 é
o teto do que um molde pode conter.
