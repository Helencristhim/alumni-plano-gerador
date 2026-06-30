# Auditoria — coerência Pre-class ↔ aula IN CLASS (REGRA 29)

> Gerado por `_build/model/check_preclass_coherence.py` em 2026-06-30. Relatório — **não conserta nada**. Decisão de campanha de conserto fica com o Dan.

## Resumo

- Pares hub/aula analisados: **891**
- **HARD FAIL (incoerente, bloqueia PR): 17** — em 2 aluno(s): pricila-adamo, sandra-hayasaki
- WARN (sinal isolado título/gramática, advisory): 58
- Aulas de review (exceção, dispensadas): 51
- Coerentes: 727  ·  Pulados (markup ilegível): 0

HARD FAIL = vocab do Pre-class **disjunto** do da aula (sinal de alta precisão, pega o caso Sandra), ou título **e** gramática divergindo juntos sem vocab legível. Sinais isolados de título/gramática viram WARN (títulos narrativos do IN CLASS divergem do literal do Pre-class sem serem incoerentes).

## HARD FAIL — Pre-class incoerente (corrigir o bloco `ex-lesson-N` no hub)

| Aluno | Aula | O que diverge |
|---|---|---|
| pricila-adamo | 1 | VOCAB disjunto (Pre-class não previewa o vocab da aula) · TÍTULO divergente (IN CLASS "Reintroducing Myself at B2" vs Pre-class "Who Is Pricila Adamo?") |
| pricila-adamo | 2 | VOCAB disjunto (Pre-class não previewa o vocab da aula) |
| pricila-adamo | 3 | VOCAB disjunto (Pre-class não previewa o vocab da aula) · TÍTULO divergente (IN CLASS "A Fresh Chapter Ahead" vs Pre-class "The Retirement Dream") |
| pricila-adamo | 4 | VOCAB disjunto (Pre-class não previewa o vocab da aula) |
| pricila-adamo | 5 | VOCAB disjunto (Pre-class não previewa o vocab da aula) · TÍTULO divergente (IN CLASS "Wellbeing &amp; Resilience" vs Pre-class "Health and Wellness") |
| pricila-adamo | 6 | VOCAB disjunto (Pre-class não previewa o vocab da aula) |
| pricila-adamo | 7 | VOCAB disjunto (Pre-class não previewa o vocab da aula) · TÍTULO divergente (IN CLASS "The Perfect Stay: Hotels" vs Pre-class "At the Hotel") |
| pricila-adamo | 8 | VOCAB disjunto (Pre-class não previewa o vocab da aula) · TÍTULO divergente (IN CLASS "Navigating New Cities" vs Pre-class "Getting Around") |
| pricila-adamo | 9 | VOCAB disjunto (Pre-class não previewa o vocab da aula) |
| pricila-adamo | 10 | VOCAB disjunto (Pre-class não previewa o vocab da aula) |
| pricila-adamo | 11 | VOCAB disjunto (Pre-class não previewa o vocab da aula) · TÍTULO divergente (IN CLASS "The Confident Conversationalist" vs Pre-class "Small Talk -- Conversation with Strangers") |
| pricila-adamo | 12 | VOCAB disjunto (Pre-class não previewa o vocab da aula) · TÍTULO divergente (IN CLASS "Diplomatic Disagreement" vs Pre-class "Sharing Opinions -- Agreeing & Disagreeing") |
| pricila-adamo | 13 | VOCAB disjunto (Pre-class não previewa o vocab da aula) · TÍTULO divergente (IN CLASS "Stories Worth Telling" vs Pre-class "Making Plans & Invitations") |
| pricila-adamo | 14 | VOCAB disjunto (Pre-class não previewa o vocab da aula) · TÍTULO divergente (IN CLASS "Staying in Touch" vs Pre-class "Phone & Messages") |
| pricila-adamo | 15 | VOCAB disjunto (Pre-class não previewa o vocab da aula) · TÍTULO divergente (IN CLASS "Handling the Unexpected" vs Pre-class "Asking for Help & Emergencies") |
| pricila-adamo | 16 | VOCAB disjunto (Pre-class não previewa o vocab da aula) |
| sandra-hayasaki | 5 | VOCAB disjunto (Pre-class não previewa o vocab da aula) |

