# A transição do molde antigo para o consultivo

> Para quem for implantar. O que está aqui é o **como**; o **quando**, aluno a aluno, é
> decisão do Dan.

## O fato que governa tudo

Os alunos **já têm o link** — `/aluno/{slug}.html` — e **ainda têm aula no material
antigo**. Esse caminho não muda, nunca, em nenhuma fase. Tudo abaixo existe para que isso
continue verdadeiro enquanto o molde novo entra.

## Fase 1 — piloto (dois materiais vivos ao mesmo tempo)

No `config.json` do aluno:

```json
"fase": "piloto"
```

O builder escreve em `{slug}-c{N}.html`, nos mesmos diretórios, **sem encostar** no material
atual:

```
/professor/{slug}.html      antigo — é onde a aula acontece
/aluno/{slug}.html          antigo — é o link que ele já tem
/professor/{slug}-c1.html   novo — piloto
/aluno/{slug}-c1.html       novo — piloto
```

Mesmos diretórios, não um `/novo/` à parte: o GATE 36 e toda a convenção de isolamento se
apoiam em `/professor/` vs `/aluno/`.

Para o painel mostrar os dois, declare em `public/materiais-extra.json` (chave = `perfis.id`):

```json
"{perfis.id}": [{ "rotulo": "Molde novo — ciclo 1 (piloto)",
                  "professor": "/professor/{slug}-c1.html",
                  "aluno": "/aluno/{slug}-c1.html" }]
```

O painel confere cada caminho por HTTP antes de virar botão — caminho que não responde não
aparece, então declarar cedo não quebra o card de ninguém.

## Fase 2 — cutover (por decisão, aluno a aluno)

No mesmo PR:

1. copie o hub antigo para `{slug}-anterior.html` (professor e aluno) — **arquivo novo**,
   nada apagado, nada renomeado, o guard do `[remove-ok]` não entra;
2. tire `"fase"` do config e rode o builder: ele escreve em `{slug}.html`, a URL de sempre;
3. troque a declaração em `materiais-extra.json`: sai o piloto, entra
   `"rotulo": "Aulas anteriores"` apontando para `-anterior`;
4. **`[cutover]` na mensagem do commit** — sem isso o GATE 47 reprova.

O aluno nunca soube do `-c1`. Para ele o link é o mesmo desde o começo, e passa a abrir o
material novo. O progresso feito no piloto **sobrevive**: a chave é
`pv_{slug}-c{N}_v1`, a mesma nos dois.

## Por que o sufixo nunca fica na URL viva

`daniela-feitoza` e `percival-jr` trocaram de molde pelo caminho inverso: o material **novo**
ganhou `-v2` e o antigo virou redirect. Os dois carregam o sufixo até hoje, mais dois
redirects cada no `vercel.json` — e a próxima troca seria `-v3`.

Aqui o sufixo marca só o que é **provisório** (`-c1`, durante o piloto) ou o que já
**congelou** (`-anterior`, depois do cutover). O padrão permanente fica sendo o mais simples
possível: **`{slug}.html` é o material atual**, sem sufixo e sem lista de redirects crescendo
a duas linhas por aluno.

E repete: quando o ciclo 2 começar, o ciclo 1 vira `{slug}-c1.html` e `{slug}.html` continua
sendo "agora".

## As travas

| Gate | O que impede |
|---|---|
| **47** `check_cutover_explicito.py` | arquivo que era imersivo virar consultivo sem `[cutover]` no commit — o acidente de rodar o builder sem `fase` |
| **48** `check_link_namespace.py` | o botão entre materiais virar porta: `/aluno/` não aponta para `/professor/` |
| **36** `check_isolamento_aluno.py` | o arquivo do aluno conter o que é do professor (bytes e elevação de papel) |

## O que ainda falta antes do primeiro aluno real

O progresso do consultivo vive só em `localStorage`. A chave já tem o aluno dentro
(`pv_{slug}-c{N}_v1`), então dois materiais não se sobrescrevem mais — mas continua **sem
Supabase**: não atravessa aparelho, some se a aluna limpar o navegador, e o painel não conta.
O imersivo faz isso por `activity-sync.js` (`student_activity` + Storage `recordings`).

Dá para pilotar assim — o aluno não perde nada que tinha, porque o material é novo. **Não dá
para fazer cutover assim.**
