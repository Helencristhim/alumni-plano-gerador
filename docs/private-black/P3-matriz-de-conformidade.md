> **Documento normativo importado do Drive — nao editar aqui.**
> Origem: `P3_Matriz_de_Conformidade_e_Especificacao_da_Suite.docx`
> Drive ID: `1UOTsOLa10QiC-80Fwko4YFHuo4eaGlWN`
> Modificado no Drive: 2026-08-21
> Reimportar: `python3 scripts/black/docx_to_md.py <arquivo.docx> docs/private-black/P3-matriz-de-conformidade.md`
> A fonte e o .docx. Divergencia entre este arquivo e o Drive se resolve reimportando, nunca editando o .md.

**P3 · MATRIZ DE CONFORMIDADE E ESPECIFICAÇÃO DA SUÍTE EXECUTÁVEL**

**Como provar, requisito a requisito — Private Class Alumni Black**

**O que este arquivo é, e o que ele não é.** Ele especifica a **matriz normativa** e os **requisitos da suíte executável**. **A implementação dos testes é entrega técnica separada e não está contida aqui.** Consultar esta especificação **não é** executar a suíte: nenhum resultado pode ser declarado a partir da leitura deste documento.

**Série P — plataforma.** Terceiro documento da série: **P1** é o contrato funcional (o *quê*), **P2** é o protocolo de implementação e QA (o *como se mexe e como se prova*), e **P3** é a **matriz** que transforma cada requisito do P1 em prova objetiva — positiva e negativa.

**O que ainda não existe.** Código executável · catálogo individual de casos com identificadores · automação no navegador · *fixtures* · comandos de execução · relatório gerado automaticamente.

**Sobre as checagens já existentes.** O conjunto acumulado num material específico é **base de migração, não a suíte**: é majoritariamente **estático**, foi construído em torno de **um** material, não executa todos os fluxos no navegador, **não é parametrizado para qualquer aluno** e não comprova os recursos que dependem do ambiente oficial. Aproveitá-lo é certo; **reconhecê-lo como a suíte final não**.

**O P3 não cria regra.** Não cria regra pedagógica, editorial, visual nem funcional. Se um teste daqui exige algo que o P1 não pede, **o teste está errado** — não o material. Regra nova entra pelo P1, e só então ganha teste aqui.

**Uma consequência que é o ponto.** A conformidade **não é a presença de texto, seletor ou função no código**. Sempre que o requisito envolver **interação, estado, visibilidade ou comportamento por perfil**, a prova é **executar o fluxo no navegador**. Buscar a string Finish lesson no arquivo prova que a palavra existe; não prova que o botão conclui a aula.

**Cada teste declara seis campos.** Teste sem eles não entra na suíte:

| **Campo** | **Por que existe** |
|---|---|
| **Requisito de origem no P1** | teste órfão vira regra clandestina, e ninguém sabe se pode removê-lo |
| **Condição verificada** | a afirmação que está sendo testada, em uma frase |
| **Evidência positiva esperada** | o que se observa quando está certo |
| **Mutação / caso negativo** | o defeito deliberado que o teste **tem** de pegar |
| **Ambiente de execução** | onde ele vale — e onde ele não pode concluir |
| **Classificação** | **bloqueante · condicional · informativo** |

**1. Perfil de capacidades do ambiente — antes de qualquer teste funcional**

A suíte **primeiro descobre onde está rodando**. Sem isso, toda falha fica ambígua entre defeito do material e restrição do host — e a ambiguidade sempre se resolve a favor de quem escreveu o código.

Capacidades a identificar: execução de JavaScript · persistência local · reprodução de áudio · permissão para abrir nova janela ou aba · restrições de sandbox · compartilhamento ou isolamento de estado · suporte aos recursos que o produto exige.

| **Ambiente** | **O que ele pode concluir** |
|---|---|
| **Artefato de revisão** | sujeito a restrição externa do host — bloqueio de pop-up, entre outras |
| **Ambiente oficial do produto** | é onde as funcionalidades definitivas se validam |
| **Modo local de desenvolvimento** | serve ao diagnóstico; **não substitui** a validação no publicado |

**Limitação externa detectada é registrada COMO limitação do ambiente.** Não se oculta, não se converte automaticamente em defeito do HTML, e **não serve para declarar aprovada** uma funcionalidade que não chegou a ser testada.

**1.1 Carga limpa — a primeira prova de todas**

