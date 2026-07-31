# Eixo FRAMEWORK — categorias, métodos e a trava de isolamento

> **Fonte única:** `public/data/frameworks.json`. Quem lê: o catálogo (prateleira por
> categoria), o builder (`assert_framework` + etiqueta) e o GATE 11
> (`scripts/check_framework_isolation.py`). **Acrescentar framework = acrescentar um objeto
> no JSON.** Não se mexe em HTML, builder nem gate.

---

## 1. Os dois eixos (não confundir)

| Eixo | O que é | Valores hoje |
|---|---|---|
| **Categoria** (`model` no config) | O **público**. Decide pele, tom, duração e a régua de idioma. | `adulto` · `kids` · `teens` |
| **Framework** (`framework` no config) | O **método**. Decide a ordem dos capítulos e a natureza de cada etapa. | `imersivo-prototipo` (todas) · `ppp`, `communicative`, `task-based` (só adulto) |

**Framework é aninhado na categoria.** Cada categoria tem a sua própria prateleira: os três
frameworks do documento pedagógico entram **só em Adulto, por enquanto** (ordem do Dan,
27/07/2026). Kids e Teens ficam com a prateleira aberta para quando ele quiser.

O que **não** é framework: *pele* (kids/teens mudam CSS, não a sequência pedagógica) e
*tipo de aula* (Fala/Leitura/Camada B2/Diagnóstica — variações de quais blocos entram
dentro do mesmo método).

---

## 2. Os frameworks

### `imersivo-prototipo` — "Imersivo - Protótipo" (produção)

O framework da casa. **É o que gera tudo hoje: 1.221 aulas, 71 alunos.** A aula é uma
história em 7 capítulos com nome próprio ("The Tuesday Call"), vocabulário por reveal,
**gramática explícita descoberta pelo aluno**, artefato em CSS e produção em três degraus
(guiado → semi-livre → livre). 25–30 slides.

Nome escolhido pelo Dan em 27/07/2026. "Protótipo" é dele, e é deliberado: sinaliza que é o
que roda hoje, não a palavra final. Referência: `helen-mendes-aula2`.

### `ppp` — PPP (especificado, ainda não gerado pelo builder)

`Let's Get Started` → `Packing Words` → `Brainstorming` (gist/detail/post) → `Diving Deep`
→ `Practice` → `Your Turn` → `Wrap-up`. **Gramática implícita** (sem prática gramatical
explícita), uma skill receptiva principal por aula, **7–15 slides**.

Spec: `_build/model/V4-SPEC.md`. Existem 5 pilotos (`helen-mendes-v4-aula1..5`). **O builder
não sabe produzir isto** — os pilotos foram feitos por fora.

### `communicative` — Communicative Approach (documentado)

6 stages: Lead-in comunicativo → Check it out (exposure) → Language for Communication →
Pre-communicative → **Communicative Task** (núcleo, 25–30 min) → Feedback/accuracy.
*Information gap* adaptado ao 1-a-1: a assimetria é de **papel**, não de conhecimento — a
professora vira personagem e o aluno extrai a informação pela conversa.

### `task-based` — Task-Based / TBL (documentado)

TBLT com priming leve. A linguagem-alvo é **exposta** antes da tarefa, mas **não ensinada**:
a forma é refinada **depois** da produção, no Focus on Form diferido. É essa inversão que o
distingue do PPP. O Task Cycle é o centro de gravidade da aula.

---

## 3. A trava de isolamento (GATE 11)

> **Ordem do Dan, 27/07/2026:** *"não quero que NADA DE ALUNOS JÁ ATUAIS utilize os
> frameworks que vamos inserir agora [...] gerar alunos mock, validar, pra só depois
> implementar."*

Intenção não é garantia. A garantia são **duas travas**, uma na entrada e outra na saída:

1. **No builder** (`assert_framework`): recusa o config **antes** de escrever qualquer
   arquivo. Melhor recusar do que gerar 25 slides e 50 MP3 de uma aula que o gate barraria.
2. **No CI** (`scripts/check_framework_isolation.py`, GATE 11): varre o repo e barra o PR.

As três regras, todas bloqueantes:

| # | Regra | Por quê |
|---|---|---|
| 1 | Framework declarado tem de existir **naquela categoria** | Pega typo e framework não cadastrado |
| 2 | Framework com status ≠ `producao` só em slug listado em `mocks` | **É a ordem do Dan.** Aluno real nunca recebe método em validação |
| 3 | Troca de framework só passa se **declarada em `migracoes`** — e o corte tem de ser cumprido | Troca intencional é legítima; a acidental não |
| 4 | Aulas do mesmo aluno declaram **um só** `TOTAL_AULAS` | Garantia financeira: a barra do pacote é `concluídas / TOTAL_AULAS` |

