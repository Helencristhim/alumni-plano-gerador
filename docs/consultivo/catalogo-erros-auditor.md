> **Documentacao de apoio importada do Drive — nao editar aqui.**
> Origem: `catalogo_erros_recorrentes_auditor_private_black_2026-09-04.xlsx`
> Drive ID: `1wyvs0gsGxHwkHQnoKbrehMBUkDkwg97e`
> Modificado no Drive: 2026-09-04
> Reimportar: conector do Drive (`read_file_content` com o fileId acima).
> A fonte e a planilha no Drive. Divergencia entre este arquivo e ela se resolve
> reimportando, nunca editando o .md.
>
> **Estatuto.** O relatorio de alteracoes normativas classifica o catalogo como
> *documentacao de apoio*, nao como documento normativo — os 16 normativos estao no
> `README.md`. Ele entra no repo porque e a fonte dos IDs que os gates citam: quando o
> `check_preclass_nao_entrega.py` diz PRO-006, e daqui que o codigo vem.

# Catálogo de erros recorrentes — Auditor Private Black Adults

Base consolidada dos 14 documentos vigentes, decisões posteriores e falhas comprovadas em
artefatos. Refinamento do registro pós-aula incorporado em 02/09/2026; REG-004 e REG-005
ampliados em 04/09/2026.

## Cobertura

| Indicador | Total |
| :-: | :-: |
| Erros catalogados | **85** |
| BLOCKER | 57 |
| MAJOR | 28 |
| Comprovados em testes | 67 |

| Categoria | Quantidade |
| :-: | :-: |
| Integridade | 20 |
| Anatomia | 21 |
| Processo | 21 |
| Sequência | 8 |
| Regressão | 9 |
| Autorização | 5 |
| Auditor | 1 |

**Leitura do campo Origem.** *Comprovado* = falha já encontrada em artefato ou rodada de QA;
é obrigatória como teste de regressão. *Derivado* = modo de falha diretamente invertido de
regra normativa; exige mutation test antes de ativar o bloqueio. A presença da regra na
lista **não** comprova que o teste já foi implementado: catálogo, mutation test e bloqueio
ativo são coisas distintas.

## Integridade (INT)

