# Padrao: Exercicio de Ordenacao (Put It in Order)

## Referencia: Patricia Ruffo (order-l3) = CORRETO

## Estrutura HTML obrigatoria

```
1. Instrucao: <p> "Put the sentences in the correct order."
2. Botao LISTEN (ANTES do container de frases)
3. Container com frases embaralhadas
4. Botao Check Order
```

## Botao Listen — posicao e formato EXATO

```html
<button class="btn btn-listen" onclick="speakText('[order-lN]', this)"
  style="margin-bottom:1rem;display:inline-flex;align-items:center;gap:.4rem;
  padding:.55rem 1.2rem;background:var(--accent);color:#fff;border:none;
  border-radius:8px;font-size:.85rem;font-weight:600;cursor:pointer">
  <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor"
    stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
    <polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/>
    <path d="M15.54 8.46a5 5 0 0 1 0 7.07"/>
    <path d="M19.07 4.93a10 10 0 0 1 0 14.14"/>
  </svg>
  Listen
</button>
```

**Posicao**: DEPOIS da instrucao `<p>`, ANTES do `<div class="order-container">`

## AudioMap — entrada obrigatoria

```javascript
"[order-lN]": "/audio/{slug}/order_lN_descriptive.mp3",
```

## Audio MP3 — conteudo obrigatorio

O MP3 deve conter EXATAMENTE as frases do HTML lidas na ordem correta (data-order 1, 2, 3...).

**Processo:**
1. Extrair todas as frases do `<span class="order-text">` do container
2. Ordenar por `data-order` (1, 2, 3...)
3. Concatenar em um unico texto
4. Gerar MP3 via ElevenLabs com esse texto

**Voz:** genero do aluno (Arthur=masculino, Ellen=feminino)

## Checklist de validacao (4 criterios)

| # | Criterio | Como verificar |
|---|----------|----------------|
| 1 | Botao Listen EXISTE e esta ANTES do container | grep no HTML |
| 2 | audioMap tem entrada `[order-lN]` | grep no audioMap |
| 3 | Arquivo MP3 existe no disco | ls no diretorio /audio/{slug}/ |
| 4 | Texto do MP3 = frases do HTML na ordem correta | comparar script de geracao vs HTML |

Se QUALQUER criterio falhar -> exercicio QUEBRADO.
