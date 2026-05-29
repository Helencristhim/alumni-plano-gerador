#!/usr/bin/env python3
"""
Build Gabriela Pires - Aula 6: Numbers, Time & Dates
Inserts Pre-class, IN CLASS slides, Complementary, and audioMap into both professor and aluno files.
"""
import re, os

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROF = os.path.join(BASE, 'public', 'professor', 'gabriela-pires.html')
ALUNO = os.path.join(BASE, 'public', 'aluno', 'gabriela-pires.html')

# ============================================================
# AULA 6 AUDIO MAP ENTRIES
# ============================================================
AULA6_AUDIO = {
  "O'clock": "oclock",
  "It is three o'clock.": "it_is_three_oclock",
  "Quarter": "quarter",
  "It is a quarter past two.": "it_is_a_quarter_past_two",
  "Half past": "half_past",
  "It is half past ten.": "it_is_half_past_ten",
  "Noon": "noon",
  "We have lunch at noon.": "we_have_lunch_at_noon",
  "Midnight": "midnight",
  "The flight arrives at midnight.": "the_flight_arrives_at_midnight",
  "Flight": "flight",
  "My flight is at nine o'clock.": "my_flight_is_at_nine_oclock",
  "Ticket": "ticket",
  "How much is the ticket?": "how_much_is_the_ticket",
  "Price": "price",
  "What is the price?": "what_is_the_price",
  "What time is it?": "what_time_is_it",
  "It is a quarter to five.": "it_is_a_quarter_to_five",
  "My flight is on February 3rd.": "my_flight_is_on_february_3rd",
  "How much does this cost?": "how_much_does_this_cost",
  "Excuse me, what time is it?": "excuse_me_what_time_is_it",
  "The museum opens at ten o'clock.": "the_museum_opens_at_ten_oclock",
  "The Eiffel Tower visit is at a quarter past four.": "the_eiffel_tower_visit_is_at_a_quarter_past_four",
  "Lunch is at half past twelve.": "lunch_is_at_half_past_twelve",
  "The departure time is eight thirty.": "the_departure_time_is_eight_thirty",
  "One ticket, please. How much is it?": "one_ticket_please_how_much_is_it",
  "It is ten euros.": "it_is_ten_euros",
  "Here you go. Thank you!": "here_you_go_thank_you",
  "What time does the next tour start?": "what_time_does_the_next_tour_start",
  "The next tour starts at a quarter past three.": "the_next_tour_starts_at_a_quarter_past_three",
  "When is your flight to Paris?": "when_is_your_flight_to_paris",
  "My flight is on February 3rd, 2027.": "my_flight_is_on_february_3rd_2027",
  "What time does it depart?": "what_time_does_it_depart",
  "It departs at nine fifteen in the morning.": "it_departs_at_nine_fifteen_in_the_morning",
  "And what time does it arrive?": "and_what_time_does_it_arrive",
  "It arrives at eleven thirty at night.": "it_arrives_at_eleven_thirty_at_night",
  "That is a long flight!": "that_is_a_long_flight",
  "Yes! But I am so excited!": "yes_but_i_am_so_excited",
  "Gabriela is planning her trip to Paris. Her flight is on February 3rd, 2027. The departure time is 9:15 AM from São Paulo. She arrives in Paris at 11:30 PM. On February 4th, she visits the Louvre at 10 o'clock. Lunch is at half past twelve at a French café. The Eiffel Tower visit is at a quarter past four. A ticket to the Eiffel Tower costs 26 euros. On February 5th, she goes to Versailles. The train departs at a quarter to nine.": "gabriela_is_planning_her_trip_to_paris_full_listening",
  "Good afternoon! Welcome to the Louvre. How can I help you?": "good_afternoon_welcome_to_the_louvre",
  "One student ticket, please. How much is it?": "one_student_ticket_please_how_much_is_it",
  "It is 15 euros. Here is your ticket.": "it_is_15_euros_here_is_your_ticket",
  "Thank you! What time does the museum close?": "thank_you_what_time_does_the_museum_close",
  "We close at six o'clock.": "we_close_at_six_oclock",
  "And what time is the next guided tour?": "and_what_time_is_the_next_guided_tour",
  "The next tour starts at a quarter past three. It is in English.": "the_next_tour_starts_at_a_quarter_past_three_in_english",
  "Perfect! Thank you very much!": "perfect_thank_you_very_much",
  "Enjoy your visit!": "enjoy_your_visit",
  "It is seven o'clock.": "it_is_seven_oclock",
  "It is a quarter past nine.": "it_is_a_quarter_past_nine",
  "It is half past twelve.": "it_is_half_past_twelve",
  "It is a quarter to five.": "it_is_a_quarter_to_five_drill",
  "It is midnight.": "it_is_midnight",
  "It is noon.": "it_is_noon",
  "Excuse me, what time is it? It is half past ten.": "excuse_me_what_time_is_it_half_past_ten",
  "My flight is on February 3rd. What is the price?": "my_flight_is_on_february_3rd_what_is_the_price",
  "One ticket, please. How much does this cost?": "one_ticket_please_how_much_does_this_cost",
  "The museum opens at ten. It closes at six.": "the_museum_opens_at_ten_it_closes_at_six",
  "What time is your English class? My class is at three o'clock.": "what_time_is_your_english_class_my_class_is_at_three_oclock",
  "February 3rd": "february_3rd",
  "March 15th": "march_15th",
  "It is eight forty-five.": "it_is_eight_fortyfive",
  "The train departs at a quarter to nine.": "the_train_departs_at_a_quarter_to_nine",
  "Departure": "departure",
  "The departure time is 8 AM.": "the_departure_time_is_8_am",
  "Arrival": "arrival",
  "The arrival time is noon.": "the_arrival_time_is_noon",
  "Change": "change",
  "Here is your change.": "here_is_your_change",
  "Total": "total",
  "The total is twenty-six euros.": "the_total_is_twentysix_euros",
}

# Build audioMap JS entries
def build_audiomap_entries():
    lines = []
    for phrase, slug in AULA6_AUDIO.items():
        escaped = phrase.replace("'", "\\'")
        lines.append(f'  "{escaped}": "/audio/gabriela-pires/{slug}.mp3?v=2"')
    return ',\n'.join(lines)

