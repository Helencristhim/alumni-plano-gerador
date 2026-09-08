> **Documento normativo importado do Drive — nao editar aqui.**
> Origem: `A04_Referencial_CEFR_para_Nivelamento_e_Calibracao_Linguistica_v1.3.docx`
> Drive ID: `1W_SfHdaKB2lAc8IHDVDDNacsFOWQWp5z`
> Modificado no Drive: 2026-09-03
> Reimportar: conector do Drive (`read_file_content` com o fileId acima). Os BYTES do .docx nao
> chegam integros por este caminho — em 08/09/2026 o round-trip corrompeu o zip em 2 de 3
> tentativas (CRC invalido) —, entao a importacao usa o texto renderizado pelo conector, e nao
> o `docx_to_md.py`.
> A fonte e o .docx no Drive. Divergencia entre este arquivo e o Drive se resolve reimportando,
> nunca editando o .md.

# A04 — Referencial CEFR para Nivelamento e Calibração Linguística

PRIVATE BLACK · A04 · REFERENCIAL CEFR

ADENDO NORMATIVO

Private Black Adults

> **Finalidade.** Fonte normativa única para atribuição de nível e calibração linguístico-comunicativa no Private Black. Este adendo não altera nem substitui a metodologia, os frameworks ou a arquitetura de produção vigentes.

| Estatuto | Ordem de aplicação | Faixa efetiva |
| :-: | :-: | :-: |
| Normativo | Leitura prévia obrigatória antes do pacote | A0/Pre-A1 a C1; C2 como referência superior para C1+ |

Versão 1.3 · 03 de setembro de 2026

## Como usar este adendo

> **Regra de fronteira.** O CEFR é a referência normativa para declaração de nível de proficiência e calibração linguístico-comunicativa. Não determina metodologia, framework, arquitetura da aula, quantidade ou duração de etapas, quantidade de slides nem organização Pre-class, In-class e Post-class.

Este documento consolida a interpretação operacional que o gerador, o professor e o auditor devem aplicar antes de interpretar qualquer referência ao CEFR presente no pacote. A consulta direta às fontes ou a leitura posterior de outro documento não autoriza criar uma regra concorrente. Se uma situação não estiver suficientemente resolvida aqui, ela deve ser registrada para decisão normativa; não deve ser preenchida por inferência livre.

### Fluxo obrigatório de decisão

| 1. Evidência | 2. Escala pertinente | 3. Descritor | 4. Qualidade | 5. Decisão |
| :-: | :-: | :-: | :-: | :-: |
| Desempenho observável em contexto | Atividade/competência relevante ao perfil | Capacidade demonstrada, não presumida | Autonomia, controle, alcance e condições | Faixa sustentada + emergências + lacunas |

> **Resultado esperado.** Toda declaração de nível deve ser rastreável. O registro mínimo contém: habilidade ou atividade; situação e tarefa; evidência; escala CEFR pertinente; descritores sustentados; condições e apoios; qualidade observada; faixa atribuída; características emergentes; e insuficiências de evidência.

### Mapa do documento

| Seção | Função |
| :-: | :-: |
| 1. Escopo e fontes | Delimita autoridade, precedência, nomenclaturas e proveniência. |
| 2. Declaração de nível | Transforma evidência em faixa sustentada por habilidade e perfil. |
| 3. Atividades comunicativas | Seleciona as escalas pertinentes de recepção, produção, interação e mediação. |
| 4. Competências comunicativas | Qualifica como o desempenho é realizado. |
| 5. Repertório do inglês | Usa o Core Inventory como referência de plausibilidade, não como currículo obrigatório. |
| 6. Nivelamento de conteúdo | Distingue nível do aluno, input, tarefa e produção esperada. |

## 1. Escopo, fontes e proveniência

### 1.1 Autoridade normativa

O A04 é a fonte única de interpretação CEFR para o Private Black. Sua autoridade se limita a:

- atribuição e revisão de faixa de proficiência;
- seleção e interpretação de escalas e descritores pertinentes;
- caracterização das faixas de transição;
- calibração linguístico-comunicativa de input, tarefa e produção esperada;
- distinção entre critérios CEFR e heurísticas institucionais de produção.

O A04 não redefine decisões pedagógicas ou técnicas que pertencem aos documentos responsáveis do pacote. Parâmetros como duração típica de áudio, número de turnos, extensão de texto, quantidade de language chunks e grau de scaffolding são calibrações Alumni. Podem ser relacionados ao nível, mas não devem ser apresentados como exigências do CEFR.