**Antes de qualquer verificação de conteúdo, a página abre e o console fica limpo.** Este teste custa segundos e vale mais que centenas de checagens de texto, porque é o único que enxerga a classe de defeito que nenhuma delas alcança.

| **Verificação** | **Resultado obrigatório** |
|---|---|
| Carga | **zero erro e zero exceção** no console, nas duas visões |
| Construtores | cada componente que se monta por script **existe no DOM depois da carga** — contado, não presumido |
| Cobertura | a contagem de componentes construídos bate com a de gatilhos presentes no markup |

**Por que esta seção abre o documento.** Uma exceção no boot **aborta o resto do manipulador**: o sintoma aparece longe da causa. No caso que originou esta regra, um acesso de propriedade sobrevivente a um renome derrubava o preenchimento do pre-class — e o que **sumiu** foi o transporte de áudio de **todo** o material, em pre-class e in-class. O texto estava inteiro: a função existia, o identificador existia, e 435 casos negativos estáticos passaram.

**Mutações obrigatórias:** introduzir um erro em qualquer função do boot e confirmar que a suíte reprova **por não haver componente construído**, e não apenas por haver erro no console — as duas evidências são distintas, e a segunda sem a primeira deixa passar um construtor que falha em silêncio.

**2. Integridade estrutural**

Verificar: existência das visões e seções obrigatórias · associação correta entre ciclo, aulas, cards e conteúdos · correspondência entre identificadores, botões e painéis · **ausência de id duplicado** · validade de HTML, CSS e JavaScript · ausência de referência quebrada · ausência de controle sem função · **nenhum conteúdo obrigatório acessível só por mecanismo bloqueado** · **nenhuma URL absoluta de teste ou domínio fixado no código** · isolamento entre materiais, ciclos e alunos.

**Mutações que a suíte tem de pegar:** alterar um identificador · remover uma seção obrigatória · fazer dois botões apontarem para o mesmo conteúdo.

**2.1 Etapas — nenhuma contagem própria**

Origem: P1 §4. A regra diz que a quantidade e a sequência vêm da **saída pedagógica**, que o HTML não fixa contagem, que as etapas do registro correspondem à saída e que **não há etapa fictícia**. Sem teste, essa regra é uma declaração de intenção — e a intenção não impede o oito de voltar.

**O teste precisa de mais de uma aula, com contagens DIFERENTES.** Suíte que roda sobre um único percurso aprova qualquer número fixo, porque nunca vê o segundo.

| **Verificação** | **Resultado obrigatório** |
|---|---|
| Variedade | o conjunto testado inclui aulas com **quantidades diferentes** de etapas |
| Correspondência | etapas da **saída pedagógica** = etapas do **registro** = etapas **navegáveis**, item a item e na mesma ordem |
| Combinação | duas etapas que compartilham uma tela aparecem **uma vez cada**, sem duplicata artificial para "fechar a conta" |
| Omissão | etapa justificadamente ausente **não é recriada** pelo HTML para completar a interface |
| Ausência de contagem | **nenhum número de etapas escrito** no HTML, no CSS ou na checagem — o N sai sempre do registro |

**Mutações obrigatórias:**

•  **fixar o número oito** — na checagem, num laço, numa barra de progresso ou num rótulo — e confirmar que a suíte reprova;

•  **acrescentar uma etapa fictícia** só para completar a interface, e confirmar que a comparação com a saída pedagógica a acusa;

•  **duplicar** a etapa que compartilha tela com outra, para provar que a contagem não é inflada;

•  **remover uma etapa do registro** mantendo a tela, e o inverso, para provar que a correspondência é verificada **nos dois sentidos**.

**A que mais engana é a contagem escrita na própria checagem.** Uma checagem que "confere se há oito etapas" passa em todas as aulas de oito e reprova as legítimas de sete — e parece rigor. O N deriva dos blocos existentes, nunca de número escrito na checagem (P2 §3).

**Quando o material só tem aulas de uma contagem**, o arquivo sozinho não prova nada: a contagem dele passaria igual numa implementação que a fixasse. A prova então se faz **fora do navegador**, como a de migração (§3.0): extraem-se as funções de derivação e alimentam-se **registros fabricados** com contagens diferentes — abaixo, dentro e **acima** da faixa que o material conhece. E o registro editorial que acompanha a contagem (numeral por extenso, plural, rótulos derivados) entra na mesma prova: **um mapa com uma entrada só é vestígio da contagem antiga**, e faz uma aula fora dela ler diferente das demais.

