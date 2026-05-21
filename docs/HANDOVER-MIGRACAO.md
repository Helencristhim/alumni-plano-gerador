# HANDOVER — Migração para Formato Individual por Aula

> **Este documento é a fonte de verdade para a migração.** Leia INTEGRALMENTE antes de qualquer ação. Ele sobrevive a compactações de contexto e contém tudo que você precisa.

---

## 1. CONTEXTO DO PROJETO

- **Repositório**: /Users/helenmendes/alumni-plano-gerador
- **Deploy**: https://alumni-plano-gerador.vercel.app
- **O que é**: Plataforma de materiais pedagógicos de inglês para alunos da Alumni by Better
- **Estrutura**: HTMLs estáticos em `public/professor/` e `public/aluno/`, deploy na Vercel via git push
- **Regras do sistema**: `CLAUDE.md` na raiz do projeto (ler sempre)

---

## 2. OBJETIVO DA MIGRAÇÃO

9 alunos têm todas as aulas num arquivo HTML monolítico. Precisamos que cada aula tenha seu próprio HTML individual, seguindo o padrão da Pricila Adamo.

**O conteúdo já existe.** A migração EXTRAI e REORGANIZA. Nada é gerado do zero.

---

## 3. REGRAS DE SEGURANÇA — INVIOLÁVEIS

```
1. NUNCA alterar nenhum arquivo existente
2. NUNCA deletar nenhum arquivo
3. NUNCA usar sed em arquivos HTML de aluno (já zerou arquivo antes)
4. NUNCA fazer deploy sem validar antes
5. Um aluno por vez — commitar, validar, só depois próximo
6. Conferir wc -l do main file ANTES e DEPOIS de cada operação
7. Pre-commit hook ativo: bloqueia HTML < 500 bytes ou que encolheu > 50%
8. Rodar bash scripts/pre-deploy-check.sh antes de todo push
```

---

## 4. APRENDIZADOS CRÍTICOS (erros que já aconteceram)

| Erro | O que causou | Como evitar |
|------|-------------|-------------|
| Arquivo zerado | `sed` com múltiplas substituições UTF-8 no macOS | Usar `Edit` tool ou `perl` em vez de sed |
| Arquivos 404 na Vercel | Arquivo existia local mas não estava no git | Sempre conferir `git ls-files` antes de assumir que está no ar |
| MP3s sem som | 4022 MP3s nunca commitados | Conferir `git status public/audio/` |
| lesson-progress.js 404 | Nunca commitado no git, quebrou stamps de TODOS os alunos | Conferir `public/lib/` está no git |
| Merge trouxe versão antiga | `git pull` aceitou versão remota antiga sobrescrevendo a correta | Cuidado com merges, conferir diff |
| Slides misturados (17/148) | Faltava lessonRanges no JS | Cada arquivo individual tem slides de UMA aula só, sem esse risco |

---

## 5. PADRÃO DE REFERÊNCIA

Usar `public/professor/pricila-adamo-aula2.html` como template estrutural.

Cada arquivo individual `slug-aulaN.html` contém:

```html
<head>
  meta charset, viewport, robots noindex
  title: "Professor View — {Nome} | Aula N | Alumni by Better"
  Google Fonts (Inter + Cormorant Garamond)
  Supabase CDN + supabase-config.js
  window.STUDENT_SLUG='{slug}'; window.TOTAL_AULAS={total};
  var audioMap = { /* SÓ frases desta aula */ };
  <style> /* CSS completo copiado do main */ </style>
</head>
<body>
  logo-bar (com slide-counter)
  main-content:
    header hero (mesmo do main)
    speed-control
    tabs (4 abas: Planejamento, Pre-class, IN CLASS, Complementares)
    tab-planning (currículo completo — mesmo em todas as aulas)
    tab-exercises (Pre-class SÓ desta aula — ex-lesson-N)
    tab-inclass (menu com 1 card para entrar nos slides)
  slides-wrapper FORA do main-content:
    phase-bar + phase-labels
    slides-container (slides SÓ desta aula, numerados de 1)
    nav-bar (prev/next + dots)
    teacher-panel
  tab-complementary (recomendações SÓ desta aula)
  confetti-container
  <script> /* JS completo — REGRA 26 do CLAUDE.md */ </script>
  <script src="/lib/lesson-progress.js"></script>
</body>
```

