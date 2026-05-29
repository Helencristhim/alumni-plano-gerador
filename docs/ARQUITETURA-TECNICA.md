# Arquitetura Tecnica — Alumni Plano Gerador

> Documentacao completa da arquitetura, banco de dados, fluxos de dados e provedores.

---

## 1. VISAO GERAL

```
+------------------+       git push        +------------------+
|     GitHub       | --------------------> |     Vercel       |
|  (Repositorio)   |   (auto-deploy)      |  (Hosting +      |
|                  |                       |   Serverless)    |
+------------------+                       +------------------+
                                                  |
                              +-------------------+-------------------+
                              |                   |                   |
                        Static Files        API Routes          CDN Assets
                        /public/**          /api/**             Fonts, JS
                              |                   |
                              v                   v
                     +------------------+  +------------------+
                     |   Browser        |  |  Anthropic API   |
                     |   (Professor/    |  |  (Claude Sonnet) |
                     |    Aluno)        |  +------------------+
                     +------------------+         |
                              |                   |
                              v                   v
                     +------------------+  +------------------+
                     |    Supabase      |  |   ElevenLabs     |
                     |  (PostgreSQL)    |  |  (TTS Audio)     |
                     +------------------+  +------------------+
```

**Stack:**
- **Frontend**: HTML estatico + Vanilla JS (sem framework)
- **Backend**: Vercel Serverless Functions (Node.js)
- **Database**: Supabase (PostgreSQL)
- **AI**: Anthropic Claude Sonnet 4.6
- **Audio**: ElevenLabs TTS
- **Deploy**: Vercel via GitHub (auto-deploy on push)

---

## 2. DIAGRAMA ENTIDADE-RELACIONAMENTO

```
+============================================+
|                  perfis                     |
+============================================+
| PK  id              TEXT                   |  <-- slug do aluno (ex: "eduarda-gabriel")
|     nome            TEXT                   |
|     nivel           TEXT                   |  <-- CEFR: A0, A1, A2, B1, B1+, B2, C1, C2
|     num_aulas       INTEGER                |
|     foco            TEXT                   |  <-- "Business English", "Travel English", etc.
|     status          TEXT                   |  <-- rascunho | em_revisao | aprovado | material_publicado | sem_perfil
|     ativo           BOOLEAN                |  <-- aluno ativo na plataforma
|     deactivated     BOOLEAN                |  <-- aluno arquivado
|     professor       TEXT                   |  <-- nome do professor alocado
|     horarios        TEXT                   |  <-- "Sextas, 08h"
|     alocacao        JSONB                  |  <-- dados de alocacao (dias, horarios, detalhes)
|     data            JSONB                  |  <-- Perfil 360 completo (ver estrutura abaixo)
|     created_at      TIMESTAMP WITH TZ      |  <-- auto
|     updated_at      TIMESTAMP WITH TZ      |  <-- auto
+============================================+
           |
           | 1:N (semantico, sem FK explicita)
           |
+============================================+
|            lesson_progress                 |
+============================================+
| PK  student_slug    TEXT                   |  <-- referencia perfis.id
| PK  lesson_number   INTEGER                |  <-- numero da aula (1, 2, 3...)
|     inclass_done    BOOLEAN                |  <-- aula completada (5/5 checks)
|     inclass_marked_at TIMESTAMP WITH TZ    |  <-- quando foi marcada
+============================================+
  Composite PK: (student_slug, lesson_number)
```

### Estrutura do campo `perfis.data` (JSONB)

```json
{
  "dadosFormulario": {
    "nome": "Eduarda Gabriel",
    "nivel": "B1+",
    "numAulas": 50,
    "foco": "Business English",
    "modalidadeAula": "Online",
    "dataEvento": "",
    "tipoEvento": ""
  },
  "dadosExtraidos": {
    "nivel": { "valor": "B1+", "justificativa": "..." },
    "forcas": ["..."],
    "pontosMelhoria": ["..."]
  },
  "perfil": {
    "jornada": "De X a Y",
    "promessa": "...",
    "curriculo": [
      { "aula": 1, "tema": "...", "foco": "...", "atividade": "...", "homework": "..." }
    ]
  },
  "transcricao": "...",
  "observacoesProfessor": "...",
  "blocosGeracoes": [
    { "bloco": 1, "status": "gerado", "aulas": [1,2,3,4,5] }
  ],
  "status": "aprovado"
}
```

