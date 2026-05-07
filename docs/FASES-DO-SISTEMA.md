# FASES DO SISTEMA — Alumni by Better

Documento mestre que define o fluxo completo da plataforma em 3 fases.
Cada fase referencia documentos estruturais como fonte de verdade.

## Documentos Estruturais (fonte de verdade)

| Documento | Escopo | Referenciado por |
|---|---|---|
| `/docs/INVESTIGACAO-CONSULTORIA.md` | O que a IA investiga na transcrição | `api/perfil-360.js` |
| `/docs/REFERENCIA-FAAP.md` | Padrão de qualidade pedagógica e UX para materiais | Gerador de material |
| `/docs/PADROES-UX-ALUMNI.md` | Padrões de UX/design para toda interface | `design-system.css`, todos os componentes |
| `/docs/INTEGRACAO-ELEVENLABS.md` | Integração de áudio nos materiais | Gerador de material |
| `/docs/API-CONTRACT.md` | Contrato de cada API | Todas as APIs |
| `/docs/COMPONENTS.md` | Componentes visuais reutilizáveis | Todas as páginas |

## Infraestrutura de qualidade

| Arquivo | Função |
|---|---|
| `/lib/profile-schema.js` | Schema único de dados (fonte de verdade) |
| `/lib/sanitize-json.js` | Sanitização e parse robusto de JSON |
| `/lib/profile-validator.js` | Validação de completude do Perfil 360 |
| `/lib/aluno-data-validator.js` | Validação por fase |
| `/lib/strings-pt-br.js` | Strings centralizadas PT-BR |
| `/scripts/validate-accents.js` | Auditoria de acentuação (pré-deploy) |
| `/scripts/validate-coherence.js` | Validação de coerência interna (pré-publicação) |

---

## FASE 1 — CAPTAÇÃO COMPLETA DE DADOS

**O que é:** Gestor preenche formulário rico com 8 blocos + sobe áudio + cola transcrição + observações estruturadas.

**Arquivo:** `public/index.html`

**8 Blocos do formulário:**

| Bloco | Campos | Obrigatórios |
|---|---|---|
| 1. Perfil Pessoal | Nome, idade, profissão, cidade, modalidade trabalho, email, WhatsApp | Nome, email |
| 2. Programa Desejado | Foco, n° aulas, duração, frequência, modalidade, plataforma, horários | Foco, n° aulas, frequência, modalidade |
| 3. Urgência | Toggle evento + tipo, data, local | — |
| 4. Motivação Emocional | Stake, Vitória | Stake, Vitória |
| 5. Histórico com Inglês | Onde estudou, nível, tempo fora de aula | Nível |
| 6. Personalidade e Estilo | Estilo aprendizagem, estrutura, erros, energia | — |
| 7. Interesses Pessoais | Séries/filmes, músicas/podcasts, hobbies | — |
| 8. Consultoria | Áudio, transcrição, observações estruturadas | Transcrição (200+ palavras) |

**Output:** POST para `/api/perfil-360` com JSON de todos os campos. Salva em localStorage. Redirect para `perfil.html`.

**Validações:** Campos obrigatórios, transcrição mínima 200 palavras.

**Próxima fase:** Fase 2

---

## FASE 2 — INVESTIGAÇÃO PROFUNDA PELA IA (Perfil 360)

**O que é:** API processa TODOS os dados da Fase 1 e gera análise pedagógica completa.

**Arquivos:** `api/perfil-360.js`, `public/perfil.html`

**Referência:** `/docs/INVESTIGACAO-CONSULTORIA.md`

**O que a IA faz:**
1. **Valida** dados declarados pelo gestor contra transcrição (selos 🟢🟡🟠🔴)
2. **Capta** o que só a transcrição revela (frases textuais, vocabulário real, gaps, padrões de fala)
3. **Infere** baseado nas observações do professor (tolerância ao erro, estilo, energia, postura)
4. **Gera** análise pedagógica completa (9 seções + 10 campos extraídos)

**Output — 9 seções obrigatórias:**
1. Resumo executivo (mín 100 chars)
2. Frases textuais capturadas (mín 3)
3. Mapa de personalidade (7 eixos com evidência)
4. Forças (mín 3)
5. Melhorias (mín 3)
6. Necessidades pedagógicas (8 sub-campos)
7. Indicação de professor (nome + justificativa)
8. Justificativa do programa (mín 50 chars)
9. Promessa transformadora

**+ 10 campos extraídos da consultoria** (cada um com valor, selo, evidência, status encontrado/não):
idade, profissão, cidade, nível, foco, histórico, evento-alvo, hobbies, stake automático, vitória automática

**Validação obrigatória:** Schema validation (`/lib/profile-schema.js`) antes de retornar. Retry até 2x se incompleto. 500 SCHEMA_INCOMPLETE se falhar.

**Gestor revisa e aprova:** Perfil editável, status Rascunho → Em Revisão → Aprovado.

**Próxima fase:** Fase 3

---

## FASE 3 — GERAÇÃO DE MATERIAL PERSONALIZADO

**O que é:** Com Perfil 360 aprovado, gestor clica "Gerar Prompt" e cola no Claude Code. Material é gerado com 5 abas.

**Referências:**
- `/docs/REFERENCIA-FAAP.md` — 7 tipos de exercício, microcopy, estrutura de aula
- `/docs/PADROES-UX-ALUMNI.md` — identidade visual, UX, acessibilidade
- `/docs/INTEGRACAO-ELEVENLABS.md` — áudios em todos os blocos

**5 abas obrigatórias:**
1. Planejamento Pedagógico Completo
2. Pre-class (exercícios interativos — 7 tipos FAAP)
3. Plano de Aula (roteiro PPP com Teacher Guide)
4. Material do Professor (tela compartilhada, sem respostas)
5. Atividades Complementares (filmes, séries, podcasts, TED Talks)

**Coerência interna:** 8 regras obrigatórias (vocabulário fechado, estruturas coerentes, frases em múltiplos pontos, exercícios só com conteúdo apresentado, imagens conectadas, áudios = texto, guia referencia material exato, pre-class prepara não substitui).

**Duas visões públicas (sem senha):**
- `/professor/[slug]` — todas as 5 abas
- `/aluno/[slug]` — Pre-class + Atividades Complementares apenas

**Validação pré-publicação:** Script `/scripts/validate-coherence.js` + `/scripts/validate-accents.js`.

---

## FLUXO VISUAL

```
FASE 1 (index.html — 8 blocos)
    ↓ POST /api/perfil-360
FASE 2 (api/perfil-360.js → perfil.html)
    ↓ Gestor revisa + aprova + clica "Gerar Prompt"
FASE 3 (Claude Code terminal → material HTML → deploy Vercel)
    ↓ Gestor cola URL de volta
    ↓
Material live em duas visões:
  /professor/[slug] — completo
  /aluno/[slug] — pre-class + atividades
```
