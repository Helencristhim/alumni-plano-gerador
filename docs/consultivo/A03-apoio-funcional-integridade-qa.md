> **Documento normativo importado do Drive — nao editar aqui.**
> Origem: `A03_Apoio_Funcional_Integridade_Pedagogica_e_QA.docx`
> Drive ID: ``
> Modificado no Drive: 2026-08-25
> Reimportar: `python3 scripts/consultivo/docx_to_md.py <arquivo.docx> docs/consultivo/A03-apoio-funcional-integridade-qa.md`
> A fonte e o .docx. Divergencia entre este arquivo e o Drive se resolve reimportando, nunca editando o .md.

## ADENDO NORMATIVO 03

**Apoio funcional, integridade pedagógica e safeguards de produção**

Private Class · Alumni by Better · Vigência: 24/08/2026

## 1. Status normativo, escopo e precedência

Este adendo tem caráter normativo e complementa os Documentos pedagógicos 00–06 e a Série P. Ele regula o apoio funcional em português nas atividades autônomas Black A1/A2, o modo de consulta do Pre-class na visão do professor e safeguards adicionais de integridade pedagógica, produção, interface e QA.

Em caso de formulação mais geral ou incompleta nos documentos anteriores, prevalece a especificação posterior e objetiva deste adendo nos temas aqui tratados. Nos demais assuntos, permanece a precedência definida no Documento 00.

As regras valem para novas produções e para revisões de artefatos ainda não liberados. Não obrigam a reabrir materiais já liberados, salvo quando houver defeito funcional relevante, exposição indevida, divergência entre atividade e gabarito ou prejuízo real de uso.

## 2. Finalidade e áreas abrangidas

O adendo estabelece três frentes complementares:

garantir apoio funcional completo e padronizado em português para todos os prompts operacionais do Pre-class e do Post-class Black A1/A2, sem substituir o contato necessário com o inglês;

preservar o caráter autônomo e assíncrono do Pre-class, separando a realização pelo aluno da consulta posterior realizada pelo professor;

transformar lacunas observadas em safeguards objetivos para In-class, Guided Discovery, noticing, pronúncia, Post-class, Teacher’s Guide, Answer Key, composição visual e validação.

## PARTE A — Apoio funcional em português no Pre-class e no Post-class

### 3. Cobertura obrigatória

Em todo Pre-class e Post-class Black A1 ou A2, cada prompt operacional dirigido ao aluno deve aparecer primeiro em inglês e ser acompanhado imediatamente por uma versão funcional em português, inicialmente recolhida e aberta por controle padronizado.

Considera-se prompt operacional todo texto que determine o que o aluno deve fazer, em que sequência deve agir, quais critérios deve observar ou qual resposta, escolha ou produção deve registrar. A regra se aplica a todas as mecânicas, inclusive escolha, matching, sorting, ordering, associação, preenchimento, escuta, preparação linguística, reflexão e produção escrita.

Nenhum prompt pode permanecer somente em inglês por ser considerado simples, recorrente ou intuitivo. A cobertura deve incluir, no mínimo, atividades de Key language, prompts de escuta como Listen to..., e qualquer outra instrução operacional do Pre-class ou do Post-class.

#### 3.1 Instruções distribuídas em mais de um parágrafo

Quando o contexto, a ação, a sequência ou o produto solicitado estiverem distribuídos entre dois ou mais parágrafos em inglês, o apoio em português deve cobrir o conjunto completo da orientação. Não é suficiente traduzir apenas o elemento visualmente marcado como prompt final.

### 4. Componente e rótulos

O apoio deve ficar imediatamente abaixo do conjunto de instruções em inglês e começar fechado. Todas as ocorrências devem usar os mesmos rótulos:

estado fechado: “Ver em português”;

estado aberto: “Ocultar português”.

O mesmo controle deve permitir abrir e recolher o conteúdo repetidamente, com estado, foco e rótulo acessível coerentes.

### 5. Tradução funcional e limites