# ============================================================
# AULA 6 PRE-CLASS HTML
# ============================================================
PRECLASS_HTML = '''<div class="lesson-card" id="ex-lesson-6">
  <div class="lesson-header" onclick="toggleLesson(this)">
    <div class="lesson-header-img" style="background-image:url('https://images.unsplash.com/photo-1502602898657-3e91760cbb34?w=600&q=80')"></div>
    <div class="lesson-header-content">
      <div class="lesson-number">Aula 06 &mdash; Pre-class</div>
      <h3>Numbers, Time &amp; Dates &mdash; The Tools You Need to Survive in Paris</h3>
      <div class="lesson-desc">Depois desta aula, voc&ecirc; consegue perguntar as horas, entender hor&aacute;rios de voo e comprar ingressos em Paris sem travar.</div>
      <div class="lesson-progress-mini"><div class="mini-bar"><div class="mini-bar-fill" data-lesson-progress="6" style="width:0%"></div></div><span class="mini-percent" data-lesson-pct="6">0%</span></div>
    </div>
    <div class="expand-icon">&#9660;</div>
  </div>
  <div class="lesson-body">
    <p style="font-size:0.85rem;color:var(--text-mid);margin-bottom:1.5rem;"><strong style="color:var(--accent);">Objetivo:</strong> Ao final desta aula, Gabriela ser&aacute; capaz de dizer as horas, perguntar pre&ccedil;os e dizer datas em ingl&ecirc;s &mdash; tudo que precisa para sobreviver em Paris.</p>

    <!-- ===== STAGE 1.1: VOCABULARY CARDS ===== -->
    <div class="exercise-section">
      <div class="section-header-row">
        <h4>Vocabul&aacute;rio <span class="badge badge-vocab">Vocabulary</span></h4>
        <button class="listen-all-btn" onclick="listenAllVocab(this)">&#9654; Ouvir todos</button>
      </div>
      <p class="microcopy">Olha a palavra, a tradu&ccedil;&atilde;o e o exemplo juntos. Toca em Ouvir &mdash; o som ajuda muito a mem&oacute;ria.</p>

      <div class="vocab-card">
        <div class="vocab-word">O&rsquo;clock</div>
        <div class="vocab-translation">em ponto</div>
        <div class="vocab-example">&ldquo;It is three <strong>o&rsquo;clock</strong>.&rdquo;</div>
        <button class="audio-btn" onclick="speakText('It is three o\\'clock.', this)">&#9654; Ouvir</button>
      </div>
      <div class="vocab-card">
        <div class="vocab-word">Quarter</div>
        <div class="vocab-translation">quinze minutos (quarto de hora)</div>
        <div class="vocab-example">&ldquo;It is a <strong>quarter</strong> past two.&rdquo;</div>
        <button class="audio-btn" onclick="speakText('It is a quarter past two.', this)">&#9654; Ouvir</button>
      </div>
      <div class="vocab-card">
        <div class="vocab-word">Half past</div>
        <div class="vocab-translation">meia hora (e meia)</div>
        <div class="vocab-example">&ldquo;It is <strong>half past</strong> ten.&rdquo;</div>
        <button class="audio-btn" onclick="speakText('It is half past ten.', this)">&#9654; Ouvir</button>
      </div>
      <div class="vocab-card">
        <div class="vocab-word">Noon</div>
        <div class="vocab-translation">meio-dia</div>
        <div class="vocab-example">&ldquo;We have lunch at <strong>noon</strong>.&rdquo;</div>
        <button class="audio-btn" onclick="speakText('We have lunch at noon.', this)">&#9654; Ouvir</button>
      </div>
      <div class="vocab-card">
        <div class="vocab-word">Midnight</div>
        <div class="vocab-translation">meia-noite</div>
        <div class="vocab-example">&ldquo;The flight arrives at <strong>midnight</strong>.&rdquo;</div>
        <button class="audio-btn" onclick="speakText('The flight arrives at midnight.', this)">&#9654; Ouvir</button>
      </div>
      <div class="vocab-card">
        <div class="vocab-word">Flight</div>
        <div class="vocab-translation">voo</div>
        <div class="vocab-example">&ldquo;My <strong>flight</strong> is at nine o&rsquo;clock.&rdquo;</div>
        <button class="audio-btn" onclick="speakText('My flight is at nine o\\'clock.', this)">&#9654; Ouvir</button>
      </div>
      <div class="vocab-card">
        <div class="vocab-word">Ticket</div>
        <div class="vocab-translation">passagem / ingresso</div>
        <div class="vocab-example">&ldquo;How much is the <strong>ticket</strong>?&rdquo;</div>
        <button class="audio-btn" onclick="speakText('How much is the ticket?', this)">&#9654; Ouvir</button>
      </div>
      <div class="vocab-card">
        <div class="vocab-word">Price</div>
        <div class="vocab-translation">pre&ccedil;o</div>
        <div class="vocab-example">&ldquo;What is the <strong>price</strong>?&rdquo;</div>
        <button class="audio-btn" onclick="speakText('What is the price?', this)">&#9654; Ouvir</button>
      </div>
    </div>

    <!-- ===== STAGE 1.2: MATCHING ===== -->
    <div class="exercise-section">
      <h4>V2. Match the words <span class="badge badge-vocab">Matching</span></h4>
      <p class="microcopy">Fa&ccedil;a um de cada vez. Errou? Leia a explica&ccedil;&atilde;o com calma &mdash; &eacute; a&iacute; que voc&ecirc; aprende de verdade.</p>
      <div class="match-grid" id="match-l6">
        <div class="match-row" data-answer="em ponto">
          <span class="match-word">O&rsquo;clock</span>
          <select onchange="checkMatch(this)">
            <option value="">Select...</option>
            <option value="meia hora">meia hora</option>
            <option value="voo">voo</option>
            <option value="em ponto">em ponto</option>
            <option value="meio-dia">meio-dia</option>
            <option value="pre&ccedil;o">pre&ccedil;o</option>
          </select>
        </div>
        <div class="match-row" data-answer="quinze minutos">
          <span class="match-word">Quarter</span>
          <select onchange="checkMatch(this)">
            <option value="">Select...</option>
            <option value="meia-noite">meia-noite</option>
            <option value="quinze minutos">quinze minutos</option>
            <option value="ingresso">ingresso</option>
            <option value="em ponto">em ponto</option>
            <option value="voo">voo</option>
          </select>
        </div>
        <div class="match-row" data-answer="meia hora">
          <span class="match-word">Half past</span>
          <select onchange="checkMatch(this)">
            <option value="">Select...</option>
            <option value="pre&ccedil;o">pre&ccedil;o</option>
            <option value="meia hora">meia hora</option>
            <option value="quinze minutos">quinze minutos</option>
            <option value="meio-dia">meio-dia</option>
            <option value="em ponto">em ponto</option>
          </select>
        </div>
        <div class="match-row" data-answer="meio-dia">
          <span class="match-word">Noon</span>
          <select onchange="checkMatch(this)">
            <option value="">Select...</option>
            <option value="ingresso">ingresso</option>
            <option value="meia-noite">meia-noite</option>
            <option value="meio-dia">meio-dia</option>
            <option value="voo">voo</option>
            <option value="meia hora">meia hora</option>
          </select>
        </div>
        <div class="match-row" data-answer="meia-noite">
          <span class="match-word">Midnight</span>
          <select onchange="checkMatch(this)">
            <option value="">Select...</option>
            <option value="meio-dia">meio-dia</option>
            <option value="em ponto">em ponto</option>
            <option value="meia-noite">meia-noite</option>
            <option value="pre&ccedil;o">pre&ccedil;o</option>
            <option value="quinze minutos">quinze minutos</option>
          </select>
        </div>
        <div class="match-row" data-answer="voo">
          <span class="match-word">Flight</span>
          <select onchange="checkMatch(this)">
            <option value="">Select...</option>
            <option value="meia hora">meia hora</option>
            <option value="voo">voo</option>
            <option value="ingresso">ingresso</option>
            <option value="meia-noite">meia-noite</option>
            <option value="meio-dia">meio-dia</option>
          </select>
        </div>
        <div class="match-row" data-answer="ingresso">
          <span class="match-word">Ticket</span>
          <select onchange="checkMatch(this)">
            <option value="">Select...</option>
            <option value="quinze minutos">quinze minutos</option>
            <option value="pre&ccedil;o">pre&ccedil;o</option>
            <option value="em ponto">em ponto</option>
            <option value="ingresso">ingresso</option>
            <option value="voo">voo</option>
          </select>
        </div>
        <div class="match-row" data-answer="pre&ccedil;o">
          <span class="match-word">Price</span>
          <select onchange="checkMatch(this)">
            <option value="">Select...</option>
            <option value="ingresso">ingresso</option>
            <option value="meia hora">meia hora</option>
            <option value="voo">voo</option>
            <option value="pre&ccedil;o">pre&ccedil;o</option>
            <option value="meia-noite">meia-noite</option>
          </select>
        </div>
      </div>
      <button class="verify-all-btn" onclick="verifyAllMatches('match-l6')">Check Answers</button>
    </div>

    <!-- ===== STAGE 1.3: GRAMMAR IN CONTEXT ===== -->
    <div class="exercise-section">
      <h4>Stage 1.2: Grammar in Context <span class="badge badge-practice">Grammar</span></h4>
      <p class="microcopy">Leia o texto com calma. As palavras em negrito s&atilde;o do vocabul&aacute;rio de hoje.</p>
      <div class="context-text" style="background:var(--accent-dim);border:1px solid rgba(212,50,106,0.15);border-radius:8px;padding:1.2rem;margin-bottom:1.2rem;line-height:1.9;font-size:0.95rem;">
        Gabriela is planning her trip to Paris. Her <strong>flight</strong> is on <strong>February 3rd</strong>, 2027. The departure time is <strong>nine fifteen</strong> in the morning. She arrives in Paris at <strong>half past eleven</strong> at night. On February 4th, she visits the Louvre at <strong>ten o&rsquo;clock</strong>. Lunch is at <strong>half past twelve</strong> at a French caf&eacute;. The Eiffel Tower visit is at <strong>a quarter past four</strong>. A <strong>ticket</strong> to the Eiffel Tower costs twenty-six euros. Gabriela asks: &ldquo;<strong>What time</strong> is it?&rdquo; and &ldquo;How much is the <strong>price</strong>?&rdquo;
      </div>
      <div class="quiz-item">
        <div class="quiz-question">What time does Gabriela visit the Louvre?</div>
        <div class="quiz-options">
          <div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> At half past ten</div>
          <div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> At ten o&rsquo;clock</div>
          <div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> At a quarter past ten</div>
        </div>
      </div>
      <div class="quiz-item">
        <div class="quiz-question">How much is the Eiffel Tower ticket?</div>
        <div class="quiz-options">
          <div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> Fifteen euros</div>
          <div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> Thirty euros</div>
          <div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">C</span> Twenty-six euros</div>
        </div>
      </div>
      <div class="quiz-item">
        <div class="quiz-question">What time is the Eiffel Tower visit?</div>
        <div class="quiz-options">
          <div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> A quarter past four</div>
          <div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> Half past four</div>
          <div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> Four o&rsquo;clock</div>
        </div>
      </div>
    </div>

    <!-- ===== STAGE 1.4: GRAMMAR TIP ===== -->
    <div class="exercise-section">
      <h4>Grammar Tip <span class="badge badge-practice">Grammar</span></h4>
      <div style="background:var(--accent-dim);border:1px solid rgba(212,50,106,0.15);border-radius:8px;padding:1.2rem;margin-bottom:1rem;">
        <p style="font-weight:700;color:var(--accent);margin-bottom:0.8rem;font-size:1rem;">Telling Time in American English / Dizendo as horas em ingl&ecirc;s americano</p>
        <table style="width:100%;border-collapse:collapse;font-size:0.9rem;">
          <tr style="border-bottom:1px solid var(--border);"><td style="padding:0.5rem;font-weight:600;">3:00</td><td style="padding:0.5rem;">It is three <strong>o&rsquo;clock</strong>.</td><td style="padding:0.5rem;color:var(--text-dim);">S&atilde;o tr&ecirc;s horas.</td></tr>
          <tr style="border-bottom:1px solid var(--border);"><td style="padding:0.5rem;font-weight:600;">3:15</td><td style="padding:0.5rem;">It is <strong>a quarter past</strong> three.</td><td style="padding:0.5rem;color:var(--text-dim);">S&atilde;o tr&ecirc;s e quinze.</td></tr>
          <tr style="border-bottom:1px solid var(--border);"><td style="padding:0.5rem;font-weight:600;">3:30</td><td style="padding:0.5rem;">It is <strong>half past</strong> three.</td><td style="padding:0.5rem;color:var(--text-dim);">S&atilde;o tr&ecirc;s e meia.</td></tr>
          <tr style="border-bottom:1px solid var(--border);"><td style="padding:0.5rem;font-weight:600;">3:45</td><td style="padding:0.5rem;">It is <strong>a quarter to</strong> four.</td><td style="padding:0.5rem;color:var(--text-dim);">S&atilde;o quinze para as quatro.</td></tr>
          <tr style="border-bottom:1px solid var(--border);"><td style="padding:0.5rem;font-weight:600;">12:00 PM</td><td style="padding:0.5rem;">It is <strong>noon</strong>.</td><td style="padding:0.5rem;color:var(--text-dim);">&Eacute; meio-dia.</td></tr>
          <tr><td style="padding:0.5rem;font-weight:600;">12:00 AM</td><td style="padding:0.5rem;">It is <strong>midnight</strong>.</td><td style="padding:0.5rem;color:var(--text-dim);">&Eacute; meia-noite.</td></tr>
        </table>
      </div>
      <div style="background:var(--accent-dim);border:1px solid rgba(212,50,106,0.15);border-radius:8px;padding:1.2rem;">
        <p style="font-weight:700;color:var(--accent);margin-bottom:0.8rem;font-size:1rem;">Dates in American English / Datas em ingl&ecirc;s americano</p>
        <p style="font-size:0.88rem;line-height:1.7;">In American English, the format is: <strong>Month + Day (ordinal) + Year</strong>.<br>
        Exemplo: <strong>February 3rd, 2027</strong> (n&atilde;o &ldquo;3 February&rdquo;).<br>
        Ordinals: 1st, 2nd, 3rd, 4th, 5th... 15th... 21st, 22nd, 23rd... 31st.</p>
        <p style="font-size:0.88rem;line-height:1.7;margin-top:0.5rem;"><strong>Questions / Perguntas:</strong><br>
        &ldquo;<strong>What time is it?</strong>&rdquo; &mdash; Que horas s&atilde;o?<br>
        &ldquo;<strong>How much is it?</strong>&rdquo; / &ldquo;<strong>How much does this cost?</strong>&rdquo; &mdash; Quanto custa?<br>
        &ldquo;<strong>When is your flight?</strong>&rdquo; &mdash; Quando &eacute; o seu voo?</p>
      </div>
    </div>

    <!-- ===== STAGE 1.5: FILL-IN-THE-BLANK ===== -->
    <div class="exercise-section">
      <h4>P1. Complete with the correct word <span class="badge badge-practice">Practice</span></h4>
      <p class="microcopy">Fa&ccedil;a um de cada vez. Errou? Leia a dica com calma.</p>

      <div class="fill-blank-item">
        <div class="fill-blank-sentence">
          &ldquo;Excuse me, what
          <input class="blank-input" data-answer="time" data-hint="Hint: you ask this about the clock" data-phrase="Excuse me, what time is it?" placeholder="___">
          is it?&rdquo;
        </div>
        <button class="check-btn" onclick="checkBlank(this)">Check</button>
        <button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button>
      </div>

      <div class="fill-blank-item">
        <div class="fill-blank-sentence">
          &ldquo;My
          <input class="blank-input" data-answer="flight" data-hint="Hint: you take this to travel by airplane" data-phrase="My flight is on February 3rd." placeholder="___">
          is on February 3rd.&rdquo;
        </div>
        <button class="check-btn" onclick="checkBlank(this)">Check</button>
        <button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button>
      </div>

      <div class="fill-blank-item">
        <div class="fill-blank-sentence">
          &ldquo;How much is the
          <input class="blank-input" data-answer="ticket" data-hint="Hint: you buy this to enter a museum" data-phrase="How much is the ticket?" placeholder="___">
          ?&rdquo;
        </div>
        <button class="check-btn" onclick="checkBlank(this)">Check</button>
        <button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button>
      </div>

      <div class="fill-blank-item">
        <div class="fill-blank-sentence">
          &ldquo;It is
          <input class="blank-input" data-answer="half past" data-alt="half past" data-hint="Hint: 30 minutes past the hour" data-phrase="It is half past ten." placeholder="___">
          ten.&rdquo;
        </div>
        <button class="check-btn" onclick="checkBlank(this)">Check</button>
        <button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button>
      </div>

      <div class="fill-blank-item">
        <div class="fill-blank-sentence">
          &ldquo;The museum opens at ten
          <input class="blank-input" data-answer="o'clock" data-alt="oclock" data-hint="Hint: the word for exact hours" data-phrase="The museum opens at ten o'clock." placeholder="___">
          .&rdquo;
        </div>
        <button class="check-btn" onclick="checkBlank(this)">Check</button>
        <button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button>
      </div>
    </div>

    <!-- ===== STAGE 2: ORDERING ===== -->
    <div class="exercise-section">
      <h4>P2. Put in order <span class="badge badge-order">Order</span></h4>
      <p class="microcopy">Coloque as frases na ordem correta para formar um di&aacute;logo no guich&ecirc; do Louvre.</p>
      <div class="order-container" id="order-l6">
        <div class="order-item" draggable="true" data-order="3" onclick="selectOrderItem(this,'order-l6')">
          <span class="order-num">?</span>
          <span class="order-text">&ldquo;It is 15 euros. Here is your ticket.&rdquo;</span>
          <span class="order-arrows">
            <button class="arrow-btn" onclick="moveItem(this,-1,'order-l6')">&#9650;</button>
            <button class="arrow-btn" onclick="moveItem(this,1,'order-l6')">&#9660;</button>
          </span>
        </div>
        <div class="order-item" draggable="true" data-order="5" onclick="selectOrderItem(this,'order-l6')">
          <span class="order-num">?</span>
          <span class="order-text">&ldquo;We close at six o&rsquo;clock. Enjoy your visit!&rdquo;</span>
          <span class="order-arrows">
            <button class="arrow-btn" onclick="moveItem(this,-1,'order-l6')">&#9650;</button>
            <button class="arrow-btn" onclick="moveItem(this,1,'order-l6')">&#9660;</button>
          </span>
        </div>
        <div class="order-item" draggable="true" data-order="1" onclick="selectOrderItem(this,'order-l6')">
          <span class="order-num">?</span>
          <span class="order-text">&ldquo;Good afternoon! One student ticket, please.&rdquo;</span>
          <span class="order-arrows">
            <button class="arrow-btn" onclick="moveItem(this,-1,'order-l6')">&#9650;</button>
            <button class="arrow-btn" onclick="moveItem(this,1,'order-l6')">&#9660;</button>
          </span>
        </div>
        <div class="order-item" draggable="true" data-order="4" onclick="selectOrderItem(this,'order-l6')">
          <span class="order-num">?</span>
          <span class="order-text">&ldquo;Thank you! What time does the museum close?&rdquo;</span>
          <span class="order-arrows">
            <button class="arrow-btn" onclick="moveItem(this,-1,'order-l6')">&#9650;</button>
            <button class="arrow-btn" onclick="moveItem(this,1,'order-l6')">&#9660;</button>
          </span>
        </div>
        <div class="order-item" draggable="true" data-order="2" onclick="selectOrderItem(this,'order-l6')">
          <span class="order-num">?</span>
          <span class="order-text">&ldquo;How much is it?&rdquo;</span>
          <span class="order-arrows">
            <button class="arrow-btn" onclick="moveItem(this,-1,'order-l6')">&#9650;</button>
            <button class="arrow-btn" onclick="moveItem(this,1,'order-l6')">&#9660;</button>
          </span>
        </div>
      </div>
      <button class="verify-all-btn" onclick="checkOrder('order-l6')">Check Order</button>
    </div>

    <!-- ===== STAGE 3: PRONUNCIATION ===== -->
    <div class="exercise-section">
      <h4>S1. Read aloud <span class="badge badge-speak">Speaking</span></h4>
      <p class="microcopy">Toque em Ouvir, repita, depois grave e compare. O objetivo &eacute; praticar, n&atilde;o ser perfeito.</p>

      <div class="speech-card" data-phrase="Excuse me, what time is it?">
        <div class="speech-phrase">Excuse me, what time is it?</div>
        <div class="speech-translation">Com licen&ccedil;a, que horas s&atilde;o?</div>
        <div class="speech-controls">
          <button class="btn btn-listen" onclick="speakPhrase(this)">&#9654; Ouvir</button>
          <button class="btn btn-record" onclick="startRecording(this)">&#9679; Gravar</button>
          <button class="btn btn-stop" onclick="stopRecording(this)">&#9632; Parar</button>
        </div>
        <div class="speech-result"></div>
      </div>

      <div class="speech-card" data-phrase="My flight is on February 3rd, 2027.">
        <div class="speech-phrase">My flight is on February 3rd, 2027.</div>
        <div class="speech-translation">Meu voo &eacute; no dia 3 de fevereiro de 2027.</div>
        <div class="speech-controls">
          <button class="btn btn-listen" onclick="speakPhrase(this)">&#9654; Ouvir</button>
          <button class="btn btn-record" onclick="startRecording(this)">&#9679; Gravar</button>
          <button class="btn btn-stop" onclick="stopRecording(this)">&#9632; Parar</button>
        </div>
        <div class="speech-result"></div>
      </div>

      <div class="speech-card" data-phrase="One ticket, please. How much is it?">
        <div class="speech-phrase">One ticket, please. How much is it?</div>
        <div class="speech-translation">Uma entrada, por favor. Quanto custa?</div>
        <div class="speech-controls">
          <button class="btn btn-listen" onclick="speakPhrase(this)">&#9654; Ouvir</button>
          <button class="btn btn-record" onclick="startRecording(this)">&#9679; Gravar</button>
          <button class="btn btn-stop" onclick="stopRecording(this)">&#9632; Parar</button>
        </div>
        <div class="speech-result"></div>
      </div>

      <div class="speech-card" data-phrase="The museum opens at ten o'clock.">
        <div class="speech-phrase">The museum opens at ten o&rsquo;clock.</div>
        <div class="speech-translation">O museu abre &agrave;s dez horas.</div>
        <div class="speech-controls">
          <button class="btn btn-listen" onclick="speakPhrase(this)">&#9654; Ouvir</button>
          <button class="btn btn-record" onclick="startRecording(this)">&#9679; Gravar</button>
          <button class="btn btn-stop" onclick="stopRecording(this)">&#9632; Parar</button>
        </div>
        <div class="speech-result"></div>
      </div>
    </div>

    <!-- ===== STAGE 4: QUIZ ===== -->
    <div class="exercise-section">
      <h4>Q1. Choose the best answer <span class="badge badge-quiz">Quiz</span></h4>
      <p class="microcopy">Imagine a situa&ccedil;&atilde;o e escolha a melhor resposta.</p>

      <div class="quiz-item">
        <div class="quiz-question">You are at the Louvre and want to buy a ticket. What do you say?</div>
        <div class="quiz-options">
          <div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> &ldquo;I want ticket Louvre.&rdquo;</div>
          <div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> &ldquo;One ticket, please. How much is it?&rdquo;</div>
          <div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> &ldquo;Give me one ticket now.&rdquo;</div>
        </div>
      </div>

      <div class="quiz-item">
        <div class="quiz-question">You need to know the time. What do you ask?</div>
        <div class="quiz-options">
          <div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> &ldquo;What is the hour?&rdquo;</div>
          <div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> &ldquo;Tell me the clock.&rdquo;</div>
          <div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">C</span> &ldquo;Excuse me, what time is it?&rdquo;</div>
        </div>
      </div>

      <div class="quiz-item">
        <div class="quiz-question">The clock shows 4:45. How do you say it?</div>
        <div class="quiz-options">
          <div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> &ldquo;It is a quarter to five.&rdquo;</div>
          <div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> &ldquo;It is a quarter past four.&rdquo;</div>
          <div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> &ldquo;It is half past four.&rdquo;</div>
        </div>
      </div>

      <div class="quiz-item">
        <div class="quiz-question">Someone asks: &ldquo;When is your flight?&rdquo; What do you answer?</div>
        <div class="quiz-options">
          <div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> &ldquo;My flight is 3 February.&rdquo;</div>
          <div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> &ldquo;My flight is on February 3rd.&rdquo;</div>
          <div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> &ldquo;Flight February three.&rdquo;</div>
        </div>
      </div>
    </div>

    <!-- ===== STAGE 5: THINK ===== -->
    <div class="exercise-section">
      <h4>T1. Think and respond <span class="badge badge-think">Reflection</span></h4>
      <p class="microcopy">Aqui n&atilde;o tem resposta certa &mdash; &eacute; pra voc&ecirc; pensar em ingl&ecirc;s. Toque no microfone e responde como vier.</p>
      <div class="think-card">
        <div style="font-size:0.92rem;color:var(--text);margin-bottom:1rem;line-height:1.8;">You are at the Eiffel Tower ticket counter in Paris. Tell the person: your name, when your flight arrived, ask for one ticket, ask the price, and ask what time the tower closes.</div>
        <div class="speech-card" data-phrase="Hi, my name is Gabriela. My flight arrived on February 3rd. One ticket, please. How much is it? What time does the tower close?" style="background:var(--accent-dim);border:1px solid rgba(212,50,106,0.25);">
          <div style="font-size:0.72rem;font-weight:600;text-transform:uppercase;letter-spacing:1.5px;color:var(--accent);margin-bottom:0.5rem;">Sugest&atilde;o de resposta</div>
          <div class="speech-phrase" style="font-size:1.05rem;">&ldquo;Hi, my name is Gabriela. My flight arrived on February 3rd. One ticket, please. How much is it? What time does the tower close?&rdquo;</div>
          <div class="speech-translation">Oi, meu nome &eacute; Gabriela. Meu voo chegou dia 3 de fevereiro. Uma entrada, por favor. Quanto custa? Que horas a torre fecha?</div>
          <div class="speech-controls">
            <button class="btn btn-listen" onclick="speakPhrase(this)">&#9654; Ouvir</button>
            <button class="btn btn-record" onclick="startRecording(this)">&#9679; Gravar e comparar</button>
            <button class="btn btn-stop" onclick="stopRecording(this)">&#9632; Parar</button>
          </div>
          <div class="speech-result"></div>
        </div>
      </div>
    </div>

    <!-- ===== SURVIVAL CARD ===== -->
    <div class="survival-card">
      <h4>Survival Card &mdash; Lesson 6: Numbers, Time &amp; Dates</h4>
      <div class="survival-phrase"><span class="sp-num">1</span><span class="sp-en">Excuse me, what time is it?</span><span class="sp-pt">Com licen&ccedil;a, que horas s&atilde;o?</span><button class="btn btn-listen" onclick="speakText('Excuse me, what time is it?', this)">&#9654;</button></div>
      <div class="survival-phrase"><span class="sp-num">2</span><span class="sp-en">My flight is on February 3rd.</span><span class="sp-pt">Meu voo &eacute; dia 3 de fevereiro.</span><button class="btn btn-listen" onclick="speakText('My flight is on February 3rd.', this)">&#9654;</button></div>
      <div class="survival-phrase"><span class="sp-num">3</span><span class="sp-en">One ticket, please. How much is it?</span><span class="sp-pt">Uma entrada, por favor. Quanto custa?</span><button class="btn btn-listen" onclick="speakText('One ticket, please. How much is it?', this)">&#9654;</button></div>
      <div class="survival-phrase"><span class="sp-num">4</span><span class="sp-en">The museum opens at ten o&rsquo;clock.</span><span class="sp-pt">O museu abre &agrave;s dez horas.</span><button class="btn btn-listen" onclick="speakText('The museum opens at ten o\\'clock.', this)">&#9654;</button></div>
      <div class="survival-phrase"><span class="sp-num">5</span><span class="sp-en">It is half past twelve.</span><span class="sp-pt">&Eacute; meio-dia e meia.</span><button class="btn btn-listen" onclick="speakText('It is half past twelve.', this)">&#9654;</button></div>
    </div>

  </div>
</div>'''

