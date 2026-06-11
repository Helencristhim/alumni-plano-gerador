# Dialeto do hub da Andreia (inline-monolítico puro, SEM standalones)

- Aula 5 = "Talking About Experience — Have You Ever...?" (present perfect/experiência, B1,
  cirurgia robótica/Einstein). Currículo linha 5. Q&A experiência profissional; homework: 5 frases pp.
- Slides novos: data-slide 113-140, data-lesson="5"; classes: slide-image / slide-light / slide-dark
  (slide-image usa background-image:url(...) direto, sem gradiente).
- lessonRanges (formato com espaços): `4: { start: 85, end: 112 } }` → vira `..., 5: { start: 113, end: 140 } }`
- Menu IN CLASS: card com onclick="enterSlideMode(113);" (formato dos outros, número 05).
- Vocab: class="vocab-card" onclick="revealVocab(this)" com card-icon (gradiente+card-hint) +
  card-body (card-word/card-def/card-example/card-audio). Grids da aula 5: vocabGrid9/vocabCount9
  e vocabGrid10/vocabCount10 (7 e 8 já usados pela aula 4). revealVocab é GLOBAL e one-way.
- Diálogo: id="dialogueBox5", linhas .dialogue-line data-line data-voice, avatar "dr"/"student",
  bolhas dr-bubble/student-bubble, vocab-highlight nos termos. 8 FALAS (threshold 8).
  JS: var dialogueLine5 = 1; function nextDialogueLine5() {...querySelector("#dialogueBox5 ...")...
  >= 8 → nextLineBtn5 disable} (copiar shape da nextDialogueLine4).
- Listening: listening-player completo (seekbar/time/controls/speed) ids lp-listen9 e lp-listen10,
  data-src="/audio/andreia-heins/a5_listening_*.mp3" (copiar bloco de _referencia, trocar id).
- Checklist: check-grid id="checkGrid5" + 8 check-item toggleCheck(this) (global).
- Stamps: stamp5 depois do stamp4; totalLessons 4→5; audioMap merge (prefixo a5_).
- Pre-class: accordion ex-lesson-5 antes de </div><!-- /tab-exercises --> (marca existe 1x).
- Personagens aula 5: Dr. Adams (visitante EUA, arthur) / Andreia (ellen).
- B1: 50% bilíngue no pre-class; 8-10 vocab; zero PT nos slides.