### Legado-tolerante (REGRA 30/31)

Aula **sem** a etiqueta `alumni-framework` é ignorada pelo gate. As ~1.240 aulas anteriores
a este eixo não têm a etiqueta e **não serão tocadas em varredura** — elas já são
identificáveis pela estrutura (7 capítulos), e aula que já foi dada não se mexe.

Etiqueta-se **por aluno, sob demanda** (`scripts/tag_framework.py`), no PR em que se for
mexer no framework daquele aluno. Duas razões para nunca fazer em massa: a REGRA 30 (foi
uma varredura gulosa que quase reescreveu 2.182 arquivos por engano) e a operacional — o
repo tem dezenas de gerações em paralelo o tempo todo, e um commit tocando 1.221 arquivos
conflitaria com quase toda branch aberta.

> **Exceção conhecida:** `sandra-hayasaki-aula5` foi refeita em PPP antes desta conversa —
> é a única aula de aluno real fora do Imersivo. Sem etiqueta ⇒ o gate não a vê, de
> propósito: ela é legado, não um caso novo. Fica registrada aqui para não virar surpresa.

---

## 3.1 Migrar um aluno de framework (sem quebrar o pacote dele)

> Decisão do Dan, 27/07/2026: *"é necessário ser possível a alteração de frameworks sem
> influenciar nas aulas passadas e no que já aconteceu, mas ao mesmo tempo mantendo o
> progresso do pacote do aluno — financeiramente."*

**O progresso é imune ao framework por construção.** `lesson_progress` grava
`(student_slug, lesson_number, inclass_done)` — não há coluna de framework nem de
estrutura. A aula 13 conta como a 13ª do pacote tenha ela nascido em qualquer método, e as
aulas passadas não são tocadas. O que precisa de vigilância é o **denominador**: a barra é
`concluídas / TOTAL_AULAS`, então duas aulas do mesmo aluno declarando totais diferentes
fazem o aluno ver percentuais diferentes conforme a aula que abrir. Daí a **regra 4**.

> Medição de 27/07/2026: **9 alunos já têm esse defeito no legado** (nilo 40 vs 96, simone
> 12 vs 48, natalie 5/6/26, diogo 36 vs 40, tania 10 vs 20…) — anterior a tudo isto e sem
> relação nenhuma com framework. A regra 4 só olha aula **etiquetada**, então nasce em 0 e
> não cobra retrofit (REGRA 30).

**O passo a passo:**

1. Etiquete as aulas existentes do aluno — `python3 scripts/tag_framework.py --slug fulano`
   (dry-run; `--write` para valer). Sem isso o gate não sabe o que as aulas antigas são e
   não consegue conferir o corte.
2. Declare a migração em `migracoes` de `frameworks.json`:
   `{"slug": "fulano", "de": "imersivo-prototipo", "para": "ppp", "a_partir_da_aula": 13}`.
3. Gere a aula 13 em diante com `"framework": "ppp"` no config, **`hub: "snippets"`**.
   ⚠️ **Nunca `hub: "new"` numa migração** — ele reescreve o hub do zero e as aulas
   anteriores somem do menu. É o único jeito conhecido de a migração machucar o pacote.
4. `TOTAL_AULAS` **não muda**: o pacote comprado é o mesmo, só o método mudou.

Declarar e não cumprir também é erro: se a declaração diz "imersivo até a 12" e a aula 2
aparece em PPP, o gate barra. Sem isso a declaração viraria carta branca — buraco real,
pego em teste em 27/07/2026 (migrando **todas** as aulas o slug voltava a ter um framework
só, a checagem de mistura não disparava, e a declaração passava a mentir).

---

## 3.1b RODÍZIO — o método alterna por posição de aula (30/07/2026)

> Pedido do Dan: *"a ideia é intercalar a rodada de frameworks nas aulas"* — a nova
> estratégia de produção do Black adulto.

