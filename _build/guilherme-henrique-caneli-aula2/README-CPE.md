# Aula 2 do Guilherme em formato de prova (CPE)

## De onde veio

Feedback do professor Andre Marinho, 18/09/2026, depois da aula 1 (pacote de 8
aulas, C1/C1+ real). Em resumo: para um aluno que "poderia dar aula de ingles",
card de vocabulario com definicao e matching palavra-definicao e RECONHECIMENTO.
Ele pediu tarefa de prova internacional, com critical thinking e "reading between
the lines", e mandou dois modelos proprios:

- `cpe-infrastructure-finance-lesson_12.html` (C2 Proficiency, e usa exatamente o
  mesmo lexico da aula 1 deste aluno: project finance, concession, greenfield,
  sovereign wealth fund, regulatory framework)
- `w11_l11e.html` (curso proprio dele, C1, tarefas por papel da prova)

Decisao da Helen: piloto na aula 2, formato CPE, nas tres superficies
(Pre-class, IN CLASS e Complementares), seguindo os modelos do professor.

## O que NAO mudou, de proposito

- Os 14 termos do lexico e o `grammar_point` (causative have/get x passiva). Sao
  a espinha do programa; as aulas vizinhas e os 25 MP3s `pc2_*` dependem deles.
- Os tres links dos Complementares (reais e conferidos; ver REGRA 17).
- A casca das paginas: abas, stamps, progresso, audioMap, slide-mode.
- Qualquer coisa de outro aluno.

## O que mudou

A TAREFA. Cada bloco passou a ser uma tarefa no formato do exame, montada sobre
as primitivas que o hub JA tem (e que o CI ja conhece):

| Tarefa de prova | Primitiva usada |
|---|---|
| Gapped text (Paper 1, Part 6) | `.match-row` + `checkMatch()` |
| Multiple choice (Part 5) | `.quiz-item` + `selectQuiz()` |
| Word formation (Part 3) | `.blank-input` + `checkBlank()` |
| Key-word transformation (Part 4) | `.blank-input` + `checkBlank()` (`data-alt`) |
| Sentence completion (Paper 3, Part 2) | player `.lp` + `.blank-input` |
| Multiple matching, 2 tarefas (Part 4) | `.match-row` + `checkMatch()` |
| Gabarito e transcricao | `.comp-q` + `revealComp()` |

Assim o progresso continua sendo contado (updateProgress le essas classes), o
GATE 7b continua satisfeito (nenhum handler novo) e o GATE 10 tambem (reveal por
stylesheet, sem `display:none` inline).

## Audio novo

Seis MP3s, gerados pelo `gen_audio.py` do modelo (procedencia no `_src.json`):

- `pc2_talk_who_gets_paid_first.mp3` — 3 min, voz `daniel`, para o Part 2
- `pc2_mm_speaker_1..5.mp3` — ~30 s cada, CINCO vozes diferentes, para o Part 4

As cinco vozes entraram em `config.json["voices"]`, que e o eixo de sotaque POR
ALUNO (o `gen_audio` e o `validate_lesson` ja leem esse override). O
`voices.json` global NAO foi tocado: ele e compartilhado com todo mundo.

## Ordem de execucao

```
python3 _build/guilherme-henrique-caneli-aula2/build_preclass_cpe.py   # gera preclass.html
python3 _build/guilherme-henrique-caneli-aula2/build_slides_cpe.py    # gera slides.html
python3 _build/guilherme-henrique-caneli-aula2/inject_shell_l2.py     # player + reveal no hub do ALUNO
python3 _build/guilherme-henrique-caneli-aula2/inject_score_l2.py     # nota por atividade nos 2 hubs
python3 _build/guilherme-henrique-caneli-aula2/patch_hub_l2.py        # troca o card da aula 2 nos 2 hubs
python3 _build/guilherme-henrique-caneli-aula2/patch_deck_l2.py       # troca o deck + espelha o aluno
python3 _build/guilherme-henrique-caneli-aula2/patch_complementary_l2.py
ELEVENLABS_API_KEY=... python3 _build/model/gen_audio.py \
    _build/guilherme-henrique-caneli-aula2/config.json --only=<so os novos>
```

`--only` e obrigatorio: sem ele o `gen_audio` regera os 50 MP3s do manifesto
(os antigos nao estao materializados num clone parcial, entao ele nao os "pula").

## Armadilhas encontradas

