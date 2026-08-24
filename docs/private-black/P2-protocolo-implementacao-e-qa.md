> **Documento normativo importado do Drive — nao editar aqui.**
> Origem: `P2_Protocolo_de_Implementacao_e_QA.docx`
> Drive ID: `1zKuAMsZNkHaYaNkR5OiYsYa98RE0sjbi`
> Modificado no Drive: 2026-08-21
> Reimportar: `python3 scripts/black/docx_to_md.py <arquivo.docx> docs/private-black/P2-protocolo-implementacao-e-qa.md`
> A fonte e o .docx. Divergencia entre este arquivo e o Drive se resolve reimportando, nunca editando o .md.

**P2 · PROTOCOLO DE IMPLEMENTAÇÃO E QA**

**Como produzir e como provar — Private Class Alumni Black**

**Série P — plataforma.** Companheiro do **P1**, que especifica o produto, e do **P3**, que reúne a matriz de conformidade e especifica os requisitos da suíte executável. Este especifica o **processo**: como mexer no arquivo sem destruí-lo, e como provar que a validação valida.

**Para quem é.** Para quem **implementa** e para quem **escreve ou mantém as checagens**. O gerador que produz a aula não precisa dele para decidir o que entregar — precisa dele para não quebrar o que já está entregue. Manter isto separado do P1 é deliberado: misturado, faz o gerador priorizar engenharia interna em vez da entrega.

**Origem.** Cada regra abaixo custou pelo menos uma rodada de produção real. Elas vêm **com o motivo**: regra sem motivo é otimizada para fora pelo próximo editor.

**1. Antes de tocar no arquivo**

1.  **Ao modificar um arquivo existente, faça backup antes da primeira alteração. Numa geração nova, registre a versão inicial produzida antes da primeira rodada de correções.** Tirar o backup depois da primeira edição já produziu backup que continha o defeito — e o script de refazer inseriu um bloco duplicado.

2.  **Nunca regravar HTML lido com leitura que assume a codificação do sistema.** Ler UTF-8 sem BOM como ANSI e regravar grava o mojibake **como texto** e corrompe o arquivo inteiro em silêncio. Leia sempre declarando UTF-8. *É reversível — reencodar e decodificar desfaz o passo —, e a prova é o diff contra o backup.*

3.  **Recompor o arquivo UMA vez só**, conferindo a estrutura antes de gravar. Duas recomposições cortam em índices da versão antiga e destroem o arquivo.

**2. Ao mudar qualquer coisa**

4.  **Corrigir N ocorrências não é varrer.** Varra por padrão, sobre o arquivo inteiro, e **leia cada ocorrência no contexto** — nem toda coincidência é resíduo.

5.  **Rótulo se renomeia; identificador, não.** Identificadores governam armazenamento e roteamento: trocá-los junto com o texto quebra a separação por papel em silêncio.

6.  **Resíduo de rótulo antigo se procura NA INTERFACE, e com caixa** — comentário de código não é interface, e comparação sem caixa acusa o inocente.

7.  **Ao trocar a cor de um componente, varra o CSS inteiro** por outras regras que alcancem o mesmo seletor, e confira a cor **computada** no navegador. *"A cor existe no sistema" não é "a cor certa chegou ao elemento"* — regra antiga que sobrevive mais abaixo vence por cascata.

8.  **Traduzir sem reauditar a afirmação** carrega junto o que a frase afirmava, inclusive o que já era falso. Nenhuma checagem pega isso: elas garantem a língua, não a verdade.

9.  **<strong>** **que ABRE um parágrafo é rótulo; no meio, é ênfase.** Não os trate igual.

10.  **Comentário de código com dado é segunda fonte.** É o que o próximo editor lê antes de mexer no bloco, e é onde um valor antigo sobrevive. Confira contra o registro.

11.  **Texto de apoio que CITA um rótulo é segunda cópia do rótulo.** Renomeie o controle e a orientação passa a mandar procurar um botão que não existe com aquele nome — e nada acusa, porque as duas frases continuam gramaticais. **A checagem confere a citação contra o rótulo VISÍVEL**, nunca contra um texto escrito nela própria: escrito nela, ela vira a terceira cópia.

**3. Ao escrever ou manter as checagens**

12.  **Toda checagem se prova contra um caso negativo, ou não vale.** Checagem que nunca falhou não está conferindo nada.

13.  **Checagem que não falha, só não faz nada.** A variante mais silenciosa: **remover o elemento que ela examinava** faz a checagem passar sem conferir. **Ao mudar a FORMA de cumprir um requisito, reaponte a checagem para o REQUISITO, não para a forma antiga.**

