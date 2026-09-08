# GATE 22 (`check_espinha.py`) — aposentado em 08/09/2026

> O `gates.json` manda, para todo gate sem objeto: *"Reaponte-o para o requisito, ou
> aposente-o com o motivo escrito (P2 §13/§23)."* Este é o motivo escrito.

## O que ele cobrava

A ESPINHA da anatomia das quatro modalidades, em quatro regras:

| | regra |
|---|---|
| (a) | toda tela declara a sua etapa (`data-phase`) |
| (b) | a etapa declarada existe na barra |
| (c) | a barra tem 7 ou 8 etapas |
| (d) | a soma dos minutos dos rótulos fecha o `percurso_min` do contrato |

## Por que ele não media nada

Ele selecionava o material por `-aulaN.html` + `<meta name="alumni-framework">`. Medido em
08/09/2026: **zero** arquivos publicados carregam esse meta. O gate rodava no CI, imprimia
`0 aula(s)` e um `AVISO — SEM OBJETO`, e passava verde sobre um repo que nunca mediu.

## Por que ele foi aposentado, e não repontado

Os outros cinco gates cegos (19, 23, 25, 26, 27) foram repontados para a anatomia
`consultivo`, que é onde essas quatro modalidades foram ao ar. O 22 não, por duas razões
independentes — qualquer uma bastaria.

**1. As quatro regras já são cobradas, e melhor, pelo GATE 37** (`validate_consultivo.py`):

| GATE 22 | GATE 37 |
|---|---|
| (c) 7 ou 8 etapas | **R2** — exatamente OITO (Doc 03 §6.1). Mais estrito, e é o número certo desta anatomia. |
| (d) os minutos fecham o contrato | **R3** — soma contra o `CICLO.percurso` que o próprio material declara, e ainda acusa etapa sem minutos e etapa sem nome |
| (a) toda tela declara a etapa | **R5** — tela com `data-stage` e sem `data-lesson`, e aula sem nenhuma tela |
| (b) a etapa declarada existe | **R5** — telas que não representam as etapas, e etapas fora de ordem |

E o 37 lê de `LESSONS`, a fonte de onde o deck monta a barra em runtime. O 22 lia o HTML
estático da barra — que no consultivo é um resquício do artefato, reescrito na entrada do
deck. Um gate que confere o resquício não confere o que a aluna vê.

**2. A regra (d) cobra o que a norma tirou da tela.** O ajuste P8 removeu a minutagem da
barra de etapas, e o próprio shell registra o porquê:

> *"Só o nome da etapa: a minutagem saiu da barra na P8 — tempo na tela projetada é info
> técnica, e quem conduz já tem os minutos na nota e na seção B do cartão."*

Repontar (d) como estava exigiria `data-min` nos rótulos, isto é, exigiria de volta na tela
projetada exatamente o que o pacote normativo mandou sair dela.

## O que ficou no lugar

Nada foi perdido: o GATE 37 já cobrava as quatro. E a metade da (d) que o P8 mudou de lugar
— *"quem conduz já tem os minutos na nota"* — passou a ser verdade por construção no mesmo
dia: o `min` do `guia_telas.json` virou um inteiro obrigatório, o `build_consultivo.py`
exige que as telas de cada etapa somem o orçamento dela, e o **GATE 23** cobra que toda nota
abra com o tempo. Antes disso, 52 das 240 telas não diziam tempo nenhum.