---

## 3. PROVEDORES E SERVICOS

### 3.1 Vercel (Hosting + Serverless)

| Item | Detalhe |
|------|---------|
| **URL de producao** | https://alumni-plano-gerador.vercel.app |
| **Tipo** | Static Files + Serverless Functions |
| **Deploy** | Automatico via git push (GitHub webhook) |
| **Diretorio estatico** | `/public/` |
| **Functions** | `/api/` (Node.js) |

**Serverless Functions:**

| Endpoint | Timeout | Funcao |
|----------|---------|--------|
| `POST /api/perfil-360` | 800s | Gera Perfil 360 via Claude |
| `POST /api/gerar-plano` | 300s | Gera plano de aulas via Claude |
| `POST /api/gerar-temas` | 800s | Gera temas de aulas via Claude |
| `POST /api/assistente` | 300s | Modifica plano via Claude |
| `POST /api/save-perfil` | 30s | Salva perfil no Supabase |
| `POST /api/save-alocacao` | default | Salva alocacao professor/horario |

**Variaveis de ambiente (Vercel Dashboard):**

| Variavel | Uso |
|----------|-----|
| `ANTHROPIC_API_KEY` | Acesso a API Claude |
| `SUPABASE_URL` | URL do projeto Supabase |
| `SUPABASE_SERVICE_KEY` | Chave de servico Supabase (server-side) |
| `ELEVENLABS_API_KEY` | Geracao de audio TTS |

### 3.2 Supabase (Banco de Dados)

| Item | Detalhe |
|------|---------|
| **URL** | https://xxdggcopydghbmgqqebq.supabase.co |
| **Tipo** | PostgreSQL gerenciado + API REST |
| **Chave publica** | `sb_publishable_RjekGapp8WtVbDx0J8etDg_hVq7na29` |
| **SDK** | `@supabase/supabase-js` v2 (CDN no browser, npm no server) |
| **Tabelas** | `perfis`, `lesson_progress` |

### 3.3 Anthropic Claude (IA)

| Item | Detalhe |
|------|---------|
| **Modelo** | `claude-sonnet-4-6` |
| **SDK** | `@anthropic-ai/sdk` v0.39.0 |
| **Uso** | Geracao de perfis, planos de aula, temas |
| **Chamado por** | Serverless functions (`/api/`) |

### 3.4 ElevenLabs (Audio TTS)

| Item | Detalhe |
|------|---------|
| **Endpoint** | `https://api.elevenlabs.io/v1/text-to-speech/{voice_id}` |
| **Formato** | MP3 44100Hz 128kbps |
| **Vozes** | Arthur (`sfJopaWaOtauCD3HKX6Q`) e Ellen (`BIvP0GN1cAtSRTxNHnWS`) |
| **Regra** | Alternar Arthur/Ellen (nunca voz unica) |
| **Uso** | Build-time (scripts locais), nao em runtime |
| **Armazenamento** | `/public/audio/{slug}/` (arquivos estaticos no repo) |

### 3.5 Outros CDNs

| Servico | URL | Uso |
|---------|-----|-----|
| **Google Fonts** | `fonts.googleapis.com` | Inter + Cormorant Garamond |
| **jsDelivr** | `cdn.jsdelivr.net` | Supabase JS SDK no browser |
| **Unsplash** | `images.unsplash.com` | Fotos de fundo (hero, slides, stamps) |

---

## 4. FLUXOS DE DADOS

### 4.1 Criacao de Novo Aluno

```
Professor preenche            API Serverless              Supabase
formulario (index.html)       /api/perfil-360             tabela: perfis
        |                          |                          |
        |-- POST dados ---------> |                          |
        |                         |-- Claude Sonnet -------> |  (gera Perfil 360)
        |                         |<-- JSON Perfil 360 ----- |
        |                         |-- UPSERT -------------> |  perfis (id, data, status, nome, nivel...)
        |<-- Redirect perfil.html |                          |
        |                          |                          |
```

**Colunas escritas:** `id`, `data` (JSONB completo), `status`, `nome`, `nivel`, `num_aulas`, `foco`

### 4.2 Dashboard — Carregamento

