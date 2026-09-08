> **Documento normativo importado do Drive — nao editar aqui.**
> Origem: `P1_Camada_Funcional_HTML.docx`
> Drive ID: `1WteN8zCZ3ouQ8WRskG45PuoGSDH-wF_d`
> Modificado no Drive: 2026-09-05
> Reimportar: conector do Drive (`read_file_content` com o fileId acima). Os BYTES do .docx nao
> chegam integros por este caminho — em 08/09/2026 o round-trip corrompeu o zip em 2 de 3
> tentativas (CRC invalido) —, entao a importacao usa o texto renderizado pelo conector, e nao
> o `docx_to_md.py`.
> A fonte e o .docx no Drive. Divergencia entre este arquivo e o Drive se resolve reimportando,
> nunca editando o .md.

## P1 · CAMADA FUNCIONAL (HTML)

Especificação do meio de entrega — Private Class Alumni Black · adultos · A0/Pre-A1–C1 · C2 como referência superior para C1+

**Série P — plataforma.** Na versão vigente, o núcleo pedagógico validado compreende os documentos 00–06. A série P reúne especificações de plataforma externas ao núcleo — a camada que o 00 §6 retirou dele por decisão declarada: P1 (esta, o contrato funcional), P2 (protocolo de implementação e QA) e P3 (matriz de conformidade e especificação da suíte executável). A criação futura de documentos numerados após o 06 é possível, desde que seja deliberada e acompanhada da atualização do índice e das referências do Documento 00.

**Estatuto.** É a especificação separada do meio de entrega que o 00 §7 prevê como entrada e que o Documento 06 espera receber. Na precedência do 00 §4 ocupa o nono e último degrau. Uma decisão técnica nunca modifica silenciosamente uma regra pedagógica. Se o HTML não comportar o que a aula pede, quem cede é o HTML; não havendo como ceder, pare e declare.

**Uso.** Entregue ao gerador: o pacote 00–06, as entradas do 00 §7, e este documento. O gerador produz primeiro as saídas pedagógicas do 06 e só então converte em HTML. A conversão não altera conteúdo: se algo precisar mudar para caber na tela, isso é achado pedagógico e volta uma etapa — não se resolve aqui.

### 0. Dois modos de entrega

Toda regra abaixo vale nos dois modos, salvo onde indicado.

| Modo | Quando | Áudio | Declaração |
| :-: | :-: | :-: | :-: |
| Protótipo / validação | antes da aprovação do conteúdo | síntese do navegador identificada como provisória | o material declara que o áudio não é final |
| Produção final | material aprovado, para uso em aula | áudios definitivos gerados pela API da ElevenLabs no pipeline seguro de produção, vinculados à versão aprovada do transcript e entregues como arquivos de mídia | sem aviso de provisoriedade e sem síntese executada no navegador |

O modo é entrada obrigatória do pipeline e não pode ser deixado indefinido. A validação não confia somente nessa declaração: infere o modo efetivamente entregue pelos recursos e mecanismos presentes no build e verifica sua correspondência. Em produção final, síntese do navegador é defeito; em protótipo, é o mecanismo provisório esperado.

#### 0.1 Fonte obrigatória do áudio na produção final

Na produção final, todo áudio criado automaticamente para o material oficial é gerado pela API da ElevenLabs, conforme o Anexo P-A — Padrão de Produção de Áudios com ElevenLabs. A síntese nativa do navegador, incluindo Web Speech API, `speechSynthesis` e `SpeechSynthesisUtterance`, é **proibida** no artefato final.

A chamada à API ocorre somente no ambiente seguro do pipeline, antes da publicação. Chaves, tokens, cabeçalhos de autenticação e chamadas autenticadas à ElevenLabs nunca aparecem no HTML, no JavaScript entregue, no armazenamento local, no console ou em requisições iniciadas pelo navegador do aluno ou do professor.

O build recebe arquivos definitivos vinculados ao transcript aprovado. Qualquer alteração no transcript invalida o arquivo anterior e exige nova geração, nova associação e nova validação auditiva. O anexo governa modelo, vozes, parâmetros, pré-processamento, nomenclatura e QA; o P1 governa como o áudio aprovado é entregue e controlado na interface.

## PARTE I — O QUE PRODUZIR

### 1. O artefato

A produção final entrega **duas URLs e dois builds separados por papel**. O build do professor contém a visão docente e uma prévia fiel da visão do aluno. O build do aluno contém exclusivamente a visão do aluno. Protótipo interno pode usar um único arquivo com alternância somente quando o modo protótipo estiver explicitamente declarado.

| Camada / aba | Visão | Função |
| :-: | :-: | :-: |
| Perfil | professor · aluno (recorte próprio) | quem é o aluno |
| Planejamento — Planning na visão do aluno | professor · aluno | projeção do ciclo |
| Pre-class | aluno responde · professor consulta | preparação |
| In-class | professor | deck projetado |
| Feedback | aluno | recebe os dois campos que o professor compartilha |
| Post-class | aluno | continuação |

A aba Feedback é camada funcional obrigatória na visão do aluno: é onde chegam What worked e Keep developing — e só esses dois.

Na URL do professor, os rótulos Visão professor e Visão aluno alternam entre a área docente e a prévia discente. Na URL do aluno não existe alternador, rota de professor nem conteúdo docente incorporado. Os identificadores internos `professor` e `aluno` governam roteamento e armazenamento, sem permitir promoção de papel por parâmetro editável.

**Separação de entrega.** Conteúdo docente não pode estar apenas oculto por CSS, atributo, template, comentário ou condição JavaScript. Teacher's Guide, answer keys reservados, hipóteses pedagógicas, registros internos, evidências restritas e controles administrativos **não integram o HTML, o payload, o estado persistido ou os recursos enviados ao navegador do aluno**.

### 2. Dependência externa — a distinção que decide

O funcionamento e a identidade do artefato não podem depender de ativos externos. Links editoriais do post-class para fontes autênticas são permitidos e, quando previstos pedagogicamente, obrigatórios — e não contam como dependência estrutural.

