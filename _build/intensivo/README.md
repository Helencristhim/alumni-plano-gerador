# Intensivo — molde Private Black

Material de intensivo (poucas aulas, um evento comunicativo só) no molde **Private Black
Adults**. Hoje serve a Rita Rodrigues: seis aulas ESP entre 20 e 28 de agosto para a
reunião com o presidente da Carestream em 31 de agosto.

## O que roda

```
python3 _build/intensivo/make_shell.py    # molde -> shell.html   (só quando o molde muda)
python3 _build/intensivo/build.py         # shell + conteúdo -> os DOIS arquivos publicados
```

`build.py` escreve:

```
public/intensivo/rita-rodrigues.html        visão do professor
public/intensivo/rita-rodrigues-aluna.html  visão da aluna
```

## Uma fonte, dois arquivos

O molde nasceu como UM arquivo com botão de troca de visão. Aqui são dois links, e a regra
é mais forte que esconder: **o que a aluna não pode ver não existe no arquivo dela**, nem a
um Ctrl+U de distância. A divisão é mecânica, feita por `separa()`:

| Sai do arquivo do professor | Sai do arquivo da aluna |
|---|---|
| tudo com `data-view="aluno"` (aba Feedback) | tudo com `data-view="professor"` (Planejamento, In-class, o deck inteiro, os painéis do cartão) |

E não só o markup: os rótulos que o **motor** monta em string (`'<span data-view="professor">
Aula '+n+'</span>'`) também são reescritos por papel, e no arquivo da aluna o construtor do
gabarito (`akBuild`) sai inteiro — ele DERIVA a resposta do próprio exercício, então esvaziar
`PC_NOTAS` não bastaria.

## O feedback atravessa por Supabase

No molde original o professor escreve e a aluna lê o mesmo `localStorage`. Com dois arquivos
em dois navegadores isso não acontece sozinho: `public/lib/intensivo-sync.js` leva o espaço
COMPARTILHADO do registro (`sfb_l{n}_worked` / `_develop` e `af_l{n}_status`) por
`student_activity`, `view_type='intensivo-compartilhado'`. O professor escreve, a aluna lê.
Ela nunca escreve nesse canal.

## Onde mora cada coisa

| Arquivo | O que é |
|---|---|
| `molde-black-private.reference.html` | o molde, como veio do artefato. Não se edita: é a referência. |
| `make_shell.py` | tira o conteúdo do molde e deixa os hosts + marcadores `<!--SLOT:X-->` |
| `shell.html` | resultado do acima: CSS + motor, sem conteúdo nenhum |
| `content_aulas.py` | as 6 aulas: telas do in-class, fecho, recapitulação e confiança |
| `content_pre.py` | os 6 pre-class (5 atividades cada) + o gabarito do professor |
| `content_post.py` | os 6 post-class |
| `content_perfil.py` | perfil, planejamento, registro do ciclo e o cartão de preparação |
| `notas_professor.json` | as notas do Teacher's Guide por tela |
| `render.py` | os componentes do molde em funções |
| `build.py` | monta, separa por papel e escreve os dois arquivos |

## O que o molde trazia cravado e foi destravado

- **quatro aulas** em 14 laços `for(n=1;n<=4;n++)` → `NAULAS`, tirado de `LESSONS`;
- **o fecho da aula 1** era função própria (`recapBuild`, chaves `rc0`) e as outras três eram
  `closeBuild(n,RECAPn,CONFn)` → um `FECHO` só, para qualquer número de aulas;
- **`ld().aluna`** em dois pontos do pre-class (o registro virou `aluno` na P19): o boot
  morria na primeira linha do `preInit` e nada depois dele rodava;
- **`papelDe()`** não conhecia `post_`: o que a aluna escrevia no post-class caía no espaço
  do professor, que `load()` não devolve para ela — ela escrevia e não via mais.
