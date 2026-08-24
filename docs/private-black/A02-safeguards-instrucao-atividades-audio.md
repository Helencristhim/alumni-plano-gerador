> **Documento normativo importado do Drive — nao editar aqui.**
> Origem: `A02_Safeguards_de_Instrucao_Atividades_e_Audio.docx`
> Drive ID: `1jY0HC2k_QNrTGdPDkJsIQLtqX-2TPdqU`
> Modificado no Drive: 2026-08-21
> Reimportar: `python3 scripts/black/docx_to_md.py <arquivo.docx> docs/private-black/A02-safeguards-instrucao-atividades-audio.md`
> A fonte e o .docx. Divergencia entre este arquivo e o Drive se resolve reimportando, nunca editando o .md.

## ADENDO NORMATIVO 02

**Safeguards de instrução, atividades e áudio**

*Private Class · Alumni by Better · Vigência: 21/08/2026*

## 1. Status normativo, vigência e alcance

Este adendo tem caráter normativo e complementa os Documentos pedagógicos 00–06 e a Série P. Em caso de formulação mais geral nos documentos anteriores, prevalece a especificação mais objetiva deste adendo nos temas que ele regula.

As regras deste adendo:

valem para todas as novas produções;

devem ser aplicadas às revisões de artefatos ainda não liberados;

não obrigam a reabrir materiais já liberados, salvo quando houver defeito funcional relevante, exposição indevida, divergência de conteúdo ou prejuízo real de uso;

não autorizam o gerador a generalizar exemplos de um aluno ou artefato específico.

## 2. Finalidade

Este adendo transforma princípios amplos — como clareza, tom didático e hierarquia visual — em verificações objetivas de entrega. Seu foco é prevenir redundância instrucional, respostas previsíveis pela posição, referências frágeis e integração visual inadequada entre áudio e conteúdo linguístico.

## PARTE A — Regras pedagógico-produtivas

### 3. Tempos de produção oral

Indicações de tempo para a produção oral do aluno pertencem ao Teacher’s Guide e não devem aparecer na superfície projetada ao aluno. A tela pode apresentar sequência, objetivo ou condição comunicativa, mas não cronômetro, contagem de minutos ou pressão temporal, salvo quando o tempo for parte autêntica e pedagogicamente justificada da tarefa.

Validação bloqueante: nenhum slide ou prompt dirigido ao aluno exibe “three minutes”, “2 min”, “you have X minutes” ou equivalente sem justificativa funcional registrada no Teacher’s Guide.

### 4. Subprompts com função real

Todo subprompt deve acrescentar uma ação, um critério, uma sequência ou um apoio que não esteja suficientemente expresso no prompt principal. Se apenas repetir, contar ou comentar a resposta esperada, deve ser retirado.

#### 4.1 Teste de necessidade

Antes da entrega, remover provisoriamente o subprompt e verificar:

a ação solicitada fica incompleta ou ambígua?

algum critério necessário deixa de existir?

a ordem de execução deixa de estar clara?

um apoio compatível com o nível desaparece?

Se todas as respostas forem “não”, o subprompt é redundante e deve ser eliminado.

#### 4.2 Formulações não autorizadas

comentários sobre a quantidade de respostas quando o prompt já a define;

frases que apenas anunciam que uma resposta será diferente da anterior;

pistas que descrevem a estrutura do gabarito em vez de apoiar a operação linguística;

metacomentários do gerador apresentados como instrução ao aluno.

### 5. Instruções diretas, mas não abruptas

As instruções devem ser breves, acionáveis e didáticas, sem imperativos desnecessariamente absolutos ou tom punitivo. A suavização não pode tornar a tarefa vaga: deve preservar verbo de ação, objeto e critério quando necessários.

| **Evitar quando soar abrupto ou punitivo** | **Preferir formulação didática equivalente** |
|---|---|
| Find the unsupported statement. | Try to identify the statement that is not supported by the text. |
| The last one is the trap. | One statement is not supported. Which one is it? |
| Give two answers. The second must be different. | What is this document, and who does it bind? |

