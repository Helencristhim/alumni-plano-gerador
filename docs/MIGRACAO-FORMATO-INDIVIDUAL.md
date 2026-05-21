# Migração para Formato Individual por Aula

## REGRA MÁXIMA — NÃO NEGOCIÁVEL

**NUNCA alterar, mover ou deletar NENHUM arquivo existente.**
Os materiais atuais estão em uso por alunos e professores.
A migração CRIA arquivos novos. Os originais ficam intactos.

---

## O que é esta migração

9 alunos têm todas as aulas num arquivo só (monolítico). Precisamos que cada aula tenha seu próprio HTML, como já funciona para Pricila Adamo, Patrícia Ruffo, Percival Jr, Roberto Pires, Tânia Rosa e Gabriela Paulucci.

O conteúdo já existe nos arquivos monolíticos. A migração EXTRAI e REORGANIZA em arquivos individuais. Nada é gerado do zero.

---

## Padrão de Referência: Pricila Adamo

```
pricila-adamo.html          → main file (Planejamento geral + Pre-class de todas as aulas)
pricila-adamo-aula2.html    → 4 abas completas SÓ da aula 2
pricila-adamo-aula3.html    → 4 abas completas SÓ da aula 3
pricila-adamo-aula4.html    → 4 abas completas SÓ da aula 4
pricila-adamo-aula5.html    → 4 abas completas SÓ da aula 5
```

Cada arquivo individual tem:
- Planejamento (currículo completo — mesmo em todos)
- Pre-class (exercícios SÓ daquela aula)
- IN CLASS (slides SÓ daquela aula, renumerados a partir de 1)
- Complementares (recomendações SÓ daquela aula)
- audioMap filtrado (SÓ frases usadas naquela aula)
- CSS completo (copiado do main)
- JavaScript completo (REGRA 26 do CLAUDE.md — copiado integralmente)
- Supabase: STUDENT_SLUG + TOTAL_AULAS + lesson-progress.js

---

## Alunos que Precisam de Migração

| # | Aluno | Slug | Aulas com Conteúdo | Aulas com Slides |
|---|-------|------|--------------------|------------------|
| 1 | Eduarda Gabriel | eduarda-gabriel | 5 | 5 |
| 2 | Milton Sayegh | milton-sayegh | 5 | 5 |
| 3 | Rafael Gasparelli Lima | rafael-gasparelli-lima | 5 | 5 |
| 4 | Vanessa Maluf | vanessa-maluf | 5 | 5 |
| 5 | Luiz Bressane | luiz-bressane | 5 | 5 |
| 6 | Maísa de Oliveira Santos | maisa-de-oliveira-santos | 5 | 5 |
| 7 | Elaine Mieko Pinho | elaine-mieko-pinho | 5 | 5 |
| 8 | Daniela Feitoza | daniela-feitoza | 5 (modelo antigo) | 0 (sem IN CLASS) |
| 9 | Gabriela Pires | gabriela-pires | 10 (5+5 blocos) | 5 (só bloco 1) |

---

## Alunos já no Formato Correto (não mexer)

| Aluno | Slug | Individuais |
|-------|------|-------------|
| Pricila Adamo | pricila-adamo | aula2-5 |
| Patrícia Ruffo | patricia-ruffo | aula1-5 |
| Percival Jr | percival-jr | aula2-5 |
| Roberto Pires | roberto-pires | aula1-5 |
| Tânia Rosa | tania-rosa | aula2-8 |
| Gabriela Paulucci | gabriela-paulucci | aula2-5 |

---

## Mapeamento do Arquivo Monolítico (exemplo: Gabriela Pires)

O arquivo `gabriela-pires.html` (8085 linhas) tem esta estrutura:

```
Linhas 1-9:        <head> + audioMap (todas as aulas)
Linhas 10-1177:    CSS + Supabase config
Linhas 1178-1219:  Header (logo-bar + hero)
Linhas 1220-1652:  Slides aula 1 (data-lesson="1", slides 1-28)
Linhas 1653-2085:  Slides aula 2 (data-lesson="2", slides 29-55)
Linhas 2086-2550:  Slides aula 3 (data-lesson="3", slides 56-85)
Linhas 2551-3016:  Slides aula 4 (data-lesson="4", slides 86-115)
Linhas 3017-3648:  Slides aula 5 (data-lesson="5", slides 116-146)
Linhas 3649-3653:  Tabs navigation
Linhas 3654-3804:  Tab Planejamento (currículo 48 aulas)
Linhas 3805-4087:  Pre-class aula 1 (ex-lesson-1)
Linhas 4088-4370:  Pre-class aula 2 (ex-lesson-2)
Linhas 4371-4650:  Pre-class aula 3 (ex-lesson-3)
Linhas 4651-4932:  Pre-class aula 4 (ex-lesson-4)
Linhas 4933-5395:  Pre-class aula 5 (ex-lesson-5)
Linhas 5396-6576:  Pre-class aulas 21-25 (bloco 2, placeholders)
Linhas 6577-7215:  Pre-class aula 25 + restantes
Linhas 7216-7431:  Tab Complementares (todas as aulas)
Linhas 7432-8082:  JavaScript completo
Linhas 8083-8085:  lesson-progress.js + </body></html>
```