### 1.2 Ordem de carregamento e resolução de conflitos

> **CEFR-LVL-000 — Aplicação anterior à produção.** O A04 deve ser carregado, lido e aplicado antes do Documento 00 e dos demais documentos em toda geração, revisão ou auditoria que utilize o pacote normativo. Sua precedência sobre os demais documentos é temática e se restringe a nível, descritores, faixas de transição, atividades e competências comunicativas e calibração linguístico-comunicativa. Ele não funciona como validação tardia de uma produção já construída: deve orientar o planejamento e a geração desde a primeira decisão.

| Ordem | Ação do gerador | Regra de decisão |
| :-: | :-: | :-: |
| 1 | Carregar o A04. | Fixar a régua CEFR e seus limites de autoridade antes de interpretar o pacote. |
| 2 | Carregar o perfil, as evidências e os documentos normativos aplicáveis. | Ler referências ao CEFR à luz do A04; preservar nos demais documentos suas regras pedagógicas, produtivas e técnicas. |
| 3 | Classificar possíveis divergências. | Se a divergência tratar de nível ou calibração CEFR, aplicar o A04 e desconsiderar a formulação conflitante apenas nesse domínio; registrar o conflito para harmonização. |
| 4 | Planejar e gerar o material. | Produzir já com a faixa e a demanda calibradas; não gerar primeiro para somente depois corrigir pelo A04. |
| 5 | Executar a validação final. | Confirmar a aplicação da régua previamente definida; a validação é controle, não primeira aplicação. |

A ordem material dos arquivos em uma pasta, prompt ou lote não altera a precedência temática do A04.

Uma formulação posterior não substitui o A04 apenas por ter sido lida depois. A substituição exige atualização normativa explícita deste adendo ou ato que declare formalmente sua revisão.

Em conflito restrito ao CEFR, não descartar o documento inteiro: desconsiderar somente a regra incompatível e preservar suas demais competências normativas.

Não combinar regras divergentes por média, conciliação automática ou escolha da formulação mais recente.

### 1.3 Precedência das fontes

| Ordem | Fonte | Uso autorizado |
| :-: | :-: | :-: |
| 1 | CEFR Companion Volume (2020) | Referência principal para níveis, perfis, descritores, atividades, estratégias e competências. |
| 2 | CEFR (2001) | Fundamentação conceitual original quando o Companion Volume remete ao framework ou exige aprofundamento. |
| 3 | Council of Europe — Reference Level Descriptions (RLD) | Enquadramento oficial da relação entre níveis CEFR e especificação linguística por idioma. |
| 4 | Core Inventory for General English — Posters 2018 | Referência operacional para plausibilidade de funções, gramática, discurso e vocabulário do inglês, entre A1 e C1. |
| 5 | English Profile | Consulta complementar para aprofundar ou conferir usos lexicais e gramaticais específicos do inglês; não é fonte-base obrigatória. |
| 6 | Diretrizes Alumni | Operacionalização local, sem atribuir ao CEFR parâmetros institucionais. |

Base: CEFR Companion Volume, §§2.6–2.9, capítulos 3 e 5; CEFR 2001, capítulos 3–5; Council of Europe RLD; Core Inventory A1–C1; English Profile como consulta complementar.

### 1.4 Códigos de proveniência

| Código | Classe | Exemplo de uso |
| :-: | :-: | :-: |
| CEFR-LVL | Critério de nível | Consolidação, transição, perfil e suficiência de evidência. |
| CEFR-CLA | Communicative Language Activity | Recepção, produção, interação, mediação e estratégias. |
| CEFR-CLC | Communicative Language Competence | Competências linguística, sociolinguística e pragmática. |
| ENG-CORE | Repertório específico do inglês | Funções, gramática, discurso e vocabulário plausíveis. |
| ALU-CAL | Calibração operacional Alumni | Parâmetros de produção e apoio que não constituem critério CEFR. |

> **Safeguard de proveniência.** Uma regra ALU-CAL não pode ser justificada como se fosse exigência CEFR. O auditor deve reprovar tanto a calibração inadequada quanto a atribuição incorreta da fonte.

### 1.5 Correspondência institucional

