> **Documento normativo importado do Drive — nao editar aqui.**
> Origem: `04_Planejamento_e_Producao_da_Aula.docx`
> Drive ID: `1IJOoR5sI3DDd79NJ-pl5O4HBmZzHEBPk`
> Modificado no Drive: 2026-08-21
> Reimportar: `python3 scripts/black/docx_to_md.py <arquivo.docx> docs/private-black/04-planejamento-e-producao-da-aula.md`
> A fonte e o .docx. Divergencia entre este arquivo e o Drive se resolve reimportando, nunca editando o .md.

## 04 · PLANEJAMENTO E PRODUÇÃO DA AULA

**Núcleo pedagógico — aulas individuais de inglês, A1–C1, ciclo de 20 aulas** Documento normativo · independente de plataforma, de meio de entrega e de aluno

**Finalidade.** Definir como uma linha do syllabus vira material: a especificação que antecede a produção, o registro único que impede divergência, as regras de cada uma das três camadas, as duas superfícies de leitura, e o que bloqueia a entrega.

### 1. A aula tem três camadas

| Camada | Função | Duração | Estatuto |
|---|---|---|---|
| **Pre-class** | Reduzir barreiras de entrada e preparar operações da aula | 15–20 min | Preparatório; o in-class não depende dele |
| **In-class** | A aula: etapas previstas pelo framework e pela rota aplicável, produção, feedback e retask | 55 min + 5 de margem | Obrigatório |
| **Post-class** | Ampliar contato com a língua depois da aula | Livre | **Opcional e não avaliativo** |

A relação entre as três é assimétrica de propósito. O pre-class **prepara sem resolver**; o in-class **é autônomo**; o post-class **não é continuação obrigatória de nada**.

### 2. O registro único da aula

Este é o contrato de dado do sistema, e a única garantia real contra divergência: **não ter a** **segunda versão**. Pre-class, in-class, post-class e a linha do syllabus bebem do mesmo registro.

| Campo | Conteúdo |
|---|---|
| Identificador | Chave única da aula |
| Número · bloco · framework | Posição no ciclo e na distribuição personalizada |
| Tema | Assunto da aula |
| Situação comunicativa | Quem, com quem, com que objetivo |
| Objetivo comunicativo | O que o aluno conseguirá fazer |
| Vocabulário | Léxico selecionado, com significado contextual |
| Functional language / target language | Linguagem-alvo por função |
| Foco gramatical | Quando aplicável |
| Input principal | Material de partida e sua origem |
| Produto comunicativo | A performance observável que encerra a aula |
| Critérios de sucesso | Dois a quatro comportamentos observáveis |
| Modelo de avaliação e instrumento | Avaliação formal com teste ou Acompanhamento docente; no segundo caso, eventual instrumento de consolidação e sua relação com a aula. Na ausência de escolha explícita no perfil ou syllabus, aplicar Acompanhamento docente. |
| Etapas e distribuição de tempo | As etapas previstas pelo framework e pela rota aplicável, com tempos de referência |
| Conteúdo do pre-class | O que a camada prepara |
| Conteúdo reservado ao in-class | O núcleo protegido |
| Conteúdo do post-class | O que a camada oferece |
| Feedback | O registro pós-aula |
| Status | Não iniciada · em andamento · realizada |
| Relação com as aulas anteriores e seguintes | Continuidade e dependência |

**Regras do registro:**

- Uma alteração no registro **não exige copiar a informação** para várias seções.
- O registro **não é exibido como metadado** em nenhuma superfície.
- O sistema **não cria conteúdo** para preencher campo que a aula não precisa: campo sem objeto se declara vazio, não se simula.
- Se algum material passar a repetir um valor do registro, a duplicata precisa ser **ligada** ao registro e a coincidência precisa ser verificada — duas cópias divergem, é uma questão de tempo.
- Uma fonte única para gabarito e correção é **preferível como solução técnica**, mas não é requisito pedagógico. Representações separadas são permitidas quando necessárias; é obrigatória a ausência de divergência entre correção, answer key, Teacher’s Guide e versão da atividade.

Regra de avaliação. O planejamento consome o modelo vigente do perfil e do syllabus; não cria um modelo próprio. Ausência de escolha explícita significa Acompanhamento docente. Teste formal só aparece quando Avaliação formal com teste estiver registrada.

### 3. A especificação pedagógica vem antes do material

Nenhuma aula é produzida sem esta ficha. Ela é interna e nunca aparece em superfície alguma.

| Campo | Pergunta de controle |
|---|---|
| Necessidade prioritária | Qual necessidade do perfil esta aula atende? |
| Framework | Por que este framework é o mais adequado? |
| **Operação nova** | O que o aluno fará que não repete a aula anterior? |
| Origem da necessidade | Perfil, evidência de aula, evento futuro ou hipótese diagnóstica? |
| Conteúdo recuperado | O que será retomado sem reapresentação extensa? |
| Conteúdo excluído | O que pertence a outro framework ou já está consolidado? |
| Input e output | Nível receptivo do material; nível produtivo esperado |
| Microciclo de descoberta | Sobre o que o aluno formulará hipótese, e onde |
| Produto final | Qual performance observável encerra a aula? |
| Critérios de sucesso | Que comportamentos serão registrados? |
| Relação com a avaliação | Qual dos dois modelos está registrado e como a evidência da aula, o teste formal ou o eventual instrumento de consolidação se relacionam com ele? Se não houver escolha explícita, registrar Acompanhamento docente; a aula não pode criar, preparar ou pressupor teste formal por inferência. |
| Mecânicas | Mecânica + função + operação cognitiva + grau de controle + evidência |
| Retask | Que trecho poderá ser repetido, por quê, e com que mudança esperada? |
| Relação com o ciclo | O que recupera de trás e o que prepara adiante |

