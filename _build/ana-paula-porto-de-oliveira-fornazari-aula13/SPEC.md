# Lesson 13 — "How Long? — Settling into a New Life" (Ana Paula, A2+ / Essential 4)

CANONICAL SPEC. All authored files (slides.html, preclass.html, complementary.html) must
use EXACTLY this vocab, grammar, dialogue and examples so the four tabs stay coherent (REGRA 29).

- Student: Ana Paula, female, médica revalidando diploma, living in Florida, USA.
- Level: **A2+ (Essential 4)** — ZERO Portuguese on the student screen (REGRA 13). Only
  `data-teacher` (icon T) is in Portuguese (professor instructions).
- Grammar: **present perfect + for / since** (duration — actions that started in the past and
  continue now). This is NEW here; aula 12 was present perfect ever/never (experiences).
- Theme: how long Ana Paula has done things **since she moved to Florida** — settling in,
  adapting, feeling at home. Personal / everyday. **No business vocabulary.**
- Callback to aula 12: last time = WHAT you have done (ever/never). Today = HOW LONG you have
  done it (for/since).
- Accent color: `--accent:#b45309` (amber). Palette already in the shell.

## The 12 vocab words (English def + example — NEVER Portuguese on screen)
1. To move — to go and live in a new place. "I moved to Florida last year."
2. To settle in — to start to feel at home in a new place. "It took me a month to settle in."
3. To get used to — to slowly become comfortable with something new. "I am getting used to the hot weather."
4. So far — up until now. "So far, I love my new city."
5. Ever since — continuously from a moment in the past until now. "I have felt happy ever since I arrived."
6. Recently — a short time ago. "I found a great coffee shop recently."
7. Lately — in the recent past, these days. "I have been very busy lately."
8. Homesick — sad because you are far from home. "Sometimes I feel homesick for my family."
9. To adapt — to change so you fit a new situation. "I have adapted to life in a new country."
10. A while — a period of time. "I have lived here for a while now."
11. To belong — to feel you are in the right place. "For the first time, I feel like I belong here."
12. Gradually — slowly, over a period of time. "Gradually, this city has become home."

Vocab icon gradients (reuse per-word unique gradients like the reference; amber/teal/blue/green mix).

## Grammar — for / since (present perfect for duration)
DISCOVERY examples (all present perfect, highlight the for/since part in accent):
- "I have lived in Florida **for** three months."
- "I have lived here **since** March."
- "She has worked at the clinic **for** two years."
- "We have known each other **since** we were kids."
Question form: "**How long have** you lived here?"
Rule table (reveal after):
- Present perfect = have/has + past participle. Use it when something STARTED in the past and
  CONTINUES now.
- **for** + a PERIOD of time (for three months, for a while, for two years).
- **since** + a POINT in the past (since March, since 2024, since I moved).
- Question: How long have you + past participle...?

Common Mistake slide (slide-light, `.mistake-wrong` / `.mistake-right`, text DIRECT in the div):
- WRONG "I am living here since 2024." / RIGHT "I have lived here since 2024." (present perfect, not present continuous)
- WRONG "I live here for two years." / RIGHT "I have lived here for two years."
- WRONG "I have lived here since three months." / RIGHT "I have lived here for three months." (for = period, since = point)
Explanation `<p>` below: For duration up to now, use the present perfect. Use **for** with a
period of time and **since** with a point in the past.

## Dialogue (line-by-line, dark slide). Two speakers, TWO voices:
Ana Paula = `data-voice="ellen"` (avatar class `anapaula`), Dave (male neighbor) = `data-voice="arthur"` (avatar class `ben` reused, letter "D").
Highlight lesson vocab with `<span class="vocab-highlight">`.
1. Dave (arthur): "Hi! You must be my new neighbor. Have you lived in this building for a long time?"
2. Ana Paula (ellen): "Hi! Nice to meet you. Actually, I moved here quite recently. I have lived here for about three months."
3. Dave (arthur): "Oh, welcome! And how do you like it so far? It takes a while to settle in."
4. Ana Paula (ellen): "So far, I love it. I am still getting used to the hot weather, but I have adapted little by little."
5. Dave (arthur): "That is great. I have lived here since 2015, and honestly, it still feels like home. Do you ever feel homesick?"
6. Ana Paula (ellen): "Sometimes, especially for my family. But ever since I joined the local community, I have started to feel like I belong here."

Dialogue Comprehension slide (3 questions, ABOUT DAVE — the other person, REGRA 27F; click-to-reveal `.comp-q`/`.q-answer`):
1. How long has Dave lived in the building? → Since 2015.
2. Does the building still feel like home to Dave? → Yes, it still feels like home to him.
3. What does Dave say about settling in? → It takes a while to settle in.