**2.2 Modo de entrega declarado na interface**

Origem: P1 §0 e §17. No modo protótipo o material **declara uma vez** que o áudio não é final.

| **Verificação** | **Resultado obrigatório** |
|---|---|
| Existência | o aviso existe quando o áudio é de síntese do navegador |
| Unicidade | aparece **uma vez**, não a cada player |
| Linguagem | fala da **consequência** — a voz é provisória — e **não nomeia tecnologia** nem navegador |
| Língua | o trecho declara a própria língua, para o leitor de tela |
| Lugar | onde a pessoa **encontra** o áudio, não no conteúdo projetado durante a aula |

**O modo se DERIVA, não se pergunta.** Síntese do navegador é, pela definição do P1 §0, modo protótipo. Uma checagem que dependesse de alguém declarar o modo falharia exatamente no caso em que ninguém declarou — e no dia em que o áudio virar definitivo, a exigência do aviso desaparece sozinha, junto com a síntese.

**Mutações obrigatórias:** remover o aviso · duplicá-lo · trocar a consequência por tecnologia (*"as vozes do navegador"*) · retirar a marca de língua.

**2.3 Origem, segurança e correspondência dos áudios**

Origem: P1 §0.1 e Anexo P-A. A suíte trata o áudio oficial como artefato produzido previamente pelo pipeline ElevenLabs, nunca como fala sintetizada no navegador.

No build de produção final, verificar por exclusão: ausência de Web Speech API, speechSynthesis, SpeechSynthesisUtterance, endpoints autenticados da ElevenLabs, API keys, tokens ou fallback para síntese local. A simples existência de arquivos de áudio não aprova a origem.

Verificar pelo manifesto: cada arquivo possui transcript e versão aprovados, categoria funcional, modelo, Voice ID, parâmetros, duração e checksum; o arquivo existente confere com o checksum; o player aponta para esse arquivo; o transcript exibido é o mesmo que originou a geração.

Executar todos os players no build, não uma amostra: carregar, reproduzir, pausar, retomar, parar e reiniciar. Confirmar ausência de requisição de síntese ou geração em tempo de execução e registrar falhas de mídia sem fallback silencioso.

Mutações obrigatórias: inserir SpeechSynthesisUtterance; adicionar fallback por speechSynthesis; expor uma chave falsa no JavaScript; trocar o arquivo de dois transcripts; alterar o transcript sem regenerar; modificar o checksum; substituir um Voice ID no manifesto; remover um arquivo; fazer o player chamar a API no cliente. Cada mutação deve reprovar pela causa correspondente.

Classificação: síntese no cliente, credencial exposta, mídia ausente ou divergência transcript–arquivo são falhas bloqueantes na produção final. No protótipo, a síntese provisória é permitida somente com o aviso único previsto no P1.

**3. Separação entre Visão professor e Visão aluno**

Os testes **executam as duas visões** — não inspecionam o markup de uma só.

•  conteúdo exclusivo do professor **não aparece** na visão do aluno;

•  Teacher's Guide, gabaritos prévios, registro pós-aula e controles administrativos ficam **restritos ao professor**;

•  **ação do professor não aparece como ação concluída pelo aluno**;

•  resposta e atividade do aluno **podem** aparecer para o professor, onde essa visualização estiver prevista;

•  controle do aluno **não se confunde** com controle administrativo;

•  **trocar de visão não apaga resposta** nem altera indevidamente o estado da aula;

•  elemento oculto **não permanece alcançável** por teclado nem por tecnologia assistiva.

**display:none** **não é evidência suficiente.** Se o conteúdo reaparece por outra interação, ou é anunciado ao leitor de tela, a separação não existe — ela é de **armazenamento e de árvore acessível**, não de folha de estilo (P1 §5).

**3.0 Migração de espaços de estado**

Origem: P1 §5. Migração é o código que **ninguém vê rodar** — ela acontece uma vez, na primeira abertura, e o que ela erra some antes de alguém procurar.

| **Verificação** | **Resultado obrigatório** |
|---|---|
| Cada formato já existente | um bucket de **cada** convenção anterior migra **sem perder chave** |
| Formato corrente | bucket já na convenção nova passa **intacto** |
| Vazio | bucket ausente ou ilegível resulta nos espaços vazios, sem exceção |
| Sem resíduo | o que fica gravado **não conserva** os nomes antigos |
| Ordem | renomear antes de classificar (P1 §5) |

