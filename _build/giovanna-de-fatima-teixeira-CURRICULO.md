# Giovanna de Fátima Teixeira — Currículo do Programa (48 aulas, **A2**)

> Fonte única: consultoria de 01/09/2026 no Drive (transcrição `1DmgbxeQyRaj0TI9png8A2lJx8mARKhlP`,
> conduzida por **Rodrigo Guedes**) + Perfil 360 (`perfis.id = giovanna-de-fatima-teixeira`) +
> aba PRIVATE da planilha Metas_B2C.

| Campo | Valor |
|---|---|
| Slug | `giovanna-de-fatima-teixeira` |
| Modelo do material | **adulto** (o molde de sempre — sem chave `model` no config) |
| Nível | **A2** — ordem direta do Dan, 15/09/2026 (ver *Re-nivelamento*, abaixo) |
| Encontros | **48** aulas de **60 min** |
| Frequência | 1x por semana — **segundas, 21h** |
| Modalidade | Online (Zoom) |
| Idade | 23 anos |
| Profissão | Engenheira civil — obras de metrô e túnel, presencial em canteiro |
| Cidade | **Não consta em fonte nenhuma.** Ela disse só "moro no Brasil". Fica vazia — não inventar |
| E-mail | `defatimagiovanna@gmail.com` |
| Consultor | Rodrigo Guedes |
| Paleta | `--accent: #1F5673` · `--accent-light: #3E8DB5` |

---

## Re-nivelamento para A2 (15/09/2026)

**Ordem direta do Dan.** As 48 aulas passam de A1 bilíngue para **A2**, e o material é refeito
do currículo para baixo. A PRIVATE e o Perfil 360 traziam **A1**; a ordem do Dan vence, e a
divergência fica registrada aqui em vez de sumir.

**Por que dá para refazer sem ferir a REGRA 30.** O Attendance íntegro de 11/09/2026 registra
**0 encontros realizados**: as 10 aulas que estavam no ar (geradas em 02/09, em A1 bilíngue)
**nunca foram dadas**. Não há legado a preservar — há rascunho a substituir.

O que isso muda, e o que **não** muda:

| | |
|---|---|
| Muda | O ponto gramatical de cada aula: a banda A1 (verb *to be*, present simple puro) sai |
| Muda | **O idioma da tela do aluno: A2 = ZERO português** (REGRA 13). O bilíngue cai inteiro |
| Muda | A densidade: **8–10 palavras novas por aula** (A1 eram 5–7) |
| Muda | `"level": "A2"` no config de cada aula e o 1º chip do header |
| **Não** muda | O eixo (base geral + técnico de metrô e túnel), a promessa, a paleta, o modelo |
| **Não** muda | A paridade FALA/LEITURA nem a estrutura de 5 fases |

### O que "A2 = zero português" significa em cada peça

| Peça | Era (A1) | É (A2) |
|---|---|---|
| Vocab card (Pre-class 1.1) | palavra + tradução PT | palavra + **definição em inglês simples** |
| Matching (Pre-class 1.2) | palavra EN ↔ tradução PT | palavra EN ↔ **definição em INGLÊS** |
| Grammar Tip (Pre-class 1.4) | bilíngue EN + PT | **só inglês** |
| `data-hint` do fill-in-the-blank | "Dica: ..." | **"Hint: ..." em inglês** |
| Survival card | `.sp-en` + `.sp-pt` | **só `.sp-en`** |
| Speech card | `.speech-phrase` + `.speech-translation` | **só `.speech-phrase`** |
| Complementares (descrição, tip, CTA) | PT | **inglês** |
| Planejamento e `data-teacher` | PT | **PT — continua** (é do professor, o aluno não vê) |

> **Ordem de execução do chip de nível.** O gate de idioma lê o CEFR do **1º chip do header**
> (`nivel_do_html`, em `_build/model/validate_lesson.py`). Enquanto os blocos Pre-class 1–10 do
> hub ainda forem bilíngues, virar o chip para A2 faz o gate reprovar o hub inteiro (10 falhas
> de `IDIOMA A2: PORTUGUÊS no Pre-class`) e o GATE 8 barra por defeito novo em arquivo
> existente. **O chip vira `A2 (Pré-Intermediário)` no PR que entregar as 10 aulas em A2**, não
> antes.

