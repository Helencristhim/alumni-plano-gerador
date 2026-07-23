---
description: Trava o escopo de trabalho no ADULTO (helen-mendes + alunos adultos). Proíbe qualquer alteração em KIDS/TEENS. Argumento opcional = tarefa a executar já nesse modo.
---

# /adulto — modo ADULTO (kids/teens travado)

Ative o modo de escopo **adulto** e trabalhe só nele.

1. **Ligue a trava dura**: escreva `.claude/scope.lock` com o conteúdo exato `adulto`
   (uma linha, nada mais) usando Write. O hook `PreToolUse` (`scripts/scope-guard.sh`)
   passa a **bloquear** (exit 2) qualquer Edit/Write em arquivo kids/teens.
   > Se o hook ainda não estiver carregado nesta sessão, respeite o escopo por conta até a
   > próxima sessão.

2. **Pode tocar**: material e modelo **adulto** (`helen-mendes*`, alunos adultos) e infra
   compartilhada. Lembre que material ATIVO/legado é intocável sem OK explícito do Dan
   (REGRA 12/30/31) — a trava não afrouxa isso.

3. **NÃO pode** (bloqueado): qualquer arquivo kids/teens — `bento*`, `theo*`, `word-arena`,
   `kids*`, `teens*`, `assets/kids`, `audio/bento`, `kids-theme`, perfis/catálogo na parte
   kids/teens.

4. **Confirme** ao usuário: "Escopo travado em ADULTO — kids/teens bloqueado." e diga como
   sair (`/kids-teens` troca de modo · `/escopo-livre` remove a trava).

Vale junto com TODAS as regras do `CLAUDE.md`.
