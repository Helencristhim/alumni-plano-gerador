# REGRAS ABSOLUTAS DE EXECUÇÃO — 138 A 144

## REGRA 138 — 90 MINUTOS UNIVERSAL EM MATERIAL DO PROFESSOR E PLANO DE AULA

Todas as aulas no Material do Professor e no Plano de Aula têm conteúdo para 90 minutos, independente do nível CEFR do aluno.

VÁLIDO PARA: A0 adulto, A1 adulto, A2 adulto, B1 adulto, B2 adulto, C1 adulto, C1+ adulto, C2 adulto.

EXCEÇÃO ÚNICA: Crianças (5-12 anos) têm aulas de 30 minutos independente do nível CEFR.

A distribuição PPP varia por nível mas o tempo total é sempre 90 minutos (ou 30 para crianças).
- Plano de Aula tem tabela de tempos somando 90 minutos.
- Material do Professor tem conteúdo visual suficiente para 90 minutos.
- Pre-class continua sendo 30-45 minutos de preparação antes da aula.

---

## REGRA 139 — VOCABULARY + EXPRESSIONS OBRIGATÓRIOS EM TODOS OS NÍVEIS

Todo Pre-class tem seção de Vocabulary E seção de Expressions, independente do nível CEFR.

ADAPTAÇÃO POR NÍVEL:
- A0: 6-8 palavras + chunks funcionais simples. NÃO ensina alfabeto/cores/números básicos. Começa com situações reais.
- A1/A2: 7-10 palavras + chunks funcionais e idiomáticas transparentes.
- B1: 8-10 palavras + 2-3 idiomatic + 2-3 collocations + 1-2 phrasal verbs.
- B2: 10-12 palavras + 3-4 collocations + 2-3 phrasal verbs + 1-2 idiomáticas + hedging.
- C1/C1+: 10-12 palavras + 4-5 collocations + 3-4 phrasal verbs + 2-3 idiomáticas culturais + discourse markers.
- C2: refinamento, 10 mínimo + variações regionais, slang sofisticado, idioms literários.

REGRA: nenhum Pre-class é publicado sem AMBAS as seções (Vocabulary + Expressions).

---

## REGRA 140 — NUNCA REPETIR VOCABULÁRIO/EXPRESSIONS COMO NOVO CONTEÚDO

Vocabulário e Expressions ensinados como NOVO CONTEÚDO em uma aula NUNCA se repetem como novo conteúdo em aulas posteriores.

PERMITIDO: revisão, callback, production, atividades complementares.
PROIBIDO: reapresentar como novo, listar como inédito.

Sistema rastreia lista cumulativa por aluno/programa. Validação automática ao gerar nova aula.

---

## REGRA 141 — ÁUDIOS SEMPRE ELEVENLABS, SEM EXCEÇÃO

Todo botão Ouvir/Listen em qualquer página usa ÁUDIO MP3 ELEVENLABS.
- VOZ: Arthur (inglês americano)
- FORMATO: .mp3
- LOCAL: /public/audio/{perfilId}/
- Web Speech API existe APENAS como fallback de emergência.

VERIFICAÇÃO OBRIGATÓRIA: extrair TODAS as frases com botão Ouvir, gerar MP3, construir audioMap, verificar correspondência, incluir variantes (contrações, ponto final).

CONSEQUÊNCIA: se alguma frase não tem MP3, material é REJEITADO.

---

## REGRA 142 — INVOCAR FUNÇÃO UX/UI AO CRIAR NOVA PÁGINA

Toda nova página HTML invoca função UX/UI obrigatoriamente.