**Mutações obrigatórias:** inverter a ordem das migrações · remover a migração de renome · fazer a classificação rodar sobre um bucket já classificado.

**A migração se testa fora do navegador.** As funções de armazenamento se extraem e rodam contra buckets montados à mão — é a única forma de exercitar um formato que **já não existe** em nenhuma máquina de teste.

**3.1 Os dois campos compartilhados**

Origem: P1 §8. **What worked** **e** **Keep developing** **são os únicos campos que chegam ao aluno.** A checagem que confirma que os dois estão lá **não é** a checagem que reprova um terceiro: a primeira passa com dez campos na tela. É preciso a segunda, e ela se faz por **exclusão**, não por presença.

| **Verificação** | **Resultado obrigatório** |
|---|---|
| Presença | os dois campos aparecem na aba Feedback da visão do aluno |
| **Exclusividade** | **nenhum outro campo** do registro pós-aula aparece ali — a contagem de campos na aba é **exatamente dois** |
| Restrição | escala, engajamento, evidência observável, ponto prioritário e próxima ação permanecem **restritos ao professor**, no armazenamento e na árvore acessível |
| Troca de visão | alternar professor → aluno → professor **não expõe** registro interno, nem deixa resíduo pintado na tela |

**Mutações obrigatórias:**

•  **expor um terceiro campo** ao aluno — Language to revisit, Next focus ou outro — e confirmar que a suíte reprova **por ele existir**, não por faltar algum dos dois;

•  **compartilhar um campo numérico** da escala, que é o vazamento mais provável, porque não parece texto de feedback;

•  **fazer a troca de visão repintar** um campo do professor na superfície do aluno.

**Por que a exclusividade tem de ser contada.** Um terceiro campo não quebra nada: a aba abre, os dois campos certos continuam lá, e a tela parece correta. O defeito é o que **a mais** apareceu, e só uma verificação por exclusão o encontra.

**4. Estados e transições**

Testar **inicial, intermediário e final** de cada componente: aula não realizada / realizada · conteúdo recolhido / expandido · resposta não preenchida / preenchida / conferida / redefinida · áudio parado / tocando / pausado / retomado / encerrado · card selecionado / movido / devolvido no sorting · aula iniciada / concluída / redefinida · registro pós-aula não salvo / salvo / redefinido.

**Cada teste verifica a mudança visual E o estado funcional.** Trocar o rótulo do botão sem mudar o comportamento **falha**. É a forma mais barata de parecer conforme.

**5. Componentes interativos — em todas as ocorrências**

A suíte testa cada mecânica compartilhada **em todas as suas ocorrências, nunca num slide de amostra**. Componente compartilhado que se testa uma vez só é como checagem que nunca falhou: não está conferindo nada.

Mínimo: expansores de conteúdo extra ou opcional · mostrar e fechar gabarito · reset de respostas · botões de conclusão e redefinição · players de áudio · sorting por arrastar **e** por clicar · campos do registro pós-aula · navegação entre slides · controles do Teacher's Guide · alternância de visão · cards e mapa de aulas.

**E confirmar que a expansão abre para baixo e preserva a posição do usuário** — sem saltar ao topo.

**Painéis do card de aula** (P1 §9.1), cada um exercitado no navegador, não lido no arquivo:

| **Verificação** | **Resultado obrigatório** |
|---|---|
| Ordem | consulta de preparação · abrir a aula · abrir o guia · registro pós-aula |
| Rótulo | **não muda** ao abrir — nada de *Ocultar X* |
| Substituição | abrir um painel **fecha o outro do mesmo card** |
| Recolhimento | clicar de novo no mesmo botão **recolhe** |
| Grupo | o acordeão é **do card**, não da página: o painel de outra aula continua aberto |
| Estado | aria-expanded correto no botão que abriu **e** no irmão que fechou |
| Posição | expandir **não** leva a tela ao topo do conteúdo aberto |

**Mutações obrigatórias:** devolver a troca de rótulo · impedir o fechamento do irmão · travar a alternância, de modo que o segundo clique não recolha · remover a atualização do aria-expanded · **deixar o irmão fechado com** **aria-expanded="true"** · estender o grupo do acordeão à página inteira · remover um dos quatro controles do card.

**A que mais engana é a do irmão.** Ela não muda nada na tela: o painel fecha, o rótulo está certo, e só o leitor de tela recebe a informação errada. Sem caso negativo, passa para sempre.