**Gate.** A aula não é gerada se a especificação repetir substancialmente outra aula do mesmo bloco. O momento de descobrir isso é aqui, não depois de o material existir.

#### 3.1 Ordem de produção

- Validar a suficiência dos dados de entrada.
- Produzir a especificação pedagógica.
- Aplicar **somente** o framework pertinente.
- Escolher conteúdo, fontes e mecânicas.
- Redigir a arquitetura pedagógica **e só depois** o material final.
- Executar as validações — pedagógica, linguística, factual, técnica.
- Entregar apenas quando as checagens estiverem comprovadas.

### 4. Pre-class

#### 4.1 Função e limite

**Reduzir barreiras de entrada, criar familiaridade com o contexto e preparar as operações que a** **aula exigirá.** O pre-class não substitui explicação, interação, feedback nem prática acompanhada.

Duas autonomias precisam valer ao mesmo tempo:

- **O pre-class roda sem o professor** — nenhuma atividade depende de correção posterior ou de conteúdo inacessível.
- **O in-class roda sem o pre-class** — a retomada inicial pode aproveitar o preparo, mas nunca depender dele.

#### 4.2 A regra estrutural

**Exatamente seis atividades reais, entre 15 e 20 minutos**, contando leitura de instrução, reprodução de mídia, resposta e feedback.

A quantidade é fixa como parâmetro operacional. **Função, ordem, operação e mecânica variam** por framework, nível, aluno e relação com a aula. **Nenhuma posição numérica tem função permanente**: apresentação lexical não mora na atividade 2, consolidação não mora na 3.

#### 4.3 O que conta como atividade real

| Conta | Não conta isoladamente |
|---|---|
| Uma ação com objetivo, instrução, conteúdo, resposta e conclusão observável | Título, transição, ou explicação passiva sem operação |
| Uma operação cognitiva nova, ou reutilização funcional que acrescenta processamento | O mesmo conjunto de perguntas reapresentado em outro formato |
| Um novo uso coerente do conteúdo: inferir, classificar, localizar evidência, comparar, decidir, aplicar | Dividir artificialmente uma atividade em duas para chegar a seis |
|  | Feedback exibido depois de outra tarefa |
|  | A mesma busca factual repetida em áudio e depois em texto |

#### 4.4 O núcleo protegido do in-class

Estas coisas **não acontecem no pre-class**:

- produção oral extensa;
- a discussão ou o role-play principal;
- feedback corretivo personalizado;
- a descoberta decisiva que sustenta a aula;
- o repertório completo de functional language;
- a análise crítica, negociação ou tomada de decisão central;
- a prática livre da estrutura-alvo.

E, transversalmente: **o pre-class não ensina a linguagem que será diagnosticada** na aula.

##### A linha que separa preparar de resolver

A proteção é frequentemente mal lida em Grammar, onde o pre-class **pode** trabalhar observação e o in-class **precisa** diagnosticar. As duas coisas convivem, e a fronteira é esta:

| O pre-class **pode** | O pre-class **não pode** |
|---|---|
| Preparar o aluno para observar a linguagem | Formular a regra em definitivo |
| Noticing preliminar — perceber que há um padrão | Clarificar o sistema por completo |
| Familiarizar com o contexto e com a evidência | Praticar o suficiente para o desempenho inicial deixar de revelar a lacuna |
| Uma síntese curta, provisória, do que foi observado | Substituir a etapa de descoberta da aula |

**O teste é o diagnóstico.** Se, depois do pre-class, a primeira tentativa do aluno na aula já não mostra onde está a dificuldade, o pre-class resolveu o que devia apenas preparar — e a aula perdeu o instrumento com que decide o que ensinar.

Vale igualmente para os outros frameworks: o noticing preliminar é bem-vindo em qualquer um; a **conclusão** pertence à aula.

#### 4.5 Idioma de apoio e quantidade de escuta

Duas regras que dependem do nível e do framework:

| Regra | Norma |
|---|---|
| **Idioma de apoio** | Instrução ao aluno em inglês em todos os níveis. **A1 e A2 admitem apoio complementar em português**, breve e restrito ao necessário para garantir autonomia. B1 a C1 ficam em inglês, salvo necessidade registrada. O apoio nunca substitui o contato com o inglês. |
| **Quantidade de escuta** | **Listening admite até duas escutas** no pre-class, com operações diferentes entre elas. Os demais frameworks: **zero ou uma**. Uma terceira recuperação do mesmo áudio para completar a contagem de seis é proibida. |

Quando o perfil do aluno proíbe apoio em português, **o perfil vence** — restrição de aluno tem precedência sobre diretriz de curso.

#### 4.6 Léxico

Uma ou duas atividades trabalham léxico, e **somente o necessário** — o que bloqueia a compreensão ou a execução. Cada item prioritário recebe significado contextual, exemplo e, quando útil, apoio sonoro, visual, collocation ou contraste. O léxico apresentado é **reutilizado em ao menos uma** **atividade posterior**; caso contrário é lista, não preparação.

Não pré-ensinar palavras que o nível permite inferir com segurança.

#### 4.7 Funções por framework

Estas funções aparecem distribuídas nas seis atividades, combinadas e ordenadas livremente.