| Nome Alumni | Referência CEFR | Interpretação normativa |
| :-: | :-: | :-: |
| A0 / Real Beginner | Pre-A1 | Faixa abaixo de A1; não significa ausência total de inglês. |
| A1 | A1 | Criterion level A1. |
| A1+ | A1 → A2 | Nomenclatura institucional; não é plus level oficial a ser inventado. |
| A2 / A2+ | A2 / A2+ | A2+ corresponde ao plus level representado nas escalas CEFR. |
| B1 / B1+ | B1 / B1+ | B1+ corresponde ao plus level representado nas escalas CEFR. |
| B2 / B2+ | B2 / B2+ | B2+ corresponde ao plus level representado nas escalas CEFR. |
| C1 | C1 | Criterion level C1. |
| C1+ | C1 → C2 | Nomenclatura institucional; C2 é referência superior, não nível presumido. |

Base: Companion Volume, §2.6 e Appendix 1. A1+ e C1+ são convenções Alumni explicitamente delimitadas neste adendo.

## 2. Critérios para declarar o nível do aluno

### 2.1 Princípio de evidência

> **CEFR-LVL-001 — Declaração sustentada.** A atribuição de faixa não pode decorrer de impressão global, domínio isolado de uma estrutura, tempo de estudo, duração da produção ou média aritmética entre habilidades. Deve resultar de desempenho em atividades comunicativas pertinentes e da qualidade desse desempenho segundo as competências aplicáveis.

A faixa é atribuída separadamente às habilidades ou atividades para as quais existe evidência suficiente. Um rótulo geral só pode resumir o perfil; não apaga assimetrias. O perfil deve preservar diferenças relevantes entre, por exemplo, compreensão oral, leitura, produção oral e interação.

### 2.2 Unidade mínima de decisão

| Elemento | Pergunta de decisão | Registro mínimo |
| :-: | :-: | :-: |
| Atividade | O que o aluno conseguiu fazer comunicativamente? | Ação, propósito, interlocutor, produto e resultado. |
| Condições | Em que condições conseguiu? | Preparação, repetição, apoio, velocidade, familiaridade, colaboração e pressão. |
| Descritor | Qual descritor pertinente é sustentado? | Escala, faixa e evidência que corresponde ao descritor. |
| Qualidade | Como realizou? | Range, accuracy, fluency, interaction, coherence e phonological control, quando pertinentes. |
| Consistência | A capacidade reaparece? | Evidência recorrente ou convergente; exceções e fatores contextuais. |

### 2.3 Suficiência e recorrência

- Uma ocorrência isolada não consolida uma faixa por habilidade.
- Evidências diferentes podem convergir para a mesma capacidade; não precisam repetir exatamente a mesma tarefa.
- Uma ocorrência acima da faixa predominante é registrada como característica emergente.
- Uma ocorrência abaixo não reduz automaticamente a faixa quando houver fatores contextuais ou desempenho predominantemente mais alto.
- Ausência de oportunidade de demonstrar uma capacidade deve ser registrada como não avaliada ou evidência insuficiente, nunca como incapacidade.

### 2.4 Regra de atribuição

> **CEFR-LVL-002 — Faixa sustentada.** Atribuir a faixa mais alta cujos descritores essenciais, entre os pertinentes ao perfil e às evidências disponíveis, sejam demonstrados com consistência e autonomia suficientes. Características do nível seguinte que sejam parciais, dependentes de apoio ou inconsistentes permanecem emergentes.

| Status | Significado | Efeito |
| :-: | :-: | :-: |
| Sustentado | Evidência recorrente/convergente e autonomia compatível. | Pode fundamentar a faixa atribuída. |
| Emergente | Característica do nível seguinte aparece, mas ainda não fecha o critério. | Informa objetivo e calibragem; não promove sozinha. |
| Não avaliado | Não houve oportunidade adequada de observar. | Não autoriza inferência positiva nem negativa. |
| Evidência insuficiente | Amostra inadequada, ambígua ou abaixo do necessário para decidir. | Exige nova evidência pertinente. |

### 2.5 Faixas "+"

O sinal "+" indica competência forte e suficientemente consolidada no nível nominal, com emergência recorrente de características do nível seguinte, mas evidência ainda insuficiente para atribuir o próximo criterion level.

- Não resulta de percentual, média aritmética ou soma de itens.
- Não resulta da presença isolada de uma estrutura ou de um desempenho excepcional.
- A2+, B1+ e B2+ correspondem aos plus levels explicitamente representados nas escalas CEFR.
- A1+ e C1+ são nomenclaturas Alumni: A1 em transição para A2 e C1 em transição para C2.
- Não se criam descritores oficiais A1+ ou C1+; a decisão cruza consolidação do nível atual com emergência do nível seguinte.

Base: Companion Volume, §2.6 e Appendix 1: o plus level representa competência forte no nível, ainda aquém do mínimo do próximo criterion level.

### 2.6 A0 / Pre-A1