A versão em português deve preservar todas as ações solicitadas, sua sequência, os critérios necessários e o produto esperado. O objetivo é esclarecer como realizar a tarefa, sem antecipar a solução nem reduzir indevidamente o processamento em inglês.

O apoio em português não pode:

revelar, sugerir ou restringir a resposta correta;

traduzir alternativas quando sua compreensão fizer parte da atividade;

traduzir automaticamente vocabulário-alvo;

traduzir textos que constituam insumo linguístico da atividade;

traduzir áudios ou transcripts;

antecipar feedback, critérios ou explicações que permitam deduzir o Answer Key;

substituir a leitura, a escuta ou a produção em inglês exigida pela tarefa.

Títulos, alternativas, vocabulário-alvo, textos de trabalho, áudios e transcripts permanecem em inglês, salvo quando a própria atividade tiver tradução como objeto pedagógico explicitamente declarado.

### 6. Sínteses pós-correção

Sínteses em português apresentadas depois da correção, como “Em outras palavras”, podem ser utilizadas quando a explicação em inglês estiver acima da faixa de compreensão independente esperada. Elas devem aparecer somente após a resposta ou correção, não podem revelar antecipadamente a solução e não substituem a tradução funcional do prompt.

### 7. Visibilidade por modo ativo

O componente de apoio em português pertence exclusivamente à visão do aluno. Nessa visão podem aparecer o botão “Ver em português / Ocultar português”, o texto recolhível e as sínteses pós-correção em português.

Na visão do professor, o componente inteiro deve estar ausente da interface e da navegação; não é suficiente ocultar apenas o texto ou desabilitar o botão. A visibilidade é determinada pelo modo ativo: quando a URL do professor oferece uma visualização deliberada da visão do aluno, essa visualização deve reproduzir a interface do aluno; ao retornar à visão do professor, o componente não pode permanecer no DOM interativo, no foco do teclado nem na superfície visível.

### 8. Exclusão do In-class

O apoio escrito recolhível em português não deve ser inserido no In-class. Nessa área, o professor pode oferecer apoio oral em português conforme a necessidade, preservando a participação e o contato prioritário com o inglês.

## PARTE B — Pre-class e Answer Key na visão do professor

### 9. Natureza autônoma e assíncrona

O Pre-class é realizado autonomamente pelo aluno. O professor acessa posteriormente apenas os dados que a interface efetivamente registrou. Nenhuma nota do Answer Key pode presumir intervenção oral, correção síncrona ou solicitação adicional durante a realização.

### 10. Modo de consulta na visão do professor

Na visão do professor, o Pre-class deve ser apresentado exclusivamente em modo de consulta. Controles destinados à realização, correção ou reinicialização da atividade pelo aluno não devem aparecer.

Devem estar ausentes, e não apenas desabilitados:

seleção de alternativas;

campos editáveis de preenchimento;

controles de ordenação, associação ou movimentação de itens;

gravação, envio ou substituição de respostas;

botões “Check”, “Submit”, “Try again”, “Reset”, “Clear” ou equivalentes;

botão “Show transcript” ou equivalente nas atividades de áudio;

feedback automático acionado pela realização da atividade.

A visão do professor pode exibir os itens da atividade, mas não deve oferecer uma segunda execução. As respostas registradas pelo aluno, quando disponíveis, são apresentadas como dados de consulta em representação estática equivalente: texto, linha, etiqueta, cartão ou tabela sem semântica de botão, campo, select, checkbox, radio, área arrastável ou outro controle interativo, ainda que desabilitado. A representação distingue resposta registrada, ausência de resposta e, quando aplicável, estado de correção, sem permitir alteração.

O controle “Fechar todos os gabaritos” permanece disponível na visão do professor, pois organiza a consulta e não realiza nem corrige a atividade. Na visão do aluno, esse controle não aparece; permanece o controle “Reset my answers”, conforme a regra da atividade, para reinicializar apenas as respostas do próprio aluno.