| Categoria | Estatuto |
| :-: | :-: |
| Ativo estrutural externo — fonte tipográfica, imagem, script, CSS, biblioteca, ícone | proibido. O CSP do meio de publicação bloqueia host externo: o ativo não chega a ser projetado e a fonte passa a divergir do publicado em silêncio |
| Link editorial do post-class — artigo, vídeo, podcast, YouGlish, dicionário | permitido e às vezes obrigatório (06, post-class: pelo menos uma leitura e uma escuta/vídeo externas autênticas) |

Consequências práticas: aberturas de aula são composições em CSS; o logotipo vai embutido, do arquivo oficial, nunca reconstruído em texto; e a validação conta ativos estruturais, não links de navegação.

### 3. Registro único — escopo delimitado

Para metadados estruturais repetidos, uma referência compartilhada é a solução preferencial para prevenir divergências. Quando houver representações separadas, sua correspondência deve ser validada. Esta regra **NÃO** obriga correção, answer key, feedback e Teacher's Guide a derivarem tecnicamente da mesma fonte; nesses casos, o requisito obrigatório é a ausência de divergência (§18).

O registro é para **metadados estruturais repetidos**, não para o conteúdo da aula.

Nome do aluno, tamanho do ciclo, nível, número de aulas, estado, título de aula, framework, etapas e demais metadados repetidos saem do registro único. Dados pedagógicos e fatos do conteúdo permanecem no conteúdo da aula.

Datas, números de processo, citações, títulos de documento, trechos e qualquer fato autêntico da aula ficam onde estão — não vão para registro.

```js
var ARTEFATO={id:'…'}; // identificador TÉCNICO: sem dado pessoal
var ALUNO={nome:'…',sobrenome:'…'}; // NEUTRO; sobrenome é campo PRÓPRIO
var CICLO={numero:…,aulas:…,nivel:'…',rotulo:'…',rotuloAluno:'…'};
var LESSONS={ n:{ n:…, bloco:…, mod:'…', cod:'…', fwNome:'…', tema:'…', temaPre:'…',
  stages:[{n:'…',min:…}, …], nav:[…] } };
```

- Identificador técnico é NEUTRO, e não varia de forma nem de gênero. Um único par governa tudo: `aluno` e `professor` — o mesmo dos rótulos internos do §1, que já governam `data-view`. Daí saem o nome do registro (`ALUNO`) e os espaços de estado (§5). Nada de `ALUNA`, `aluna`, `prof` ou `shared` convivendo com eles: identificador que muda de forma conforme o perfil deixa de ser identificador — vira rótulo, e obriga a editar código a cada aluno novo. O gênero da prosa segue a pessoa; o do identificador, ninguém.
- `ARTEFATO.id` é identificador técnico, não rótulo. Único por material ou ciclo, sem nome nem sobrenome do aluno, estável, e é dele que saem os nomes de janela e as chaves que precisam distinguir materiais abertos ao mesmo tempo (§15.1). Dado pessoal em identificador técnico vaza para fora da interface e sobrevive a toda troca de rótulo.
- O texto no markup é só estado inicial; quem pinta é a repintura, por `data-lf`. O estado inicial tem de concordar com o registro — divergir faz a tela piscar o valor errado.
- Nome: duas regras sobre o mesmo registro. Identificação (página inicial, título da aba) usa o nome inteiro; prosa do Perfil e do Planejamento usa só o primeiro nome.
- Se algo passar a repetir um valor do registro, ligue por `data-lf` e acrescente a comparação à validação.

### 4. Etapas e telas

Cada framework possui **oito etapas pedagógicas normativas**, definidas pelo Documento 03. A camada HTML representa as oito na mesma ordem, sem estabelecer quantidade fixa de slides.

O registro recebe exatamente as oito etapas do framework. O HTML não acrescenta, elimina, duplica ou reordena etapas. A checagem exige oito etapas, mas deriva livremente a quantidade de slides da distribuição declarada.

Sobre telas:

- cada etapa está representada e navegável;
- uma tela pode reunir atividades relacionadas;
- duas etapas só compartilham uma tela quando houver dependência pedagógica real — por exemplo feedback e retask condicional, quando a retomada depende diretamente do que acabou de ser construído;
- quando isso ocorrer, declare no registro, por atributo próprio, sem criar etapa fictícia e sem sequenciamento paralelo;
- não existe quantidade universal de telas — ela sai do conteúdo.

Hierarquia de atividade é arquitetura, não etiqueta. Conteúdo Conditional, Extension e Optional começa recolhido, num controle dentro da tela essencial, e não ganha tela própria.

Quando o status integra o nome da ação, ele compõe o rótulo completo de um ÚNICO botão — por exemplo `Optional follow-up` — e nunca aparece como fragmento separado. Não duplicar o status em etiqueta e botão.

A distinção é entre etiqueta visual e rótulo funcional: etiqueta de status que existe por si fica fora do botão; status que faz parte do nome da ação vai dentro dele, inteiro. Partir `Optional` de `Optional follow-up` é o defeito que a regra existe para impedir — e a palavra do status é dita uma vez só.

## PARTE II — REGRAS FUNCIONAIS

### 5. Papel e estado

- Estado separado por PAPEL: três espaços — aluno, professor, compartilhado —, roteados por prefixo. Os nomes são os do §3: um par só, neutro, igual ao que governa `data-view`.
- Regra assimétrica: o que o aluno faz, o professor consulta; o que o professor faz não aparece na visão do aluno — separação de armazenamento, não de CSS.
- Trava de CSS não é guarda. `pointer-events` impede o clique, não a chamada: a marca mudava na tela enquanto a gravação recusava, e a tela mentia para o professor. A guarda vai em cada porta de escrita.
- Persistência por `data-k` no próprio elemento, nunca por lista de ids no boot.
- Metade das respostas não é campo — vive em classe (opção selecionada, marca de certo/errado). Persista a posição das marcas por bloco, com ouvinte delegado.
- Reset que limpa campo a campo não reseta nada: restaure o HTML inicial do bloco, com a cópia tirada depois de montar o gabarito e antes de preencher.
- Migrar o bucket anterior é obrigatório, trabalhando no armazenamento bruto — a leitura filtrada por papel não enxerga o espaço do professor e perderia o texto em silêncio.
- Renomear um espaço é migração, não substituição — e a ORDEM entre migrações decide. Quando houver mais de uma, a que renomeia vem antes da que classifica. O motivo é mecânico: a migração que classifica costuma se disparar por "nenhum espaço existe", e um bucket na convenção antiga responde exatamente isso. Tratado como não classificado, ele teria a função de classificação aplicada aos próprios espaços — as chaves aluno, professor e compartilhado cairiam todas no destino padrão, e o pre-class do aluno reapareceria dentro do espaço do professor. Nada falha, nada avisa. Migração se prova com o bucket de cada formato já existente, e com o canário que confirma que a ordem invertida seria pega.