**6. Player de áudio**

Para **cada** áudio existente no pre-class e no in-class — todos, sem amostragem:

um único botão combinado **Play/Pause** · um botão separado **Stop** · os dois **lado a lado** · Play vira Pause durante a reprodução · a pausa **não reinicia** · a retomada parte do ponto pausado · Stop interrompe e volta ao início · Play depois de Stop começa do zero · **nenhum terceiro botão redundante** de Pause ou Resume · funcionamento independente quando há mais de um áudio no mesmo slide.

**Caso negativo obrigatório:** introduzir **três** botões — Play, Pause/Resume e Stop — e confirmar que a inconsistência é detectada.

**7. Conteúdo extra e opcional**

Todo conteúdo **extra, opcional, follow-up ou extensão** começa **recolhido**, atrás de expansor (P1 §4).

Detectar: conteúdo opcional exibido direto na tela · rótulo Optional separado indevidamente da ação Optional follow-up · expansor que muda a posição da página de forma abrupta · **conteúdo essencial colocado por engano dentro de área opcional** · estado expandido que sobrepõe elementos ou os joga fora da área visível.

**8. Correção, gabaritos e respostas esperadas**

Origem: P1 §18. A coerência se verifica **por tipo de tarefa**, não por regra única.

**Pre-class:** atividade autocorrigida usa referência de resposta coerente · o feedback imediato e o gabarito do professor **não divergem** · o reset do aluno e o controle de fechar gabarito aparecem **depois** de todo o conteúdo, nunca antes dos exercícios · o professor consulta o gabarito e **não apaga a resposta do aluno** por um controle ambíguo.

**In-class:** resposta esperada, critério de aceite, alternativa possível e orientação de condução ficam **no Teacher's Guide** · a tela compartilhada **não revela antes da tentativa** · atividade fechada pode usar Check · referência ou comparação usa See ou Compare, **nunca** **Check** · guided discovery pode revelar One possible answer depois da tentativa · discussão, simulação, role-play e produção aberta **não recebem resposta única artificial**.

**Post-class:** atividade fechada ou autocorrigida segue a mesma coerência; atividade aberta **não se converte** em exercício de resposta única para facilitar a automação.

**A fonte única de respostas é a implementação preferencial. O requisito BLOQUEANTE é a ausência de divergência perceptível entre correção, gabarito e feedback.** O teste compara **o que cada visão apresenta**, não a forma como o dado foi guardado.

**Caso negativo obrigatório:** inserir divergência deliberada entre correção e answer key.

**9. Teacher's Guide em janela ou aba separada**

Origem: P1 §15.1; protocolo dos dois ambientes: P2 §5.

A rota deriva da URL corrente — ?mode=teacher-guide&lesson={id}. **Nenhum domínio, URL oficial, URL de teste ou endereço de artefato escrito à mão no código.**

| **Verificação** | **Resultado obrigatório** |
|---|---|
| Disponibilidade | o botão aparece em **todos** os cards de In-class da visão professor |
| Restrição por perfil | o botão **não** aparece na visão do aluno |
| Associação | cada card abre o guia **da sua** aula |
| Entrada | o guia abre direto no início da aula selecionada |
| Conteúdo | a janela apresenta **somente** o guia e sua navegação |
| Identificação | a aula aberta está claramente identificada |
| Independência | navegar no guia não altera slide, visão, resposta ou estado da janela principal |
| Endereçamento | a rota vem da URL corrente e não depende de domínio fixo |
| Isolamento | materiais, ciclos e alunos diferentes **não compartilham estado** |
| Nome da janela | deriva dos identificadores do **artefato** e da **aula**; sem dado pessoal; sem constante comum a todos os materiais |
| Posição | o botão fica **ao lado** do controle que abre a aula — as duas ações de entrar, antes dos controles de consulta |
| Rótulo | o verbo está na língua da superfície do professor (P1 §16); só o nome próprio do componente fica em inglês, **marcado com** **lang**; e o rótulo é **um só item de layout**, para o gap do botão não entrar no meio da frase |
| Fonte do rótulo | os cards trazem **o mesmo** rótulo entre si, e o texto de apoio dentro da aula **cita o rótulo visível** — não um texto escrito à parte |
| Fallback | bloqueio → aviso breve, e o guia interno continua disponível |
| Ambiente oficial | a abertura efetiva se comprova **na URL real do produto** |
| Regressão | o guia interno continua funcional enquanto for a alternativa |