---

## Processo de Migração — Passo a Passo

### Para CADA aluno, para CADA aula:

**1. Ler o main file SEM alterá-lo**

**2. Copiar as seções fixas (iguais em todos os arquivos individuais):**
- `<head>` completo (meta, fonts, CSS)
- Header (logo-bar + hero)
- Tab Planejamento (currículo completo)
- JavaScript completo (REGRA 26)
- Supabase integration (CDN + config + STUDENT_SLUG + lesson-progress.js)

**3. Extrair as seções específicas da aula N:**
- Pre-class: conteúdo entre `ex-lesson-N` e `ex-lesson-(N+1)`
- Slides: todos os `<div class="slide"` com `data-lesson="N"`, renumerados de 1
- Complementares: media cards daquela aula
- audioMap: filtrar SÓ frases que aparecem no Pre-class + slides desta aula

**4. Montar o arquivo individual seguindo a estrutura da Pricila**

**5. Verificar ANTES de commitar:**
- [ ] Arquivo tem mais de 1000 linhas (não está vazio/truncado)
- [ ] 4 abas presentes (Planejamento, Pre-class, IN CLASS, Complementares)
- [ ] Pre-class tem: vocab-card, match-grid, Grammar in Context, Grammar Tip, blank-input, speech-card
- [ ] Slides: quantidade correta (28-31 por aula), numerados de 1
- [ ] audioMap: todas as frases com speakText têm entrada correspondente
- [ ] STUDENT_SLUG e TOTAL_AULAS presentes
- [ ] lesson-progress.js referenciado
- [ ] Main file NÃO foi alterado (conferir wc -l)

**6. Commitar e fazer deploy SÓ daquele aluno**

**7. Verificar na Vercel:**
- [ ] URL abre sem 404
- [ ] Tabs clicáveis
- [ ] Áudios funcionam
- [ ] Slides navegam

**8. Só então passar para o próximo aluno**

---

## Regras de Segurança INVIOLÁVEIS

1. **NUNCA alterar nenhum arquivo existente** — os .html atuais ficam como estão
2. **NUNCA deletar nenhum arquivo** — mesmo após migração completa
3. **NUNCA usar sed em arquivos de aluno** — risco de zerar o arquivo (já aconteceu)
4. **Pre-commit hook ativo** — bloqueia commit se arquivo HTML < 500 bytes ou encolheu > 50%
5. **Um aluno por vez** — commitar, validar, só depois próximo
6. **Conferir main file após cada operação** — wc -l deve manter o mesmo número de linhas
7. **Conferir áudios** — todos os MP3 referenciados no audioMap devem existir em public/audio/

---

## Verificação Final (após toda migração)

```bash
# Rodar para cada aluno migrado:
bash scripts/pre-deploy-check.sh

# Verificar que TODOS os main files continuam intactos:
for f in gabriela-pires elaine-mieko-pinho eduarda-gabriel luiz-bressane \
         maisa-de-oliveira-santos milton-sayegh rafael-gasparelli-lima \
         vanessa-maluf daniela-feitoza; do
  echo "$f: $(wc -l < public/professor/$f.html) linhas"
done

# Verificar que novos arquivos existem e não estão vazios:
for f in public/professor/*-aula*.html; do
  echo "$(basename $f): $(wc -l < $f) linhas"
done
```

---

## Tamanhos Esperados dos Main Files (referência para validação)

| Arquivo | Linhas (antes da migração) |
|---------|---------------------------|
| gabriela-pires.html | 8085 |
| elaine-mieko-pinho.html | 6697 |
| eduarda-gabriel.html | 8557 |
| luiz-bressane.html | 8866 |
| maisa-de-oliveira-santos.html | 5835 |
| milton-sayegh.html | 8272 |
| rafael-gasparelli-lima.html | 6364 |
| vanessa-maluf.html | 8490 |
| daniela-feitoza.html | 5277 |

Esses números DEVEM permanecer iguais após a migração. Se mudarem, algo foi alterado indevidamente.
