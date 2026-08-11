# Instrução Corretiva Ao Gerador

> **Fonte:** `Instrucao_corretiva_gerador_Private_Black_Adults_revisado.docx`, entregue pelo Dan em **11/08/2026**. Cabecalho do proprio
> documento: *"Private Black Adults · Documento normativo consolidado · Agosto de 2026"*.
>
> **Transcricao fiel**, extraida do XML do `.docx` (`word/document.xml`). Nada foi
> acrescentado, resumido nem interpretado; a unica mudanca e a formatacao em Markdown
> (tabelas e titulos). Esta copia existe para que o molde possa **citar a fonte** de cada
> ajuste sem depender de um arquivo em `~/Downloads`.
>
> A revisao pedida ao lote do molde: 16 correcoes obrigatorias e 13 criterios de aceite.
>
> **Documentos irmaos:** `docs/NORMATIVO-planejamento-aulas-2026-08.md` (o .docx de planejamento) · `docs/NORMATIVO-arquitetura-frameworks-2026-08.md` (a apresentacao de 16 slides) · `docs/NORMATIVO-estrutura-frameworks-2026-08.md` · `docs/NORMATIVO-diretrizes-producao-2026-08.md` · `docs/NORMATIVO-prompt-controlador-2026-08.md`.
>
> **Onde isto virou codigo:** cada criterio de aceite da secao 4 e uma linha da matriz de
> `scripts/relatorio_validacao.py`, com o gate que o comprova ou a marca NAO VERIFICADO.

---

Revisão do perfil-modelo, syllabus provisório e quatro aulas do bloco Build

| OBJETIVO. Corrigir o lote já produzido com base exclusivamente nos quatro documentos normativos fornecidos. Esta instrução não autoriza uma reconstrução livre: preserve o que estiver adequado e altere todos os pontos abaixo de forma integrada. |
|---|

## 1. Escopo e hierarquia da revisão

Use como fonte normativa: os quatro documentos enviados — Diretrizes Pedagógicas/Proposta de Planejamento, Estrutura dos Frameworks, Diretrizes de Produção e Prompt Controlador Único.

Revise simultaneamente: o perfil-modelo, o syllabus provisório de 20 aulas, o arquivo principal e os quatro arquivos de aula. Não corrija cada arquivo isoladamente.

Critério de decisão: quando houver divergência entre o lote gerado e os documentos, prevalecem os documentos. Não invente uma nova regra para justificar a versão atual.

## 2. Correções obrigatórias

### 2.1 Remover resíduos de outros templates

Falha observada: O artefato mantém o cabeçalho “Travel English — 48 Aulas”, incompatível com o perfil de Stephanie e com o ciclo atual.

Correção obrigatória: Substitua todos os metadados, títulos, cards, summaries, scripts, answer keys e notas herdados. Faça busca global por resíduos de versões anteriores e valide que nomes, quantidade de aulas, nível, perfil e projeto correspondam ao mesmo lote.

Base nos documentos: Diretrizes de Produção e Prompt Controlador: validação final sem resíduos de versões.

### 2.2 Reconstruir o perfil nos 14 campos estruturais

Falha observada: O perfil foi reduzido a poucos dados biográficos, contexto profissional, comportamento, dificuldade, nível estimado e três hipóteses.

Correção obrigatória: Apresente os 14 campos previstos na consultoria. Use somente dados fornecidos. Marque dados ausentes como “não informado” ou “a validar”; não complete lacunas como fatos. Separe claramente dado confirmado, percepção da aluna e hipótese pedagógica.

Base nos documentos: Proposta de Planejamento e Prompt Controlador: perfil estruturado de 14 campos como entrada e saída obrigatória.

### 2.3 Tratar o perfil inicial como hipótese

Falha observada: H1, H2 e H3 foram tratadas como diagnóstico praticamente fechado, e as quatro aulas foram desenhadas para confirmá-las.

Correção obrigatória: Mantenha hipóteses iniciais como itens a validar. Redesenhe o bloco para também permitir descoberta de necessidades não previstas. Nenhuma conclusão deve ser declarada antes das evidências das aulas 1–4.