# ============================================================
# AULA 6 IN CLASS SLIDES HTML (28 slides, data-slide 147-174)
# ============================================================
SLIDES_HTML = '''
<!-- ================ LESSON 6: NUMBERS, TIME & DATES ================ -->

<!-- SLIDE 147: L6 CHAPTER 1 - THE DREAM -->
<div class="slide slide-image" data-slide="147" data-phase="1" data-lesson="6" data-teacher="<strong>Abertura (2 min):</strong> 'Welcome back, Gabriela! Last class we talked about likes and dislikes. Today: NUMBERS, TIME, and DATES &mdash; the survival tools for Paris!' Tom animado." style="background-image:url('https://images.unsplash.com/photo-1502602898657-3e91760cbb34?w=600&q=80')">
  <div class="slide-inner">
    <div class="chapter-label">Chapter 1 &mdash; The Dream</div>
    <h1 class="slide-title">Numbers, Time &amp; <span class="accent">Dates</span></h1>
    <p class="slide-subtitle">The tools you need to survive in Paris</p>
  </div>
</div>

<!-- SLIDE 148: L6 WARM-UP CALLBACK -->
<div class="slide slide-dark" data-slide="148" data-phase="1" data-lesson="6" data-teacher="<strong>Callback Aula 5 (3 min):</strong> Perguntas r&aacute;pidas usando like/love/hate da aula anterior. Gabriela responde com frases completas. Depois: 'Tell me 3 things you love in 30 seconds!' Corrija gentilmente. Depois: 'Today you learn something you NEED for Paris: NUMBERS and TIME.'">
  <div class="slide-inner">
    <div class="chapter-label">Warm-up</div>
    <h2 class="slide-heading">Quick <span class="accent">Callback</span></h2>
    <div class="warm-questions">
      <div class="warm-q">Tell me one series you love and one you hate.</div>
      <div class="warm-q">What is your favorite celebrity? Why?</div>
      <div class="warm-q">Imagine: you are in Paris. What TIME is it right now in France?</div>
    </div>
  </div>
</div>

<!-- SLIDE 149: L6 CHAPTER 2 TRANSITION -->
<div class="slide slide-image" data-slide="149" data-phase="2" data-lesson="6" data-teacher="<strong>Transi&ccedil;&atilde;o (10s):</strong> 'Let us pack the words you need for time, dates, and prices!' Avance." style="background-image:url('https://images.unsplash.com/photo-1502602898657-3e91760cbb34?w=600&q=80')">
  <div class="slide-inner">
    <div class="chapter-label">Chapter 2</div>
    <h1 class="slide-title">Packing <span class="accent">Words</span></h1>
    <p class="slide-subtitle">Your time and date vocabulary for Paris</p>
  </div>
</div>

<!-- SLIDE 150: L6 VOCAB CARDS 1-4 -->
<div class="slide slide-light" data-slide="150" data-phase="2" data-lesson="6" data-teacher="<strong>Vocabul&aacute;rio (8 min):</strong> ANTES de clicar, leia a pista: 'What word do you think this is?' DEPOIS de revelar, toque audio 2x. Drill: o'clock /&obreve;-KLAK/ &mdash; 2 s&iacute;labas. quarter /KWOR-ter/ &mdash; som do QU. half past /haf past/ &mdash; L mudo em half. noon /nuun/ &mdash; som longo do OO. Drill cada 3x.">
  <div class="slide-inner">
    <h2 class="slide-heading">Time <span class="accent">Words</span></h2>
    <div class="vocab-grid">
      <div class="vocab-card" onclick="this.classList.toggle('revealed')">
        <div class="card-icon" style="background:linear-gradient(135deg,#003080,#1e5fa0)">
          <svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="1.5"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>
          <div class="card-hint">The exact hour &mdash; no minutes</div>
        </div>
        <div class="card-body">
          <div class="card-word">O&rsquo;clock</div>
          <div class="card-def">Used for exact hours</div>
          <div class="card-example">&ldquo;It is three <strong>o&rsquo;clock</strong>.&rdquo;</div>
          <div class="card-audio"><button class="audio-btn-sm" onclick="event.stopPropagation();speakText('It is three o\\'clock.',this)"><svg viewBox="0 0 24 24"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M19.07 4.93a10 10 0 010 14.14M15.54 8.46a5 5 0 010 7.07"/></svg> Listen</button></div>
        </div>
      </div>
      <div class="vocab-card" onclick="this.classList.toggle('revealed')">
        <div class="card-icon" style="background:linear-gradient(135deg,#7c3aed,#a855f7)">
          <svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="1.5"><circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/></svg>
          <div class="card-hint">15 minutes past or before</div>
        </div>
        <div class="card-body">
          <div class="card-word">Quarter</div>
          <div class="card-def">15 minutes of an hour</div>
          <div class="card-example">&ldquo;It is a <strong>quarter</strong> past two.&rdquo;</div>
          <div class="card-audio"><button class="audio-btn-sm" onclick="event.stopPropagation();speakText('It is a quarter past two.',this)"><svg viewBox="0 0 24 24"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M19.07 4.93a10 10 0 010 14.14M15.54 8.46a5 5 0 010 7.07"/></svg> Listen</button></div>
        </div>
      </div>
      <div class="vocab-card" onclick="this.classList.toggle('revealed')">
        <div class="card-icon" style="background:linear-gradient(135deg,#dc2626,#ef4444)">
          <svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="1.5"><circle cx="12" cy="12" r="10"/><path d="M12 6v6"/><circle cx="12" cy="12" r="2"/></svg>
          <div class="card-hint">30 minutes after the hour</div>
        </div>
        <div class="card-body">
          <div class="card-word">Half past</div>
          <div class="card-def">30 minutes after an hour</div>
          <div class="card-example">&ldquo;It is <strong>half past</strong> ten.&rdquo;</div>
          <div class="card-audio"><button class="audio-btn-sm" onclick="event.stopPropagation();speakText('It is half past ten.',this)"><svg viewBox="0 0 24 24"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M19.07 4.93a10 10 0 010 14.14M15.54 8.46a5 5 0 010 7.07"/></svg> Listen</button></div>
        </div>
      </div>
      <div class="vocab-card" onclick="this.classList.toggle('revealed')">
        <div class="card-icon" style="background:linear-gradient(135deg,#d97706,#f59e0b)">
          <svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="1.5"><circle cx="12" cy="12" r="5"/><line x1="12" y1="1" x2="12" y2="3"/><line x1="12" y1="21" x2="12" y2="23"/><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"/><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"/></svg>
          <div class="card-hint">12:00 PM &mdash; the sun is highest</div>
        </div>
        <div class="card-body">
          <div class="card-word">Noon</div>
          <div class="card-def">12:00 in the daytime</div>
          <div class="card-example">&ldquo;We have lunch at <strong>noon</strong>.&rdquo;</div>
          <div class="card-audio"><button class="audio-btn-sm" onclick="event.stopPropagation();speakText('We have lunch at noon.',this)"><svg viewBox="0 0 24 24"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M19.07 4.93a10 10 0 010 14.14M15.54 8.46a5 5 0 010 7.07"/></svg> Listen</button></div>
        </div>
      </div>
    </div>
    <div class="vocab-counter"><span id="vc6a">0</span> / 4 words</div>
  </div>
</div>

<!-- SLIDE 151: L6 VOCAB CARDS 5-8 -->
<div class="slide slide-light" data-slide="151" data-phase="2" data-lesson="6" data-teacher="<strong>Vocabul&aacute;rio (6 min):</strong> midnight /MID-nait/ &mdash; 2 s&iacute;labas. flight /flait/ &mdash; som do AI longo. ticket /TI-ket/ &mdash; 2 s&iacute;labas, T forte. price /prais/ &mdash; som do AI longo. Drill cada 3x. Pergunte: 'What is the PRICE of a ticket to the Louvre?'">
  <div class="slide-inner">
    <h2 class="slide-heading">Travel <span class="accent">Words</span></h2>
    <div class="vocab-grid">
      <div class="vocab-card" onclick="this.classList.toggle('revealed')">
        <div class="card-icon" style="background:linear-gradient(135deg,#1e3a5f,#334155)">
          <svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="1.5"><path d="M21 12.79A9 9 0 1111.21 3 7 7 0 0021 12.79z"/></svg>
          <div class="card-hint">12:00 AM &mdash; the darkest hour</div>
        </div>
        <div class="card-body">
          <div class="card-word">Midnight</div>
          <div class="card-def">12:00 at night</div>
          <div class="card-example">&ldquo;The flight arrives at <strong>midnight</strong>.&rdquo;</div>
          <div class="card-audio"><button class="audio-btn-sm" onclick="event.stopPropagation();speakText('The flight arrives at midnight.',this)"><svg viewBox="0 0 24 24"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M19.07 4.93a10 10 0 010 14.14M15.54 8.46a5 5 0 010 7.07"/></svg> Listen</button></div>
        </div>
      </div>
      <div class="vocab-card" onclick="this.classList.toggle('revealed')">
        <div class="card-icon" style="background:linear-gradient(135deg,#0891b2,#06b6d4)">
          <svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="1.5"><path d="M17.8 19.2L16 11l3.5-3.5C21 6 21.5 4 21 3c-1-.5-3 0-4.5 1.5L13 8 4.8 6.2c-.5-.1-.9.1-1.1.5l-.3.5c-.2.4-.1.9.3 1.1l5.1 3 1.5 1.5-3.6 2.4-1.6-.6c-.4-.2-.9 0-1.1.4l-.2.3c-.2.4 0 .9.4 1.1l2.8 1.2 1.2 2.8c.2.4.7.6 1.1.4l.3-.2c.4-.2.6-.7.4-1.1l-.6-1.6 2.4-3.6 1.5 1.5 3 5.1c.2.4.7.5 1.1.3l.5-.3c.4-.2.6-.6.5-1.1z"/></svg>
          <div class="card-hint">It takes you from one country to another</div>
        </div>
        <div class="card-body">
          <div class="card-word">Flight</div>
          <div class="card-def">A trip by airplane</div>
          <div class="card-example">&ldquo;My <strong>flight</strong> is at nine o&rsquo;clock.&rdquo;</div>
          <div class="card-audio"><button class="audio-btn-sm" onclick="event.stopPropagation();speakText('My flight is at nine o\\'clock.',this)"><svg viewBox="0 0 24 24"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M19.07 4.93a10 10 0 010 14.14M15.54 8.46a5 5 0 010 7.07"/></svg> Listen</button></div>
        </div>
      </div>
      <div class="vocab-card" onclick="this.classList.toggle('revealed')">
        <div class="card-icon" style="background:linear-gradient(135deg,#059669,#10b981)">
          <svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="1.5"><rect x="2" y="7" width="20" height="14" rx="2" ry="2"/><path d="M16 3v4M8 3v4"/><line x1="2" y1="11" x2="22" y2="11"/></svg>
          <div class="card-hint">You buy this to enter a museum</div>
        </div>
        <div class="card-body">
          <div class="card-word">Ticket</div>
          <div class="card-def">A pass to enter a place or travel</div>
          <div class="card-example">&ldquo;How much is the <strong>ticket</strong>?&rdquo;</div>
          <div class="card-audio"><button class="audio-btn-sm" onclick="event.stopPropagation();speakText('How much is the ticket?',this)"><svg viewBox="0 0 24 24"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M19.07 4.93a10 10 0 010 14.14M15.54 8.46a5 5 0 010 7.07"/></svg> Listen</button></div>
        </div>
      </div>
      <div class="vocab-card" onclick="this.classList.toggle('revealed')">
        <div class="card-icon" style="background:linear-gradient(135deg,#be185d,#ec4899)">
          <svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="1.5"><line x1="12" y1="1" x2="12" y2="23"/><path d="M17 5H9.5a3.5 3.5 0 000 7h5a3.5 3.5 0 010 7H6"/></svg>
          <div class="card-hint">How much something costs</div>
        </div>
        <div class="card-body">
          <div class="card-word">Price</div>
          <div class="card-def">The amount of money something costs</div>
          <div class="card-example">&ldquo;What is the <strong>price</strong>?&rdquo;</div>
          <div class="card-audio"><button class="audio-btn-sm" onclick="event.stopPropagation();speakText('What is the price?',this)"><svg viewBox="0 0 24 24"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M19.07 4.93a10 10 0 010 14.14M15.54 8.46a5 5 0 010 7.07"/></svg> Listen</button></div>
        </div>
      </div>
    </div>
    <div class="vocab-counter"><span id="vc6b">0</span> / 4 words</div>
  </div>
</div>

<!-- SLIDE 152: L6 PRONUNCIATION DRILL -->
<div class="slide slide-light" data-slide="152" data-phase="2" data-lesson="6" data-teacher="<strong>Pron&uacute;ncia (4 min):</strong> Drill de pron&uacute;ncia das palavras de tempo. Foco: quarter /KWOR-ter/ &mdash; QU brasileiro n&atilde;o funciona. half /haf/ &mdash; L MUDO, n&atilde;o &eacute; 'ralf'. o'clock /&obreve;-KLAK/ &mdash; acento na 2a s&iacute;laba. Repita 3x cada com Gabriela.">
  <div class="slide-inner">
    <h2 class="slide-heading">Say It <span class="accent">Right</span></h2>
    <div class="pron-grid">
      <div class="pron-item" onclick="speakText('O\\'clock',this)">
        <div class="pron-word">O&rsquo;clock</div>
        <div class="pron-stress"><span class="pron-syl">o&rsquo;</span><span class="pron-syl stressed">CLOCK</span></div>
        <div class="pron-audio"><button class="audio-btn-sm" onclick="event.stopPropagation();speakText('O\\'clock',this)"><svg viewBox="0 0 24 24"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M19.07 4.93a10 10 0 010 14.14"/></svg> Listen</button></div>
      </div>
      <div class="pron-item" onclick="speakText('Quarter',this)">
        <div class="pron-word">Quarter</div>
        <div class="pron-stress"><span class="pron-syl stressed">QUAR</span><span class="pron-syl">ter</span></div>
        <div class="pron-audio"><button class="audio-btn-sm" onclick="event.stopPropagation();speakText('Quarter',this)"><svg viewBox="0 0 24 24"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M19.07 4.93a10 10 0 010 14.14"/></svg> Listen</button></div>
      </div>
      <div class="pron-item" onclick="speakText('Half past',this)">
        <div class="pron-word">Half past</div>
        <div class="pron-stress"><span class="pron-syl stressed">HAF</span><span class="pron-syl stressed">PAST</span></div>
        <div class="pron-audio"><button class="audio-btn-sm" onclick="event.stopPropagation();speakText('Half past',this)"><svg viewBox="0 0 24 24"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M19.07 4.93a10 10 0 010 14.14"/></svg> Listen</button></div>
      </div>
      <div class="pron-item" onclick="speakText('Midnight',this)">
        <div class="pron-word">Midnight</div>
        <div class="pron-stress"><span class="pron-syl stressed">MID</span><span class="pron-syl">night</span></div>
        <div class="pron-audio"><button class="audio-btn-sm" onclick="event.stopPropagation();speakText('Midnight',this)"><svg viewBox="0 0 24 24"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M19.07 4.93a10 10 0 010 14.14"/></svg> Listen</button></div>
      </div>
      <div class="pron-item" onclick="speakText('Ticket',this)">
        <div class="pron-word">Ticket</div>
        <div class="pron-stress"><span class="pron-syl stressed">TIC</span><span class="pron-syl">ket</span></div>
        <div class="pron-audio"><button class="audio-btn-sm" onclick="event.stopPropagation();speakText('Ticket',this)"><svg viewBox="0 0 24 24"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M19.07 4.93a10 10 0 010 14.14"/></svg> Listen</button></div>
      </div>
      <div class="pron-item" onclick="speakText('February 3rd',this)">
        <div class="pron-word">February 3rd</div>
        <div class="pron-stress"><span class="pron-syl stressed">FEB</span><span class="pron-syl">ru</span><span class="pron-syl">ary</span> <span class="pron-syl stressed">THIRD</span></div>
        <div class="pron-audio"><button class="audio-btn-sm" onclick="event.stopPropagation();speakText('February 3rd',this)"><svg viewBox="0 0 24 24"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M19.07 4.93a10 10 0 010 14.14"/></svg> Listen</button></div>
      </div>
    </div>
  </div>
</div>

<!-- SLIDE 153: L6 CHAPTER 3 TRANSITION -->
<div class="slide slide-image" data-slide="153" data-phase="3" data-lesson="6" data-teacher="<strong>Transi&ccedil;&atilde;o (10s):</strong> 'Words packed! Now let us crack the TIME CODE!' Avance." style="background-image:url('https://images.unsplash.com/photo-1502602898657-3e91760cbb34?w=600&q=80')">
  <div class="slide-inner">
    <div class="chapter-label">Chapter 3</div>
    <h1 class="slide-title">The <span class="accent">Code</span></h1>
    <p class="slide-subtitle">How to tell time like an American</p>
  </div>
</div>

<!-- SLIDE 154: L6 GRAMMAR DISCOVERY -->
<div class="slide slide-light" data-slide="154" data-phase="3" data-lesson="6" data-teacher="<strong>Grammar Discovery (5 min):</strong> Mostre as 4 frases. Pergunte: 'Look at the pink words. What pattern do you see?' Espere. Se n&atilde;o perceber: 'We use IT IS + time. For minutes, we use PAST (after) or TO (before).' Discovery method &mdash; ela descobre antes de voc&ecirc; explicar.">
  <div class="slide-inner">
    <h2 class="slide-heading">Spot the <span class="accent">Pattern</span></h2>
    <div class="grammar-sentences">
      <div class="grammar-sentence"><strong>It is</strong> three <strong>o&rsquo;clock</strong>.</div>
      <div class="grammar-sentence"><strong>It is</strong> a quarter <strong>past</strong> two.</div>
      <div class="grammar-sentence"><strong>It is</strong> <strong>half past</strong> ten.</div>
      <div class="grammar-sentence"><strong>It is</strong> a quarter <strong>to</strong> five.</div>
    </div>
    <p style="text-align:center;margin-top:1.5rem;font-size:1.1rem;color:var(--text);">What do the <span class="accent-bold">pink words</span> have in common?</p>
    <div style="text-align:center;margin-top:1rem;">
      <button class="btn-primary" onclick="this.nextElementSibling.classList.toggle('show');this.style.display='none'">Reveal the Rule</button>
      <div class="grammar-table-wrap">
        <table class="grammar-table">
          <tr><th>Time</th><th>Say</th></tr>
          <tr><td>3:00</td><td><strong>It is</strong> three <strong>o&rsquo;clock</strong></td></tr>
          <tr><td>3:15</td><td><strong>It is</strong> a quarter <strong>past</strong> three</td></tr>
          <tr><td>3:30</td><td><strong>It is</strong> <strong>half past</strong> three</td></tr>
          <tr><td>3:45</td><td><strong>It is</strong> a quarter <strong>to</strong> four</td></tr>
          <tr><td>12:00 PM</td><td><strong>It is noon</strong></td></tr>
          <tr><td>12:00 AM</td><td><strong>It is midnight</strong></td></tr>
        </table>
      </div>
    </div>
  </div>
</div>

<!-- SLIDE 155: L6 COMMON MISTAKE -->
<div class="slide slide-light" data-slide="155" data-phase="3" data-lesson="6" data-teacher="<strong>Common Mistake (3 min):</strong> 'Em portugu&ecirc;s: S&Atilde;O 3 horas. Em ingl&ecirc;s: IT IS &mdash; sempre IT IS, nunca THEY ARE ou ARE. E PAST = depois da hora, TO = antes da pr&oacute;xima hora.' Drill: 'It is a quarter PAST (not TO) two.' 3x cada.">
  <div class="slide-inner">
    <h2 class="slide-heading">Common <span class="accent">Mistake</span></h2>
    <div class="mistake-card">
      <div class="mistake-item mistake-wrong">
        <div class="mistake-icon"><svg viewBox="0 0 24 24" fill="none" stroke="#dc2626"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg></div>
        &ldquo;Are three o&rsquo;clock.&rdquo;
      </div>
      <div class="mistake-item mistake-right">
        <div class="mistake-icon"><svg viewBox="0 0 24 24" fill="none" stroke="#16a34a"><polyline points="20 6 9 17 4 12"/></svg></div>
        &ldquo;<strong>It is</strong> three o&rsquo;clock.&rdquo;
      </div>
    </div>
    <div class="mistake-card" style="margin-top:1rem;">
      <div class="mistake-item mistake-wrong">
        <div class="mistake-icon"><svg viewBox="0 0 24 24" fill="none" stroke="#dc2626"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg></div>
        &ldquo;3 February&rdquo; (British/PT order)
      </div>
      <div class="mistake-item mistake-right">
        <div class="mistake-icon"><svg viewBox="0 0 24 24" fill="none" stroke="#16a34a"><polyline points="20 6 9 17 4 12"/></svg></div>
        &ldquo;<strong>February 3rd</strong>&rdquo; (American order)
      </div>
    </div>
  </div>
</div>

<!-- SLIDE 156: L6 GRAMMAR PRACTICE -->
<div class="slide slide-light" data-slide="156" data-phase="3" data-lesson="6" data-teacher="<strong>Grammar Practice (4 min):</strong> Clique cada item para revelar. Gabriela tenta PRIMEIRO, depois clique. 'What time is 8:30?' Ela diz, voc&ecirc; confirma. Foco em past vs to.">
  <div class="slide-inner">
    <h2 class="slide-heading">Say the <span class="accent">Time</span></h2>
    <div class="fill-grid">
      <div class="fill-item" onclick="this.classList.toggle('revealed')">
        <div class="fill-text">7:00 &rarr; <span class="fill-blank">???</span><span class="fill-answer">It is seven o&rsquo;clock.</span></div>
      </div>
      <div class="fill-item" onclick="this.classList.toggle('revealed')">
        <div class="fill-text">9:15 &rarr; <span class="fill-blank">???</span><span class="fill-answer">It is a quarter past nine.</span></div>
      </div>
      <div class="fill-item" onclick="this.classList.toggle('revealed')">
        <div class="fill-text">12:30 &rarr; <span class="fill-blank">???</span><span class="fill-answer">It is half past twelve.</span></div>
      </div>
      <div class="fill-item" onclick="this.classList.toggle('revealed')">
        <div class="fill-text">4:45 &rarr; <span class="fill-blank">???</span><span class="fill-answer">It is a quarter to five.</span></div>
      </div>
      <div class="fill-item" onclick="this.classList.toggle('revealed')">
        <div class="fill-text">12:00 AM &rarr; <span class="fill-blank">???</span><span class="fill-answer">It is midnight.</span></div>
      </div>
      <div class="fill-item" onclick="this.classList.toggle('revealed')">
        <div class="fill-text">12:00 PM &rarr; <span class="fill-blank">???</span><span class="fill-answer">It is noon.</span></div>
      </div>
    </div>
  </div>
</div>

<!-- SLIDE 157: L6 CHAPTER 4 TRANSITION -->
<div class="slide slide-image" data-slide="157" data-phase="4" data-lesson="6" data-teacher="<strong>Transi&ccedil;&atilde;o (10s):</strong> 'Now imagine: you are at the Louvre in Paris. Let us practice!' Avance." style="background-image:url('https://images.unsplash.com/photo-1502602898657-3e91760cbb34?w=600&q=80')">
  <div class="slide-inner">
    <div class="chapter-label">Chapter 4</div>
    <h1 class="slide-title">Getting <span class="accent">There</span></h1>
    <p class="slide-subtitle">Gabriela at the Louvre ticket counter</p>
  </div>
</div>

<!-- SLIDE 158: L6 DIALOGUE LINE-BY-LINE -->
<div class="slide slide-dark" data-slide="158" data-phase="4" data-lesson="6" data-teacher="<strong>Di&aacute;logo (8 min):</strong> Clique Next Line para cada fala. Professor l&ecirc; Agent (voz masculina Arthur), Gabriela l&ecirc; suas falas. Vocabul&aacute;rio da aula em destaque rosa. Foco em how much, what time, o'clock, quarter past. Depois pergunte: 'How much is the ticket? What time does the museum close?'">
  <div class="slide-inner">
    <h2 class="slide-heading" style="color:#fff">At the <span class="accent">Louvre</span></h2>
    <div class="dialogue-box" id="dial6">
      <div class="dialogue-line" data-voice="arthur" style="opacity:0;transform:translateY(10px)">
        <div class="avatar" style="background:var(--navy)">A</div>
        <div class="bubble"><strong>Agent:</strong> Good afternoon! Welcome to the Louvre. How can I help you?<br><button class="audio-btn-sm" onclick="speakText('Good afternoon! Welcome to the Louvre. How can I help you?',this)"><svg viewBox="0 0 24 24"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/></svg> Listen</button></div>
      </div>
      <div class="dialogue-line" data-voice="ellen" style="opacity:0;transform:translateY(10px)">
        <div class="avatar" style="background:var(--accent)">G</div>
        <div class="bubble"><strong>Gabriela:</strong> One student <strong>ticket</strong>, please. How much is it?<br><button class="audio-btn-sm" onclick="speakText('One student ticket, please. How much is it?',this)"><svg viewBox="0 0 24 24"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/></svg> Listen</button></div>
      </div>
      <div class="dialogue-line" data-voice="arthur" style="opacity:0;transform:translateY(10px)">
        <div class="avatar" style="background:var(--navy)">A</div>
        <div class="bubble"><strong>Agent:</strong> It is 15 euros. Here is your <strong>ticket</strong>.<br><button class="audio-btn-sm" onclick="speakText('It is 15 euros. Here is your ticket.',this)"><svg viewBox="0 0 24 24"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/></svg> Listen</button></div>
      </div>
      <div class="dialogue-line" data-voice="ellen" style="opacity:0;transform:translateY(10px)">
        <div class="avatar" style="background:var(--accent)">G</div>
        <div class="bubble"><strong>Gabriela:</strong> Thank you! What <strong>time</strong> does the museum close?<br><button class="audio-btn-sm" onclick="speakText('Thank you! What time does the museum close?',this)"><svg viewBox="0 0 24 24"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/></svg> Listen</button></div>
      </div>
      <div class="dialogue-line" data-voice="arthur" style="opacity:0;transform:translateY(10px)">
        <div class="avatar" style="background:var(--navy)">A</div>
        <div class="bubble"><strong>Agent:</strong> We close at six <strong>o&rsquo;clock</strong>.<br><button class="audio-btn-sm" onclick="speakText('We close at six o\\'clock.',this)"><svg viewBox="0 0 24 24"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/></svg> Listen</button></div>
      </div>
      <div class="dialogue-line" data-voice="ellen" style="opacity:0;transform:translateY(10px)">
        <div class="avatar" style="background:var(--accent)">G</div>
        <div class="bubble"><strong>Gabriela:</strong> And what <strong>time</strong> is the next guided tour?<br><button class="audio-btn-sm" onclick="speakText('And what time is the next guided tour?',this)"><svg viewBox="0 0 24 24"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/></svg> Listen</button></div>
      </div>
      <div class="dialogue-line" data-voice="arthur" style="opacity:0;transform:translateY(10px)">
        <div class="avatar" style="background:var(--navy)">A</div>
        <div class="bubble"><strong>Agent:</strong> The next tour starts at a <strong>quarter past</strong> three. It is in English.<br><button class="audio-btn-sm" onclick="speakText('The next tour starts at a quarter past three. It is in English.',this)"><svg viewBox="0 0 24 24"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/></svg> Listen</button></div>
      </div>
      <div class="dialogue-line" data-voice="ellen" style="opacity:0;transform:translateY(10px)">
        <div class="avatar" style="background:var(--accent)">G</div>
        <div class="bubble"><strong>Gabriela:</strong> Perfect! Thank you very much!<br><button class="audio-btn-sm" onclick="speakText('Perfect! Thank you very much!',this)"><svg viewBox="0 0 24 24"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/></svg> Listen</button></div>
      </div>
    </div>
    <div style="text-align:center;margin-top:1rem;">
      <button class="btn-primary" onclick="var lines=document.querySelectorAll('#dial6 .dialogue-line');var shown=document.querySelectorAll('#dial6 .dialogue-line[style*=\\'opacity: 1\\']').length||document.querySelectorAll('#dial6 .dialogue-line.shown').length;lines.forEach(function(l,i){if(i<=shown){l.style.opacity='1';l.style.transform='translateY(0)';l.classList.add('shown')}})">Next Line</button>
    </div>
  </div>
</div>

<!-- SLIDE 159: L6 COMPREHENSION -->
<div class="slide slide-dark" data-slide="159" data-phase="4" data-lesson="6" data-teacher="<strong>Comprehension (3 min):</strong> Pergunte SEM mostrar respostas. Depois clique para revelar. Se Gabriela acertar, celebre! Foco: compreens&atilde;o do que o AGENTE disse.">
  <div class="slide-inner">
    <h2 class="slide-heading" style="color:#fff">Did You <span class="accent">Catch</span> That?</h2>
    <div class="comp-questions">
      <div class="comp-q" onclick="this.classList.toggle('revealed')">
        <div class="q-text">How much is the student ticket?</div>
        <div class="q-answer">15 euros</div>
      </div>
      <div class="comp-q" onclick="this.classList.toggle('revealed')">
        <div class="q-text">What time does the museum close?</div>
        <div class="q-answer">At six o&rsquo;clock</div>
      </div>
      <div class="comp-q" onclick="this.classList.toggle('revealed')">
        <div class="q-text">What time is the next guided tour?</div>
        <div class="q-answer">A quarter past three</div>
      </div>
    </div>
  </div>
</div>

<!-- SLIDE 160: L6 LISTENING 1 -->
<div class="slide slide-dark" data-slide="160" data-phase="4" data-lesson="6" data-teacher="<strong>Listening 1 (4 min):</strong> Toque o &aacute;udio PRIMEIRO. Gabriela ouve SEM texto. Depois pergunte: 'When is the flight? What time is the Eiffel Tower visit? How much is the ticket?' Toque novamente se preciso. Foco em extra&ccedil;&atilde;o de informa&ccedil;&atilde;o temporal.">
  <div class="slide-inner">
    <h2 class="slide-heading" style="color:#fff">Listen <span class="accent">First</span></h2>
    <p style="color:rgba(255,255,255,.6);text-align:center;margin-bottom:1.5rem;">Close your eyes and listen. What times and dates do you hear?</p>
    <div style="display:flex;flex-direction:column;align-items:center;gap:1rem;">
      <div style="width:200px;height:60px;background:rgba(255,255,255,.06);border-radius:30px;display:flex;align-items:center;justify-content:center;">
        <button class="btn-primary" onclick="speakText('Gabriela is planning her trip to Paris. Her flight is on February 3rd, 2027. The departure time is 9:15 AM from S\\u00e3o Paulo. She arrives in Paris at 11:30 PM. On February 4th, she visits the Louvre at 10 o\\'clock. Lunch is at half past twelve at a French caf\\u00e9. The Eiffel Tower visit is at a quarter past four. A ticket to the Eiffel Tower costs 26 euros. On February 5th, she goes to Versailles. The train departs at a quarter to nine.',this)" style="border-radius:30px;padding:.8rem 2rem;">
          <svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2"><polygon points="5 3 19 12 5 21 5 3"/></svg>
          &nbsp;Play
        </button>
      </div>
    </div>
    <div class="comp-questions" style="margin-top:2rem;">
      <div class="comp-q" onclick="this.classList.toggle('revealed')">
        <div class="q-text">When is Gabriela&rsquo;s flight?</div>
        <div class="q-answer">February 3rd, 2027</div>
      </div>
      <div class="comp-q" onclick="this.classList.toggle('revealed')">
        <div class="q-text">What time is the Eiffel Tower visit?</div>
        <div class="q-answer">A quarter past four</div>
      </div>
      <div class="comp-q" onclick="this.classList.toggle('revealed')">
        <div class="q-text">How much is the Eiffel Tower ticket?</div>
        <div class="q-answer">26 euros</div>
      </div>
    </div>
  </div>
</div>

<!-- SLIDE 161: L6 LISTENING 2 -->
<div class="slide slide-dark" data-slide="161" data-phase="4" data-lesson="6" data-teacher="<strong>Listening 2 (3 min):</strong> Di&aacute;logo entre Gabriela e amiga sobre o voo. Toque primeiro sem texto. Perguntas: 'When is the flight? What time does it depart? What time does it arrive?'">
  <div class="slide-inner">
    <h2 class="slide-heading" style="color:#fff">Listen <span class="accent">Again</span></h2>
    <p style="color:rgba(255,255,255,.6);text-align:center;margin-bottom:1.5rem;">A friend asks about the flight. Listen and answer.</p>
    <div style="display:flex;flex-direction:column;align-items:center;gap:.5rem;">
      <button class="btn-primary" onclick="speakText('When is your flight to Paris?',this)" style="border-radius:30px;padding:.6rem 1.5rem;font-size:.85rem;"><svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2"><polygon points="5 3 19 12 5 21 5 3"/></svg> &nbsp;Line 1</button>
      <button class="btn-primary" onclick="speakText('My flight is on February 3rd, 2027.',this)" style="border-radius:30px;padding:.6rem 1.5rem;font-size:.85rem;"><svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2"><polygon points="5 3 19 12 5 21 5 3"/></svg> &nbsp;Line 2</button>
      <button class="btn-primary" onclick="speakText('What time does it depart?',this)" style="border-radius:30px;padding:.6rem 1.5rem;font-size:.85rem;"><svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2"><polygon points="5 3 19 12 5 21 5 3"/></svg> &nbsp;Line 3</button>
      <button class="btn-primary" onclick="speakText('It departs at nine fifteen in the morning.',this)" style="border-radius:30px;padding:.6rem 1.5rem;font-size:.85rem;"><svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2"><polygon points="5 3 19 12 5 21 5 3"/></svg> &nbsp;Line 4</button>
      <button class="btn-primary" onclick="speakText('And what time does it arrive?',this)" style="border-radius:30px;padding:.6rem 1.5rem;font-size:.85rem;"><svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2"><polygon points="5 3 19 12 5 21 5 3"/></svg> &nbsp;Line 5</button>
      <button class="btn-primary" onclick="speakText('It arrives at eleven thirty at night.',this)" style="border-radius:30px;padding:.6rem 1.5rem;font-size:.85rem;"><svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2"><polygon points="5 3 19 12 5 21 5 3"/></svg> &nbsp;Line 6</button>
    </div>
    <div class="comp-questions" style="margin-top:1.5rem;">
      <div class="comp-q" onclick="this.classList.toggle('revealed')">
        <div class="q-text">What time does the flight depart?</div>
        <div class="q-answer">Nine fifteen in the morning (9:15 AM)</div>
      </div>
      <div class="comp-q" onclick="this.classList.toggle('revealed')">
        <div class="q-text">What time does it arrive?</div>
        <div class="q-answer">Eleven thirty at night (11:30 PM)</div>
      </div>
    </div>
  </div>
</div>

<!-- SLIDE 162: L6 ARTIFACT - PARIS ITINERARY -->
<div class="slide slide-light" data-slide="162" data-phase="4" data-lesson="6" data-teacher="<strong>Artefato (3 min):</strong> 'Look! This is Gabriela&rsquo;s Paris Itinerary.' Pergunte: 'What time is the Louvre visit? When does Gabriela arrive in Paris? How much is the Eiffel Tower ticket?' Gabriela responde usando o vocabul&aacute;rio da aula.">
  <div class="slide-inner">
    <h2 class="slide-heading">Gabriela&rsquo;s Paris <span class="accent">Itinerary</span></h2>
    <div style="background:#fff;border-radius:16px;overflow:hidden;max-width:520px;margin:0 auto;box-shadow:0 20px 60px rgba(0,0,0,.1);border:2px solid var(--accent)">
      <div style="background:var(--accent);color:#fff;padding:1rem 1.5rem;display:flex;align-items:center;justify-content:space-between">
        <span style="font-weight:700;letter-spacing:1px;">PARIS TRIP 2027</span>
        <span style="font-size:.7rem;letter-spacing:2px;text-transform:uppercase;opacity:.8">Gabriela Pires</span>
      </div>
      <div style="padding:1.2rem 1.5rem;">
        <div style="display:grid;grid-template-columns:auto 1fr;gap:.4rem 1rem;font-size:.88rem;line-height:1.6;">
          <strong style="color:var(--accent)">Feb 3rd</strong><span>Flight departs: <strong>9:15 AM</strong></span>
          <strong style="color:var(--accent)">Feb 3rd</strong><span>Arrives Paris CDG: <strong>11:30 PM</strong></span>
          <strong style="color:var(--accent)">Feb 4th</strong><span>Louvre Museum: <strong>10:00 AM</strong> &mdash; Ticket: <strong>&euro;15</strong></span>
          <strong style="color:var(--accent)">Feb 4th</strong><span>Lunch at caf&eacute;: <strong>12:30 PM</strong></span>
          <strong style="color:var(--accent)">Feb 4th</strong><span>Eiffel Tower: <strong>4:15 PM</strong> &mdash; Ticket: <strong>&euro;26</strong></span>
          <strong style="color:var(--accent)">Feb 5th</strong><span>Train to Versailles: <strong>8:45 AM</strong></span>
        </div>
      </div>
    </div>
  </div>
</div>

<!-- SLIDE 163: L6 CHAPTER 5 TRANSITION -->
<div class="slide slide-image" data-slide="163" data-phase="5" data-lesson="6" data-teacher="<strong>Transi&ccedil;&atilde;o (10s):</strong> 'Time to practice! Show me you can tell the time!' Avance." style="background-image:url('https://images.unsplash.com/photo-1502602898657-3e91760cbb34?w=600&q=80')">
  <div class="slide-inner">
    <div class="chapter-label">Chapter 5</div>
    <h1 class="slide-title"><span class="accent">Practice</span></h1>
    <p class="slide-subtitle">Numbers, time, and prices in action</p>
  </div>
</div>

<!-- SLIDE 164: L6 QUICK FIRE -->
<div class="slide slide-light" data-slide="164" data-phase="5" data-lesson="6" data-teacher="<strong>Quick Fire (6 min):</strong> Uma pergunta por vez. Gabriela responde ORALMENTE primeiro, depois clique Show Answer. Se travar: 'Start with IT IS...' Score: 6 acertos = confetti!">
  <div class="slide-inner">
    <h2 class="slide-heading">Quick <span class="accent">Fire</span></h2>
    <div id="qf6" style="min-height:200px;">
      <div class="qf-item" data-qf="1" style="display:block;">
        <p style="font-size:1.2rem;text-align:center;margin-bottom:1rem;">The clock shows <strong>10:30</strong>. What time is it?</p>
        <div style="text-align:center;">
          <button class="btn-secondary" onclick="this.nextElementSibling.style.display='block';this.style.display='none'">Show Answer</button>
          <p style="display:none;font-size:1.1rem;color:var(--accent);font-weight:700;">It is half past ten.</p>
        </div>
      </div>
      <div class="qf-item" data-qf="2" style="display:none;">
        <p style="font-size:1.2rem;text-align:center;margin-bottom:1rem;">You want to know the time. What do you ask?</p>
        <div style="text-align:center;">
          <button class="btn-secondary" onclick="this.nextElementSibling.style.display='block';this.style.display='none'">Show Answer</button>
          <p style="display:none;font-size:1.1rem;color:var(--accent);font-weight:700;">Excuse me, what time is it?</p>
        </div>
      </div>
      <div class="qf-item" data-qf="3" style="display:none;">
        <p style="font-size:1.2rem;text-align:center;margin-bottom:1rem;">Your flight date is February 3rd. How do you say it?</p>
        <div style="text-align:center;">
          <button class="btn-secondary" onclick="this.nextElementSibling.style.display='block';this.style.display='none'">Show Answer</button>
          <p style="display:none;font-size:1.1rem;color:var(--accent);font-weight:700;">My flight is on February 3rd.</p>
        </div>
      </div>
      <div class="qf-item" data-qf="4" style="display:none;">
        <p style="font-size:1.2rem;text-align:center;margin-bottom:1rem;">The clock shows <strong>2:15</strong>. What time is it?</p>
        <div style="text-align:center;">
          <button class="btn-secondary" onclick="this.nextElementSibling.style.display='block';this.style.display='none'">Show Answer</button>
          <p style="display:none;font-size:1.1rem;color:var(--accent);font-weight:700;">It is a quarter past two.</p>
        </div>
      </div>
      <div class="qf-item" data-qf="5" style="display:none;">
        <p style="font-size:1.2rem;text-align:center;margin-bottom:1rem;">You want to buy a museum ticket. What do you say?</p>
        <div style="text-align:center;">
          <button class="btn-secondary" onclick="this.nextElementSibling.style.display='block';this.style.display='none'">Show Answer</button>
          <p style="display:none;font-size:1.1rem;color:var(--accent);font-weight:700;">One ticket, please. How much is it?</p>
        </div>
      </div>
      <div class="qf-item" data-qf="6" style="display:none;">
        <p style="font-size:1.2rem;text-align:center;margin-bottom:1rem;">The clock shows <strong>8:45</strong>. What time is it?</p>
        <div style="text-align:center;">
          <button class="btn-secondary" onclick="this.nextElementSibling.style.display='block';this.style.display='none'">Show Answer</button>
          <p style="display:none;font-size:1.1rem;color:var(--accent);font-weight:700;">It is a quarter to nine.</p>
        </div>
      </div>
    </div>
    <div style="text-align:center;margin-top:1rem;">
      <span id="qf6score" style="font-weight:700;color:var(--accent);">1 / 6</span>
      <button class="btn-primary" style="margin-left:1rem;" onclick="var items=document.querySelectorAll('#qf6 .qf-item');var cur=0;items.forEach(function(it,i){if(it.style.display==='block')cur=i});if(cur<items.length-1){items[cur].style.display='none';items[cur+1].style.display='block';document.getElementById('qf6score').textContent=(cur+2)+' / 6';}">Next Question</button>
    </div>
  </div>
</div>

<!-- SLIDE 165: L6 SPOT THE ERROR -->
<div class="slide slide-light" data-slide="165" data-phase="5" data-lesson="6" data-teacher="<strong>Spot the Error (4 min):</strong> Gabriela identifica o erro PRIMEIRO. Depois clique para revelar. Foco: IT IS (n&atilde;o ARE), February 3RD (n&atilde;o 3 February), a quarter PAST (n&atilde;o a quarter after).">
  <div class="slide-inner">
    <h2 class="slide-heading">Spot the <span class="accent">Error</span></h2>
    <div style="display:flex;flex-direction:column;gap:.8rem;">
      <div class="error-card" onclick="this.classList.toggle('revealed')" style="background:#fff;border:1px solid #e8e4df;border-radius:10px;padding:1rem 1.2rem;cursor:pointer;transition:all .3s;">
        <div class="error-wrong" style="font-size:1rem;color:var(--danger);text-decoration:line-through;">&ldquo;Are three o&rsquo;clock.&rdquo;</div>
        <div class="error-correct" style="display:none;font-size:1rem;color:var(--success);font-weight:700;margin-top:.5rem;">&ldquo;It is three o&rsquo;clock.&rdquo; &mdash; Always use IT IS</div>
      </div>
      <div class="error-card" onclick="this.classList.toggle('revealed')" style="background:#fff;border:1px solid #e8e4df;border-radius:10px;padding:1rem 1.2rem;cursor:pointer;transition:all .3s;">
        <div class="error-wrong" style="font-size:1rem;color:var(--danger);text-decoration:line-through;">&ldquo;My flight is on 3 February.&rdquo;</div>
        <div class="error-correct" style="display:none;font-size:1rem;color:var(--success);font-weight:700;margin-top:.5rem;">&ldquo;My flight is on February 3rd.&rdquo; &mdash; American format: Month + Day</div>
      </div>
      <div class="error-card" onclick="this.classList.toggle('revealed')" style="background:#fff;border:1px solid #e8e4df;border-radius:10px;padding:1rem 1.2rem;cursor:pointer;transition:all .3s;">
        <div class="error-wrong" style="font-size:1rem;color:var(--danger);text-decoration:line-through;">&ldquo;It is quarter after two.&rdquo;</div>
        <div class="error-correct" style="display:none;font-size:1rem;color:var(--success);font-weight:700;margin-top:.5rem;">&ldquo;It is a quarter past two.&rdquo; &mdash; Use A QUARTER PAST</div>
      </div>
      <div class="error-card" onclick="this.classList.toggle('revealed')" style="background:#fff;border:1px solid #e8e4df;border-radius:10px;padding:1rem 1.2rem;cursor:pointer;transition:all .3s;">
        <div class="error-wrong" style="font-size:1rem;color:var(--danger);text-decoration:line-through;">&ldquo;How much costs the ticket?&rdquo;</div>
        <div class="error-correct" style="display:none;font-size:1rem;color:var(--success);font-weight:700;margin-top:.5rem;">&ldquo;How much is the ticket?&rdquo; or &ldquo;How much does the ticket cost?&rdquo;</div>
      </div>
    </div>
  </div>
</div>

<!-- SLIDE 166: L6 ORAL DRILLING -->
<div class="slide slide-light" data-slide="166" data-phase="5" data-lesson="6" data-teacher="<strong>Oral Drilling (5 min):</strong> Leia o hor&aacute;rio na tela. Gabriela diz o tempo em ingl&ecirc;s. 15 segundos por prompt. Se travar: 'Start with IT IS...' Aumente a velocidade progressivamente.">
  <div class="slide-inner">
    <h2 class="slide-heading">Say the <span class="accent">Time</span> Fast!</h2>
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:1rem;margin-top:1.5rem;">
      <div style="background:#fff;border:1px solid #e8e4df;border-radius:10px;padding:1.2rem;text-align:center;font-size:2rem;font-weight:800;color:var(--accent);">3:00</div>
      <div style="background:#fff;border:1px solid #e8e4df;border-radius:10px;padding:1.2rem;text-align:center;font-size:2rem;font-weight:800;color:var(--accent);">7:15</div>
      <div style="background:#fff;border:1px solid #e8e4df;border-radius:10px;padding:1.2rem;text-align:center;font-size:2rem;font-weight:800;color:var(--accent);">10:30</div>
      <div style="background:#fff;border:1px solid #e8e4df;border-radius:10px;padding:1.2rem;text-align:center;font-size:2rem;font-weight:800;color:var(--accent);">4:45</div>
      <div style="background:#fff;border:1px solid #e8e4df;border-radius:10px;padding:1.2rem;text-align:center;font-size:2rem;font-weight:800;color:var(--accent);">12:00 PM</div>
      <div style="background:#fff;border:1px solid #e8e4df;border-radius:10px;padding:1.2rem;text-align:center;font-size:2rem;font-weight:800;color:var(--accent);">12:00 AM</div>
    </div>
  </div>
</div>

<!-- SLIDE 167: L6 CHAPTER 6 TRANSITION -->
<div class="slide slide-image" data-slide="167" data-phase="6" data-lesson="6" data-teacher="<strong>Transi&ccedil;&atilde;o (10s):</strong> 'From guided to free &mdash; show what you learned!' Avance." style="background-image:url('https://images.unsplash.com/photo-1502602898657-3e91760cbb34?w=600&q=80')">
  <div class="slide-inner">
    <div class="chapter-label">Chapter 6</div>
    <h1 class="slide-title">Your <span class="accent">Turn</span></h1>
    <p class="slide-subtitle">From guided to free &mdash; show what you learned</p>
  </div>
</div>

<!-- SLIDE 168: L6 ROLE-PLAY GUIDED -->
<div class="slide slide-dark" data-slide="168" data-phase="6" data-lesson="6" data-teacher="<strong>Role-play Guided (5 min):</strong> Professor = ticket agent no Louvre. Gabriela usa as keywords vis&iacute;veis para montar frases. CCQ: 'How do you ask for the price?' &rarr; 'How much is it?' Se travar: modele a frase e ela repete.">
  <div class="slide-inner">
    <h2 class="slide-heading" style="color:#fff">Role-Play: <span class="accent">Guided</span></h2>
    <div class="roleplay-card" style="background:linear-gradient(135deg,rgba(212,50,106,.15),rgba(212,50,106,.05));border:1px solid rgba(212,50,106,.3);border-radius:12px;padding:1.5rem;">
      <div style="display:flex;align-items:center;gap:.8rem;margin-bottom:1rem;">
        <svg viewBox="0 0 24 24" width="32" height="32" fill="none" stroke="var(--accent)" stroke-width="1.5"><rect x="2" y="7" width="20" height="14" rx="2" ry="2"/><path d="M16 3v4M8 3v4"/><line x1="2" y1="11" x2="22" y2="11"/></svg>
        <div>
          <div style="font-weight:700;font-size:1.1rem;color:#fff;">At the Louvre Ticket Counter</div>
          <div style="font-size:.8rem;color:rgba(255,255,255,.6);">Teacher = Agent &middot; Gabriela = Tourist</div>
        </div>
      </div>
      <p style="color:rgba(255,255,255,.8);font-size:.9rem;margin-bottom:1rem;">Buy a ticket, ask the price, and ask about tour times.</p>
      <div style="display:flex;flex-wrap:wrap;gap:.4rem;">
        <span style="padding:.3rem .8rem;border:1px solid var(--accent);border-radius:20px;font-size:.82rem;color:var(--accent);">one ticket</span>
        <span style="padding:.3rem .8rem;border:1px solid var(--accent);border-radius:20px;font-size:.82rem;color:var(--accent);">how much</span>
        <span style="padding:.3rem .8rem;border:1px solid var(--accent);border-radius:20px;font-size:.82rem;color:var(--accent);">what time</span>
        <span style="padding:.3rem .8rem;border:1px solid var(--accent);border-radius:20px;font-size:.82rem;color:var(--accent);">close</span>
        <span style="padding:.3rem .8rem;border:1px solid var(--accent);border-radius:20px;font-size:.82rem;color:var(--accent);">guided tour</span>
        <span style="padding:.3rem .8rem;border:1px solid var(--accent);border-radius:20px;font-size:.82rem;color:var(--accent);">thank you</span>
      </div>
    </div>
  </div>
</div>

<!-- SLIDE 169: L6 ROLE-PLAY SEMI-FREE -->
<div class="slide slide-dark" data-slide="169" data-phase="6" data-lesson="6" data-teacher="<strong>Role-play Semi-free (5 min):</strong> Professor = ticket agent na Torre Eiffel. MENOS keywords. Gabriela precisa lembrar sozinha. Se travar em 5s, d&ecirc; 1 palavra de pista. CCQ: 'What is the American date format?' &rarr; 'Month + day.' Elogie flu&ecirc;ncia.">
  <div class="slide-inner">
    <h2 class="slide-heading" style="color:#fff">Role-Play: <span class="accent">Semi-Free</span></h2>
    <div class="roleplay-card" style="background:linear-gradient(135deg,rgba(0,48,128,.15),rgba(0,48,128,.05));border:1px solid rgba(0,48,128,.3);border-radius:12px;padding:1.5rem;">
      <div style="display:flex;align-items:center;gap:.8rem;margin-bottom:1rem;">
        <svg viewBox="0 0 24 24" width="32" height="32" fill="none" stroke="var(--accent)" stroke-width="1.5"><path d="M17.8 19.2L16 11l3.5-3.5C21 6 21.5 4 21 3c-1-.5-3 0-4.5 1.5L13 8 4.8 6.2c-.5-.1-.9.1-1.1.5l-.3.5c-.2.4-.1.9.3 1.1l5.1 3 1.5 1.5-3.6 2.4"/></svg>
        <div>
          <div style="font-weight:700;font-size:1.1rem;color:#fff;">At the Eiffel Tower</div>
          <div style="font-size:.8rem;color:rgba(255,255,255,.6);">Less help this time!</div>
        </div>
      </div>
      <p style="color:rgba(255,255,255,.8);font-size:.9rem;margin-bottom:1rem;">Buy a ticket, ask the price, ask when the last elevator goes up, and tell the agent your flight date.</p>
      <div style="display:flex;flex-wrap:wrap;gap:.4rem;">
        <span style="padding:.3rem .8rem;border:1px solid rgba(255,255,255,.3);border-radius:20px;font-size:.82rem;color:rgba(255,255,255,.5);">February 3rd</span>
        <span style="padding:.3rem .8rem;border:1px solid rgba(255,255,255,.3);border-radius:20px;font-size:.82rem;color:rgba(255,255,255,.5);">26 euros</span>
      </div>
    </div>
  </div>
</div>

<!-- SLIDE 170: L6 ROLE-PLAY FREE -->
<div class="slide slide-dark" data-slide="170" data-phase="6" data-lesson="6" data-teacher="<strong>Role-play Free (5 min):</strong> Professor = person&aacute;rio do trem para Versailles. ZERO keywords. Gabriela compra passagem, pergunta hor&aacute;rio de partida, pre&ccedil;o, e diz a data. Delayed feedback: anote erros e corrija DEPOIS. Elogie muito &mdash; ela est&aacute; no n&iacute;vel m&aacute;ximo da aula.">
  <div class="slide-inner">
    <h2 class="slide-heading" style="color:#fff">Role-Play: <span class="accent">Free</span></h2>
    <div class="roleplay-card" style="background:linear-gradient(135deg,rgba(22,163,74,.12),rgba(22,163,74,.04));border:1px solid rgba(22,163,74,.3);border-radius:12px;padding:1.5rem;">
      <div style="display:flex;align-items:center;gap:.8rem;margin-bottom:1rem;">
        <svg viewBox="0 0 24 24" width="32" height="32" fill="none" stroke="#16a34a" stroke-width="1.5"><rect x="1" y="3" width="15" height="13" rx="2"/><path d="M16 8h2a2 2 0 012 2v8a2 2 0 01-2 2H8a2 2 0 01-2-2v-2"/></svg>
        <div>
          <div style="font-weight:700;font-size:1.1rem;color:#fff;">At the Versailles Train Station</div>
          <div style="font-size:.8rem;color:rgba(255,255,255,.6);">No keywords &mdash; you are on your own!</div>
        </div>
      </div>
      <p style="color:rgba(255,255,255,.8);font-size:.9rem;">Buy a train ticket to Versailles. Ask what time the train departs, how much it costs, and tell the agent when you need to return.</p>
    </div>
  </div>
</div>

<!-- SLIDE 171: L6 CHAPTER 7 TRANSITION -->
<div class="slide slide-image" data-slide="171" data-phase="7" data-lesson="6" data-teacher="<strong>Transi&ccedil;&atilde;o (10s):</strong> 'Amazing work today! Let us wrap up.' Avance." style="background-image:url('https://images.unsplash.com/photo-1502602898657-3e91760cbb34?w=600&q=80')">
  <div class="slide-inner">
    <div class="chapter-label">Chapter 7</div>
    <h1 class="slide-title">Wrap-<span class="accent">Up</span></h1>
    <p class="slide-subtitle">Your time survival kit for Paris</p>
  </div>
</div>

<!-- SLIDE 172: L6 SURVIVAL CARD -->
<div class="slide slide-dark" data-slide="172" data-phase="7" data-lesson="6" data-teacher="<strong>Survival Card (2 min):</strong> Leia cada frase com Gabriela. Toque audio. Ela repete 2x cada. Estas 5 frases s&atilde;o as que ela PRECISA em Paris.">
  <div class="slide-inner">
    <h2 class="slide-heading" style="color:#fff">Survival <span class="accent">Card</span></h2>
    <div style="display:flex;flex-direction:column;gap:.6rem;margin-top:1.5rem;">
      <div class="survival-item-ic" style="display:flex;align-items:center;gap:1rem;background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.1);border-radius:10px;padding:.8rem 1rem;">
        <span style="color:var(--accent);font-weight:800;font-size:1.1rem;">1</span>
        <span style="flex:1;font-size:.95rem;">Excuse me, what time is it?</span>
        <button class="audio-btn-sm" onclick="speakText('Excuse me, what time is it?',this)"><svg viewBox="0 0 24 24"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/></svg> Listen</button>
      </div>
      <div class="survival-item-ic" style="display:flex;align-items:center;gap:1rem;background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.1);border-radius:10px;padding:.8rem 1rem;">
        <span style="color:var(--accent);font-weight:800;font-size:1.1rem;">2</span>
        <span style="flex:1;font-size:.95rem;">My flight is on February 3rd.</span>
        <button class="audio-btn-sm" onclick="speakText('My flight is on February 3rd.',this)"><svg viewBox="0 0 24 24"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/></svg> Listen</button>
      </div>
      <div class="survival-item-ic" style="display:flex;align-items:center;gap:1rem;background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.1);border-radius:10px;padding:.8rem 1rem;">
        <span style="color:var(--accent);font-weight:800;font-size:1.1rem;">3</span>
        <span style="flex:1;font-size:.95rem;">One ticket, please. How much is it?</span>
        <button class="audio-btn-sm" onclick="speakText('One ticket, please. How much is it?',this)"><svg viewBox="0 0 24 24"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/></svg> Listen</button>
      </div>
      <div class="survival-item-ic" style="display:flex;align-items:center;gap:1rem;background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.1);border-radius:10px;padding:.8rem 1rem;">
        <span style="color:var(--accent);font-weight:800;font-size:1.1rem;">4</span>
        <span style="flex:1;font-size:.95rem;">The museum opens at ten o&rsquo;clock.</span>
        <button class="audio-btn-sm" onclick="speakText('The museum opens at ten o\\'clock.',this)"><svg viewBox="0 0 24 24"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/></svg> Listen</button>
      </div>
      <div class="survival-item-ic" style="display:flex;align-items:center;gap:1rem;background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.1);border-radius:10px;padding:.8rem 1rem;">
        <span style="color:var(--accent);font-weight:800;font-size:1.1rem;">5</span>
        <span style="flex:1;font-size:.95rem;">It is half past twelve.</span>
        <button class="audio-btn-sm" onclick="speakText('It is half past twelve.',this)"><svg viewBox="0 0 24 24"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/></svg> Listen</button>
      </div>
    </div>
  </div>
</div>

<!-- SLIDE 173: L6 CHECKLIST -->
<div class="slide slide-dark" data-slide="173" data-phase="7" data-lesson="6" data-teacher="<strong>What I Learned (2 min):</strong> Gabriela leia cada item em voz alta. Se disser 'sim, eu sei fazer isso' para TODAS &mdash; a li&ccedil;&atilde;o est&aacute; dominada. Marque os checks juntos. 5/5 = aula conclu&iacute;da no sistema.">
  <div class="slide-inner">
    <h2 class="slide-heading" style="color:#fff">What I <span class="accent">Learned</span></h2>
    <ul class="checklist" id="checklist-6" style="list-style:none;display:flex;flex-direction:column;gap:.6rem;margin-top:1.5rem;">
      <li style="display:flex;align-items:center;gap:.8rem;background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.1);border-radius:8px;padding:.7rem 1rem;cursor:pointer;" onclick="this.querySelector('input').click()">
        <input type="checkbox" onchange="toggleChecklist(this)" style="width:20px;height:20px;accent-color:var(--accent);">
        <span style="font-size:.9rem;">I can tell the time in English (o&rsquo;clock, quarter past, half past, quarter to).</span>
      </li>
      <li style="display:flex;align-items:center;gap:.8rem;background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.1);border-radius:8px;padding:.7rem 1rem;cursor:pointer;" onclick="this.querySelector('input').click()">
        <input type="checkbox" onchange="toggleChecklist(this)" style="width:20px;height:20px;accent-color:var(--accent);">
        <span style="font-size:.9rem;">I can say dates in American English (February 3rd, 2027).</span>
      </li>
      <li style="display:flex;align-items:center;gap:.8rem;background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.1);border-radius:8px;padding:.7rem 1rem;cursor:pointer;" onclick="this.querySelector('input').click()">
        <input type="checkbox" onchange="toggleChecklist(this)" style="width:20px;height:20px;accent-color:var(--accent);">
        <span style="font-size:.9rem;">I can ask &ldquo;How much is it?&rdquo; and &ldquo;What time is it?&rdquo;</span>
      </li>
      <li style="display:flex;align-items:center;gap:.8rem;background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.1);border-radius:8px;padding:.7rem 1rem;cursor:pointer;" onclick="this.querySelector('input').click()">
        <input type="checkbox" onchange="toggleChecklist(this)" style="width:20px;height:20px;accent-color:var(--accent);">
        <span style="font-size:.9rem;">I can buy a ticket at a museum or monument in Paris.</span>
      </li>
      <li style="display:flex;align-items:center;gap:.8rem;background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.1);border-radius:8px;padding:.7rem 1rem;cursor:pointer;" onclick="this.querySelector('input').click()">
        <input type="checkbox" onchange="toggleChecklist(this)" style="width:20px;height:20px;accent-color:var(--accent);">
        <span style="font-size:.9rem;">I know the vocabulary: o&rsquo;clock, quarter, half past, noon, midnight, flight, ticket, price.</span>
      </li>
    </ul>
  </div>
</div>

<!-- SLIDE 174: L6 BADGE -->
<div class="slide slide-dark" data-slide="174" data-phase="7" data-lesson="6" data-teacher="<strong>Badge (1 min):</strong> 'You earned your Time Traveler Stamp!' Confetti. Energia alta. Preview: pr&oacute;xima aula sobre pa&iacute;ses e nacionalidades. Diga o homework ORALMENTE: 1) Escrever o 'Dream Paris Itinerary' para 5 dias com hor&aacute;rios e datas em ingl&ecirc;s americano. 2) Praticar dizendo as horas por 5 min olhando o rel&oacute;gio. 3) Assistir v&iacute;deo YouTube 'Telling Time in English' e anotar 3 express&otilde;es novas.">
  <div class="slide-inner">
    <div class="badge-card">
      <div class="badge-icon">
        <div class="sparkles"><div class="sparkle"></div><div class="sparkle"></div><div class="sparkle"></div><div class="sparkle"></div><div class="sparkle"></div><div class="sparkle"></div></div>
        <div class="badge-circle"><svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg></div>
      </div>
      <h2 class="slide-heading">Time Traveler <span class="accent">Stamp</span>!</h2>
      <p style="color:rgba(255,255,255,.7);font-size:1rem">Day 6: Numbers, Time &amp; Dates &mdash; Complete</p>
    </div>
  </div>
</div>

<!-- SLIDE 175: L6 CLOSING -->
<div class="slide slide-dark" data-slide="175" data-phase="7" data-lesson="6" data-teacher="<strong>Fechamento (1 min):</strong> 'Pr&oacute;xima aula: pa&iacute;ses e nacionalidades! See you!' Diga o homework ORALMENTE.">
  <div class="slide-inner" style="text-align:center">
    <div class="chapter-label">Coming Up Next</div>
    <h2 class="slide-heading">Lesson 7: <span class="accent">Where Are You From?</span></h2>
    <p style="color:rgba(255,255,255,.6);font-size:1rem;margin-top:1rem">Countries, nationalities, and the world around Gabriela</p>
    <p style="color:rgba(255,255,255,.4);font-size:.85rem;margin-top:2rem">Day 6 &mdash; Complete</p>
  </div>
</div>
'''