(The BUILDER auto-injects the "Before you listen/read" task slide before the dialogue — do NOT
author it. Just author the dialogue slide + the comprehension slide.)

## Listening 1 (dark, full player, `a13_listening1.mp3`, arthur). Questions VISIBLE before play (REGRA 2.1).
Transcript (already in config.json — do NOT print it on screen):
"I moved to this city about five years ago... now I truly feel like I belong."
Comprehension questions (visible, click-to-reveal):
1. How long has the speaker lived in the same apartment? → Since his second year in the city.
2. How did he feel in the first few months? → A little homesick.
3. What helped him make good friends? → Joining a local running club.

## Listening 2 (dark, full player, `a13_listening2.mp3`, ellen). A voicemail from a friend, Sofia.
Comprehension questions (visible, click-to-reveal):
1. How did Sofia feel in her first month abroad? → Very homesick.
2. What helped life feel normal again for Sofia? → Finding a daily routine.
3. How many countries has Sofia lived in so far? → Three.

## Artifact (CSS card, personalized — a personal timeline). Title "Ana Paula — Since I Arrived in Florida"
Rows:
- Arrived in Florida: March 2025
- In this apartment: since April 2025
- English classes: for 10 months
- Volunteering at the clinic: since June
Comprehension (`.comp-q`):
1. How long has Ana Paula been in her apartment? → Since April 2025.
2. How long has she studied English? → For 10 months.
3. When did she start volunteering at the clinic? → In June (she has volunteered since June).

## Quick Fire (one question per screen, English, Show Answer → Next):
1. How long have you lived in your city? → "I have lived here for / since ..."
2. How long have you studied English? → "I have studied English for ..."
3. What is one thing you are still getting used to? → "I am still getting used to ..."
4. Since when have you felt at home in Florida? → "I have felt at home ever since ..."
5. How long have you known your best friend? → "I have known ... for / since ..."

## Spot the Error (click reveals correction):
1. WRONG "I live in Florida since March." → RIGHT "I have lived in Florida since March."
2. WRONG "I am here for three months." → RIGHT "I have been here for three months."
3. WRONG "I have studied English since ten months." → RIGHT "I have studied English for ten months."
4. WRONG "How long you have lived here?" → RIGHT "How long have you lived here?"

## Role-plays (3 levels, gradient + SVG cards, keyword chips):
- Guided: "Tell me three things about your life in Florida. Use 'I have ... for ...' or 'I have ... since ...'."
- Semi-free: keyword chips — `for three months`, `since March`, `gradually`, `so far`. Describe how you have settled in.
- Free: "A new neighbor asks how long you have lived here and how you like it. Have the whole conversation." (no keywords)

## Wrap-up
Survival Card (5 phrases, `data-speak` + Listen, REGRA 7.1 — text in attribute):
1. "I have lived in Florida for three months."
2. "I have felt at home ever since I arrived."
3. "I am still getting used to the weather."
4. "So far, I love my new life here."
5. "How long have you lived here?"
What I Learned checklist (5 checkboxes): the 12 words; for + period / since + point; present perfect
for duration; talking about settling in; asking How long...?
Closing: "Lesson 13 — Complete" + preview of lesson 14 (Food, Culture & Eating Out).

## Pre-class (preclass.html) — 5 mandatory stages (REGRA 4), A2+ (English only):
- Stage 1.1 Vocab cards (the 12 words, English def, audio via data-speak).
- Stage 1.2 Matching dropdown (word ↔ English definition, SHUFFLED — REGRA 24).
- Stage 1.3 "Grammar in Context" — short narrative using for/since (bold the target) + selectQuiz comprehension.
- Stage 1.4 "Grammar Tip" — for/since table, affirmative/negative/question (English only, A2+).
- Stage 1.5 Fill-in-the-blank (checkBlank) with English "Hint: ..." + data-phrase audio.
- Stage 2 Practice: ordering (checkOrder) using the `[order-l13]` audio narrative (see config extra_audio) OR word-cloud fill.
- Stage 3 Pronunciation: speech-cards (speakPhrase/startRecording) — NO .speech-translation (A2+).
- Stage 4 Situational quiz (selectQuiz) — Florida / everyday-life contexts.
- Stage 5 Free production: think-card + startFreeRecording.
- Survival card at the end (same 5 phrases as above, NO .sp-pt).

## Complementary (complementary.html) — 3 media (series + podcast + youtube), A2+ English, REAL exact links.
Theme: settling into life in a new country / everyday American life. (Author handles links.)