### 6. Pre-class — gabarito, respostas e reset

- Answer key começa fechado.
- O professor abre e fecha o gabarito de cada atividade.
- As respostas registradas do aluno aparecem para o professor em representação estática equivalente. Na visão docente, mecanismos de resposta não permanecem como controles interativos nem desabilitados: alternativas, selects, checkboxes, radios, campos e cards arrastáveis tornam-se texto, linha, etiqueta, cartão ou tabela sem semântica de controle. A representação distingue resposta registrada, ausência de resposta e, quando aplicável, estado de correção, sem permitir alteração.
- Ações do professor não alteram as respostas do aluno — nem por acidente, nem por repintura.
- Controle geral do professor: **Fechar todos os gabaritos desta aula** — e ele tem de alcançar também os painéis criados por script, que não têm id próprio.
- Controle do aluno: **Reset my answers**.
- Ambos aparecem no fim do pre-class, depois de todo o conteúdo — no topo, apareceriam antes de haver o que resetar ou fechar.
- Reset exige confirmação, no documento, nunca por diálogo nativo.

### 7. Controles da aula — obrigatórios

- **Reset lesson** e **Finish lesson** são obrigatórios no deck.
- Ambos exigem confirmação antes de executar.
- A conclusão independe de checklist.
- Finish lesson é a única fonte do estado "realizada". Nem visita a slide, nem checklist, nem posição no deck produzem conclusão. "Visitado" não é "concluído".
- O reset é restrito à aula ativa — nunca alcança as outras.

### 8. Registro pós-aula

- Escala linguística de 1 a 5, igual para os três critérios, guardando o **número**, não a palavra — sem ele não há média nem evolução.
- Critérios: Fala e interação · Compreensão auditiva · Precisão estrutural.
- Engajamento tem escala própria e fica FORA da média de desempenho linguístico.
- A escala de Desempenho é uniforme nas quatro aulas do bloco por implementação e estado, mas **essa regra não aparece como nota editorial ou metalinguística na interface**. O professor vê somente o critério, os descritores e os controles de registro.
- Três campos escritos: Evidência observável · Ponto prioritário de desenvolvimento · Próxima ação.
- Os três campos alinham-se em colunas iguais no desktop e em uma coluna em telas menores. Grade genérica com auto-fit não serve para número fixo de campos: cai em duas colunas mais uma isolada. Use colunas explícitas, com alinhamento entre elas — senão o título mais longo empurra o próprio campo para baixo dos vizinhos.
- Só What worked e Keep developing chegam ao aluno, na aba Feedback.
- Botões para confirmar e para limpar/refazer o registro. Confirmação gravada, que sobrevive à recarga e cai na primeira edição — botão "salvar" em tela com autosave é promessa vazia.
- Proibido justificar tecnicamente na interface: nada de explicar cálculo de média, armazenamento numérico ou por que a opção guarda o número. A regra vive na lógica; a tela recebe descrição funcional.
- O resumo para o checkpoint dá média, série e contagem — nunca veredito.

### 9. Mapa das aulas do ciclo

- Título: **Aulas neste ciclo / Lessons in this cycle**.
- Um minicard quadrado por aula do ciclo, derivado do registro — nunca contado à mão.
- Estados: realizada (nítida) · disponível e não realizada (estado próprio) · ainda indisponível (menor ênfase).
- Estado nunca identificado só pela cor — três sinais, e nenhum deles cromático sozinho: marca, traço da borda e presença do código.
- Menos ênfase se faz com token de texto mais fraco, nunca com `opacity`, que derruba o contraste sem controle.
- Conclusão vem de Finish lesson, não de visita.
- Visão professor: aulas disponíveis podem abrir. Visão aluno: o mapa é informativo e não abre o in-class — casa que não leva a lugar nenhum não é botão.
- Grade de quadrados precisa de teto de largura, ou o card cresce com a tela.

#### 9.1 Controles do card de aula

A ordem é fixa e declarada: consulta de preparação · abrir a aula · abrir o guia · registro pós-aula. As duas ações de entrar na aula ficam juntas, no meio; as duas de consulta ficam nas pontas. Ordem de controle é decisão de tela — sem checagem, volta na próxima edição.

Os painéis do card funcionam em acordeão, e o rótulo NÃO muda:

- o botão nomeia o que abre, e continua nomeando depois de aberto. Trocar para `Ocultar X` faz o botão nomear a ação em vez do destino, e quem lê perde de vista o que aquele controle é;
- abrir um painel fecha o outro do mesmo card — o conteúdo anterior é substituído;
- clicar de novo no mesmo botão recolhe;
- o grupo é o card, nunca a página. Fechar o painel de outra aula ao abrir esta esconderia algo que o professor deixou aberto de propósito, para comparar;
- o estado sai do rótulo, então tem de estar em `aria-expanded` — no botão que abriu e no irmão que fechou. Irmão com `aria-expanded` desatualizado é a tela mentindo para o leitor de tela, que é o defeito que o rótulo fixo poderia introduzir sem que nada acusasse.

**Fronteira declarada.** Isto vale para os painéis do card de aula. O expansor de conteúdo dentro do deck mantém o comportamento próprio — lá o gatilho é o único ponto de retorno, e a alternância do rótulo é o que diz como voltar. A diferença é deliberada; diferença acidental entre dois expansores reprova.