> **CEFR-LVL-003 — Interpretação de Pre-A1.** A0 / Real Beginner utiliza Pre-A1 como referência de calibração. Pre-A1 não é "zero inglês": representa uma faixa abaixo de A1 em que o aprendiz ainda não adquiriu a capacidade generativa característica de A1 e depende predominantemente de repertório familiar, palavras e expressões formulaicas, enunciados muito curtos, preparação, apoio contextual e colaboração do interlocutor.

- Usar descritores Pre-A1 existentes nas escalas específicas dos capítulos 3 e 5 do Companion Volume.
- Não criar uma linha Pre-A1 no Appendix 3, que começa em A1.
- Quando uma escala trouxer "No descriptors available", isso não significa incapacidade, proibição ou impossibilidade.
- Não simplificar automaticamente um descritor A1 para inventar um descritor oficial Pre-A1.
- Se houver evidência suficiente de que o desempenho ainda não sustenta os descritores Pre-A1 disponíveis, registrar "abaixo de Pre-A1 na escala observada", sem criar uma nova faixa CEFR. Se a amostra não permitir decisão, registrar "evidência insuficiente".
- O Core Inventory A1 é horizonte de desenvolvimento, não repertório presumido de Pre-A1.

Base: Companion Volume, §2.6, capítulos 3 e 5 e Appendix 6; Appendix 1 para a caracterização de A1 como o nível mais baixo de uso generativo.

Fronteira de governança institucional: regras sobre quando um nível institucional pode ser formalmente revisto — por exemplo, ciclo, checkpoint, aluno vigente ou validação docente — pertencem aos documentos responsáveis do pacote. Quando uma revisão for autorizada por essas regras, a atribuição da faixa deve aplicar os critérios deste A04.

## 3. Communicative Language Activities

O nivelamento deve selecionar somente escalas pertinentes às necessidades, aos domínios de uso e às evidências disponíveis. Não é obrigatório obter evidência de todas as escalas do Companion Volume. As sínteses abaixo orientam a busca por evidência; não substituem os descritores integrais das escalas selecionadas.

### 3.1 Modos comunicativos

| Modo | O que observar | Escalas possíveis |
| :-: | :-: | :-: |
| Recepção | Construção de sentido a partir de input oral, escrito ou audiovisual. | Overall oral comprehension; understanding conversation; announcements; media; overall reading; correspondence; orientation; information and argument. |
| Produção | Criação de discurso oral ou escrito para um propósito e público. | Overall oral production; sustained monologue; public announcements; presentations; overall written production; reports/essays. |
| Interação | Co-construção, turnos, respostas contingentes, negociação e reparo. | Overall oral interaction; conversation; discussion; goal-oriented cooperation; information exchange; interviewing; written/online interaction. |
| Mediação | Criação de acesso, colaboração e construção de sentido entre pessoas, textos ou conceitos. | Mediating a text; mediating concepts; mediating communication, quando pertinentes ao perfil. |

Base: Companion Volume, capítulo 3.

### 3.2 Síntese operacional por faixa

| Faixa | Recepção | Produção e interação |
| :-: | :-: | :-: |
| A0 / Pre-A1 | Reconhece palavras, sinais e expressões muito familiares em condições muito claras, lentas e apoiadas; usa pistas visuais e contexto. | Transmite dados pessoais e intenções muito básicos com palavras/expressões isoladas; reconhece saudações e participa com forte apoio, repetição e colaboração. |
| A1 | Compreende linguagem muito simples, concreta e familiar quando apresentada devagar, com clareza e possibilidade de apoio. | Produz enunciados simples sobre si e necessidades imediatas; interage de forma básica se o interlocutor repetir, reformular e colaborar. |
| A2 | Compreende mensagens e textos curtos sobre necessidades imediatas, rotinas e tópicos familiares, com organização clara. | Descreve aspectos cotidianos em sequência simples e realiza trocas rotineiras diretas, embora nem sempre sustente a conversa sozinho. |
| B1 | Compreende os pontos principais de discurso claro e textos factuais sobre assuntos familiares, profissionais ou de interesse; acompanha sequência e argumento explícitos. | Produz discurso conectado sobre temas familiares; relata, explica brevemente e dá razões; entra e se mantém em conversas pertinentes, apesar de pausas e reparos visíveis. |
| B2 | Compreende ideias principais, detalhes relevantes e linhas de argumento em discurso/textos complexos dentro e além de sua área, com alguma inferência. | Interage com fluência e espontaneidade suficientes; desenvolve posições, sustenta discussão e produz apresentações/explicações claras e detalhadas. |
| C1 | Compreende discurso e textos longos e exigentes, inclusive relações implícitas, variedade de organização e linguagem especializada quando pertinente. | Usa a língua com flexibilidade e eficácia; estrutura produção complexa e detalhada, gere turnos e formulações com pouca busca aparente e adapta registro e precisão. |
| C2 — referência | Processa com facilidade ampla variedade de discurso complexo, rápido ou denso, inclusive nuances e implicações. | Produz e interage com controle amplo, precisão fina, flexibilidade e capacidade de reformular sem perda perceptível. Serve como referência superior para C1+. |