| Framework | Funções que devem aparecer |
|---|---|
| **Reading** | Orientação e previsão · preparação lexical · leitura global · leitura focalizada · noticing funcional (opcional) · ponte para a fala |
| **Listening** | Orientação e previsão · preparação lexical · primeira escuta **sem transcrição** · segunda escuta com operação diferente · percepção sonora (opcional) · ponte para a reação |
| **Grammar** | Orientação comunicativa · contexto e léxico de suporte · input contextualizado · **noticing preliminar** · **síntese curta e provisória** do que foi observado · ponte para a tentativa diagnóstica |
| **ESP** | Orientação realista · léxico técnico e situacional · artefato · processamento orientado à tarefa · preview funcional ou microdecisão · ponte para a simulação |

#### 4.8 Extensão do input por nível

Faixas do pre-class. O quadro completo — todos os parâmetros de cada framework em cada nível — está no documento **06**.

| Nível | Reading | Listening |
|---|---|---|
| A1 | 50–100 palavras · 4–6 itens lexicais | 20–45 s · dois falantes claros |
| A2 | 90–160 palavras · 5–7 itens | 30–60 s · problema e resposta identificáveis |
| B1 | 150–260 palavras · 5–8 itens | 45–90 s · justificativas e follow-up |
| B2 | 220–380 palavras · 4–7 itens | 60–120 s · ritmo natural, mitigação, implícito |
| C1 | 280–500 palavras · 3–6 itens não inferíveis | 75–150 s · nuance de tom, reformulação, fala conectada |

**Princípio de progressão.** A complexidade cresce pela profundidade do processamento, menor previsibilidade, menos apoio e mais autonomia — **nunca** pelo aumento do número de atividades, do tamanho das instruções ou das listas lexicais.

#### 4.9 Bloqueios do pre-class

- Seis questionários de compreensão em sequência.
- A mesma localização literal repetida em formatos diferentes.
- Uma terceira recuperação do mesmo conteúdo só para completar a contagem.
- Transcrição antes da primeira escuta.
- A segunda escuta repetindo as perguntas da primeira.
- Começar por nomenclatura e regra abstrata sem contexto comunicativo.
- A sequência fixa contexto → vocabulário → regra → lacuna → lacuna → frase.
- Escolher o artefato antes de definir a tarefa e o resultado (ESP).
- Ensinar terminologia como lista isolada (ESP).
- Miniaturizar em nível inicial uma situação concebida para nível avançado.

#### 4.10 Instrução e feedback

| Elemento | Diretriz |
|---|---|
| Instrução | Um verbo de ação claro, conteúdo identificável e condição de resposta |
| Apoio à instrução | Só o necessário — número de opções, possibilidade de repetir, uso de evidência. Não duplicar a instrução |
| Idioma | Instruções ao aluno em inglês, com complexidade sintática ajustada ao nível e sem infantilizar adultos |
| Feedback | Confirmar e explicar brevemente; em erro, mostrar a pista relevante e permitir nova tentativa quando couber |
| Resposta aberta | Usar quando não exigir correção humana para completar o percurso; oferecer modelo ou critério de autoavaliação |
| Acessibilidade | Não depender apenas de cor; texto alternativo funcional; navegação e contraste legíveis |

#### 4.11 A camada do professor no pre-class

Para cada atividade, o professor dispõe de: resposta esperada · alternativas aceitáveis · rationale breve · transcrição quando houver áudio · pontos que podem gerar dúvida · relação com o in-class quando pedagogicamente necessária.

O professor encontra as respostas **sem precisar executar os exercícios**. O aluno não vê nada disso antes da própria tentativa.

### 5. In-class

A arquitetura está no documento **03**. Aqui ficam as regras de produção que dela decorrem.

#### 5.1 Regras da produção principal

- **Uma** produção principal por aula. As atividades anteriores a alimentam.
- Objeções e mudanças de condição são **escalas da mesma tarefa**, não tarefas novas.
- O feedback é **emergente**: um ponto forte e um ou dois pontos de maior impacto, tirados da formulação real do aluno.
- O **retask repete somente o trecho** que se beneficia do feedback, e é escolhido **depois** do feedback, com o aluno, por critério observável.
- O fechamento é obrigatório e distingue quatro coisas: o que foi realizado, a percepção de confiança, a evidência de aprendizagem e o plano de transferência.

#### 5.2 O quadro de feedback

| Campo | Uso |
|---|---|
| What worked | Uma estratégia, escolha linguística ou efeito comunicativo bem-sucedido |
| Keep developing | O ponto de maior impacto para clareza, precisão ou interação |
| First version | A formulação **realmente produzida** pelo aluno |
| Clearer version | Reformulação coconstruída, preservando a intenção original |
| Effect check | Pergunta curta sobre o que ficou mais claro ou mais eficaz |

**O quadro de condução começa vazio e é preenchido durante a aula.** Nunca vem pré-preenchido com um erro que o aluno ainda não cometeu, e nunca exibe uma produção inteiramente marcada como incorreta. *First version*, *Clearer version* e *Effect check* apoiam a condução e o retask; não se tornam campos adicionais da devolutiva persistente ao aluno.

Se a dificuldade impedir a tarefa: pausar brevemente, apoiar e retomar do ponto necessário. Reiniciar tudo só quando for realmente útil.

#### 5.3 O fechamento registra, não confere

O fechamento **não pressupõe percurso completo**. A formulação importa: *“**reveja o que você* *trabalhou hoje**”* é verdadeira tanto no percurso completo quanto no parcial; *“**marque o que* *cobrimos**”* transforma percurso parcial em sensação de falha.

