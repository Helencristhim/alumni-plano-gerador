> **Documento normativo importado do Drive — nao editar aqui.**
> Origem: `P1_Camada_Funcional_HTML.docx`
> Drive ID: `1CgtgTwqgBGuy-_B5yQKbMDFyK0AMEZuK`
> Modificado no Drive: 2026-08-24
> Reimportar: `python3 scripts/black/docx_to_md.py <arquivo.docx> docs/private-black/P1-camada-funcional-html.md`
> A fonte e o .docx. Divergencia entre este arquivo e o Drive se resolve reimportando, nunca editando o .md.

**P1 · CAMADA FUNCIONAL (HTML)**

**Especificação do meio de entrega — Private Class Alumni Black · adultos · A1–C1**

**Série P — plataforma.** Na versão vigente, o núcleo pedagógico validado compreende os documentos 00–06. A **série P** reúne especificações de plataforma **externas ao núcleo** — a camada que o 00 §6 retirou dele por decisão declarada: **P1** (esta, o contrato funcional), **P2** (protocolo de implementação e QA) e **P3** (matriz de conformidade e especificação da suíte executável). A criação futura de documentos numerados após o 06 é possível, desde que seja **deliberada** e acompanhada da atualização do índice e das referências do Documento 00.

**Estatuto.** É a *especificação separada do meio de entrega* que o 00 §7 prevê como entrada e que o Documento 06 espera receber. Na precedência do 00 §4 ocupa o **nono e último degrau**. **Uma decisão técnica nunca modifica silenciosamente uma regra pedagógica.** Se o HTML não comportar o que a aula pede, quem cede é o HTML; não havendo como ceder, **pare e declare**.

**Uso.** Entregue ao gerador: o pacote 00–06, as entradas do 00 §7, e este documento. O gerador produz primeiro as saídas pedagógicas do 06 e só então converte em HTML. **A conversão não altera conteúdo:** se algo precisar mudar para caber na tela, isso é achado pedagógico e volta uma etapa — não se resolve aqui.

**0. Dois modos de entrega**

Toda regra abaixo vale nos dois modos, salvo onde indicado.

| **Modo** | **Quando** | **Áudio** | **Declaração** |
|---|---|---|---|
| **Protótipo / validação** | antes da aprovação do conteúdo | síntese do navegador **identificada como provisória** | o material declara que o áudio **não é final** |
| **Produção final** | material aprovado, para uso em aula | áudios definitivos gerados pela API da ElevenLabs no pipeline seguro de produção, vinculados à versão aprovada do transcript e entregues como arquivos de mídia | sem aviso de provisoriedade e sem síntese executada no navegador |

**O modo é entrada obrigatória.** Não se infere. Em produção final, síntese do navegador é defeito; em protótipo, é o esperado — e a interface diz isso uma vez, sem explicar tecnologia.

**0.1 Fonte obrigatória do áudio na produção final**

Na produção final, todo áudio criado automaticamente para o material oficial é gerado pela API da ElevenLabs, conforme o Anexo P-A — Padrão de Produção de Áudios com ElevenLabs. A síntese nativa do navegador, incluindo Web Speech API, speechSynthesis e SpeechSynthesisUtterance, é proibida no artefato final.

A chamada à API ocorre somente no ambiente seguro do pipeline, antes da publicação. Chaves, tokens, cabeçalhos de autenticação e chamadas autenticadas à ElevenLabs nunca aparecem no HTML, no JavaScript entregue, no armazenamento local, no console ou em requisições iniciadas pelo navegador do aluno ou do professor.

O build recebe arquivos definitivos vinculados ao transcript aprovado. Qualquer alteração no transcript invalida o arquivo anterior e exige nova geração, nova associação e nova validação auditiva. O anexo governa modelo, vozes, parâmetros, pré-processamento, nomenclatura e QA; o P1 governa como o áudio aprovado é entregue e controlado na interface.

**PARTE I — O QUE PRODUZIR**

**1. O artefato**

A produção final entrega duas URLs e dois builds separados por papel. O build do professor contém a visão docente e uma prévia fiel da visão do aluno. O build do aluno contém exclusivamente a visão do aluno. Protótipo interno pode usar um único arquivo com alternância somente quando o modo protótipo estiver explicitamente declarado.

| **Camada / aba** | **Visão** | **Função** |
|---|---|---|
| Perfil | professor · aluno (recorte próprio) | quem é o aluno |
| Planejamento — **Planning** na visão do aluno | professor · aluno | projeção do ciclo |
| Pre-class | aluno responde · professor consulta | preparação |
| In-class | professor | deck projetado |
| **Feedback** | **aluno** | recebe os dois campos que o professor compartilha |
| Post-class | aluno | continuação |

