# API Contract — Alumni by Better

Contrato de cada API do projeto. Toda mudança em inputs/outputs deve atualizar este documento.

---

## POST /api/perfil-360

Gera Perfil 360 a partir da transcrição da consultoria.

### Request

```json
{
  "nome": "string (obrigatório)",
  "email": "string (obrigatório)",
  "whatsapp": "string (opcional)",
  "numAulas": "string/number (obrigatório)",
  "duracao": "string (obrigatório)",
  "frequencia": "string (obrigatório)",
  "modalidade": "string (obrigatório)",
  "plataforma": "string (condicional — se online)",
  "temAudio": "boolean",
  "audioUrl": "string (opcional)",
  "transcricao": "string (obrigatório, mín 200 palavras)",
  "observacoesProfessor": "string (opcional, mas crítico)"
}
```

### Response (200)

```json
{
  "id": "slug-do-aluno",
  "perfil": {
    "dadosExtraidos": {
      "idade": { "valor": "47", "selo": "🟢", "evidencia": "...", "encontrado": true },
      "profissao": { "valor": "...", "selo": "🟢", "evidencia": "...", "encontrado": true },
      "cidade": { "valor": "...", "selo": "🟢", "evidencia": "...", "encontrado": true },
      "nivel": { "valor": "B1 (Intermediário)", "selo": "🟡", "evidencia": "...", "encontrado": true },
      "foco": { "valor": "Travel English", "selo": "🟢", "evidencia": "...", "encontrado": true },
      "historico": { "valor": "...", "selo": "🟢", "evidencia": "...", "encontrado": true },
      "eventoAlvo": { "valor": { "tipo": "...", "data": "...", "local": "...", "stake": "...", "vitoria": "..." }, "selo": "🟡", "evidencia": "...", "encontrado": true },
      "hobbies": { "valor": null, "selo": "🔴", "evidencia": "...", "encontrado": false }
    },
    "resumoExecutivo": "string (mín 100 chars)",
    "frasesTextuais": [
      { "frase": "string", "uso": "promessa_programa|cabecalho_material|definicao_jornada|citacao_motivacional", "contexto": "string" }
    ],
    "promessaTransformadora": "string",
    "personagemJornada": { "de": "string", "para": "string", "emQuantasAulas": 5 },
    "mapaPersonalidade": {
      "introversaoExtroversao": { "valor": 1-10, "inferencia": "string", "confianca": 0-100, "selo": "🟢|🟡|🟠|🔴", "evidencias": ["string"] },
      "seriedadeLudicidade": { "...mesmo formato..." },
      "reflexivoImpulsivo": { "..." },
      "confianteInseguro": { "..." },
      "toleranciaErro": { "valor": "alta|media|baixa", "..." },
      "estiloAprendizagem": { "valor": "visual|auditivo|cinestesico|leitura_escrita", "..." },
      "energiaPreferida": { "valor": "calma_estruturada|dinamica_variada|mista", "..." }
    },
    "forcas": [{ "item": "string", "selo": "🟢|🟡|🟠", "evidencia": "string" }],
    "melhorias": [{ "item": "string", "selo": "🟢|🟡|🟠", "evidencia": "string" }],
    "necessidadesPedagogicas": {
      "adaptacaoNivel": "string",
      "adaptacaoIdade": "string",
      "estiloAprendizagem": "string",
      "toleranciaTraducao": "alta|media|baixa",
      "ritmoIdeal": "string",
      "tiposExercicio": ["string"],
      "midiasApropriadas": ["string"],
      "adaptacaoModalidade": "string"
    },
    "indicacaoProfessor": { "perfilIdeal": "string", "justificativa": ["string"] },
    "justificativaPrograma": "string (mín 50 chars)",
    "stakeAutomatico": { "texto": "string", "evidencia": "string", "selo": "🟢|🟡|🟠|🔴" },
    "vitoriaAutomatica": { "texto": "string", "evidencia": "string", "selo": "🟢|🟡|🟠|🔴" },
    "perguntasValidacao": ["string"],
    "conflitosIdentificados": ["string"]
  },
  "dadosExtraidos": "referência a perfil.dadosExtraidos",
  "dadosFormulario": { "nome": "...", "email": "...", "..." },
  "transcricao": "string completa",
  "observacoesProfessor": "string",
  "criadoEm": "ISO timestamp",
  "status": "rascunho"
}
```

### Response (500) — Erro

```json
{
  "error": "JSON_PARSE_ERROR | string genérica",
  "message": "Mensagem amigável para o frontend",
  "retries": 3,
  "lastError": "Detalhes técnicos",
  "responseLength": 22000
}
```

### Validações aplicadas

1. `robustJSONParse()` — sanitização + 3 estratégias de parse
2. Retry com feedback (até 2 retries) se JSON malformado
3. `validatePerfil()` — verifica completude (resumo, 7 eixos, 3+ forças, 3+ melhorias, promessa, justificativa)
4. Retry com feedback (até 2 retries) se perfil incompleto
5. Charset header UTF-8

### Modelo

`claude-sonnet-4-6` com `max_tokens: 16000`

### Timeout

`maxDuration: 300` (Vercel Pro)

---

## POST /api/gerar-plano

Gera plano pedagógico completo com exercícios.

### Request

```json
{
  "nome": "string",
  "idade": "number",
  "localizacao": "string",
  "profissao": "string",
  "frequencia": "string",
  "nivel": "string",
  "historico": "string",
  "objetivo": "string",
  "numAulas": "number",
  "observacoes": "string",
  "transcricao": "string (opcional)"
}
```

### Response (200)

```json
{
  "id": "slug-timestamp",
  "plano": {
    "aluno": { "nome", "localizacao", "profissao", "frequencia", "nivel", "historico" },
    "objetivoPedagogico": "string",
    "diagnostico": { "forcas": ["string"], "melhorias": ["string"] },
    "metodologia": [{ "titulo": "string", "descricao": "string" }],
    "aulas": [{ "numero": 1, "fase": "foundation", "tema": "...", "focoLinguistico": "...", "atividadeEmSala": "...", "deverDeCasa": "..." }],
    "continuidade": "string",
    "exercicios": [{ "aulaNumero": 1, "tema": "...", "vocabulario": [...], "frasesPronuncia": [...], "completarFrases": [...], "quiz": [...], "dialogo": {...}, "midias": [...] }]
  },
  "criadoEm": "ISO timestamp"
}
```

### Validações

1. `robustJSONParse()` + logging de erros

### Modelo

`claude-sonnet-4-6` com `max_tokens: 16000`

---

## POST /api/assistente

Modifica plano existente via instrução do professor.

### Request

```json
{
  "plano": { "...plano completo..." },
  "instrucao": "string com a alteração desejada"
}
```

### Response (200)

```json
{
  "plano": { "...plano atualizado..." }
}
```

### Validações

1. `robustJSONParse()` + logging de erros

### Modelo

`claude-sonnet-4-6` com `max_tokens: 16000`
