# Instrução Corretiva — Luis Fernando da Silva

> **Fonte:** feedback da professora sobre o material do private Luis Fernando Silva, enviado
> por WhatsApp em **02/09/2026**, durante e logo após a aula 1. Transcrição fiel das
> mensagens, sem resumo nem interpretação.
>
> **Escopo:** apenas o aluno `luis-fernando-da-silva`. Esta instrução **não** altera o
> builder, o modelo, os gates nem o material de qualquer outro aluno. Foi aplicada às
> aulas 2 a 10 (PR #2508) e vale para as aulas 11 a 48, que ainda não existem.
>
> **A aula 1 não foi tocada** e não deve ser: já foi dada (REGRA 30).

---

## 1. O que a professora observou

| Slide | Mensagem |
|---|---|
| 16, pergunta 2 | *"Notei que esse tipo de pergunta é um tanto abstrato para ele. Ele tem dificuldade de captar a ideia. Minha sugestão seria perguntas mais assertivas (não óbvias), como por exemplo a pergunta 3."* |
| 17 | *"A ideia aqui é make predictions before listening. Ele simplesmente não captou a ideia aqui. Não sei se imaginar cenários é algo muito abstrato pra ele."* |
| 18 | *"Ele entendeu 0% do listening. Toquei em 0.75 duas vezes. Acho que esse tipo de listening não funciona pra ele. Algo que tenha um contexto mais real (como um diálogo) onde o target language esteja contextualizado. Esse exercício deixou ele bem frustrado."* |

**Diagnóstico.** O material da aula 1 não estava rápido demais, estava abstrato demais. Os
dois listenings eram ensaios reflexivos de 152 a 192 palavras, de 70 a 80 segundos de opinião
sem situação e sem interlocutor, e ficavam mais longos a cada aula (aula 9 chegava a 192
palavras). Eram cobrados com pergunta de inferência. As aberturas de leitura e as âncoras de
predição partiam de um universal (*"Somebody who...", "Every company...", "Anybody who..."*).

---

## 2. Correções obrigatórias

As três regras abaixo valem para **toda aula nova deste aluno**. Nenhuma delas autoriza sair
do tema da aula, da estrutura gramatical que ela trabalha, nem do nível dele (B1). Onde uma
regra daqui divergir do `CLAUDE.md` ou do `_build/model/README.md`, **o sistema vence**: esta
instrução é sobre conteúdo, não sobre forma.

### 2.1 Listening: recado situacional, não ensaio

**Falha observada:** monólogo reflexivo, longo, sem destinatário e sem situação.

**Correção obrigatória:** o listening é um **recado de voz de uma pessoa nomeada para o
Luiz**, de 75 a 95 palavras (26 a 34 segundos), contendo:

- quem fala e de onde
- pelo menos um número, uma data ou um prazo
- um pedido explícito, ou uma instrução

Os dois listenings de uma mesma aula são **os dois lados do mesmo caso**: o segundo já nasce
com o contexto que o primeiro montou. O elenco se repete entre as aulas, para ele nunca ter
de montar um mundo novo: Megan (regional), Claire (conselho), Diane (eventos), Tom Baker
(conselheiro novo), Paulo Rezende (revendedor), Marco (sênior), Sandra (compliance), Almir
(veterano), Rui (eventos), Nora Whitfield (visitante).

**A gramática da aula tem de aparecer carregando fato**, não como enfeite. Na aula 2
(*present perfect com for/since*) o recado diz *"Rezende Agro has been overdue since March"*
e *"they have bought from us for eleven years"*: a forma é a da aula e a resposta é um dado.

> **O que NÃO fazer, e por quê.** A professora pediu diálogo. O gerador não permite dentro do
> listening: é **1 MP3 com 1 voz** (`_build/model/README.md`, seção *"Áudio de listening =
> MONÓLOGO"*), e o `validate_lesson.py` derruba o PR se personagens distintos dividirem voz.
> Conversa de duas pessoas vai para o bloco `dialogue-line`, que é outro slide. O contexto
> real entra pelo **gênero** do monólogo, não pela estrutura. Não prometer diálogo no
> listening e não contornar o builder para conseguir um.

### 2.2 Pergunta de compreensão: recuperação de dado, não inferência

**Falha observada:** perguntas que pedem interpretação (*"qual é a diferença", "por que isso
importa", "o que isso torna possível, socialmente", "por que vale um segundo olhar"*).

**Correção obrigatória:** toda pergunta de compreensão tem a resposta **dita com todas as
letras** na fonte. O formato aprovado pela professora é o da pergunta 3 daquele slide: duas
partes, factual, e não óbvia no sentido de exigir pescar o dado certo, não no sentido de
exigir deduzir.

| Não | Sim |
|---|---|
| *Claire does not repeat his job title. How does she describe his job in her own words?* | *Since when has Rezende Agro been overdue, and how many months is that?* |
| *Two lines on this report talk about time in opposite ways. What is the difference?* | *Since when has the oldest account been overdue, and in what year did the region open?* |

Vale para as três superfícies: listening, compreensão de diálogo e artefato. **Exercício de
produção continua** (*"Turn the first two lines into one sentence using used to"*): ali a
tarefa é produzir, e é concreta.

### 2.3 Abertura concreta: âncora de predição e primeira linha de leitura

**Falha observada:** o slide de predição não foi captado.

**Correção obrigatória:** a pergunta do slide de predição é **emitida pelo builder** e é fixa
(`inject_predict_prompts`, REGRA 2.3). Não se mexe nela. O que se escreve é a **âncora**, que
o builder extrai da primeira frase:

| Superfície | De onde sai a âncora |
|---|---|
| Listening | 1ª frase de `lesson.listenings[].text` |
| Leitura | 1ª frase de `inclass_blocks.reading[0].paras[0]` |
| Diálogo | 1ª fala do bloco `dialogue-line` |

Essa frase tem de **abrir em cena**: uma pessoa, um lugar, um número ou um momento. Nunca um
universal.

| Não | Sim |
|---|---|
| *The thing people get wrong about agricultural credit is that they compare it to a mortgage.* | *Luiz, it's Megan from the regional office.* |
| *Anybody who has joined a large company has had the same experience.* | *On your first day you are handed a chart with two hundred names on it.* |

Limite técnico: o extrator (`_primeira_frase`) pega a primeira frase entre 20 e 170
caracteres terminada em `.`, `!` ou `?`. Frase de abertura mais longa que isso é cortada.

---

## 3. Os três limites que a correção não pode atropelar

Concretude não autoriza reescrever a aula. Antes de trocar qualquer texto:

1. **Tema da aula.** O recado e a leitura ficam dentro do assunto daquela aula. O mundo é
   sempre o dele: crédito e cobrança numa empresa de defensivos, revendas e produtores,
   região sul, pagamento que segue a safra.
2. **Estrutura gramatical da aula.** O texto novo usa o `grammar_point` daquela aula e os das
   aulas anteriores, nunca o de uma aula futura. Ao reescrever a aula 5 e a 7 em 02/09/2026,
   três frases tiveram de ser corrigidas por isso: duas perguntas indiretas (aula 9) e uma
   passiva (aula 8) que tinham entrado antes da hora.
3. **Nível B1.** As leituras são B1 e continuam B1. Frase curta e vocabulário conhecido não
   é simplificar o conteúdo, é tirar o obstáculo que não estava sendo ensinado.

E uma trava de integridade: ao trocar a abertura de uma leitura, **conferir que nenhum item
de True/False, gap-fill ou compreensão citava a frase removida**.

---

## 4. Antes do PR

Os gates de sempre (`_build/model/README.md`, "Fluxo por aula"), mais estas três checagens
específicas deste aluno:

| Checagem | Como |
|---|---|
| Listening entre 75 e 95 palavras | contar `lesson.listenings[].text` |
| Âncora abre em cena, nas três superfícies | ler as `ic-predict-line` do arquivo buildado |
| Zero pergunta de inferência | varrer as `q-text` atrás de *"what is the difference"*, *"why does that matter"*, *"why is that worth"*, *"in her own words"* |

---

## 5. Histórico

| Data | O que |
|---|---|
| 02/09/2026 | Feedback da professora sobre a aula 1 |
| 02/09/2026 | PR #2508: aulas 2 a 10. Listening situacional, perguntas de dado, âncora concreta de listening. 18 MP3 regerados |
| 03/09/2026 | Abertura das leituras das aulas 2, 4, 6, 8 e 10 (âncora de predição da leitura). Sem áudio novo |