Os exemplos ilustram o princípio e não constituem frases obrigatórias.

### 6. Embaralhamento funcional

Em matching, sorting, ordering e associação, a ordem visual inicial não pode revelar ou reproduzir a sequência do gabarito. Antes da entrega, deve-se verificar a existência de padrões como 1–A, 2–B, 3–C, correspondência por posição, blocos paralelos ou qualquer ordenação que permita responder sem processar o conteúdo.

#### 6.1 Requisitos por mecânica

Matching e associação: pelo menos um dos conjuntos deve ser apresentado em ordem funcionalmente embaralhada; a correspondência correta não pode seguir a mesma posição visual.

Sorting: os itens de entrada devem misturar as categorias; não agrupar previamente todos os itens de uma categoria.

Ordering: os itens devem começar fora da sequência-alvo; a interface não pode preservar o gabarito na ordem do DOM, em atributos, numeração visível ou fallback textual acessível ao aluno.

Alternativas: quando houver padrão recorrente de posição da resposta correta, redistribuir as posições sem introduzir ambiguidade.

#### 6.2 Validação bloqueante

comparar a ordem mostrada ao aluno com o Answer Key;

reprovar padrões 1–A, 2–B, 3–C ou equivalentes;

reprovar correspondência correta por simples alinhamento de linhas ou colunas;

confirmar que o embaralhamento não altera o conteúdo, a acessibilidade ou o gabarito.

### 7. Referências posicionais frágeis

Evitar “the first one”, “the third field”, “the last statement” ou equivalentes quando os itens podem ser reorganizados, embaralhados, filtrados ou refluídos em outro tamanho de tela. Nomear diretamente o campo, a frase, a categoria ou um identificador semanticamente estável.

“Revise the third field” → “Revise the Expected impact field”.

“The last one is not supported” → “One statement is not supported. Which one is it?”.

“Match it with the first one” → nomear a expressão ou categoria correspondente.

Referências posicionais são permitidas somente quando a posição é parte estável e necessária da própria operação, como ordenar etapas cronológicas explicitamente numeradas.

### 8. Consistência entre tela, Teacher’s Guide e Answer Key

A tela do aluno, o Teacher’s Guide e o Answer Key devem pertencer à mesma versão da atividade e concordar quanto a instrução, conteúdo, ordem relevante, respostas aceitas, rationale e tratamento de alternativas. Uma alteração em qualquer representação exige nova conferência das demais.

a instrução descrita no Teacher’s Guide corresponde à ação disponível na tela;

o Answer Key corresponde aos itens e à ordem efetivamente apresentados;

nenhuma dica do Teacher’s Guide aparece indevidamente na visão do aluno;

o embaralhamento visual não invalida referências, numeração ou explicações do gabarito.

## PARTE B — Regras de interface aplicáveis à Série P

### 9. Separação visual entre player e conteúdo linguístico

O player deve constituir um controle visual separado do conteúdo linguístico. Botões não podem aparecer colados à frase, ao modelo de pronúncia, ao transcript ou à instrução, nem parecer pontuação, continuação ou parte clicável do texto.

#### 9.1 Requisitos visuais e estruturais

agrupar os controles em contêiner próprio, com espaçamento consistente antes e depois;

preservar distinção de fundo, borda, alinhamento ou ritmo suficiente para identificar o player como controle;

manter separação legível em desktop, tablet e larguras reduzidas;

não inserir botão no mesmo fluxo inline da frase, salvo componente explicitamente desenhado e validado para essa função;

preservar foco visível, rótulos acessíveis e área de toque adequada.

### 10. Controles obrigatórios nos microáudios

Aplicar Play/Pause no mesmo botão e um botão Stop separado também aos microáudios e modelos curtos de pronúncia. Uma exceção somente é permitida quando estiver explicitamente documentada, tiver justificativa funcional e não produzir comportamento inconsistente ou perda de controle para o usuário.