**Concluir a aula nunca depende** de checklist preenchido, de todas as unidades terem sido percorridas, de todas as respostas estarem preenchidas, nem do feedback estar completo. Concluir não atribui nota nem percentual.

#### 5.4 Escrita do aluno durante a aula

Não há atividade de escrita extensa do aluno durante o in-class. A superfície da aula é conduzida pelo professor; a produção escrita, quando pedida, pertence ao pre-class ou ao post-class.

### 6. Post-class

#### 6.1 Definição

**Um acervo complementar, autêntico, personalizado, opcional e não avaliativo.** Ele amplia o contato com a língua depois da aula — sem funcionar como tarefa de casa, continuação obrigatória ou requisito de progressão.

**Princípio de autonomia.** Não realizar qualquer item **não configura falta, pendência nem** **evidência de baixo desempenho.** Nada de nota, pontuação, prazo, badge, checklist obrigatório, trava de navegação ou confirmação de conclusão.

#### 6.2 O que o post-class não é

- Tarefa obrigatória ou avaliativa.
- Prova de compreensão, retenção ou desempenho.
- Nova sequência de reading ou listening com exercícios.
- Repetição do pre-class ou do in-class.
- Condição para concluir a aula ou liberar conteúdo.
- Fonte de conteúdo essencial para a aula seguinte.
- Atividade que dependa de correção ou acompanhamento obrigatório do professor.

#### 6.3 Os cinco componentes funcionais

O post-class é um **banco de sugestões**, não uma sequência fixa. O que é normativo são os componentes que precisam estar **disponíveis** — não a forma como se organizam.

| Componente | Função | Natureza |
|---|---|---|
| **Speaking** | Uma proposta de produção oral ligada ao objetivo comunicativo | Prática opcional |
| **Writing** | Uma proposta de produção escrita breve e funcional | Prática opcional |
| **Reading** | Curadoria de leituras externas autênticas | Acervo; sem exercício |
| **Listening / watching** | Curadoria de áudio ou vídeo externo autêntico | Acervo; sem exercício |
| **Apoio linguístico** | Referência ao foco trabalhado, com fonte externa confiável | Consulta; sem exercício |

**Uma contextualização ou retomada da aula pode ser incluída quando acrescentar valor** — situar o acervo, lembrar o foco. Ela **não é componente obrigatório**: uma aula cujo post-class dispensa recapitulação não está incompleta.

**A organização pertence ao meio.** Blocos, páginas, cartões, seções, ordem de apresentação — nada disso é regra pedagógica. O que o núcleo exige é que os cinco componentes estejam disponíveis, que o aluno não precise segui-los em ordem nem consumir tudo, e que **prática opcional** fique distinguível de **recurso para explorar**.

#### 6.4 Regras de conteúdo

**Retomada da aula, quando houver** — curta e autossuficiente: tema, objetivo comunicativo em linguagem acessível, functional language ou estrutura central, vocabulário essencial, dois ou três exemplos contextualizados. **Sem quiz, sem perguntas de revisão, sem resumo extenso.**

**Speaking e writing** — cada um traz contexto completo (compreensível sem acesso à aula), propósito, destinatário quando aplicável, dois a quatro pontos de orientação, apoio linguístico que **não é roteiro pronto**, e extensão sugerida por nível. A opcionalidade é explícita na formulação.

**Independência.** As duas propostas podem citar o acervo como inspiração, mas **nunca podem** **exigir** que o aluno leia, assista ou ouça algo para conseguir realizá-las.

**Reading e listening / watching** — material **externo, real e originalmente publicado em** **inglês**. O sistema **não fabrica** texto, áudio ou vídeo e os apresenta como autênticos. E o acervo **não leva atividade**: nada de perguntas, lacunas, verdadeiro ou falso, busca de vocabulário, resumo, anotação ou qualquer evidência de consumo.

**Language Reference** — síntese interna curta, fiel ao foco trabalhado, mais uma ou mais referências externas confiáveis que levem à **página específica**, nunca à página inicial. Não vira aula gramatical extensa nem contém exercício obrigatório.

#### 6.5 Extensão por nível

| Nível | Speaking | Writing | Curadoria prioritária |
|---|---|---|---|
| A1 | 30–45 s · situação concreta · 3–5 apoios | 3–5 frases · modelo parcial | Textos muito curtos, vídeos breves e visuais, fala clara |
| A2 | 45–60 s · relato ou escolha simples | 5–7 frases · frames e conectores | Textos curtos e segmentados, situações familiares |
| B1 | 1–1,5 min · opinião, explicação, narrativa | 60–90 palavras · apoio por função | Artigos acessíveis, entrevistas curtas, podcasts segmentados |
| B2 | 1,5–2 min · posição justificada, recomendação | 80–130 palavras · apoio seletivo | Notícias, análises, perspectivas divergentes |
| C1 | 2–3 min · nuance, síntese, argumentação | 100–160 palavras · precisão, tom, organização | Opinião, entrevistas longas com recorte, conteúdo especializado |

#### 6.6 Curadoria: as duas camadas do metadado

Esta distinção evita um conflito recorrente. **Verificar não é exibir.**

| Camada | O que carrega |
|---|---|
| **Curadoria (interna, obrigatória)** | Título original · fonte, autor ou canal · link direto verificado · gênero e formato · duração total · trecho recomendado com minutagem · relação com a aula · nível estimado · tempo de leitura · data · legenda ou transcrição · condição de acesso · data da verificação |
| **Exibição (mínima)** | Título · fonte ou canal · link direto · descrição breve · duração, quando útil |