14.  **Regra certa + checagem certa + objeto fora do escopo = requisito não cumprido, e ninguém vê.** Ao herdar uma regra, confira se ela alcança **todos** os objetos que a regra descreve.

15.  **A menção não é a expressão.** Corpo que "cita" um nome aprova mutação que o torna inalcançável. **E o nome citado no próprio comentário satisfaz a checagem** — exija a **forma**, não a palavra.

16.  **Varredura que devolve zero precisa de canário.** Plante um elemento deliberadamente errado e exija que ele seja pego. **E canário que vaza reprova o inocente:** marque-o e exclua-o da consulta de alvos.

17.  **Checagem que confere N itens deriva o N dos blocos existentes**, nunca de número escrito nela.

18.  **Comparação com** **<=** **não prova soma.** Declarar menos que o orçamento passa em silêncio: imprima o **vão** entre declarado e previsto, ou o que sumiu não deixa rastro.

19.  **Exceção a uma regra é NOMEADA e SINGULAR.** Quem foge da regra entra numa lista com o motivo; a própria exceção se confere, para não ficar obsoleta em silêncio quando o objeto voltar ao padrão. **E exceção que ninguém reconfere deixa de ser exceção e vira permissão:** uma checagem que *espera* uma ocorrência do que a regra proíbe imprime o defeito como resultado normal, rodada após rodada. Ao herdar uma exceção, pergunte primeiro se o motivo dela ainda existe — no caso que originou esta regra, o código já cumpria o requisito por outro caminho e a exceção era puro resíduo.

20.  **Varredura de grafia se faz por CLASSE DE SUFIXO, nunca por lista de palavras** — lista é a ocorrência apontada com outro nome. A classe traz falso positivo: vire **allowlist com justificativa**, faça o padrão casar **palavra de prosa, não identificador**, e **alcance o JavaScript**, não só o markup.

21.  **A rodada COMPLETA é o que pega âncora vencida em suíte alheia.** Mudar o alvo de uma função deixa negativos de **outras** prioridades apontando para a forma anterior — e eles não reprovam, devolvem "não aplicado", que parece defeito do alvo. **E não se mede sobre alvo em movimento:** rodada que continua enquanto o código é editado lê versões diferentes da árvore.

22.  **Negativo que não remove nada não prova ausência**, e negativo que muta um prefixo deixa intacto o que vem depois.

23.  **Negativo aposentado se aposenta COM o motivo escrito.** Teste sem objeto é ruído com aparência de cobertura. Quando um mecanismo sai, seus negativos saem junto — e os requisitos que eles cobriam reaparecem na forma nova.

**3.1 O que checagem estática nunca vê**

**Nenhuma varredura de texto detecta um erro de execução.** Todo identificador existe, toda função existe, todo seletor casa — e a página quebra ao abrir. Uma suíte inteiramente estática pode passar com **centenas de casos** sobre um artefato cujo *boot* morre na primeira linha.

24.  **Depois de renomear, ABRA A PÁGINA e leia o console.** Renome não é substituição de texto: a mesma propriedade se acessa em **formas diferentes** — d.x, obj().x, a['x'] —, e a varredura que troca uma não vê as outras. O que sobra vira undefined em tempo de execução.

25.  **Uma exceção no boot não fica onde nasceu.** Ela aborta o restante do manipulador: uma função que morre no início derruba **tudo o que viria depois dela**, inclusive construtores de outros componentes. O sintoma aparece longe da causa — no caso que originou esta regra, o defeito estava no preenchimento do pre-class e o que sumiu foi o **transporte de áudio de todo o material**. Ao investigar um componente ausente, **procure primeiro um erro anterior**.

26.  **Se o meio de publicação não deixa inspecionar, sirva o arquivo localmente.** file:// costuma estar bloqueado para automação, e o artefato publicado roda em **origem isolada** — nenhum dos dois permite ler o DOM. Um servidor mínimo sobre o próprio arquivo resolve, e é o que torna a exigência do P3 executável.

27.  **Ao exercitar áudio, silencie a saída sem trocar o caminho:** basta zerar o volume do *utterance* dentro do próprio speak. Simular o mecanismo testaria o simulador.

**3.2 Produção e validação dos áudios oficiais**

O pipeline recebe o modo de entrega antes de gerar o build. Em protótipo, pode usar síntese do navegador, declarada uma vez como provisória. Em produção final, gera os arquivos pela API da ElevenLabs conforme o Anexo P-A e remove integralmente qualquer caminho de síntese no cliente.