**Rodízio não é migração.** Migração tem UM corte e dois frameworks ("imersivo até a 12,
PPP da 13 em diante"). Rodízio tem N frameworks e **nenhum corte**: o método alterna por
posição, para sempre. Espremer um no outro transformaria `migracoes[]` em carta branca —
exatamente o buraco que a regra 3 fechou em 27/07. Por isso é uma declaração própria:

```json
"rodizios": [
  {"slug": "mock-rodizio-tiago", "desde_aula": 1,
   "ciclo": ["ppp", "communicative", "task-based"]}
]
```

Framework esperado da aula N = `ciclo[(N - desde_aula) % len(ciclo)]`. O **GATE 11** confere
aula a aula, com a mesma severidade da troca acidental, e o **builder** (`assert_framework`)
confere antes de escrever o primeiro arquivo — aqui isso importa mais que no CI, porque o
config é a única fonte da aula e o erro só apareceria depois de ~50 MP3 gerados.

Detalhes que já custaram tempo:

- **Slug com rodízio precisa estar em `mocks[]` de CADA framework do ciclo** enquanto nenhum
  deles for de produção. São regras independentes (a 2 é "quem pode receber", a 3b é "o quê,
  em que ordem").
- **Rodízio + migração no mesmo slug = erro.** Com os dois, não há resposta única para "qual
  framework a aula N devia ter".
- **Ciclo de 1 framework = erro.** Não é rodízio: é o framework do aluno, e a declaração só
  serviria para desligar a checagem de mistura.
- **O hub (`{slug}.html`) fica com a etiqueta da ÚLTIMA aula gerada** e isso é ruído, não
  declaração — ele contém aulas de vários métodos. O gate só confere arquivos com número de
  aula.

Primeiro caso: `mock-rodizio-tiago` (perfil e syllabus em `_build/mock-rodizio-tiago/`).

---

## 3.2 Gate novo por framework — **escopar, não generalizar**

> Decisão do Dan, 27/07/2026: *"não precisa generalizar, apenas caso os frameworks
> compartilhem o mesmo tipo de exercício; do contrário os mocks novos gerarão gates
> diferentes futuros."*

**Generalizar um gate é afrouxá-lo.** Ensinar o `validate_lesson` a aceitar aula sem
"Grammar Tip" o torna permissivo para **todo mundo** — inclusive para as 1.221 aulas do
Imersivo, que é justamente onde ele precisa continuar estrito.

**Escopar é outra coisa:** o gate continua exigindo exatamente o que exige hoje, mas só de
quem é **do framework dele**. Aula de outro framework ele não é dono, e ignora. Na prática
é ler a etiqueta `alumni-framework`: *"não é do meu framework? não é comigo."* A regra não
muda em nada.

O critério para o mock novo:

- **Mesmo tipo de exercício** (matching, gap-fill, true/false…) → **reusa o gate que já
  existe**: mesma classe-mecanismo, mesma checagem.
- **Tipo que não existe** (o Task Cycle do TBL, o Focus on Form diferido) → **nasce gate
  novo junto com o mock**, já escopado àquele framework.

Consequência: promover um framework a `producao` deixa de ser mudar uma palavra no JSON —
é promover algo que já tem trava própria.

---

## 4. Como acrescentar um framework

1. Acrescente o objeto em `public/data/frameworks.json`, dentro da categoria certa, com
   `status: "documentado"` (ou `"mock"` quando já houver aluno mock).
2. Ponha o slug do aluno mock em `mocks.{id-do-framework}`.
3. Gere a aula do mock com `"framework": "{id}"` no config. O builder valida sozinho.
4. Valide (todos os gates + medição no navegador). **Só então** o Dan decide se promove a
   `producao` — e é a promoção que o libera para aluno real.

O catálogo se atualiza sozinho: ele desenha a prateleira a partir do JSON.

---

## 5. `alumni-gen` — como criar regra nova sem acusar o passado

Toda aula nasce carimbada com a versão do builder que a gerou:

```html
<meta name="alumni-gen" content="1">
```

**O problema que isso resolve.** Uma invariante nova (a pergunta de predição, 28/07/2026)
não existe nas aulas já publicadas — por definição. Sem um critério de data, o gate novo
sai acusando aula que está no ar, funcionando, que o aluno **já teve**. Foi o que
aconteceu na primeira versão deste gate: ele usou "tem etiqueta de framework?" como proxy
de "é nova?", e a etiqueta já estava em ~8 aulas publicadas de alunos reais. Oito falsos
positivos, zero aulas melhoradas, baseline de legado subindo — exatamente o que a
REGRA 30 proíbe.

**A regra.** Gate de invariante nova roda **só em quem nasceu depois dela**:

```python
GEN_MINHA_REGRA = 2                      # a versão em que a regra entrou
if _gen(c) < GEN_MINHA_REGRA:
    return                               # nasceu antes: não é comigo
```

`BUILDER_GEN` (em `build_from_model.py`) **sobe quando uma invariante nova entra** — nunca
por mudança cosmética, senão volta a ser um proxy de data. Aula sem o carimbo = `0` =
passado = intocável.

| GEN | O que entrou |
|-----|--------------|
| 1 | player de listening completo · pergunta de predição · banco do gap-fill desembaralhado |

**Por que não usar a data do arquivo ou o git log.** Porque o carimbo tem de viajar
DENTRO do HTML: o gate roda sobre o conteúdo, o arquivo é reescrito a cada rebuild, e o
git log conta a história do commit, não a da geração.

---

## 6. O catálogo de AULAS MODELO (por aluno)

O catálogo mostra três camadas, e elas respondem perguntas diferentes:

| Camada | Pergunta que responde | Fonte |
|---|---|---|
| **Modelo** | Que molde é esse (adulto/kids/teens)? | escrito em `public/catalogo.html` |
| **Framework** | Que método a aula roda? | `public/data/frameworks.json` |
| **Aula modelo** | *Dentro do mesmo aluno, quais aulas são diferentes entre si?* | `public/data/modelos-aulas.json` |

A terceira é a que some sem ninguém notar: a Helen tem 5 aulas, e as 2 primeiras não têm a
camada de blocos B2 que as 3 seguintes têm; o Tiago tem 5 aulas e cada uma roda um método
(o rodízio da seção 3.1b). Sem ver lado a lado, "aula modelo" vira uma lista de links.

**Nada ali é digitado.** `scripts/gen_catalogo_modelos.py` MEDE cada aula no HTML — título,
nº de slides, capítulos (`.phase-label`), framework (`<meta name="alumni-framework">`) e os
componentes de IN CLASS presentes — e agrupa em **variantes** as aulas de mesma estrutura.
O único texto humano é o `ROSTER` de personas dentro do script.

```
python3 scripts/gen_catalogo_modelos.py            # regera o JSON
python3 scripts/gen_catalogo_modelos.py --check    # o passo do CI: falha se estiver velho
```

Aula modelo nova (ou mexida) sem regerar = **PR vermelho**, porque catálogo que mente é pior
que catálogo nenhum: ninguém desconfia dele. Aula de aluno REAL não entra no ROSTER e nunca
dispara esse passo.

---

## 7. CONTRATO — o que cada método promete entregar (GATE 12)

`framework` diz QUAL método a aula roda. O **contrato** diz o que aquela aula tem de
TER. Sem ele, *"gere 3 aulas do tipo Leitura"* é um pedido sem conferência: os gates
são todos universais (áudio, vozes, português na tela) e nenhum sabe que uma aula de
leitura precisa de texto central, gist e true/false.

### As três peças

| Peça | Onde | Como se prova |
|---|---|---|
| **Banco de exercícios** | `public/data/exercicios.json` | gerado por `scripts/gen_banco_exercicios.py`, que **chama `render_block()` do builder** para cada exercício e guarda as classes que sairam. Componente de shell (vocab reveal, diálogo, player) é provado pela presença da classe no molde. |
| **Contrato** | `contrato` de cada framework em `frameworks.json` | decisão humana, semeada por medição (`--sugerir`) |
| **Gate** | `scripts/check_contrato_aula.py` | casa contrato × HTML pela classe-marcador |

### A regra de ouro ao editar um contrato

> **Suba a versão e empurre a anterior pra `contrato_historico`. Nunca edite a versão
> em uso.**

A aula carimba `<meta name="alumni-contrato" content="ppp@1">` ao nascer, e o gate a
julga pela versão **dela**. É isso que torna o editor do catálogo seguro: tirar um
exercício do contrato hoje cria a versão 2 e não encosta em nada que nasceu na 1. Sem
o histórico, uma edição de dois cliques viraria centenas de aulas vermelhas — e a saída
seria desligar o gate, que é como gate morre.

Duas travas herdadas, no mesmo espírito: aula **sem** o carimbo é ignorada (todo o
legado, REGRA 30), e exercício sem classe exclusiva (`verificavel: false` no banco —
hoje `questions`, `analyse` e `bank`) nunca reprova, porque o gate não consegue
distingui-lo de outro.

```
python3 scripts/gen_banco_exercicios.py            # regera o banco (prova contra o builder)
python3 scripts/check_contrato_aula.py             # GATE 12 no repo inteiro
python3 scripts/check_contrato_aula.py --selftest  # prova que morde
python3 scripts/check_contrato_aula.py --sugerir ppp   # mede as aulas e propõe contrato
```

### Semente dos contratos (31/07/2026)

Nenhum contrato foi inventado: cada um saiu da **interseção medida** das aulas que já
rodam aquele método — o que está em TODAS elas. Para o `imersivo-prototipo` isso deu 4
itens (`checklist`, `role-play`, `slide-tarefa`, `vocab-reveal`) sobre 183 aulas adultas
publicadas; o `min_slides` veio da REGRA 11 (piso), não da média, e é menor no Kids
porque a aula lá é de 30–45 min. Contrato apertado demais barra aula legítima, e o
prejuízo disso é maior que o de um contrato frouxo que se aperta depois no editor.

---

## 8. O EDITOR — o catálogo virou interface

`/catalogo.html` deixou de ser vitrine. Em cada método há **Editar**, e em cada
prateleira **+ novo método**. Dá pra criar um método, trocar o resumo e mexer no
contrato (marcar exercício como *obrigatório*, *proibido* ou *livre*, e o mínimo de
slides). A lista de exercícios oferecida é o banco — provado contra o builder, então
**não dá pra exigir o que o builder não sabe montar**.

### Salvar NÃO grava em produção — abre um PR

`api/save-framework.js` cria branch, commita o `frameworks.json` e abre PR. Os gates
rodam ali (GATE 12, GATE 11, banco) e o merge acontece no verde. A interface é rápida;
a segurança fica onde ela já morava.

O botão **Baixar JSON** existe sempre e não depende de backend. O arquivo baixado é
**byte-a-byte** o que entraria no PR, porque a mutação mora em um lugar só
(`public/lib/framework-edit.js`, carregado pelo navegador **e** pela função). Duas
cópias divergiriam no primeiro ajuste, e as duas "funcionariam".

### O que o editor NÃO deixa fazer, de propósito

| Bloqueio | Por quê |
|---|---|
| mudar `status` | promover a `producao` libera **aluno real** (GATE 11). É decisão pedagógica, não clique de tela. Método novo nasce `mock`. |
| editar contrato no lugar | toda mudança **sobe a versão** e empurra a anterior pro histórico — é o que impede a edição de hoje reprovar aula de ontem |
| exigir exercício fora do banco | o banco é gerado do builder; exigir o que ele não monta quebraria a aula na geração |

### Pelo terminal (sem token, sem navegador)

A MESMA regra, pela linha de comando — `scripts/framework-edit.mjs` carrega o mesmo
`public/lib/framework-edit.js`. **Três portas, uma regra só**: navegador, função
serverless e terminal. Editar o JSON na mão é a única porta que não sobe a versão
sozinha — e é por isso que ela não deve ser usada.

```
node scripts/framework-edit.mjs --listar               # métodos, contrato e versão
node scripts/framework-edit.mjs --ver adulto/ppp       # o contrato inteiro
node scripts/framework-edit.mjs --exercicios           # o banco, agrupado

node scripts/framework-edit.mjs --cat adulto --id ppp --tirar gapfill        # sobe pra v2
node scripts/framework-edit.mjs --cat adulto --id ppp --por reading --min 12
node scripts/framework-edit.mjs --cat adulto --id dogme --label "Dogme" \
  --obrigatorios dialogo,slide-tarefa,checklist --min 20                     # nasce mock
```

`--dry-run` mostra o resultado sem gravar. Depois é o fluxo de sempre: branch, commit,
PR, gates, merge.

### Configuração do editor por PR (opcional)

Vercel → Settings → Environment Variables:

| Variável | O que é |
|---|---|
| `GITHUB_TOKEN` | fine-grained token, só neste repo, com **Contents: RW** e **Pull requests: RW** |
| `CATALOGO_SENHA` | senha combinada — **o site é público**, e sem isso qualquer um abriria PR |

Sem as duas o endpoint responde 503 com mensagem clara e o editor continua servindo
pelo "Baixar JSON".

### Medido no navegador (31/07/2026)

Chromium dirigido: abre o editor do PPP com os 13 obrigatórios já marcados e o mínimo
de 14; desmarcar um exercício muda a prévia para `v1 → v2`; Escape fecha; "+ novo
método" abre em branco com o aviso de `mock`. Dois defeitos foram achados **assim** e
corrigidos: (1) o mesmo `imersivo-prototipo` existe em Adulto, Kids e Teens, e a busca
só por id abria o contrato da categoria errada — hoje cada prateleira abre o seu (25,
20 e 24 slides de piso); (2) resposta não-JSON estourava `Unexpected token '<'` na cara
de quem editava.
