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
| 3 | Um slug não pode ter aulas de frameworks diferentes | Um aluno segue um método; misturar no meio do curso confunde aluno e professora |

### Legado-tolerante (REGRA 30/31)

Aula **sem** a etiqueta `alumni-framework` é ignorada pelo gate. As ~1.240 aulas anteriores
a este eixo não têm a etiqueta e **não serão tocadas para ganhar uma** — elas já são
identificáveis pela estrutura (7 capítulos), e aula que já foi dada não se mexe.

> **Exceção conhecida:** `sandra-hayasaki-aula5` foi refeita em PPP antes desta conversa —
> é a única aula de aluno real fora do Imersivo. Sem etiqueta ⇒ o gate não a vê, de
> propósito: ela é legado, não um caso novo. Fica registrada aqui para não virar surpresa.

---

## 4. Como acrescentar um framework

1. Acrescente o objeto em `public/data/frameworks.json`, dentro da categoria certa, com
   `status: "documentado"` (ou `"mock"` quando já houver aluno mock).
2. Ponha o slug do aluno mock em `mocks.{id-do-framework}`.
3. Gere a aula do mock com `"framework": "{id}"` no config. O builder valida sozinho.
4. Valide (todos os gates + medição no navegador). **Só então** o Dan decide se promove a
   `producao` — e é a promoção que o libera para aluno real.

O catálogo se atualiza sozinho: ele desenha a prateleira a partir do JSON.
