# Relatorio de validacao — stephanie-vicente

> Saida C do prompt controlador (04 §4). **PASSOU so aparece quando um gate
> concreto rodou e voltou zero**; camada sem trava automatica sai NAO VERIFICADO,
> com o nome de quem tem de olhar. Nao ha caminho por onde uma intencao vire
> PASSOU — o status e o codigo de saida de um processo.
>
> Gerado por `scripts/relatorio_validacao.py`. Refaca depois de cada mudanca.

| Camada | Status | Evidencia | Acao |
|---|---|---|---|
| Entrada / perfil | **PASSOU** | PERFIL-360.md: 14 dos 14 campos estruturais em tabela | nenhuma |
| Framework | **PASSOU** | GATE 11: ✅ OK — nenhum aluno real com framework experimental. \| GATE 16: GATE 16 OK — 356 arquivo(s) com contrato conferido, 3135 sem carimbo (legado, ignorado por regra) \| GATE 22: OK — espinha integra em 4 aula(s) guided-discovery (etapas declaradas, telas dentro delas, minutos fechando o contrato). | nenhuma |
| Progressao | **PASSOU** | GATE 9: === REGRA 22 (gramática) OK === \| REGRA 22: === REGRA 22 OK === | nenhuma |
| Ciclo | **PASSOU** | GATE 24: OK — 1 syllabus de ciclo: dez campos por aula, ficha de especificacao completa, mecanicas declaradas e batendo com o que a aula gastou. | nenhuma |
| Linguagem | **PASSOU** | validate_lesson (inclui idioma por nivel, REGRA 13): === TODOS PASSARAM === | nenhuma |
| Factual | **NAO VERIFICADO** | nao ha gate que confira autoria, data, trecho e estatuto das fontes (03 §6). check_media_links so cobre Complementares, que esta anatomia nao tem. | leitura humana: quem autora a aula confere fonte por fonte |
| Coerencia interna | **NAO VERIFICADO** | nao ha gate que compare a instrucao da TELA com a nota do professor e o gabarito (03 §3, item 2.10 da corretiva: a nota mandava "toque o audio" numa aula de leitura). O GATE 23 cobre a EXISTENCIA e o TOM da nota, nunca o conteudo dela contra a tela. | leitura humana, slide a slide |
| Tempo | **PASSOU** | GATE 22 (a soma dos minutos das etapas fecha percurso_min=55): OK — espinha integra em 4 aula(s) guided-discovery (etapas declaradas, telas dentro delas, minutos fechando o contrato). | nenhuma |
| Tecnica | **PASSOU** | integridade: gate vermelho por arquivo de OUTRO aluno (legado, REGRA 30) — nada deste material \| GATE 19: OK — nenhuma aula da anatomia nova sem audio. | nenhuma |
| Artefato final | **PASSOU** | residuo de outro perfil/curso/versao: nenhum | nenhuma |
| Artefato x relatorio | **PASSOU** | cada PASSOU acima e o codigo de saida de um gate que rodou agora; nenhuma linha vem de intencao declarada | nenhuma |

## Criterios de aceite (instrucao corretiva, secao 4)

| # | Criterio | Quem comprova |
|---|---|---|
| 1 | O perfil apresenta os 14 campos e nao transforma hipotese em fato | camada Entrada/perfil + leitura humana da secao de hipoteses |
| 2 | O syllabus mostra as 20 aulas e diferencia Build das 5-20 ajustaveis | GATE 24 |
| 3 | Ha uma unica ordem oficial, sem divergencia de numeracao | GATE 11 + syllabus.json |
| 4 | As quatro primeiras ensinam e produzem evidencias distribuidas | campo "evidencia_a_registrar" de cada aula (GATE 24 cobra a existencia, nao o merito) |
| 5 | Cada framework preserva funcao, operacao e produto proprios | GATE 12 + GATE 22 |
| 6 | Grammar e ESP nao sistematizam extensamente o mesmo conteudo | NAO VERIFICADO — nao ha gate; o campo "conteudo_excluido" da ficha declara a fronteira |
| 7 | A rotacao altera a acao cognitiva, nao so o widget | GATE 24 (mecanica + funcao + operacao + controle registrados por aula) |
| 8 | Tela, midia, nota, chave e acao do professor alinhadas | NAO VERIFICADO — camada Coerencia interna |
| 9 | Predictions nao antecipam as respostas do input | NAO VERIFICADO — leitura humana do slide de predicao |
| 10 | O audio principal e estavel; sintese variavel so como fallback declarado | GATE 19 + GATE 5 (MP3 real no manifest) |
| 11 | Teacher notes operacionais e sem tom enfatico | GATE 23 |
| 12 | Nao existem residuos de outro perfil, curso, quantidade de aulas ou versao | camada Artefato final |
| 13 | Os tempos somam 55 min de percurso e preservam 5 de margem | GATE 22 |

## O que continua sem trava automatica

Tres camadas do 03 §8 nao tem gate, e e assim que elas aparecem aqui:

- **Factual** — autoria, data, trecho e estatuto das fontes.
- **Coerencia interna** — a instrucao da tela contra a nota do professor e o
  gabarito. Foi o defeito 2.10 da corretiva (nota mandando "toque o audio" numa
  aula de leitura).
- **Fronteira Grammar x ESP** — a ficha declara `conteudo_excluido`, mas quem le
  se as duas aulas de fato nao sistematizam a mesma coisa e uma pessoa.

Sao candidatos a gate, nao pendencias escondidas: enquanto nao existirem,
aparecem como NAO VERIFICADO em todo relatorio.