| ID | Erro recorrente | Manifestação auditável | Sev. | Origem |
| :-: | :-: | :-: | :-: | :-: |
| INT-001 | Contaminação de aluno | O artefato contém nome, dados, contexto ou objetivo pertencente a outro aluno. | BLOCKER | Comprovado |
| INT-002 | Contaminação de ciclo | Aparecem números de aula, bloco, checkpoint ou decisões de outro ciclo sem identificação explícita. | BLOCKER | Comprovado |
| INT-003 | Contaminação de versão | Tela, mídia, resposta, rationale, Possible Answers e Teacher's Guide pertencem a versões diferentes. | BLOCKER | Comprovado |
| INT-004 | Perfil tratado como diagnóstico | Hipótese inicial, autorrelato ou ocorrência isolada é apresentada como fato confirmado. | BLOCKER | Comprovado |
| INT-005 | Nível sem base | Nível geral ou por habilidade informado sem origem, amostra ou qualificador de estimativa. | BLOCKER | Derivado |
| INT-006 | Generalização entre habilidades | Evidência de uma habilidade usada para concluir nível nas demais. | BLOCKER | Comprovado |
| INT-007 | Preferência ou causa inventada | Preferência, dificuldade, experiência ou condição preenchida por inferência como fato. | BLOCKER | Comprovado |
| INT-008 | Informação ausente preenchida | Dado materialmente necessário é inventado em vez de solicitado. | BLOCKER | Derivado |
| INT-009 | Repertório dominado sem evidência | Conteúdo entra no campo de exclusão com base apenas em exposição ou autorrelato. | MAJOR | Comprovado |
| INT-010 | Conteúdo anterior genérico | Planejamento lista linguagem anterior sem origem, evidência, decisão e forma de retomada. | MAJOR | Comprovado |
| INT-011 | Retomada como repetição | Conteúdo anterior reaparece na mesma operação, sem mudança de interlocutor, pressão ou contexto. | MAJOR | Comprovado |
| INT-012 | Objetivo sem evidência | Objetivo comunicativo sem tarefa capaz de gerar a evidência declarada. | BLOCKER | Comprovado |
| INT-013 | Evidência sem impacto | Ponto a validar é coletado sem decisão prevista para confirmar ou descartar a hipótese. | MAJOR | Derivado |
| INT-014 | Autoavaliação como prova | Confiança do aluno usada isoladamente para comprovar desempenho. | BLOCKER | Derivado |
| INT-015 | Contradição entre seções | Perfil, syllabus, cards, aula, guia ou estado declaram objetivos, nível ou duração incompatíveis. | BLOCKER | Comprovado |
| INT-016 | Conflito normativo resolvido silenciosamente | O gerador escolhe uma das instruções conflitantes sem registrar o conflito e a precedência. | BLOCKER | Comprovado |
| INT-017 | Etapas confundidas com slides | O artefato altera a quantidade de etapas porque mudou de slides, ou trata slide como sinônimo de etapa. | BLOCKER | Comprovado |
| INT-018 | Metadado interno ou observação editorial expostos | Códigos de hipótese, notas do gerador ou observações metalinguísticas aparecem na interface. Inclui anunciar que a escala de Desempenho é a "mesma nas quatro aulas do bloco". | BLOCKER | Comprovado |
| INT-019 | Atualização parcial após mudança estrutural | Objetivo, produto, etapa ou condição é corrigido na superfície principal, mas mapa, card, guia, Answer Key ou pre/post-class mantêm a versão anterior. | BLOCKER | Comprovado |
| INT-020 | Fonte editável duplicada ou superfícies vinculadas divergentes | O mesmo foco, decisão ou formulação possui fontes editáveis independentes, ou superfícies multilíngues do mesmo registro divergem em ação, intervalo ou consequência. | BLOCKER | Comprovado |

## Anatomia (ANA)