---

## O que a consultoria revelou e moldou este currículo

1. **Ela não está começando: está voltando.** Cinco anos de curso na infância, parou aos 13,
   dez anos sem usar. A frase dela é de conclusão: *"eu quero voltar a fazer o inglês para
   concluir."* O enquadramento em toda aula é **recuperar**, nunca "aprender do zero" — e é
   isso que sustenta o A2: o que falta é uso, não capacidade.

2. **O gargalo tem nome e a consultora o mediu: preposições e estrutura de frase.**
   *"Você se confunde um pouco com algumas preposições, aí se eu vou usar o to ou não, o at or
   in."* Por isso a **aula 1** ataca preposições direto, e elas voltam como **segunda linha
   gramatical** em todas as aulas do bloco 1 — nunca como lista solta.

3. **Ela travou na ROTINA, não no vocabulário.** Repetiu *"eu me acordei às sete da manhã"*
   várias vezes sem conseguir avançar. A **aula 3** é dedicada a isso (advérbios de frequência
   + sequenciadores), com scaffolding alto: os conectivos vêm ANTES de pedir produção livre.

4. **Ela produz sem travar quando o tema é tempo livre.** Foi o único trecho da consultoria em
   que fez frases inteiras: festas, filmes, séries, cinema, música e o namorado. O **bloco 2
   inteiro** usa esse campo como plataforma para esticar a frase.

5. **Ela pediu o inglês técnico, com um plano pronto.** *"Eu pensei em dividir em 20 aulas
   voltadas para a minha área... as outras 28 voltadas mais para a questão do dia a dia."* O
   currículo acolhe: **18 aulas (31–48) são técnicas** e o contexto do canteiro atravessa o
   resto. A consultora explicou a inversão — base primeiro — e ela aceitou sem resistência.
   Na **aula 10** a professora mostra a ela este desenho: é o momento de co-autoria.

6. **Os softwares dela são em inglês e ela decorou os comandos sem entender.** *"Pelo hábito do
   dia a dia eu já acabei decorando o que é cada coisa."* A **aula 24** (zero conditional) usa
   exatamente isso: o manual do software vira leitura compreendida.

7. **A queixa número um é velocidade.** *"Quando o pessoal fala um pouco mais rápido, a gente
   acaba confundindo as palavras."* Pediu repetição duas vezes no nivelamento. Por isso as
   **aulas 35 e 39** treinam pedir esclarecimento e ouvir em ruído — e todo listening tem
   player com 0.5x a 1.25x.

8. **A vitória é medível e tem forma de conversa:** dez minutos sobre si, o trabalho e os
   gostos, com preposições corretas e sem recorrer ao português. O programa **cronometra essa
   conversa cinco vezes** (aulas 10, 20, 30, 40 e 47/48) e compara com a gravação da aula 1.

9. **Dado que NÃO existe e não vira material:** a cidade. Ela disse só *"moro no Brasil"*.
   Nenhuma aula é ancorada em cidade, bairro ou empresa. Empresa e cargo exato também não
   foram informados.

---

## A REGRA DO FATO ÚNICO

> **Nenhum fato biográfico sustenta a espinha de mais de uma aula.**

A consultoria durou pouco, foi pelo celular, no horário de almoço, com áudio cortando — o
inventário de fatos concretos é curto (cerca de 14) para 48 aulas. Se o gerador tratar cada
fato como tema disponível, esgota os quatro mais fáceis e passa a repetir. Depois da aula dona,
o fato volta como **exemplo, callback ou frase solta** — nunca como tema. As outras aulas se
sustentam em **mundos**: o canteiro, o túnel, a cidade, o tempo, o equipamento, a reunião.

### Livro-razão dos fatos