### 10. Player de áudio — componente único

- Dois controles lado a lado, ambos sempre visíveis.
- O primeiro alterna Play e Pause. O segundo é Stop.
- Depois de Stop, Play reinicia do começo.
- Não criar três botões separados para Play, Pause/Resume e Stop.
- Todos os players — pre-class e in-class — usam o mesmo componente. Um transporte só; nada de mecanismo próprio por aula.
- O reset da atividade interrompe e reinicializa o áudio, e o componente se refaz quando o bloco é restaurado — senão sobra o disparador sem transporte.
- Ao iniciar um áudio, pausar qualquer outro. Estado em texto (tocando/pausado/terminado), não só em ícone, e rótulo acessível em todo botão.
- Quando houver versões (velocidade, trecho, voz), elas são seletores, não botões de reprodução: parado, o seletor só seleciona; correndo, troca a faixa.
- Na produção final, cada player reproduz arquivo definitivo gerado pelo pipeline ElevenLabs. O componente não sintetiza, regenera nem transforma a fala em tempo de execução.
- O transcript exibido, o transcript enviado à geração e o arquivo reproduzido pertencem à mesma versão. A associação é registrada por identificador estável ou hash no manifesto de mídia.
- Falha de carregamento recebe mensagem dentro do documento e não autoriza fallback automático para síntese do navegador.

### 11. Teclado, foco e Escape

- Todo botão do deck precisa de guarda de foco. O manipulador de teclas intercepta espaço e setas: sem a guarda, o espaço avança o slide em vez de acionar o botão em foco. A guarda é restrita às teclas de navegação.
- Hierarquia do Escape: diálogo/menu → interação ativa no exercício → aula. Cada nível cede a vez ao de cima e consome o evento quando é o dono.
- Dois ouvintes de Escape no mesmo nó não se coordenam por ordem de registro. Quem decide primeiro vai em fase de captura e corta com `stopImmediatePropagation`. E ouvinte em captura cede a vez a quem está por cima, ou o modal fica preso.
- Nunca `confirm()` nem `alert()` — bloqueiam a página. Confirmação no documento, com armadilha de foco.
- Nada abre por hover. Abertura por clique ou tecla, com `aria-expanded`.

### 12. Interações do aluno

- Escolha explícita, nunca sequência de cliques a descobrir. Em classificação: o card se seleciona e a coluna é o destino — por clique, arrasto e teclado. Sem menu pendurado no card.
- Uma rota só de escrita: todas as entradas passam pela mesma função, que é onde a marca da conferência anterior se limpa.
- O caminho por clique não consulta o estado de arrasto — em toque o arrasto não existe.
- Não repintar no `dragstart` (o navegador cancela o arrasto); `dragleave` precisa de guarda contra o próprio filho.
- Correção nunca só por cor: símbolo na tela e frase para leitor de tela.
- O destino precisa de controle focalizável, ou o teclado seleciona e não tem como dizer onde.
- Verbo de botão promete comportamento: `Check` diz que corrige; se só revela, é `See`.
- Expandir preserva a rolagem, abre para baixo, e o gatilho continua visível.

### 13. Sistema visual

O **Kit de Layout Alumni Black** incluído em `/referencias` é a referência canônica da aparência. Esta seção traduz seus contratos visuais; nenhuma regra do Kit altera comandos, estados, persistência, isolamento por papel, acessibilidade funcional ou comportamento definidos nas demais seções.

- **Paleta clara:** página osso `#F7F5F1`; cartões `#FFFFFF`; plano elevado `#F3F0EA`; plano recuado `#EFEAE1`; texto forte `#2E2E2C`; texto intermediário `#5E584F`; texto secundário `#6E6961`. Ouro para texto `#886308`; ouro para preenchimento com texto branco `#996F09`; ouro profundo `#644906`; ouro original `#B8860B` somente em filetes, bordas, ícones e contornos quando a medição permitir.
- **Paleta escura:** fundo Onyx `#08080A`; superfície Grafite `#15151B`; texto `#F4F4F6`; texto intermediário `#C2C2CC`; texto secundário `#9FA0AC`; acento `#E0B34A`; progresso visitado `#C8951F`. Os fundos escuros pertencem à mesma família visual da página, com alternância de profundidade, não a uma identidade paralela.
- **Cores semânticas** são reservadas ao seu papel: sucesso `#12633C`, perigo `#A8121C` e alerta `#7A5709` em superfícies claras; `#4ADE80`, `#F87171` e `#E0B34A` em superfícies escuras. Modalidades usam ESP `#5E584F`, Listening `#1D4FD8`, Grammar `#2E2E2C` e Reading `#886308`. Conditional, Extension e Optional usam tokens próprios; não emprestam cor de sucesso, erro ou alerta.
- **Hierarquia de superfície:** página plana → cartão elevado → linha ou área recuada → controle elevado. Cartões usam hairline discreto e sombra dupla quente; borda dura não substitui elevação. A borda de separação `#E7E1D7` é decorativa; quando a borda identifica componente, usar o token de limite `#8D8D98` ou outro indicador que cumpra §13.1.
- **Tipografia por função:** display para títulos e destaques editoriais; interface para corpo, instruções, dados e controles; question para perguntas projetadas; marca apenas para o qualificador do lockup. No Kit, os papéis correspondem a Jost, Inter, Cormorant e Poppins. Esses nomes só podem ser usados quando os ativos licenciados estiverem incorporados localmente; sem eles, valem as pilhas de sistema/fallback declaradas. É proibida chamada estrutural a Google Fonts ou outro host.
- **Pesos permitidos:** 300, 400, 600 e 700. Alturas de linha por função: 1.2, 1.45, 1.5, 1.62 e 1.85. Tracking negativo aplica-se somente a títulos a partir de 1.3rem; tracking positivo aplica-se somente a caixa alta curta e marca. Texto corrente não recebe letter-spacing decorativo.
- **Piso tipográfico:** `.55rem` somente para etiqueta curta em caixa alta com espaçamento; `.76rem` para texto corrente. Falta de espaço se resolve por composição, quebra, largura ou densidade, nunca encolhendo abaixo do piso.
- Toda distância estrutural deriva da escala de espaço do Kit, de `.125rem` a `3rem`, incluindo os meios-degraus declarados. Ficam fora apenas espessura de borda, tamanho de ícone, largura mínima, posicionamento absoluto e deslocamentos estruturais superiores a 3rem. Valor literal novo exige justificativa como exceção nomeada.
- **Raios** seguem o tamanho da caixa: 6px, 10px, 14px, 18px, 24px e pill. Não escolher raio por gosto nem transformar caixas pequenas em cápsulas acidentais.
- Capa e barra fixa preservam o lockup Alumni Black: capa com wordmark, filete dourado e qualificador black; barra compacta com símbolo quando o lockup completo violaria o tamanho mínimo ou consumiria o deck. A zona de proteção da marca permanece livre. Não usar "Alumni by Better" dentro do lockup Black.
- A capa usa campo Onyx/Grafite com uma única origem de luz dourada e grão incorporado; evita grade decorativa, múltiplos focos cromáticos e ativo externo. O ouro permanece acento minoritário. O conteúdo alinha-se à mesma coluna da página.
- O In-class em modo slide usa fundo escuro, barra fixa, progresso por etapas e superfícies Grafite/Noir. O conteúdo de consulta usa fundo osso, cartões claros e largura de leitura controlada. Grades são responsivas; tabelas extensas possuem contêiner rolável sem cortar conteúdo.
- Cor, tipografia, espaço, raio, elevação e movimento se corrigem no token ou na classe compartilhada, nunca por remendo local. Propriedade visual duplicada mais abaixo no CSS não pode restabelecer paleta ou composição anterior por cascata.
- Movimento é discreto e funcional. A rotação do anel da marca e transições respeitam `prefers-reduced-motion`; nenhum efeito pode deslocar conteúdo, ocultar foco ou impedir operação.