Sequência obrigatória: congelar o transcript aprovado; selecionar categoria e voz no manifesto validado; pré-processar sem alterar o conteúdo pedagógico; chamar a API no ambiente seguro; armazenar o arquivo; registrar transcript, versão, modelo, Voice ID, parâmetros, duração e checksum; ouvir e aprovar; associar o arquivo ao player; gerar o build; validar a fonte e o build.

Segurança bloqueante: a chave da ElevenLabs permanece em secret manager ou variável protegida do pipeline. É proibido incluí-la no repositório, prompt, HTML, JavaScript, source map, log público, relatório distribuído ou chamada do navegador. Qualquer exposição reprova a publicação e exige revogação e rotação da credencial.

Validação mínima: nenhum speechSynthesis, SpeechSynthesisUtterance ou chamada autenticada à ElevenLabs no build; todos os players resolvem arquivos existentes; transcript e mídia pertencem à mesma versão; vozes e parâmetros conferem com o manifesto; diálogos preservam personagens distinguíveis; não há cortes, ruídos, respirações artificiais, pronúncia inadequada ou velocidade incompatível com o nível.

Uma alteração de transcript, modelo, Voice ID, parâmetro ou arquivo invalida a aprovação anterior. Regenerar apenas o item afetado é permitido quando o manifesto registra a nova versão e a suíte confirma que nenhuma associação vizinha foi alterada.

**3.3 Conferência visual das perguntas projetadas**

Validar no navegador e por regressão visual, usando as fontes efetivamente disponíveis no build: pergunta principal curta e longa; lista de perguntas; quiz projetado; fundos claro, escuro e de abertura; larguras desktop e responsivas.

A conferência compara estilo computado e resultado visual: família pertencente ao sistema; pergunta principal em família display, itálico moderado e peso médio; corpo maior que o texto corrente e menor que o título; largura controlada; quebra sem corte ou overflow; contraste sobre o fundo composto; caixa normal em perguntas longas; alinhamento à esquerda como padrão; centralização somente em pergunta curta e tela dedicada.

Casos negativos obrigatórios: carregar uma terceira família; depender de Google Fonts; remover a família display da pergunta principal; diferenciar apenas por tamanho; aplicar caixa alta a pergunta longa; centralizar pergunta longa ou acompanhada de outros focos; igualar .slide-question, .q-item e .slide .quiz-question; produzir contraste insuficiente em fundo claro ou escuro; causar linha órfã, corte ou overflow.

**4. Ao medir no navegador**

28.  **Teste de teclado exige o CONTROLE POSITIVO na mesma rodada.** "Não aconteceu" é o mesmo resultado de uma guarda que funciona e de um manipulador morto. Prove primeiro que a tecla chega.

29.  **Medir com a aba fora de foco mede o temporizador, não a página** — o navegador limita setTimeout a ~1/s, e cada passo parece custar quase um segundo.

30.  **Neutralizar a animação faz parte da medição, não a falsifica.** Elemento que entra a partir de opacidade zero devolve contraste falso se medido antes de assentar. O estado que vale é o assentado.

31.  **getComputedStyle** **e** **getBoundingClientRect** **em elemento oculto mentem** — devolvem zeros e valores próprios. Meça só o que tem caixa.

32.  **textContent** **concatena filhos ocultos e vizinhos.** Medir folha a folha, ou separar.

33.  **Contraste se mede sobre a superfície composta e com a opacidade herdada acumulada.**

**5. Teacher's Guide separado — implementação e validação em dois ambientes**

A regra do produto está no P1 §15.1. Aqui está **como implementar e como provar**.

**Implementação.** Rota ou parâmetro **derivados da URL corrente** — ?mode=teacher-guide&lesson={id}. **Nenhum domínio, URL oficial, endereço de teste ou URL de artefato escrito à mão no código.** Cada card do In-class transmite o identificador da sua aula; a janela do guia **interpreta**, **confere se a aula existe** e abre direto no guia correspondente. O guia interno se **preserva** até que a abertura separada seja validada na URL oficial.

**A validação ocorre em DOIS ambientes, e um não substitui o outro:**

| **Ambiente** | **O que se prova ali** |
|---|---|
| **Artefato de revisão** | presença dos botões, associação card↔aula, construção da rota, detecção do bloqueio e comportamento do *fallback*. O bloqueio de pop-up pelo sandbox do host se registra como **limitação do ambiente**, nunca como defeito do HTML |
| **Ambiente oficial** | abertura efetiva em janela ou aba, aula correta, independência entre as janelas, isolamento entre materiais e compatibilidade com os navegadores suportados |

