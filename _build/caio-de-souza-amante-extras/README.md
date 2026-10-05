# Caio de Souza Amante: aba "Gramática em português"

**Regra permanente (pedido da Helen, 05/10/2026): TODA aula nova do Caio entra com o seu
bloco nesta aba, no mesmo PR da aula.** Não é opcional e não espera pedido.

## Por quê

Feedback do Caio (05/10/2026): o Stage 1.3 *Grammar in Context* do pre-class é um texto corrido
em inglês e ele se perde. Pediu explicação gramatical em português, com exemplo e com o próprio
texto em português. A REGRA 13 (GATE 1) proíbe português dentro do bloco `ex-lesson-N` em A2+,
então a explicação vive numa aba suplementar (`tab-gramatica`), fora do pre-class, como a
Legal English da Adriana. O pre-class continua igual.

## Como acrescentar a aula N

1. Escrever o bloco `<div class="exercise-section" id="gr-aulaN">` … `<!-- /AULA N -->` em
   `gramatica.html`, logo antes de `</div><!-- /tab-gramatica -->`, copiando a estrutura da aula 10:
   1. O que é · 2. Quando usar · 3. A regra em uma frase
   2. Tabela com a forma, exemplo do mundo dele (Dataside, comprador, due diligence) e tradução
   3. Casos especiais da estrutura e "Onde o português atrapalha"
   4. "Em vez de / Diga" (cinza x normal, **nunca** vermelho x verde: Common Mistake é proibido)
   5. **O texto do Pre-class, trecho a trecho**: o Grammar in Context da aula, em partes, cada
      uma com "EM PORTUGUÊS" logo abaixo
   6. Teste rápido com `<details>` (sem JS; respostas tiradas do fill-in da própria aula)
2. Só a gramática da aula N e das anteriores (teto de nível). Sem travessão no português.
3. Aplicar nos DOIS hubs:
   ```
   python3 _build/model/insert_hub_extras.py --replace --hub public/professor/caio-de-souza-amante.html \
     --aba "gramatica:_build/caio-de-souza-amante-extras/gramatica.html:Gramática em português"
   python3 _build/model/insert_hub_extras.py --replace --hub public/aluno/caio-de-souza-amante.html \
     --aba "gramatica:_build/caio-de-souza-amante-extras/gramatica.html:Gramática em português"
   ```
   Atenção: o `insert_hub` de uma aula nova pode mexer no hub. Rodar o `--replace` DEPOIS dele.
4. `git add --sparse` neste diretório (fica fora do sparse-checkout padrão).

Histórico: aula 9 (PR #3060, texto em PT no #3063), aula 10.