Base nos documentos: Diretrizes Pedagógicas: o perfil inicial é hipótese; as quatro primeiras aulas ensinam e diagnosticam.

### 2.4 Apresentar um syllabus provisório de 20 aulas

Falha observada: A interface anuncia 20 aulas, mas só apresenta as quatro primeiras.

Correção obrigatória: Inclua aulas 1–20 no planejamento provisório. Detalhe as aulas 1–4 como bloco Build e marque as aulas 5–20 como ajustáveis após o checkpoint. Para cada aula, registre número, bloco, framework, foco, objetivo/produto, relação com a progressão e posição na rotação.

Base nos documentos: Proposta de Planejamento e Prompt Controlador: syllabus provisório antes da Aula 1; confirmação, ajuste ou reconfiguração das aulas 5–20 após a Aula 4.

### 2.5 Fixar uma única ordem oficial

Falha observada: O arquivo principal usa ESP–Listening–Grammar–Reading, enquanto os arquivos individuais numeram Reading–Listening–Grammar–ESP. As referências entre aulas ficam cronologicamente impossíveis.

Correção obrigatória: Defina uma única sequência oficial e aplique-a em nomes de arquivo, interface, syllabus, cabeçalhos, dependências, evidências e Teacher’s Notes. Toda aula só pode usar como evidência uma produção já coletada. Corrija todas as referências “aula anterior/seguinte”.

Base nos documentos: Prompt Controlador: número, bloco, framework, posição no lote e relação com aulas anteriores e seguintes.

### 2.6 Ampliar a função diagnóstica do bloco Build

Falha observada: As quatro aulas permanecem no mesmo micronicho: observação de aula, materiais, syllabus e feedback pedagógico. Isso pode distorcer a estimativa de nível pela familiaridade temática.

Correção obrigatória: Mantenha personalização, mas varie contexto, demanda comunicativa, grau de familiaridade e tipo de apoio. O conjunto deve gerar evidências sobre nível, habilidades, linguagem, interação e scaffolding, além de verificar adequação temática e objetivos. Não transforme as quatro aulas em testes; elas devem ensinar e diagnosticar.

Base nos documentos: Diretrizes Pedagógicas: bloco Build valida nível, objetivos, contextos e apoio e gera evidências por habilidade, linguagem e interação.

### 2.7 Diferenciar efetivamente os quatro frameworks

Falha observada: Os rótulos mudam, mas o percurso se repete: input, classificação, regra funcional, banco de frases, produção cronometrada, feedback e retask.

Correção obrigatória: Preserve a função central de cada framework: Reading into Speaking deve transformar leitura em construção de conteúdo oral; Listening into Interaction deve desenvolver compreensão e gestão da interação; Grammar for Communication deve resolver uma lacuna estrutural em contexto; ESP deve culminar em uma tarefa real completa. Diferencie operação cognitiva, interação, produto e evidência — não apenas título, widget ou conteúdo.

Base nos documentos: Estrutura dos Frameworks e Diretrizes de Produção: frameworks reconhecíveis, função própria e variedade real de operações.

### 2.8 Eliminar a sobreposição Grammar–ESP

Falha observada: Grammar e ESP voltam aos mesmos contrastes: descrição versus julgamento, past continuous/past simple, might/could e you have to/never.

Correção obrigatória: Reserve a sistematização estrutural para Grammar. Na aula ESP, recupere a linguagem apenas como recurso de performance e expanda a tarefa profissional: compreender o caso, apresentar evidência, verificar intenção, responder à discordância, negociar uma alternativa e confirmar próximos passos. Ao recuperar conteúdo anterior, altere objetivo, interlocutor, fonte ou transformação exigida.

Base nos documentos: Estrutura dos Frameworks: ESP não deve sistematizar extensamente a gramática reservada à aula Grammar; uma aula não deve assumir a função de outra.

### 2.9 Refazer a rotação de mecânicas

Falha observada: Sorting, cards/reveal, banco de expressões, fala cronometrada, interlocutor que interpreta mal, dois campos de feedback e retask aparecem repetidamente.

