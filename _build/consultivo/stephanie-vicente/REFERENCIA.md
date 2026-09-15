# Molde stephanie-vicente — onde está cada padrão

Índice para quem gera aula nova do consultivo: **qual tela do molde mostra qual padrão, e de
qual revisão das aulas 19–21 da Gabriela Pires ele veio**. As aulas da Gabriela foram
revisadas pela professora e tomadas como exemplo pelo Dan em 15/09/2026. O que é só dela
(16 anos, A2, 85 min, aula presencial, eixo "sustentar a conversa") **não** passou para o
molde: a Stephanie continua adulta, B1, com 55 min de percurso e os temas e frameworks de
sempre.

Toda aula do molde reescrita a partir daqui tem `geracao.json` com `{"gen": 1}` e passa pelos
GATES 74 (tempo na tela), 75 (cartões encostados) e 76 (deck declarado). Aula nova copia o
carimbo — sem ele o builder recusa (`scripts/consultivo/geracao.py`).

## Padrões e onde olhar

| Padrão | Onde está no molde | De onde veio (Gabriela) |
|---|---|---|
| Atividade fechada do deck declarada em `blocos.json` com `nu: true` e `<!--BLOCOS:chave-->` na tela | aula 1, telas 5 e 6 (`ev1`, `cl1`) | aula 19, telas 5–7 (`ev19`, `tf19`, `gd19`) |
| `porque` em cada item da atividade fechada | aula 1, `ev1` e `cl1` | aula 19; `r_par` passou a emitir `porque` na revisão da aula 21 (PR #2618) |
| `Expected` do guia = gabarito: cita cada item e cada resposta (GATE 71) | aula 1, guia das telas 5 e 6 | aula 19, telas 5–7 (PR #2592); aula 21, telas 4, 5, 7, 8 (PR #2618) |
| `Expected` de tela aberta descreve como é uma resposta completa, com exemplo | aula 1, guia das telas 1, 9, 10 | aula 19, telas 1 e 12 (PR #2595, #2592) |
| `exact` (Suggested prompts) com as perguntas que o professor faz escritas por extenso | aula 1, guia das telas 9 (interrupção) e 10 (duas perguntas) | aula 20, telas 8 e 9 (PR #2605); aula 19, tela 9 (PR #2592) |
| Depois do turno preparado, uma tela de conversa: duas perguntas reais e uma pergunta da aluna de volta | aula 1, telas 9 → 10 | aula 19, telas 11 → 12 (a tela de 21 min virou duas, PR #2592) |
| Instrução em tela (`slide-question`), e não só no guia | aula 1, telas 2, 4, 5, 6, 8 | aula 21, telas 2, 3, 4 (PR #2618); aula 20, tela 8 (pergunta subiu para o topo, PR #2605) |
| Apoio da produção atrás de botão fechado ("Show the sentence starters") | aula 1, telas 9 e 10 | aula 19, telas 11 e 12 |
| Descoberta guiada: pergunta na tela, resposta atrás de botão, e o guia pede exemplos da aluna | aula 1, tela 7 | aula 21, tela 6 (PR #2618) |
| Replay = mesma tarefa com outra pessoa / nova condição (quem discorda) | aula 1, tela 11 (o professor que escreveu o plano) | aula 19, tela 13; aula 21, tela 12 (PR #2618) |
| Guia em tom descritivo ("She may", "Leave corrections for screen 11"), sem caixa-alta | aula 1, `guia_telas.json` e `guide.js` | aula 21, `guide.js` (PR #2618: *will* → *may*) |
| Nota do pre-class aponta item citando o texto, nunca por ordinal | aula 1, `notas.json` 1-5 | aula 19–22, `notas.json` (PR #2611) |
| Pre-class promete de forma permissiva ("They all appear in the documents you read in your lesson", "you can use") | aula 1, `sec2`, `sec3`, `sec5` | aula 19–22, `blocos.json` (PR #2592, #2605) |
| Callout "Optional" do post-class convida, não desobriga | aula 1, `postclass.html` | aula 19 e 20, `postclass.html` (PR #2592, #2605) |
| Espaço entre cartões empilhados (`margin-top` da escala do Kit); botão de documentos depois da atividade | aula 1, tela 5 | aula 21, tela 10 (PR #2626); aula 19, tela 6 |
| Nada de tempo de produção na tela; nada de metadado de produção ("written for this lesson") | todas as telas da aula 1 | aula 19, telas 2 e 4; aula 20, telas 1 e 8 |
| Tarefa comunicativa com opções A/B, escolhidas na própria tela | aula 2, tela 9 (o que ela precisa saber na call) | aula 21, tela 10 (Option A / Option B, PR #2618) |
| Escuta com as perguntas lidas antes do Play, e o transcript só depois da checagem | aula 2, telas 4 e 5 (`wq2`) | aula 20, telas 4–6 (PR #2605: "Before pressing play" no `exact`) |
| Conversa depois da tarefa gravada: o interlocutor faz duas perguntas escritas no `exact` | aula 2, tela 10 (Marta depois da call) | aula 19, tela 12; aula 21, tela 11 |
| Replay com nova condição: outra pessoa responde e discorda | aula 2, tela 11 (Peter responde) | aula 19, tela 13 |
| Lacuna de forma verbal declarada (`kind: lacuna`, `nu`), com o verbo entre parênteses para a resposta ser única, sem banco | aula 3, tela 7 (`cz3`) | aula 21, telas 4–6 (a mecânica tem de ser a que diz ser, PR #2618) |
| Preparação em papel antes do turno longo (opção A/B + notas), sem campos de digitação na tela | aula 3, tela 8 | aula 21, tela 10 (escreve três perguntas e as faz sem ler na tela 11) |
| A frase da aluna no diagnóstico volta mais tarde na aula, e o guia diz onde | aula 3, telas 2 → 6 → 11 | aula 21, telas 2 → 9 ("Your first six questions again") |
| Referência posicional trocada por citação: "Number 3 is the politest…" vira a frase escrita na tela | aula 4, tela 6 | notas das aulas 19–22 (PR #2611); A02 §7 |
| Opções A/B que mudam o conteúdo da conversa, com as falas do professor escritas para cada opção no `exact` | aula 4, telas 8 e 11 | aula 21, telas 10–12 (PR #2618) |
| Sem metadado de produção na tela: "The teacher and the class in this lesson are invented" sai; o cartão diz "se ela perguntar, confirme" | aula 4, tela 2 e `sec4` do pre-class | aula 19, tela 4 e cartão (PR #2592, #2595) |

## O que NÃO copiar da Gabriela

- percurso de 85 min e 13–14 telas (o molde tem 55 min; a aula 1 tem 12 telas);
- aula presencial, escola, idade, A2 e o eixo do ciclo dela;
- personagens (Maya, Chris, Nina, Leo, Sofia) e temas (filmes, escola).