```
Professor abre                  Supabase                   Registry JSON
dashboard.html                  tabela: perfis             /planos/registry.json
     |                               |                          |
     |-- SELECT all perfis --------> |                          |
     |<-- Array de alunos ---------- |                          |
     |-- fetch registry.json --------|------------------------> |
     |<-- Array legacy -------------|--------------------------|
     |                               |                          |
     |-- MERGE (Supabase + Registry) |                          |
     |-- Renderiza cards             |                          |
     |-- checkMaterialExists()       |  (verifica se HTML existe na Vercel)
```

**Colunas lidas:** `id`, `data`, `status`, `nome`, `nivel`, `num_aulas`, `foco`, `ativo`, `deactivated`, `professor`, `horarios`, `alocacao`, `created_at`, `updated_at`

### 4.3 Alocacao de Professor

```
Manager clica "Fazer Alocacao"    API Serverless              Supabase
no dashboard                      /api/save-alocacao          tabela: perfis
     |                                  |                          |
     |-- POST {id, professor, horarios} |                          |
     |                                  |-- SELECT data ---------> |  (le estado atual)
     |                                  |<-- JSONB atual --------- |
     |                                  |-- MERGE novo + atual     |
     |                                  |-- UPDATE data ----------> |  (data mesclado)
     |                                  |-- UPDATE professor -----> |  (coluna top-level)
     |                                  |-- UPDATE horarios ------> |  (coluna top-level)
     |<-- 200 OK -------------------- |                          |
```

### 4.4 Progresso de Aula (Stamps/Checklist)

```
Professor marca 5/5 checks        lesson-progress.js          Supabase
no "What I Learned"                                           tabela: lesson_progress
     |                                  |                          |
     |-- toggleCheck() (5/5 done) ---> |                          |
     |                                  |-- UPSERT {              |
     |                                  |    student_slug,         |
     |                                  |    lesson_number,        |
     |                                  |    inclass_done: true,   |
     |                                  |    inclass_marked_at     |
     |                                  |  } --------onConflict--> |
     |                                  |                          |
     |-- Stamp acende (visual) <------ |                          |
     |-- Progress bar atualiza <------ |                          |
```

**Na carga da pagina:**

```
Pagina carrega                  lesson-progress.js          Supabase
(professor ou aluno .html)                                  tabela: lesson_progress
     |                                  |                          |
     |-- loadGlobalProgress() -------> |                          |
     |                                  |-- SELECT lesson_number,  |
     |                                  |   inclass_done           |
     |                                  |   WHERE student_slug --> |
     |                                  |<-- Array de aulas ------ |
     |<-- Stamps acesos + barra ------- |                          |
```

### 4.5 Geracao de Audio (Build-time)

```
Desenvolvedor roda               ElevenLabs API              Repositorio
script local                     /v1/text-to-speech          /public/audio/{slug}/
     |                                  |                          |
     |-- POST {text, voice_id} ------> |                          |
     |<-- MP3 binary ---------------- |                          |
     |-- Salva arquivo ---------------------------------> *.mp3    |
     |-- git add + commit + push                                   |
     |                                                             |
     |  (Vercel auto-deploy serve os MP3s como static files)       |
```

### 4.6 Acoes do Dashboard

| Acao | Operacao Supabase | Tabela | Colunas |
|------|-------------------|--------|---------|
| Tornar Ativo | `UPDATE` | perfis | `ativo = true` |
| Remover dos Ativos | `UPDATE` | perfis | `ativo = false` |
| Arquivar | `UPDATE` | perfis | `deactivated = true` |
| Reativar | `UPDATE` | perfis | `deactivated = false` |
| Excluir | `DELETE` | perfis | (remove row inteira) |
| Editar Professor | `UPDATE` via API | perfis | `professor`, `data.professor` |
| Editar Horarios | `UPDATE` via API | perfis | `horarios`, `data.horarios` |

---

## 5. MAPA DE ARQUIVOS