### 11. Conteúdo disponível ao professor

O professor deve poder consultar:

o prompt original em inglês;

os conteúdos e itens apresentados ao aluno;

as respostas efetivamente registradas pelo aluno, quando disponíveis;

o Answer Key;

o transcript completo correspondente, dentro do Answer Key, em toda atividade que utilize áudio;

os critérios de correção e as respostas aceitas pela interface;

as justificativas pedagógicas e diagnósticas pertinentes;

orientações de retomada posterior, quando explicitamente planejadas no Teacher’s Guide ou no In-class.

O Answer Key é a fonte de consulta do professor para compreender a resposta esperada e interpretar o registro produzido pelo aluno. Ele deve corresponder exatamente à versão da atividade apresentada ao aluno.

Em atividades de áudio, o transcript integra obrigatoriamente o Answer Key e deve corresponder ao arquivo efetivamente reproduzido. Por isso, a visão do professor não utiliza um controle separado “Show transcript”: a consulta ao transcript ocorre no próprio gabarito, junto da resposta, do rationale e das demais informações da atividade.

### 12. Conteúdo não autorizado no Answer Key

Orientações como “aceite”, “peça”, “pergunte”, “confirme com o aluno”, “solicite uma segunda resposta” ou equivalentes não pertencem ao gabarito de uma atividade assíncrona. Quando pedagogicamente necessárias, devem ser transferidas para uma retomada posterior explicitamente planejada, para o Teacher’s Guide ou para o In-class, onde exista mediação docente real.

Notas sobre embaralhamento, organização visual, implementação técnica ou justificativas de design também não constituem respostas alternativas. Essas informações pertencem às diretrizes de produção, à documentação técnica ou à validação de conformidade.

É permitida uma nota explicativa que esclareça por que determinado item não integra as opções, desde que ela descreva a lógica da atividade sem mandar o professor intervir durante o Pre-class. Exemplo de formulação funcional: “And you? não aparece entre as opções desta atividade porque é um movimento conversacional, não uma das expressões representadas pelas falas.”

### 13. Regra para “Também aceitável”

Em atividades fechadas, “Também aceitável” somente pode existir quando todas as condições abaixo forem atendidas:

a interface permite ao aluno registrar a resposta alternativa;

a resposta alternativa fica armazenada e disponível para consulta;

há uma regra explícita para interpretá-la;

a alternativa é pedagogicamente válida para o objetivo declarado;

a correção automática, quando houver, reconhece essa possibilidade sem gerar divergência.

Se a interface não aceita, não registra ou não permite recuperar a resposta, ela não pode aparecer como alternativa aceitável. Em atividades de escolhas fechadas, o Answer Key não pode aceitar formulações orais ou respostas livres que a interface não consegue receber.

## PARTE C — Integridade pedagógica e de produção

### 14. Responsabilidade entre tela compartilhada e Teacher’s Guide

A tela compartilhada deve apresentar ao aluno o contexto, a ação, a sequência, o apoio e o produto necessários para realizar a atividade. Falas operacionais do professor, decisões de condução, respostas que o professor dará, informações que deverá inventar e instruções sobre o que fará durante a atividade pertencem ao Teacher’s Guide.

A formulação projetada deve ser centrada na operação do aluno, e não na voz momentânea do professor. Evitar “Ask me…”, “I will answer…” e “Report it back to me” quando me ou I representa apenas o professor como interlocutor circunstancial. Preferir formulações estáveis, como “Ask three questions”, “Report what you heard” ou “Ask for the missing detail”.

Esse safeguard complementa a regra de subprompts com função real do A02: além de acrescentar informação necessária, cada instrução deve atribuir a ação à camada correta.

### 15. Contraste observável em Guided Discovery

Esta seção especifica objetivamente a regra já existente de que Guided Discovery exige evidência suficiente, operação cognitiva, hipótese, verificação, clarificação e aplicação. Uma pergunta de descoberta não pode exigir que o aluno infira regra, distinção ou efeito a partir de um único exemplo correto.