| Fato da consultoria | Aula dona | Depois disso |
|---|---|---|
| 23 anos, engenheira civil, volta ao inglês | **01** | só callback |
| Trabalho presencial em canteiro de metrô e túnel | **04** | é o mundo do programa; só a 04 é *sobre* ele |
| Confunde to / at / in | **01** | vira eixo permanente, não tema |
| Travamento ao contar a rotina | **03** | só callback |
| Festas e fim de semana | **07** | só callback |
| Cinema, filmes e séries | **11** | só callback |
| Namorado | **16** | só callback |
| Rotina corrida, só livre depois das 20h | **18** | só callback |
| Música | **19** | só callback |
| Proposta dela de dividir 20 técnicas / 28 gerais | **10** | é co-autoria, mostrada uma vez |
| Parou o inglês aos 13, cinco anos de curso | **27** | só callback |
| Softwares em inglês decorados por hábito | **24** | só callback |
| Pesquisa o termo na internet quando precisa | **36** | só callback |
| Perde o fio quando falam rápido | **35** e **39** | é gargalo de habilidade, treinado, não tema |
| Cidade | — | **não existe.** Nunca inventar |

---

## Paridade obrigatória (REGRA 29.2)

- **Aula ÍMPAR = FALA** — diálogo line-by-line + 3 role-plays (guided → semi-free → free).
- **Aula PAR = LEITURA** — texto central `ic-reading` + gist + true/false, e os role-plays.

Vale inclusive nos checkpoints (10, 20, 30, 40 — todos pares, todos LEITURA). O que muda no
checkpoint é a **densidade** (nenhum ponto gramatical novo, tudo é recuperação), nunca o formato.

## Segunda camada — o que parece repetição e não é

O programa volta a três territórios de propósito, uma camada acima e dezenas de encontros
depois. Não são repetições e não se "consertam":

| Território | Primeira | Segunda camada |
|---|---|---|
| Preposições | 01 · in / on / at (lugar e tempo) | 04 · lugar e movimento (through, along, across, into) |
| Comparação | 13 · comparativos simples | 38 · precisão (twice as deep as, slightly, far more) |
| Voz passiva | 28 · present simple | 33 · past simple |
| Futuro | 15 · going to | 16 · present continuous para arranjos → 25 · will espontâneo |

---


## Currículo — 48 aulas


### Fase 1 — A base que ela veio buscar (aulas 1–10)
*Falar de si, da rotina e do trabalho com as preposições no lugar, e entrar no passado. É o gargalo que a consultoria mediu: ela travou justamente na rotina.*

