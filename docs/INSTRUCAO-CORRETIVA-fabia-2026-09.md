# Instrução corretiva — Fábia Aparecida Alves Calusa — 09/2026

> Normativo por aluno. Vale para `fabia-aparecida-alves-calusa` da **aula 6 em diante**.
> As aulas 1 a 5 não são tocadas: ela já as fez (REGRA 30).

## Os dois feedbacks

**21/09/2026 — sobre o enunciado.** Áudios e perguntas longos demais, pergunta de inferência,
speaking do fim sem apoio. Resolvido nos PRs **#2791** e **#2792**: listening de 30 a 80
palavras, toda pergunta com resposta literal no áudio e em ordem crescente, situation card
lido em vez de inventado, role-play livre trocado por quatro frases com esqueleto.

**24/09/2026 — sobre a arquitetura da aula.** A professora Lua, por áudio e por escrito:

> "precisa ser refeito com estrutura realmente mais simples não apenas nos exercícios, mas com
> **menos volume gramatical a cada aula** pois ela não está conseguindo acompanhar e precisa de
> muita validação pra avançar."
>
> "Menos palavras novas por aula, idealmente **4** ao invés de 8."
>
> "Aluna sente que aprende vocabulário em excesso, pula pra gramática, gaps, respostas complexas
> e acaba a aula. Próxima aula tudo novo e ela se perde **sem rever o conteúdo**."
>
> "Sugiro que a gente apresente **1 ponto gramatical por semana (primeira aula)**, sendo a
> **aula 2 uma revisão com exercícios de produção (less controlled e freer)**, dando a chance de
> usar ao menos 2 das 4 novas palavras."

A medição confirmou a queixa: nas aulas 5 a 10, **toda** aula trazia 1 ponto gramatical novo,
8 palavras novas e 6 pares de matching. Não havia uma única aula de revisão no material dela.

## O modelo de par

O material passa a andar em pares. Não é sugestão: é a forma da aula desta aluna.

| | aula que APRESENTA | aula que REVISA |
|---|---|---|
| gramática | 1 ponto novo, declarado em `lesson.grammar_point` | **nenhuma**. O campo **não existe** no config |
| palavras novas | **4** | **0**. Recicla as 4 da aula anterior |
| título | livre | contém **Review** (é assim que o gerador reconhece) |
| peso da produção | o normal | mais da metade da aula |
| formato do fim | quatro frases com esqueleto | esqueleto na primeira rodada, sem esqueleto na segunda |

### O mapa a partir da aula 6

```
aula 5   apresentou modais (já dada, não tocada)
aula 6   REVISA a 5
aula 7   APRESENTA  used to
aula 8   REVISA a 7
aula 9   APRESENTA  voz passiva
aula 10  REVISA a 9
aula 11  APRESENTA  echo questions        (ainda não construída)
aula 13  APRESENTA  comparativos          (ainda não construída)
aula 15  APRESENTA  reported speech       (ainda não construída)
```

A ordem gramatical que já estava desenhada para ela é preservada. Só passa a andar na metade da
velocidade, e o conteúdo que estava nas aulas 8, 9 e 10 é empurrado para 11, 13 e 15.

## A anatomia da aula que revisa

Sete fases, a mesma contagem de telas da aula que substitui (ver *travas*, abaixo).

| fase | o que acontece |
|---|---|
| Warm-Up | uma pergunta curta sobre a aula anterior, resposta de uma frase |
| The Words Again | as 4 palavras: reconhecer primeiro (definição → palavra), depois usar numa frase |
| The Pattern Again | a mesma estrutura, sem regra nova, com a tabela de apoio visível daí em diante |
| Controlled | completar e escolher, com o banco de opções à vista |
| Your Turn — *less controlled* | pergunta curta, resposta de UMA frase; e o cliente real dela, não o do material |
| Your Turn — *freer* | a mesma tarefa duas vezes: com esqueleto na tela, depois sem |
| Wrap | checklist de "eu consigo" **e uma tela de validação com os números da aula** |

**A validação é peça do material, não boa vontade do professor.** A Lua escreveu que a aluna
"precisa de muita validação pra avançar", então a penúltima tela traz três contadores para o
professor preencher em voz alta com ela (respostas curtas, palavras usadas sem a pista, respostas
na call sem esqueleto), e o `data-teacher` manda dizer o que saiu certo **antes** de qualquer
correção.

## As travas do repositório que este modelo encosta

Quem for gerar a aula 8 ou a 10 vai bater nestas. Todas têm saída conhecida.

**1. `check_no_regression.py` conta telas com tolerância ZERO.**
`_build/model/check_no_regression.py` compara `ex-lesson`, `stamp` e `slides`; qualquer queda de
uma unidade reprova (só `bytes` tem folga de 10%). Uma aula de revisão **não pode ter menos telas**
que a aula que substitui. Por isso a revisão mantém a contagem e usa as telas para rodadas de
produção, em vez de encurtar o arquivo. Válvula, se algum dia for mesmo necessário encurtar:
declarar a transição em `_build/model/shrink_allowlist.json`, nos dois arquivos.

**2. `validate_lesson.py` exige `vocab-card-pc >= 6` no Pre-class do hub.**
Cortar o Pre-class para 4 palavras reprova com `vocab-card-pc (4/6)`. A saída é a que a Lua queria
de qualquer jeito: o Pre-class traz **6 cards**, sendo 4 palavras novas e 2 recicladas da aula
anterior. Na aula de revisão, os 6 são todos reciclados.

**3. `check_vocab_progression.py` reprova palavra reapresentada (REGRA 22).**
Ele lê `vocab-card-word`, que só existe no Pre-class do hub. Toda palavra reciclada entra em
`_build/model/vocab_allow_repeat.json` sob o slug dela. O arquivo é compartilhado, mas indexado por
slug: não toca o material de ninguém.

**4. O build ABORTA se a revisão declarar `grammar_point`.**
`inject_grammar_marker` (em `build_from_model.py`) morre quando há `grammar_point` no config e
nenhum slide de descoberta nos slides. Numa aula de revisão, **apague o campo**. É o próprio erro
que diz isso.

**5. O áudio muda de prefixo quando o conteúdo muda de aula.**
O nome do MP3 carrega `a{N}_`. Mover o conteúdo da aula 6 para a 7 gera arquivos novos e deixa os
antigos órfãos no disco. Nenhum gate reclama de órfão, e eles ficam.

## O que fica valendo

- Da aula 11 em diante, **gerar em pares**: ímpar apresenta, par revisa.
- **Quatro palavras novas por par**, não por aula, e nunca oito.
- **Nada de gramática nova na aula par.** Se aparecer, o par deixou de existir.
- A tela de validação do Wrap é obrigatória na aula que revisa.