Sempre que o objetivo for descobrir contraste de significado, uso ou forma, a atividade deve oferecer:

contexto curto e suficiente para interpretar a diferença;

duas ou mais versões realmente contrastantes;

escolha, classificação ou comparação concreta;

justificativa em linguagem comum, sem exigir terminologia gramatical;

explicação revelada somente depois da resposta;

teste breve do padrão em um novo exemplo.

Quando duas formas forem possíveis, o contexto deve permitir analisar diferença de significado, perspectiva ou efeito. A atividade não pode apresentar uma delas como simplesmente errada. Perguntas metalinguísticas hipotéticas sem erro, contraste ou evidência observável não constituem Guided Discovery.

### 16. Modalidade funcional do noticing

Cada operação de noticing deve ter uma modalidade principal claramente definida. Se o contraste é apresentado integralmente por escrito e a decisão depende da forma escrita, a atividade é de Reading; repetir imediatamente as mesmas versões em áudio não cria uma segunda operação. Se o contraste deve ser descoberto auditivamente, as formas escritas não podem revelar previamente a resposta.

O áudio só deve ser acrescentado a uma atividade visual quando cumprir função distinta e explícita, como tonicidade, redução, ritmo, segmentação, inteligibilidade ou confirmação posterior. Não usar áudio como duplicação decorativa do texto.

Quando texto e áudio participarem da mesma atividade, devem representar exatamente o mesmo contraste, com correspondência verificável entre roteiro aprovado, mídia reproduzida, alternativas, resposta e rationale.

### 17. Pronúncia: descoberta ou drilling

Usar contraste auditivo para descoberta somente quando as versões puderem representar de forma confiável a diferença que o aluno deve perceber. Quando isso não for possível, apresentar um modelo correto, indicar o foco auditivo e realizar repetição apoiada.

Nesse segundo caso, identificar a operação como pronunciation practice ou drilling, e não como Guided Discovery. O rótulo pedagógico deve corresponder ao trabalho cognitivo efetivamente solicitado, sem simular descoberta onde existe modelagem seguida de repetição.

### 18. Diferenciação funcional no Post-class

Esta seção especifica a classificação funcional de Reading e Language Reference no Post-class. Os dois componentes podem abordar o mesmo tema, objetivo comunicativo ou repertório linguístico; essa sobreposição temática não constitui redundância. A classificação depende da função predominante, da organização principal da fonte e da operação oferecida ao aluno.

Reading proporciona contato com texto discursivamente desenvolvido, preferencialmente externo e autêntico, para ampliar contexto, perspectiva ou repertório comunicativo, profissional ou temático. Pode ensinar estratégias, comentar escolhas linguísticas e apresentar exemplos de uso sem deixar de ser Reading. Language Reference funciona como recurso organizado de consulta: explica, sistematiza, exemplifica ou apoia o uso de formas, funções, padrões, estruturas ou vocabulário. Texto corrido não transforma uma referência em Reading quando a leitura está subordinada à consulta ou à prática linguística.

Quando a fonte combinar características das duas categorias, classificar pela operação predominante: ler para ampliar compreensão, perspectiva, contexto ou repertório corresponde a Reading; consultar, compreender ou praticar uma sistematização linguística corresponde a Language Reference. O mesmo recurso não ocupa simultaneamente as duas categorias apenas para preencher componentes.

Há redundância somente quando os componentes reproduzem substancialmente o mesmo conteúdo, no mesmo enquadramento e para a mesma operação, sem acrescentar desenvolvimento discursivo, nova fonte, modalidade, organização de consulta ou possibilidade de uso. Um artigo sobre estratégias comunicativas ou profissionais pode ser Reading; uma página organizada em torno de regras, padrões e exercícios pertence a Language Reference.

### 19. Precisão proporcional do Answer Key no In-class