| ID | Erro recorrente | Manifestação auditável | Sev. | Origem |
| :-: | :-: | :-: | :-: | :-: |
| ANA-001 | Perfil fora dos 14 campos | Campos omitidos, fundidos de forma destrutiva ou substituídos. | BLOCKER | Comprovado |
| ANA-002 | Avaliação indefinida ou presumida | Ausência de escolha deixa o modelo vazio, presume teste ou cria terceiro modelo. | BLOCKER | Comprovado |
| ANA-003 | Ciclo diferente de 20 aulas | Syllabus regular não apresenta 20 aulas ou mistura horizonte de ciclos. | BLOCKER | Comprovado |
| ANA-004 | Diagnóstico inicial incompleto | Aulas 1–4 não cobrem Reading, Listening, Grammar e Personalized Real-World English uma vez cada. | BLOCKER | Derivado |
| ANA-005 | Distribuição pós-aula 4 tratada como fixa | Aulas 5–20 apresentadas como grade imutável, sem dependência das evidências. | BLOCKER | Comprovado |
| ANA-006 | Produção antecipada de blocos | O gerador produz blocos futuros em vez de apenas o bloco vigente. | BLOCKER | Comprovado |
| ANA-007 | Etapas declaradas ausentes ou fora de ordem | Uma etapa prevista não aparece ou sua função é deslocada. | BLOCKER | Derivado |
| ANA-008 | Estrutura fixa de oito etapas não preservada | Um framework omite, acrescenta, funde, reordena ou descaracteriza uma das oito etapas. | BLOCKER | Comprovado |
| ANA-009 | Duração essencial incorreta | Tempos declarados não totalizam 55 minutos ou reduzem produção/feedback essenciais. | BLOCKER | Comprovado |
| ANA-010 | Pre-class fora da anatomia ou sem apoio proporcional | Não cumpre seis atividades e 15–20 min, não antecipa vocabulário, ou o apoio em português é insuficiente apesar do mínimo numérico. | MAJOR | Comprovado |
| ANA-011 | In-class dependente do pre-class | A aula pressupõe resposta ou conclusão do pre-class para funcionar. | BLOCKER | Comprovado |
| ANA-012 | Áudio em pre-class de framework não Listening | Pre-class de Reading, Grammar ou Personalized Real-World English introduz listening sem autorização funcional. | MAJOR | Derivado |
| ANA-013 | Post-class transformado em exercício obrigatório | Reading, Listening/Watching ou Language Reference contém quiz, tarefa ou exigência de consumo. | BLOCKER | Comprovado |
| ANA-014 | Post-class sem componentes mínimos | Banco não oferece ao menos Reading, Listening/Watching e apoio linguístico. | MAJOR | Derivado |
| ANA-015 | Reading e Language Reference duplicados | O mesmo recurso/operação repetido nas duas categorias sem mudança funcional. | MAJOR | Comprovado |
| ANA-016 | Teacher's Guide externo fora da organização vigente | Falta orientação necessária, repete bloco geral, recria overview ou deixa espaço reservado fora do primeiro slide. | BLOCKER | Comprovado |
| ANA-017 | Answer Key na camada errada ou com condução oral | Gabarito antes da correção autorizada, ausente na visão docente, divergente da atividade, ou com comandos ao professor em atividade assíncrona. | BLOCKER | Comprovado |
| ANA-018 | Card de checkpoint sem comandos operacionais | Cards 04/08/12/16/20 não orientam revisar antes e atualizar depois o Estado pedagógico. | MAJOR | Derivado |
| ANA-019 | Tentativa diagnóstica sem apoio operacional | A ausência de modelo vira tela vazia; faltam situação, papéis, quem inicia ou condição de conclusão. | BLOCKER | Comprovado |
| ANA-020 | Round 2 do Personalized Real-World English tratado como opcional | A etapa 7 vira menu para decidir se haverá continuidade, ou a etapa 8 pode ser omitida. | BLOCKER | Comprovado |
| ANA-021 | Lesson overview fora da composição definitiva | Overview fora do primeiro slide, aberto por padrão, reaberto na navegação, com número diferente de cinco seções, ou com fonte editável independente. | BLOCKER | Derivado |

## Processo (PRO)