O metadado de curadoria **prova que o recurso foi verificado** e alimenta o controle de repetição. Ele **não vira etiqueta** para o aluno: nível estimado, tempo de leitura, data, sotaque e detalhe de legenda ficam fora da superfície. Nunca exibir validação, auditoria ou selo de conferência.

#### 6.7 Verificação de fontes

- Abrir o link e confirmar que o recurso existe.
- Conferir que título e fonte correspondem ao item descrito.
- Identificar restrição de acesso, região, cadastro ou remoção.
- Confirmar duração e a minutagem do trecho recomendado.
- Confirmar se legenda ou transcrição realmente existem.
- **Não inventar** sotaque, nível, data, duração ou qualquer metadado não verificável.

**Hierarquia:** priorizar a publicação original — veículo, canal, organização, autor. Usar agregador apenas quando for o local oficial. Evitar cópias, reuploads, páginas espelho, resultados de busca, links encurtados e páginas iniciais genéricas.

**Falha bloqueante.** Recurso que não pode ser verificado **não entra**. Substitui-se por outro validado; nunca se preenche campo por inferência apresentada como fato. **Conseguir abrir é** **condição para incluir, não razão para incluir** — e impossibilidade de conferir não é o mesmo que link quebrado.

#### 6.8 Não repetição

Não repetir a mesma mídia no ciclo · evitar o mesmo veículo ou canal em aulas consecutivas · variar gêneros, vozes, registros e variedades do inglês · não repetir a situação comunicativa do in-class apenas trocando nomes · não duplicar material do pre-class · registrar cada recurso no histórico do ciclo.

#### 6.9 Tom

| Adequado | Evitar |
|---|---|
| Explore these resources if you would like to learn more about today’s topic. | Read the article and answer the questions. |
| If you would like to practice speaking, record a short response. | Record your answer to complete the lesson. |
| Choose anything that interests you and return whenever you like. | Complete all resources before the next class. |
| This article offers another perspective on the topic. | Find five new words and submit a summary. |

Nenhum controle usa verbo de obrigação ou de conclusão.

### 7. As duas superfícies

Todo material tem dois leitores com direitos diferentes — e uma terceira camada que nenhum dos dois lê. A separação vale em qualquer meio.

#### 7.1 O que cada superfície contém

|  | Aluno | Professor |
|---|---|---|
| **Vê** | Planejamento (só o bloco liberado) · Pre-class · Feedback compartilhável · Post-class | Perfil · Planejamento completo · Pre-class com gabarito · In-class · Post-class · Estado pedagógico do ciclo |
| **Nunca vê** | In-class · notas do professor · gabaritos reservados · hipóteses diagnósticas · estado pedagógico interno · instrumentos de checkpoint · regras de geração · justificativas de framework · controles administrativos | — |

#### 7.1.1 As três camadas, e o que cada uma admite

| Camada | Pode conter | Não deve conter |
|---|---|---|
| **Superfície do aluno** | Contexto, tarefa, input, opções, apoio, modelos, status de conteúdo extra | Código interno, hipótese diagnóstica, cronômetro sem função, rubrica oculta, lógica de geração |
| **Material de condução do professor** | Finalidade, condução, apoio condicional, resposta esperada, evidência a observar, critério de transição | Ordem dramatizada, proibição rígida, conclusão diagnóstica antecipada, contagem arbitrária |
| **Registro interno da aula** | Função, evidência, mecânica, grau de controle, tempo, status, relação com a tarefa e com o ciclo | Texto antigo que contradiga o material produzido; causa não sustentada por evidência |

O registro interno é a terceira camada: alimenta as outras duas e **não é exibido a ninguém**. Quando ele diverge do material, é o material que está certo e o registro que envelheceu — ou o inverso; o que não pode é a divergência sobreviver.

#### 7.2 O feedback que chega ao aluno

O registro pós-aula do professor tem doze campos: data de realização · status · desempenho observado · realização concreta · ponto prioritário de desenvolvimento · linguagem introduzida ou retomada · linguagem ainda apoiada · dificuldade ou necessidade emergente · apoio utilizado · resultado do retask · implicação para a aula seguinte · **observação compartilhável**.

O registro interno pode conter todas as evidências e decisões pedagógicas necessárias ao acompanhamento. **Somente dois campos são compartilhados com o aluno: What worked e Keep** **developing.** Linguagem a retomar e próximo foco permanecem incorporados ao registro interno ou são sintetizados dentro desses dois campos, sem gerar campos adicionais na superfície do aluno. Nunca chegam ao aluno: evidência diagnóstica interna, hipótese sobre causa de dificuldade ou decisão sobre reconfiguração do syllabus.

#### 7.3 O que nenhuma superfície contém

- Diretriz de produção, metadado do sistema, auditoria, histórico de revisão.
- Justificativa editorial ou explicação do desenho da atividade.
- Explicação sobre o framework, sobre a quantidade de atividades ou sobre a distribuição de tempo.
- Instrução dirigida a revisor; comentário sobre alterações anteriores.
- Metalinguagem que anuncie o que será encontrado ou desenvolvido depois.
- Rubrica oculta, código interno, timer sem função.

**Comentário interno documenta o estado vigente, nunca o histórico da revisão.** Sem “a versão anterior fazia X”, sem “o feedback N pediu”. O teste: se a frase deixa de fazer sentido quando o histórico é esquecido, ela é histórico — e histórico desorienta quem for alterar o material depois.

### 8. O material de condução do professor