**REGRA CRÍTICA**: `slides-wrapper` DEVE ficar FORA do `main-content`. Senão `body.slide-mode .main-content { display:none }` esconde os slides.

---

## 6. ESTADO ATUAL — QUEM JÁ TEM INDIVIDUAL

| Aluno | Slug | Status | Individuais |
|-------|------|--------|-------------|
| Pricila Adamo | pricila-adamo | OK | aula2-5 |
| Patrícia Ruffo | patricia-ruffo | OK | aula1-5 |
| Percival Jr | percival-jr | OK | aula2-5 |
| Roberto Pires | roberto-pires | OK | aula1-5 |
| Tânia Rosa | tania-rosa | OK | aula2-8 |
| Gabriela Paulucci | gabriela-paulucci | OK | aula2-5 |

---

## 7. ROADMAP — ALUNOS A MIGRAR

### Etapa 1: Eduarda Gabriel (5 aulas)
- Main: `eduarda-gabriel.html` (7547 linhas)
- Criar: `eduarda-gabriel-aula1.html` até `eduarda-gabriel-aula5.html`
- Status: **PENDENTE**

### Etapa 2: Milton Sayegh (5 aulas)
- Main: `milton-sayegh.html` (6906 linhas)
- Criar: `milton-sayegh-aula1.html` até `milton-sayegh-aula5.html`
- Status: **PENDENTE**

### Etapa 3: Rafael Gasparelli Lima (5 aulas)
- Main: `rafael-gasparelli-lima.html` (6364 linhas)
- Criar: `rafael-gasparelli-lima-aula1.html` até `rafael-gasparelli-lima-aula5.html`
- Status: **PENDENTE**

### Etapa 4: Vanessa Maluf (5 aulas)
- Main: `vanessa-maluf.html` (8729 linhas)
- Criar: `vanessa-maluf-aula1.html` até `vanessa-maluf-aula5.html`
- Status: **PENDENTE**

### Etapa 5: Luiz Bressane (5 aulas)
- Main: `luiz-bressane.html` (8499 linhas)
- Criar: `luiz-bressane-aula1.html` até `luiz-bressane-aula5.html`
- Status: **PENDENTE**

### Etapa 6: Maísa de Oliveira Santos (5 aulas)
- Main: `maisa-de-oliveira-santos.html` (5530 linhas)
- Criar: `maisa-de-oliveira-santos-aula1.html` até `maisa-de-oliveira-santos-aula5.html`
- Status: **PENDENTE**

### Etapa 7: Elaine Mieko Pinho (5 aulas)
- Main: `elaine-mieko-pinho.html` (7358 linhas)
- Criar: `elaine-mieko-pinho-aula1.html` até `elaine-mieko-pinho-aula5.html`
- Status: **PENDENTE**

### Etapa 8: Daniela Feitoza (5 aulas — modelo antigo, SEM IN CLASS)
- Main: `daniela-feitoza.html` (4087 linhas)
- NOTA: Este aluno usa modelo antigo de 5 abas, sem slides IN CLASS
- Criar individuais só com Pre-class + Complementares (sem IN CLASS)
- Status: **PENDENTE**

### Etapa 9: Gabriela Pires (10 aulas — 2 blocos)
- Main: `gabriela-pires.html` (8085 linhas)
- Bloco 1 (aulas 1-5): têm Pre-class + IN CLASS completos
- Bloco 2 (aulas 21-25): têm Pre-class + IN CLASS completos
- Criar: `gabriela-pires-aula1.html` até `gabriela-pires-aula5.html` + `gabriela-pires-aula21.html` até `gabriela-pires-aula25.html`
- Status: **PENDENTE**