### pricila-adamo (aulas 1–16 — 16 aulas, programa inteiro)

O IN CLASS foi **refeito em B2** (idiomático) mas os blocos Pre-class do hub continuam com o vocab/tema **A1-A2 antigos**. Mesmo tema geral, vocab disjunto — o Pre-class não previewa a aula. Ex. aula 6 (Travel): IN CLASS = `a layover / jet lag / overbooked / to clear security`; Pre-class = `boarding pass / carry-on / check-in / luggage`. Os títulos também denunciam: aula 1 IN CLASS "Reintroducing Myself at B2" vs Pre-class "Who Is Pricila Adamo?".

| Aula | Vocab IN CLASS (amostra) | Vocab Pre-class (amostra) |
|---|---|---|
| 1 | a career path, a fresh perspective, a milestone, a turning point, demanding | abroad, accomplish, confident, experience, explore |
| 2 | a defining moment, a gut feeling, a leap of faith, a pivotal moment, a setback | achievement, challenge, chapter, decade, memorable |
| 3 | a bucket list, a fresh start, an aspiration, attainable, long-overdue | adventure, bucket list, dream, embrace, freedom |
| 4 | a getaway, a hidden gem, a landmark, awe-inspiring, bustling | ancient, authentic, breathtaking, cozy, crowded |
| 5 | burnout, downtime, overwhelmed, resilience, self-care | balance, habit, mindful, prescription, prevent |
| 6 | a connecting flight, a layover, baggage claim, customs, ground staff | aisle seat, boarding pass, carry-on, check-in, delay |
| 7 | a discrepancy, a suite, a vacancy, a wake-up call, an upgrade | amenities, check-out, complaint, double room, floor |
| 8 | a crosswalk, a detour, a one-way street, a pedestrian, a roundabout | exit, fare, line, platform, stop |
| 9 | a craving, a generous portion, bland, hearty, peckish | allergy, bill, dessert, main course, menu |
| 10 | a knock-off, a rip-off, a steal, an impulse buy, on a tight budget | bargain, cash, change, discount, market |
| 11 | a lull, an acquaintance, rapport, tactful, to change the subject | awkward, coincidence, icebreaker, in common, local |
| 12 | a counterargument, a fair point, common ground, to agree to disagree, to be at odds | a good point, it depends, on the other hand, opinion, point of view |
| 13 | a mishap, a turning point, an anecdote, eventful, to end up | a plan, a suggestion, available, sounds good, to invite |
| 14 | a catch-up, a long-lost friend, to catch up, to check in on, to drift apart | a missed call, an extension, the line is busy, to call back, to dial |
| 15 | a backup plan, a contingency plan, a curveball, a hiccup, a worst-case scenario | a pharmacy, a wallet, a witness, an emergency, first aid |
| 16 | a daily allowance, a flat rate, a hidden cost, a markup, a service charge | a banknote, a fee, a receipt, a transaction, an atm |

### sandra-hayasaki aula 5

- IN CLASS "My Life in 3 Minutes (Conversation)" (vocab: background, challenge, dream of, grow up, look forward to, memory…) vs Pre-class "Review -- My Life in 3 Minutes" (vocab: confident, fluent, improve, mistake, practice, progress…). O Pre-class previewa uma aula de "Review" com vocab totalmente diferente — caso de referência do gate.

## WARN — sinal isolado (advisory, não bloqueia)

Título narrativo do IN CLASS ≠ título literal do Pre-class, **ou** termo gramatical genérico solto diverge. Conferir caso a caso — muitos são coerentes.

