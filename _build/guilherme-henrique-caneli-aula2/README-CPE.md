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

## Proximo passo

Se o professor aprovar, as aulas 3 a 8 seguem o mesmo caminho: escrever o
`lessonN_content.py`, reusar `cpe_lib.py`, e rodar a mesma ordem acima.