1. **O hub do ALUNO nao tinha player nem reveal.** Essas funcoes so existiam no
   hub do professor, porque ate agora so a aba IN CLASS usava audio com controle.
   Sem elas, seis players e onze gabaritos ficariam mudos EM SILENCIO. Resolvido
   pelo `inject_shell_l2.py`, copiando o codigo verbatim do professor.
2. **As regras `.lp-*` do hub foram escritas para slide ESCURO.** Na aba
   Pre-class, que e clara, o player sairia branco no branco. Por isso a classe
   propria `.cpe-lp`.
3. **A navegacao do deck e hardcoded** (`totalSlides`, `slidePhases`, o texto
   inicial do contador). Trocar slides sem trocar os tres deixa o Next morto no
   slide 35. Nenhum gate pega: o JS compila. O `patch_deck_l2.py` reescreve.
4. **`insert_hub.py` nao serve aqui.** Ele e aditivo por decisao (REGRA 20) e
   pula aula que ja existe. Substituicao pede patch cirurgico.
5. **O `.think-card` so fecha com gravacao.** A tarefa de Writing nao tem
   microfone; se fosse `.think-card`, a aula nunca chegaria a 100%.
6. **Texto de leitura longo estoura a tela projetada.** O artigo foi dividido em
   quatro telas (medido no Chrome headless a 1400x900 e 1280x800).

## Segunda rodada: o que faltava do modelo do professor (18/09/2026)

Comparando tarefa por tarefa com o `w11_l11e.html`, a estrutura batia inteira
(plano com tempos, lead-in falado, collocation bank, gap-fill, gapped text,
multiple choice, word formation, transformations, sentence completion, multiple
matching com duas tarefas, collaborative task, long turn, gabarito e transcricao
na tela). Faltavam TRES coisas, agora fechadas:

**1. Nota por atividade e nota final.** Cada bloco de prova virou um `.cpe-exam`
com contador ("Correct 0 / 6") e a licao fecha num painel de nota por papel
(`cpe_lib.exam` e `cpe_lib.grade_panel`). Nao e enfeite: no modelo do professor a
questao TRAVA na primeira resposta e so a primeira conta. Por isso o
`inject_score_l2.py` embrulha `checkBlank`, `selectQuiz`, `checkMatch` e
`verifyAllMatches` -- delegando para as originais fora dos blocos de prova, de
modo que as aulas 1 e 3 a 8 do mesmo hub nao mudaram em nada. Barra de progresso
= quanto ele fez; nota = quanto ele acertou. Sao duas perguntas diferentes, e o
aluno precisa das duas.

**2. Follow-up depois do long turn.** Quatro perguntas de examinador, no deck
(slide 51) e na Pre-class (Stage 2.13). A pergunta 2 e a da gramatica da aula:
obriga a nomear o agente que ele mesmo apagou.

**3. Segundo debate.** O modelo tem dois; a aula tinha um. O novo (`DEBATE_2_*`)
da o lado ao aluno em vez de deixar escolher, e cobra CONCESSAO: reformular o
ponto mais forte do outro lado antes de responder.

Armadilhas desta rodada:

- **O contador poderia mentir.** `confere_totais()` no `build_preclass_cpe.py`
  barra bloco cujo `data-total` nao bate com as questoes que existem dentro dele,
  e painel de nota que nao soma o mesmo que as atividades.
- **Errar nao pode travar a aula em 99%.** Item errado ganha `.correct` (que e o
  que `updateProgress` conta) MAIS `.cpe-miss`, que vence no CSS e pinta de
  vermelho. Sem isso, quem errasse uma questao nunca fecharia a licao.
- **A nota vive por INDICE do item dentro do bloco.** Aula que ganhar ou perder
  questao precisa de `data-exam` novo, senao a nota antiga gruda na questao errada.
- **O percentual e sobre o RESPONDIDO, nao sobre a prova inteira.** Com 8 de 75
  feitas, "7%" se lia como reprovacao quando era so aula pela metade.
- **Nota ao professor vira atributo `data-teacher`**, e o `esc_attr` do deck
  escapa `&`: entidade HTML ali sai como texto cru. Aspas nessas strings sao
  aspas mesmo.
- **O injetor precisa poder rodar DE NOVO.** Os blocos injetados tem marca de
  inicio e de fim, e o `inject_score_l2.py` substitui em vez de duplicar. A
  primeira versao nao tinha marca de fim e obrigou a refazer os hubs do zero.