A aba **Feedback** é camada funcional obrigatória na visão do aluno: é onde chegam **What worked** e **Keep developing** — e **só** esses dois.

**Na URL do professor, os rótulos Visão professor e Visão aluno alternam entre a área docente e a prévia discente. Na URL do aluno não existe alternador, rota de professor nem conteúdo docente incorporado. Os identificadores internos professor e aluno governam roteamento e armazenamento, sem permitir promoção de papel por parâmetro editável.**

**Separação de entrega. Conteúdo docente não pode estar apenas oculto por CSS, atributo, template, comentário ou condição JavaScript. Teacher’s Guide, answer keys reservados, hipóteses pedagógicas, registros internos, evidências restritas e controles administrativos não integram o HTML, o payload, o estado persistido ou os recursos enviados ao navegador do aluno.**

**2. Dependência externa — a distinção que decide**

**O funcionamento e a identidade do artefato não podem depender de ativos externos. Links editoriais do post-class para fontes autênticas são permitidos e, quando previstos pedagogicamente, obrigatórios — e não contam como dependência estrutural.**

| **Categoria** | **Estatuto** |
|---|---|
| **Ativo estrutural externo** — fonte tipográfica, imagem, script, CSS, biblioteca, ícone | **proibido**. O CSP do meio de publicação bloqueia host externo: o ativo não chega a ser projetado e a fonte passa a divergir do publicado **em silêncio** |
| **Link editorial do post-class** — artigo, vídeo, podcast, YouGlish, dicionário | **permitido e às vezes obrigatório** (06, post-class: pelo menos uma leitura e uma escuta/vídeo externas autênticas) |

Consequências práticas: aberturas de aula são composições em CSS; o logotipo vai **embutido**, do arquivo oficial, nunca reconstruído em texto; e a validação conta ativos estruturais, **não** links de navegação.

**3. Registro único — escopo delimitado**

**Para metadados estruturais repetidos, uma referência compartilhada é a solução preferencial para prevenir divergências. Quando houver representações separadas, sua correspondência deve ser validada. Esta regra NÃO obriga correção, answer key, feedback e Teacher's Guide a derivarem tecnicamente da mesma fonte; nesses casos, o requisito obrigatório é a ausência de divergência (§18).**

O registro é para **metadados estruturais repetidos**, não para o conteúdo da aula.

**Nome do aluno, tamanho do ciclo, nível, número de aulas, estado, título de aula, framework, etapas e demais metadados repetidos saem do registro único. Dados pedagógicos e fatos do conteúdo permanecem no conteúdo da aula.**

Datas, números de processo, citações, títulos de documento, trechos e qualquer fato autêntico da aula **ficam onde estão** — não vão para registro.

var ARTEFATO={id:'…'};                     // identificador TÉCNICO: sem dado pessoal

var ALUNO={nome:'…',sobrenome:'…'};        // NEUTRO; sobrenome é campo PRÓPRIO

var CICLO={numero:…,aulas:…,nivel:'…',rotulo:'…',rotuloAluno:'…'};

var LESSONS={ n:{ n:…, bloco:…, mod:'…', cod:'…', fwNome:'…', tema:'…', temaPre:'…',

stages:[{n:'…',min:…}, …], nav:[…] } };

•  **Identificador técnico é NEUTRO, e não varia de forma nem de gênero.** Um único par governa tudo: **aluno** e **professor** — o mesmo dos rótulos internos do §1, que já governam data-view. Daí saem o nome do registro (ALUNO) e os espaços de estado (§5). **Nada de** **ALUNA****,** **aluna****,** **prof** **ou** **shared** **convivendo com eles:** identificador que muda de forma conforme o perfil deixa de ser identificador — vira rótulo, e obriga a editar código a cada aluno novo. O gênero da prosa segue a pessoa; o do identificador, ninguém.

•  **ARTEFATO.id** **é identificador técnico, não rótulo.** Único por material ou ciclo, **sem nome nem sobrenome do aluno**, estável, e é dele que saem os nomes de janela e as chaves que precisam distinguir materiais abertos ao mesmo tempo (§15.1). Dado pessoal em identificador técnico vaza para fora da interface e sobrevive a toda troca de rótulo.

•  **O texto no markup é só estado inicial**; quem pinta é a repintura, por data-lf. O estado inicial **tem de concordar com o registro** — divergir faz a tela piscar o valor errado.

•  **Nome: duas regras sobre o mesmo registro.** Identificação (página inicial, título da aba) usa o **nome inteiro**; prosa do Perfil e do Planejamento usa **só o primeiro nome**.

•  Se algo passar a repetir um valor do registro, ligue por data-lf e acrescente a comparação à validação.

**4. Etapas e telas**

