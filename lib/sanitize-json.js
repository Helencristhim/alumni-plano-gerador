/**
 * ALUMNI — Sanitização e parsing robusto de JSON da Anthropic API
 * Reutilizável em todas as APIs: perfil-360, gerar-plano, assistente
 *
 * Camadas de robustez:
 * 1. Sanitização de caracteres problemáticos
 * 2. Múltiplas estratégias de parse
 * 3. Logging estruturado de erros
 */

/**
 * Sanitiza string JSON bruta antes de parse.
 * Remove/corrige problemas comuns na geração por LLMs.
 */
function sanitizeJSON(raw) {
  if (!raw || typeof raw !== 'string') return raw;

  let s = raw;

  // Remove BOM (Byte Order Mark)
  s = s.replace(/^\uFEFF/, '');

  // Remove whitespace e caracteres invisíveis no início/fim
  s = s.trim();

  // Remove markdown wrapping (```json ... ```)
  s = s.replace(/^```(?:json)?\s*\n?/i, '').replace(/\n?```\s*$/i, '');
  s = s.trim();

  // Substitui aspas curvas (smart quotes) por aspas retas
  s = s.replace(/[\u201C\u201D\u201E\u201F\u2033\u2036]/g, '"');
  s = s.replace(/[\u2018\u2019\u201A\u201B\u2032\u2035]/g, "'");

  // Remove trailing commas antes de } ou ]
  s = s.replace(/,\s*([}\]])/g, '$1');

  // Remove caracteres de controle (exceto \n \r \t que são válidos em JSON escapados)
  s = s.replace(/[\x00-\x08\x0B\x0C\x0E-\x1F\x7F]/g, '');

  // Tenta consertar quebras de linha literais dentro de strings
  // (caracteres newline reais entre aspas — devem ser \n escapados)
  s = s.replace(/"([^"]*?)"/g, (match) => {
    return match.replace(/\n/g, '\\n').replace(/\r/g, '\\r').replace(/\t/g, '\\t');
  });

  return s;
}

/**
 * Tenta fazer parse de JSON com múltiplas estratégias de fallback.
 * Retorna { success: boolean, data: object|null, error: string|null, strategy: string }
 */
function robustJSONParse(rawText) {
  // Estratégia 1: Parse direto
  try {
    return { success: true, data: JSON.parse(rawText), error: null, strategy: 'direct' };
  } catch (e1) {
    // Continua para próxima estratégia
  }

  // Estratégia 2: Extrai bloco JSON + sanitiza
  let jsonText = rawText;
  const match = rawText.match(/\{[\s\S]*\}/);
  if (match) {
    jsonText = match[0];
  }

  const sanitized = sanitizeJSON(jsonText);

  try {
    return { success: true, data: JSON.parse(sanitized), error: null, strategy: 'sanitized' };
  } catch (e2) {
    // Continua para próxima estratégia
  }

  // Estratégia 3: Remoção agressiva de problemas
  let aggressive = sanitized;

  // Tenta consertar aspas não escapadas dentro de strings
  // Abordagem: encontra padrões "key": "value com "aspas" dentro"
  // e substitui aspas internas por aspas simples
  aggressive = aggressive.replace(/"([^"]{0,20}):\s*"([\s\S]*?)"\s*([,}\]])/g, (full, key, val, end) => {
    // Se o valor tem aspas internas não escapadas, substitui por aspas simples
    const fixedVal = val.replace(/(?<!\\)"/g, "'");
    if (fixedVal !== val) {
      return `"${key}: "${fixedVal}"${end}`;
    }
    return full;
  });

  try {
    return { success: true, data: JSON.parse(aggressive), error: null, strategy: 'aggressive' };
  } catch (e3) {
    // Todas as estratégias falharam
    return {
      success: false,
      data: null,
      error: e3.message,
      strategy: 'failed',
      rawLength: rawText.length,
      rawStart: rawText.substring(0, 200),
      rawEnd: rawText.substring(rawText.length - 200)
    };
  }
}

/**
 * Loga erro de parse estruturado no console do servidor.
 */
function logJSONError(context, error, attempt, rawText) {
  const logEntry = {
    timestamp: new Date().toISOString(),
    context,
    attempt,
    error: typeof error === 'string' ? error : error.message || String(error),
    responseLength: rawText ? rawText.length : 0,
    first200: rawText ? rawText.substring(0, 200) : '',
    last200: rawText ? rawText.substring(rawText.length - 200) : ''
  };
  console.error('=== ALUMNI JSON PARSE ERROR ===');
  console.error(JSON.stringify(logEntry, null, 2));
  return logEntry;
}

module.exports = { sanitizeJSON, robustJSONParse, logJSONError };