**A suíte detecta e bloqueia:** todos os cards abrindo o mesmo guia · guia aberto na aula errada · botão exposto ao aluno · URL absoluta gravada no HTML · navegação no guia alterando a janela principal · chave genérica de armazenamento misturando materiais · **falha silenciosa quando** **window.open()** **devolve** **null** · aviso afirmando que o guia abriu quando não abriu · remoção do guia interno antes da validação oficial · **aprovação baseada só no artefato em iframe restrito** · fluxo manual de sincronização entre abas tratado como solução definitiva.

**A ausência de** **allow-popups** **no artefato de revisão é limitação do host.** Ali a suíte valida o botão, a construção da rota, a associação da aula, a detecção do bloqueio e o *fallback* — e **não pode declarar comprovada a abertura externa**.

Classificação: **condicional** no protótipo, quando implementação e *fallback* estiverem corretos e o host bloquear pop-up; **bloqueante** na publicação definitiva, até validar na URL oficial e nos navegadores suportados.

**10. Conteúdo editorial e linguagem de interface**

Procurar: linguagem de decisão de produção · explicação sobre implementação, armazenamento ou cálculo interno · justificativa dirigida ao gerador · nota sobre limitação que não diz respeito a quem usa · instrução de QA deixada em tela · mistura indevida de português e inglês · grafia britânica em material definido em American English · erro de digitação e rótulo inconsistente · **Markdown literal ou quebrado** · título truncado ou quebrado por erro de layout.

**Lista expansível de expressões proibidas + lista controlada de exceções.** E **a palavra isolada não autoriza correção automática sem análise de contexto** — citação literal de fonte autêntica preserva a grafia original (P1 §16), e corrigi-la é destruir o objeto da aula.

**11. Sistema visual, tipografia e espaçamento**

Por análise do DOM, estilo computado e regressão visual: tokens aprovados da identidade Alumni by Better · preservação da identidade premium/black · ausência de ativo tipográfico externo · famílias efetivamente disponíveis no build · pergunta principal na família display do sistema, em itálico moderado e peso médio · tamanho maior que o corpo e menor que o título · listas e quiz projetado na mesma família de referência, preservando componentes distintos · contraste mínimo aplicável sobre fundos claros, escuros e compostos · largura controlada · quebra de linha sem corte, overflow ou linha órfã crítica · caixa normal em perguntas longas · alinhamento à esquerda como padrão · centralização restrita a pergunta curta que seja o único foco da tela · espaçamento entre pergunta, texto, cards e controles · responsividade nas larguras previstas.

Mutações obrigatórias: restaurar Google Fonts como dependência estrutural; trocar a pergunta principal para a fonte de interface; introduzir terceira família; remover itálico ou peso médio; igualar os três componentes; aplicar caixa alta a pergunta longa; centralizar pergunta longa; remover max-width; reduzir contraste em um dos fundos; forçar quebra ou overflow. A suíte precisa reprovar cada mutação pela propriedade correspondente.

**Contraste se mede sobre o fundo efetivamente composto, transparências incluídas — e a rotina traz canário conhecido**, para provar que consegue detectar uma falha real. Varredura que devolve zero sem canário não provou nada (P2 §3).

Regressão visual abrange: as duas visões · todas as abas · fundos claros e escuros · conteúdo recolhido e expandido · estados dos players · formulários e campos de feedback · os tamanhos de tela suportados.

**12. Acessibilidade**

Navegação completa por teclado · foco visível · ordem lógica de tabulação · nome acessível em todo botão · aria-expanded atualizado · associação entre rótulo e campo · identificação de imagens e composições visuais · contraste · **nada identificado só por cor** · **equivalência funcional entre arrastar e clicar no sorting** · ocultação acessível do conteúdo do professor · anúncio adequado de mensagem de erro e de *fallback*.

**O sorting funciona pelos dois caminhos:** arrastar o card até a coluna, **e** selecionar o card e depois a coluna de destino (P1 §12).

**13. Referências compartilhadas e prevenção de divergência**

Os componentes compartilhados se testam **como unidades reutilizáveis**. Correção aplicada ao player, ao expansor, ao sorting, ao registro pós-aula, à pergunta ou ao Teacher's Guide **reflete-se em todas as aulas e materiais que usam o mesmo componente**.