São **duas peças**, e confundi-las é o erro que faz uma delas não existir:

| Peça | O que é | Alcance |
|---|---|---|
| **Teacher’s Guide** | A **entrega pedagógica completa** da aula: identidade, objetivos, preparação, procedimento estágio a estágio, foco linguístico, dificuldades previstas, evidência a registrar e gabarito | A aula inteira |
| **Teacher’s Note** | A orientação pontual de uma atividade: o que fazer ali, o que esperar, o que observar | Uma atividade |

**O guia é obrigatório e as notas não o substituem.** As notas locais acompanham cada atividade por conveniência de condução; o guia é o documento que permite a um professor **preparar e** **conduzir a aula inteira** — inclusive um professor que não a produziu. Uma aula entregue só com notas locais está incompleta.

O guia é escrito **em inglês** e é **independente do meio de entrega**. Como ele é apresentado — documento, caderno, painel, ficha — é decisão da plataforma, não deste núcleo.

#### 8.1 A composição do Teacher’s Guide

| Campo | Conteúdo |
|---|---|
| **Lesson identity** | Número, bloco, framework, nível, tema e modelo de avaliação vigente |
| **Goals** | O objetivo comunicativo e os objetivos específicos da aula |
| **Communicative product** | A performance observável que encerra a aula |
| **Success criteria** | Dois a quatro comportamentos observáveis |
| **Teacher preparation** | O que precisa estar pronto, lido, testado ou impresso antes da aula |
| **Lesson overview** | A aula em uma tabela: as etapas previstas, sua função e seu tempo de referência |
| **Stage-by-stage procedure** | O detalhamento de cada etapa — ver §8.2 |
| **Language focus** | Functional language, vocabulário e, quando houver, o foco estrutural |
| **Anticipated difficulties** | O que provavelmente será difícil, e por quê |
| **Scaffolding and challenge** | O apoio disponível se a dificuldade aparecer; a extensão se não aparecer |
| **Feedback and retask** | Como o feedback será construído e que trecho é candidato a retask |
| **Evidence to record** | O que esta aula precisa produzir para o acompanhamento do ciclo e, quando aplicável, para o teste formal ou instrumento de consolidação |
| **Pre/post-class connection** | O que o pre-class preparou e o que o post-class oferece |
| **Answer key / possible answers** | Gabarito e respostas aceitáveis, quando a atividade os tiver |

#### 8.2 O procedimento, estágio a estágio

Cada etapa prevista recebe:

| Campo | Conteúdo |
|---|---|
| **Goal** | A finalidade da etapa, começando por infinitivo |
| **Interaction** | Quem fala com quem, e em que arranjo |
| **Steps** | A sequência de condução |
| **Exact prompt** | A formulação literal, quando a precisão da instrução importar |
| **Expected / possible answers** | A resposta esperada e as alternativas aceitáveis |
| **Conditional support** | O apoio a oferecer **se** a dificuldade prevista ocorrer |
| **Challenge** | O que propor se o aluno resolver antes do previsto |
| **Monitoring** | O que observar enquanto o aluno trabalha |
| **Evidence to record** | O que desta etapa entra no registro do ciclo |
| **Transition** | O critério para avançar, e como a passagem é feita |

**Conditional support e Challenge são um par.** Um guia que só prevê a dificuldade deixa o professor sem resposta quando o aluno vai bem — e é aí que a aula perde a etapa mais produtiva.

#### 8.3 Anatomia da nota local

Toda nota traz, na ordem, e **em inglês**:

| Campo | Conteúdo |
|---|---|
| **Goal** | A finalidade da atividade, começando por infinitivo |
| **Run it** | A sequência de condução |
| **Expected** | A resposta ou as respostas possíveis |
| **If needed** | Apoio condicional |
| **Watch for** | A evidência a observar |
| **Move on when** | O critério para avançar |
| **Optional** | Atividade complementar da mesma etapa, quando houver |

Rótulos terminam em dois-pontos. O título da nota não leva ponto final. Grafia americana; decimal com ponto.

#### 8.4 O que a nota não carrega

- Justificativa editorial ou explicação de decisão de desenho — isso vive no registro de revisão.
- Histórico de feedback ou comentário sobre revisões.
- Frases prontas de transição; roteiro extenso de fala do professor.
- Instrução para ler integralmente o material em voz alta.
- Teoria que não ajuda na condução.
- Conclusão diagnóstica antecipada.
- Conteúdo de **outra** atividade.

#### 8.5 Três regras que evitam erro de conteúdo

- **Antes de escrever a nota, ler o gabarito que a atividade já tem.** Nota que contradiz o próprio gabarito é o defeito mais comum e o menos visível.
- A atividade complementar indicada na nota **é opcional**, roda só se houver tempo ou necessidade observada, e **nunca substitui** a função essencial que ela apenas complementa.
- **A nota conduz a atividade que está na sua unidade.** Quando uma atividade muda de lugar, a orientação dela muda junto.

#### 8.6 Comentário de atividade ≠ nota do professor

O comentário que o aluno lê depois de responder é **feedback da atividade**: fica na superfície do aluno, em inglês, e não migra para o material do professor.

### 9. Tom e linguagem

| Para o aluno | Para o professor |
|---|---|
| Adulto, direto, claro, respeitoso, orientado à ação | Operacional, claro, escaneável |
| Desafiador sem linguagem ameaçadora | Centrado em objetivo, condução, apoio e evidência |
| Apoio disponível sem infantilização | Distingue apoio condicional de procedimento obrigatório |
| Cenários realistas, declarados fictícios quando inventados | Aceita resposta plausível e registra evidência |
| Sem explicar a engenharia da atividade, sem antecipar respostas, sem hipótese sobre o desempenho | Sem frase de transição decorativa, sem justificativa editorial, sem metalinguagem |