**Cada framework possui oito etapas pedagógicas normativas, definidas pelo Documento 03. A camada HTML representa as oito na mesma ordem, sem estabelecer quantidade fixa de slides.**

O registro recebe exatamente as oito etapas do framework. O HTML não acrescenta, elimina, duplica ou reordena etapas. A checagem exige oito etapas, mas deriva livremente a quantidade de slides da distribuição declarada.

Sobre telas:

•  **cada etapa está representada e navegável**;

•  **uma tela pode reunir atividades** relacionadas;

•  **duas etapas só compartilham uma tela quando houver dependência pedagógica real** — por exemplo feedback e retask, quando o retask depende diretamente do que acabou de ser construído;

•  quando isso ocorrer, **declare no registro**, por atributo próprio, **sem criar etapa fictícia** e sem sequenciamento paralelo;

•  **não existe quantidade universal de telas** — ela sai do conteúdo.

**Hierarquia de atividade é arquitetura, não etiqueta.** Conteúdo *Conditional*, *Extension* e *Optional* começa **recolhido**, num controle dentro da tela essencial, e **não ganha tela própria**.

**Quando o status integra o nome da ação, ele compõe o rótulo completo de um ÚNICO botão** — por exemplo Optional follow-up — **e nunca aparece como fragmento separado. Não duplicar o status em etiqueta e botão.**

A distinção é entre **etiqueta visual** e **rótulo funcional**: etiqueta de status que existe por si fica fora do botão; status que faz parte do nome da ação **vai dentro dele, inteiro**. Partir Optional de Optional follow-up é o defeito que a regra existe para impedir — e **a palavra do status é dita uma vez só**.

**PARTE II — REGRAS FUNCIONAIS**

**5. Papel e estado**

•  **Estado separado por PAPEL:** três espaços — **aluno**, **professor**, **compartilhado** —, roteados por prefixo. Os nomes são os do §3: um par só, neutro, igual ao que governa data-view.

•  **Regra assimétrica:** o que o aluno faz, o professor consulta; **o que o professor faz não aparece na visão do aluno** — separação de **armazenamento**, não de CSS.

•  **Trava de CSS não é guarda.** pointer-events impede o clique, não a chamada: a marca mudava na tela enquanto a gravação recusava, e **a tela mentia para o professor**. A guarda vai em **cada porta de escrita**.

•  **Persistência por** **data-k** **no próprio elemento**, nunca por lista de ids no boot.

•  **Metade das respostas não é campo** — vive em classe (opção selecionada, marca de certo/errado). Persista a **posição das marcas** por bloco, com ouvinte delegado.

•  **Reset que limpa campo a campo não reseta nada:** restaure o **HTML inicial do bloco**, com a cópia tirada depois de montar o gabarito e antes de preencher.

•  **Migrar o bucket anterior é obrigatório**, trabalhando no armazenamento bruto — a leitura filtrada por papel não enxerga o espaço do professor e perderia o texto em silêncio.

•  **Renomear um espaço é migração, não substituição — e a ORDEM entre migrações decide.** Quando houver mais de uma, a que **renomeia** vem antes da que **classifica**. O motivo é mecânico: a migração que classifica costuma se disparar por *"nenhum espaço existe"*, e um bucket na convenção antiga responde exatamente isso. Tratado como não classificado, ele teria a **função de classificação aplicada aos próprios espaços** — as chaves aluno, professor e compartilhado cairiam todas no destino padrão, e o pre-class do aluno reapareceria dentro do espaço do professor. **Nada falha, nada avisa.** Migração se prova com o bucket **de cada formato já existente**, e com o canário que confirma que a ordem invertida seria pega.

**6. Pre-class — gabarito, respostas e reset**

•  **Answer key começa fechado.**

•  O **professor abre e fecha o gabarito de cada atividade**.

•  As **respostas do aluno aparecem para o professor**.

•  **Ações do professor não alteram as respostas do aluno** — nem por acidente, nem por repintura.

•  Controle geral do professor: **Fechar todos os gabaritos desta aula** — e ele tem de alcançar também os painéis criados por script, que não têm id próprio.

•  Controle do aluno: **Reset my answers**.

•  **Ambos aparecem no fim do pre-class, depois de todo o conteúdo** — no topo, apareceriam antes de haver o que resetar ou fechar.

•  **Reset exige confirmação**, no documento, nunca por diálogo nativo.

**7. Controles da aula — obrigatórios**

•  **Reset lesson** e **Finish lesson** são obrigatórios no deck.

•  Ambos **exigem confirmação** antes de executar.

•  **A conclusão independe de checklist.**

•  **Finish lesson** **é a única fonte do estado "realizada".** Nem visita a slide, nem checklist, nem posição no deck produzem conclusão. **"Visitado" não é "concluído".**

•  **O reset é restrito à aula ativa** — nunca alcança as outras.