Base: Síntese operacional de escalas do Companion Volume, capítulo 3, e dos salient features do Appendix 1. Não constitui transcrição integral de descritores.

### 3.3 Seleção das escalas

> **CEFR-CLA-001 — Pertinência.** Selecionar escalas pela situação de uso e pela evidência que a tarefa pode produzir. A prioridade profissional "reuniões", por exemplo, pode exigir Conversation, Formal discussion, Goal-oriented cooperation, Information exchange, Asking for clarification e, quando aplicável, Sustained monologue. Outra necessidade exige outra combinação.

- Não declarar uma escala como avaliada se a tarefa não oferece oportunidade real de demonstrá-la.
- Uma atividade pode produzir evidência para mais de uma escala, desde que a relação seja explícita.
- A mediação só é avaliada quando existe uma operação real de tornar texto, conceito ou comunicação acessível; resumir por si só não basta se não houver propósito mediador.
- O domínio pessoal, público, profissional ou educacional calibra o contexto, mas não funciona como nível.

## 4. Communicative Language Competences

As atividades comunicativas mostram o que o aluno consegue realizar. As competências qualificam como ele realiza. Nenhuma dimensão isolada — especialmente complexidade gramatical — determina o nível.

### 4.1 Dimensões pertinentes

| Competência | Dimensões de observação | Safeguard |
| :-: | :-: | :-: |
| Linguística | General linguistic range; vocabulary range/control; grammatical accuracy; phonological control; orthographic control, quando pertinente. | Estrutura rara ou complexa não eleva a faixa sem significado, uso, controle e autonomia. |
| Sociolinguística | Adequação a relação, situação, registro, convenções e marcas socioculturais relevantes. | Formalidade superficial não equivale a adequação nem a nível. |
| Pragmática | Flexibility; turntaking; thematic development; coherence/cohesion; propositional precision; fluency. | Extensão e velocidade, isoladamente, não provam desenvolvimento discursivo ou fluência. |

Base: Companion Volume, capítulo 5.

### 4.2 Matriz qualitativa de spoken performance

Para A1–C2, o Appendix 3 pode funcionar como síntese qualitativa, sempre em conjunto com as escalas de atividade pertinentes. Para A0/Pre-A1, o Appendix 3 não oferece uma linha própria: a análise qualitativa deve resultar dos descritores Pre-A1 disponíveis nas escalas pertinentes dos capítulos 3 e 5. Não extrapolar retrospectivamente os descritores A1 nem construir uma linha Pre-A1 artificial.

| Faixa | Range e accuracy | Fluency, interaction e coherence |
| :-: | :-: | :-: |
| A1 | Repertório básico para necessidades concretas; controle limitado de poucos padrões memorizados. | Produção fragmentada, com pausas; interação depende de repetição/reformulação; conexão elementar. |
| A2 | Repertório simples para situações previsíveis; controle razoável de padrões frequentes, com erros sistemáticos. | Consegue manter trocas curtas e ligar grupos simples, ainda com hesitação e necessidade de ajuda. |
| B1 | Range suficiente para tópicos familiares; accuracy razoável em repertório frequente, embora os erros sejam perceptíveis. | Mantém discurso e interação, com planejamento e reparo visíveis; conexão predominantemente linear. |
| B2 | Range suficiente para formular com clareza e variar expressão; bom controle, com erros ocasionais não sistemáticos. | Ritmo relativamente regular, turnos e respostas eficazes; discurso claro e coerente com conectores variados. |
| C1 | Amplo repertório e seleção precisa; alto controle consistente, com erros raros e prontamente corrigidos. | Fluência espontânea, gestão habilidosa de interação e discurso bem estruturado, coeso e flexível. |
| C2 — referência | Amplitude, precisão e controle muito altos, incluindo nuances finas. | Fluxo natural, interação sofisticada e organização plenamente coerente, com reformulação imperceptível. |

Base: Companion Volume, Appendix 3 (A1–C2) e escalas pertinentes do capítulo 5. Síntese operacional, não reprodução integral.