Esta seção se aplica exclusivamente ao Answer Key e às orientações de resposta do In-class, área que pode conter atividades fechadas, apoiadas mas abertas e produções abertas. Ela não redefine o Answer Key do Pre-class e não autoriza a criação de atividades semiabertas ou abertas no estudo autônomo.

No In-class, o conteúdo do Answer Key deve ser proporcional ao grau de abertura da atividade:

atividade fechada: apresentar a correspondência exata de cada item, e não apenas quantidades, categorias gerais ou o princípio da resposta;

atividade apoiada, mas aberta: apresentar uma ou mais respostas possíveis claramente identificadas como apoio, sem convertê-las em modelo obrigatório;

produção aberta: apresentar critérios de sucesso, evidências esperadas e pontos de comparação, e não um texto pronto para reprodução.

A existência de Possible Answers não autoriza transformar produção aberta em exercício de resposta única. O professor deve conseguir distinguir gabarito exato, possibilidade legítima e critério de sucesso.

### 20. Teacher’s Guide: safeguard de aplicação da regra vigente

Os Documentos 04 e 06 já determinam que o Teacher’s Guide acrescente condução profissional e não carregue justificativa editorial, histórico do gerador ou instrução de produção. Este adendo não cria uma definição concorrente; torna sua aplicação verificável.

O Teacher’s Guide deve explicar como conduzir, o que observar, quais respostas esperar, quando oferecer apoio e quando avançar. Deve reprovar a presença de:

limitações da ferramenta, da voz ou do ambiente de geração;

justificativas internas do gerador;

decisões de implementação;

defesa da mecânica escolhida;

comentários sobre o que foi deliberadamente produzido ou omitido.

Quando explicar contraste linguístico, o guia deve nomear o padrão observável e fornecer exemplos. Formulações vagas, como “this version is not available in English”, não substituem explicação didática. Formulação adequada: “After an indirect-question opening, the clause uses statement order: what the deadline is, not what is the deadline.”

### 21. Unidade de versão: safeguard ampliado

A unidade de versão já é obrigatória no Documento 04, na Série P e no A02. Como reforço de aplicação, a validação deve comparar conjuntamente instrução, alternativas, texto projetado, áudio, transcript, resposta correta, rationale, Possible Answers, Answer Key e Teacher’s Guide.

Toda mudança de mecânica ou contraste exige atualização conjunta dos componentes afetados. Reprovar contraste visual diferente do reproduzido em áudio, prompt atualizado em tela com “Exact prompt” residual no guia, alternativa removida que permanece no gabarito e rationale pertencente a versão anterior.

## PARTE D — Safeguards visuais, QA e aplicação

### 22. Perguntas na tela de abertura

Esta é uma exceção específica ao tratamento geral das perguntas projetadas definido na Série P. Quando a tela de abertura incluir uma pergunta comunicativa, ela deve integrar o bloco introdutório e seguir a mesma família tipográfica, o mesmo peso, a mesma cor e a mesma hierarquia visual do subtítulo da abertura.

Não aplicar nessa tela o tratamento destinado às perguntas principais das etapas internas, como fonte específica, itálico, cor de destaque, fundo, centralização adicional ou aumento isolado de tamanho.

A pergunta pode ser separada da contextualização por espaçamento, quebra de linha ou novo parágrafo, mas deve permanecer visualmente subordinada ao título da aula e coerente com o padrão das demais aberturas do artefato.

### 23. QA de composição renderizada

A presença correta dos elementos no HTML ou no DOM não confirma que a tela esteja funcional. A QA deve inspecionar a composição efetivamente renderizada, nos estados relevantes e nas larguras suportadas.

Verificar, no mínimo:

subprompt após listas, tabelas e cartões;

margens negativas herdadas e deslocamentos produzidos por seletores amplos;

textos sobrepostos, cortados ou fora do contêiner;

controles encostados ao conteúdo linguístico;

expansão de perguntas, instruções, transcripts e feedback após revisões;

comportamento em fundos claros e escuros e em diferentes larguras de tela.