#### 13.1 Percepção de componentes e estados interativos

O indicador visual necessário para reconhecer um componente interativo atinge contraste mínimo de 3:1 em relação às cores adjacentes. O indicador pode ser borda, preenchimento, forma, ícone ou outra característica visual. Quando a borda é o elemento necessário para identificar o componente, ela cumpre integralmente a razão de 3:1; borda meramente decorativa não precisa cumpri-la isoladamente quando outro indicador conforme identifica o componente de modo inequívoco.

Foco, seleção, expansão, revelação, resposta correta, resposta incorreta e estado desabilitado são perceptíveis e não dependem exclusivamente de alteração sutil de cor. A diferenciação pode combinar contraste, preenchimento, espessura, contorno externo, ícone, marca, texto ou mudança de forma. O indicador de foco permanece visível.

Hover é reforço visual apenas nos dispositivos que o suportam. Não é o único meio de comunicar interatividade ou estado, e todo comportamento disponível por hover permanece identificável e acionável por teclado e toque.

### 14. Hierarquia da pergunta projetada

Perguntas projetadas usam o token question do Kit: Cormorant itálico quando o ativo local estiver disponível, com Georgia/Times como fallback. É uma exceção editorial deliberada e não autoriza outras famílias serifadas. A pergunta principal permanece maior que o corpo, menor que o título, com peso visual intermediário, largura controlada e contraste medido.

- A diferenciação combina família, itálico real, escala, ritmo, largura e cor; nunca depende apenas do tamanho. Perguntas longas ficam em caixa normal e alinhadas à esquerda. Centralização só ocorre quando a pergunta é curta, constitui o único foco da tela e permanece confortável nas larguras suportadas.
- Listas orientadoras e quiz projetado podem apontar para o mesmo token question, mas preservam escala, recuo, borda e ritmo próprios. Compartilhar a família não torna `.slide-question`, `.q-item` e `.slide .quiz-question` componentes idênticos. Perguntas internas de formulário mantêm a tipografia de interface.
- Na tela de abertura, a pergunta comunicativa integra o bloco introdutório e segue a família, o peso, a cor e a hierarquia do subtítulo; não recebe o tratamento das perguntas internas.
- A pergunta não incorpora instrução operacional. Tela cujo título já é a pergunta não cria pergunta duplicada.

### 15. Teacher's Guide na superfície projetada

1. o controle nomeia o que abre;
2. abre por ação deliberada, nunca por aproximação;
3. aberto, permanece aberto;
4. o conteúdo acompanha a unidade ativa;
5. começa fechado a cada aula — o estado não atravessa aulas, mas persiste dentro de uma;
6. não cobre o essencial;
7. alcançável sem o ponteiro.

Mais:

- A nota e as ações ficam em nós separados — quem repinta a nota apagaria um botão vizinho.
- A janela ou aba separada é recurso adicional OBRIGATÓRIO na produção final — e não substitui de imediato o guia interno. O guia dentro da aula se preserva como alternativa até que a abertura separada esteja validada no ambiente oficial e a retirada dele seja deliberadamente autorizada.
- `window.open` só funciona dentro do manipulador do clique; adiado, o navegador bloqueia. Janela bloqueada não passa em silêncio.
- A janela lê a fonte, nunca uma cópia.
- Sair da aula não fecha a janela do professor; fechar a janela não quebra o deck; e reabrir tem de ser possível.
- A janela separada destina-se à consulta do professor. Durante o compartilhamento, oriente que seja compartilhada apenas a janela da aula. O Teacher's Guide não integra o conteúdo projetado para o aluno.
- O que não se faz é prometer ocultação: a orientação diz o que fazer, nunca que as notas ficam invisíveis — quem compartilha a tela inteira vê tudo.

#### 15.1 Abertura por aula, em janela ou aba separada