Correção obrigatória: Mapeie, para cada atividade, mecânica, função, operação cognitiva, grau de controle e evidência. Substitua combinações repetidas dentro do bloco. Uma troca de widget sem mudança na ação do aluno não conta como variedade. Preserve a progressão do apoio controlado para produção mais autônoma.

Base nos documentos: Diretrizes de Produção e Prompt Controlador: evitar repetição imediata da mesma combinação; não chamar troca de widget de variedade.

### 2.10 Corrigir inconsistências entre tela e procedimento

Falha observada: Na aula de Reading, a Teacher’s Note instrui “toque o áudio”, embora a tarefa exija leitura de documentos.

Correção obrigatória: Faça auditoria slide a slide. Prompt, subprompt, mídia, widget, Teacher’s Note, answer key e turnos do professor devem solicitar a mesma ação, usar a mesma fonte e respeitar o mesmo objetivo. Remova instruções herdadas de outros frameworks.

Base nos documentos: Diretrizes de Produção: alinhamento obrigatório entre instrução na tela, nota, chave e ação do professor.

### 2.11 Reescrever a prediction da aula de Reading

Falha observada: A previsão e seu racional já direcionam a aluna para a inconsistência de tempo que deveria ser descoberta na leitura; o widget ainda marca alternativas de modo inadequado.

Correção obrigatória: Crie uma hipótese genuinamente verificável que ative contexto sem antecipar a resposta. Não apresente racional conclusivo antes da leitura. Revise labels, estados e feedback do widget para que não sugiram que todas as alternativas são “Main idea”.

Base nos documentos: Estrutura de Reading: ativar contexto sem antecipar respostas e gerar hipótese verificável.

### 2.12 Distribuir melhor as evidências diagnósticas

Falha observada: O lote promete validação ampla, mas coleta repetidamente evidências sobre mitigação, descrição/julgamento e feedback pedagógico.

Correção obrigatória: Defina previamente quais evidências cada aula produzirá. Ao final do bloco, deve haver base suficiente para atualizar reading, listening, speaking, interaction, writing quando relevante, recursos linguísticos, inteligibilidade/pronúncia, estratégias, fatores afetivos e tipo de apoio. Não exija que cada aula cubra tudo; distribua a cobertura pelo conjunto.

Base nos documentos: Proposta de Planejamento: evidências por habilidade, linguagem, interação e apoio para confirmação ou reconfiguração após a Aula 4.

### 2.13 Ampliar o repertório funcional

Falha observada: A dificuldade comunicativa foi reduzida principalmente a trocar you have to/never por might/could.

Correção obrigatória: Trate mitigação como um recurso, não como todo o objetivo. Inclua funções compatíveis com a tarefa: contextualizar, apresentar evidência, separar observação de interpretação, verificar intenção e entendimento, reformular, responder à discordância, negociar alternativa, sinalizar prioridade e fechar com ação acordada. Selecione apenas as funções necessárias em cada framework.

Base nos documentos: Diretrizes dos frameworks: linguagem funcional subordinada à operação comunicativa e ao produto da aula.

### 2.14 Garantir áudio principal estável

Falha observada: A aula de Listening depende de síntese e disponibilidade de vozes do navegador, o que pode alterar identidade, sotaque, ritmo e distinção entre participantes.

Correção obrigatória: Use arquivo de áudio principal estável e testado entre dispositivos. Se síntese do navegador permanecer, identifique-a somente como fallback e não como fonte avaliativa principal. Garanta distinção consistente entre as vozes e funcionamento sem depender de configuração local.

Base nos documentos: Diretrizes de Produção e Prompt Controlador: áudio avaliativo estável; síntese variável apenas como fallback declarado.

### 2.15 Reescrever as Teacher’s Notes em tom operacional

Falha observada: As notas usam formulações enfáticas ou editoriais, como “NÃO ajude”, “force a resposta” e “TEM de responder”.

Correção obrigatória: Mantenha o idioma atual, pois os documentos não fixam idioma. Reescreva as notas para orientar ação, timing, interação, evidência esperada e apoio condicional. Diferencie procedimento obrigatório de opção de scaffolding. Retire justificativas editoriais e comandos agressivos.