### 4.3 Regras de interpretação

- Aplicar somente dimensões pertinentes à atividade e ao produto observado.
- Separar falta de conhecimento linguístico de efeitos de pressão, tema, áudio, familiaridade, acessibilidade ou desenho da tarefa.
- Grammatical accuracy descreve controle em uso; não pode ser inferida exclusivamente pela complexidade da estrutura utilizada.
- Fluency não é velocidade máxima: considera manutenção do fluxo, pausas, planejamento, reparo e efeito comunicativo.
- Phonological control considera inteligibilidade e controle de recursos sonoros pertinentes; sotaque nativo não é critério.
- Interaction requer resposta contingente, iniciativa, gestão de turnos e/ou colaboração; fala longa diante de outra pessoa não se torna interação automaticamente.
- Coherence deve ser avaliada em relação à extensão e à complexidade esperadas para a tarefa.

## 5. Repertório linguístico do inglês

### 5.1 Função do Core Inventory

> **ENG-CORE-001 — Uso autorizado.** O Core Inventory é referência para verificar se funções, gramática, discurso e vocabulário selecionados são plausíveis para uma faixa do inglês. Não é checklist cumulativa obrigatória, currículo prescritivo nem critério suficiente para atribuir nível a um aluno, input ou tarefa.

A presença de uma estrutura em determinada faixa não fixa o nível. A decisão considera conjuntamente forma, significado, uso, complexidade, autonomia, controle, contexto e demanda comunicativa.

### 5.2 Síntese de progressão A1–C1

| Faixa | Funções e discurso — orientação | Gramática e vocabulário — orientação |
| :-: | :-: | :-: |
| A1 | Contato básico; informação pessoal; perguntas e respostas simples; necessidades imediatas; conexão mínima. | Padrões frequentes de presente/passado simples, perguntas, modais básicos, quantificação e léxico cotidiano concreto. |
| A2 | Rotinas, descrições, convites, pedidos, planos, experiências e trocas diretas; sequências curtas. | Ampliação de tempos e aspectos frequentes, comparações, obrigação/conselho, condicionais iniciais e léxico cotidiano/profissional familiar. |
| B1 | Relatar, explicar, justificar, opinar, planejar e lidar com situações familiares; discurso conectado e marcadores mais variados. | Maior combinação de tempos, voz passiva e discurso reportado em usos pertinentes, modais e condicionais; repertório mais abstrato e profissional. |
| B2 | Argumentar, negociar, desenvolver posição, sintetizar e adaptar comunicação a contextos mais complexos. | Controle e flexibilidade ampliados em estruturas complexas, coesão, registro e collocations; vocabulário menos frequente e mais preciso. |
| C1 | Gerir discurso complexo, nuançar posição, reformular, mediar e ajustar registro com flexibilidade. | Amplo repertório gramatical e lexical, controle de registro, idiomaticidade e precisão; seleção orientada pelo efeito, não por lista de estruturas. |

Base: Core Inventory for General English — Posters 2018 Update, painéis A1–C1. Síntese seletiva; consultar os painéis para exemplos e inventário detalhado.

### 5.3 Limites de cobertura

- A0/Pre-A1: o Core Inventory não oferece uma faixa própria; A1 é horizonte de desenvolvimento, não piso nem requisito presumido.
- C1+: usar descritores C2 do CEFR como referência superior quando o inventário específico de inglês não fornecer cobertura equivalente.
- English Profile pode resolver dúvidas pontuais sobre usos lexicais ou gramaticais; não constitui fonte-base obrigatória deste adendo.
- Exemplos do inventário não devem ser convertidos em listas fechadas nem em proibições de contato com repertório de outra faixa.
- Input pode conter itens acima da faixa quando o processamento exigido, os apoios e o objetivo forem adequados.

### 5.4 Matriz de uso do repertório

| Pergunta | Decisão válida | Atalho proibido |
| :-: | :-: | :-: |
| O item é plausível para a faixa? | Consultar ENG-CORE e o uso específico em contexto. | "Aparece em B2; portanto a atividade é B2." |
| O aluno domina o item? | Verificar uso recorrente, significado, precisão e autonomia. | "Produziu uma passive; portanto é B2." |
| O item pode aparecer no input? | Calibrar densidade, saliência, apoio e operação de compreensão. | Proibir qualquer item acima da faixa nominal. |
| O item é objetivo de produção? | Definir função, condições e qualidade esperada. | Selecionar por cobertura curricular. |

## 6. Critérios para nivelar conteúdo

