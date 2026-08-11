# Diretrizes De Produção

> **Fonte:** `03_Diretrizes_de_Producao_Automatica.docx`, entregue pelo Dan em **11/08/2026**. Cabecalho do proprio
> documento: *"Private Black Adults · Documento normativo consolidado · Agosto de 2026"*.
>
> **Transcricao fiel**, extraida do XML do `.docx` (`word/document.xml`). Nada foi
> acrescentado, resumido nem interpretado; a unica mudanca e a formatacao em Markdown
> (tabelas e titulos). Esta copia existe para que o molde possa **citar a fonte** de cada
> ajuste sem depender de um arquivo em `~/Downloads`.
>
> As regras da producao automatica: ordem, especificacao, mecanicas, tom, fontes e validacao.
>
> **Documentos irmaos:** `docs/NORMATIVO-planejamento-aulas-2026-08.md` (o .docx de planejamento) · `docs/NORMATIVO-arquitetura-frameworks-2026-08.md` (a apresentacao de 16 slides) · `docs/NORMATIVO-estrutura-frameworks-2026-08.md` · `docs/NORMATIVO-prompt-controlador-2026-08.md` · `docs/INSTRUCAO-CORRETIVA-stephanie-2026-08.md`.
>
> **Onde isto virou codigo:** `_build/model/ciclo.json` (`microciclo_guided_discovery`, `tom_didatico`,
> `validacao_tres_camadas`), `_build/{slug}/syllabus.json` (a ficha de especificacao e as mecanicas
> por aula) e `scripts/relatorio_validacao.py` (a matriz de validacao por camada).

---

Regras estruturais para geração automática, tom didático, mecânicas e validação

Private Black Adults · Documento normativo consolidado · Agosto de 2026

| Escopo — Este documento regula a produção automática de lesson plans e HTML. Ele deve ser lido em conjunto com a Estrutura dos Frameworks e com o estado do aluno/ciclo. |
|---|

## 1. Ordem obrigatória de produção

Validar suficiência dos dados de entrada.

Construir uma especificação pedagógica da aula.

Selecionar e aplicar somente o framework pertinente.

Escolher conteúdo, fontes e mecânicas.

Redigir primeiro a arquitetura pedagógica e depois o HTML.

Executar validações pedagógica, linguística, factual, técnica e de artefato.

Entregar o arquivo apenas quando as checagens forem comprovadas.

## 2. Especificação pedagógica obrigatória

| Campo | Pergunta de controle |
|---|---|
| Necessidade prioritária | Qual necessidade do perfil esta aula atende? |
| Framework | Por que este framework é o mais adequado? |
| Operação nova | O que o aluno fará que não repetirá a aula anterior? |
| Origem da necessidade | Perfil, evidência de aula, evento futuro ou hipótese diagnóstica? |
| Conteúdo recuperado | O que será retomado sem reapresentação extensa? |
| Conteúdo excluído | O que pertence a outro framework ou já está consolidado? |
| Produto final | Qual performance observável encerra a aula? |
| Critérios de sucesso | Que comportamentos ou resultados serão registrados? |
| Retask | Que parte poderá ser repetida após feedback? |

## 3. Regras estruturais transversais

Guided Discovery precisa conter evidência suficiente; uma pergunta genérica não o constitui.

A progressão interna tende a: compreender/identificar → escolher → reformular/usar com apoio → produzir → retask.

Uma etapa pode ter um exercício, duas fases relacionadas ou interação sem slide; não há número universal de slides.

O percurso essencial deve totalizar 55 minutos e preservar 5 minutos de margem.

Uma aula tem uma produção principal; atividades anteriores a alimentam.

O feedback seleciona pontos de alto impacto e usa formulações reais do aluno quando disponíveis.

O retask repete apenas o trecho que se beneficia do feedback e é decidido com critério observável.

Hipóteses sobre o aluno aparecem como cenário fictício ou item a validar.

A instrução na tela, a teacher’s note, o answer key e os turnos do professor devem exigir as mesmas ações.

Teacher’s notes contêm condução, respostas, apoio condicional e evidência a registrar; justificativa editorial pertence às diretrizes.

## 4. Banco de dinâmicas e mecânicas

Mecânica é a forma operacional; função é o trabalho cognitivo/comunicativo. A mesma mecânica pode aparecer em frameworks diferentes desde que objeto, função, complexidade e evidência mudem.