#### 9.1 A regra da instrução

**Toda instrução indica a ação, o objeto da ação e o resultado esperado.**

| Adequado | Evitar |
|---|---|
| Listen and identify why the speakers are meeting. | This listening prepares you for the type of interaction you will work with in class. |
| Match each role to its responsibility. | The same words, a different case. |
| Choose the meaning that best fits each expression. | You will meet that use in class. |

#### 9.2 Tom probabilístico

Quando o efeito não é universal, a formulação é condicional. Impacto verbal nunca substitui precisão pedagógica.

| Evitar | Preferir |
|---|---|
| Não ajude. Deixe o silêncio existir. | Convide a tentativa; ofereça apoio focalizado se a dificuldade impedir a continuidade. |
| Use uma holding phrase toda vez. | Use a expressão quando ela ajudar a organizar a resposta ou manter o turno. |
| Você não precisa de mais palavras. | Estas expressões podem ajudar nesta parte da tarefa. |
| Este erro causa X. | Esta formulação pode levar o interlocutor a interpretar X. |

#### 9.3 O verbo promete comportamento

O rótulo de um controle descreve exatamente o que ele faz. Um controle que apenas **revela** comentários não pode prometer que **corrige** — *“**veja os comentários**”*, nunca *“**corrija e veja os* *comentários**”*. O aluno lê o verbo como contrato.

#### 9.4 Não explicar a atividade, e não tranquilizar de antemão

Duas formas do mesmo excesso. A primeira é conhecida: o material não explica ao aluno por que a atividade foi desenhada assim. A segunda é mais sutil e passa por gentileza.

| Evitar | Preferir |
|---|---|
| *Your own reading, today. There is no right answer here.* + a pergunta | Só a pergunta |
| *Este exercício vai preparar você para o que virá na aula.* | A instrução da tarefa |
| *Não se preocupe se achar difícil.* | Silêncio — ou apoio real, se a dificuldade for prevista |

**Tranquilizar antes de a dificuldade existir anuncia que ela existe.** Uma pergunta aberta *é* aberta; dizer que não há resposta certa é comentar o desenho da atividade, não conduzi-la. Se a instrução precisa de uma frase de conforto para não intimidar, o problema está na instrução.

E vale a formulação geral, que cobre os dois casos: **nada de linguagem metadidática, defensiva ou** **editorial dirigida ao aluno.**

#### 9.5 A camada muda o estatuto da mesma frase

Este é o teste que resolve a maioria das dúvidas de tom. *“**There is no right answer here**”* é imprópria na superfície do aluno — comenta a atividade — e **apropriada** na nota do professor, onde é orientação de condução: diz a quem conduz que não deve corrigir a resposta.

**A mesma frase não tem um único estatuto.** Antes de cortar uma formulação por tom, verificar em que camada ela está:

| A frase está em… | Ela é… |
|---|---|
| Instrução ao aluno | Comando: ação, objeto, resultado. Nada além |
| Comentário que o aluno lê depois de responder | Feedback da atividade — explica a resposta, não o desenho |
| Nota do professor | Orientação de condução — pode dizer o que não fazer, o que aceitar, onde não corrigir |
| Registro interno | Justificativa de desenho — o único lugar onde ela cabe |

Uma varredura de tom que não distingue camadas corta orientação legítima do professor junto com metalinguagem exposta ao aluno.

#### 9.6 Variedade linguística — American English

**American English é o padrão transversal de produção.** A regra vale para todo conteúdo produzido ou editado: Student Material, prompts, subprompts, feedback, language support, Teacher’s Notes, Teacher’s Guide, answer keys, possible answers, transcrições, scripts de áudio e rótulos pedagógicos.

- Aplicar ortografia, vocabulário, pontuação, números e datas segundo convenções americanas.
- Usar ponto decimal em conteúdo em inglês.
- Manter coerência interna — por exemplo: *organize, behavior, center, color* e *practice* como substantivo e verbo — salvo quando outra forma for objeto explícito de análise.
- Fontes externas autênticas preservam sua variedade original. Não alterar citações, transcrições fiéis nem a fala da fonte para forçar o padrão americano.
- Quando outra variedade for pedagogicamente relevante, identificá-la como variação do input, não como padrão de produção do curso.
- Não misturar convenções americanas e britânicas sem objetivo pedagógico declarado.

### 10. Fontes, factualidade e privacidade

- Preferir fonte autêntica quando ela agregar valor real à operação da aula.
- Verificar existência, autoria, data, trecho e estatuto documental. **Verificar existência não é** **verificar a natureza do conteúdo**: se é conversa ou montagem, entrevista ou leitura, é onde a inferência se disfarça de fato.
- Cada resposta-modelo é sustentada **pelo material apresentado ao aluno**. Nenhum gabarito afirma mais do que a evidência disponível.
- Distinguir fato, inferência e simulação — e marcar cada um.
- Não confundir anúncio, proposta, confirmação, entrada em vigor e resultado posterior.
- **Não chamar de real ou autêntico** material escrito para a aula. Usar *sample*, *adapted* ou *fictional* conforme a origem.
- Material real é **anonimizado**: nomes, empresas, valores e dados sensíveis são removidos ou substituídos. Casos compostos ou fictícios são alternativas válidas.
- Áudio principal usa arquivo estável. Síntese variável serve apenas como recurso declarado de contingência, nunca como material final.
- Registrar fonte, adaptação, licença ou autoria interna na camada apropriada.

