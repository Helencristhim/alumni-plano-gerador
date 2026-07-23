---
description: Trava o escopo de trabalho em KIDS + TEENS. Proíbe qualquer alteração no modelo/materiais ADULTO (helen-mendes e alunos adultos). Argumento opcional = tarefa a executar já nesse modo.
---

# /kids-teens — modo de construção KIDS + TEENS (adulto travado)

Ative o modo de escopo **kids/teens** e trabalhe só nele.

1. **Ligue a trava dura**: escreva `.claude/scope.lock` com o conteúdo exato `kids-teens`
   (uma linha, nada mais) usando Write. A partir daí o hook `PreToolUse`
   (`scripts/scope-guard.sh`) **bloqueia automaticamente** (exit 2) qualquer Edit/Write em
   material adulto — você não precisa lembrar, a trava é dura.
   > Se o hook ainda não estiver carregado nesta sessão (settings.json é lido no início),
   > a trava vale plenamente a partir da próxima sessão; nesta, **respeite o escopo por conta**.

2. **Pode tocar**: `bento*`, `theo*`, `word-arena`, `kids*`, `teens*`, `assets/kids`,
   `audio/bento`, `kids-theme`, catálogo, perfis kids/teens, e infra compartilhada
   (builder/gates/css/lib) **desde que a mudança seja model-gated pra kids/teens**.

3. **NÃO pode** (bloqueado): `helen-mendes` (modelo adulto) nem qualquer material de aluno
   adulto (`public/professor|aluno|audio/...` que não seja kids/teens). NUNCA regerar aula
   adulta. NUNCA propor "serve os três modelos". Mudança no shell/builder compartilhado só
   vale se for model-gated (`if cfg model in kids/teens`), nunca no caminho default do adulto.

4. **Confirme** ao usuário: "Escopo travado em KIDS+TEENS — adulto bloqueado." e diga como
   sair (`/adulto` troca de modo · `/escopo-livre` remove a trava).

Vale junto com TODAS as regras do `CLAUDE.md`. Se veio uma tarefa no argumento, execute-a já
sob esse escopo.