- Cada card de aula da seção In-class, na visão professor, tem o controle que abre o guia daquela aula. O botão não existe na visão do aluno.
- Ele fica ao lado do controle que abre a aula (§9.1). A ordem dos controles é decisão de tela, e por isso é ela que a checagem guarda — senão volta na próxima edição do bloco.
- O rótulo inteiro é um só item de layout. Botão que dispõe os filhos em flex com gap transforma texto solto e elemento irmão em dois itens, e o espaçamento entra além do espaço da frase: o rótulo aparece com espaço duplo. O gap existe para separar ícone de rótulo, não para partir uma frase.
- O rótulo desse botão segue o §16, não o inglês do deck. O card é superfície que o professor lê fora da projeção: o verbo vai em português — **Abrir o Teacher's Guide** —, e só o nome próprio do componente fica em inglês, marcado com `lang` para o leitor de tela. Fixar aqui um rótulo em inglês criaria uma ilha de outra língua no meio de um cartão inteiramente português.
- O rótulo tem uma fonte só. Onde o texto de apoio dentro da aula mandar usar o botão, ele cita o rótulo visível — duas cópias do mesmo nome divergem na primeira edição, e a orientação passa a mandar procurar um botão que não existe com aquele nome.
- O endereço deriva da URL corrente — rota ou parâmetro, na forma `?mode=teacher-guide&lesson={id}`. Nenhum domínio, URL oficial, endereço de teste ou URL de artefato escrito à mão no código. O card transmite o identificador da aula; a janela do guia o interpreta, confere se a aula existe e abre direto no início do guia correspondente.
- O nome técnico da janela deriva de identificadores do artefato e da aula. Não contém nome literal nem qualquer dado pessoal do aluno, e não é constante comum a todos os materiais — nome igual em dois artefatos faz o guia de um reaproveitar ou substituir a janela do outro. O identificador do artefato é campo próprio do registro (§3), único por material ou ciclo, sanitizado antes de compor o nome da janela e compartilhado pelas rotas do mesmo artefato.
- No modo `teacher-guide`: só o guia da aula pedida; a aula claramente identificada; navegação pelas orientações correspondentes aos slides; sem visão do aluno e sem controles do aluno; sem alterar slide, visão ou estado da janela principal; sem comunicação de estado entre materiais ou alunos diferentes.
- Entrada e prioridade: a rota abre diretamente no slide solicitado. No topo aparecem somente aula, título, slide ativo, etapa e minutagem; a orientação operacional do slide vem imediatamente depois.
- **Lesson overview:** informações gerais aparecem uma única vez em componente inicialmente recolhido. O componente não se expande automaticamente ao abrir o guia nem ao navegar entre slides.
- Não repetir antes de cada orientação o bloco geral de identidade, objetivos, produto, critérios, preparação ou percurso. Answer Key, Possible Answers, apoios, decisões e evidências específicas permanecem associados ao slide ou à atividade correspondente.
- Estrutura e preparação, Lesson overview e cabeçalhos reutilizam o mesmo estado ou registro. Uma reapresentação pode ser somente leitura; nenhuma delas cria uma segunda fonte editável.
- O guia dentro da aula permanece disponível como caminho alternativo enquanto a abertura separada não estiver validada no ambiente real do produto. Removê-lo antes disso é defeito.
- Janela bloqueada informa, brevemente, que o guia continua disponível dentro da aula. Não se propõe fluxo manual de sincronização entre abas, e não se afirma que a janela abriu quando ela não abriu — retorno nulo de `window.open` é detectado, nunca silencioso.
- A limitação observada no artefato de revisão é do sandbox do host, não da solução. Ela não vira limitação permanente do produto: o funcionamento definitivo se prova na URL real. O protocolo dos dois ambientes e o gate de publicação estão no P2; a matriz de prova, no P3.

### 16. Língua e rótulos editoriais

Tudo o que se projeta é em inglês — controles, modais, rótulos de abertura, feedback de atividade. Português fica no que o professor lê fora da projeção. O diálogo descreve o efeito em vez de citar rótulo que está em outra língua.

American English em todo conteúdo produzido ou editado. Fonte externa autêntica preserva a variedade original, e citação literal não se corrige nem para uniformizar grafia — as palavras do documento são o objeto da aula.

Rótulos consolidados, a usar sem variação:

| Rótulo | Onde |
| :-: | :-: |
| Visão professor · Visão aluno | alternador exclusivo da URL do professor |
| Pre-class · In-class · Post-class | abas — as três com a mesma forma hifenizada |
| Planning | aba do Planejamento na visão do aluno |
| Objetivo comunicativo: · Produto principal: | preparação da aula — com dois-pontos |
| Aulas neste ciclo / Lessons in this cycle | mapa do ciclo |
| Reset lesson · Finish lesson | controles do deck |
| Fechar todos os gabaritos desta aula · Reset my answers | fim do pre-class |
| What worked · Keep developing | únicos campos compartilhados com o aluno |

Mais: nenhum tempo aparece na tela projetada; tempo não é critério de encerramento de produção; fechamento registra, não confere; a nota do professor orienta a condução, não justifica o desenho, e é sempre slide N, nunca tela N.

#### 16.1 Slide e screen — referentes diferentes

Slide é a unidade numerada ou identificável do deck In-class. Screen é uma visão, interface, modo ou estado técnico que não corresponde necessariamente a um slide. Por isso, o texto visível e o Teacher's Guide usam Slide N, next slide, second-listening slide, input slide e preparation slide quando se referem ao percurso do deck; screen permanece válido em expressões como teacher view, consultation screen, login screen ou em um estado funcional específico.

A distinção editorial não renomeia automaticamente a implementação. Identificadores técnicos como `.screen` podem permanecer quando nomeiam a estrutura ou o estado da interface, enquanto `.slide` e `data-slide` identificam unidades do deck. Em uma estrutura que contém uma screen e, dentro dela, um slide, cada termo conserva sua função.

First-listening screen só é correto quando identifica um estado da experiência auditiva; se nomear o slide usado para a primeira escuta, usar first-listening slide. Toda ocorrência deve ser validada pelo referente real. É proibida a substituição global de screen por slide.

### 17. O que nunca aparece na interface

