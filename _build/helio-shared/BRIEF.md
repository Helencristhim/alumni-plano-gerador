# Brief compartilhado — geração de aula ES (Helio Santana)

Você vai criar os 4 arquivos de conteúdo de UMA aula e rodar o builder. NÃO gere áudio, NÃO toque nos hubs. Apenas crie os arquivos e rode `build_from_model.py`.

## Aluno
- slug: `helio-santana` — A2 Business Spanish, exec antifraude/fintech (HS Private), São Paulo. Voz masc = arthur. Idade 50 (tom respeitoso/prático, ritmo claro).
- Personagens fixos: **Helio = arthur**, **Carolina = ellen** (Carolina Vega, cliente fintech de Ciudad de México, conhecida na aula 1 num almuerzo).
- Paleta: accent #047857 / #0E9F6E.

## REFERÊNCIA OBRIGATÓRIA (espelhe a ESTRUTURA exatamente, só troque o conteúdo)
Diretório de referência (aula ES já montada, 27 slides, passou nos gates):
`/home/dan/dev/work/better/alumni-plano-gerador/wt-fabiana-17-20/_build/daniel-bastos-aula2/`
- `slides.html` — 27 slides, 7 capítulos. Copie a ESTRUTURA slide a slide (mesmas classes, mesmos componentes, mesmos data-slide/data-phase, mesmos botões de áudio, mesmo player de listening com mpToggle/mpSeek/mpSkip/mpSpeed, mesmo diálogo line-by-line com data-voice, mesma autoavaliação/badge). Troque só os textos para o tema desta aula.
- `preclass.html` — accordion (lesson-card) com as 5 etapas (1.1 vocab, 1.2 matching embaralhado, 1.3 Gramática en Contexto + quiz, 1.4 Consejo de Gramática (tabela), 1.5 fill-in-blank) + Etapa 2 Ordenar (com áudio [order-lN]) + Etapa 3 Pronunciación (4 speech-cards) + Etapa 4 Cuestionario (3 quiz) + Etapa 5 Producción Libre (think-card) + Tarjeta de Supervivencia (5 frases). Copie a estrutura, troque conteúdo.
- `complementary.html` — 3 media-cards (Serie / Pódcast / YouTube) em espanhol. Mesmos SVG, `data-media="lN-serie/-podcast/-youtube"`.
- `config.json` — veja regras abaixo.

## config.json
Base = copie `/home/dan/dev/work/better/wt-helio/_build/helio-santana-aula1/config.json`.
MANTENHA idênticos: palette, header, stamps, characters, voices, lang, total_aulas (50), e TODO o bloco ui_strings — EXCETO troque a chave `"LESSON 1": "CLASE 1"` por `"LESSON {N}": "CLASE {N}"` (com o N desta aula).
MUDE: `"hub": "new"` → `"hub": "snippets"`.
SUBSTITUA todo o objeto `"lesson"` pelo da sua aula (n, menu_num com 2 dígitos, menu_title, menu_desc terminando em "-- 27 slides", subtitle, title_tag, phases [7 labels ES], listenings [2, com file aN_listening1/2.mp3 e voice], extra_audio [1, key "[order-lN]", file pc_order_lN.mp3, voice arthur]).

## REGRAS DE ESPANHOL (CRÍTICAS — gate bloqueia)
- TELA IN CLASS (slides, vocab, diálogo, listening, exercícios visíveis) = 100% ESPANHOL. Zero português na tela.
- Apoio em PORTUGUÊS só em: atributo `data-teacher` (instruções ao professor) e no Pre-class (defs/traduções/hints/pista, ~80% bilíngue p/ A2). O `data-teacher` é em português.
- Acentos do espanhol (á é í ó ú ñ ¿ ¡) são CORRETOS — use à vontade. PROIBIDO na tela IN CLASS: grafias com ã/õ/ç (português). Ex.: escreva "Soy de Brasil" / "de aquí", NUNCA "São Paulo" na tela IN CLASS (só no header/config). O validador "PT na tela" usa a regra [ãõç] sem whitelist.
- Diálogo: TODA `dialogue-line` tem `data-voice`. Helio/masculino=arthur, Carolina/feminino=ellen. Vozes distintas no mesmo diálogo (só 2 personagens — nunca um 3º falante novo).
- Listening = SEMPRE monólogo (1 voz). Use os textos fornecidos.

## Dosagem A2
8 palavras novas (exatamente as fornecidas). Frases curtas (5-8 palavras). Pre-class com tradução/def visível. Gramática progressiva conforme fornecido.

## Saída e build
Crie em `/home/dan/dev/work/better/wt-helio/_build/helio-santana-aula{N}/`: config.json, slides.html, preclass.html, complementary.html.
Rode: `cd /home/dan/dev/work/better/wt-helio && python3 _build/model/build_from_model.py _build/helio-santana-aula{N}/config.json`
Confirme: build sem erro (assert) + 27 slides + `public/professor/helio-santana-aula{N}.html` e `public/aluno/...` gerados + `hub_snippets.html` gerado.
Se o builder falhar com assert, AJUSTE seu conteúdo (não o builder) e rode de novo. Reporte: nº de slides, status do build, qualquer assert.
