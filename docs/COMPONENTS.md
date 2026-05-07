# Componentes Visuais — Alumni by Better

Padrões visuais reutilizáveis do sistema. Referência para consistência entre páginas.

---

## 1. Status Badges

4 estados com dot colorido + label.

| Estado | Classe CSS | Cor | Quando usar |
|---|---|---|---|
| Rascunho | `.badge--draft` | Amarelo (#b45309) | Perfil recém-criado, não revisado |
| Em Revisão | `.badge--review` | Laranja (#c2410c) | Gestor editando/revisando |
| Aprovado | `.badge--approved` | Verde (#16803d) | Pronto para gerar material |
| Publicado | `.badge--published` | Azul (#1e50c8) | Material live para o aluno |
| Sem Perfil | `.badge--none` | Cinza (#555566) | Aluno sem perfil 360 |

HTML: `<span class="badge badge--draft"><span class="badge__dot"></span>Rascunho</span>`

---

## 2. Cards de Campo Extraído

4 estados visuais para campos extraídos da consultoria.

| Estado | Visual | Quando usar |
|---|---|---|
| Encontrado (🟢) | Fundo branco, borda normal, dot verde | API encontrou na transcrição |
| Inferido (🟡) | Fundo branco, borda normal, dot amarelo | API inferiu de pistas indiretas |
| Moderado (🟠) | Fundo branco, borda normal, dot laranja | 1-2 sinais, confiança média |
| Não encontrado (🔴) | Fundo amarelo claro, borda warning, dot vermelho, mensagem | Nenhuma pista |

Classes: `.extracted-field`, `.extracted-field.not-found`

---

## 3. Componente de Evidência

Mostra citação da transcrição que justifica uma inferência.

```html
<div class="extracted-field__evidence">
  <svg><!-- Lucide quote icon --></svg>
  <strong>Evidência:</strong> "Trecho citado da transcrição"
</div>
```

Regras:
- Sempre entre aspas curvas (" ")
- Prefixado com "Evidência:" em bold
- Fonte: `--text-micro`, cor: `--text-dim`
- Ícone SVG de quote (Lucide) antes do texto

---

## 4. Banner de Validação

Dois tipos: warnings (amarelo) e errors (vermelho).

```html
<div class="validation-banner validation-banner--warning">
  <strong>Atenção:</strong> 3 campos não foram encontrados na consultoria.
</div>

<div class="validation-banner validation-banner--error">
  <strong>Erro:</strong> Perfil incompleto — faltam 2 eixos do mapa.
</div>
```

Regras:
- Warnings: fundo `--warning-bg`, borda `--warning-border`
- Errors: fundo `--error-bg`, borda `--error-border`
- Posição: topo da página, antes do conteúdo

---

## 5. Loading States

### Botão com spinner
```html
<button class="btn btn--primary is-loading">
  <span class="btn__spinner"></span> Processando...
</button>
```

### Texto de loading
```html
<div class="loading-text show">
  Gerando Perfil 360... Isso leva cerca de 2 minutos.
</div>
```

Regras:
- Botão: desabilitado + spinner + texto alterado
- Texto: fonte regular, cor muted, centralizado
- Nunca deixar UI sem feedback durante operação > 300ms

---

## 6. Estados Vazios

```html
<div class="empty-state">
  <h3>Nenhum aluno encontrado</h3>
  <p>Clique em "+ Novo Aluno" para começar.</p>
  <a href="index.html" class="btn btn--primary">Criar Primeiro Aluno</a>
</div>
```

Regras:
- Centralizado, padding generoso
- Título em `--text-dim`
- Mensagem explicativa
- CTA com botão primário

---

## 7. Modal

```html
<div class="modal-overlay show">
  <div class="modal">
    <h3 class="modal__title">Título</h3>
    <div class="modal__body">Conteúdo</div>
    <div class="modal__footer">
      <button class="btn btn--ghost">Cancelar</button>
      <button class="btn btn--primary">Confirmar</button>
    </div>
  </div>
</div>
```

Regras:
- Overlay: `rgba(0,0,0,0.3)`
- Modal: border-radius 12px, shadow-lg
- Fechar com Escape ou clique no overlay
- Botão primário sempre à direita

---

## 8. Selo de Confiança (Dot)

```html
<span class="extracted-field__seal" style="background: var(--success);" title="Fato declarado"></span>
```

| Selo | Cor | Significado |
|---|---|---|
| 🟢 | `--success` | Fato declarado pelo aluno |
| 🟡 | `--warning` | Inferência forte (3+ sinais) |
| 🟠 | `#c2410c` | Inferência moderada (1-2 sinais) |
| 🔴 | `--error` | Hipótese (precisa validação) |

Tamanho: 8x8px, border-radius 50%.

---

## 9. Indicador "Editado"

Quando gestor modifica um valor gerado pela IA:

```html
<span class="extracted-field__edited" title="Editado pelo gestor">Editado</span>
```

Regras:
- Aparece ao lado do selo quando `_editado === true`
- Fonte micro, cor `--text-dim`
- Ícone de lápis (opcional)
