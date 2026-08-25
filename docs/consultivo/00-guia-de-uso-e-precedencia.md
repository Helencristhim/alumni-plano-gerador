> **Documento normativo importado do Drive — nao editar aqui.**
> Origem: `00_Guia_de_Uso_e_Precedencia_6_Documentos.docx`
> Drive ID: `1NTbdDL6LoYrtYgPp93gHvY6z7ajhrl9q`
> Modificado no Drive: 2026-08-24
> Reimportar: `python3 scripts/consultivo/docx_to_md.py <arquivo.docx> docs/consultivo/00-guia-de-uso-e-precedencia.md`
> A fonte e o .docx. Divergencia entre este arquivo e o Drive se resolve reimportando, nunca editando o .md.

## 00 · GUIA DE USO E PRECEDÊNCIA

**Núcleo pedagógico oficial — Private Class Alumni Black · adultos · A1–C1**
**Versão consolidada · 20 de agosto de 2026 · independente de plataforma e de aluno**

### 1. Finalidade

Este guia define qual conjunto deve ser entregue a qualquer gerador para criar, revisar ou validar perfil, syllabus, aula e ciclo. Os documentos 01–05 formam a referência normativa de governança. O documento 06 consolida e operacionaliza esse núcleo para a geração.

**Composição vigente.** Na versão vigente, o núcleo pedagógico validado compreende os documentos 00–06. A criação futura de documentos numerados posteriormente é possível quando deliberadamente aprovada e acompanhada da atualização do índice, da composição do pacote e das referências cruzadas deste guia. A Série P reúne especificações de plataforma externas ao núcleo pedagógico.

Nenhum arquivo isolado substitui o conjunto quando o gerador estiver sendo configurado do zero. Para produzir uma aula depois da configuração, o gerador também recebe o perfil, o syllabus vigente, o estado pedagógico e a solicitação da aula.

### 2. Pacote obrigatório

| Ordem | Documento | Função |
|---|---|---|
| **00** | **Guia de Uso e Precedência** | Define o pacote, a ordem de leitura, a precedência e o que fica fora dele |
| **01** | **Perfil do Aluno** | Define o esquema único dos 14 campos, o estatuto das informações e, separadamente, a governança da avaliação |
| **02** | **Syllabus do Ciclo** | Converte o perfil em vinte aulas organizadas em cinco blocos |
| **03** | **Estrutura dos Frameworks** | Define identidade, fronteiras, organização por etapas, parâmetros de tempo e mecânicas dos quatro frameworks |
| **04** | **Planejamento e Produção da Aula** | Define pre-class, in-class, post-class, tom, American English, Teacher’s Guide, fontes e validação |
| **05** | **Ciclo de Evolução** | Define estado pedagógico, checkpoints, avaliação e decisão de progressão |
| **06** | **Prompt Controlador Pedagógico Único** | Consolida os parâmetros CEFR, orquestra a produção e valida a entrega |

### 3. Ordem de leitura

Para configurar um gerador novo: **00 → 01 → 02 → 03 → 04 → 05 → 06**.

Para produzir uma aula depois da configuração: aplicar o **06** e fornecer como entradas o perfil estruturado conforme o **01**, o syllabus vigente conforme o **02** e o estado pedagógico conforme o **05**. Os documentos **03 e 04** permanecem como referência de auditoria, manutenção e resolução de dúvida.

### 4. Ordem de precedência

Quando duas instruções colidirem, vence a que estiver mais alta. Conflito sem precedência clara deve ser declarado, nunca resolvido silenciosamente.

- decisão explícita do operador para o caso;
- perfil e restrições do aluno;
- evidência real e estado pedagógico vigente;
- syllabus vigente;
- estrutura dos frameworks;
- parametrização CEFR normativa;
- planejamento e diretrizes de produção;
- Prompt Controlador;
- especificação técnica ou visual da plataforma.

