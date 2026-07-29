# Padrao: Exercicio de Ordenacao (Put It in Order)

> **O padrao SEGUE VALIDO** — no modelo (helen-mendes) e em todos os alunos. O que muda
> abaixo sao duas cautelas medidas em 28/07/2026, e uma excecao de UM aluno.

## Duas cautelas (medidas em aula, nao teoria)

**1. Ordene FRASES, nunca palavras soltas.** A variante *Word Order* espalhava as palavras
de uma frase unica como itens arrastaveis — inclusive uma **virgula**:

```
The likelihood / is / low / , / but / the impact / would be / severe
```

Virgula nao e unidade de sentido; nao ha o que "ordenar" ali. O Dan, sobre a aula 9 do
Rafael Pelizaro: *"o exercicio de ordering esta muito confuso."* Ordene as 5 frases/passos
do padrao (secao abaixo) — e so.

**2. O audio e o exercicio sao a MESMA coisa.** Ja esta no criterio 4 do checklist, e e o
criterio que mais quebra na pratica: se ha botao "Listen", o que o MP3 narra e o que esta na
tela. Um MP3 que narra CONSELHOS ("First, say clearly what is done today...") debaixo de um
exercicio que pede uma MENSAGEM CONCRETA nao e um exercicio dificil — e um exercicio
impossivel, porque a resposta nao esta no audio. Se nao da pra garantir o casamento, **o
botao nao entra** e a fonte vira um texto na tela.

## Excecao: rafael-pelizaro NAO usa ordering

O Pre-class dele saiu 100% do ordering em 28/07/2026 (aulas 1, 2, 4, 5, 6, 9, 12, 15, 18 →
*Complete the text* / *True or False*). Duas medicoes: a Stephanie achou repetitivo *("toda
aula tem o mesmo exercicio, so que em outro contexto, ai fica cansativo e realmente nao
agrega")* e o Dan achou confuso.

**Isso e personalizacao de aluno, nao mudanca de padrao.** O produto Black Private admite
customizacao exclusiva por aluno — decisao do Dan, 28/07/2026. NAO existe gate barrando
ordering, e NAO se deve propagar essa remocao para outros alunos nem para o modelo.

---

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