| ID | Erro recorrente | Manifestação auditável | Sev. | Origem |
| :-: | :-: | :-: | :-: | :-: |
| PRO-001 | Guided Discovery nominal | A atividade apresenta regra/modelo diretamente ou pede inferência a partir de um único exemplo. | BLOCKER | Comprovado |
| PRO-002 | Ajuda revela resposta antes da tentativa | Explicação, tradução, apoio ou pista acessível antes da tentativa antecipa a resposta ou substitui a operação cognitiva. | MAJOR | Comprovado |
| PRO-003 | Pronúncia rotulada como descoberta sem contraste | Drilling/model/repetition aparece como Guided Discovery sem evidência auditiva comparável. | MAJOR | Comprovado |
| PRO-004 | Modalidade principal indefinida | Noticing mistura texto e áudio sem declarar qual evidência sustenta a decisão. | MAJOR | Comprovado |
| PRO-005 | Áudio duplicativo | Áudio apenas lê o que já está visível, sem contraste, confirmação posterior ou função própria. | MAJOR | Comprovado |
| PRO-006 | **Transcript liberado cedo** | Em listening contrast, transcript aparece antes da tentativa ou da escuta que precisa ser puramente auditiva. | BLOCKER | Comprovado |
| PRO-007 | Player separado da alternativa | Rótulo, player e controle de seleção não estão no mesmo card. | MAJOR | Comprovado |
| PRO-008 | Referência posicional frágil | Instrução usa first/second/left/right/above quando há rótulos estáveis ou o layout pode mudar. | MAJOR | Comprovado |
| PRO-009 | **Sorting não embaralhado** | Itens aparecem agrupados pela categoria ou na ordem da resposta, tornando a classificação previsível. | MAJOR | Comprovado |
| PRO-010 | Instrução redundante, contraditória ou checklist indevido | Tela repete comandos, descreve outra operação, diverge do guia, ou transforma o closing em checklist obrigatório. | MAJOR | Comprovado |
| PRO-011 | Verbo sem ação correspondente | Prompt manda open/reveal/select/listen/submit quando a interface não oferece esse estado ou ação. | BLOCKER | Comprovado |
| PRO-012 | Produção com input novo excessivo | Transferência final introduz vocabulário ou cenário não apoiado que passa a determinar o sucesso. | BLOCKER | Comprovado |
| PRO-013 | Produção desalinhada ao objetivo | Aluno executa operação diferente, inferior ou mais ampla que o objetivo declarado. | BLOCKER | Comprovado |
| PRO-014 | Role-play automático | Speaking/Interaction traduzido sempre em simulação ou professor como interlocutor, sem necessidade funcional. | MAJOR | Comprovado |
| PRO-015 | Possible Answers prescritivas ou ausentes | Prática apoiada recebe resposta única rígida, ou falta apoio quando o professor pode precisar destravar a produção. | MAJOR | Comprovado |
| PRO-016 | Answer Key desproporcional | Tarefa fechada sem mapeamento exato; tarefa aberta com gabarito; produção sem critérios. | MAJOR | Comprovado |
| PRO-017 | Ação não executável no Teacher's Guide | O guia manda mostrar, retomar, comparar ou voltar a um elemento inexistente ou oculto no estado errado. | BLOCKER | Comprovado |
| PRO-018 | Recurso condicional fora do ponto de uso | Personagem, card ou apoio de rota adaptativa aparece antecipadamente em outra etapa, ainda que recolhido. | MAJOR | Comprovado |
| PRO-019 | Rótulo condicional antecipa a rota | O controle fechado revela personagem, condição ou material antes da seleção adaptativa. | MAJOR | Comprovado |
| PRO-020 | Metalinguagem técnica na interface A1/A2 | A interface exige que o aluno compreenda termos como react, repair ou retask para executar a tarefa. | MAJOR | Derivado |
| PRO-021 | Prompt comum falso para uma variante | Título ou instrução compartilhada pressupõe repetição, mas uma rota autorizada realiza transferência. | BLOCKER | Comprovado |

## Sequência (SEQ)

| ID | Erro recorrente | Manifestação auditável | Sev. | Origem |
| :-: | :-: | :-: | :-: | :-: |
| SEQ-001 | Frameworks diagnósticos fora da ordem | Aulas 1–4 não seguem Reading → Listening → Grammar → Personalized Real-World English quando essa é a ordem vigente. | BLOCKER | Comprovado |
| SEQ-002 | **Descoberta após clarificação** | A regra/MPF é apresentada antes da tentativa de noticing ou descoberta. | MAJOR | Derivado |
| SEQ-003 | Produção antes do apoio previsto | Tarefa comunicativa exige linguagem ainda não trabalhada, salvo diagnóstico explícito. | BLOCKER | Comprovado |
| SEQ-004 | Feedback sem retask quando previsto | A produção recebe correção sem nova oportunidade de uso quando a rota exige retask. | MAJOR | Derivado |
| SEQ-005 | Transcript e resposta fora de ordem | Transcript/rationale antes da escolha; ou resposta sem explicação e novo teste. | BLOCKER | Comprovado |
| SEQ-006 | Checkpoint consultado tarde | Card de aula final de bloco não orienta consulta antes e consolidação depois. | MAJOR | Derivado |
| SEQ-007 | Bloco seguinte definido antes do checkpoint | Distribuição, apoios ou objetivos futuros fechados antes das evidências da quarta aula. | BLOCKER | Derivado |
| SEQ-008 | Foco redefinido no Round 2 | O feedback registra um foco e o Round 2 pede nova escolha ou aplica foco diferente sem nova evidência. | MAJOR | Comprovado |

## Regressão (REG)