# ============================================================
# COMPLEMENTARY CONTENT FOR AULA 6
# ============================================================
COMPLEMENTARY_HTML = '''
<h3 style="font-family:'Cormorant Garamond',serif;font-size:1.3rem;font-weight:600;color:var(--accent);margin:2rem 0 1rem;">Aula 6 &mdash; Numbers, Time &amp; Dates</h3>
<div class="media-grid" style="margin-bottom:2rem;">
  <div class="media-card-wrapper" data-media="l6-series">
    <label class="media-check"><input type="checkbox" onchange="toggleMediaDone(this)"></label>
    <div class="media-card">
      <div class="media-thumb series"></div>
      <div class="media-info">
        <div class="media-type">S&eacute;rie</div>
        <h5>Emily in Paris &mdash; S01E01 (Netflix)</h5>
        <p>Emily chega a Paris e precisa lidar com hor&aacute;rios, compromissos e compras. Vocabul&aacute;rio de viagem perfeito para esta aula.</p>
        <div class="media-tip">Foco: anote toda vez que algu&eacute;m diz um hor&aacute;rio ou pre&ccedil;o em ingl&ecirc;s. Pausa e repita.</div>
      </div>
    </div>
  </div>
  <div class="media-card-wrapper" data-media="l6-youtube">
    <label class="media-check"><input type="checkbox" onchange="toggleMediaDone(this)"></label>
    <div class="media-card">
      <div class="media-thumb youtube"></div>
      <div class="media-info">
        <div class="media-type">YouTube</div>
        <h5>Telling Time in English &mdash; English with Lucy</h5>
        <p>V&iacute;deo curto e did&aacute;tico sobre como dizer as horas em ingl&ecirc;s americano. Perfeito para refor&ccedil;ar a aula.</p>
        <div class="media-tip">Assista 1x e anote 3 express&otilde;es de tempo que voc&ecirc; n&atilde;o conhecia.</div>
      </div>
    </div>
  </div>
  <div class="media-card-wrapper" data-media="l6-podcast">
    <label class="media-check"><input type="checkbox" onchange="toggleMediaDone(this)"></label>
    <div class="media-card">
      <div class="media-thumb podcast"></div>
      <div class="media-info">
        <div class="media-type">Atividade</div>
        <h5>Clock Challenge &mdash; 5 minutos por dia</h5>
        <p>A cada hora do dia, olhe o rel&oacute;gio e diga as horas em ingl&ecirc;s. Fa&ccedil;a por 3 dias seguidos.</p>
        <div class="media-tip">Se n&atilde;o lembrar, consulte o Survival Card da Aula 6.</div>
      </div>
    </div>
  </div>
</div>'''