| Aluno | Aula | Sinal |
|---|---|---|
| aline-sberci | 5 | aula=['going to'] vs Pre-class=['present perfect'] |
| andreia-heins | 9 | aula=['comparative', 'superlative'] vs Pre-class=['past simple', 'present continuous', 'present simple', 'used to'] |
| andreia-heins | 19 | aula=['conditional', 'second conditional'] vs Pre-class=['modal', 'modals'] |
| anna-flavia-miranda-da-silva | 2 | TÍTULO divergente (IN CLASS "Anna Flávia's" vs Pre-class "My Daily Routine") |
| anna-flavia-miranda-da-silva | 3 | TÍTULO divergente (IN CLASS "Anna Flávia's" vs Pre-class "My Workspace") |
| carlos-vinicius-vale-bassan | 6 | TÍTULO divergente (IN CLASS "Agreement and" vs Pre-class "Persuading, Compromising & Navigating Disagreement") |
| daniel-bastos | 2 | TÍTULO divergente (IN CLASS "Vista del Profesor -- Daniel Bastos / Clase 2 -- Mi Día" vs Pre-class "Mi Día en Sucafina -- Rutina y Horario") |
| dienane-brandao-de-mesquita | 2 | TÍTULO divergente (IN CLASS "Dienane's Day" vs Pre-class "My Daily Routine") |
| dienane-brandao-de-mesquita | 4 | TÍTULO divergente (IN CLASS "Dienane Orders Breakfast" vs Pre-class "Food and Drinks") |
| dienane-brandao-de-mesquita | 5 | TÍTULO divergente (IN CLASS "Dienane Schedules a Meeting &mdash; Lesson 5 / Alumni by Better" vs Pre-class "Numbers and Time") |
| diogo-leal | 3 | TÍTULO divergente (IN CLASS "The Weekly Sprint" vs Pre-class "My Week at Oracle — Describing Daily Routines") |
| diogo-leal | 4 | TÍTULO divergente (IN CLASS "The Coffee Break" vs Pre-class "Breaking the Ice — Small Talk Strategies") |
| eduarda-gabriel | 13 | aula=['have to'] vs Pre-class=['conditional', 'first conditional', 'present simple'] |
| eduarda-gabriel | 14 | aula=['have to'] vs Pre-class=['present perfect', 'present perfect continuous'] |
| eduarda-gabriel | 15 | aula=['present perfect', 'present perfect continuous'] vs Pre-class=['conditional', 'first conditional', 'third conditional'] |
| eduardo-chiba | 6 | aula=['present perfect'] vs Pre-class=['imperative'] |
| fabiana-michelly-silva | 4 | aula=['modal'] vs Pre-class=['past perfect', 'past simple', 'used to'] |
| fabiana-michelly-silva | 17 | aula=['passive'] vs Pre-class=['imperative'] |
| fernanda-gabriela-silva-rodrigues | 1 | TÍTULO divergente (IN CLASS "Diagnostic" vs Pre-class "Who Is Fernanda? -- First Words in English at Sucafina") |
| fernanda-gabriela-silva-rodrigues | 7 | aula=['present simple'] vs Pre-class=['present continuous'] |
| graziele-dias | 1 | TÍTULO divergente (IN CLASS "Diagnostic" vs Pre-class "Who Is Graziele? -- First Hello at the Hospital") |
| helio-santana | 2 | TÍTULO divergente (IN CLASS "Vista del Profesor -- Helio Santana / Clase 2 -- Mi Día" vs Pre-class "Mi Día en HS Private -- Rutina y Horario") |
| karina-macedo | 8 | aula=['going to'] vs Pre-class=['used to'] |
| marcos-mansour | 9 | aula=['present simple'] vs Pre-class=['present continuous'] |
| maria-claudia-curimbaba | 5 | TÍTULO divergente (IN CLASS "Maria Claudia at the Gallery" vs Pre-class "Colors and Opinions") |
| maria-claudia-curimbaba | 6 | TÍTULO divergente (IN CLASS "The Invisible Hand" vs Pre-class "The Passive Voice") |
| milton-sayegh | 7 | aula=['going to'] vs Pre-class=['comparative', 'superlative'] |
| milton-sayegh | 17 | aula=['past perfect'] vs Pre-class=['conditional', 'third conditional'] |
| nilo-mesquita-patucci | 7 | aula=['have to'] vs Pre-class=['modal', 'modal verb'] |
| nilo-mesquita-patucci | 8 | aula=['have to'] vs Pre-class=['passive', 'passive voice'] |
| nilo-mesquita-patucci | 13 | aula=['question word'] vs Pre-class=['used to'] |
| nilo-mesquita-patucci | 14 | aula=['conditional', 'first conditional', 'present simple'] vs Pre-class=['used to'] |
| rafael-de-andrade-brandao | 2 | TÍTULO divergente (IN CLASS "Rafael de Andrade Brand&atilde;o / Alumni by Better" vs Pre-class "Your Daily Story") |
| rafael-de-andrade-brandao | 3 | TÍTULO divergente (IN CLASS "Rafael de Andrade Brand&atilde;o / Alumni by Better" vs Pre-class "Your Company Story") |
| rafael-de-andrade-brandao | 10 | aula=['modal'] vs Pre-class=['used to'] |
| rafael-de-andrade-brandao | 12 | aula=['comparative', 'going to'] vs Pre-class=['conditional', 'first conditional', 'used to'] |
| rafael-pelizaro | 3 | aula=['going to'] vs Pre-class=['comparative'] |
| rafael-pelizaro | 18 | aula=['past simple', 'present simple'] vs Pre-class=['reported speech'] |
| roberto-pires | 1 | aula=['going to'] vs Pre-class=['present simple'] |
| roberto-pires | 3 | TÍTULO divergente (IN CLASS "IN CLASS / Alumni by Better" vs Pre-class "Survival Kit Part 2 -- Numbers, Prices, and Saying No Politely") |
| roberto-pires | 4 | aula=['going to'] vs Pre-class=['past simple'] |
| roberto-pires | 7 | aula=['present continuous'] vs Pre-class=['imperative'] |
| roberto-rezende | 2 | TÍTULO divergente (IN CLASS "From Lab" vs Pre-class "My Professional Identity") |
| roberto-rezende | 3 | TÍTULO divergente (IN CLASS "Roberto's" vs Pre-class "Weekly Routines") |
| roberto-rezende | 4 | TÍTULO divergente (IN CLASS "The Engine" vs Pre-class "Meeting the Team") |
| roberto-rezende | 7 | aula=['going to'] vs Pre-class=['comparative', 'superlative'] |
| roberto-rezende | 8 | aula=['comparative'] vs Pre-class=['tag question'] |
| roberto-rezende | 9 | TÍTULO divergente (IN CLASS "Email" vs Pre-class "Writing Professional Emails") |
| roberto-rezende | 11 | TÍTULO divergente (IN CLASS "The Agenda" vs Pre-class "Running a Meeting") |
| rubens-tofolo | 5 | aula=['present perfect'] vs Pre-class=['comparative', 'superlative'] |
| rubens-tofolo | 7 | aula=['going to'] vs Pre-class=['used to'] |
| tania-rosa | 2 | aula=['going to'] vs Pre-class=['can / could'] |
| tuca-dias | 7 | aula=['question word'] vs Pre-class=['past simple', 'used to'] |
| vanessa-giuriati | 15 | TÍTULO divergente (IN CLASS "Professor View &mdash; Vanessa Giuriati / Aula 15 &mdash; Rich Descriptions" vs Pre-class "Describing People, Places & Feelings") |
| victor-malvezi-paschotto | 11 | aula=['past simple'] vs Pre-class=['past continuous', 'past perfect'] |
| victor-malvezi-paschotto | 17 | aula=['infinitive'] vs Pre-class=['imperative'] |
| walyson-ginaldo-silva | 1 | TÍTULO divergente (IN CLASS "Diagnostic" vs Pre-class "Who Is Walyson? -- First Impressions at the Coffee Summit") |
| walyson-ginaldo-silva | 2 | aula=['present simple'] vs Pre-class=['used to'] |