---

## 8. PROCESSO POR AULA (executar para cada uma)

```
1. Ler o main file (Read tool, NÃO cat)
2. Identificar os intervalos de linhas:
   - Pre-class: entre ex-lesson-N e ex-lesson-(N+1)
   - Slides: linhas com data-lesson="N"
   - Complementares: media cards da aula N
3. Ler pricila-adamo-aula2.html como template estrutural
4. Montar o arquivo individual usando Write tool:
   - Seções fixas do main (head, CSS, header, planejamento, JS)
   - Seções específicas da aula N (pre-class, slides, complementares)
   - audioMap filtrado (só frases desta aula)
   - Slides renumerados a partir de 1
5. Validar ANTES de commitar:
   - wc -l do novo arquivo > 1000
   - grep -c 'tab-btn' = 4+ (tem as 4 abas)
   - grep -c 'vocab-card' > 0 (Pre-class existe)
   - grep -c 'data-slide=' = 25-35 (slides existem)
   - grep -c 'STUDENT_SLUG' > 0 (Supabase OK)
   - wc -l do main file = mesmo de antes (não foi alterado)
6. git add + commit + push (SÓ o novo arquivo)
7. Confirmar na Vercel: curl -s -o /dev/null -w "%{http_code}" da URL
8. Atualizar este documento: mudar Status de PENDENTE para OK
```

---

## 9. TAMANHOS DOS MAIN FILES (validação)

Após CADA operação, conferir que estes números NÃO mudaram:

```
gabriela-pires.html:            8085 linhas
elaine-mieko-pinho.html:        7358 linhas
eduarda-gabriel.html:           7547 linhas
luiz-bressane.html:             8499 linhas
maisa-de-oliveira-santos.html:  5530 linhas
milton-sayegh.html:             6906 linhas
rafael-gasparelli-lima.html:    6364 linhas
vanessa-maluf.html:             8729 linhas
daniela-feitoza.html:           4087 linhas
```

Se QUALQUER número mudar, PARAR TUDO e investigar.

---

## 10. COMO FILTRAR O AUDIOMAP POR AULA

O audioMap do main tem frases de TODAS as aulas. Para o individual, filtrar:

```
1. Extrair Pre-class + slides da aula N para uma string
2. Buscar todas as chamadas speakText('...') e data-phrase="..." nessa string
3. Coletar as frases únicas
4. Do audioMap do main, manter SÓ as entradas cujas chaves estão na lista
5. Conferir que nenhuma frase ficou sem MP3
```

---

## 11. COMO RENUMERAR SLIDES

Os slides no monolítico usam data-slide="1" até data-slide="146" (todas as aulas juntas). No individual, renumerar:

```
Aula 1: slides 1-28 no main → data-slide="1" até "28" no individual (sem mudança)
Aula 2: slides 29-55 no main → data-slide="1" até "27" no individual
Aula 3: slides 56-85 no main → data-slide="1" até "30" no individual
```

Atualizar também: totalSlides no JS, slideCounter, dots, e qualquer referência a número de slide.

---

## 12. FERRAMENTAS DE APOIO

- `bash scripts/pre-deploy-check.sh` — governança pré-deploy
- Pre-commit hook em `.git/hooks/pre-commit` — bloqueia HTMLs vazios/corrompidos
- `public/governanca.html` — auditoria visual por aluno na Vercel

---

## 13. APÓS COMPLETAR TODA MIGRAÇÃO

1. Atualizar `CLAUDE.md`: formato individual é OBRIGATÓRIO para novos materiais
2. Atualizar `docs/MIGRACAO-FORMATO-INDIVIDUAL.md`: marcar todos como OK
3. Atualizar governança: verificar individuais
4. Main files mantidos como backup (NUNCA deletar)
5. Rodar governança em todos os alunos para confirmar zero problemas
