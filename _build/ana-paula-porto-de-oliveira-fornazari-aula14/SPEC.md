# Aula 14 — "The Way I Used To Live" (A2+, Ana Paula) — CANONICAL SPEC

Reading model (even lesson). Student: Ana Paula, médica revalidando diploma, morou pro
Estados Unidos. Level **A2+ (Essential 4)**. Reforço de passado + estrutura nova A2+.

## Grammar
`used to` for **past habits and states** (marker: `data-grammar="used to for past habits and states"`).
- Affirmative: I/she/they **used to** + base verb (used to walk, used to feel, used to think).
- Negative/question drops the d: "I did not use to worry", "Did you use to live there?", also
  "I never used to worry".
- CONTRAST with Lesson 13: `used to do` (past habit) ≠ `to be used to doing` (be comfortable with).

## The 12 vocab (matching defs in config; reveal cards + example sentences here)
| # | word | definition (EN, A2+) | example sentence (for reveal card + audio) |
|---|------|----------------------|--------------------------------------------|
| 1 | to miss | to feel sad that someone or something is not with you | I really miss my family back home. |
| 2 | nowadays | at the present time, in contrast with the past | Nowadays, I feel much more confident. |
| 3 | back then | at that time in the past | Back then, I did not speak any English. |
| 4 | to look back | to think about something in your past | When I look back, I feel proud of myself. |
| 5 | to remind | to make someone remember something | This song reminds me of my old home. |
| 6 | familiar | well known to you and easy to recognize | The streets are familiar to me now. |
| 7 | fond | having warm, gentle feelings about someone or something | I have fond memories of that little town. |
| 8 | nostalgic | feeling happy and a little sad when you remember the past | Old photos always make me nostalgic. |
| 9 | to realize | to suddenly understand or notice something | I realized that I could belong to two places. |
| 10 | to adjust | to change a little so you feel comfortable in a new situation | It took me months to adjust to the new city. |
| 11 | lifestyle | the way a person lives from day to day | My lifestyle is much busier nowadays. |
| 12 | eventually | in the end, after a long time | At first it was hard, but eventually it felt like home. |

NONE of these 12 were taught in Lessons 1-13 (REGRA 22 clear). Words like homesick, traffic,
bakery, routine, belong may APPEAR in prose (review) but are NOT new vocab cards here.

## Reading text (already in config `inclass_blocks.reading`) — 3 paragraphs, title "The Way I Used To Live".

## Dialogue (In Conversation phase) — Ana Paula (ellen) + Dave (arthur), a friend. 8-9 lines,
alternating, first line ellen. Theme: Ana Paula tells Dave how her life used to be and how it
changed; Dave shares his own "used to". Vocabulary of the lesson in bold accent. Natural, real
speech (REGRA 27.D). Comprehension slide AFTER dialogue tests DAVE (the other person), per
REGRA 27.F — e.g. "Where did Dave use to live?", "What does Dave miss?", "How does Dave feel now?"
Task slide BEFORE dialogue with the SAME questions is emitted by the builder (do not hand-write it).

Suggested dialogue (rewrite naturally, keep used to + lesson vocab):
1. Ana Paula: You know, this street reminds me of my old neighborhood back home.
2. Dave: Oh yeah? What was it like back then?
3. Ana Paula: Very quiet. I used to walk to a little bakery every morning. I really miss it.
4. Dave: I know that feeling. I used to live in a small town too, before I moved here.
5. Ana Paula: Really? Was it hard to adjust?
6. Dave: At first, yes. I used to feel lost all the time. But eventually, this city became home.
7. Ana Paula: That is exactly it. Nowadays my lifestyle is so different, but I have fond memories of both places.
8. Dave: Same here. Sometimes I look back and feel nostalgic, but I would not change a thing.

Comprehension (about Dave): 
- Where did Dave use to live? (In a small town.)
- How did Dave use to feel at first? (Lost / it was hard to adjust.)
- How does Dave feel about the city now? (It became home; he would not change a thing.)

## 2 Listenings — already in config (arthur + ellen). Questions VISIBLE before play (REGRA 2.1),
data-teacher tells teacher to read questions WITH student BEFORE playing. Suggested comprehension:
- L1 (arthur): Where did he use to live? / How did he feel when he moved? / How does he feel nowadays?
- L2 (ellen, Sarah voicemail): What did Sarah find? / What did they use to do in college? / What does Sarah miss now?

## 3 Role-plays (guided → semi-free → free) in "Your Turn" phase (config `practice` covers the
scenario block; the 3 role-play situation cards are narrative slides). Keywords must be produzível
(REGRA 27.G): use concrete values, not "age"/"hobby".
- Guided: "Your old routine" — keywords: used to, every morning, back then.
- Semi-free: "Then and now" — keywords: nowadays, lifestyle, eventually, adjust.
- Free: "Looking back" — keywords: miss, fond memories, nostalgic, realize.

## Survival Card (5 phrases, A2+ — NO .sp-pt). data-speak on the audio button (REGRA 7.1).
1. Back then, my life used to be very different.
2. I used to feel homesick, but eventually I adjusted.
3. Nowadays, my lifestyle is much busier.
4. This song reminds me of home and makes me nostalgic.
5. When I look back, I have fond memories of both places.

## Wrap-up "What I Learned" checklist (5 items, EN):
1. I can talk about past habits with "used to".
2. I can use the negative: "I did not use to ...".
3. I can compare back then and nowadays.
4. I can use: miss, remind, fond, nostalgic, look back.
5. I can describe how I adjusted to a new lifestyle.

## LANGUAGE / GATES (non-negotiable)
- REGRA 13: ZERO Portuguese on student screen (slides text, preclass, complementares, incl.
  data-hint / <option> / placeholder). PT ONLY in data-teacher (icon T) and Planejamento.
- REGRA 7.1: audio text in `data-speak="..."`, NEVER inside a JS string. Handles apostrophes.
- REGRA 27.E: reveal cards toggle (classList.toggle).
- data-teacher on EVERY slide, in PT, complete (timing, how-to, CCQs, obstacle alerts).
- Every slide `data-lesson="14"`.
- Reading/dialogue/listening comprehension questions never born hidden (no display:none on
  .comp-questions / .ic-* answers live in DOM only via reveal handlers).