Limitações técnicas não aparecem na interface, salvo quando afetam diretamente a decisão ou a expectativa de quem usa. No modo protótipo, o estado provisório do áudio é informado uma única vez no artefato, na primeira área autônoma da visão do aluno que contenha áudio, sem explicar tecnologia. O aviso não é repetido no Teacher's Guide, nos cartões de preparação nem nas notas de slide. Ao professor pode ser apresentada somente a ação operacional de verificar se o áudio funciona, sem nova declaração de provisoriedade. Informações como a permanência de uma gravação no dispositivo seguem a mesma regra de consequência, não de implementação.

- O lugar da limitação técnica é o relatório de validação.
- Quando ela precisar aparecer, aparece uma vez, em linguagem de consequência, nunca de implementação: *a gravação permanece neste dispositivo* — e não o nome do mecanismo que a guarda.
- Nunca nome de tecnologia, decisão do gerador, funcionamento interno, justificativa de produção, hipótese de desempenho, diagnóstico, código interno ou scaffolding.
- Só prometa o que a plataforma sustenta. Sem integração confirmada, não há envio: um controle de submissão só existe se a tela disser que é simulação.

### 18. Consistência entre correção, resposta e Teacher's Guide

A resposta apresentada ao aluno e a orientação consultada pelo professor não podem divergir.

A forma de garantir isso depende da camada e do tipo de atividade — e a distinção que governa tudo o que vem abaixo é entre **atividade fechada**, que tem resposta definida, e **atividade aberta**, que admite produção pessoal.

**Pre-class — atividades autocorrigíveis:**

- a correção mostrada ao aluno e o answer key do professor indicam a mesma resposta;
- alternativas aceitáveis, rationale e transcript pertencem à mesma versão da atividade — enunciado editado sem levá-los junto é a forma mais comum da divergência;
- as respostas do aluno ficam disponíveis para consulta do professor;
- conteúdo reservado ao professor não aparece na visão do aluno, nem antes nem depois da tentativa;
- rationale e alternativas aceitáveis entram quando são pedagogicamente pertinentes — nunca como campo obrigatório artificial em toda atividade.

**In-class.** Respostas esperadas, critérios de aceite, alternativas possíveis e orientações de condução ficam no Teacher's Guide. Na tela projetada:

- a resposta não aparece antes da tentativa;
- atividade fechada pode revelar a correção depois da tentativa, por Check;
- quando o controle apenas mostra referência ou exemplo, o verbo é See ou Compare, nunca Check — o verbo promete comportamento (§12);
- guided discovery pode apresentar One possible answer, contraste, regra ou modelo depois da tentativa;
- atividade aberta — discussão, simulação, role-play, produção oral, feedback — não recebe gabarito único; depois da tentativa pode oferecer modelo de comparação, versão mais clara, critérios de sucesso ou apoio linguístico;
- o que a tela revela não pode divergir da orientação do guia.

**Post-class.** A regra alcança só as atividades autocorrigíveis: correção e answer key concordam. Link externo, sugestão de leitura ou escuta, gravação e escrita aberta não exigem gabarito; fala e escrita opcionais não recebem resposta única quando admitem produção pessoal; e modelo de apoio se apresenta como exemplo possível, nunca como a resposta correta.

**Implementação — o que é preferência e o que é requisito.**

- A fonte única de dados é a arquitetura preferencial, não obrigação absoluta. Sempre que viável, correção, feedback e answer key derivam da mesma fonte.
- Quando a natureza da atividade exigir representações separadas, a validação compara o conteúdo efetivamente apresentado em cada visão e reprova qualquer divergência.
- A aprovação depende da ausência de divergência, não do uso de uma estrutura específica em JavaScript.
- Nenhuma solução técnica reduz alternativas pedagogicamente aceitáveis a uma resposta única só para facilitar a automação. Esse é o erro que a regra existe para impedir: automatizar a conferência estreitando a pedagogia.

### 19. O que esta camada não implementa

**Fronteira da API de áudio.** O HTML implementa reprodução, controles, estados e acessibilidade; não implementa a geração. A API da ElevenLabs pertence ao pipeline seguro de produção definido no Anexo P-A.

Limites desta camada funcional: não simule autenticação, upload, armazenamento ou integração externa como se fossem reais.

| Requisito | Estatuto |
| :-: | :-: |
| Áudio em produção final | implementado no modo produção final (§0); no modo protótipo, provisório e declarado |
| Envio e integração do post-class | fora: exige backend. Sem ele, não há envio |
| Produção e incorporação de imagens | fora, salvo o que for embutido; ativo estrutural externo é proibido (§2) |

#### 19.1 Teacher's Guide externo — organização definitiva

Exatamente um Lesson overview aparece somente no primeiro slide, inicialmente recolhido, sem abertura automática, recriação, repetição ou espaço residual nos demais slides. Seu estado é preservado ao navegar e retornar. Não existe conteúdo geral residual não autorizado nem bloco equivalente.

O overview contém exclusivamente Lesson at a glance, Outcome and success, Before the lesson, Essential pathway e Language and connections. Títulos ficam destacados; corpo, listas e itens usam peso regular; negrito é pontual; expressões linguísticas podem usar itálico. Não usar `opacity` para reduzir contraste e não permitir que a regra tipográfica alcance o Stage-by-stage procedure.

Ao final do overview expandido, incluir o botão **Close overview and start procedure**. Ele fecha o overview, move o foco e rola para o início do procedimento, funciona por mouse e teclado, possui rótulo acessível, respeita movimento reduzido e oferece fallback. Não muda slide, aula, janela principal ou painel. O destino programático não cria parada adicional desnecessária no fluxo normal de Tab.

#### 19.2 Confirmação de escrita aberta no Post-class

Campos de produção escrita aberta usam **Confirm response** com estados *Response confirmed.* e *Changes not yet confirmed.* O estado persiste por aluno, aula e atividade, sobrevive ao recarregamento, volta a pendente após edição e é removido com reset. Não há correção, nota ou validação pelo professor; a visão docente é consulta. Confirmação escrita e confirmação de gravação oral são estados distintos.

## PARTE III — ENTREGA

### 20. Autovalidação obrigatória