A validação deve combinar presença estrutural, estilo computado, interação e regressão visual. Um elemento presente, mas sobreposto, inacessível ou visualmente incorporado ao conteúdo errado deve ser considerado falha.

### 24. Pontuação dos rótulos do Teacher’s Guide: checkpoint de conformidade

O uso de dois-pontos nos rótulos que introduzem conteúdo já é regra editorial do Documento 04. Não se trata de nova definição. O safeguard automático deve verificar sua aplicação em todas as ocorrências.

Devem usar dois-pontos: Goal:, Run it:, Exact prompt:, Expected:, Expected matching:, Conditional support:, Challenge:, Watch for: e Move on when:, além de qualquer rótulo equivalente que introduza conteúdo.

Reprovar ponto-final entre o rótulo e o conteúdo introduzido, como “Expected matching.” ou “The two discovery questions.”. O segundo exemplo deve ser tratado como rótulo somente quando efetivamente introduzir as perguntas; nesse caso, usar “The two discovery questions:”.

### 25. Classificação normativa e destino

| **Tema** | **Status** | **Aplicação principal** |
|---|---|---|
| Tela × condução docente | Regra nova | In-class, Teacher’s Guide e QA |
| Contraste observável | Especificação objetiva | Documento 03, Grammar e QA pedagógica |
| Modalidade do noticing | Regra nova | Frameworks, mídia e QA |
| Pronúncia: descoberta/drilling | Regra nova | Frameworks e Teacher’s Guide |
| Reading × Language Reference | Reforço funcional | Post-class e revisão pedagógica |
| Answer Key proporcional | Safeguard novo | Somente In-class e Teacher’s Guide |
| Conteúdo operacional do guia | Checkpoint de regra vigente | Teacher’s Guide e QA |
| Unidade de versão | Ampliação de checkpoint vigente | Tela, mídia, guia e gabarito |
| Pergunta de abertura | Exceção visual nova | Série P e regressão visual |
| Composição renderizada | Safeguard de QA | P2/P3 |
| Dois-pontos nos rótulos | Checkpoint de regra vigente | QA editorial automático |
| Card da quarta aula do bloco | Safeguard operacional novo | Visão do professor, Estado pedagógico e QA |

### 26. Matriz funcional por visão

| **Elemento** | **Visão do aluno** | **Visão do professor** |
|---|---|---|
| Prompt original em inglês | Visível | Visível |
| Apoio recolhível em português | Visível em A1/A2 | Ausente |
| Controles de realização e Check | Visíveis quando aplicáveis | Ausentes |
| Reset/Try again | Conforme regra da atividade | Ausente |
| Fechar todos os gabaritos | Ausente | Visível |
| Transcript do áudio no Pre-class | Show/Hide quando aplicável | Dentro do Answer Key |
| Respostas registradas | Editáveis apenas durante a realização prevista | Somente consulta |
| Answer Key e rationale | Não visíveis antes da correção autorizada | Visíveis |

### 27. Validação bloqueante

☐ Todo prompt operacional do Pre-class e do Post-class Black A1/A2 possui apoio funcional completo em português.

☐ O apoio está imediatamente associado ao conjunto integral da instrução e começa recolhido.

☐ Os rótulos “Ver em português” e “Ocultar português” são usados de forma uniforme.

☐ A tradução não omite ação, sequência, critério ou produto e não revela respostas ou conteúdo linguístico indevido.

☐ O componente de português aparece somente quando a visão do aluno está ativa e não existe como controle desabilitado na visão do professor.

☐ O In-class não contém apoio escrito recolhível em português.

☐ Na visão do professor, o Pre-class está em modo de consulta e não apresenta seleção, preenchimento, Check, Submit, Reset ou equivalentes.

☐ Na visão do professor, atividades de áudio apresentam o transcript dentro do Answer Key e não exibem “Show transcript”.