| ID | Erro recorrente | Manifestação auditável | Sev. | Origem |
| :-: | :-: | :-: | :-: | :-: |
| REG-001 | **Contagem divergente** | Título, lead, TG, gabarito ou conclusão declara quantidade diferente dos itens reais. | BLOCKER | Comprovado |
| REG-002 | Terminologia divergente | Personagens, versões, funções, alternativas ou stages mudam de nome entre tela, mídia e guia. | BLOCKER | Comprovado |
| REG-003 | Texto corrompido por patch | Ajuste mecânico remove, concatena ou injeta fragmentos de HTML no texto visível. | BLOCKER | Comprovado |
| REG-004 | Controle visual sem função ou rótulo incompatível | Botão, reset, finish, transcript, player ou confirmação não executa a ação prometida, ou mantém rótulo incompatível com a próxima ação — por exemplo Check quando o clique seguinte reinicia a atividade. | BLOCKER | Comprovado |
| REG-005 | Reset de atividade ou aula e confirmação de escrita incompletos | Redo mantém resposta ou devolutiva; Reset lesson limpa apenas o slide atual, preserva conclusão indevida, reaparece após recarga ou apaga dados fora do In-class ativo. Inclui Confirm response incompleto. | BLOCKER | Comprovado |
| REG-006 | Sobreposição ou corte visual | Texto, botões, players ou expansões se sobrepõem, são cortados ou extrapolam larguras suportadas. | BLOCKER | Comprovado |
| REG-007 | Hierarquia visual incorreta | Pergunta interna sem destaque próprio, ou pergunta de abertura com o estilo interno. | MAJOR | Comprovado |
| REG-008 | Persistência fictícia | Interface sugere salvar ou atualizar histórico, mas usa apenas estado local ou função inexistente. | BLOCKER | Comprovado |
| REG-009 | Dupla contagem da minutagem | Etapa distribuída em vários slides repete a duração em cada um, ou fechamento/replay fica fora da soma dos 55 minutos. | BLOCKER | Comprovado |

## Autorização (AUT) e Auditor (AUD)

| ID | Erro recorrente | Manifestação auditável | Sev. | Origem |
| :-: | :-: | :-: | :-: | :-: |
| AUT-001 | Student e Teacher no mesmo arquivo | Conteúdo docente ocultado por toggle/CSS, mas integrando HTML, payload, estado ou recursos da URL do aluno. | BLOCKER | Comprovado |
| AUT-002 | Produção fora do bloco autorizado | Gerador cria, altera ou publica aula/bloco não solicitado. | BLOCKER | Derivado |
| AUT-003 | Teste formal criado sem decisão | Material cria ou pressupõe teste sem escolha explícita por Avaliação formal com teste. | BLOCKER | Comprovado |
| AUT-004 | Áudio oficial por tecnologia proibida | Build final usa Web Speech API/speechSynthesis, ou chama ElevenLabs/expõe credenciais no navegador. | BLOCKER | Derivado |
| AUT-005 | Mídia ou dado não autorizado | Clonagem de voz, dado pessoal desnecessário, mídia fabricada ou fonte externa não validada. | BLOCKER | Derivado |
| AUD-001 | Montagem reprovada retorna código 0 ou contrato não decidido | O processo aceita montagem inválida ou escolhe silenciosamente qual código não zero representa reprovação. | BLOCKER | Comprovado |

## Decisões vigentes e exclusões obrigatórias