**8. Registro pós-aula**

•  **Escala linguística de 1 a 5**, igual para os três critérios, guardando o **número**, não a palavra — sem ele não há média nem evolução.

•  Critérios: **Fala e interação · Compreensão auditiva · Precisão estrutural**.

•  **Engajamento tem escala própria e fica FORA da média** de desempenho linguístico.

•  **Três campos escritos:** Evidência observável · Ponto prioritário de desenvolvimento · Próxima ação.

•  **Os três campos alinham-se em colunas iguais no desktop e em uma coluna em telas menores.** Grade genérica com auto-fit não serve para número fixo de campos: cai em duas colunas mais uma isolada. Use colunas explícitas, com alinhamento entre elas — senão o título mais longo empurra o próprio campo para baixo dos vizinhos.

•  **Só** **What worked** **e** **Keep developing** **chegam ao aluno**, na aba Feedback.

•  **Botões para confirmar e para limpar/refazer** o registro. Confirmação **gravada**, que sobrevive à recarga e cai na primeira edição — botão "salvar" em tela com autosave é promessa vazia.

•  **Proibido justificar tecnicamente na interface:** nada de explicar cálculo de média, armazenamento numérico ou por que a opção guarda o número. A regra vive na lógica; a tela recebe descrição funcional.

•  O resumo para o checkpoint dá média, série e contagem — **nunca veredito**.

**9. Mapa das aulas do ciclo**

•  Título: **Aulas neste ciclo** / **Lessons in this cycle**.

•  **Um minicard quadrado por aula do ciclo**, derivado do registro — nunca contado à mão.

•  Estados: **realizada** (nítida) · **disponível e não realizada** (estado próprio) · **ainda indisponível** (menor ênfase).

•  **Estado nunca identificado só pela cor** — três sinais, e nenhum deles cromático sozinho: marca, traço da borda e presença do código.

•  **Menos ênfase se faz com token de texto mais fraco, nunca com** **opacity**, que derruba o contraste sem controle.

•  **Conclusão vem de** **Finish lesson**, não de visita.

•  **Visão professor:** aulas disponíveis podem abrir. **Visão aluno:** o mapa é informativo e **não abre o in-class** — casa que não leva a lugar nenhum não é botão.

•  Grade de quadrados precisa de **teto de largura**, ou o card cresce com a tela.

**9.1 Controles do card de aula**

**A ordem é fixa e declarada:** consulta de preparação · **abrir a aula** · **abrir o guia** · registro pós-aula. As duas ações de **entrar** na aula ficam juntas, no meio; as duas de **consulta** ficam nas pontas. Ordem de controle é decisão de tela — sem checagem, volta na próxima edição.

**Os painéis do card funcionam em acordeão, e o rótulo NÃO muda:**

•  **o botão nomeia o que abre, e continua nomeando depois de aberto.** Trocar para *Ocultar X* faz o botão nomear a **ação** em vez do **destino**, e quem lê perde de vista o que aquele controle é;

•  **abrir um painel fecha o outro** do mesmo card — o conteúdo anterior é substituído;

•  **clicar de novo no mesmo botão recolhe**;

•  **o grupo é o card, nunca a página.** Fechar o painel de outra aula ao abrir esta esconderia algo que o professor deixou aberto de propósito, para comparar;

•  **o estado sai do rótulo, então tem de estar em** **aria-expanded** — no botão que abriu **e** no irmão que fechou. Irmão com aria-expanded desatualizado é a tela mentindo para o leitor de tela, que é o defeito que o rótulo fixo poderia introduzir sem que nada acusasse.

**Fronteira declarada.** Isto vale para os painéis do **card de aula**. O expansor de conteúdo **dentro do deck** mantém o comportamento próprio — lá o gatilho é o único ponto de retorno, e a alternância do rótulo é o que diz como voltar. **A diferença é deliberada; diferença acidental entre dois expansores reprova.**

**10. Player de áudio — componente único**

•  **Dois controles lado a lado**, ambos sempre visíveis.

•  **O primeiro alterna** **Play** **e** **Pause****.** O segundo é **Stop**.

•  **Depois de** **Stop****,** **Play** **reinicia do começo.**

•  **Não criar três botões separados** para Play, Pause/Resume e Stop.

•  **Todos os players — pre-class e in-class — usam o mesmo componente.** Um transporte só; nada de mecanismo próprio por aula.

•  **O reset da atividade interrompe e reinicializa o áudio**, e o componente se **refaz** quando o bloco é restaurado — senão sobra o disparador sem transporte.

•  Ao iniciar um áudio, **pausar qualquer outro**. Estado em **texto** (tocando/pausado/terminado), não só em ícone, e **rótulo acessível** em todo botão.