Base nos documentos: Diretrizes de Produção: notas operacionais, escaneáveis, centradas na condução e com apoio condicional claramente identificado.

### 2.16 Executar validação global comprovada

Falha observada: O lote contém metadados residuais, ordem divergente, referências impossíveis, instrução de áudio em Reading e mecânicas repetidas — sinais de validação apenas local.

Correção obrigatória: Após corrigir, faça auditoria cruzada de perfil, syllabus, arquivo principal e quatro aulas. Não declare apenas que validou: entregue uma matriz final com item verificado, arquivo/trecho revisado, resultado e correção aplicada. Nenhum item pode ficar como “corrigido” sem evidência localizável.

Base nos documentos: Prompt Controlador: validação final do artefato, do ciclo e dos resíduos, com evidência da correção.

## 3. Procedimento obrigatório de revisão

Defina e registre a ordem oficial das quatro aulas antes de editar qualquer referência interna.

Reconstrua o perfil nos 14 campos, separando fatos, dados ausentes e hipóteses a validar.

Produza o syllabus provisório completo de 20 aulas, com aulas 5–20 explicitamente ajustáveis após o checkpoint.

Crie uma matriz diagnóstica do bloco Build: evidência pretendida por aula, habilidade/operação observada e tipo de apoio.

Revise os quatro frameworks em conjunto para eliminar sobreposição de função, conteúdo e produto.

Mapeie as mecânicas de todas as atividades e substitua repetições imediatas da mesma combinação.

Faça auditoria de coerência de cada slide e de cada nota: ação, mídia, resposta, chave, timing e interação.

Teste o áudio principal e os elementos interativos em condições estáveis.

Faça auditoria global de metadados, nomes, ordem, dependências e resíduos de template.

Entregue os artefatos corrigidos acompanhados da matriz de comprovação descrita na seção 6.

## 4. Critérios de aceite do lote corrigido

☐ O perfil apresenta os 14 campos e não transforma hipótese em fato.

☐ O syllabus mostra as 20 aulas e diferencia o bloco Build das aulas 5–20 ajustáveis.

☐ Há uma única ordem oficial, sem divergência de numeração ou referência temporal.

☐ As quatro primeiras aulas ensinam e produzem evidências diagnósticas distribuídas.

☐ Cada framework preserva sua função, operação e produto próprios.

☐ Grammar e ESP não sistematizam extensamente o mesmo conteúdo.

☐ A rotação altera a ação cognitiva/comunicativa, não apenas widget ou aparência.

☐ Tela, mídia, nota, chave e ação do professor estão alinhadas em todos os estágios.

☐ Predictions não antecipam as respostas do input.

☐ O áudio principal é estável; qualquer síntese variável está declarada como fallback.

☐ Teacher’s Notes estão operacionais e sem tom enfático, independentemente do idioma.

☐ Não existem resíduos de outro perfil, curso, quantidade de aulas ou versão.

☐ Os tempos somam 55 minutos de percurso essencial e preservam 5 minutos de margem.

## 5. Formato obrigatório da entrega

Entregue: (1) perfil corrigido; (2) syllabus provisório de 20 aulas; (3) arquivo principal corrigido; (4) quatro aulas corrigidas; e (5) matriz de comprovação da revisão.

Não entregue: apenas uma explicação sobre o que deveria mudar, uma lista genérica de conformidade ou declarações sem alteração localizável nos artefatos.

| Item verificado | Onde estava a falha | Correção aplicada | Evidência no arquivo final |
|---|---|---|---|
| [preencher] | [preencher] | [preencher] | [preencher] |
| [preencher] | [preencher] | [preencher] | [preencher] |

## 6. Comando final ao gerador

| EXECUTE A REVISÃO. Aplique todas as correções obrigatórias ao lote completo, preserve os elementos já adequados e não introduza os requisitos excluídos na seção 3. Antes de finalizar, confira cada critério de aceite e preencha a matriz de comprovação com referências localizáveis nos artefatos corrigidos. |
|---|