**Se uma afirmação precisa de nota de rodapé para não enganar, o problema é a afirmação.**

### 11. Registro e persistência

- Informar quando um registro pode desaparecer.
- **Só prometer salvamento quando houver integração confirmada.** Enquanto não houver, o que precisa persistir tem de ser transcrito, e o material diz isso.
- Autoavaliação registra percepção; não comprova aprendizagem, e é tratada em separado dela.
- A governança aceita somente dois modelos: avaliação formal com teste ou acompanhamento docente. Tarefa integrada, simulação, apresentação, portfólio, demonstração de desempenho e produção final são instrumentos possíveis do acompanhamento docente, não modelos adicionais.
- Teste formal e instrumento de consolidação complementam as evidências; nenhum deles substitui o acompanhamento nem determina sozinho a progressão.

### 12. Gate de aprovação

**“****Aplicado****”** **só pode ser declarado após verificação literal no material final.** Falha parcial aparece como parcial; item não verificado aparece como pendente. **Quem produz não pode** **certificar a própria intenção como resultado.**

#### 12.1 Camadas de validação

| Camada | Checagens mínimas |
|---|---|
| Entrada e perfil | Campos completos; hipóteses marcadas; restrições respeitadas |
| Framework | Todas as funções essenciais declaradas estão representadas; a organização das etapas é coerente; produto e fronteira preservados |
| Avaliação | Um dos dois modelos está registrado; teste formal ou eventual instrumento está corretamente subordinado ao acompanhamento e à validação final do professor |
| Progressão | Operações não duplicadas; controle reduzido; tempo suficiente para a produção |
| Ciclo | Conteúdo anterior recuperado sem reensino; operação nova; mecânicas registradas |
| Linguagem | Correção, naturalidade, adequação ao nível, coerência entre modelo e gabarito |
| Variedade linguística | American English consistente em todo conteúdo produzido; variedade original preservada em fontes autênticas |
| Factual | Fonte, data, evidência, temporalidade, inferências marcadas |
| Coerência interna | Instrução, nota do professor, gabarito e papel do professor exigem **as mesmas ações** |
| Tempo | O essencial soma 55 minutos e as decomposições fecham |
| Camadas | Pre-class, in-class, post-class e syllabus descrevem a mesma aula |
| Resíduo | Nenhum fragmento de versão anterior sobrevive em qualquer parte do material |

#### 12.2 Quando parar em vez de entregar

- O framework é incompatível com o objetivo e não houve autorização para mudá-lo.
- Falta dado que altera materialmente a personalização ou a avaliação.
- Uma fonte obrigatória está inacessível ou não sustenta o gabarito.
- Há conflito entre normas sem precedência clara. **Declarar o conflito; nunca escolher em** **silêncio.**
- Não é possível verificar o material produzido.

### 13. Checklist bloqueante de entrega

Não entregar se alguma resposta for “não”.

☐ A superfície do aluno está livre do in-class e de qualquer conteúdo reservado ao professor? ☐ O pre-class tem exatamente seis atividades reais, somando 15–20 minutos? ☐ O pre-class preserva o núcleo protegido, e o in-class roda sem ele? ☐ Nenhuma minutagem por atividade aparece na superfície do aluno? ☐ A metalinguagem de produção foi removida de todas as superfícies? ☐ A aula tem **Teacher’s Guide completo**, em inglês, com os catorze campos de §8.1? ☐ O procedimento cobre todas as **etapas previstas**, cada uma com os dez campos de §8.2? ☐ Cada etapa declara apoio condicional **e** desafio — e não só o apoio? ☐ As notas locais acompanham as atividades sem substituir o guia? ☐ A superfície do aluno está livre de frase que explique o desenho da atividade ou tranquilize antes da dificuldade? ☐ Todas as funções essenciais declaradas para a aula estão representadas, sem validação por contagem fixa de etapas? ☐ Um dos dois modelos de avaliação está registrado, sem tratar teste, instrumento de consolidação ou autoavaliação como decisão isolada? ☐ O percurso essencial soma 55 minutos, com 5 de margem? ☐ Atividades condicionais, de extensão e opcionais começam recolhidas, sem unidade própria? ☐ Concluir a aula independe de checklist, de percurso completo e de respostas preenchidas? ☐ O que limpa o progresso de uma aula preserva feedback permanente e estado do ciclo? ☐ O feedback permanente está junto do acesso de cada aula, e não dentro do material da aula? ☐ O estado pedagógico do ciclo está em área exclusiva do professor? ☐ O post-class disponibiliza os cinco componentes funcionais, sem metadado novo e sem qualquer obrigatoriedade? ☐ Todo recurso externo foi aberto e verificado na fonte original? ☐ Pre-class, in-class, post-class e syllabus continuam alinhados pelo registro único? ☐ A correção apresentada ao aluno, o answer key e as orientações do Teacher’s Guide são coerentes entre si e pertencem à mesma versão da atividade? ☐ Nenhum campo foi preenchido com conteúdo inventado? ☐ Cada afirmação de “aplicado” tem evidência localizável no material final?

### Documentos relacionados

- **02 · Syllabus do Ciclo** — a linha que esta aula realiza.
- **03 · Estrutura dos Frameworks** — as funções pedagógicas, a progressão e as etapas previstas.
- **05 · Ciclo de Evolução** — o que o feedback desta aula alimenta.