•  Quando houver versões (velocidade, trecho, voz), elas são **seletores**, não botões de reprodução: parado, o seletor só seleciona; correndo, troca a faixa.

• Na produção final, cada player reproduz arquivo definitivo gerado pelo pipeline ElevenLabs. O componente não sintetiza, regenera nem transforma a fala em tempo de execução.

• O transcript exibido, o transcript enviado à geração e o arquivo reproduzido pertencem à mesma versão. A associação é registrada por identificador estável ou hash no manifesto de mídia.

• Falha de carregamento recebe mensagem dentro do documento e não autoriza fallback automático para síntese do navegador.

**11. Teclado, foco e Escape**

•  **Todo botão do deck precisa de guarda de foco.** O manipulador de teclas intercepta espaço e setas: sem a guarda, **o espaço avança o slide em vez de acionar o botão em foco**. A guarda é restrita às teclas de navegação.

•  **Hierarquia do Escape: diálogo/menu → interação ativa no exercício → aula.** Cada nível cede a vez ao de cima e consome o evento quando é o dono.

•  **Dois ouvintes de Escape no mesmo nó não se coordenam por ordem de registro.** Quem decide primeiro vai em **fase de captura** e corta com **stopImmediatePropagation**. **E ouvinte em captura cede a vez a quem está por cima**, ou o modal fica preso.

•  **Nunca** **confirm()** **nem** **alert()** — bloqueiam a página. Confirmação no documento, com armadilha de foco.

•  **Nada abre por hover.** Abertura por clique ou tecla, com aria-expanded.

**12. Interações do aluno**

•  **Escolha explícita, nunca sequência de cliques a descobrir.** Em classificação: o card se seleciona e **a coluna é o destino** — por clique, arrasto e teclado. Sem menu pendurado no card.

•  **Uma rota só de escrita:** todas as entradas passam pela mesma função, que é onde a marca da conferência anterior se limpa.

•  **O caminho por clique não consulta o estado de arrasto** — em toque o arrasto não existe.

•  **Não repintar no** **dragstart** (o navegador cancela o arrasto); dragleave precisa de guarda contra o próprio filho.

•  **Correção nunca só por cor:** símbolo na tela **e** frase para leitor de tela.

•  **O destino precisa de controle focalizável**, ou o teclado seleciona e não tem como dizer onde.

•  **Verbo de botão promete comportamento:** Check diz que corrige; se só revela, é See.

•  **Expandir preserva a rolagem**, abre para baixo, e o gatilho continua visível.

**13. Sistema visual**

•  **Contraste se mede sobre a superfície COMPOSTA**, nunca sobre o fundo nominal.

•  **Cor clara sobre escuro se deriva por cálculo**, não se escolhe no olho. Cor nova passa por allowlist — que cobre **hex e** **rgb**.

•  **Etiqueta de status e de modalidade não emprestam cor semântica.** *Conditional* em verde de sucesso faz a etiqueta dizer um juízo que ela não carrega.

•  **Cor se conserta na classe compartilhada, nunca por estilo local.**

•  **Toda distância estrutural sai de uma escala declarada** — zero literal estrutural. Ficam fora, declarados: borda, ícone, largura mínima e posicionamento absoluto.

• Duas famílias tipográficas disponíveis no próprio artefato, por token, com papel fixo. Não depender de webfont ou chamada externa. No protótipo, remover Google Fonts e validar a hierarquia com as famílias de sistema/fallback efetivamente disponíveis no publicado. Fonte licenciada só pode ser incorporada localmente quando houver autorização e empacotamento aprovados.

•  **Piso de tamanho é piso.** Falta de espaço não se resolve encolhendo abaixo do legível.

•  **Medida que depende de outro elemento se DERIVA, não se constanta**; posição de painel se **mede** em tempo de execução.

**14. Hierarquia da pergunta projetada**

Perguntas projetadas possuem identidade visual própria e utilizam uma das famílias já pertencentes ao sistema do material. A pergunta principal usa a família display, em itálico moderado e peso médio, com tamanho superior ao texto corrente e inferior ao título. Não utilizar uma terceira família tipográfica.

• A diferenciação não depende apenas do tamanho: combina família, estilo, espaçamento, largura controlada e cor institucional com contraste validado sobre o fundo composto. Perguntas longas permanecem em caixa normal e alinhadas à esquerda. Centralização é admitida somente quando a pergunta é curta, constitui o único foco da tela e mantém leitura confortável.

• Listas de perguntas, itens orientadores e quiz projetado utilizam a mesma família de referência, mas preservam componentes próprios, com tamanho, recuo, borda, peso e ritmo distintos. Compartilhar a família não torna .slide-question, .q-item e .slide .quiz-question componentes idênticos. Perguntas internas de formulário mantêm sua escala funcional.