☐ “Fechar todos os gabaritos” permanece na visão do professor; “Reset my answers” permanece somente na visão do aluno.

☐ As respostas registradas pelo aluno são consultáveis, mas não editáveis, na visão do professor.

☐ O Answer Key corresponde à atividade e não presume intervenção oral durante sua realização.

☐ “Também aceitável” só aparece quando a alternativa pode ser registrada, recuperada e interpretada pela interface.

☐ Nenhuma justificativa de design ou implementação aparece como resposta alternativa.

☐ A tela compartilhada contém somente ações e informações destinadas ao aluno; falas e decisões do professor permanecem no Teacher’s Guide.

☐ Toda descoberta de contraste apresenta evidência comparável, resposta antes da explicação e teste breve em novo exemplo.

☐ A modalidade principal do noticing está definida e o áudio cumpre função distinta ou confirmação posterior.

☐ Pronunciation practice e drilling não são rotulados como Guided Discovery.

☐ Reading e Language Reference foram classificados pela função predominante; sobreposição temática não foi tratada como redundância, e o mesmo recurso não foi usado nas duas categorias apenas para preencher componentes.

☐ No In-class, o Answer Key é exato em tarefas fechadas, não prescritivo em tarefas apoiadas e criterial em produções abertas.

☐ O Teacher’s Guide não contém justificativas de produção e explica contrastes com padrão observável e exemplos.

☐ Tela, mídia, resposta, rationale, Possible Answers e Teacher’s Guide pertencem à mesma versão.

☐ Perguntas de abertura seguem o subtítulo, sem receber o tratamento visual das perguntas internas.

☐ A regressão visual verifica composição, sobreposição, expansão e larguras suportadas.

☐ Os cards das aulas 04, 08, 12, 16 e 20 apresentam os comandos Antes da aula e Após a aula com bloco e intervalo corretos; “Estado pedagógico do ciclo” abre o painel existente sem duplicar seu conteúdo.

☐ Rótulos do Teacher’s Guide que introduzem conteúdo usam dois-pontos em todas as ocorrências.

### 28. Card da quarta aula de cada bloco — lembrete do Estado pedagógico do ciclo

Na visão do professor, os cards das aulas 04, 08, 12, 16 e 20 orientam a consulta e a atualização do Estado pedagógico do ciclo. Informar que a aula encerra o bloco ou corresponde ao checkpoint não substitui os comandos operacionais.

Antes da aula. No início de “Estrutura e preparação”, apresentar: “Antes da aula: revise o Estado pedagógico do ciclo e os registros das aulas {início–fim}. Esta aula encerra o bloco {n} e fornece a última evidência necessária para o checkpoint.” Parametrização: bloco 1, aulas 01–04; bloco 2, 05–08; bloco 3, 09–12; bloco 4, 13–16; bloco 5, 17–20.

“Estado pedagógico do ciclo” funciona como botão ou link para o painel já existente na visão docente, preservando o retorno ao card. Não duplicar nem resumir o estado dentro do card.

Após a aula. Ao final do card, apresentar: “Após a aula: atualize o Estado pedagógico do ciclo com as evidências consolidadas das aulas {início–fim} antes de definir a distribuição, os apoios e os objetivos do bloco seguinte.” Na aula 20, usar “antes da validação pedagógica final e da decisão sobre o ciclo seguinte”. O primeiro comando é de consulta; o segundo, de consolidação.

## 29. Instrução obrigatória ao gerador

INSTRUÇÃO AO GERADOR: carregue este Adendo Normativo 03 junto aos Documentos 00–06, à Série P, aos Adendos Normativos 01 e 02 e aos anexos técnicos aplicáveis antes de planejar, gerar, revisar ou validar qualquer novo artefato Black. A ausência do A03 no lote bloqueia a declaração de conformidade integral para materiais que contenham Pre-class, In-class ou Post-class.

Na saída de validação, declare nominalmente o carregamento do A03 e reporte cada tema da Validação bloqueante (§27), incluindo a presença e o funcionamento dos comandos de consulta e consolidação do Estado pedagógico do ciclo nos cards das aulas 04, 08, 12, 16 e 20.