Provado em navegador (playwright, Supabase bloqueado pela regra do
[hub-teste-local]): 31 checagens, incluindo a regressao de que a aula 1 continua
deixando tentar de novo. O teste esta no scratchpad da sessao, nao no repo.

## Terceira rodada: o layout, pelo feedback do professor (21/09/2026)

Andre aprovou o CONTEUDO ("ficou bom, algo mais profundo, o aluno vai se sentir
desafiado no nivel") e reprovou o LAYOUT do deck, em dois pontos:

> "Nessa parte da leitura, o aluno tem que incluir as frases, entao cada slide
> tem alguma coisa, a leitura ficou quebrada. (...) E a mesma coisa dos audios:
> e um audio e DUAS atividades ao mesmo tempo. Teria que ser pelo menos a
> imagem da atividade toda junta, porque o aluno tem que ver todas as opcoes e
> escolher. (...) Tira uma foto dessas frases e nos vamos lendo o texto
> incluindo; eu posso ir passando as paginas."

Ele ficou so no deck (IN CLASS). A pre-class e o hub ja mostravam tudo junto,
porque sao pagina que rola: o defeito era exclusivo da tela projetada.

**1. Part 6 -- as sete frases numa imagem so.** Tela nova, `The Seven
Sentences`, antes do texto: as sete inteiras, e e essa a tela que ele fotografa.
O texto continua paginado, que foi o que ele disse que manobra.

**2. As frases eram CORTADAS em 102 caracteres com reticencias.** So no deck. A
tarefa era impossivel de responder ali: metade das opcoes so se decide pelo fim
da frase ("...a predictable income in 2050"). Agora vao inteiras nas seis telas
de lacuna e na do distrator.

**3. Part 4 -- as duas tarefas numa imagem so.** Eram duas telas, uma por
tarefa. Viraram `Two Tasks, One Page`: os cinco audios numa tira de botoes, a
Task One e a Task Two lado a lado, os cinco falantes com as duas respostas. O
gabarito das duas foi para a tela seguinte (`What Gave Each One Away`).

**4. O deck anunciava oito opcoes e desenhava cinco.** `matching()` so recebia
as opcoes USADAS, entao os tres distratores de cada tarefa nunca chegavam ao
projetor -- embora o texto da propria tela dissesse "three of the eight are not
used", e embora eles existissem no conteudo e na pre-class. Agora `matching()`
aceita `opts=` com a lista completa.

Armadilhas desta rodada:

- **Classe a mais no `.ic-choices` faz o slide sumir dos gates.** O
  `validate_lesson` (751 e 1530) e o `build_from_model` (1180) procuram a string
  `class="ic-choices"` ao pe da letra. `class="ic-choices cpe-long"` nao falha
  nada -- so faz o slide deixar de contar como checagem, e aparece um aviso novo
  que nao existia. O modificador de densidade virou `data-dense` NO CARTAO.
- **Id de audio repetido nao da erro, da botao mudo.** Os cinco falantes ja tem
  player nos slides individuais; a tira usa `mp-l2-mmx1..5`, porque com o mesmo
  id o `mpIcon` pintaria sempre o primeiro do documento.
- **Frase inteira estoura onde a cortada cabia.** Com as sete completas no
  tamanho padrao, a lista cortava 144px a 1280x800. Medido no Chrome a 1400x900
  e 1280x800: agora nenhuma tela desta aula corta.
- **O injetor de CSS nao era re-executavel.** A guarda antiga testava um unico
  seletor, entao a segunda rodada nao atualizava o resto do bloco. Agora tem
  marca de inicio e de fim, e o patcher roda duas vezes byte a byte igual.

**Fica em aberto, e NAO e desta rodada:** os slides 7, 8, 9 e 10 (o vocabulario)
cortam 127, 127, 118 e 306px a 1400x900 -- e 227, 227, 218 e 406px a 1280x800.
Ja cortavam antes desta aula virar prova, o professor nao falou deles, e por
isso nao foram tocados. Mas o slide 10 perde um terco da tela.

## Quarta rodada: a Pre-class para de ser a aula (22/09/2026)

Andre aprovou a licao e olhou o pre class:

> "Esta exatamente a mesma coisa. Pre class e licao sao exatamente a mesma coisa."

Estava. **53 dos 69 itens de exercicio eram identicos nas duas telas**, porque as
duas superficies liam as MESMAS constantes deste `lesson2_content.py`. O aluno
fazia a prova em casa e refazia a mesma prova, com os mesmos itens, na aula. A
decisao que gerou isso esta registrada no topo do `build_slides_cpe.py`, e citava
a REGRA 1: a REGRA 1 manda repetir tema, vocabulario e gramatica, e **nao** manda
repetir os itens. A REGRA 146 (`docs/REGRAS-138-A-146.md:184`) ja proibia isso
com todas as letras; nenhum gate executava a proibicao.

### O criterio, dado por ele stage a stage

| stage | o que ele mandou |
|---|---|
| ate 2.3 | fica como esta, "e so matching de vocabulario" |
| 2.4 | manter o formato, trocar as frases, **do lado do pre class** |
| 2.5 + 2.6 | viram um: "outro reading com as mesmas palavras e comprehension questions" |
| 2.7, 2.8 | manter a atividade, trocar as frases |
| 2.9 + 2.10 | viram um: "so uma atividade listen + choose" |
| 2.12 a 2.15 | removidos do pre class |
| 2.11 | ele ainda nao falou; segue como esta ate ele responder |

### Como ficou

Constantes **novas** com sufixo `_PC` (`CLOZE_ITEMS_PC`, `ARTICLE_PC` +
`COMPREHENSION_PC`, `WORD_FORMATION_PC`, `TRANSFORMATIONS_PC`, `LISTEN_PC_*`). As
antigas ficaram intactas, e e isso que garante que **o deck nao mudou um byte**:
o `build_slides_cpe.py` continua lendo as antigas, e o `patch_deck_l2.py` nao
roda nesta rodada. Os 14 termos e o `grammar_point` nao mudaram: sao a espinha do
programa.

Resultado medido: **76% -> 0%**. Nenhum item de prova da aula esta no pre class.

### Audio

Um MP3 novo, `pc2_listen_choose.mp3`, voz `ellen` -- que nao e a voz do talk da
aula (`daniel`) nem a de nenhum dos cinco falantes. 97 segundos, 295 palavras.
Se a pre-class usasse os audios da aula, o aluno chegaria tendo ouvido as mesmas
pessoas dizerem as mesmas coisas.

### Armadilhas desta rodada

1. **O `lesson-desc` do `HEADER` e escrito a mao** e anunciava "gapped text and
   multiple choice (Paper 1, Parts 6 and 5)". Virou mentira no segundo em que os
   dois sairam do pre class. O `plan_at_a_glance()` tem o mesmo problema: linhas
   e tempos cravados, incluindo uma linha "Speaking & Writing" que deixou de
   existir.
2. **O Survival Card NAO pode sair.** Ele consome o conteudo do stage 2.12, que
   foi removido, mas o `validate_lesson` exige pelo menos um survival-card por
   aula. Ele nao e exercicio: e cartao de referencia, mesma categoria do
   vocabulario que o professor liberou.
3. **O `grade()` se conserta sozinho, o `confere_totais()` nao perdoa.** O painel
   deriva os totais do tamanho das listas, entao fundir stages nao quebra a nota.
   Mas o `data-total` de cada bloco tem de bater com as questoes dentro dele.
4. **Testar o hub local grava no Supabase do aluno.** O teste de navegador desta
   rodada bloqueia `http://` e `https://` no playwright antes de clicar em
   qualquer exercicio.

### O gate, e o que ele revelou

`scripts/check_preclass_nao_repete.py` compara os itens de tarefa do deck com o
bloco `ex-lesson-N` do hub, descontando vocabulario dos dois lados (que a REGRA 1
manda repetir). **Ele e de regressao, nao de teto absoluto**, e o motivo importa:
medido nos 1.924 pares (hub, aula) que existem hoje, a mediana e 0% e a media e
5,2%, mas **257 pares passam de 10% e alguns marcam 100%** -- outros alunos, com
a mesma pergunta de compreensao e as mesmas opcoes nas duas telas. Um teto
absoluto obrigaria quem mexesse nessas aulas a consertar divida alheia antes de
mergear. Entao: aula que ja existe reprova se PIORAR; aula nova reprova acima de
15%.

**O gate NAO entrou neste PR**, e o motivo e o GATE 17, o meta-gate do registro:
gate novo tem de estar em `scripts/gates.json` E ser invocado em
`.github/workflows/`. As duas coisas, ou nenhuma -- "gate que nao roda nao barra
nada, e o registro afirma que ele barra". Como o token nao tem escopo `workflow`
e push que toca `.github/workflows` e rejeitado, as tres pecas (script, registro
e workflow) tem de entrar juntas, num PR proprio.

Destrava com `gh auth refresh -s workflow`. O script esta pronto e testado
(selftest + medicao dos 1.924 pares); falta so poder mexer no workflow.

## Quinta rodada: o pacote inteiro em formato de prova (24/09/2026)

Com as oito Pre-class prontas (#2829, #2842), os decks das aulas 3 a 8 vieram
para o modelo da aula 2, e o Stage 2.11 -- o unico que o professor nao tinha
comentado -- foi fechado pelo mesmo criterio dos outros.

### Onde mora o que

O que era generico do deck de prova saiu deste builder e virou
`_build/guilherme-henrique-caneli/cpe_deck.py`, **verbatim**: o envelope do
slide, os cartoes, as escolhas, o pareamento, os players e o gabarito. A aula 2
continua usando o builder dela, que veio primeiro. Cada aula de 3 a 8 tem um
`deck_cpe.py` proprio com a PROSA dela (titulo, ordem, nota ao professor) e um
`lesson{N}_content.py` com o conteudo de prova.

O conteudo importa o lexico e o `grammar_point` do `specs/aula{N}.py` em vez de
copiar: o spec continua sendo o dono, e os dois nunca divergem.

### As travas que valem para toda aula daqui para a frente

1. **Nada do deck pode estar na Pre-class daquela aula.** Conferido item a item
   em cada uma: 110 a 147 itens por aula, zero coincidencias. Duas foram
   pegas e reescritas (uma opcao de multipla escolha na aula 5 e um item de
   producao de gramatica na aula 3, que batia com o Survival Card).
2. **Os 14 termos aparecem no material de leitura da aula.**
3. **Zero telas cortando** a 1400x900 e a 1280x800, nas oito.

### Armadilhas desta rodada

- **O `mklesson.py` tambem grava `slides.html`.** Os dois builders gravavam no
  mesmo nome e quem rodasse por ultimo vencia, sem erro nenhum. O deck de prova
  grava `slides_cpe.html`.
- **O GATE 16 exige um exercicio de role-play** pelo contrato do framework
  (`imersivo-prototipo@1`), e so roda no servidor. A aula 2 tinha; os decks
  novos nao, e reprovaram depois de tudo pronto. Agora todos tem o degrau
  guiado, com chips na tela, antes do collaborative task.
- **As chaves de imagem mudam de aula para aula** (umas tem `ch3`, outras `ch4`,
  outras `ch7`). O deck pega o que o spec declarou, na ordem, e cicla.
- **Portugues na tela reprova.** O `WRITING_MODEL` foi escrito em portugues e
  caiu num reveal: a REGRA 13 proibe portugues no IN CLASS. O recado ao
  professor vive no `data-teacher`; o criterio na tela vai em ingles.
- **Cinco falantes exigem cinco vozes.** O `voices.json` global so tem tres e e
  compartilhado com todos os alunos. O override por aula vive no spec e o
  `mklesson` o passa para o TOPO do `config.json`, que e onde o `gen_audio` o
  procura -- dentro de `lesson` ele e ignorado em silencio.
- **Os slides 7 a 10 desta aula cortavam desde a segunda rodada** (127 a 406px)
  e ficaram assim porque nenhum gate mede corte: so o Chrome. Resolvido com a
  classe `.cpe-tight` e, no cloze, dividindo as oito lacunas em duas telas --
  apertar mais deixaria a letra ilegivel num projetor.

### Audio

42 MP3 novos: seis por aula (um talk de 3 min para a Part 2 e cinco falantes
para a Part 4), nas aulas 3 a 8. Vozes `daniel`, `alice`, `arthur`, `matilda`,
`george` e `antonio`. A `sarah_us` NAO aparece em nenhum deck: ela e a voz das
Pre-class, e o aluno nao pode chegar na aula tendo ouvido a mesma pessoa.

## Proximo passo

Se o professor aprovar, as aulas 3 a 8 seguem o mesmo caminho: escrever o
`lessonN_content.py`, reusar `cpe_lib.py`, e rodar a mesma ordem acima.