Garante: consistência Alumni (#003080, #d70c0c, #f5f5f0), WCAG AAA (7:1), responsividade mobile-first, microinterações 200ms, tema claro, estrutura semântica, alt text, labels, imports design-system.css.

REGRA: nenhuma página nova é criada sem passar por UX/UI. Sem exceção.

---

## REGRA 143 — INGLÊS AMERICANO COMO PADRÃO ABSOLUTO

Todo material, vocabulário, pronúncia, expressões, spelling e exemplos usam INGLÊS AMERICANO por padrão.

- Spelling: color (não colour), organize (não organise), center (não centre)
- Pronúncia/áudio: sotaque americano (Arthur ElevenLabs)
- Datas: March 15th (não the 15th of March)
- Vocabulário: apartment (não flat), elevator (não lift), schedule (não timetable)
- Expressões: American idioms e collocations

EXCEÇÃO ÚNICA: quando o perfil do aluno indicar necessidade de inglês britânico (ex: trabalha com UK, evento em Londres), o material deve SINALIZAR explicitamente: "[British English]" antes do termo/expressão britânica, seguido do equivalente americano.

REGRA: nenhum material é publicado com mistura não sinalizada de variantes. American English é o default. Qualquer desvio é marcado.

---

## REGRA 144 — MATERIAIS ATIVOS SÃO INTOCÁVEIS

Nenhuma mudança no sistema — seja em componentes compartilhados, documentação, prompts, templates ou qualquer outro arquivo — pode alterar, quebrar ou modificar materiais de alunos com status ATIVO.

**O QUE É MATERIAL ATIVO:**
- Qualquer `/public/professor/{id}.html` ou `/public/aluno/{id}.html` de aluno que já está em aula
- Materiais que já foram entregues ao professor e/ou ao aluno

**PROIBIDO (sem exceção):**
- Modificar HTML de aluno ativo sem pedido EXPLÍCITO ("vamos trabalhar no material da Daniela")
- Remover, renomear ou alterar a assinatura de funções em componentes compartilhados (exercises.js, design-system.css, audio-generator.js, image-validator.js)
- Deploy que quebre funcionalidade de materiais ativos

**COMPONENTES COMPARTILHADOS — regras de retrocompatibilidade:**
- exercises.js: APENAS adicionar funções novas. NUNCA remover ou renomear funções existentes (checkBlank, selectQuiz, checkMatch, verifyAllMatches, checkOrder, selectOrderItem, moveItem, startRecording, stopRecording, speakPhrase, startFreeRecording, stopFreeRecording, toggleLesson, listenBlank, playAllVocab, toggleMediaDone, toggleChecklist)
- design-system.css: APENAS adicionar classes/variáveis novas. NUNCA remover ou renomear existentes
- Novas features vão em funções/classes NOVAS, sem tocar as antigas

**FLUXO CORRETO PARA MELHORIAS:**
1. Testar no material em desenvolvimento (aluno novo ou material sendo criado)
2. Se aprovado, incorporar ao padrão do sistema (docs)
3. Novos materiais já nascem com a melhoria
4. Materiais ativos SÓ migram quando explicitamente solicitado

**VERIFICAÇÃO ANTES DE CADA DEPLOY:**
- `stat -f "%Sm %N" public/professor/*.html public/aluno/*.html` — confirmar que APENAS o arquivo em trabalho foi modificado
- Testar 1 URL de material ativo no navegador

CONSEQUÊNCIA: se um material ativo for alterado sem pedido explícito, a mudança deve ser REVERTIDA imediatamente.

---

## REGRA 145 — PROFESSOR É A BASE, ALUNO É DERIVADO

O arquivo do professor é a FONTE DE VERDADE. O arquivo do aluno é um ESPELHO parcial extraído dele. Nunca o contrário.

**FLUXO DE PRODUÇÃO (ordem obrigatória):**

```
1. CRIAR arquivo professor/{id}.html (5 abas completas)
2. EXTRAIR Pre-class + Atividades Complementares → aluno/{id}.html
3. VALIDAR ambos (5 checks obrigatórios)
4. GERAR áudios ElevenLabs
5. DEPLOY
```

**O QUE CADA ARQUIVO CONTÉM:**

| | Professor | Aluno |
|--|-----------|-------|
| Planejamento Pedagógico | SIM | NÃO |
| Pre-class | SIM | SIM (espelho) |
| Plano de Aula | SIM | NÃO |
| Material do Professor | SIM | NÃO |
| Atividades Complementares | SIM | SIM (espelho) |
| Teacher Guide / Gabaritos | SIM | NÃO |
| Homework | SIM | NÃO |

**REGRA DE PROPAGAÇÃO:**
- Qualquer correção no Pre-class ou Atividades Complementares do professor DEVE ser propagada para o aluno
- O conteúdo do Pre-class no professor e no aluno é IDÊNTICO (mesmo HTML, mesmos exercícios, mesmas frases)
- O conteúdo das Atividades Complementares no professor e no aluno é IDÊNTICO
- Se uma palavra, frase, exercício ou áudio muda no professor → muda no aluno
- NUNCA editar o aluno diretamente sem antes editar o professor

**VERIFICAÇÃO:**
- Após qualquer edição no professor, comparar Pre-class e Complementares com o aluno
- Se houver divergência → aluno deve ser regenerado a partir do professor

---

## REGRA 146 — CONCORDÂNCIA OBRIGATÓRIA ENTRE AS 4 ABAS DE CONTEÚDO

As 4 abas de conteúdo pedagógico (Pre-class, Plano de Aula, Material do Professor, Atividades Complementares) DEVEM abordar o MESMO tópico, as MESMAS palavras e o MESMO contexto gramatical. Sempre. Sem exceção.

**O QUE É IDÊNTICO entre as abas:**
- Vocabulário: as MESMAS 8-12 palavras/expressões
- Gramática: a MESMA estrutura gramatical (ex: present simple, verb to be)
- Tema: o MESMO contexto profissional (ex: "introdução profissional", "descrevendo colegas")
- Survival Card: as MESMAS frases progressivas

**O QUE É DIFERENTE entre as abas (mesma matéria, aplicação diferente):**

| Aba | Propósito | Como aplica o conteúdo |
|-----|-----------|----------------------|
| **Pre-class** | PREPARAR — primeiro contato | Matching, fill-in, quiz, pronúncia, roleplay guiado. Aluno estuda SOZINHO antes da aula. Introduz vocabulário e gramática pela primeira vez. |
| **Plano de Aula** | CONDUZIR — roteiro do professor | Tabela PPP com 9 fases, CCQs, alertas de obstáculo, drilling notes. Descreve COMO o professor deve usar o Material do Professor. |
| **Material do Professor** | APROFUNDAR — tela compartilhada | Warm-up, vocabulário com NOVAS frases-exemplo, diálogo situacional, gramática visual, oral drilling, role-play livre. REFORÇA e CONSOLIDA o que o Pre-class preparou. |
| **Complementares** | REFORÇAR — exposição passiva | Séries, podcasts, YouTube relacionados ao tema. Aluno consome ENTRE aulas. |

**A RELAÇÃO PEDAGÓGICA:**
- Pre-class PREPARA de forma consistente → o aluno chega à aula com vocabulário reconhecido e gramática introduzida
- Plano de Aula + Material do Professor APROFUNDAM → reforçam o que já foi visto, aplicam em contextos novos, consolidam o aprendizado através de produção oral
- Atividades Complementares REFORÇAM → exposição passiva ao mesmo tema via mídia autêntica

**PROIBIDO:**
- Pre-class com vocabulário X e Material do Professor com vocabulário Y (palavras diferentes = material quebrado)
- Plano de Aula abordando gramática A e Pre-class abordando gramática B (tudo deve ser a mesma estrutura)
- Material do Professor repetindo os MESMOS exercícios do Pre-class (mesma matéria, exercícios DIFERENTES)
- Atividades Complementares sobre tema desconectado da aula

**EXEMPLO CONCRETO (Aula 1 — Maísa):**
- Vocabulário nas 4 abas: Finance, Company, Partner, Meeting, Schedule, Client, Nervous, Practice
- Gramática nas 4 abas: Verb to be (am/is/are)
- Pre-class: matching Finance→Finanças, fill-in "Maísa ___ a financial professional" (is), quiz sobre pronomes
- Material do Professor: diálogo Maísa-David no elevador usando as MESMAS palavras, oral drilling PT→EN, role-play livre
- Complementares: Suits S1E1 (contexto corporativo com as mesmas palavras)

**VALIDAÇÃO:**
- Extrair lista de vocabulário de cada aba → devem ser IDÊNTICAS
- Extrair estrutura gramatical de cada aba → deve ser a MESMA
- Extrair tema de cada aba → deve ser o MESMO
- Exercícios/frases de cada aba → devem ser DIFERENTES (mesma matéria, aplicação diferente)

---

## REGRA META — COERÊNCIA ABSOLUTA ENTRE AS 5 ABAS (CONSOLIDADA)

As 5 abas mantêm coerência ABSOLUTA conforme Regras 145 e 146:
1. PLANEJAMENTO: define jornada, critério de sucesso, survival kit
2. PRE-CLASS: PREPARA o aluno — primeiro contato com vocabulário + gramática (aplicação A)
3. PLANO DE AULA: roteiro do professor — conduz a aula usando o Material do Professor
4. MATERIAL DO PROFESSOR: APROFUNDA e CONSOLIDA — mesma matéria do Pre-class, exercícios diferentes (aplicação B)
5. ATIVIDADES COMPLEMENTARES: REFORÇA — exposição passiva via mídia conectada ao tema

HIERARQUIA: Professor é a base → Aluno é derivado (Pre-class + Complementares espelhados).
PROPAGAÇÃO: Mudança no professor → propaga para o aluno. Nunca editar aluno diretamente.
VALIDAÇÃO: vocabulário idêntico nas 4 abas, aplicações diferentes, tema coerente.