> **CEFR-LVL-004 — Variáveis distintas.** Nível do aluno, nível do input, nível da tarefa comunicativa e nível da produção esperada são variáveis relacionadas, mas não equivalentes. Uma não pode ser copiada automaticamente para as demais.

### 6.1 Quatro objetos de calibração

| Objeto | O que significa | Como registrar |
| :-: | :-: | :-: |
| Nível do aluno | Faixa sustentada por evidência em atividades e competências pertinentes. | Perfil por habilidade/atividade, emergências e condições. |
| Nível do input | Demanda de processamento do texto, áudio, vídeo ou interação recebida. | Complexidade, densidade, explicitude, organização, velocidade, variedade e apoios. |
| Nível da tarefa | Demanda comunicativa criada pelo propósito, operação, interlocutor e condições. | Ação, decisão, inferência, pressão, colaboração, previsibilidade e autonomia. |
| Nível da produção esperada | Qualidade e alcance necessários no produto para cumprir o objetivo. | Função, extensão pertinente, range, accuracy, fluency, interaction, coherence e controle fonológico, conforme aplicável. |

### 6.2 Calibração de recepção

Para declarar a demanda de uma atividade receptiva, registrar:

- o que deve ser compreendido: gist, informação explícita, detalhe, posição, intenção, implicação ou organização;
- o tipo e a organização do discurso;
- a familiaridade do domínio e do vocabulário;
- velocidade, clareza, variedade, densidade e possibilidade de repetição no áudio;
- extensão, estrutura, densidade e recursos visuais no texto;
- grau de explicitude ou inferência necessário;
- apoios disponíveis e autonomia esperada;
- produto que demonstrará a compreensão.

### 6.3 Calibração de produção e interação

Para declarar a demanda de uma produção, cruzar o que o aluno precisa fazer com a qualidade necessária para fazê-lo. Registrar:

- função e propósito comunicativos;
- interlocutor, relação, registro e consequência;
- grau de preparação, previsibilidade e apoio;
- necessidade de iniciativa, contingência, negociação, reparo ou mediação;
- complexidade conceitual e organizacional;
- range, accuracy, fluency, interaction, coherence e phonological control pertinentes;
- critério observável de conclusão e evidência esperada.

### 6.4 Exemplos de distinção

| Situação | Interpretação correta |
| :-: | :-: |
| Aluno B1 lê texto com alguns itens B2. | O input pode ser adequado se a operação, a densidade e os apoios forem calibrados; o aluno não se torna B2. |
| Aluno B1 realiza tarefa A2. | Pode ser revisão, automatização ou coleta de evidência sob menos apoio; não reduz automaticamente o nível. |
| Aluno A2 realiza tarefa B1 com scaffolding. | Pode constituir desenvolvimento ou evidência emergente; não sustenta B1 sem autonomia e consistência compatíveis. |
| Atividade usa passive voice. | A estrutura isolada não determina faixa; avaliar função, uso, controle, demanda e condições. |
| Áudio tem três minutos. | Duração é parâmetro operacional; não constitui critério CEFR independente. |

### 6.5 Registro obrigatório da calibração

| Campo | Conteúdo |
| :-: | :-: |
| Objeto | Aluno, input, tarefa ou produção esperada. |
| Faixa-alvo | Pre-A1, A1, A2, B1, B2, C1 ou referência C2; "+" somente segundo a regra deste adendo. |
| Escala(s) | CEFR-CLA pertinente(s). |
| Competência(s) | CEFR-CLC pertinente(s). |
| Condições | Apoio, preparação, repetição, familiaridade, pressão e colaboração. |
| Repertório | ENG-CORE pertinente, quando aplicável. |
| Heurísticas | ALU-CAL utilizadas, claramente identificadas como institucionais. |
| Justificativa | Relação entre demanda, evidência, descritores e qualidade esperada. |

## Checklist normativo de aplicação