Quando dois materiais usam a mesma regra funcional — por exemplo dois alunos do mesmo produto —, a suíte compara **os resultados esperados**, sem exigir igualdade literal de conteúdo ou de CSS onde a variação de perfil, nível ou identidade for legítima.

**Toda divergência entre materiais está prevista por uma regra, justificada pelo perfil ou pelo desenho pedagógico, e documentada como exceção — nomeada e singular (****P2 §3****). Diferença acidental falha.**

**14. Testes negativos e mutações**

**Cada requisito crítico tem pelo menos um caso negativo.** A suíte altera de propósito uma condição válida e comprova que o erro é detectado.

Exemplos: expor conteúdo do professor ao aluno · trocar o guia associado a dois cards · remover o Stop de um player · recriar três controles de áudio · deixar conteúdo opcional aberto · introduzir cor sem token · reduzir contraste · inserir grafia britânica · mover o reset para o topo do pre-class · criar resposta diferente no gabarito · fixar uma URL de teste · substituir o nome dinâmico por um literal · quebrar o alinhamento do campo central · remover a alternativa por clique do sorting · **separar** **Optional** **de** **Optional follow-up** em etiqueta e botão · **fixar o número de etapas** ou **acrescentar etapa fictícia** (§2.1) · **expor um terceiro campo ao aluno** na aba Feedback (§3.1) · **alternar a forma de um identificador técnico** — ALUNA por ALUNO, prof por professor.

**Mutações obrigatórias do nome da janela do Teacher's Guide** — nenhuma delas se detecta com um material aberto sozinho:

•  substituir o identificador dinâmico da janela por um **nome literal do aluno**;

•  usar **o mesmo nome de janela para dois materiais**;

•  usar **nome ou sobrenome do aluno como identificador técnico**;

•  **introduzir deliberadamente uma colisão de nomes de janela, abrir dois materiais e confirmar que a suíte DETECTA** quando o guia de um material substitui indevidamente o guia do outro.

**Mutações obrigatórias do rótulo do botão do guia:**

•  **passar o rótulo do card para a língua do deck**, contrariando o P1 §16;

•  **remover a marca** **lang** do nome próprio em inglês;

•  **dar a um card um rótulo diferente** dos demais;

•  **fazer o texto de apoio citar um rótulo que o botão não tem** — a segunda cópia divergindo, que é como a orientação passa a mandar procurar um botão inexistente;

•  **mover o botão para o fim da barra de controles**, separando-o do controle que abre a aula;

•  **partir o rótulo em dois itens de layout**, devolvendo o espaço duplo que o gap do botão produz.

**Suíte que aprova tanto a implementação correta quanto a mutação defeituosa não é válida.** É a mesma lei do P2 §3: checagem que não falha só não faz nada — e a variante mais silenciosa é a mutação que **remove** o elemento examinado.

**15. Evidências e relatório**

O relatório traz: versão do material · versão dos documentos normativos · data e ambiente do teste · navegador e versão · testes executados · resultados positivos · falhas · limitações externas · evidência visual ou registro do navegador · **requisitos não testáveis naquele ambiente** · decisão.

**"Zero falhas" só vale quando:** os testes positivos foram executados · os casos negativos correspondentes foram **detectados** · os estados interativos foram exercitados · as limitações do ambiente foram declaradas · **nenhum requisito dependente da plataforma foi apresentado como comprovado sem teste no ambiente oficial**.

Vocabulário do resultado, do 06 §4: **PASSOU · PARCIAL · FALHOU · NÃO VERIFICADO**. *"NÃO VERIFICADO" é resposta legítima; "PASSOU" sem evidência não é.*

**16. Gates de aprovação**

| **Resultado** | **Condição** |
|---|---|
| **Aprovado** | todos os requisitos bloqueantes comprovados nos ambientes aplicáveis |
| **Aprovado condicionalmente** | a implementação está correta, mas uma capacidade **externa** não pode ser comprovada no artefato restrito; o *fallback* funciona e a pendência está registrada |
| **Reprovado** | falha funcional · exposição entre perfis · inconsistência pedagógica · falha silenciosa · perda de dados · inacessibilidade crítica · requisito bloqueante não atendido no ambiente oficial |

**No caso do Teacher's Guide:** o protótipo recebe **aprovação condicional** se o host impedir pop-up. A publicação definitiva só se aprova depois que a abertura do guia correspondente for testada com sucesso **na URL oficial do material**.