• Pergunta de quiz projetada ocupa faixa própria entre o corpo e a pergunta principal, usando a família de referência com escala e ritmo do componente. Pergunta de formulário no pre-class não é ampliada nem convertida em pergunta projetada.

•  **A pergunta não carrega a instrução operacional junto:** nó que traz as duas se **parte**. A oração de que a pergunta depende gramaticalmente fica **com** ela.

•  **Tela cujo título já é a pergunta não ganha pergunta nova.** **As capas ficam fora.**

**15. Teacher's Guide na superfície projetada**

1.  o controle **nomeia** o que abre;

2.  abre por **ação deliberada**, nunca por aproximação;

3.  aberto, **permanece aberto**;

4.  o conteúdo **acompanha a unidade ativa**;

5.  **começa fechado a cada aula** — o estado não atravessa aulas, mas persiste dentro de uma;

6.  **não cobre o essencial**;

7.  **alcançável sem o ponteiro**.

Mais:

•  **A nota e as ações ficam em nós separados** — quem repinta a nota apagaria um botão vizinho.

•  **A janela ou aba separada é recurso adicional OBRIGATÓRIO na produção final — e não substitui de imediato o guia interno.** O guia dentro da aula se preserva como alternativa **até que a abertura separada esteja validada no ambiente oficial e a retirada dele seja deliberadamente autorizada.**

•  window.open **só funciona dentro do manipulador do clique**; adiado, o navegador bloqueia. **Janela bloqueada não passa em silêncio.**

•  **A janela lê a fonte, nunca uma cópia.**

•  **Sair da aula não fecha a janela do professor**; fechar a janela não quebra o deck; e reabrir tem de ser possível.

•  **A janela separada destina-se à consulta do professor.** Durante o compartilhamento, oriente que seja compartilhada **apenas a janela da aula**. **O Teacher's Guide não integra o conteúdo projetado para o aluno.**

•  O que **não** se faz é **prometer ocultação**: a orientação diz o que **fazer**, nunca que as notas ficam invisíveis — quem compartilha a tela inteira vê tudo.

**15.1 Abertura por aula, em janela ou aba separada**

•  **Cada card de aula da seção In-class, na visão professor, tem o controle que abre o guia daquela aula.** **O botão não existe na visão do aluno.**

•  **Ele fica ao lado do controle que abre a aula** (§9.1). A ordem dos controles é decisão de tela, e por isso é ela que a checagem guarda — senão volta na próxima edição do bloco.

•  **O rótulo inteiro é um só item de layout.** Botão que dispõe os filhos em flex com gap transforma texto solto e elemento irmão em **dois itens**, e o espaçamento entra **além** do espaço da frase: o rótulo aparece com espaço duplo. O gap existe para separar ícone de rótulo, não para partir uma frase.

•  **O rótulo desse botão segue o §16, não o inglês do deck.** O card é superfície que o professor lê **fora da projeção**: o verbo vai em **português** — Abrir o Teacher's Guide —, e só o **nome próprio do componente** fica em inglês, **marcado com** **lang** para o leitor de tela. Fixar aqui um rótulo em inglês criaria uma ilha de outra língua no meio de um cartão inteiramente português.

•  **O rótulo tem uma fonte só.** Onde o texto de apoio dentro da aula mandar usar o botão, ele **cita o rótulo visível** — duas cópias do mesmo nome divergem na primeira edição, e a orientação passa a mandar procurar um botão que não existe com aquele nome.

•  **O endereço deriva da URL corrente** — rota ou parâmetro, na forma ?mode=teacher-guide&lesson={id}. **Nenhum domínio, URL oficial, endereço de teste ou URL de artefato escrito à mão no código.** O card transmite o identificador da aula; a janela do guia o interpreta, **confere se a aula existe** e abre direto no início do guia correspondente.

•  **O nome técnico da janela deriva de identificadores do artefato e da aula.** Não contém nome literal nem qualquer dado pessoal do aluno, e **não é constante comum a todos os materiais** — nome igual em dois artefatos faz o guia de um **reaproveitar ou substituir** a janela do outro. O identificador do artefato é campo próprio do registro (§3), **único por material ou ciclo**, **sanitizado** antes de compor o nome da janela e **compartilhado pelas rotas do mesmo artefato**.

•  **No modo** **teacher-guide****:** só o guia da aula pedida; a aula **claramente identificada**; navegação pelas orientações correspondentes aos slides; **sem visão do aluno e sem controles do aluno**; **sem alterar slide, visão ou estado da janela principal**; **sem comunicação de estado entre materiais ou alunos diferentes**.

•  **O guia dentro da aula permanece disponível** como caminho alternativo enquanto a abertura separada não estiver validada no ambiente real do produto. **Removê-lo antes disso é defeito.**