Uma decisão técnica nunca modifica silenciosamente uma regra pedagógica.

### 5. Estatuto do núcleo validado

Por ora, os seis documentos 01–06 constituem integralmente o conjunto validado.

- A parametrização CEFR necessária à geração está consolidada no Documento 06.
- As escalas transversais e regras estruturais permanecem nos Documentos 03 e 04.
- Cada um dos quatro frameworks possui oito etapas pedagógicas normativas, com nomes, funções e ordem definidos no Documento 03. O nível, a rota aplicável e a saída pedagógica parametrizam conteúdo, apoio, complexidade, mecânicas e produto, mas não eliminam, acrescentam ou reordenam essas etapas. A quantidade de slides, telas, páginas ou cartões é variável e não se confunde com a quantidade de etapas.
- A governança da avaliação adota exatamente um de dois modelos: **avaliação formal com teste** ou **acompanhamento docente**, com eventual instrumento de consolidação. Em ambos, a decisão final cabe ao professor e a autoavaliação é apenas complementar.

Fallback normativo. Quando não houver escolha explícita registrada, aplicar Acompanhamento docente. A ausência de valor não autoriza deixar o modelo indefinido, presumir avaliação formal ou criar teste. Somente decisão explícita posterior autoriza a mudança para Avaliação formal com teste.

Rotas e variações somente se aplicam quando estiverem previstas no framework, na parametrização por nível ou na saída pedagógica vigente; não podem ser introduzidas por documento externo ou banco provisório não validado.

Nenhum documento externo a essa composição integra o núcleo ou deve ser tratado como fonte normativa.

Regra de entrega final. A produção publicada gera duas URLs distintas: a URL do professor contém a visão docente e a prévia da visão do aluno; a URL do aluno contém exclusivamente a visão do aluno. Conteúdo docente não pode estar apenas oculto: não integra o arquivo, o HTML, o payload, o estado ou os recursos entregues pela URL do aluno.

### 6. Regra de fronteira com a plataforma

Se uma regra deixa de fazer sentido quando o meio de entrega muda, ela é requisito de plataforma. Se sobrevive à troca de meio, ela é pedagógica.

Por isso, não pertencem ao núcleo pedagógico: interface, layout, navegação, abertura de painéis, formato de arquivo, autenticação, armazenamento, pipeline de imagens e implementação técnica de áudio.

### 7. Entradas obrigatórias para produzir uma aula

Além do guia e dos seis documentos validados, fornecer:

- perfil estruturado nos 14 campos do Documento 01, acompanhado da governança da avaliação; na ausência de escolha explícita, registrar Acompanhamento docente como modelo vigente;
- syllabus vigente de 20 aulas;
- estado pedagógico acumulado e evidências anteriores;
- número, bloco, framework e objetivo da aula;
- nível receptivo e produtivo;
- modalidade e duração;
- restrições, materiais obrigatórios e conteúdos proibidos;
- especificação separada do meio de entrega, incluindo o modo — protótipo ou produção final — e, na produção final, as duas saídas distintas de professor e aluno.

Informação ausente não pode ser inventada. Dado materialmente necessário deve ser solicitado; ausência não bloqueante deve ser registrada como hipótese.

### 8. Saídas obrigatórias por aula

- especificação pedagógica;
- pre-class;
- Student Material do in-class;
- Teacher’s Notes locais;
- Teacher’s Guide completo em inglês;
- answer key e possible answers;
- post-class;
- relatório de validação;
- atualização proposta do estado pedagógico, separando observação de hipótese.

Todo conteúdo produzido ou editado em inglês usa **American English**, conforme o Documento 04. Fontes externas autênticas preservam sua variedade original.

### 9. Controle de versão

Os documentos 00–06 formam uma única versão. Uma alteração normativa deve atualizar o documento responsável, o Prompt Controlador e este guia quando afetar precedência, entrada, saída ou composição do pacote.