- A declaração identifica a habilidade ou atividade avaliada, em vez de depender apenas de um rótulo global?
- O A04 foi carregado e aplicado antes da interpretação das referências CEFR dos demais documentos?
- Uma divergência temática foi resolvida pelo A04 antes da geração, sem mistura de regras incompatíveis?
- A tarefa oferece evidência pertinente às escalas selecionadas?
- A decisão se apoia em evidência recorrente ou convergente?
- Condições, apoios e grau de autonomia estão registrados?
- A faixa atribuída é a mais alta cujos descritores essenciais pertinentes estão sustentados?
- Características do nível seguinte estão registradas como emergentes quando ainda não consolidam o próximo criterion level?
- A0/Pre-A1 usa descritores existentes dos capítulos 3 e 5, sem inventar linha no Appendix 3?
- "No descriptors available" foi tratado como ausência de descritor calibrado, não como incapacidade?
- O sinal "+" não decorre de média, percentual ou item isolado?
- Nível do aluno, input, tarefa e produção esperada foram distinguidos?
- Nenhum item gramatical, lexical, funcional, duração ou extensão determinou sozinho o nível?
- O Core Inventory foi usado como referência de plausibilidade, não como checklist obrigatório?
- Heurísticas Alumni estão identificadas como ALU-CAL, sem falsa atribuição ao CEFR?
- O registro preserva assimetrias, emergências, lacunas e evidências insuficientes?

> **Bloqueio.** A produção ou classificação deve ser devolvida para revisão quando: inventar descritor; converter ausência de descritor em incapacidade; usar média entre habilidades; atribuir nível por estrutura isolada; confundir parâmetro Alumni com regra CEFR; ou declarar faixa sem evidência rastreável.

## Matriz mínima para o gerador e o auditor

| Código | Regra bloqueante | Evidência de conformidade |
| :-: | :-: | :-: |
| CEFR-LVL-000 | A04 aplicado antes da interpretação do pacote e da geração. | Log de carregamento e decisões de calibração anteriores à produção. |
| CEFR-LVL-001 | Sem impressão global, média ou atalho estrutural. | Cadeia evidência → escala → descritor → qualidade → decisão. |
| CEFR-LVL-002 | Faixa mais alta sustentada; próximo nível parcial = emergente. | Registro de consolidação e emergência. |
| CEFR-LVL-003 | Pre-A1 sem extrapolação indevida. | Descritores específicos dos capítulos 3/5 e tratamento explícito de ausência. |
| CEFR-LVL-004 | Aluno, input, tarefa e produção não são equivalentes. | Quatro objetos calibrados separadamente. |
| CEFR-CLA-001 | Somente escalas pertinentes e executáveis. | Relação entre necessidade, tarefa e escala. |
| CEFR-CLC-001 | Nenhuma competência isolada determina a faixa. | Qualidade analisada por dimensões pertinentes. |
| ENG-CORE-001 | Core Inventory não é checklist nem critério suficiente. | Uso contextual de forma, significado, função e controle. |
| ALU-CAL-001 | Parâmetros institucionais não são apresentados como CEFR. | Proveniência explícita de heurísticas. |

## Referências normativas e complementares

As sínteses deste adendo são interpretações operacionais selecionadas das fontes indicadas. O texto-fonte prevalece para fins de revisão, correção e atualização normativa deste A04. Durante geração ou auditoria, porém, uma divergência percebida não autoriza o gerador a substituir autonomamente a regra vigente: ela deve ser registrada para revisão normativa do A04.

- [CV 2020] Council of Europe. *Common European Framework of Reference for Languages: Learning, Teaching, Assessment — Companion Volume*. 2020. Seções 2.6–2.9; capítulos 3 e 5; Appendices 1, 3 e 6. <https://rm.coe.int/common-european-framework-of-reference-for-languages-learning-teaching/16809ea0d4>
- [CEFR 2001] Council of Europe. *Common European Framework of Reference for Languages: Learning, Teaching, Assessment*. 2001. Capítulos 3, 4 e 5. <https://www.coe.int/en/web/common-european-framework-reference-languages/cefr-and-its-language-versions>
- [CORE 2018] EAQUALS / British Council. *Core Inventory for General English — Posters 2018 Update*. Painéis A1–C1. <https://www.eaquals.org/resources/the-core-inventory-for-general-english/>
- [RLD] Council of Europe. *Reference Level Descriptions*: relação entre níveis CEFR e conteúdo específico de cada língua. <https://www.coe.int/en/web/common-european-framework-reference-languages/reference-level-descriptions-rlds-developed-so-far>
- [English Profile] English Profile. Fonte complementar opcional para consulta de usos lexicais e gramaticais do inglês. <https://englishprofile.org>

### Nota de implantação

> **Escopo desta entrega.** Este arquivo permanece como adendo autônomo. Nenhum documento do pacote normativo 00–06, A01–A03, Anexo P-A ou Série P foi alterado nesta etapa. Até a harmonização posterior desses documentos, o A04 deve ser fornecido e carregado primeiro; qualquer formulação CEFR conflitante encontrada depois deve ser desconsiderada somente no domínio de nivelamento e calibração, com registro do conflito.

Adendo normativo · versão 1.3 · 03/09/2026