34.  **A abertura bloqueada é DETECTADA, nunca silenciosa.** O código lê o retorno nulo (ou equivalente), dá aviso breve e mantém o acesso ao guia interno. **Aviso que afirma ter aberto a janela quando ela não abriu é pior que a falha**, porque encerra a investigação.

35.  **Validar a abertura simultânea de DOIS materiais e de DUAS aulas.** É o único teste que expõe o nome de janela mal formado: sozinho, qualquer nome funciona. O nome tem de **impedir que o guia de um artefato reutilize ou substitua a janela pertencente a outro** — e não pode carregar nome literal nem dado pessoal do aluno (P1 §15.1).

36.  **Registro obrigatório do teste no ambiente oficial:** ambiente e URL testados · navegador e versão · aula ou conjunto de aulas verificado · resultado da abertura · resultado da independência entre as janelas · falhas e *fallback* observado. Sem esse registro, o requisito fica **NÃO VERIFICADO** — e "NÃO VERIFICADO" é resposta legítima; "PASSOU" sem evidência não é.

**6. Anexo — armadilhas de PowerShell**

Válido apenas para quem escreve as checagens neste ambiente.

•  **+** **dentro de** **@()**: a vírgula fecha o elemento antes da soma, o array se parte e os campos trocam de lugar. **Monte a string ANTES do array.** Mordeu sete vezes.

•  **-eq****/****-ne** **e chave de** **@{}** **são case-INSENSITIVE.** Onde a caixa importa, -ceq/-cne; e @{'Practise'=…;'practise'=…} é erro de chave duplicada.

•  **Variável de quebra de linha não declarada some em silêncio:** 'a' + $null + 'b' vira 'ab', e o caso devolve "não aplicado".

•  **\"** **não escapa em aspas duplas** — a aspa fecha a string e o script inteiro deixa de compilar. Use aspas simples.

•  **Âncora incompleta casa dentro de outro nome:** function paint casa paintX; .classe{ casa .outra.classe{; e **a vírgula é caractere de seletor** — .a{ casa dentro de .b,.a{.

•  **Janela de tamanho fixo é âncora que expira sozinha:** extrair {0,320} do corpo de uma função e procurar ali dentro reprova no dia em que alguém acrescentar um comentário. **Recorte a unidade inteira** — o requisito é "passa pelo transporte único", não "passa nos primeiros 320 caracteres".

•  **Varredura de proibição se faz sobre CÓDIGO, não sobre menção:** o comentário que explica a regra cita o que ela proíbe, e contá-lo reprova justamente quem documentou.

•  **Mensagem de aprovação e de reprovação não podem compartilhar a frase que o teste procura** — o negativo casa a linha de sucesso e reporta falha onde não há. Procure o **marcador de falha**.

•  **Padrão que exige adjacência quebra** quando entra um atributo: sempre [^>]*.

•  **Nunca extrair bloco com** **[\s\S]*?** **até** **</div>** — para no primeiro filho fechado.

•  **Balanço global de tags não detecta nada** (dois erros simétricos somam zero): confira **dentro de cada tela**. E **tag escrita num comentário entra no balanço**.

•  **.Replace(string,[char])** escolhe a sobrecarga errada — converta para [string].

•  **O porter escapa não-ASCII**: normalize antes de comparar, **nos dois sentidos** — passar na fonte e falhar no build, e o inverso.

•  **Apóstrofo tipográfico é delimitador** no PS 5.1: texto editorial vai por arquivo, nunca inline.

•  **Script sem BOM é lido como ANSI:** mantenha o script ASCII e monte caractere acentuado por [char].

**7. Antes de publicar**

37.  **Rodar o validador na FONTE e no BUILD.** O porter transforma o arquivo, e checagem já passou num e falhou no outro.

38.  **Provar o superset:** extraia os fragmentos substantivos do que está publicado e liste os que **sumiram** na versão nova. A lista tem de bater, item a item, com as mudanças deliberadas.

39.  **Rodada completa das suítes, sobre árvore parada**, depois da última edição de código.

40.  **Depois de publicar, conferir marcadores no que está no ar** — não no que se acabou de gerar.

41.  **A abertura separada do Teacher's Guide é requisito BLOQUEANTE para a publicação definitiva no ambiente oficial.** No protótipo ou artefato de revisão sujeito a sandbox, admite-se **aprovação condicional** quando a implementação, o endereçamento e o *fallback* estiverem corretos e a limitação externa estiver documentada. **Aprovação baseada só no artefato restrito não conta como publicação aprovada.**