## PARTE E — SAFEGUARDS ADICIONAIS DE ATIVIDADE E INTERFACE

### 30. Estado real da interface

Verbos como open, reveal, select, compare, listen, read, write e submit somente podem ser usados quando a interface oferece exatamente essa ação naquele estado. Se todos os itens já estiverem visíveis, usar present, work through, focus on ou equivalente, e não reveal. Se um cartão estiver fechado, a instrução não pode mandar ler conteúdo ainda indisponível. Tela, estado interativo e Teacher’s Guide devem permanecer sincronizados.

### 31. Player, rótulo e seleção no mesmo card

Em atividades auditivas de escolha, cada alternativa deve apresentar no mesmo card o rótulo semântico — por exemplo, Version A ou Version B —, o player correspondente e o controle de seleção. Não separar players das alternativas nem recorrer a referências posicionais como “the first one” e “the second one” quando as versões já possuem rótulos estáveis.

### 32. Transcript posterior em listening contrast

Quando a escolha depender exclusivamente do áudio, o transcript permanece indisponível antes da tentativa. Depois da escolha, a explicação revela os transcripts completos, identificados pela mesma nomenclatura dos players, para verificação, comparação e sistematização. Player, transcript, alternativa, resposta e rationale devem pertencer à mesma versão.

### 33. Possible Answers em prática menos controlada

Atividades menos controladas não precisam de gabarito único, mas o Teacher’s Guide deve oferecer Possible Answers quando o professor puder precisar de apoio para modelar, esclarecer ou destravar a produção. Cada resposta possível corresponde individualmente ao estímulo, preserva a função comunicativa, é identificada como apoio e admite outras respostas coerentes. Não exibir nem induzir essas respostas como única solução.

### 34. Contagem funcional e terminologia

Verificar se toda quantidade declarada no título, instrução, Teacher’s Guide, Answer Key e critério de conclusão corresponde aos itens reais da atividade. Nomes de funções, alternativas, versões, personagens e estágios devem ser usados de forma estável em todas as camadas. Divergência quantitativa ou terminológica é falha de versão, ainda que todos os elementos estejam presentes.

#### Checklist adicional

O verbo da instrução corresponde à ação realmente disponível naquele estado?

Cada alternativa auditiva reúne rótulo, player e seleção no mesmo card?

Listening contrast mantém transcripts ocultos antes da tentativa e os revela depois com rótulos correspondentes?

Possible Answers de prática menos controlada correspondem individualmente aos estímulos e permanecem apoio, não script?

Todas as contagens e nomenclaturas coincidem entre tela, mídia, guia, gabarito e conclusão?

### 35. Rotação funcional da produção principal

Antes da entrega do bloco, comparar as produções principais das quatro aulas. Reprovar repetição automática da mesma mecânica — especialmente role-play, simulação ou professor como interlocutor — quando não houver justificativa funcional e diferença material entre as operações.

A validação distingue repetição legítima de homogeneização:

Repetição legítima: a mecânica permanece, mas operação, decisão, interlocutor, pressão, consequência, produto ou evidência mudam materialmente.

Homogeneização: apenas tema, contexto superficial ou vocabulário mudam, enquanto a mesma dinâmica e o mesmo produto são reproduzidos.

A rotação não exige quatro mecânicas diferentes por bloco. Exige variedade funcional suficiente e ausência de escolha automática baseada apenas na prioridade de Speaking ou Interaction.

#### Checkpoint de aplicação

A prioridade de modalidade foi traduzida em frequência e peso da evidência, sem fixar uma mecânica?

Role-play ou simulação possui papéis, interlocutores, objetivos e consequências constitutivos?

Repetições no bloco apresentam diferença material de operação, produto ou evidência?

A comparação foi feita com as quatro aulas do bloco, sem impor cota artificial de formatos?