•  **Janela bloqueada informa, brevemente, que o guia continua disponível dentro da aula.** Não se propõe fluxo manual de sincronização entre abas, e **não se afirma que a janela abriu quando ela não abriu** — retorno nulo de window.open é detectado, nunca silencioso.

•  **A limitação observada no artefato de revisão é do sandbox do host, não da solução.** Ela **não** vira limitação permanente do produto: o funcionamento definitivo se prova na URL real. O protocolo dos dois ambientes e o gate de publicação estão no **P2**; a matriz de prova, no **P3**.

**16. Língua e rótulos editoriais**

**Tudo o que se projeta é em inglês** — controles, modais, rótulos de abertura, feedback de atividade. Português fica no que o professor lê **fora** da projeção. O diálogo **descreve** o efeito em vez de citar rótulo que está em outra língua.

**American English em todo conteúdo produzido ou editado.** **Fonte externa autêntica preserva a variedade original**, e **citação literal não se corrige nem para uniformizar grafia** — as palavras do documento são o objeto da aula.

Rótulos consolidados, a usar sem variação:

| **Rótulo** | **Onde** |
|---|---|
| Visão professor · Visão aluno | alternador exclusivo da URL do professor |
| Pre-class · In-class · Post-class | abas — **as três com a mesma forma hifenizada** |
| Planning | aba do Planejamento **na visão do aluno** |
| Objetivo comunicativo: · Produto principal: | preparação da aula — **com dois-pontos** |
| Aulas neste ciclo / Lessons in this cycle | mapa do ciclo |
| Reset lesson · Finish lesson | controles do deck |
| Fechar todos os gabaritos desta aula · Reset my answers | fim do pre-class |
| What worked · Keep developing | únicos campos compartilhados com o aluno |

Mais: **nenhum tempo aparece na tela projetada**; **tempo não é critério de encerramento de produção**; **fechamento registra, não confere**; a nota do professor **orienta a condução, não justifica o desenho**, e é sempre *slide N*, nunca *tela N*.

**17. O que nunca aparece na interface**

**Limitações técnicas não aparecem na interface, salvo quando afetam diretamente a decisão ou a expectativa de quem usa** — como a indicação única de áudio provisório no modo protótipo, ou a informação de que uma gravação permanece no dispositivo.

•  O lugar da limitação técnica é o **relatório de validação**.

•  Quando ela precisar aparecer, aparece **uma vez**, em linguagem de consequência, nunca de implementação: *a gravação permanece neste dispositivo* — e não o nome do mecanismo que a guarda.

•  **Nunca** nome de tecnologia, decisão do gerador, funcionamento interno, justificativa de produção, hipótese de desempenho, diagnóstico, código interno ou scaffolding.

•  **Só prometa o que a plataforma sustenta.** Sem integração confirmada, não há envio: um controle de submissão só existe se a tela disser que é **simulação**.

**18. Consistência entre correção, resposta e Teacher's Guide**

**A resposta apresentada ao aluno e a orientação consultada pelo professor não podem divergir.**

A forma de garantir isso **depende da camada e do tipo de atividade** — e a distinção que governa tudo o que vem abaixo é entre **atividade fechada**, que tem resposta definida, e **atividade aberta**, que admite produção pessoal.

**Pre-class — atividades autocorrigíveis:**

•  a correção mostrada ao aluno e o **answer key** do professor indicam **a mesma resposta**;

•  **alternativas aceitáveis, rationale e transcript pertencem à mesma versão da atividade** — enunciado editado sem levá-los junto é a forma mais comum da divergência;

•  as respostas do aluno ficam disponíveis para consulta do professor;

•  **conteúdo reservado ao professor não aparece na visão do aluno, nem antes nem depois da tentativa**;

•  **rationale e alternativas aceitáveis entram quando são pedagogicamente pertinentes** — nunca como campo obrigatório artificial em toda atividade.

**In-class.** Respostas esperadas, critérios de aceite, alternativas possíveis e orientações de condução ficam **no Teacher's Guide**. Na tela projetada:

•  **a resposta não aparece antes da tentativa**;

•  **atividade fechada pode revelar a correção depois da tentativa, por** **Check**;

•  **quando o controle apenas mostra referência ou exemplo, o verbo é** **See** **ou** **Compare****, nunca** **Check** — o verbo promete comportamento (§12);

•  **guided discovery** pode apresentar **One possible answer**, contraste, regra ou modelo **depois** da tentativa;

•  **atividade aberta — discussão, simulação, role-play, produção oral, feedback — não recebe gabarito único**; depois da tentativa pode oferecer modelo de comparação, versão mais clara, critérios de sucesso ou apoio linguístico;

•  **o que a tela revela não pode divergir da orientação do guia.**