# ============================================================
# IN CLASS MENU CARD
# ============================================================
INCLASS_MENU_CARD = '''
<div class="inclass-lesson-card" onclick="startLesson(6)">
  <div class="ilc-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg></div>
  <div class="ilc-info">
    <div class="ilc-number">Lesson 06</div>
    <div class="ilc-title">Numbers, Time &amp; Dates</div>
    <div class="ilc-desc">Telling time + dates + prices &mdash; Paris survival &mdash; 60 min &mdash; 29 slides</div>
  </div>
  <div class="ilc-arrow">&rarr;</div>
</div>
'''

# ============================================================
# MAIN BUILD LOGIC
# ============================================================
def patch_file(filepath, is_aluno=False):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Add audioMap entries (before the first existing entry)
    audio_entries = build_audiomap_entries()
    # Find first entry in audioMap and add before it
    marker = '"A gap year sounds amazing."'
    if marker in html:
        html = html.replace(marker, audio_entries + ',\n  ' + marker)

    # Also add entries that might use escaped apostrophes
    extra_entries = '''  "Hi, my name is Gabriela. My flight arrived on February 3rd. One ticket, please. How much is it? What time does the tower close?": "/audio/gabriela-pires/hi_my_name_is_gabriela_my_flight_arrived_on_february_3rd.mp3?v=2",
  "We close at six o'clock.": "/audio/gabriela-pires/we_close_at_six_oclock.mp3?v=2",
  "And what time is the next guided tour?": "/audio/gabriela-pires/and_what_time_is_the_next_guided_tour.mp3?v=2",
  "Thank you! What time does the museum close?": "/audio/gabriela-pires/thank_you_what_time_does_the_museum_close.mp3?v=2",
  "One student ticket, please. How much is it?": "/audio/gabriela-pires/one_student_ticket_please_how_much_is_it_dialogue.mp3?v=2",
  "The next tour starts at a quarter past three. It is in English.": "/audio/gabriela-pires/the_next_tour_starts_at_a_quarter_past_three_in_english.mp3?v=2",
  "It is 15 euros. Here is your ticket.": "/audio/gabriela-pires/it_is_15_euros_here_is_your_ticket.mp3?v=2"'''
    html = html.replace(audio_entries + ',\n  ' + marker,
                        audio_entries + ',\n' + extra_entries + ',\n  ' + marker)

    # 2. Replace Aula 6 placeholder in Pre-class
    old_placeholder = '''<div class="lesson-card">
  <div class="lesson-header" onclick="toggleLesson(this)">
    <div class="lesson-header-img" style="background-image:url('https://images.unsplash.com/photo-1502602898657-3e91760cbb34?w=600&q=80');opacity:0.35;"></div>
    <div class="lesson-header-content">
      <div class="lesson-number">Aula 06 &mdash; Pre-class</div>
      <h3 style="opacity:0.7;">Numbers, Time &amp; Dates &mdash; Tools to Survive in Paris</h3>
      <div class="lesson-desc" style="font-style:italic;color:var(--text-dim);">Conte&uacute;do ser&aacute; adicionado no pr&oacute;ximo bloco.</div>
    </div>
    <div class="expand-icon">&#9660;</div>
  </div>
  <div class="lesson-body"><p style="text-align:center;padding:2rem;color:var(--text-dim);font-style:italic;">Conte&uacute;do ser&aacute; adicionado no pr&oacute;ximo bloco.</p></div>
</div>'''

    # Try different HTML entity encodings
    for variant in [old_placeholder,
                    old_placeholder.replace('&mdash;', '—').replace('&amp;', '&'),
                    old_placeholder.replace('Conte&uacute;do', 'Conteúdo').replace('ser&aacute;', 'será').replace('pr&oacute;ximo', 'próximo')]:
        if variant in html:
            html = html.replace(variant, PRECLASS_HTML)
            print(f"  [OK] Replaced Aula 6 placeholder in Pre-class")
            break
    else:
        # Try a simpler match
        import re
        pattern = r'<div class="lesson-card">\s*<div class="lesson-header"[^>]*onclick="toggleLesson\(this\)">\s*<div class="lesson-header-img"[^>]*opacity:0\.35[^>]*></div>\s*<div class="lesson-header-content">\s*<div class="lesson-number">Aula 06[^<]*</div>'
        match = re.search(pattern, html)
        if match:
            # Find the full block
            start = match.start()
            # Find the closing </div> of this lesson-card
            depth = 0
            i = start
            found_end = False
            while i < len(html):
                if html[i:i+4] == '<div':
                    depth += 1
                elif html[i:i+6] == '</div>':
                    depth -= 1
                    if depth == 0:
                        end = i + 6
                        html = html[:start] + PRECLASS_HTML + html[end:]
                        print(f"  [OK] Replaced Aula 6 placeholder via regex")
                        found_end = True
                        break
                i += 1
            if not found_end:
                print("  [WARN] Could not find end of Aula 6 placeholder")
        else:
            print("  [WARN] Could not find Aula 6 placeholder")

    # 3. Insert slides before </div><!-- /slides-container -->
    if not is_aluno:
        slide_marker = '</div><!-- /slides-container -->'
        if slide_marker in html:
            html = html.replace(slide_marker, SLIDES_HTML + '\n' + slide_marker)
            print(f"  [OK] Inserted {SLIDES_HTML.count('data-slide=')} slides")
        else:
            # Try variant
            for m in ['</div><!-- /slides-container', '</div>\n\n<!-- Navigation Bar']:
                if m in html:
                    html = html.replace(m, SLIDES_HTML + '\n' + m)
                    print(f"  [OK] Inserted slides (variant marker)")
                    break

    # 4. Update lessonRanges
    if not is_aluno:
        old_ranges = "var lessonRanges = {1:[1,28], 2:[29,55], 3:[56,85], 4:[86,115], 5:[116,146]};"
        new_ranges = "var lessonRanges = {1:[1,28], 2:[29,55], 3:[56,85], 4:[86,115], 5:[116,146], 6:[147,175]};"
        if old_ranges in html:
            html = html.replace(old_ranges, new_ranges)
            print(f"  [OK] Updated lessonRanges")

    # 5. Update totalSlides
    if not is_aluno:
        html = html.replace('var totalSlides = 146;', 'var totalSlides = 175;')
        print(f"  [OK] Updated totalSlides")

    # 6. Add IN CLASS menu card
    if not is_aluno:
        menu_marker = '<div style="background:var(--bg-card);border:1px solid var(--border);padding:2rem;border-radius:6px;text-align:center;margin-top:2rem;">'
        if menu_marker in html:
            html = html.replace(menu_marker, INCLASS_MENU_CARD + '\n' + menu_marker)
            print(f"  [OK] Added IN CLASS menu card")

    # 7. Add Complementary content
    comp_marker = '<h3 style="font-family:\'Cormorant Garamond\',serif;font-size:1.3rem;font-weight:600;color:var(--accent);margin-bottom:1rem;">Paris &amp; Viagem 2027</h3>'
    if comp_marker in html:
        html = html.replace(comp_marker, COMPLEMENTARY_HTML + '\n' + comp_marker)
        print(f"  [OK] Added Complementary content")
    else:
        # Try alternate
        comp_marker2 = 'Paris &amp; Viagem 2027'
        if comp_marker2 in html:
            idx = html.index(comp_marker2)
            # Find the h3 tag start before it
            h3_start = html.rfind('<h3', 0, idx)
            if h3_start > 0:
                html = html[:h3_start] + COMPLEMENTARY_HTML + '\n' + html[h3_start:]
                print(f"  [OK] Added Complementary content (variant)")

    # 8. Fix Aula 5 closing slide preview (if wrong)
    if not is_aluno:
        html = html.replace(
            'Lesson 6: <span class="accent">I Can Do It!</span></h2>\n    <p style="color:rgba(255,255,255,.6);font-size:1rem;margin-top:1rem">Abilities, talents, and what you can do',
            'Lesson 6: <span class="accent">Numbers, Time &amp; Dates</span></h2>\n    <p style="color:rgba(255,255,255,.6);font-size:1rem;margin-top:1rem">The tools you need to survive in Paris'
        )

    # 9. Update progress tracking
    html = html.replace("var totalLessons = 5;", "var totalLessons = 6;", 1)
    # Keep the rest at 5 if they exist for block calculations

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"  [DONE] Saved {filepath}")

if __name__ == '__main__':
    print("=== Building Gabriela Pires - Aula 6 ===")

    print("\n[1/2] Patching PROFESSOR file...")
    patch_file(PROF, is_aluno=False)

    print("\n[2/2] Patching ALUNO file...")
    patch_file(ALUNO, is_aluno=True)

    print("\n=== Build complete ===")