| Mecânica | Usos legítimos | Cuidados |
|---|---|---|
| Matching | Forma–função, fala–intenção, ideia–evidência, etapa–resultado. | Evitar pares óbvios; incluir uso posterior. |
| Multiple choice | Gist, interpretação, adequação, melhor formulação. | Distratores plausíveis e uma resposta defensável. |
| Sorting | Categorias semânticas, status, atitude, registro. | Categorias funcionalmente relevantes. |
| Fill in the blanks | Noticing seletivo ou scaffold para produção. | Não transformar aula em manipulação de forma. |
| True/False + correction | Checagem de evidência e correção de leitura/escuta. | Exigir localização ou correção. |
| Ordering/reconstruction | Sequência, organização discursiva, agenda, processo. | Itens devem sustentar produto posterior. |
| Rephrasing | Adequação, precisão, diplomacia, mudança de registro. | Aceitar múltiplas respostas válidas. |
| Information gap | Perguntar, esclarecer e integrar informação. | Lacuna genuína; turnos definidos. |
| Case/decision | Analisar alternativas e justificar escolha. | Critérios claros e dados suficientes. |
| Role-play/simulation | Realizar ação realista com interlocutor. | Papel, objetivo, dificuldade e resultado explícitos. |
| Replay/retask | Aplicar feedback a trecho focalizado. | Não repetir tarefa inteira automaticamente. |

## 4.1 Controle e sequenciamento

| Grau | Característica | Exemplos |
|---|---|---|
| Controlado | Uma resposta defensável; processamento preciso. | Matching, MCQ, ordering, seleção de evidência. |
| Semiaberto | Escolha, justificativa, reformulação ou personalização limitada. | Complete-and-use, rephrase-and-say, sort-and-explain. |
| Aberto | Aluno escolhe conteúdo e linguagem para alcançar um resultado. | Briefing, conversa, decisão, negociação, apresentação. |

Quando houver duas práticas consecutivas, elas devem usar operações e graus de controle diferentes. A antiga regra fixa “Categoria A no slide 1 + Categoria B no slide 2” é uma opção de desenho, não uma obrigação universal.

## 4.2 Rotação sem variedade artificial

Registrar mecânica, função, operação cognitiva, controle e evidência.

Evitar repetição imediata da mesma combinação, sobretudo dentro de um bloco.

Permitir repetição deliberada quando reduz carga cognitiva, permite comparação ou atende acessibilidade.

Nunca trocar apenas o widget mantendo a mesma operação e chamar isso de variedade.

## 5. Tom didático

| Para o aluno | Para o professor |
|---|---|
| Adulto, direto, respeitoso e orientado a ação. | Operacional, escaneável e centrado no que fazer. |
| Desafiador sem linguagem ameaçadora. | Não interromper produção salvo perda completa de comunicação. |
| Apoio disponível sem infantilização. | Aceitar respostas plausíveis e registrar evidências. |
| Cenários realistas, mas claramente fictícios quando inventados. | Distinguir apoio condicional de procedimento obrigatório. |
| Instruções curtas: verbo de ação + produto esperado. | Separar answer key, possíveis respostas e critério diagnóstico. |

## 6. Materiais, fontes e factualidade

Preferir fontes autênticas quando agregarem valor real à operação da aula.

Verificar existência, autoria, data, trecho e estatuto documental.

Garantir que cada resposta-modelo seja sustentada pelo material apresentado ao aluno.

Distinguir fato, inferência e simulação; marcar cada um.

Não confundir anúncio, proposta, confirmação, entrada em vigor e resultado posterior.

Manter material consultável durante tarefas que exigem atribuição ou precisão.

Para listening avaliativo, usar arquivo estável; síntese variável do navegador apenas como fallback declarado.

## 7. Diferenciação por nível e perfil assimétrico

O nível deve parametrizar extensão, densidade, velocidade, abstração, autonomia, apoio e evidência — não apenas vocabulário. Input e output podem ter níveis diferentes. Um aluno B1+ na fala e B2 na compreensão pode receber material B2 com frames produtivos B1+/B2.

## 8. Validação obrigatória

| Camada | Checagens mínimas |
|---|---|
| Entrada/perfil | Campos completos; hipóteses marcadas; restrições respeitadas. |
| Framework | Etapas cumprem funções; produto coerente; fronteiras preservadas. |
| Progressão | Operações não duplicadas; controle reduzido; tempo suficiente para produção. |
| Ciclo | Conteúdo anterior recuperado sem reensino; nova operação; mecânicas registradas. |
| Linguagem | Correção, naturalidade, nível, variedade e coerência entre modelos/gabaritos. |
| Factual | Fonte, data, evidência, temporalidade e inferências. |
| Coerência interna | Tela, teacher’s note, resposta esperada e papel do professor alinhados. |
| Técnica | Áudio, links, widgets, navegação, responsividade e acessibilidade. |
| Artefato final | Cards, summaries, scripts, answer keys e notas sem resíduos de versões. |
| Relatório | Cada alegação de ajuste é confrontada com o HTML entregue. |

## 8.1 Regra de aprovação

| Gate — “Aplicado” só pode ser declarado após verificação literal no artefato final. Falha parcial deve aparecer como parcial; item não verificado deve aparecer como pendente. O autor não pode certificar a própria intenção como resultado. |
|---|

## 9. Saídas do gerador

Especificação pedagógica interna.

Lesson plan/HTML executável.

Registro atualizado do estado do aluno e das mecânicas.

Relatório de validação por camada, com evidência concreta.

Lista explícita de pendências ou decisões editoriais quando houver.