**Post-class.** A regra alcança **só as atividades autocorrigíveis**: correção e answer key concordam. Link externo, sugestão de leitura ou escuta, gravação e escrita aberta **não exigem gabarito**; fala e escrita opcionais **não recebem resposta única** quando admitem produção pessoal; e modelo de apoio se apresenta **como exemplo possível**, nunca como a resposta correta.

**Implementação — o que é preferência e o que é requisito.**

•  **A fonte única de dados é a arquitetura preferencial, não obrigação absoluta.** Sempre que viável, correção, feedback e answer key derivam da mesma fonte.

•  **Quando a natureza da atividade exigir representações separadas**, a validação **compara o conteúdo efetivamente apresentado em cada visão** e reprova qualquer divergência.

•  **A aprovação depende da ausência de divergência, não do uso de uma estrutura específica em JavaScript.**

•  **Nenhuma solução técnica reduz alternativas pedagogicamente aceitáveis a uma resposta única só para facilitar a automação.** Esse é o erro que a regra existe para impedir: automatizar a conferência estreitando a pedagogia.

**19. O que esta camada não implementa**

Fronteira da API de áudio. O HTML implementa reprodução, controles, estados e acessibilidade; não implementa a geração. A API da ElevenLabs pertence ao pipeline seguro de produção definido no Anexo P-A.

Limites desta camada funcional: **não simule autenticação, upload, armazenamento ou integração externa como se fossem reais.**

| **Requisito** | **Estatuto** |
|---|---|
| **Áudio em produção final** | **implementado no modo produção final** (§0); no modo protótipo, provisório e declarado |
| **Envio e integração do post-class** | **fora**: exige backend. Sem ele, não há envio |
| **Produção e incorporação de imagens** | **fora**, salvo o que for embutido; ativo estrutural externo é proibido (§2) |

**PARTE III — ENTREGA**

**20. Autovalidação obrigatória**

Antes de entregar, o gerador roda e **reporta** com evidência, no vocabulário do 06 §4: **PASSOU · PARCIAL · FALHOU · NÃO VERIFICADO**. *"NÃO VERIFICADO" é resposta legítima; "PASSOU" sem evidência não é.*

| **Camada** | **O que se prova** |
|---|---|
| Registro | metadados repetidos saem do registro; markup concorda com ele; conteúdo da aula intacto |
| Etapas | oito etapas do framework no registro, na mesma ordem; nenhuma etapa fictícia; quantidade de slides variável |
| Papel | a URL do aluno não recebe conteúdo, payload, estado ou recursos do professor |
| Pre-class | gabarito fechado no início; ação do professor não altera resposta do aluno; os dois controles no fim |
| Controles da aula | Reset e Finish presentes, com confirmação; conclusão só por Finish; reset restrito à aula |
| Registro pós-aula | escala com número; engajamento fora da média; três campos; só dois compartilhados |
| Player | dois controles; Play reinicia após Stop; um componente para todos |
| Teclado | espaço aciona o controle em foco — **e avança o slide quando o foco está fora** |
| Escape | diálogo → interação ativa → aula, nessa ordem |
| Contraste | medido sobre superfície composta, em todos os fundos, **com canário** |
| Língua | deck em inglês; American English; citação literal intacta; rótulos da tabela do §16 |
| Dependência externa | zero ativo **estrutural**; links editoriais do post-class **não contam** |
| Interface | nenhuma limitação técnica, nome de tecnologia ou decisão do gerador visível |
| Modo | o modo declarado bate com o áudio entregue |
| Consistência | toda atividade autocorrigível tem resposta definida; correção e answer key concordam; o que o in-class revela concorda com o guia; nenhuma resposta reservada chega antes ao aluno; **atividade aberta não foi convertida em resposta única**; rationale, alternativas e transcript são da mesma versão — e **uma divergência inserida de propósito é detectada** |
| Teacher's Guide | botão por aula na visão professor e ausente na do aluno; rota derivada da URL corrente, sem domínio fixo; cada card abre o guia certo; navegação no guia não mexe na janela principal; bloqueio detectado, com aviso e guia interno preservado |

O **protocolo de execução dessa validação** — como provar cada checagem, canário, caso negativo, controle positivo — está no **P2**. A **matriz de conformidade**, requisito a requisito, com evidência positiva, mutação correspondente, ambiente de execução e classificação do resultado, está no **P3**.

**21. Pare e declare quando**

•  o conteúdo pedagógico não couber sem ser alterado;

•  faltar dado material — **informação ausente não se inventa**;

•  uma regra desta camada colidir com uma pedagógica (a pedagógica vence; a colisão se declara);

•  o modo de entrega não tiver sido informado;

•  não for possível validar a versão final;

•  a única forma de cumprir um requisito for **prometer o que a plataforma não sustenta**.