Antes de entregar, o gerador roda e reporta com evidência, no vocabulário do 06 §4: PASSOU · PARCIAL · FALHOU · NÃO VERIFICADO. "NÃO VERIFICADO" é resposta legítima; "PASSOU" sem evidência não é.

| Camada | O que se prova |
| :-: | :-: |
| Registro | metadados repetidos saem do registro; markup concorda com ele; conteúdo da aula intacto |
| Etapas | oito etapas do framework no registro, na mesma ordem; nenhuma etapa fictícia; quantidade de slides variável |
| Papel | a URL do aluno não recebe conteúdo, payload, estado ou recursos do professor |
| Pre-class | gabarito fechado no início; ação do professor não altera resposta do aluno; os dois controles no fim |
| Controles da aula | Reset e Finish presentes, com confirmação; conclusão só por Finish; reset restrito à aula |
| Registro pós-aula | escala com número; engajamento fora da média; três campos; só dois compartilhados |
| Player | dois controles; Play reinicia após Stop; um componente para todos |
| Teclado | espaço aciona o controle em foco — e avança o slide quando o foco está fora |
| Escape | diálogo → interação ativa → aula, nessa ordem |
| Contraste | medido sobre superfície composta, em todos os fundos, com canário |
| Língua | deck em inglês; American English; citação literal intacta; rótulos da tabela do §16 |
| Dependência externa | zero ativo estrutural; links editoriais do post-class não contam |
| Interface | nenhuma limitação técnica, nome de tecnologia ou decisão do gerador visível |
| Modo | o modo declarado bate com o áudio entregue |
| Consistência | toda atividade autocorrigível tem resposta definida; correção e answer key concordam; o que o in-class revela concorda com o guia; nenhuma resposta reservada chega antes ao aluno; atividade aberta não foi convertida em resposta única; rationale, alternativas e transcript são da mesma versão — e uma divergência inserida de propósito é detectada |
| Teacher's Guide | botão por aula apenas na visão professor; rota derivada da URL; guia certo e independente; entrada direta no slide; cabeçalho compacto; orientação operacional imediatamente acessível; Lesson overview único e recolhido; ausência de preâmbulo geral extenso ou repetido; bloqueio detectado, com aviso e guia interno preservado |

O protocolo de execução dessa validação — como provar cada checagem, canário, caso negativo, controle positivo — está no P2. A matriz de conformidade, requisito a requisito, com evidência positiva, mutação correspondente, ambiente de execução e classificação do resultado, está no P3.

### 21. Pare e declare quando

- o conteúdo pedagógico não couber sem ser alterado;
- faltar dado material — informação ausente não se inventa;
- uma regra desta camada colidir com uma pedagógica (a pedagógica vence; a colisão se declara);
- o modo de entrega não tiver sido informado;
- não for possível validar a versão final;
- a única forma de cumprir um requisito for prometer o que a plataforma não sustenta.

### 20 (adição). Estado operacional, alternativas auditivas e transcript

O texto da interface e do Teacher's Guide deve refletir o estado real do componente. Open, reveal, select, compare, listen, read, write e submit somente aparecem quando a ação está disponível naquele momento. Componentes já visíveis são apresentados ou percorridos; conteúdo fechado não pode ser tratado como já legível.

Em listening contrast, cada Version A/Version B reúne no mesmo card rótulo, player e seleção. O transcript não aparece antes da tentativa. Após a escolha, a explicação revela os transcripts completos, com os mesmos rótulos dos players. A associação entre mídia, transcript, alternativa, resposta e rationale é estável e verificável.

A interface calcula e apresenta quantidades a partir do mesmo registro dos itens. Título, instrução, estado de conclusão e conteúdo visível não podem divergir quanto à contagem ou à nomenclatura.

#### 20.1 Controles Check, Redo e Reset lesson

Em atividades verificáveis, o controle apresenta **Check** enquanto sua ação for verificar. Depois da verificação, quando o próximo acionamento reiniciar a tentativa, o controle passa a apresentar **Redo**. O texto visível e o nome acessível devem mudar juntos e corresponder à ação efetiva.

Redo reinicia somente a atividade correspondente: limpa respostas, seleções, campos e estados de correção; oculta a devolutiva anterior; retorna o controle a Check; e preserva as demais atividades, fases e aulas. Se o estado for persistido, a recarga deve reconstruir corretamente tentativa, verificação, rótulo e devolutiva.

Reset lesson atua sobre todo o In-class da aula ativa. Depois de confirmação clara, limpa as respostas e os estados interativos do In-class, retorna ao primeiro slide, remove o status de aula finalizada e atualiza as superfícies derivadas. Preserva Pre-class, Post-class, registro pós-aula, Estado pedagógico do ciclo, outras aulas e dados fora desse In-class.

Cancelar a confirmação não pode alterar nenhuma parte do estado. A implementação deve usar escopo canônico e isolado por aluno, aula, atividade, superfície e papel; não pode depender de listas independentes de chaves que deixem resíduos ou atinjam outro contexto.

### 22. Linguagem instrucional publicada — aplicação do A05

O A05 governa o texto efetivamente entregue nas superfícies do produto. P1 continua responsável pelo comportamento, pelos estados, pelos controles e pela separação de papéis; o A05 determina como essas ações e orientações são formuladas para professor e aluno.

- Não transferir literalmente para a interface, para o deck ou para o Teacher's Guide a redação absoluta usada em regras internas de geração e validação.
- O texto publicado preserva integralmente a ação disponível, a condição, a sequência, o apoio, a evidência e o produto definidos pelos documentos responsáveis.
- Imperativos instrucionais convencionais permanecem adequados quando nomeiam diretamente uma ação executável, como "Match the sentences.", "Choose the best answer." e "Listen again."
- Não usar uma lista lexical automática para aprovar, reprovar ou reescrever linguagem. "Do not", "Never", "must" e equivalentes exigem análise contextual e podem permanecer quando expressam uma restrição realmente necessária.
- A interface não expõe regras internas, justificativas do gerador, defesa da mecânica ou comandos dirigidos ao professor como se ele fosse um agente de execução.