| # | Formato | Tema | Foco linguístico | Atividade principal | Homework | Vocabulário novo |
|---|---|---|---|---|---|---|
| 01 | FALA | Ten Years Later -- Giovanna Starts Again | Present simple para falar de si + preposições in / on / at (lugar e tempo) — o gap diagnosticado, atacado já na primeira aula | Diálogo line-by-line com uma engenheira estrangeira que chega ao canteiro + 3 role-plays (guided → semi-free → free) de apresentação; gravação baseline de 60s | Gravar 60s de apresentação e guardar — é o marco zero, comparado na aula 10 | site, crew, shift, commute, degree, background, break, catch up, again |
| 02 | LEITURA | A Day in the Life of a Field Engineer | Present simple na 3ª pessoa (works / starts / doesn't check) + perguntas Wh- (What does she do? Where does she work?) | Texto ic-reading sobre o dia de uma engenheira de campo + gist + true/false; matching palavra ↔ definição em inglês | Ouvir o áudio do texto 3x e responder oralmente as 5 perguntas de compreensão | field engineer, supervisor, report, schedule, inspect, task, colleague, office, daily |
| 03 | FALA | First, Then, After That -- Giovanna's Real Day | Advérbios de frequência (always / usually / often / sometimes / never) + sequenciadores (first, then, after that, finally) | Linha do tempo do dia real dela montada no slide, do despertador ao sofá + role-play contando o dia a um colega novo | Gravar 90s narrando um dia comum, usando os quatro sequenciadores | alarm, wake up, get ready, traffic, lunch break, overtime, get home, relax, routine |
| 04 | LEITURA | Under the City -- Where Everything Is | Preposições de lugar e movimento (through, along, across, into, under, above, between) sobre there is / there are | Texto descrevendo um canteiro de metrô visto de cima + planta na tela: ela localiza sete elementos; true/false | Áudio de 60s descrevendo o próprio canteiro com cinco preposições diferentes | entrance, fence, ramp, ground level, underground, gate, container, walkway, area |
| 05 | FALA | Right Now vs Every Day | Present continuous (acontecendo agora) × present simple (rotina) — o contraste, apresentado por descoberta | Diálogo ao telefone: alguém liga durante o expediente e pergunta what are you doing? + role-plays com fotos de canteiro em ação | Mandar 4 áudios ao longo de um dia dizendo o que está fazendo naquele momento | measure, wait for, take a look, be busy, meeting, right now, at the moment, hold on, speaking |
| 06 | LEITURA | What I Can and Can't Do Yet | can / can't para habilidade e permissão + could para pedido educado | Texto com o perfil de três profissionais e o que cada um pode fazer no canteiro + true/false + matching de definições | Gravar 6 frases: 3 com I can e 3 com I can't, sobre o trabalho e sobre o inglês | allowed, permission, access, badge, training, license, operate, sign, skill |
| 07 | FALA | How Was Your Weekend? | Past simple: was / were + verbos regulares (-ed), com os três sons finais (/t/ /d/ /id/) | Diálogo de segunda-feira de manhã entre dois colegas + role-plays contando o fim de semana (festa, cinema, descanso) | Gravar 60s sobre o último fim de semana, só com verbos regulares | last night, yesterday, weekend, party, dance, tired, boring, great, invite |
| 08 | LEITURA | The Week the Rain Stopped Everything | Past simple: verbos irregulares de alta frequência (went, made, took, saw, had, said, got, came) | Texto curto sobre uma semana de imprevistos no canteiro + ordenar os fatos na sequência + true/false | Ouvir o texto e recontá-lo oralmente em 6 frases, no passado | rain, delay, decision, news, mud, stuck, cover, wait, finally |
| 09 | FALA | Did You? -- Asking About the Past | Perguntas no past simple (Did you...? / What did you do?) + short answers (Yes, I did / No, I didn't) | Diálogo de entrevista rápida + role-play find someone who, com oito perguntas no passado | Entrevistar alguém com 8 perguntas no passado e gravar a conversa inteira | interview, question, answer, remember, forget, hear, meet, travel, last time |
| 10 | LEITURA | Checkpoint 1 -- Ten Minutes About Me | CHECKPOINT: recuperação das aulas 1-9. Nenhum ponto gramatical novo | Texto de revisão + a primeira simulação cronometrada da conversa de dez minutos, comparada com a gravação da aula 1; a professora mostra a ela o desenho das 48 aulas que ela mesma propôs | Ouvir as gravações da aula 1 e de hoje e anotar três diferenças concretas | — (recuperação) |


### Fase 2 — Gente, histórias e comparações (aulas 11–20)
*O campo em que ela já produz sem travar (tempo livre, gostos, pessoas) usado para esticar a frase: descrição, comparação, plano e justificativa.*

| # | Formato | Tema | Foco linguístico | Atividade principal | Homework | Vocabulário novo |
|---|---|---|---|---|---|---|
| 11 | FALA | What I Like, What I'd Rather Do | like / love / hate + -ing e prefer + -ing / infinitivo — o campo em que ela já produz sem travar | Diálogo sobre planos de sexta-feira + role-plays escolhendo entre programas (cinema, festa, ficar em casa) | Gravar 90s sobre o que gosta e o que não gosta de fazer, com cinco verbos em -ing | hang out, go out, stay in, concert, series, playlist, crowd, movie theater, soundtrack |
| 12 | LEITURA | The People at the Site | Adjetivos de descrição (aparência e personalidade) e a ordem do adjetivo antes do substantivo | Texto apresentando quatro pessoas da equipe + matching pessoa ↔ descrição + true/false | Descrever oralmente três pessoas com quem ela trabalha, com três adjetivos cada | tall, quiet, patient, helpful, strict, friendly, hardworking, serious, funny |
| 13 | FALA | Bigger, Longer, Deeper | Comparativos: adjetivo + -er than / more ... than / less ... than | Diálogo comparando dois trechos de obra + role-plays comparando cidades, trabalhos e rotinas | Gravar 6 comparações reais entre duas coisas do trabalho dela | deep, wide, narrow, heavy, expensive, modern, safe, slow, difficult |
| 14 | LEITURA | The Longest Tunnel in the World | Superlativos (the -est / the most) + ever | Texto sobre os maiores túneis do mundo (Gotthard, Channel Tunnel, Seikan) + true/false + quiz de números | Ouvir o texto 2x e responder oralmente qual é o mais longo, o mais antigo e o mais caro | record, length, century, cost, famous, huge, amazing, underwater, border |
| 15 | FALA | What Are You Going to Do? | going to para planos já decididos e para previsão com evidência | Diálogo planejando a semana no canteiro + role-plays: plano de fim de semana, plano de carreira e plano do próprio inglês | Gravar 6 planos reais para o próximo mês | plan, next week, soon, later, maybe, probably, decide, book, cancel |
| 16 | LEITURA | The Calendar on the Wall | Present continuous para compromissos marcados × going to — o grau de decisão | Texto com a agenda de uma semana de obra + gist + true/false; ela decide qual das duas formas cabe em cada linha | Contar oralmente a agenda real da semana que vem, alternando as duas formas | appointment, deadline, visit, delivery, inspection, reschedule, confirm, available, calendar |
| 17 | FALA | How Much, How Many | Quantificadores: much / many / a lot of / a few / a little + How much...? / How many...? | Diálogo de pedido de material + role-plays de compra e de conferência de estoque | Gravar 8 perguntas de quantidade sobre o trabalho e sobre a casa | material, concrete, sand, gravel, tool, truck, load, amount, order |
| 18 | LEITURA | Too Much, Not Enough | too much / too many / (not) enough + too + adjetivo | Texto com três problemas de obra causados por excesso ou por falta + true/false + gap-fill com banco de palavras | Gravar 6 frases sobre o que sobra e o que falta na rotina dela (inclusive o tempo, que só começa às 20h) | space, noise, dust, waste, shortage, extra, missing, spare, crowded |
| 19 | FALA | Because, So, But, Although | Conectivos de razão e de contraste: because, so, but, although | Diálogo justificando um atraso + role-plays: explicar uma decisão, recusar um convite e defender uma escolha de música | Gravar 5 pares de ideias ligadas, um deles com although | reason, excuse, explain, admit, complain, apologize, mistake, point, instead |
| 20 | LEITURA | Checkpoint 2 -- Halfway to Ten Minutes | CHECKPOINT: recuperação das aulas 11-19. Nenhum ponto gramatical novo | Texto de revisão que recicla os nove pontos do bloco + segunda simulação cronometrada da conversa de dez minutos | Comparar as três gravações (aulas 1, 10 e 20) e escolher o próximo alvo pessoal | — (recuperação) |


### Fase 3 — A conversa que se sustenta (aulas 21–30)
*Conselho, regra, hipótese, narrativa de incidente e opinião. Aqui a conversa passa de resposta curta a turno de fala, e o canteiro começa a entrar como contexto técnico.*

| # | Formato | Tema | Foco linguístico | Atividade principal | Homework | Vocabulário novo |
|---|---|---|---|---|---|---|
| 21 | FALA | What Should I Do? | should / shouldn't para conselho + Why don't you...? | Diálogo: um colega novo pede conselho sobre o primeiro dia + role-plays de conselho (trabalho, estudo, viagem) | Gravar 5 conselhos para alguém que vai começar a trabalhar em obra | advice, tip, careful, ready, worried, nervous, confident, calm, suggest |
| 22 | LEITURA | Site Rules -- What You Must and Must Not Do | have to / don't have to × must / mustn't: obrigação, ausência de obrigação e proibição | Texto com o regulamento de um canteiro + true/false + classificar cada regra em obrigatória, proibida ou opcional | Gravar as 6 regras reais do canteiro dela, escolhendo a forma certa para cada uma | rule, helmet, boots, vest, warning, forbidden, entry, visitor, permit |
| 23 | FALA | If It Rains, We Stop | First conditional (If + present simple, will + verbo) | Diálogo de decisão sob previsão do tempo + role-plays de plano B | Gravar 6 frases If ..., I'll ... sobre a semana que vem | weather, forecast, storm, wind, risk, postpone, dry, flood, otherwise |
| 24 | LEITURA | If You Press This Button | Zero conditional (If + present simple, present simple): a regra fixa da máquina e do processo | Texto com o manual em inglês de um equipamento — o software que ela decorou vira leitura compreendida + true/false | Abrir um software do trabalho e gravar 5 frases If you click ..., it ... | button, screen, menu, click, press, switch, setting, restart, error |
| 25 | FALA | I'll Do It -- Deciding on the Spot | will para decisão espontânea, oferta e promessa — em contraste com o going to da aula 15 | Diálogo com três imprevistos seguidos + role-plays de oferta de ajuda | Gravar 6 reações espontâneas com I'll a seis situações dadas | offer, promise, favor, handle, take care of, sort out, right away, no problem, deal |
| 26 | LEITURA | While We Were Working | Past continuous × past simple, com when e while — narrar um incidente | Texto com o relato de um incidente no canteiro + ordenar a sequência + true/false | Contar oralmente, em 6 frases, algo que aconteceu enquanto ela fazia outra coisa | incident, suddenly, notice, shout, fall, hurt, avoid, luckily, damage |
| 27 | FALA | I Used to Study English | used to para hábitos e situações do passado que acabaram | Diálogo sobre quem eu era aos 13 + role-plays comparando antes e agora (escola, cidade, trabalho) | Gravar 90s sobre o que ela fazia aos 13 anos e não faz mais | childhood, teenager, quit, miss, grow up, back then, these days, memory, used to |
| 28 | LEITURA | How a Tunnel Is Built | Voz passiva no present simple (the concrete is poured, the walls are lined) | Texto de processo em seis etapas + ordenar as etapas + true/false; a primeira leitura técnica de verdade | Explicar oralmente, em 5 passos passivos, um processo do trabalho dela | pour, lining, reinforce, seal, drill, remove, install, layer, surface |
| 29 | FALA | I Think So -- Opinions and Reactions | Estruturas de opinião, concordância e discordância: I think / In my opinion / I agree / I'm not sure about that / It depends | Diálogo de discussão leve sobre um filme e sobre uma decisão de obra + role-plays com escala de concordância | Gravar reação a 6 afirmações, sem repetir a mesma abertura | opinion, point of view, agree, disagree, depend, doubt, obvious, fair, actually |
| 30 | LEITURA | Checkpoint 3 -- Talking Without Portuguese | CHECKPOINT: recuperação das aulas 21-29. Nenhum ponto gramatical novo | Texto de revisão + simulação de dez minutos com regra dura: nenhuma palavra em português; a professora conta os pedidos de socorro | Ouvir a gravação e anotar as três palavras que faltaram — elas viram o vocabulário pessoal do bloco 4 | — (recuperação) |


### Fase 4 — Inglês técnico I: o canteiro, o túnel, a máquina (aulas 31–40)
*O bloco que ela pediu na consultoria. Experiência profissional, processo construtivo, equipamento, medida e instrução de campo.*

| # | Formato | Tema | Foco linguístico | Atividade principal | Homework | Vocabulário novo |
|---|---|---|---|---|---|---|
| 31 | FALA | Have You Ever Worked on a Tunnel? | Present perfect para experiência (Have you ever...? / I've worked on...) — o primeiro tempo composto do programa | Diálogo de apresentação profissional a um engenheiro estrangeiro + role-plays de troca de experiência | Gravar 6 frases de experiência profissional com ever e never | experience, project, contractor, client, site manager, handover, milestone, so far, promotion |
| 32 | LEITURA | For Six Years, Since 2020 | Present perfect com for e since: duração que continua | Texto com a linha do tempo de uma carreira em infraestrutura + true/false + gap-fill de for/since com banco de palavras | Gravar 6 frases com for e com since sobre a vida e o trabalho dela | graduate, trainee, position, department, company, team leader, responsibility, achievement, growth |
| 33 | FALA | The Tunnel Was Excavated in 2019 | Voz passiva no past simple — a segunda camada da aula 28 | Diálogo contando a história de uma obra a um visitante + role-plays de visita guiada ao canteiro | Gravar 6 frases passivas no passado sobre uma obra que ela conhece | excavate, bore, portal, segment, grout, assemble, launch, stage, complete |
| 34 | LEITURA | Step by Step -- Reading a Method Statement | Sequência de processo escrita (first, next, once, after that, until, finally) + imperativo em instrução técnica | Texto com um method statement real simplificado + ordenar as etapas + true/false | Ler o texto em voz alta cronometrado e depois resumi-lo em 5 frases sem olhar | method, procedure, step, sequence, ensure, apply, verify, approve, attach |
| 35 | FALA | Could You Tell Me...? -- Asking in a Meeting | Perguntas indiretas (Could you tell me...? / Do you know if...?) e pedido de esclarecimento (Sorry, do you mean...?) | Diálogo de reunião em ritmo natural, em que a aluna PRECISA interromper e pedir esclarecimento + role-plays de reunião | Gravar 6 perguntas indiretas que ela faria na próxima reunião real | agenda, minutes, update, clarify, repeat, follow up, raise, summarize, stakeholder |
| 36 | LEITURA | Tunnel Boring Machine -- Words Made of Two Words | Substantivos compostos técnicos (noun + noun) e onde cai o acento: tunnel boring machine, ground settlement, safety harness | Texto sobre a TBM + matching composto ↔ definição em inglês + true/false | Listar e gravar 8 compostos que aparecem nos softwares e nas plantas que ela usa | tunnel boring machine, cutter head, conveyor belt, safety harness, ground settlement, water table, retaining wall, hard hat, access shaft |
| 37 | FALA | Numbers That Matter -- Depth, Width, Tonnes | Números, medidas e dimensões faladas: metros, toneladas, porcentagem, decimais, datas e anos | Diálogo de passagem de dados por telefone (o clássico erro de número) + role-plays ditando e conferindo medidas | Gravar 10 medidas reais do trabalho dela, faladas em voz alta | depth, width, diameter, gradient, ton, cubic meter, percent, average, measurement |
| 38 | LEITURA | Cut-and-Cover or TBM? | Comparação com precisão: twice as deep as, slightly wider, far more expensive, not nearly as fast — a segunda camada da aula 13 | Texto comparando dois métodos construtivos + tabela de dados + true/false | Comparar oralmente dois métodos ou dois equipamentos, com quatro graus diferentes de diferença | cut-and-cover, alternative, advantage, drawback, efficient, costly, suitable, compare, twice |
| 39 | FALA | Do It Carefully -- Giving Instructions on Site | Advérbios de modo e de grau na instrução: carefully, properly, immediately, tightly, gently | Diálogo de instrução em campo com ruído de fundo + role-plays: instruir, confirmar e corrigir uma execução | Gravar 8 instruções curtas, cada uma com um advérbio diferente | carefully, properly, immediately, tightly, gently, straight away, on purpose, by hand, step back |
| 40 | LEITURA | Checkpoint 4 -- The Technical Ten Minutes | CHECKPOINT: recuperação das aulas 31-39. Nenhum ponto gramatical novo | Texto de revisão técnica + simulação: dez minutos explicando a própria obra a um engenheiro estrangeiro | Comparar com a gravação da aula 30 e listar o vocabulário técnico que já sai automático | — (recuperação) |


### Fase 5 — Inglês técnico II: problema, reunião, apresentação (aulas 41–48)
*O técnico em uso: reportar pane, passar turno, propor solução, escrever e apresentar. Fecha com a conversa de dez minutos que é a vitória declarada dela.*

| # | Formato | Tema | Foco linguístico | Atividade principal | Homework | Vocabulário novo |
|---|---|---|---|---|---|---|
| 41 | FALA | It Broke Down Again | Phrasal verbs de operação e de falha: break down, shut down, set up, run out of, check out, come off | Diálogo de pane em equipamento + role-plays reportando problema por rádio e por telefone | Gravar 6 frases descrevendo panes reais, cada uma com um phrasal verb diferente | break down, shut down, set up, run out of, check out, come off, leak, jam, spare part |
| 42 | LEITURA | He Said the Shift Was Over | Reported speech simples com say e tell — passar recado entre turnos | Texto com o caderno de passagem de turno + true/false + transformar 6 falas diretas em relato | Relatar oralmente 5 coisas que alguém disse a ela esta semana | shift handover, message, note, pass on, warn, remind, mention, according to, log |
| 43 | FALA | Why Don't We Try This? | Sugestão e proposta: Why don't we...? / We could... / Let's... / How about + -ing / Shall we...? | Diálogo de reunião de solução de problema + role-plays propondo, aceitando e recusando propostas | Gravar 6 propostas para um problema real do trabalho dela | suggestion, proposal, option, budget, resource, contingency, priority, trade-off, approach |
| 44 | LEITURA | The Report and the Email | Conectivos de texto escrito (however, therefore, in addition, this means that) + registro formal × informal | Texto com o mesmo fato contado num e-mail informal e num relatório formal + comparação lado a lado + true/false | Ler o relatório em voz alta e reescrevê-lo oralmente como e-mail informal | attachment, subject line, regards, formal, informal, brief, request, summary, concern |
| 45 | FALA | Let Me Show You the Project | Sinalização de apresentação: First of all / Let me show you / As you can see / Moving on / To sum up | Diálogo com uma apresentação curta de projeto + role-plays: ela apresenta a própria obra em três minutos | Gravar três minutos apresentando a obra dela, com quatro sinalizadores diferentes | cross-section, alignment, station box, layout, overview, slide, highlight, audience, presenter |
| 46 | LEITURA | About, Around, Roughly -- When You Don't Know Exactly | Aproximação e estimativa: about, around, roughly, at least, up to, more or less | Texto com uma ficha de dados de números aproximados + true/false + reescrever 6 números exatos como estimativas | Gravar 8 quantidades do trabalho dela, todas aproximadas | estimate, approximately, at least, up to, tolerance, allowance, range, figure, accurate |
| 47 | FALA | Ten Minutes, No Portuguese -- The Rehearsal | Recuperação integrada de todo o programa. Nenhum ponto gramatical novo — a professora só marca reparos | Ensaio completo da conversa de dez minutos (si, trabalho, gostos), feedback ao final e um segundo take corrigido | Ouvir os dois takes e escolher a versão que vai para a aula 48 | — (recuperação) |
| 48 | LEITURA | Grand Finale -- Giovanna Speaks | Avaliação integrada e fechamento. Nenhum ponto gramatical novo | Leitura final sobre o que muda depois de 48 aulas + a conversa de dez minutos, cronometrada, gravada e comparada lado a lado com a gravação da aula 1 | — (fim do programa) | — (recuperação) |


---

## Instruções permanentes para quem gerar qualquer aula deste programa

1. **A2 = ZERO português na tela do aluno** (REGRA 13). Pre-class, IN CLASS e Complementares em
   inglês, inclusive `data-hint`, `<option>` e `placeholder`. O PT do professor (aba
   Planejamento e `data-teacher`) **continua** — é a exceção do rulebook.
2. **8–10 palavras novas por aula**, nenhuma repetida de aula anterior (REGRA 22 /
   `check_vocab_progression.py`). O bloco "Vocabulário novo" de cada linha do currículo é o contrato:
   são as palavras dos reveal cards. **Checkpoints (10, 20, 30, 40) e as aulas 47–48 não trazem
   palavra nova** — reciclam o bloco inteiro, e é por isso que passam no gate de densidade.
3. **Um ponto gramatical por aula, e nunca um que já apareceu.** A coluna "Foco linguístico"
   vira `lesson.grammar_point` no config — é ela que o `check_grammar_progression.py` lê.
   Ver a tabela de segunda camada acima antes de julgar repetição.
4. **Paridade ímpar/par** (REGRA 29.2), sem exceção.
5. **Preposição é a segunda linha gramatical de toda aula do bloco 1**, ancorada em situação
   real. É a fraqueza que o Perfil 360 nomeou e a vitória declarada dela a menciona por escrito.
6. **Ritmo e velocidade:** todo listening com player 0.5x–1.25x, e a frase de reparo
   ("Sorry, could you say that again?") ensinada na aula 1 e cobrada até o fim.
7. **`data-teacher` sempre em português**, com timing, CCQs e a instrução padrão:
   **conte até cinco em silêncio antes de ajudar** — ela é reflexiva e costuma chegar sozinha;
   e **nunca corrija no meio da fala** (reformulação implícita na frase seguinte).
8. **Complementares:** 3 por aula, com link para o episódio/vídeo exato, verificado por HTTP,
   e **descrição/tip/CTA em inglês** (A2). **Barrados:** cursos pagos (English Pod, ESLPod,
   EnglishClass101) e HBR — o Perfil 360 recomenda ESL Pod, e essa recomendação **não vale**.
9. **Nunca marcar nada fora da janela da noite** — ela trabalha presencialmente em canteiro e
   só está livre a partir das 20h. A aula é segunda, 21h.
10. **Vozes:** dois personagens adultos, `ellen` (feminino) e `arthur` (masculino), uma voz
    consistente por personagem, declarada em `data-voice` (REGRA 20).
