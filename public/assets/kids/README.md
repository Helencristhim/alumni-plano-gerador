# Biblioteca de imagens do Modelo Kids

Chaveada por **palavra**: `public/assets/kids/{word}.{png|jpg}`. O builder
(`inject_kids_images` em `_build/model/build_from_model.py`) troca o icone SVG do
vocab card pela imagem quando existe um arquivo com o nome da palavra. Palavra sem
arquivo **mantem o SVG** (fallback silencioso) — por isso a biblioteca precisa
crescer junto com o vocabulario dos alunos kids, senao a aula sai sem ilustracao e
nenhum gate reclama.

Reaproveitada entre TODOS os alunos kids: `brick.png` serve qualquer aula que
ensine "brick".

## Procedencia e licenca

- **Cartoons** (`.png`): [OpenMoji](https://openmoji.org) — **CC BY-SA 4.0**.
  Baixados de `cdn.jsdelivr.net/gh/hfg-gmuend/openmoji@master/color/618x618/{CODEPOINT}.png`.
- **Fotos** (`.jpg`): Unsplash.

## Regra de curadoria (aprendida na marra)

Toda imagem nova e **aberta e conferida** antes de entrar: a figura tem de dizer a
PALAVRA, nao um primo dela. Emoji funciona muito bem para **objeto concreto inteiro**
(brick, wheel, tower, bridge, battery) e falha para **parte de um corpo** (wings,
claws, tail, scales), **lugar** (cave) e **abstracao** (shift, heavy). Nesses casos:
- ou se escolhe um emoji em que a parte e o elemento SALIENTE da figura
  (wings = borboleta, claws = caranguejo, brave = leao, shift = lua da noite);
- ou a definicao em ingles do proprio card sustenta a figura
  (roof = casa com telhado vermelho; scales = peixe; shelf = pilha de livros).

Isso fica mais dificil conforme o nivel sobe: o vocabulario A1 e quase todo objeto
concreto, e o A2 ja pede partes e abstracoes.