| Tema | Decisão vigente | Erro que não deve ser reintroduzido |
| :-: | :-: | :-: |
| Etapas | Cada framework possui oito etapas pedagógicas fixas, com funções, identidade e ordem definidas no Documento 03. | Confundir etapa com slide/tela; omitir, acrescentar, reordenar ou descaracterizar etapas porque a representação mudou. |
| Aulas 1–4 | Cobrem Reading, Listening, Grammar e Personalized Real-World English como diagnóstico real. | Tratar as quatro como teste sem aprendizagem, ou repetir modalidade. |
| Aulas 5–20 | Distribuição adaptativa por evidência; produção por bloco. | Fixar a distribuição inteira ou produzir todos os blocos antecipadamente. |
| Arquivos | Professor e aluno recebem saídas distintas; conteúdo docente não integra a entrega Student. | Arquivo único com toggle, ou TG apenas oculto. |
| Avaliação | Na ausência de escolha explícita, usar Acompanhamento docente. | Deixar indefinido, presumir teste formal ou criar terceiro modelo. |
| Answer Key | Preferir fonte única operacional; proporcional ao tipo de tarefa. | Interpretar fonte única como obrigação de esconder apoios docentes necessários. |
| Post-class | Reading/Listening/Watching/Language Reference são acervo autêntico; apenas speaking/writing são práticas opcionais. | Inserir exercícios de compreensão ou exigir consumo dos recursos. |
| Round 2 | A etapa 7 registra um foco observável; a etapa 8 realiza Round 2 obrigatório e aplica o mesmo foco. | Tratar retask/repetition/new task como menu para decidir se haverá Round 2; redefinir o foco na etapa 8. |
| Recursos adaptativos | Recurso condicional fica recolhido no ponto de uso; rótulo neutro antes da abertura. | Antecipar personagem/rota, decidir durante preparação ou duplicar o campo editável. |
| Minutagem | Os 55 minutos incluem todos os slides essenciais; a duração de uma etapa distribuída é contabilizada uma única vez. | Repetir a duração em cada slide ou excluir fechamento/replay da soma. |
| Teacher's Guide externo | Exatamente um Lesson overview, somente no primeiro slide, inicialmente recolhido, com cinco seções e botão de fechamento. | Repetir overview, usar Lesson-wide notes, deixar espaço residual ou criar outcome editável independente. |
| Códigos de saída | 0 é exclusivo de liberação; reprovação e erro são não zero. A distribuição entre 1 e 2 permanece **pendente**. | Escolher silenciosamente uma das convenções conflitantes. |
| Escala de Desempenho | A mesma escala nas quatro aulas do bloco, mas a interface mostra somente critério, descritores e controles. | Exibir a nota metalinguística sobre a uniformidade, ou remover a uniformidade estrutural porque a nota saiu. |
| Check/Redo e Reset lesson | Check nomeia a verificação; após verificar, o controle vira Redo. Reset lesson reinicia todo e somente o In-class da aula ativa e remove a conclusão. | Manter Check para uma ação de reset; limpar apenas o slide; restaurar respostas após recarga; apagar dados de outro escopo. |

## O que este repositório mede hoje

O `scripts/consultivo/check_catalogo_auditor.py` (GATE 41) implementa 17 destas regras — as
que é possível enunciar sem ambiguidade e provar com um caso plantado. As demais dependem
de comparar o material com algo que o repositório não tem (a consultoria, o que o aluno
disse) ou de julgar se a operação pedagógica mudou de fato, e continuam sendo trabalho de
leitura humana. Outros gates cobrem IDs específicos:

| ID do catálogo | Onde é medido |
| :-: | :-: |
| PRO-006, SEQ-002 | GATE 61 · `check_preclass_nao_entrega.py` |
| PRO-009 (banco de gap-fill) | GATE 62 · `check_atividade_fechada.py` + `embaralha()` no emissor |
| PRO-009 (match-grid) | GATE 41 · `check_catalogo_auditor.py` |
| REG-001 (enunciado × itens) | GATE 62 |
| REG-001 (fala prometida × áudio) | GATE 46 · `check_contagem_declarada.py` |
| REG-004, REG-005 | GATE 31 · `check_reset_completo.py` e o contrato do shell |
| INT-018 | GATE 51 · `check_voz_do_material.py` |
| AUT-001 | GATE 36 · `check_isolamento_aluno.py` e GATE 48 · `check_link_namespace.py` |
| AUT-004 | GATE 40 · `check_audio_oficial.py` |
| ANA-004, ANA-008, ANA-009 | GATE 41 e GATE 37 · `validate_consultivo.py` |
| PRO-011 (parte) | GATE 63 · `check_instrucao_da_tela.py` |
