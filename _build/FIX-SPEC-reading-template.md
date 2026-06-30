# SPEC — 3 consertos do template de LEITURA (ic-reading / ic-tf) — 30/06/2026

Aplica-se a TODA aula que usa o template de leitura (classe `.ic-reading` e/ou `.ic-tf`).
Referência canônica: `public/professor/helen-mendes-aula3.html` (modelo) após o fix.
NÃO mudar layout fora desses componentes. Tudo aditivo/escopado.

## Bug A — texto + alternativas não cabem (rolagem)
O `.slide` tem `height:100%` e o pai `.slides-container{overflow:hidden}` corta o que
passa da viewport. Em slides com texto longo (`.ic-reading`) + card de escolhas, as
opções ficam cortadas.

**Fix (CSS, sweepável a todos):** capar a altura do bloco de texto e dar rolagem interna,
mantendo as escolhas visíveis abaixo. Inserir no `<style>` (logo após a regra `.ic-reading p`):
```css
.ic-reading{max-height:42vh;overflow-y:auto}
.ic-reading::-webkit-scrollbar{width:8px}
.ic-reading::-webkit-scrollbar-thumb{background:var(--border);border-radius:8px}
```
(idempotente: se `max-height:42vh` já estiver no `.ic-reading`, não duplicar.)

## Bug B — True/False mostra TRUE e FALSE juntos
Cada `.ic-tfrow` tem `<span class="ic-verdict ic-t">TRUE</span>` E `<span class="ic-verdict ic-f">FALSE</span>`,
e o CSS acende os dois ao revelar. Não há marcação do correto.

**Fix (CSS + markup):**
1. Em CADA `.ic-tfrow`, adicionar `data-answer="true"` ou `data-answer="false"` conforme a
   afirmação (LER a frase + a justificativa `.ic-just` pra decidir; é trabalho de conteúdo).
2. Substituir no `<style>` as 2 regras:
   ```css
   .ic-tfrow.ic-revealed .ic-verdict.ic-t { opacity: 1; background: var(--success-bg); color: var(--success); }
   .ic-tfrow.ic-revealed .ic-verdict.ic-f { opacity: 1; background: var(--danger-bg); color: var(--danger); }
   ```
   por:
   ```css
   .ic-verdict.ic-t { background: var(--success-bg); color: var(--success); }
   .ic-verdict.ic-f { background: var(--danger-bg); color: var(--danger); }
   .ic-tfrow[data-answer="true"] .ic-verdict.ic-f,
   .ic-tfrow[data-answer="false"] .ic-verdict.ic-t { display: none; }
   .ic-tfrow.ic-revealed .ic-verdict { opacity: 1; }
   ```
   Resultado: o veredicto ERRADO some (display:none), só o correto aparece ao revelar.
   (Linha sem `data-answer` continua mostrando os dois — por isso o passo 1 é obrigatório.)

## Bug C — o texto precisa reaparecer nas atividades baseadas nele
O `.ic-reading` só existe no slide de gist. Slides de atividade que dependem do texto
(True/False, "Analyse/Read again", guiding questions sobre o texto) não mostram o texto →
o aluno não tem como reler.

**Fix (markup + JS + CSS):** em CADA slide de atividade que se apoia no texto, inserir um
botão "Read the text again" que abre/fecha uma cópia ROLÁVEL do mesmo texto da aula.
1. JS (uma vez, perto de `icRevealTf`):
   ```js
   function icToggleText(btn){ var p=btn.nextElementSibling; p.classList.toggle('ic-open'); btn.textContent = p.classList.contains('ic-open') ? 'Hide the text' : 'Read the text again'; }
   ```
2. CSS (no `<style>`):
   ```css
   .ic-textbtn{display:inline-flex;align-items:center;gap:.4rem;font:600 .82rem/1 'Inter',sans-serif;color:#003080;background:var(--bg-card);border:1.5px solid var(--border);border-radius:9px;padding:.5rem .9rem;cursor:pointer;margin:0 auto .8rem;transition:border-color .2s}
   .ic-textbtn:hover{border-color:var(--accent)}
   .ic-reading.ic-collapsed{display:none}
   .ic-reading.ic-collapsed.ic-open{display:block}
   ```
3. Markup, no topo do `.slide-inner` da atividade (antes do card da atividade):
   ```html
   <button class="ic-textbtn" onclick="icToggleText(this)">Read the text again</button>
   <div class="ic-reading ic-collapsed">{COPIA EXATA do .ic-reading da aula — mesmo título, parágrafos e fonte}</div>
   ```
   Usar o MESMO conteúdo do `.ic-reading` da própria aula (não inventar texto novo).

## Gate
`_build/model/check_inclass_patterns.py` será estendido para reprovar:
- `.ic-tfrow` SEM `data-answer` (bug B), e
- `.ic-reading` SEM `max-height` (bug A).

## Ordem
1. Modelo `helen-mendes-aula3.html` primeiro (referência viva).
2. Frota: 1 subagente por aluno aplica este SPEC às aulas dele (worktree próprio, gates, auto-merge).