Play inicia; durante a reprodução, o mesmo controle passa a Pause;

Pause preserva a posição; novo Play retoma desse ponto;

Stop interrompe e retorna ao início;

o estado visual e o rótulo acessível acompanham o estado real do áudio;

iniciar outro áudio aplica a política de simultaneidade definida pelo artefato.

### 11. Uniformidade entre Pre-class e In-class

Os players do Pre-class e do In-class devem compartilhar comportamento, linguagem de controles, estados, acessibilidade e lógica de espaçamento. Diferenças de composição visual são permitidas quando exigidas pelo contexto, mas não podem mudar o significado dos controles nem retirar funcionalidades obrigatórias.

#### 11.1 Validação bloqueante

testar áudio longo e microáudio no Pre-class e no In-class;

testar Play, Pause, retomada, Stop e reinício;

verificar que controles não parecem parte da frase em fundos claros e escuros;

verificar espaçamento e quebra em desktop, tablet e viewport estreita;

reprovar qualquer microáudio sem Stop, salvo exceção documentada e aprovada;

confirmar comportamento equivalente nas visões do professor e do aluno.

## 12. Matriz de aplicação e responsabilidade

| **Safeguard** | **Diretrizes responsáveis** | **Verificação de entrega** |
|---|---|---|
| Tempo oral somente no Teacher’s Guide | Documentos 04 e 06 | P3 e revisão pedagógica |
| Subprompt necessário e tom didático | Documentos 04 e 06 | P3 e revisão pedagógica |
| Embaralhamento e referências estáveis | Documentos 04 e 06 | P2/P3 e Answer Key |
| Consistência entre representações | Documento 04 e Série P | P3 |
| Player separado e microáudios completos | Série P | P2/P3 |
| Uniformidade Pre/In-class | Série P | P2/P3 |

## 13. Composição vigente e instrução de carregamento

### 13.1 Conjunto a ser entregue ao gerador

Documentos pedagógicos 00–06;

Série P: P1, P2 e P3;

Adendo Normativo 01 — Continuidade pedagógica, transcript opcional e navegação de retorno;

Adendo Normativo 02 — Safeguards de instrução, atividades e áudio;

anexos técnicos aplicáveis ao modo de produção, como o padrão de áudio vigente, quando a entrega não for protótipo.

### 13.2 Instrução obrigatória de carregamento

**INSTRUÇÃO AO GERADOR:** Leia integralmente os Documentos 00–06, a Série P e todos os Adendos Normativos vigentes antes de planejar, gerar, revisar ou validar o artefato. Trate os adendos como requisitos normativos posteriores e específicos. Não inicie a produção se algum arquivo listado como vigente não tiver sido disponibilizado. Na saída de validação, declare nominalmente quais documentos e adendos foram carregados.

### 13.3 Controle de pacote

O índice, manifesto ou lista de composição que acompanha cada pacote deve registrar os adendos vigentes. A simples existência do arquivo fora do pacote não constitui carregamento nem conformidade. A ausência de A01 ou A02 no lote deve bloquear a declaração de conformidade integral.

## 14. Checklist final

☐ Tempos de produção oral aparecem somente no Teacher’s Guide, salvo exceção autêntica justificada.

☐ Cada subprompt acrescenta ação, critério, sequência ou apoio real.

☐ As instruções são diretas sem tom abrupto ou punitivo.

☐ Matching, sorting, ordering e associação não revelam o gabarito pela posição.

☐ Não há padrão 1–A, 2–B, 3–C ou equivalente.

☐ Não há referências posicionais frágeis em itens reorganizáveis.

☐ Tela, Teacher’s Guide e Answer Key pertencem à mesma versão e não divergem.

☐ Players estão visualmente separados do conteúdo linguístico.

☐ Microáudios possuem Play/Pause e Stop ou exceção aprovada e documentada.

☐ Pre-class e In-class mantêm comportamento uniforme.

☐ A01 e A02 constam do pacote e foram nominalmente carregados pelo gerador.