```
alumni-plano-gerador/
|
|-- api/                              # Serverless Functions (Vercel)
|   |-- perfil-360.js                 # POST: Gera Perfil 360 (Claude + Supabase)
|   |-- gerar-plano.js                # POST: Gera plano de aulas (Claude)
|   |-- gerar-temas.js                # POST: Gera temas (Claude)
|   |-- assistente.js                 # POST: Modifica plano (Claude)
|   |-- save-perfil.js                # POST: Salva perfil (Supabase UPSERT)
|   |-- save-alocacao.js              # POST: Salva alocacao (Supabase UPDATE)
|
|-- public/                           # Arquivos Estaticos (Vercel hosting)
|   |-- dashboard.html                # Painel de alunos (cards, filtros, acoes)
|   |-- index.html                    # Formulario de intake (8 blocos)
|   |-- perfil.html                   # Perfil 360 do aluno
|   |-- governanca.html               # Auditoria de qualidade dos materiais
|   |
|   |-- professor/                    # Materiais do professor
|   |   |-- {slug}.html               # Material monolitico (todas as aulas)
|   |   |-- {slug}-new.html           # Hub individual (links para aulas)
|   |   |-- {slug}-new-aula{N}.html   # Material individual por aula (4 abas)
|   |
|   |-- aluno/                        # Materiais do aluno (derivado do professor)
|   |   |-- {slug}.html               # Material do aluno (2 abas: Pre-class + Complementares)
|   |
|   |-- audio/{slug}/                 # MP3s ElevenLabs por aluno
|   |
|   |-- lib/
|   |   |-- supabase-config.js        # Cliente Supabase (URL + anon key)
|   |   |-- lesson-progress.js        # Tracking de progresso (stamps/checklist)
|   |
|   |-- assets/
|   |   |-- logo-alumni.png           # Logo Alumni by Better
|   |
|   |-- styles/
|       |-- design-system.css         # Design system global
|
|-- scripts/                          # Scripts de apoio
|   |-- pre-deploy-check.sh           # Governanca pre-deploy
|   |-- migrate-to-supabase.js        # Migracao localStorage -> Supabase
|   |-- extract-individual.py         # Extrai aulas individuais do monolitico
|   |-- create-hub.py                 # Cria pagina hub para aulas individuais
|
|-- docs/                             # Documentacao
|   |-- HANDOVER-MIGRACAO.md          # Plano de migracao individual
|   |-- MIGRACAO-FORMATO-INDIVIDUAL.md# Detalhes tecnicos da migracao
|   |-- ARQUITETURA-TECNICA.md        # Este documento
|
|-- vercel.json                       # Config de deploy (timeouts, output dir)
|-- CLAUDE.md                         # Regras do sistema (28 regras)
|-- .git/hooks/pre-commit             # Bloqueia HTML vazio/corrompido
```

---

## 6. SEGURANCA

| Aspecto | Implementacao |
|---------|---------------|
| **Autenticacao** | Nenhuma (acesso publico via anon key) |
| **RLS (Row Level Security)** | Deve estar configurado no Supabase Dashboard |
| **Chaves de API** | Server-side via env vars (nunca expostas no browser) |
| **Chave publica Supabase** | Exposta no browser (segura com RLS) |
| **HTTPS** | Sim (Vercel forcado) |
| **robots noindex** | Sim em todos os materiais de aluno |

---

## 7. RESUMO DE OPERACOES POR TABELA

### Tabela `perfis` (13 operacoes)

| Operacao | Arquivo | Trigger |
|----------|---------|---------|
| UPSERT | `/api/perfil-360.js` | Gerar Perfil 360 |
| UPSERT | `/api/save-perfil.js` | Salvar perfil |
| UPSERT | `index.html` | Submit formulario |
| UPSERT | `dashboard.html` | Migracao localStorage |
| UPSERT | `perfil.html` | Editar perfil |
| UPSERT | `migrate-to-supabase.js` | Migracao batch |
| SELECT | `dashboard.html` | Carregar cards |
| SELECT | `perfil.html` | Carregar perfil |
| SELECT | `governanca.html` | Auditoria |
| SELECT+UPDATE | `/api/save-alocacao.js` | Alocar professor |
| UPDATE | `dashboard.html` | Ativar/desativar/arquivar |
| DELETE | `dashboard.html` | Excluir aluno |

### Tabela `lesson_progress` (2 operacoes)

| Operacao | Arquivo | Trigger |
|----------|---------|---------|
| UPSERT | `lesson-progress.js` | Professor marca 5/5 checks |
| SELECT | `lesson-progress.js` | Carga da pagina (progress bar + stamps) |
