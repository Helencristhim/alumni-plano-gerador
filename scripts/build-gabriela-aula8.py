#!/usr/bin/env python3
"""
Build Gabriela Pires - Aula 8: Can You Do That? — Abilities, Possibilities & Asking for Help
Inserts Pre-class, IN CLASS slides, Complementary, and audioMap into both professor and aluno files.
"""
import re, os

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROF = os.path.join(BASE, 'public', 'professor', 'gabriela-pires.html')
ALUNO = os.path.join(BASE, 'public', 'aluno', 'gabriela-pires.html')

# ============================================================
# AULA 8 AUDIO MAP ENTRIES
# ============================================================
AULA8_AUDIO = {
  "Speak": "speak",
  "I can speak English.": "i_can_speak_english",
  "Understand": "understand",
  "I can understand you.": "i_can_understand_you",
  "Help": "help",
  "Can you help me?": "can_you_help_me",
  "Repeat": "repeat",
  "Can you repeat that, please?": "can_you_repeat_that_please",
  "Find": "find",
  "I can't find my hotel.": "i_cant_find_my_hotel",
  "Show": "show",
  "Can you show me on the map?": "can_you_show_me_on_the_map",
  "Slower": "slower",
  "Can you speak slower, please?": "can_you_speak_slower_please",
  "Map": "map",
  "Do you have a map?": "do_you_have_a_map",
  "I can speak English.": "i_can_speak_english",
  "I can't drive.": "i_cant_drive",
  "Can you help me?": "can_you_help_me",
  "Yes, I can.": "yes_i_can",
  "No, I can't.": "no_i_cant",
  "Could you help me, please?": "could_you_help_me_please",
  "I can't find my hotel.": "i_cant_find_my_hotel",
  "Can you speak slower, please?": "can_you_speak_slower_please",
  "Can you show me on the map?": "can_you_show_me_on_the_map",
  "I can speak English.": "i_can_speak_english",
  "Excuse me, can you help me?": "excuse_me_can_you_help_me",
  "I am lost. I can't find my hotel.": "i_am_lost_i_cant_find_my_hotel",
  "What is the name of your hotel?": "what_is_the_name_of_your_hotel",
  "It is Hotel Le Marais. Can you show me on the map?": "it_is_hotel_le_marais_can_you_show_me_on_the_map",
  "Of course! It is here. You can walk. It is five minutes.": "of_course_it_is_here_you_can_walk",
  "Can you repeat that? Slower, please.": "can_you_repeat_that_slower_please",
  "Yes! Walk straight. Turn left. Your hotel is on the right.": "yes_walk_straight_turn_left",
  "Thank you so much! I can find it now.": "thank_you_so_much_i_can_find_it_now",
  "You are welcome! Your English is very good!": "you_are_welcome_your_english_is_very_good",
  "Gabriela is walking in Paris. It is her second day. She can't find her hotel. She is lost. She can speak English, but she can't speak French. She sees a man near the metro station. She asks: Can you help me? The man says: Yes, I can. What is the problem? Gabriela says: I can't find my hotel. Can you show me on the map? The man shows the map. He speaks fast. Gabriela says: Can you speak slower, please? He speaks slower. Now Gabriela can understand. She can find her hotel. She says: Thank you! I can walk from here.": "gabriela_lost_in_paris_listening_full",
  "Can Gabriela speak French?": "can_gabriela_speak_french",
  "What can't Gabriela find?": "what_cant_gabriela_find",
  "What does Gabriela ask the man to do?": "what_does_gabriela_ask_the_man",
  "Hi, I am lost. Can you help me? I can't find the Eiffel Tower. Can you show me on the map?": "hi_i_am_lost_can_you_help_me_eiffel",
  "Excuse me. I can't understand the menu. Can you help me? Can you speak slower?": "excuse_me_i_cant_understand_the_menu",
  "Hello. I can't find the metro station. Can you show me? I can speak English.": "hello_i_cant_find_the_metro_station",
  "Can you help me, please?": "can_you_help_me_please",
  "I can't find my hotel.": "i_cant_find_my_hotel_survival",
  "Can you speak slower, please?": "can_you_speak_slower_please_survival",
  "Can you show me on the map?": "can_you_show_me_on_the_map_survival",
  "I can speak English.": "i_can_speak_english_survival",
  "I can swim.": "i_can_swim",
  "She can't cook.": "she_cant_cook",
  "Can he play guitar?": "can_he_play_guitar",
  "They can't speak Japanese.": "they_cant_speak_japanese",
  "I can to speak English.": "i_can_to_speak_english_wrong",
  "I can speak English.": "i_can_speak_english_correct",
  "Can you speaking?": "can_you_speaking_wrong",
  "Can you speak?": "can_you_speak_correct",
}

# Build audioMap JS entries
def build_audiomap_entries():
    lines = []
    seen = set()
    for phrase, slug in AULA8_AUDIO.items():
        key = f"{phrase}|{slug}"
        if key in seen:
            continue
        seen.add(key)
        escaped = phrase.replace("'", "\\'")
        lines.append(f'  "{escaped}": "/audio/gabriela-pires/{slug}.mp3?v=2"')
    return ',\n'.join(lines)

# ============================================================
# AULA 8 PRE-CLASS HTML
# ============================================================
PRECLASS_HTML = '''<div class="lesson-card" id="ex-lesson-8">
  <div class="lesson-header" onclick="toggleLesson(this)">
    <div class="lesson-header-img" style="background-image:url('https://images.unsplash.com/photo-1499856871958-5b9627545d1a?w=600&q=80')"></div>
    <div class="lesson-header-content">
      <div class="lesson-number">Aula 08 &mdash; Pre-class</div>
      <h3>Can You Do That? &mdash; Abilities, Possibilities &amp; Asking for Help</h3>
      <div class="lesson-desc">Depois desta aula, voc&ecirc; consegue pedir ajuda, dizer o que pode e n&atilde;o pode fazer, e sobreviver em situa&ccedil;&otilde;es de emerg&ecirc;ncia em Paris.</div>
      <div class="lesson-progress-mini"><div class="mini-bar"><div class="mini-bar-fill" data-lesson-progress="8" style="width:0%"></div></div><span class="mini-percent" data-lesson-pct="8">0%</span></div>
    </div>
    <div class="expand-icon">&#9660;</div>
  </div>
  <div class="lesson-body">
    <p style="font-size:0.85rem;color:var(--text-mid);margin-bottom:1.5rem;"><strong style="color:var(--accent);">Objetivo:</strong> Ao final desta aula, Gabriela ser&aacute; capaz de usar &ldquo;can&rdquo; e &ldquo;can&rsquo;t&rdquo; para falar sobre habilidades, pedir ajuda e usar frases de sobreviv&ecirc;ncia em Paris.</p>

    <!-- ===== STAGE 1.1: VOCABULARY CARDS ===== -->
    <div class="exercise-section">
      <div class="section-header-row">
        <h4>Vocabul&aacute;rio <span class="badge badge-vocab">Vocabulary</span></h4>
        <button class="listen-all-btn" onclick="listenAllVocab(this)">&#9654; Ouvir todos</button>
      </div>
      <p class="microcopy">Olha a palavra, a tradu&ccedil;&atilde;o e o exemplo juntos. Toca em Ouvir &mdash; o som ajuda muito a mem&oacute;ria.</p>

      <div class="vocab-card">
        <div class="vocab-word">Speak</div>
        <div class="vocab-translation">falar</div>
        <div class="vocab-example">&ldquo;I <strong>can speak</strong> English.&rdquo;</div>
        <button class="audio-btn" onclick="speakText('I can speak English.', this)">&#9654; Ouvir</button>
      </div>
      <div class="vocab-card">
        <div class="vocab-word">Understand</div>
        <div class="vocab-translation">entender</div>
        <div class="vocab-example">&ldquo;I can <strong>understand</strong> you.&rdquo;</div>
        <button class="audio-btn" onclick="speakText('I can understand you.', this)">&#9654; Ouvir</button>
      </div>
      <div class="vocab-card">
        <div class="vocab-word">Help</div>
        <div class="vocab-translation">ajudar</div>
        <div class="vocab-example">&ldquo;Can you <strong>help</strong> me?&rdquo;</div>
        <button class="audio-btn" onclick="speakText('Can you help me?', this)">&#9654; Ouvir</button>
      </div>
      <div class="vocab-card">
        <div class="vocab-word">Repeat</div>
        <div class="vocab-translation">repetir</div>
        <div class="vocab-example">&ldquo;Can you <strong>repeat</strong> that, please?&rdquo;</div>
        <button class="audio-btn" onclick="speakText('Can you repeat that, please?', this)">&#9654; Ouvir</button>
      </div>
      <div class="vocab-card">
        <div class="vocab-word">Find</div>
        <div class="vocab-translation">encontrar</div>
        <div class="vocab-example">&ldquo;I can&rsquo;t <strong>find</strong> my hotel.&rdquo;</div>
        <button class="audio-btn" onclick="speakText('I can\\'t find my hotel.', this)">&#9654; Ouvir</button>
      </div>
      <div class="vocab-card">
        <div class="vocab-word">Show</div>
        <div class="vocab-translation">mostrar</div>
        <div class="vocab-example">&ldquo;Can you <strong>show</strong> me on the map?&rdquo;</div>
        <button class="audio-btn" onclick="speakText('Can you show me on the map?', this)">&#9654; Ouvir</button>
      </div>
      <div class="vocab-card">
        <div class="vocab-word">Slower</div>
        <div class="vocab-translation">mais devagar</div>
        <div class="vocab-example">&ldquo;Can you speak <strong>slower</strong>, please?&rdquo;</div>
        <button class="audio-btn" onclick="speakText('Can you speak slower, please?', this)">&#9654; Ouvir</button>
      </div>
      <div class="vocab-card">
        <div class="vocab-word">Map</div>
        <div class="vocab-translation">mapa</div>
        <div class="vocab-example">&ldquo;Do you have a <strong>map</strong>?&rdquo;</div>
        <button class="audio-btn" onclick="speakText('Do you have a map?', this)">&#9654; Ouvir</button>
      </div>
    </div>

    <!-- ===== STAGE 1.2: MATCHING ===== -->
    <div class="exercise-section">
      <h4>V2. Match the words <span class="badge badge-vocab">Matching</span></h4>
      <p class="microcopy">Fa&ccedil;a um de cada vez. Errou? Leia a explica&ccedil;&atilde;o com calma &mdash; &eacute; a&iacute; que voc&ecirc; aprende de verdade.</p>
      <div class="match-grid" id="match-l8">
        <div class="match-row" data-answer="falar">
          <span class="match-word">Speak</span>
          <select onchange="checkMatch(this)">
            <option value="">Select...</option>
            <option value="entender">entender</option>
            <option value="mapa">mapa</option>
            <option value="falar">falar</option>
            <option value="ajudar">ajudar</option>
            <option value="repetir">repetir</option>
          </select>
        </div>
        <div class="match-row" data-answer="entender">
          <span class="match-word">Understand</span>
          <select onchange="checkMatch(this)">
            <option value="">Select...</option>
            <option value="mostrar">mostrar</option>
            <option value="entender">entender</option>
            <option value="falar">falar</option>
            <option value="mais devagar">mais devagar</option>
            <option value="encontrar">encontrar</option>
          </select>
        </div>
        <div class="match-row" data-answer="ajudar">
          <span class="match-word">Help</span>
          <select onchange="checkMatch(this)">
            <option value="">Select...</option>
            <option value="mapa">mapa</option>
            <option value="repetir">repetir</option>
            <option value="encontrar">encontrar</option>
            <option value="ajudar">ajudar</option>
            <option value="falar">falar</option>
          </select>
        </div>
        <div class="match-row" data-answer="repetir">
          <span class="match-word">Repeat</span>
          <select onchange="checkMatch(this)">
            <option value="">Select...</option>
            <option value="ajudar">ajudar</option>
            <option value="mais devagar">mais devagar</option>
            <option value="repetir">repetir</option>
            <option value="entender">entender</option>
            <option value="mostrar">mostrar</option>
          </select>
        </div>
        <div class="match-row" data-answer="encontrar">
          <span class="match-word">Find</span>
          <select onchange="checkMatch(this)">
            <option value="">Select...</option>
            <option value="falar">falar</option>
            <option value="encontrar">encontrar</option>
            <option value="ajudar">ajudar</option>
            <option value="mapa">mapa</option>
            <option value="repetir">repetir</option>
          </select>
        </div>
        <div class="match-row" data-answer="mostrar">
          <span class="match-word">Show</span>
          <select onchange="checkMatch(this)">
            <option value="">Select...</option>
            <option value="mais devagar">mais devagar</option>
            <option value="encontrar">encontrar</option>
            <option value="falar">falar</option>
            <option value="mostrar">mostrar</option>
            <option value="entender">entender</option>
          </select>
        </div>
        <div class="match-row" data-answer="mais devagar">
          <span class="match-word">Slower</span>
          <select onchange="checkMatch(this)">
            <option value="">Select...</option>
            <option value="repetir">repetir</option>
            <option value="mais devagar">mais devagar</option>
            <option value="mapa">mapa</option>
            <option value="ajudar">ajudar</option>
            <option value="mostrar">mostrar</option>
          </select>
        </div>
        <div class="match-row" data-answer="mapa">
          <span class="match-word">Map</span>
          <select onchange="checkMatch(this)">
            <option value="">Select...</option>
            <option value="encontrar">encontrar</option>
            <option value="entender">entender</option>
            <option value="mapa">mapa</option>
            <option value="falar">falar</option>
            <option value="mais devagar">mais devagar</option>
          </select>
        </div>
      </div>
      <button class="verify-all-btn" onclick="verifyAllMatches('match-l8')">Check Answers</button>
    </div>

    <!-- ===== STAGE 1.3: GRAMMAR IN CONTEXT ===== -->
    <div class="exercise-section">
      <h4>Stage 1.2: Grammar in Context <span class="badge badge-practice">Grammar</span></h4>
      <p class="microcopy">Leia o texto com calma. As palavras em negrito s&atilde;o do vocabul&aacute;rio de hoje.</p>
      <div class="context-text" style="background:var(--accent-dim);border:1px solid rgba(212,50,106,0.15);border-radius:8px;padding:1.2rem;margin-bottom:1.2rem;line-height:1.9;font-size:0.95rem;">
        Gabriela is walking in Paris. It is her second day. She <strong>can speak</strong> English, but she <strong>can&rsquo;t speak</strong> French. She is lost! She <strong>can&rsquo;t find</strong> her hotel. She sees a man near the metro. She asks: &ldquo;<strong>Can</strong> you <strong>help</strong> me?&rdquo; The man says: &ldquo;Yes, I <strong>can</strong>!&rdquo; Gabriela says: &ldquo;I <strong>can&rsquo;t find</strong> my hotel. <strong>Can</strong> you <strong>show</strong> me on the <strong>map</strong>?&rdquo; The man speaks fast. Gabriela says: &ldquo;<strong>Can</strong> you <strong>speak slower</strong>, please?&rdquo; He <strong>repeats</strong> slowly. Now Gabriela <strong>can understand</strong>! She says: &ldquo;Thank you! I <strong>can find</strong> it now!&rdquo;
      </div>
      <div class="quiz-item">
        <div class="quiz-question">Can Gabriela speak French?</div>
        <div class="quiz-options">
          <div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> Yes, she can.</div>
          <div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> No, she can&rsquo;t.</div>
          <div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> She speaks a little French.</div>
        </div>
      </div>
      <div class="quiz-item">
        <div class="quiz-question">What can&rsquo;t Gabriela find?</div>
        <div class="quiz-options">
          <div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> The metro station</div>
          <div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> Her hotel</div>
          <div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> A restaurant</div>
        </div>
      </div>
      <div class="quiz-item">
        <div class="quiz-question">What does Gabriela ask the man to do?</div>
        <div class="quiz-options">
          <div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> Walk with her to the hotel</div>
          <div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> Show her on the map and speak slower</div>
          <div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> Call a taxi</div>
        </div>
      </div>
    </div>

    <!-- ===== STAGE 1.4: GRAMMAR TIP ===== -->
    <div class="exercise-section">
      <h4>Grammar Tip <span class="badge badge-practice">Grammar</span></h4>
      <div style="background:var(--accent-dim);border:1px solid rgba(212,50,106,0.15);border-radius:8px;padding:1.2rem;margin-bottom:1rem;">
        <p style="font-weight:700;color:var(--accent);margin-bottom:0.8rem;font-size:1rem;">Modal Verb CAN / O verbo modal CAN</p>
        <table style="width:100%;border-collapse:collapse;font-size:0.9rem;">
          <tr style="border-bottom:1px solid var(--border);"><td style="padding:0.5rem;font-weight:600;">Afirmativa</td><td style="padding:0.5rem;">I <strong>can speak</strong> English.</td><td style="padding:0.5rem;color:var(--text-dim);">Eu sei/consigo falar ingl&ecirc;s.</td></tr>
          <tr style="border-bottom:1px solid var(--border);"><td style="padding:0.5rem;font-weight:600;">Negativa</td><td style="padding:0.5rem;">I <strong>can&rsquo;t find</strong> my hotel.</td><td style="padding:0.5rem;color:var(--text-dim);">Eu n&atilde;o consigo encontrar meu hotel.</td></tr>
          <tr style="border-bottom:1px solid var(--border);"><td style="padding:0.5rem;font-weight:600;">Pergunta</td><td style="padding:0.5rem;"><strong>Can</strong> you <strong>help</strong> me?</td><td style="padding:0.5rem;color:var(--text-dim);">Voc&ecirc; pode me ajudar?</td></tr>
          <tr style="border-bottom:1px solid var(--border);"><td style="padding:0.5rem;font-weight:600;">Resp. curta (+)</td><td style="padding:0.5rem;">Yes, I <strong>can</strong>.</td><td style="padding:0.5rem;color:var(--text-dim);">Sim, eu posso.</td></tr>
          <tr style="border-bottom:1px solid var(--border);"><td style="padding:0.5rem;font-weight:600;">Resp. curta (&minus;)</td><td style="padding:0.5rem;">No, I <strong>can&rsquo;t</strong>.</td><td style="padding:0.5rem;color:var(--text-dim);">N&atilde;o, eu n&atilde;o posso.</td></tr>
          <tr><td style="padding:0.5rem;font-weight:600;">Pedido educado</td><td style="padding:0.5rem;"><strong>Could</strong> you help me, <strong>please</strong>?</td><td style="padding:0.5rem;color:var(--text-dim);">Voc&ecirc; poderia me ajudar, por favor?</td></tr>
        </table>
      </div>
      <div style="background:var(--accent-dim);border:1px solid rgba(212,50,106,0.15);border-radius:8px;padding:1.2rem;">
        <p style="font-weight:700;color:var(--accent);margin-bottom:0.8rem;font-size:1rem;">Regras importantes / Important rules</p>
        <ul style="font-size:0.88rem;line-height:1.8;padding-left:1.2rem;color:var(--text-mid);">
          <li><strong>CAN + verbo BASE</strong> (sem &ldquo;to&rdquo;!): I can speak &mdash; NUNCA &ldquo;I can to speak&rdquo;</li>
          <li><strong>CAN n&atilde;o muda</strong> com he/she: She <strong>can</strong> swim (nunca &ldquo;she cans&rdquo;)</li>
          <li><strong>CAN&rsquo;T</strong> = cannot (pron&uacute;ncia: /k&aelig;nt/ &mdash; vogal curta)</li>
          <li><strong>COULD</strong> = mais educado que CAN para pedidos</li>
          <li>Pergunta: <strong>CAN + sujeito + verbo</strong> (Can you help me?)</li>
        </ul>
      </div>
    </div>

    <!-- ===== STAGE 1.5: FILL-IN-THE-BLANK ===== -->
    <div class="exercise-section">
      <h4>P1. Complete with the correct word <span class="badge badge-practice">Practice</span></h4>
      <p class="microcopy">Fa&ccedil;a um de cada vez. Errou? Leia a dica com calma.</p>

      <div class="fill-blank-item">
        <div class="fill-blank-sentence">
          &ldquo;I
          <input class="blank-input" data-answer="can" data-hint="Hint: the modal verb for ability" data-phrase="I can speak English." placeholder="___">
          speak English.&rdquo;
        </div>
        <button class="check-btn" onclick="checkBlank(this)">Check</button>
        <button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button>
      </div>

      <div class="fill-blank-item">
        <div class="fill-blank-sentence">
          &ldquo;I
          <input class="blank-input" data-answer="can't" data-alt="cannot" data-hint="Hint: negative of can" data-phrase="I can't find my hotel." placeholder="___">
          find my hotel.&rdquo;
        </div>
        <button class="check-btn" onclick="checkBlank(this)">Check</button>
        <button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button>
      </div>

      <div class="fill-blank-item">
        <div class="fill-blank-sentence">
          &ldquo;Can you
          <input class="blank-input" data-answer="help" data-hint="Hint: to assist someone" data-phrase="Can you help me?" placeholder="___">
          me?&rdquo;
        </div>
        <button class="check-btn" onclick="checkBlank(this)">Check</button>
        <button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button>
      </div>

      <div class="fill-blank-item">
        <div class="fill-blank-sentence">
          &ldquo;Can you speak
          <input class="blank-input" data-answer="slower" data-hint="Hint: less fast" data-phrase="Can you speak slower, please?" placeholder="___">
          , please?&rdquo;
        </div>
        <button class="check-btn" onclick="checkBlank(this)">Check</button>
        <button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button>
      </div>

      <div class="fill-blank-item">
        <div class="fill-blank-sentence">
          &ldquo;Can you
          <input class="blank-input" data-answer="show" data-hint="Hint: to point something out visually" data-phrase="Can you show me on the map?" placeholder="___">
          me on the map?&rdquo;
        </div>
        <button class="check-btn" onclick="checkBlank(this)">Check</button>
        <button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button>
      </div>
    </div>

    <!-- ===== STAGE 2: ORDERING ===== -->
    <div class="exercise-section">
      <h4>P2. Put in order <span class="badge badge-order">Order</span></h4>
      <p class="microcopy">Coloque as frases na ordem correta para formar uma conversa pedindo ajuda.</p>
      <div class="order-container" id="order-l8">
        <div class="order-item" draggable="true" data-order="3" onclick="selectOrderItem(this,'order-l8')">
          <span class="order-num">?</span>
          <span class="order-text">&ldquo;I can&rsquo;t find my hotel. Can you help me?&rdquo;</span>
          <span class="order-arrows">
            <button class="arrow-btn" onclick="moveItem(this,-1,'order-l8')">&#9650;</button>
            <button class="arrow-btn" onclick="moveItem(this,1,'order-l8')">&#9660;</button>
          </span>
        </div>
        <div class="order-item" draggable="true" data-order="5" onclick="selectOrderItem(this,'order-l8')">
          <span class="order-num">?</span>
          <span class="order-text">&ldquo;Can you speak slower, please?&rdquo;</span>
          <span class="order-arrows">
            <button class="arrow-btn" onclick="moveItem(this,-1,'order-l8')">&#9650;</button>
            <button class="arrow-btn" onclick="moveItem(this,1,'order-l8')">&#9660;</button>
          </span>
        </div>
        <div class="order-item" draggable="true" data-order="1" onclick="selectOrderItem(this,'order-l8')">
          <span class="order-num">?</span>
          <span class="order-text">&ldquo;Excuse me, can you help me?&rdquo;</span>
          <span class="order-arrows">
            <button class="arrow-btn" onclick="moveItem(this,-1,'order-l8')">&#9650;</button>
            <button class="arrow-btn" onclick="moveItem(this,1,'order-l8')">&#9660;</button>
          </span>
        </div>
        <div class="order-item" draggable="true" data-order="4" onclick="selectOrderItem(this,'order-l8')">
          <span class="order-num">?</span>
          <span class="order-text">&ldquo;Yes, I can. It is near the metro. Walk straight.&rdquo;</span>
          <span class="order-arrows">
            <button class="arrow-btn" onclick="moveItem(this,-1,'order-l8')">&#9650;</button>
            <button class="arrow-btn" onclick="moveItem(this,1,'order-l8')">&#9660;</button>
          </span>
        </div>
        <div class="order-item" draggable="true" data-order="2" onclick="selectOrderItem(this,'order-l8')">
          <span class="order-num">?</span>
          <span class="order-text">&ldquo;Yes, of course! What is the problem?&rdquo;</span>
          <span class="order-arrows">
            <button class="arrow-btn" onclick="moveItem(this,-1,'order-l8')">&#9650;</button>
            <button class="arrow-btn" onclick="moveItem(this,1,'order-l8')">&#9660;</button>
          </span>
        </div>
      </div>
      <button class="verify-all-btn" onclick="checkOrder('order-l8')">Check Order</button>
    </div>

    <!-- ===== STAGE 3: PRONUNCIATION ===== -->
    <div class="exercise-section">
      <h4>S1. Read aloud <span class="badge badge-speak">Speaking</span></h4>
      <p class="microcopy">Toque em Ouvir, repita, depois grave e compare. O objetivo &eacute; praticar, n&atilde;o ser perfeito.</p>

      <div class="speech-card" data-phrase="Can you help me?">
        <div class="speech-phrase">Can you help me?</div>
        <div class="speech-translation">Voc&ecirc; pode me ajudar?</div>
        <div class="speech-controls">
          <button class="btn btn-listen" onclick="speakPhrase(this)">&#9654; Ouvir</button>
          <button class="btn btn-record" onclick="startRecording(this)">&#9679; Gravar</button>
          <button class="btn btn-stop" onclick="stopRecording(this)">&#9632; Parar</button>
        </div>
        <div class="speech-result"></div>
      </div>

      <div class="speech-card" data-phrase="I can't find my hotel.">
        <div class="speech-phrase">I can&rsquo;t find my hotel.</div>
        <div class="speech-translation">Eu n&atilde;o consigo encontrar meu hotel.</div>
        <div class="speech-controls">
          <button class="btn btn-listen" onclick="speakPhrase(this)">&#9654; Ouvir</button>
          <button class="btn btn-record" onclick="startRecording(this)">&#9679; Gravar</button>
          <button class="btn btn-stop" onclick="stopRecording(this)">&#9632; Parar</button>
        </div>
        <div class="speech-result"></div>
      </div>

      <div class="speech-card" data-phrase="Can you speak slower, please?">
        <div class="speech-phrase">Can you speak slower, please?</div>
        <div class="speech-translation">Voc&ecirc; pode falar mais devagar, por favor?</div>
        <div class="speech-controls">
          <button class="btn btn-listen" onclick="speakPhrase(this)">&#9654; Ouvir</button>
          <button class="btn btn-record" onclick="startRecording(this)">&#9679; Gravar</button>
          <button class="btn btn-stop" onclick="stopRecording(this)">&#9632; Parar</button>
        </div>
        <div class="speech-result"></div>
      </div>

      <div class="speech-card" data-phrase="Can you show me on the map?">
        <div class="speech-phrase">Can you show me on the map?</div>
        <div class="speech-translation">Voc&ecirc; pode me mostrar no mapa?</div>
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
        <div class="quiz-question">You are lost in Paris and need help. What do you say?</div>
        <div class="quiz-options">
          <div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> &ldquo;Help me now!&rdquo;</div>
          <div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> &ldquo;Excuse me, can you help me?&rdquo;</div>
          <div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> &ldquo;I help you.&rdquo;</div>
        </div>
      </div>

      <div class="quiz-item">
        <div class="quiz-question">Someone speaks too fast. What do you ask?</div>
        <div class="quiz-options">
          <div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> &ldquo;Speak more fast!&rdquo;</div>
          <div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> &ldquo;Can you speak slower, please?&rdquo;</div>
          <div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> &ldquo;You can slower?&rdquo;</div>
        </div>
      </div>

      <div class="quiz-item">
        <div class="quiz-question">Someone asks: &ldquo;Can you speak French?&rdquo; and you cannot. What do you say?</div>
        <div class="quiz-options">
          <div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> &ldquo;No, I can&rsquo;t. But I can speak English.&rdquo;</div>
          <div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> &ldquo;No, I not can.&rdquo;</div>
          <div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> &ldquo;I no speak French.&rdquo;</div>
        </div>
      </div>

      <div class="quiz-item">
        <div class="quiz-question">You want to ask politely for someone to repeat. What do you say?</div>
        <div class="quiz-options">
          <div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> &ldquo;Repeat!&rdquo;</div>
          <div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> &ldquo;You can repeat?&rdquo;</div>
          <div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">C</span> &ldquo;Could you repeat that, please?&rdquo;</div>
        </div>
      </div>
    </div>

    <!-- ===== STAGE 5: THINK ===== -->
    <div class="exercise-section">
      <h4>T1. Think and respond <span class="badge badge-think">Reflection</span></h4>
      <p class="microcopy">Aqui n&atilde;o tem resposta certa &mdash; &eacute; pra voc&ecirc; pensar em ingl&ecirc;s. Toque no microfone e responde como vier.</p>
      <div class="think-card">
        <div style="font-size:0.92rem;color:var(--text);margin-bottom:1rem;line-height:1.8;">You are lost in Paris. You cannot find your hotel. You see a person on the street. Ask for help: say you are lost, you cannot find your hotel, ask them to show you on the map, and ask them to speak slower.</div>
        <div class="speech-card" data-phrase="Excuse me, can you help me? I am lost. I can't find my hotel. Can you show me on the map? Can you speak slower, please?" style="background:var(--accent-dim);border:1px solid rgba(212,50,106,0.25);">
          <div style="font-size:0.72rem;font-weight:600;text-transform:uppercase;letter-spacing:1.5px;color:var(--accent);margin-bottom:0.5rem;">Sugest&atilde;o de resposta</div>
          <div class="speech-phrase" style="font-size:1.05rem;">&ldquo;Excuse me, can you help me? I am lost. I can&rsquo;t find my hotel. Can you show me on the map? Can you speak slower, please?&rdquo;</div>
          <div class="speech-translation">Com licen&ccedil;a, voc&ecirc; pode me ajudar? Estou perdida. N&atilde;o consigo encontrar meu hotel. Pode me mostrar no mapa? Pode falar mais devagar, por favor?</div>
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
      <h4>Survival Card &mdash; Lesson 8: Abilities &amp; Asking for Help</h4>
      <div class="survival-phrase"><span class="sp-num">1</span><span class="sp-en">Can you help me, please?</span><span class="sp-pt">Voc&ecirc; pode me ajudar, por favor?</span><button class="btn btn-listen" onclick="speakText('Can you help me, please?', this)">&#9654;</button></div>
      <div class="survival-phrase"><span class="sp-num">2</span><span class="sp-en">I can&rsquo;t find my hotel.</span><span class="sp-pt">N&atilde;o consigo encontrar meu hotel.</span><button class="btn btn-listen" onclick="speakText('I can\\'t find my hotel.', this)">&#9654;</button></div>
      <div class="survival-phrase"><span class="sp-num">3</span><span class="sp-en">Can you speak slower, please?</span><span class="sp-pt">Pode falar mais devagar, por favor?</span><button class="btn btn-listen" onclick="speakText('Can you speak slower, please?', this)">&#9654;</button></div>
      <div class="survival-phrase"><span class="sp-num">4</span><span class="sp-en">Can you show me on the map?</span><span class="sp-pt">Pode me mostrar no mapa?</span><button class="btn btn-listen" onclick="speakText('Can you show me on the map?', this)">&#9654;</button></div>
      <div class="survival-phrase"><span class="sp-num">5</span><span class="sp-en">I can speak English.</span><span class="sp-pt">Eu sei falar ingl&ecirc;s.</span><button class="btn btn-listen" onclick="speakText('I can speak English.', this)">&#9654;</button></div>
    </div>

  </div>
</div>'''

# ============================================================
# AULA 8 IN CLASS SLIDES HTML (29 slides, data-slide 205-233)
# ============================================================
SLIDES_HTML = '''
<!-- ================ LESSON 8: CAN YOU DO THAT? ================ -->

<!-- SLIDE 205: L8 CHAPTER 1 - THE DREAM -->
<div class="slide slide-image" data-slide="205" data-phase="1" data-lesson="8" data-teacher="<strong>Abertura (2 min):</strong> 'Welcome back, Gabriela! Last class: countries and nationalities. Today: CAN YOU DO THAT? Abilities, asking for help, and survival English! Imagine: you are walking in Paris and suddenly... you are LOST. What do you do?' Tom animado e dramatico." style="background-image:url('https://images.unsplash.com/photo-1499856871958-5b9627545d1a?w=600&q=80')">
  <div class="slide-inner">
    <div class="chapter-label">Chapter 1 &mdash; The Dream</div>
    <h1 class="slide-title">Can You <span class="accent">Do That</span>?</h1>
    <p class="slide-subtitle">Abilities, possibilities &amp; asking for help in Paris</p>
  </div>
</div>

<!-- SLIDE 206: L8 WARM-UP CALLBACK -->
<div class="slide slide-dark" data-slide="206" data-phase="1" data-lesson="8" data-teacher="<strong>Callback Aula 7 (3 min):</strong> Perguntas rapidas usando countries/nationalities da aula anterior. 'Where are you from? What nationality are you? What languages do you speak?' Depois: 'You can say where you are from. But what happens if you are LOST in Paris and need HELP? Today you learn HOW to ask!' Ponte natural para o tema.">
  <div class="slide-inner">
    <div class="chapter-label">Warm-up</div>
    <h2 class="slide-heading">Quick <span class="accent">Callback</span></h2>
    <div class="warm-questions">
      <div class="warm-q">Where are you from? What is your nationality?</div>
      <div class="warm-q">What languages do you speak?</div>
      <div class="warm-q">Now imagine: you are walking in Paris alone. You are lost. What do you DO?</div>
    </div>
  </div>
</div>

<!-- SLIDE 207: L8 CHAPTER 2 TRANSITION -->
<div class="slide slide-image" data-slide="207" data-phase="2" data-lesson="8" data-teacher="<strong>Transicao (10s):</strong> 'Let us pack the survival words you need when you are lost in Paris!' Avance." style="background-image:url('https://images.unsplash.com/photo-1499856871958-5b9627545d1a?w=600&q=80')">
  <div class="slide-inner">
    <div class="chapter-label">Chapter 2</div>
    <h1 class="slide-title">Packing <span class="accent">Words</span></h1>
    <p class="slide-subtitle">Survival vocabulary for asking for help</p>
  </div>
</div>

<!-- SLIDE 208: L8 VOCAB CARDS 1-4 -->
<div class="slide slide-light" data-slide="208" data-phase="2" data-lesson="8" data-teacher="<strong>Vocabulario (8 min):</strong> ANTES de clicar, leia a pista: 'What word do you think this is?' DEPOIS de revelar, toque audio 2x. Drill: speak /speek/ &mdash; 1 silaba, vogal longa. understand /un-der-STAND/ &mdash; stress no STAND. help /help/ &mdash; 1 silaba, som do H claro. repeat /ri-PEET/ &mdash; stress no PEET. Drill cada 3x.">
  <div class="slide-inner">
    <h2 class="slide-heading">Survival <span class="accent">Words</span></h2>
    <div class="vocab-grid">
      <div class="vocab-card" onclick="this.classList.toggle('revealed')">
        <div class="card-icon" style="background:linear-gradient(135deg,#0891b2,#06b6d4)">
          <svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="1.5"><path d="M12 1a3 3 0 00-3 3v8a3 3 0 006 0V4a3 3 0 00-3-3z"/><path d="M19 10v2a7 7 0 01-14 0v-2M12 19v4M8 23h8"/></svg>
          <div class="card-hint">To say words out loud in a language</div>
        </div>
        <div class="card-body">
          <div class="card-word">Speak</div>
          <div class="card-def">To talk, to say words in a language</div>
          <div class="card-example">&ldquo;I <strong>can speak</strong> English.&rdquo;</div>
          <div class="card-audio"><button class="audio-btn-sm" onclick="event.stopPropagation();speakText('I can speak English.',this)"><svg viewBox="0 0 24 24"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M19.07 4.93a10 10 0 010 14.14M15.54 8.46a5 5 0 010 7.07"/></svg> Listen</button></div>
        </div>
      </div>
      <div class="vocab-card" onclick="this.classList.toggle('revealed')">
        <div class="card-icon" style="background:linear-gradient(135deg,#7c3aed,#a855f7)">
          <svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="1.5"><circle cx="12" cy="12" r="10"/><path d="M2 12h20"/><path d="M12 2v20"/></svg>
          <div class="card-hint">To know what someone means</div>
        </div>
        <div class="card-body">
          <div class="card-word">Understand</div>
          <div class="card-def">To know the meaning of what someone says</div>
          <div class="card-example">&ldquo;I can <strong>understand</strong> you.&rdquo;</div>
          <div class="card-audio"><button class="audio-btn-sm" onclick="event.stopPropagation();speakText('I can understand you.',this)"><svg viewBox="0 0 24 24"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M19.07 4.93a10 10 0 010 14.14M15.54 8.46a5 5 0 010 7.07"/></svg> Listen</button></div>
        </div>
      </div>
      <div class="vocab-card" onclick="this.classList.toggle('revealed')">
        <div class="card-icon" style="background:linear-gradient(135deg,#dc2626,#f87171)">
          <svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="1.5"><circle cx="12" cy="12" r="10"/><path d="M9.09 9a3 3 0 015.83 1c0 2-3 3-3 3M12 17h.01"/></svg>
          <div class="card-hint">When you are lost, you ask someone to...</div>
        </div>
        <div class="card-body">
          <div class="card-word">Help</div>
          <div class="card-def">To assist someone, to make things easier</div>
          <div class="card-example">&ldquo;<strong>Can</strong> you <strong>help</strong> me?&rdquo;</div>
          <div class="card-audio"><button class="audio-btn-sm" onclick="event.stopPropagation();speakText('Can you help me?',this)"><svg viewBox="0 0 24 24"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M19.07 4.93a10 10 0 010 14.14M15.54 8.46a5 5 0 010 7.07"/></svg> Listen</button></div>
        </div>
      </div>
      <div class="vocab-card" onclick="this.classList.toggle('revealed')">
        <div class="card-icon" style="background:linear-gradient(135deg,#059669,#10b981)">
          <svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="1.5"><polyline points="1 4 1 10 7 10"/><path d="M3.51 15a9 9 0 102.13-9.36L1 10"/></svg>
          <div class="card-hint">To say something again</div>
        </div>
        <div class="card-body">
          <div class="card-word">Repeat</div>
          <div class="card-def">To say something one more time</div>
          <div class="card-example">&ldquo;Can you <strong>repeat</strong> that, please?&rdquo;</div>
          <div class="card-audio"><button class="audio-btn-sm" onclick="event.stopPropagation();speakText('Can you repeat that, please?',this)"><svg viewBox="0 0 24 24"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M19.07 4.93a10 10 0 010 14.14M15.54 8.46a5 5 0 010 7.07"/></svg> Listen</button></div>
        </div>
      </div>
    </div>
    <div class="vocab-counter"><span id="vc8a">0</span> / 4 words</div>
  </div>
</div>

<!-- SLIDE 209: L8 VOCAB CARDS 5-8 -->
<div class="slide slide-light" data-slide="209" data-phase="2" data-lesson="8" data-teacher="<strong>Vocabulario (6 min):</strong> find /fahynd/ &mdash; 1 silaba, diptongo AI. show /shoh/ &mdash; 1 silaba, arredondar labios no SH. slower /SLOH-er/ &mdash; 2 silabas. map /map/ &mdash; 1 silaba, som do A curto. Drill cada 3x. Pergunte: 'I am lost and I need a...?' &rarr; 'Map!'">
  <div class="slide-inner">
    <h2 class="slide-heading">More Survival <span class="accent">Words</span></h2>
    <div class="vocab-grid">
      <div class="vocab-card" onclick="this.classList.toggle('revealed')">
        <div class="card-icon" style="background:linear-gradient(135deg,#d97706,#f59e0b)">
          <svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="1.5"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>
          <div class="card-hint">To look for and discover something</div>
        </div>
        <div class="card-body">
          <div class="card-word">Find</div>
          <div class="card-def">To locate something you are looking for</div>
          <div class="card-example">&ldquo;I can&rsquo;t <strong>find</strong> my hotel.&rdquo;</div>
          <div class="card-audio"><button class="audio-btn-sm" onclick="event.stopPropagation();speakText('I can\\'t find my hotel.',this)"><svg viewBox="0 0 24 24"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M19.07 4.93a10 10 0 010 14.14M15.54 8.46a5 5 0 010 7.07"/></svg> Listen</button></div>
        </div>
      </div>
      <div class="vocab-card" onclick="this.classList.toggle('revealed')">
        <div class="card-icon" style="background:linear-gradient(135deg,#be185d,#ec4899)">
          <svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="1.5"><path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"/><circle cx="12" cy="12" r="3"/></svg>
          <div class="card-hint">To point at something for someone to see</div>
        </div>
        <div class="card-body">
          <div class="card-word">Show</div>
          <div class="card-def">To point at or display something</div>
          <div class="card-example">&ldquo;Can you <strong>show</strong> me on the map?&rdquo;</div>
          <div class="card-audio"><button class="audio-btn-sm" onclick="event.stopPropagation();speakText('Can you show me on the map?',this)"><svg viewBox="0 0 24 24"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M19.07 4.93a10 10 0 010 14.14M15.54 8.46a5 5 0 010 7.07"/></svg> Listen</button></div>
        </div>
      </div>
      <div class="vocab-card" onclick="this.classList.toggle('revealed')">
        <div class="card-icon" style="background:linear-gradient(135deg,#1e3a5f,#003080)">
          <svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="1.5"><path d="M13 2L3 14h9l-1 8 10-12h-9l1-8z"/></svg>
          <div class="card-hint">The opposite of faster</div>
        </div>
        <div class="card-body">
          <div class="card-word">Slower</div>
          <div class="card-def">Less fast, at a reduced speed</div>
          <div class="card-example">&ldquo;Can you speak <strong>slower</strong>, please?&rdquo;</div>
          <div class="card-audio"><button class="audio-btn-sm" onclick="event.stopPropagation();speakText('Can you speak slower, please?',this)"><svg viewBox="0 0 24 24"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M19.07 4.93a10 10 0 010 14.14M15.54 8.46a5 5 0 010 7.07"/></svg> Listen</button></div>
        </div>
      </div>
      <div class="vocab-card" onclick="this.classList.toggle('revealed')">
        <div class="card-icon" style="background:linear-gradient(135deg,#002395,#ED2939)">
          <svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="1.5"><polygon points="1 6 1 22 8 18 16 22 23 18 23 2 16 6 8 2 1 6"/><line x1="8" y1="2" x2="8" y2="18"/><line x1="16" y1="6" x2="16" y2="22"/></svg>
          <div class="card-hint">A picture of streets and places</div>
        </div>
        <div class="card-body">
          <div class="card-word">Map</div>
          <div class="card-def">A drawing that shows streets and locations</div>
          <div class="card-example">&ldquo;Do you have a <strong>map</strong>?&rdquo;</div>
          <div class="card-audio"><button class="audio-btn-sm" onclick="event.stopPropagation();speakText('Do you have a map?',this)"><svg viewBox="0 0 24 24"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M19.07 4.93a10 10 0 010 14.14M15.54 8.46a5 5 0 010 7.07"/></svg> Listen</button></div>
        </div>
      </div>
    </div>
    <div class="vocab-counter"><span id="vc8b">0</span> / 4 words</div>
  </div>
</div>

<!-- SLIDE 210: L8 PRONUNCIATION DRILL -->
<div class="slide slide-light" data-slide="210" data-phase="2" data-lesson="8" data-teacher="<strong>Pronuncia (4 min):</strong> Drill de pronuncia. Foco: can /kan/ vs can't /kant/ &mdash; a diferenca e o T final + vogal mais curta no can't. understand /un-der-STAND/ &mdash; stress no STAND. repeat /ri-PEET/ &mdash; stress no PEET. slower /SLOH-er/ &mdash; NAO e 'sloer'. Repita 3x cada com Gabriela.">
  <div class="slide-inner">
    <h2 class="slide-heading">Say It <span class="accent">Right</span></h2>
    <div class="pron-grid">
      <div class="pron-item" onclick="speakText('Speak',this)">
        <div class="pron-word">Speak</div>
        <div class="pron-stress"><span class="pron-syl stressed">SPEAK</span></div>
        <div class="pron-audio"><button class="audio-btn-sm" onclick="event.stopPropagation();speakText('Speak',this)"><svg viewBox="0 0 24 24"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M19.07 4.93a10 10 0 010 14.14"/></svg> Listen</button></div>
      </div>
      <div class="pron-item" onclick="speakText('Understand',this)">
        <div class="pron-word">Understand</div>
        <div class="pron-stress"><span class="pron-syl">un</span><span class="pron-syl">der</span><span class="pron-syl stressed">STAND</span></div>
        <div class="pron-audio"><button class="audio-btn-sm" onclick="event.stopPropagation();speakText('Understand',this)"><svg viewBox="0 0 24 24"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M19.07 4.93a10 10 0 010 14.14"/></svg> Listen</button></div>
      </div>
      <div class="pron-item" onclick="speakText('Repeat',this)">
        <div class="pron-word">Repeat</div>
        <div class="pron-stress"><span class="pron-syl">re</span><span class="pron-syl stressed">PEAT</span></div>
        <div class="pron-audio"><button class="audio-btn-sm" onclick="event.stopPropagation();speakText('Repeat',this)"><svg viewBox="0 0 24 24"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M19.07 4.93a10 10 0 010 14.14"/></svg> Listen</button></div>
      </div>
      <div class="pron-item" onclick="speakText('Help',this)">
        <div class="pron-word">Help</div>
        <div class="pron-stress"><span class="pron-syl stressed">HELP</span></div>
        <div class="pron-audio"><button class="audio-btn-sm" onclick="event.stopPropagation();speakText('Help',this)"><svg viewBox="0 0 24 24"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M19.07 4.93a10 10 0 010 14.14"/></svg> Listen</button></div>
      </div>
      <div class="pron-item" onclick="speakText('Slower',this)">
        <div class="pron-word">Slower</div>
        <div class="pron-stress"><span class="pron-syl stressed">SLOW</span><span class="pron-syl">er</span></div>
        <div class="pron-audio"><button class="audio-btn-sm" onclick="event.stopPropagation();speakText('Slower',this)"><svg viewBox="0 0 24 24"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M19.07 4.93a10 10 0 010 14.14"/></svg> Listen</button></div>
      </div>
      <div class="pron-item" onclick="speakText('Map',this)">
        <div class="pron-word">Map</div>
        <div class="pron-stress"><span class="pron-syl stressed">MAP</span></div>
        <div class="pron-audio"><button class="audio-btn-sm" onclick="event.stopPropagation();speakText('Map',this)"><svg viewBox="0 0 24 24"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M19.07 4.93a10 10 0 010 14.14"/></svg> Listen</button></div>
      </div>
    </div>
  </div>
</div>

<!-- SLIDE 211: L8 CHAPTER 3 TRANSITION -->
<div class="slide slide-image" data-slide="211" data-phase="3" data-lesson="8" data-teacher="<strong>Transicao (10s):</strong> 'Words packed! Now let us crack the CAN code!' Avance." style="background-image:url('https://images.unsplash.com/photo-1499856871958-5b9627545d1a?w=600&q=80')">
  <div class="slide-inner">
    <div class="chapter-label">Chapter 3</div>
    <h1 class="slide-title">The <span class="accent">Code</span></h1>
    <p class="slide-subtitle">How to use CAN like a pro</p>
  </div>
</div>

<!-- SLIDE 212: L8 GRAMMAR DISCOVERY -->
<div class="slide slide-light" data-slide="212" data-phase="3" data-lesson="8" data-teacher="<strong>Grammar Discovery (5 min):</strong> Mostre as 4 frases. Pergunte: 'Look at the pink words. What pattern do you see?' Espere. Se nao perceber: 'CAN + verbo base = habilidade. CAN'T = nao consegue. CAN + you = pergunta. E nunca 'I can TO speak' &mdash; sem TO!' Discovery method.">
  <div class="slide-inner">
    <h2 class="slide-heading">Spot the <span class="accent">Pattern</span></h2>
    <div class="grammar-sentences">
      <div class="grammar-sentence">I <strong>can speak</strong> English.</div>
      <div class="grammar-sentence">I <strong>can&rsquo;t find</strong> my hotel.</div>
      <div class="grammar-sentence"><strong>Can</strong> you <strong>help</strong> me?</div>
      <div class="grammar-sentence">Yes, I <strong>can</strong>. / No, I <strong>can&rsquo;t</strong>.</div>
    </div>
    <p style="text-align:center;margin-top:1.5rem;font-size:1.1rem;color:var(--text);">What do the <span class="accent-bold">pink words</span> have in common?</p>
    <div style="text-align:center;margin-top:1rem;">
      <button class="btn-primary" onclick="this.nextElementSibling.classList.toggle('show');this.style.display='none'">Reveal the Rule</button>
      <div class="grammar-table-wrap">
        <table class="grammar-table">
          <tr><th>Form</th><th>Structure</th><th>Example</th></tr>
          <tr><td>Affirmative (+)</td><td>Subject + <strong>can</strong> + verb</td><td>I <strong>can speak</strong> English.</td></tr>
          <tr><td>Negative (&minus;)</td><td>Subject + <strong>can&rsquo;t</strong> + verb</td><td>I <strong>can&rsquo;t find</strong> my hotel.</td></tr>
          <tr><td>Question (?)</td><td><strong>Can</strong> + subject + verb?</td><td><strong>Can</strong> you <strong>help</strong> me?</td></tr>
          <tr><td>Short answer</td><td>Yes, I <strong>can</strong>. / No, I <strong>can&rsquo;t</strong>.</td><td>&mdash;</td></tr>
        </table>
        <p style="font-size:.85rem;margin-top:.8rem;color:var(--text-mid);"><strong>Key:</strong> CAN + base verb (no &ldquo;to&rdquo;!). Same for all subjects (I/you/he/she/they).</p>
      </div>
    </div>
  </div>
</div>

<!-- SLIDE 213: L8 COMMON MISTAKE -->
<div class="slide slide-light" data-slide="213" data-phase="3" data-lesson="8" data-teacher="<strong>Common Mistake (3 min):</strong> 'Em portugues: eu CONSIGO falar. Em ingles: I CAN speak &mdash; NUNCA 'I can TO speak'. E na pergunta: Can you speak? NUNCA 'Can you speaking?' CAN + verbo BASE, sempre!' Drill: 'I can speak.' 3x. 'Can you help?' 3x.">
  <div class="slide-inner">
    <h2 class="slide-heading">Common <span class="accent">Mistake</span></h2>
    <div class="mistake-card">
      <div class="mistake-item mistake-wrong">
        <div class="mistake-icon"><svg viewBox="0 0 24 24" fill="none" stroke="#dc2626"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg></div>
        &ldquo;I can <strong>to</strong> speak English.&rdquo;
      </div>
      <div class="mistake-item mistake-right">
        <div class="mistake-icon"><svg viewBox="0 0 24 24" fill="none" stroke="#16a34a"><polyline points="20 6 9 17 4 12"/></svg></div>
        &ldquo;I <strong>can speak</strong> English.&rdquo; &mdash; No &ldquo;to&rdquo; after CAN!
      </div>
    </div>
    <div class="mistake-card" style="margin-top:1rem;">
      <div class="mistake-item mistake-wrong">
        <div class="mistake-icon"><svg viewBox="0 0 24 24" fill="none" stroke="#dc2626"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg></div>
        &ldquo;Can you speak<strong>ing</strong>?&rdquo;
      </div>
      <div class="mistake-item mistake-right">
        <div class="mistake-icon"><svg viewBox="0 0 24 24" fill="none" stroke="#16a34a"><polyline points="20 6 9 17 4 12"/></svg></div>
        &ldquo;<strong>Can you speak</strong>?&rdquo; &mdash; Base verb only, no -ing!
      </div>
    </div>
  </div>
</div>

<!-- SLIDE 214: L8 GRAMMAR PRACTICE -->
<div class="slide slide-light" data-slide="214" data-phase="3" data-lesson="8" data-teacher="<strong>Grammar Practice (4 min):</strong> Clique cada item para revelar. 'Can you swim?' Gabriela responde yes/no. 'Can she cook?' etc. Foco em CAN + base verb e respostas curtas Yes, I can / No, I can't.">
  <div class="slide-inner">
    <h2 class="slide-heading">Can You <span class="accent">Do It</span>?</h2>
    <div class="fill-grid">
      <div class="fill-item" onclick="this.classList.toggle('revealed')">
        <div class="fill-text">You / speak English &rarr; <span class="fill-blank">???</span><span class="fill-answer">I can speak English. (Yes, I can!)</span></div>
      </div>
      <div class="fill-item" onclick="this.classList.toggle('revealed')">
        <div class="fill-text">You / speak French &rarr; <span class="fill-blank">???</span><span class="fill-answer">I can&rsquo;t speak French. (No, I can&rsquo;t.)</span></div>
      </div>
      <div class="fill-item" onclick="this.classList.toggle('revealed')">
        <div class="fill-text">You / swim &rarr; <span class="fill-blank">???</span><span class="fill-answer">I can swim. / I can&rsquo;t swim.</span></div>
      </div>
      <div class="fill-item" onclick="this.classList.toggle('revealed')">
        <div class="fill-text">You / find the hotel? (question) &rarr; <span class="fill-blank">???</span><span class="fill-answer">Can you find the hotel?</span></div>
      </div>
      <div class="fill-item" onclick="this.classList.toggle('revealed')">
        <div class="fill-text">She / cook (negative) &rarr; <span class="fill-blank">???</span><span class="fill-answer">She can&rsquo;t cook.</span></div>
      </div>
      <div class="fill-item" onclick="this.classList.toggle('revealed')">
        <div class="fill-text">He / play guitar? (question) &rarr; <span class="fill-blank">???</span><span class="fill-answer">Can he play guitar?</span></div>
      </div>
    </div>
  </div>
</div>

<!-- SLIDE 215: L8 CHAPTER 4 TRANSITION -->
<div class="slide slide-image" data-slide="215" data-phase="4" data-lesson="8" data-teacher="<strong>Transicao (10s):</strong> 'Now imagine: day 2 in Paris. You are walking... and suddenly you are LOST.' Avance." style="background-image:url('https://images.unsplash.com/photo-1499856871958-5b9627545d1a?w=600&q=80')">
  <div class="slide-inner">
    <div class="chapter-label">Chapter 4</div>
    <h1 class="slide-title">Getting <span class="accent">There</span></h1>
    <p class="slide-subtitle">Gabriela is lost in Paris and needs help</p>
  </div>
</div>

<!-- SLIDE 216: L8 DIALOGUE LINE-BY-LINE -->
<div class="slide slide-dark" data-slide="216" data-phase="4" data-lesson="8" data-teacher="<strong>Dialogo (8 min):</strong> Clique Next Line para cada fala. Professor le Passerby (voz masculina Arthur), Gabriela le suas falas. Vocabulario da aula em destaque rosa. Foco em 'can you help me', 'can you show me', 'can you speak slower'. Depois pergunte: 'What is the name of Gabriela's hotel? Can the man help her?'">
  <div class="slide-inner">
    <h2 class="slide-heading" style="color:#fff">Lost in <span class="accent">Paris</span></h2>
    <div class="dialogue-box" id="dial8">
      <div class="dialogue-line" data-voice="ellen" style="opacity:0;transform:translateY(10px)">
        <div class="avatar" style="background:var(--accent)">G</div>
        <div class="bubble"><strong>Gabriela:</strong> Excuse me, <strong>can</strong> you <strong>help</strong> me?<br><button class="audio-btn-sm" onclick="speakText('Excuse me, can you help me?',this)"><svg viewBox="0 0 24 24"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/></svg> Listen</button></div>
      </div>
      <div class="dialogue-line" data-voice="arthur" style="opacity:0;transform:translateY(10px)">
        <div class="avatar" style="background:var(--navy)">P</div>
        <div class="bubble"><strong>Passerby:</strong> Yes, of course! What is the problem?<br><button class="audio-btn-sm" onclick="speakText('What is the name of your hotel?',this)"><svg viewBox="0 0 24 24"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/></svg> Listen</button></div>
      </div>
      <div class="dialogue-line" data-voice="ellen" style="opacity:0;transform:translateY(10px)">
        <div class="avatar" style="background:var(--accent)">G</div>
        <div class="bubble"><strong>Gabriela:</strong> I am lost. I <strong>can&rsquo;t find</strong> my hotel.<br><button class="audio-btn-sm" onclick="speakText('I am lost. I can\\'t find my hotel.',this)"><svg viewBox="0 0 24 24"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/></svg> Listen</button></div>
      </div>
      <div class="dialogue-line" data-voice="arthur" style="opacity:0;transform:translateY(10px)">
        <div class="avatar" style="background:var(--navy)">P</div>
        <div class="bubble"><strong>Passerby:</strong> What is the name of your hotel?<br><button class="audio-btn-sm" onclick="speakText('What is the name of your hotel?',this)"><svg viewBox="0 0 24 24"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/></svg> Listen</button></div>
      </div>
      <div class="dialogue-line" data-voice="ellen" style="opacity:0;transform:translateY(10px)">
        <div class="avatar" style="background:var(--accent)">G</div>
        <div class="bubble"><strong>Gabriela:</strong> It is Hotel Le Marais. <strong>Can</strong> you <strong>show</strong> me on the <strong>map</strong>?<br><button class="audio-btn-sm" onclick="speakText('It is Hotel Le Marais. Can you show me on the map?',this)"><svg viewBox="0 0 24 24"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/></svg> Listen</button></div>
      </div>
      <div class="dialogue-line" data-voice="arthur" style="opacity:0;transform:translateY(10px)">
        <div class="avatar" style="background:var(--navy)">P</div>
        <div class="bubble"><strong>Passerby:</strong> Of course! It is here. You can walk. It is five minutes.<br><button class="audio-btn-sm" onclick="speakText('Of course! It is here. You can walk. It is five minutes.',this)"><svg viewBox="0 0 24 24"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/></svg> Listen</button></div>
      </div>
      <div class="dialogue-line" data-voice="ellen" style="opacity:0;transform:translateY(10px)">
        <div class="avatar" style="background:var(--accent)">G</div>
        <div class="bubble"><strong>Gabriela:</strong> <strong>Can</strong> you <strong>repeat</strong> that? <strong>Slower</strong>, please.<br><button class="audio-btn-sm" onclick="speakText('Can you repeat that? Slower, please.',this)"><svg viewBox="0 0 24 24"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/></svg> Listen</button></div>
      </div>
      <div class="dialogue-line" data-voice="arthur" style="opacity:0;transform:translateY(10px)">
        <div class="avatar" style="background:var(--navy)">P</div>
        <div class="bubble"><strong>Passerby:</strong> Yes! Walk straight. Turn left. Your hotel is on the right.<br><button class="audio-btn-sm" onclick="speakText('Yes! Walk straight. Turn left. Your hotel is on the right.',this)"><svg viewBox="0 0 24 24"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/></svg> Listen</button></div>
      </div>
      <div class="dialogue-line" data-voice="ellen" style="opacity:0;transform:translateY(10px)">
        <div class="avatar" style="background:var(--accent)">G</div>
        <div class="bubble"><strong>Gabriela:</strong> Thank you so much! I <strong>can find</strong> it now.<br><button class="audio-btn-sm" onclick="speakText('Thank you so much! I can find it now.',this)"><svg viewBox="0 0 24 24"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/></svg> Listen</button></div>
      </div>
      <div class="dialogue-line" data-voice="arthur" style="opacity:0;transform:translateY(10px)">
        <div class="avatar" style="background:var(--navy)">P</div>
        <div class="bubble"><strong>Passerby:</strong> You are welcome! Your English is very good!<br><button class="audio-btn-sm" onclick="speakText('You are welcome! Your English is very good!',this)"><svg viewBox="0 0 24 24"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/></svg> Listen</button></div>
      </div>
    </div>
    <div style="text-align:center;margin-top:1rem;">
      <button class="btn-primary" onclick="var lines=document.querySelectorAll('#dial8 .dialogue-line');var shown=document.querySelectorAll('#dial8 .dialogue-line[style*=\\'opacity: 1\\']').length||document.querySelectorAll('#dial8 .dialogue-line.shown').length;lines.forEach(function(l,i){if(i<=shown){l.style.opacity='1';l.style.transform='translateY(0)';l.classList.add('shown')}})">Next Line</button>
    </div>
  </div>
</div>

<!-- SLIDE 217: L8 COMPREHENSION -->
<div class="slide slide-dark" data-slide="217" data-phase="4" data-lesson="8" data-teacher="<strong>Comprehension (3 min):</strong> Pergunte SEM mostrar respostas. Depois clique para revelar. Se Gabriela acertar, celebre! Foco: compreensao do que o PASSERBY disse.">
  <div class="slide-inner">
    <h2 class="slide-heading" style="color:#fff">Did You <span class="accent">Catch</span> That?</h2>
    <div class="comp-questions">
      <div class="comp-q" onclick="this.classList.toggle('revealed')">
        <div class="q-text">What is the name of Gabriela&rsquo;s hotel?</div>
        <div class="q-answer">Hotel Le Marais</div>
      </div>
      <div class="comp-q" onclick="this.classList.toggle('revealed')">
        <div class="q-text">Can the passerby help her?</div>
        <div class="q-answer">Yes, he can! He shows her on the map.</div>
      </div>
      <div class="comp-q" onclick="this.classList.toggle('revealed')">
        <div class="q-text">How far is the hotel?</div>
        <div class="q-answer">Five minutes walking</div>
      </div>
    </div>
  </div>
</div>

<!-- SLIDE 218: L8 LISTENING 1 -->
<div class="slide slide-dark" data-slide="218" data-phase="4" data-lesson="8" data-teacher="<strong>Listening 1 (4 min):</strong> Toque o audio PRIMEIRO. Gabriela ouve SEM texto. Depois pergunte: 'Can Gabriela speak French? What can't Gabriela find? What does she ask the man to do?' Toque novamente se preciso.">
  <div class="slide-inner">
    <h2 class="slide-heading" style="color:#fff">Listen <span class="accent">First</span></h2>
    <p style="color:rgba(255,255,255,.6);text-align:center;margin-bottom:1.5rem;">Close your eyes and listen. What can Gabriela do? What can&rsquo;t she do?</p>
    <div style="display:flex;flex-direction:column;align-items:center;gap:1rem;">
      <div style="width:200px;height:60px;background:rgba(255,255,255,.06);border-radius:30px;display:flex;align-items:center;justify-content:center;">
        <button class="btn-primary" onclick="speakText('Gabriela is walking in Paris. It is her second day. She can\\'t find her hotel. She is lost. She can speak English, but she can\\'t speak French. She sees a man near the metro station. She asks: Can you help me? The man says: Yes, I can. What is the problem? Gabriela says: I can\\'t find my hotel. Can you show me on the map? The man shows the map. He speaks fast. Gabriela says: Can you speak slower, please? He speaks slower. Now Gabriela can understand. She can find her hotel. She says: Thank you! I can walk from here.',this)" style="border-radius:30px;padding:.8rem 2rem;">
          <svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2"><polygon points="5 3 19 12 5 21 5 3"/></svg>
          &nbsp;Play
        </button>
      </div>
    </div>
    <div class="comp-questions" style="margin-top:2rem;">
      <div class="comp-q" onclick="this.classList.toggle('revealed')">
        <div class="q-text">Can Gabriela speak French?</div>
        <div class="q-answer">No, she can&rsquo;t. She can speak English.</div>
      </div>
      <div class="comp-q" onclick="this.classList.toggle('revealed')">
        <div class="q-text">What can&rsquo;t Gabriela find?</div>
        <div class="q-answer">Her hotel</div>
      </div>
      <div class="comp-q" onclick="this.classList.toggle('revealed')">
        <div class="q-text">What does Gabriela ask the man to do?</div>
        <div class="q-answer">Show her on the map and speak slower</div>
      </div>
    </div>
  </div>
</div>

<!-- SLIDE 219: L8 LISTENING 2 -->
<div class="slide slide-dark" data-slide="219" data-phase="4" data-lesson="8" data-teacher="<strong>Listening 2 (3 min):</strong> 3 situacoes diferentes em que Gabriela pede ajuda. Toque primeiro sem texto. Perguntas: 'What can't she find in situation 1? What can't she understand in situation 2?'">
  <div class="slide-inner">
    <h2 class="slide-heading" style="color:#fff">Listen <span class="accent">Again</span></h2>
    <p style="color:rgba(255,255,255,.6);text-align:center;margin-bottom:1.5rem;">Gabriela asks for help in three different situations. Listen and answer.</p>
    <div style="display:flex;flex-direction:column;align-items:center;gap:.5rem;">
      <button class="btn-primary" onclick="speakText('Hi, I am lost. Can you help me? I can\\'t find the Eiffel Tower. Can you show me on the map?',this)" style="border-radius:30px;padding:.6rem 1.5rem;font-size:.85rem;"><svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2"><polygon points="5 3 19 12 5 21 5 3"/></svg> &nbsp;Situation 1</button>
      <button class="btn-primary" onclick="speakText('Excuse me. I can\\'t understand the menu. Can you help me? Can you speak slower?',this)" style="border-radius:30px;padding:.6rem 1.5rem;font-size:.85rem;"><svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2"><polygon points="5 3 19 12 5 21 5 3"/></svg> &nbsp;Situation 2</button>
      <button class="btn-primary" onclick="speakText('Hello. I can\\'t find the metro station. Can you show me? I can speak English.',this)" style="border-radius:30px;padding:.6rem 1.5rem;font-size:.85rem;"><svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2"><polygon points="5 3 19 12 5 21 5 3"/></svg> &nbsp;Situation 3</button>
    </div>
    <div class="comp-questions" style="margin-top:1.5rem;">
      <div class="comp-q" onclick="this.classList.toggle('revealed')">
        <div class="q-text">What can&rsquo;t she find in Situation 1?</div>
        <div class="q-answer">The Eiffel Tower</div>
      </div>
      <div class="comp-q" onclick="this.classList.toggle('revealed')">
        <div class="q-text">What can&rsquo;t she understand in Situation 2?</div>
        <div class="q-answer">The menu (at a restaurant)</div>
      </div>
      <div class="comp-q" onclick="this.classList.toggle('revealed')">
        <div class="q-text">What can Gabriela speak?</div>
        <div class="q-answer">English</div>
      </div>
    </div>
  </div>
</div>

<!-- SLIDE 220: L8 ARTIFACT - EMERGENCY CARD -->
<div class="slide slide-light" data-slide="220" data-phase="4" data-lesson="8" data-teacher="<strong>Artefato (3 min):</strong> 'Look! This is Gabriela's Emergency Card &mdash; like a survival kit in your pocket!' Pergunte: 'What phrases does Gabriela have on her card? When would she use each one?' Gabriela le cada frase em voz alta.">
  <div class="slide-inner">
    <h2 class="slide-heading">Gabriela&rsquo;s Emergency <span class="accent">Card</span></h2>
    <div style="background:#fff;border-radius:16px;overflow:hidden;max-width:420px;margin:0 auto;box-shadow:0 20px 60px rgba(0,0,0,.1);border:2px solid var(--accent)">
      <div style="background:linear-gradient(135deg,#dc2626,#991b1b);color:#fff;padding:1.2rem 1.5rem;display:flex;align-items:center;gap:1rem">
        <div style="width:50px;height:50px;border-radius:50%;background:rgba(255,255,255,.2);display:flex;align-items:center;justify-content:center;font-size:1.5rem;font-weight:800;">!</div>
        <div>
          <div style="font-weight:700;font-size:1.1rem;letter-spacing:.5px;">EMERGENCY CARD</div>
          <div style="font-size:.7rem;opacity:.7;text-transform:uppercase;letter-spacing:2px;">Gabriela Pires &mdash; Paris 2027</div>
        </div>
      </div>
      <div style="padding:1.2rem 1.5rem;">
        <div style="display:grid;grid-template-columns:auto 1fr;gap:.5rem 1rem;font-size:.9rem;line-height:1.7;">
          <strong style="color:var(--accent)">Name</strong><span>Gabriela Pires</span>
          <strong style="color:var(--accent)">From</strong><span>S&atilde;o Paulo, Brazil</span>
          <strong style="color:var(--accent)">Nationality</strong><span>Brazilian</span>
          <strong style="color:var(--accent)">I can speak</strong><span>English and Portuguese</span>
          <strong style="color:var(--accent)">I can&rsquo;t speak</strong><span>French</span>
        </div>
        <div style="margin-top:1rem;padding-top:1rem;border-top:1px solid var(--border);">
          <div style="font-weight:700;color:#dc2626;margin-bottom:.5rem;font-size:.85rem;text-transform:uppercase;letter-spacing:1px;">Emergency Phrases</div>
          <div style="font-size:.88rem;line-height:2;color:var(--text);">
            1. Can you help me, please?<br>
            2. I can&rsquo;t find my hotel.<br>
            3. Can you speak slower, please?<br>
            4. Can you show me on the map?<br>
            5. I can speak English.
          </div>
        </div>
      </div>
      <div style="background:var(--accent-dim);padding:.8rem 1.5rem;font-size:.78rem;color:var(--text-mid);text-align:center;border-top:1px solid var(--border);">
        Keep this card in your pocket &mdash; it can save your day!
      </div>
    </div>
  </div>
</div>

<!-- SLIDE 221: L8 CHAPTER 5 TRANSITION -->
<div class="slide slide-image" data-slide="221" data-phase="5" data-lesson="8" data-teacher="<strong>Transicao (10s):</strong> 'Time to practice! Show me you CAN ask for help!' Avance." style="background-image:url('https://images.unsplash.com/photo-1499856871958-5b9627545d1a?w=600&q=80')">
  <div class="slide-inner">
    <div class="chapter-label">Chapter 5</div>
    <h1 class="slide-title"><span class="accent">Practice</span></h1>
    <p class="slide-subtitle">CAN and CAN&rsquo;T in action</p>
  </div>
</div>

<!-- SLIDE 222: L8 QUICK FIRE -->
<div class="slide slide-light" data-slide="222" data-phase="5" data-lesson="8" data-teacher="<strong>Quick Fire (6 min):</strong> Uma pergunta por vez. Gabriela responde ORALMENTE primeiro, depois clique Show Answer. Se travar: 'Start with CAN YOU...' ou 'Start with I CAN'T...' Score: 6 acertos = confetti!">
  <div class="slide-inner">
    <h2 class="slide-heading">Quick <span class="accent">Fire</span></h2>
    <div id="qf8" style="min-height:200px;">
      <div class="qf-item" data-qf="1" style="display:block;">
        <p style="font-size:1.2rem;text-align:center;margin-bottom:1rem;">You are lost. Ask someone for <strong>help</strong>.</p>
        <div style="text-align:center;">
          <button class="btn-secondary" onclick="this.nextElementSibling.style.display='block';this.style.display='none'">Show Answer</button>
          <p style="display:none;font-size:1.1rem;color:var(--accent);font-weight:700;">Can you help me? / Excuse me, can you help me?</p>
        </div>
      </div>
      <div class="qf-item" data-qf="2" style="display:none;">
        <p style="font-size:1.2rem;text-align:center;margin-bottom:1rem;">You cannot find the metro station. Tell someone.</p>
        <div style="text-align:center;">
          <button class="btn-secondary" onclick="this.nextElementSibling.style.display='block';this.style.display='none'">Show Answer</button>
          <p style="display:none;font-size:1.1rem;color:var(--accent);font-weight:700;">I can&rsquo;t find the metro station.</p>
        </div>
      </div>
      <div class="qf-item" data-qf="3" style="display:none;">
        <p style="font-size:1.2rem;text-align:center;margin-bottom:1rem;">Someone speaks too fast. What do you say?</p>
        <div style="text-align:center;">
          <button class="btn-secondary" onclick="this.nextElementSibling.style.display='block';this.style.display='none'">Show Answer</button>
          <p style="display:none;font-size:1.1rem;color:var(--accent);font-weight:700;">Can you speak slower, please?</p>
        </div>
      </div>
      <div class="qf-item" data-qf="4" style="display:none;">
        <p style="font-size:1.2rem;text-align:center;margin-bottom:1rem;">You want someone to show you on the map. Ask!</p>
        <div style="text-align:center;">
          <button class="btn-secondary" onclick="this.nextElementSibling.style.display='block';this.style.display='none'">Show Answer</button>
          <p style="display:none;font-size:1.1rem;color:var(--accent);font-weight:700;">Can you show me on the map?</p>
        </div>
      </div>
      <div class="qf-item" data-qf="5" style="display:none;">
        <p style="font-size:1.2rem;text-align:center;margin-bottom:1rem;">Someone asks: &ldquo;Can you speak French?&rdquo; Answer no, but say you CAN speak English.</p>
        <div style="text-align:center;">
          <button class="btn-secondary" onclick="this.nextElementSibling.style.display='block';this.style.display='none'">Show Answer</button>
          <p style="display:none;font-size:1.1rem;color:var(--accent);font-weight:700;">No, I can&rsquo;t. But I can speak English.</p>
        </div>
      </div>
      <div class="qf-item" data-qf="6" style="display:none;">
        <p style="font-size:1.2rem;text-align:center;margin-bottom:1rem;">You didn&rsquo;t hear. Ask politely for the person to repeat.</p>
        <div style="text-align:center;">
          <button class="btn-secondary" onclick="this.nextElementSibling.style.display='block';this.style.display='none'">Show Answer</button>
          <p style="display:none;font-size:1.1rem;color:var(--accent);font-weight:700;">Could you repeat that, please?</p>
        </div>
      </div>
    </div>
    <div style="text-align:center;margin-top:1rem;">
      <span id="qf8score" style="font-weight:700;color:var(--accent);">1 / 6</span>
      <button class="btn-primary" style="margin-left:1rem;" onclick="var items=document.querySelectorAll('#qf8 .qf-item');var cur=0;items.forEach(function(it,i){if(it.style.display==='block')cur=i});if(cur<items.length-1){items[cur].style.display='none';items[cur+1].style.display='block';document.getElementById('qf8score').textContent=(cur+2)+' / 6';}">Next Question</button>
    </div>
  </div>
</div>

<!-- SLIDE 223: L8 SPOT THE ERROR -->
<div class="slide slide-light" data-slide="223" data-phase="5" data-lesson="8" data-teacher="<strong>Spot the Error (4 min):</strong> Gabriela identifica o erro PRIMEIRO. Depois clique para revelar. Foco: can + base verb (sem TO, sem -ING), word order nas perguntas.">
  <div class="slide-inner">
    <h2 class="slide-heading">Spot the <span class="accent">Error</span></h2>
    <div style="display:flex;flex-direction:column;gap:.8rem;">
      <div class="error-card" onclick="this.classList.toggle('revealed')" style="background:#fff;border:1px solid #e8e4df;border-radius:10px;padding:1rem 1.2rem;cursor:pointer;transition:all .3s;">
        <div class="error-wrong" style="font-size:1rem;color:var(--danger);text-decoration:line-through;">&ldquo;I can to speak English.&rdquo;</div>
        <div class="error-correct" style="display:none;font-size:1rem;color:var(--success);font-weight:700;margin-top:.5rem;">&ldquo;I can speak English.&rdquo; &mdash; No &ldquo;to&rdquo; after CAN!</div>
      </div>
      <div class="error-card" onclick="this.classList.toggle('revealed')" style="background:#fff;border:1px solid #e8e4df;border-radius:10px;padding:1rem 1.2rem;cursor:pointer;transition:all .3s;">
        <div class="error-wrong" style="font-size:1rem;color:var(--danger);text-decoration:line-through;">&ldquo;Can you speaking English?&rdquo;</div>
        <div class="error-correct" style="display:none;font-size:1rem;color:var(--success);font-weight:700;margin-top:.5rem;">&ldquo;Can you speak English?&rdquo; &mdash; Base verb, no -ing!</div>
      </div>
      <div class="error-card" onclick="this.classList.toggle('revealed')" style="background:#fff;border:1px solid #e8e4df;border-radius:10px;padding:1rem 1.2rem;cursor:pointer;transition:all .3s;">
        <div class="error-wrong" style="font-size:1rem;color:var(--danger);text-decoration:line-through;">&ldquo;She cans swim.&rdquo;</div>
        <div class="error-correct" style="display:none;font-size:1rem;color:var(--success);font-weight:700;margin-top:.5rem;">&ldquo;She can swim.&rdquo; &mdash; CAN never changes (no -s)!</div>
      </div>
      <div class="error-card" onclick="this.classList.toggle('revealed')" style="background:#fff;border:1px solid #e8e4df;border-radius:10px;padding:1rem 1.2rem;cursor:pointer;transition:all .3s;">
        <div class="error-wrong" style="font-size:1rem;color:var(--danger);text-decoration:line-through;">&ldquo;You can help me?&rdquo;</div>
        <div class="error-correct" style="display:none;font-size:1rem;color:var(--success);font-weight:700;margin-top:.5rem;">&ldquo;Can you help me?&rdquo; &mdash; CAN goes before the subject in questions!</div>
      </div>
    </div>
  </div>
</div>

<!-- SLIDE 224: L8 CAN vs CAN'T DRILL -->
<div class="slide slide-light" data-slide="224" data-phase="5" data-lesson="8" data-teacher="<strong>CAN vs CAN'T Drill (4 min):</strong> Mostre cada frase. Gabriela ouve e diz se e CAN ou CAN'T. Foco na diferenca de pronuncia: can /ken/ (atono, rapido) vs can't /kant/ (tonico, T final claro). Drill 3x cada.">
  <div class="slide-inner">
    <h2 class="slide-heading">CAN or <span class="accent">CAN&rsquo;T</span>?</h2>
    <p style="text-align:center;font-size:.9rem;color:var(--text-mid);margin-bottom:1.5rem;">Listen carefully. Is it CAN or CAN&rsquo;T? Click to check.</p>
    <div style="display:flex;flex-direction:column;gap:1rem;margin-top:1rem;">
      <div style="background:#fff;border:1px solid #e8e4df;border-radius:10px;padding:1rem 1.2rem;display:flex;align-items:center;gap:1rem;cursor:pointer;" onclick="this.querySelector('.answer').style.display='block'">
        <button class="audio-btn-sm" onclick="event.stopPropagation();speakText('I can swim.',this)"><svg viewBox="0 0 24 24"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/></svg></button>
        <span style="flex:1;font-size:1rem;">I ___ swim.</span>
        <span class="answer" style="display:none;color:var(--success);font-weight:700;">CAN (I can swim.)</span>
      </div>
      <div style="background:#fff;border:1px solid #e8e4df;border-radius:10px;padding:1rem 1.2rem;display:flex;align-items:center;gap:1rem;cursor:pointer;" onclick="this.querySelector('.answer').style.display='block'">
        <button class="audio-btn-sm" onclick="event.stopPropagation();speakText('She can\\'t cook.',this)"><svg viewBox="0 0 24 24"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/></svg></button>
        <span style="flex:1;font-size:1rem;">She ___ cook.</span>
        <span class="answer" style="display:none;color:var(--danger);font-weight:700;">CAN&rsquo;T (She can&rsquo;t cook.)</span>
      </div>
      <div style="background:#fff;border:1px solid #e8e4df;border-radius:10px;padding:1rem 1.2rem;display:flex;align-items:center;gap:1rem;cursor:pointer;" onclick="this.querySelector('.answer').style.display='block'">
        <button class="audio-btn-sm" onclick="event.stopPropagation();speakText('Can he play guitar?',this)"><svg viewBox="0 0 24 24"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/></svg></button>
        <span style="flex:1;font-size:1rem;">___ he play guitar?</span>
        <span class="answer" style="display:none;color:var(--success);font-weight:700;">CAN (Can he play guitar?)</span>
      </div>
      <div style="background:#fff;border:1px solid #e8e4df;border-radius:10px;padding:1rem 1.2rem;display:flex;align-items:center;gap:1rem;cursor:pointer;" onclick="this.querySelector('.answer').style.display='block'">
        <button class="audio-btn-sm" onclick="event.stopPropagation();speakText('They can\\'t speak Japanese.',this)"><svg viewBox="0 0 24 24"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/></svg></button>
        <span style="flex:1;font-size:1rem;">They ___ speak Japanese.</span>
        <span class="answer" style="display:none;color:var(--danger);font-weight:700;">CAN&rsquo;T (They can&rsquo;t speak Japanese.)</span>
      </div>
    </div>
  </div>
</div>

<!-- SLIDE 225: L8 CHAPTER 6 TRANSITION -->
<div class="slide slide-image" data-slide="225" data-phase="6" data-lesson="8" data-teacher="<strong>Transicao (10s):</strong> 'From guided to free &mdash; show what you learned!' Avance." style="background-image:url('https://images.unsplash.com/photo-1499856871958-5b9627545d1a?w=600&q=80')">
  <div class="slide-inner">
    <div class="chapter-label">Chapter 6</div>
    <h1 class="slide-title">Your <span class="accent">Turn</span></h1>
    <p class="slide-subtitle">From guided to free &mdash; show what you learned</p>
  </div>
</div>

<!-- SLIDE 226: L8 ROLE-PLAY GUIDED -->
<div class="slide slide-dark" data-slide="226" data-phase="6" data-lesson="8" data-teacher="<strong>Role-play Guided (5 min):</strong> Professor = passerby near metro. Gabriela esta perdida no metro. Keywords visiveis. CCQ: 'How do you ask for help politely?' &rarr; 'Can you help me? / Could you help me, please?' Se travar: modele a frase e ela repete.">
  <div class="slide-inner">
    <h2 class="slide-heading" style="color:#fff">Role-Play: <span class="accent">Guided</span></h2>
    <div class="roleplay-card" style="background:linear-gradient(135deg,rgba(212,50,106,.15),rgba(212,50,106,.05));border:1px solid rgba(212,50,106,.3);border-radius:12px;padding:1.5rem;">
      <div style="display:flex;align-items:center;gap:.8rem;margin-bottom:1rem;">
        <svg viewBox="0 0 24 24" width="32" height="32" fill="none" stroke="var(--accent)" stroke-width="1.5"><circle cx="12" cy="12" r="10"/><path d="M9.09 9a3 3 0 015.83 1c0 2-3 3-3 3M12 17h.01"/></svg>
        <div>
          <div style="font-weight:700;font-size:1.1rem;color:#fff;">Lost at the Metro Station</div>
          <div style="font-size:.8rem;color:rgba(255,255,255,.6);">Teacher = passerby &middot; Gabriela = herself</div>
        </div>
      </div>
      <p style="color:rgba(255,255,255,.8);font-size:.9rem;margin-bottom:1rem;">You are lost near the metro. Ask for help, say what you cannot find, and ask the person to speak slower.</p>
      <div style="display:flex;flex-wrap:wrap;gap:.4rem;">
        <span style="padding:.3rem .8rem;border:1px solid var(--accent);border-radius:20px;font-size:.82rem;color:var(--accent);">Can you help me?</span>
        <span style="padding:.3rem .8rem;border:1px solid var(--accent);border-radius:20px;font-size:.82rem;color:var(--accent);">I can&rsquo;t find...</span>
        <span style="padding:.3rem .8rem;border:1px solid var(--accent);border-radius:20px;font-size:.82rem;color:var(--accent);">slower, please</span>
        <span style="padding:.3rem .8rem;border:1px solid var(--accent);border-radius:20px;font-size:.82rem;color:var(--accent);">show me</span>
      </div>
    </div>
  </div>
</div>

<!-- SLIDE 227: L8 ROLE-PLAY SEMI-FREE -->
<div class="slide slide-dark" data-slide="227" data-phase="6" data-lesson="8" data-teacher="<strong>Role-play Semi-free (5 min):</strong> Professor = receptionist no hotel vizinho. MENOS keywords. Gabriela nao acha o hotel dela e pede ajuda na recepcao de outro hotel. Se travar em 5s, de 1 palavra de pista. Elogie fluencia.">
  <div class="slide-inner">
    <h2 class="slide-heading" style="color:#fff">Role-Play: <span class="accent">Semi-Free</span></h2>
    <div class="roleplay-card" style="background:linear-gradient(135deg,rgba(0,48,128,.15),rgba(0,48,128,.05));border:1px solid rgba(0,48,128,.3);border-radius:12px;padding:1.5rem;">
      <div style="display:flex;align-items:center;gap:.8rem;margin-bottom:1rem;">
        <svg viewBox="0 0 24 24" width="32" height="32" fill="none" stroke="var(--accent)" stroke-width="1.5"><path d="M17 21v-2a4 4 0 00-4-4H5a4 4 0 00-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 00-3-3.87M16 3.13a4 4 0 010 7.75"/></svg>
        <div>
          <div style="font-weight:700;font-size:1.1rem;color:#fff;">Can&rsquo;t Find the Hotel</div>
          <div style="font-size:.8rem;color:rgba(255,255,255,.6);">Less help this time!</div>
        </div>
      </div>
      <p style="color:rgba(255,255,255,.8);font-size:.9rem;margin-bottom:1rem;">You walk into another hotel. Tell the receptionist you are lost, you can&rsquo;t find YOUR hotel, and ask for help with the map.</p>
      <div style="display:flex;flex-wrap:wrap;gap:.4rem;">
        <span style="padding:.3rem .8rem;border:1px solid rgba(255,255,255,.3);border-radius:20px;font-size:.82rem;color:rgba(255,255,255,.5);">help</span>
        <span style="padding:.3rem .8rem;border:1px solid rgba(255,255,255,.3);border-radius:20px;font-size:.82rem;color:rgba(255,255,255,.5);">map</span>
      </div>
    </div>
  </div>
</div>

<!-- SLIDE 228: L8 ROLE-PLAY FREE -->
<div class="slide slide-dark" data-slide="228" data-phase="6" data-lesson="8" data-teacher="<strong>Role-play Free (5 min):</strong> Professor = turista que fala rapido. ZERO keywords. Gabriela precisa usar TODAS as estrategias: pedir para repetir, falar mais devagar, mostrar no mapa. Delayed feedback: anote erros e corrija DEPOIS. Elogie muito.">
  <div class="slide-inner">
    <h2 class="slide-heading" style="color:#fff">Role-Play: <span class="accent">Free</span></h2>
    <div class="roleplay-card" style="background:linear-gradient(135deg,rgba(22,163,74,.12),rgba(22,163,74,.04));border:1px solid rgba(22,163,74,.3);border-radius:12px;padding:1.5rem;">
      <div style="display:flex;align-items:center;gap:.8rem;margin-bottom:1rem;">
        <svg viewBox="0 0 24 24" width="32" height="32" fill="none" stroke="#16a34a" stroke-width="1.5"><circle cx="12" cy="12" r="10"/><path d="M9.09 9a3 3 0 015.83 1c0 2-3 3-3 3M12 17h.01"/></svg>
        <div>
          <div style="font-weight:700;font-size:1.1rem;color:#fff;">General Emergency</div>
          <div style="font-size:.8rem;color:rgba(255,255,255,.6);">No keywords &mdash; you are on your own!</div>
        </div>
      </div>
      <p style="color:rgba(255,255,255,.8);font-size:.9rem;">Something went wrong in Paris (you choose what!). Find a stranger and use ALL your survival English to get help. Use can, can&rsquo;t, repeat, slower, show, map.</p>
    </div>
  </div>
</div>

<!-- SLIDE 229: L8 CHAPTER 7 TRANSITION -->
<div class="slide slide-image" data-slide="229" data-phase="7" data-lesson="8" data-teacher="<strong>Transicao (10s):</strong> 'Amazing work today! Let us wrap up.' Avance." style="background-image:url('https://images.unsplash.com/photo-1499856871958-5b9627545d1a?w=600&q=80')">
  <div class="slide-inner">
    <div class="chapter-label">Chapter 7</div>
    <h1 class="slide-title">Wrap-<span class="accent">Up</span></h1>
    <p class="slide-subtitle">Your survival kit for Paris emergencies</p>
  </div>
</div>

<!-- SLIDE 230: L8 SURVIVAL CARD -->
<div class="slide slide-dark" data-slide="230" data-phase="7" data-lesson="8" data-teacher="<strong>Survival Card (2 min):</strong> Leia cada frase com Gabriela. Toque audio. Ela repete 2x cada. Estas 5 frases sao as que ela PRECISA quando estiver perdida em Paris.">
  <div class="slide-inner">
    <h2 class="slide-heading" style="color:#fff">Survival <span class="accent">Card</span></h2>
    <div style="display:flex;flex-direction:column;gap:.6rem;margin-top:1.5rem;">
      <div class="survival-item-ic" style="display:flex;align-items:center;gap:1rem;background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.1);border-radius:10px;padding:.8rem 1rem;">
        <span style="color:var(--accent);font-weight:800;font-size:1.1rem;">1</span>
        <span style="flex:1;font-size:.95rem;">Can you help me, please?</span>
        <button class="audio-btn-sm" onclick="speakText('Can you help me, please?',this)"><svg viewBox="0 0 24 24"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/></svg> Listen</button>
      </div>
      <div class="survival-item-ic" style="display:flex;align-items:center;gap:1rem;background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.1);border-radius:10px;padding:.8rem 1rem;">
        <span style="color:var(--accent);font-weight:800;font-size:1.1rem;">2</span>
        <span style="flex:1;font-size:.95rem;">I can&rsquo;t find my hotel.</span>
        <button class="audio-btn-sm" onclick="speakText('I can\\'t find my hotel.',this)"><svg viewBox="0 0 24 24"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/></svg> Listen</button>
      </div>
      <div class="survival-item-ic" style="display:flex;align-items:center;gap:1rem;background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.1);border-radius:10px;padding:.8rem 1rem;">
        <span style="color:var(--accent);font-weight:800;font-size:1.1rem;">3</span>
        <span style="flex:1;font-size:.95rem;">Can you speak slower, please?</span>
        <button class="audio-btn-sm" onclick="speakText('Can you speak slower, please?',this)"><svg viewBox="0 0 24 24"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/></svg> Listen</button>
      </div>
      <div class="survival-item-ic" style="display:flex;align-items:center;gap:1rem;background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.1);border-radius:10px;padding:.8rem 1rem;">
        <span style="color:var(--accent);font-weight:800;font-size:1.1rem;">4</span>
        <span style="flex:1;font-size:.95rem;">Can you show me on the map?</span>
        <button class="audio-btn-sm" onclick="speakText('Can you show me on the map?',this)"><svg viewBox="0 0 24 24"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/></svg> Listen</button>
      </div>
      <div class="survival-item-ic" style="display:flex;align-items:center;gap:1rem;background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.1);border-radius:10px;padding:.8rem 1rem;">
        <span style="color:var(--accent);font-weight:800;font-size:1.1rem;">5</span>
        <span style="flex:1;font-size:.95rem;">I can speak English.</span>
        <button class="audio-btn-sm" onclick="speakText('I can speak English.',this)"><svg viewBox="0 0 24 24"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/></svg> Listen</button>
      </div>
    </div>
  </div>
</div>

<!-- SLIDE 231: L8 CHECKLIST -->
<div class="slide slide-dark" data-slide="231" data-phase="7" data-lesson="8" data-teacher="<strong>What I Learned (2 min):</strong> Gabriela leia cada item em voz alta. Se disser 'sim, eu sei fazer isso' para TODAS &mdash; a licao esta dominada. Marque os checks juntos. 5/5 = aula concluida no sistema.">
  <div class="slide-inner">
    <h2 class="slide-heading" style="color:#fff">What I <span class="accent">Learned</span></h2>
    <ul class="checklist" id="checklist-8" style="list-style:none;display:flex;flex-direction:column;gap:.6rem;margin-top:1.5rem;">
      <li style="display:flex;align-items:center;gap:.8rem;background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.1);border-radius:8px;padding:.7rem 1rem;cursor:pointer;" onclick="this.querySelector('input').click()">
        <input type="checkbox" onchange="toggleChecklist(this)" style="width:20px;height:20px;accent-color:var(--accent);">
        <span style="font-size:.9rem;">I can ask for help using &ldquo;Can you help me?&rdquo;</span>
      </li>
      <li style="display:flex;align-items:center;gap:.8rem;background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.1);border-radius:8px;padding:.7rem 1rem;cursor:pointer;" onclick="this.querySelector('input').click()">
        <input type="checkbox" onchange="toggleChecklist(this)" style="width:20px;height:20px;accent-color:var(--accent);">
        <span style="font-size:.9rem;">I can say what I can and can&rsquo;t do (I can speak English / I can&rsquo;t find my hotel).</span>
      </li>
      <li style="display:flex;align-items:center;gap:.8rem;background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.1);border-radius:8px;padding:.7rem 1rem;cursor:pointer;" onclick="this.querySelector('input').click()">
        <input type="checkbox" onchange="toggleChecklist(this)" style="width:20px;height:20px;accent-color:var(--accent);">
        <span style="font-size:.9rem;">I can ask someone to speak slower or repeat.</span>
      </li>
      <li style="display:flex;align-items:center;gap:.8rem;background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.1);border-radius:8px;padding:.7rem 1rem;cursor:pointer;" onclick="this.querySelector('input').click()">
        <input type="checkbox" onchange="toggleChecklist(this)" style="width:20px;height:20px;accent-color:var(--accent);">
        <span style="font-size:.9rem;">I know the vocabulary: speak, understand, help, repeat, find, show, slower, map.</span>
      </li>
      <li style="display:flex;align-items:center;gap:.8rem;background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.1);border-radius:8px;padding:.7rem 1rem;cursor:pointer;" onclick="this.querySelector('input').click()">
        <input type="checkbox" onchange="toggleChecklist(this)" style="width:20px;height:20px;accent-color:var(--accent);">
        <span style="font-size:.9rem;">I can survive being lost in Paris using my emergency phrases.</span>
      </li>
    </ul>
  </div>
</div>

<!-- SLIDE 232: L8 BADGE -->
<div class="slide slide-dark" data-slide="232" data-phase="7" data-lesson="8" data-teacher="<strong>Badge (1 min):</strong> 'You earned your Survival Hero Stamp!' Confetti. Energia alta. Preview: proxima aula sobre direcoes e se locomover. Diga o homework ORALMENTE: 1) Praticar as 5 frases de emergencia no espelho (30 segundos cada). 2) Assistir 10 min de Emily in Paris e anotar toda vez que alguem pede ajuda ou diz 'can/can't'. 3) Escrever 5 coisas que voce CAN do e 5 que voce CAN'T do.">
  <div class="slide-inner">
    <div class="badge-card">
      <div class="badge-icon">
        <div class="sparkles"><div class="sparkle"></div><div class="sparkle"></div><div class="sparkle"></div><div class="sparkle"></div><div class="sparkle"></div><div class="sparkle"></div></div>
        <div class="badge-circle"><svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M9.09 9a3 3 0 015.83 1c0 2-3 3-3 3M12 17h.01"/></svg></div>
      </div>
      <h2 class="slide-heading">Survival Hero <span class="accent">Stamp</span>!</h2>
      <p style="color:rgba(255,255,255,.7);font-size:1rem">Day 8: Abilities, Possibilities &amp; Asking for Help &mdash; Complete</p>
    </div>
  </div>
</div>

<!-- SLIDE 233: L8 CLOSING -->
<div class="slide slide-dark" data-slide="233" data-phase="7" data-lesson="8" data-teacher="<strong>Fechamento (1 min):</strong> 'Proxima aula: directions and getting around Paris! See you!' Diga o homework ORALMENTE.">
  <div class="slide-inner" style="text-align:center">
    <div class="chapter-label">Coming Up Next</div>
    <h2 class="slide-heading">Lesson 9: <span class="accent">Where Is It?</span></h2>
    <p style="color:rgba(255,255,255,.6);font-size:1rem;margin-top:1rem">Directions &amp; Getting Around Paris</p>
    <p style="color:rgba(255,255,255,.4);font-size:.85rem;margin-top:2rem">Day 8 &mdash; Complete</p>
  </div>
</div>
'''

# ============================================================
# COMPLEMENTARY CONTENT FOR AULA 8
# ============================================================
COMPLEMENTARY_HTML = '''
<h3 style="font-family:'Cormorant Garamond',serif;font-size:1.3rem;font-weight:600;color:var(--accent);margin:2rem 0 1rem;">Aula 8 &mdash; Abilities &amp; Asking for Help</h3>
<div class="media-grid" style="margin-bottom:2rem;">
  <div class="media-card-wrapper" data-media="l8-series">
    <label class="media-check"><input type="checkbox" onchange="toggleMediaDone(this)"></label>
    <div class="media-card">
      <div class="media-thumb series"></div>
      <div class="media-info">
        <div class="media-type">S&eacute;rie</div>
        <h5>Emily in Paris &mdash; S01E01 (Netflix)</h5>
        <p>Emily chega em Paris e n&atilde;o fala franc&ecirc;s. Preste aten&ccedil;&atilde;o em como ela pede ajuda e usa &ldquo;can&rdquo; e &ldquo;can&rsquo;t&rdquo; nas primeiras cenas.</p>
        <div class="media-tip">Foco: anote toda vez que algu&eacute;m diz &ldquo;can you...?&rdquo; ou &ldquo;I can&rsquo;t...&rdquo; nos primeiros 15 minutos.</div>
      </div>
    </div>
  </div>
  <div class="media-card-wrapper" data-media="l8-youtube">
    <label class="media-check"><input type="checkbox" onchange="toggleMediaDone(this)"></label>
    <div class="media-card">
      <div class="media-thumb youtube"></div>
      <div class="media-info">
        <div class="media-type">YouTube</div>
        <h5>CAN and CAN&rsquo;T in English &mdash; English with Lucy</h5>
        <p>V&iacute;deo did&aacute;tico sobre como usar CAN e CAN&rsquo;T corretamente. Foco na pron&uacute;ncia e nos erros mais comuns.</p>
        <div class="media-tip">Assista 1x e anote a diferen&ccedil;a de pron&uacute;ncia entre CAN (fraco) e CAN&rsquo;T (forte, com T).</div>
      </div>
    </div>
  </div>
  <div class="media-card-wrapper" data-media="l8-podcast">
    <label class="media-check"><input type="checkbox" onchange="toggleMediaDone(this)"></label>
    <div class="media-card">
      <div class="media-thumb podcast"></div>
      <div class="media-info">
        <div class="media-type">Atividade</div>
        <h5>My CAN / CAN&rsquo;T List</h5>
        <p>Escreva uma lista: 5 coisas que voc&ecirc; CAN do em ingl&ecirc;s (I can speak English, I can understand songs...) e 5 coisas que voc&ecirc; CAN&rsquo;T do ainda (I can&rsquo;t speak French...).</p>
        <div class="media-tip">Use frases completas! Traga para a pr&oacute;xima aula para compartilhar.</div>
      </div>
    </div>
  </div>
</div>'''

# ============================================================
# IN CLASS MENU CARD
# ============================================================
INCLASS_MENU_CARD = '''
<div class="inclass-lesson-card" onclick="startLesson(8)">
  <div class="ilc-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M9.09 9a3 3 0 015.83 1c0 2-3 3-3 3M12 17h.01"/></svg></div>
  <div class="ilc-info">
    <div class="ilc-number">Lesson 08</div>
    <div class="ilc-title">Can You Do That?</div>
    <div class="ilc-desc">Abilities, asking for help &amp; survival English &mdash; Paris emergency &mdash; 60 min &mdash; 29 slides</div>
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
    # Find first entry in audioMap — use aula 7 first entry as marker
    marker = '"Country": "/audio/gabriela-pires/country.mp3?v=2"'
    if marker in html:
        html = html.replace(marker, audio_entries + ',\n  ' + marker)
        print(f"  [OK] Inserted audioMap entries before Aula 7 entries")
    else:
        # Try alternate markers
        marker2 = '"Country"'
        if marker2 in html:
            html = html.replace(marker2, audio_entries + ',\n  ' + marker2, 1)
            print(f"  [OK] Inserted audioMap entries (alt marker)")
        else:
            # Try finding audioMap opening
            am_match = re.search(r'const audioMap\s*=\s*\{', html)
            if am_match:
                insert_pos = am_match.end()
                html = html[:insert_pos] + '\n' + audio_entries + ',\n' + html[insert_pos:]
                print(f"  [OK] Inserted audioMap entries after opening brace")

    # 2. Replace Aula 8 placeholder in Pre-class
    pattern = r'<div class="lesson-card">\s*<div class="lesson-header"[^>]*onclick="toggleLesson\(this\)">\s*<div class="lesson-header-img"[^>]*opacity:0\.35[^>]*></div>\s*<div class="lesson-header-content">\s*<div class="lesson-number">Aula 08[^<]*</div>'
    match = re.search(pattern, html)
    if match:
        start = match.start()
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
                    print(f"  [OK] Replaced Aula 8 placeholder via regex")
                    found_end = True
                    break
            i += 1
        if not found_end:
            print("  [WARN] Could not find end of Aula 8 placeholder")
    else:
        # Try alternate patterns
        alt_patterns = [
            r'Aula 08[^<]*Pre-class.*?Can You Do That\?.*?opacity:0\.35',
            r'Aula 08.*?Can You Do That.*?opacity:0\.35',
            r'Aula 08.*?Conte[uú]do ser[aá] adicionado'
        ]
        found = False
        for alt_pat in alt_patterns:
            alt_match = re.search(alt_pat, html, re.DOTALL)
            if alt_match:
                search_start = max(0, alt_match.start() - 200)
                card_start = html.rfind('<div class="lesson-card">', search_start, alt_match.start())
                if card_start == -1:
                    card_start = html.rfind('<div class="lesson-card"', search_start, alt_match.start())
                if card_start >= 0:
                    depth = 0
                    i = card_start
                    while i < len(html):
                        if html[i:i+4] == '<div':
                            depth += 1
                        elif html[i:i+6] == '</div>':
                            depth -= 1
                            if depth == 0:
                                end = i + 6
                                html = html[:card_start] + PRECLASS_HTML + html[end:]
                                print(f"  [OK] Replaced Aula 8 placeholder via alt pattern")
                                found = True
                                break
                        i += 1
                if found:
                    break
        if not found:
            print("  [WARN] Could not find Aula 8 placeholder - may need manual insertion")

    # 3. Insert slides before </div><!-- /slides-container -->
    if not is_aluno:
        slide_marker = '</div><!-- /slides-container -->'
        if slide_marker in html:
            html = html.replace(slide_marker, SLIDES_HTML + '\n' + slide_marker)
            print(f"  [OK] Inserted 29 slides")
        else:
            for m in ['</div><!-- /slides-container', '</div>\n\n<!-- Navigation Bar']:
                if m in html:
                    html = html.replace(m, SLIDES_HTML + '\n' + m)
                    print(f"  [OK] Inserted slides (variant marker)")
                    break

    # 4. Update lessonRanges
    if not is_aluno:
        old_ranges = "var lessonRanges = {1:[1,28], 2:[29,55], 3:[56,85], 4:[86,115], 5:[116,146], 6:[147,175], 7:[176,204]};"
        new_ranges = "var lessonRanges = {1:[1,28], 2:[29,55], 3:[56,85], 4:[86,115], 5:[116,146], 6:[147,175], 7:[176,204], 8:[205,233]};"
        if old_ranges in html:
            html = html.replace(old_ranges, new_ranges)
            print(f"  [OK] Updated lessonRanges")
        else:
            print("  [WARN] Could not find lessonRanges to update")

    # 5. Update totalSlides
    if not is_aluno:
        if 'var totalSlides = 204;' in html:
            html = html.replace('var totalSlides = 204;', 'var totalSlides = 233;')
            print(f"  [OK] Updated totalSlides to 233")
        else:
            print("  [WARN] Could not find totalSlides = 204 to update")

    # 6. Add IN CLASS menu card (after startLesson(7) card)
    if not is_aluno:
        menu_marker = 'onclick="startLesson(7)"'
        if menu_marker in html:
            idx = html.index(menu_marker)
            card_start = html.rfind('<div class="inclass-lesson-card"', max(0, idx - 200), idx)
            if card_start >= 0:
                depth = 0
                i = card_start
                while i < len(html):
                    if html[i:i+4] == '<div':
                        depth += 1
                    elif html[i:i+6] == '</div>':
                        depth -= 1
                        if depth == 0:
                            insert_pos = i + 6
                            html = html[:insert_pos] + '\n' + INCLASS_MENU_CARD + html[insert_pos:]
                            print(f"  [OK] Added IN CLASS menu card after Lesson 7")
                            break
                    i += 1
            else:
                print("  [WARN] Could not find Lesson 7 menu card container")
        else:
            alt_marker = '<div style="background:var(--bg-card);border:1px solid var(--border);padding:2rem;border-radius:6px;text-align:center;margin-top:2rem;">'
            if alt_marker in html:
                html = html.replace(alt_marker, INCLASS_MENU_CARD + '\n' + alt_marker)
                print(f"  [OK] Added IN CLASS menu card (before placeholder)")

    # 7. Add Complementary content (before Paris & Viagem 2027)
    comp_marker = 'Paris &amp; Viagem 2027'
    if comp_marker in html:
        idx = html.index(comp_marker)
        h3_start = html.rfind('<h3', max(0, idx - 200), idx)
        if h3_start > 0:
            html = html[:h3_start] + COMPLEMENTARY_HTML + '\n' + html[h3_start:]
            print(f"  [OK] Added Complementary content")
    else:
        # Try after aula 7 complementary
        comp_marker3 = 'data-media="l7-podcast"'
        if comp_marker3 in html:
            idx = html.index(comp_marker3)
            search_pos = idx
            for _ in range(5):
                search_pos = html.find('</div>', search_pos + 6)
            if search_pos > 0:
                html = html[:search_pos + 6] + '\n' + COMPLEMENTARY_HTML + html[search_pos + 6:]
                print(f"  [OK] Added Complementary content (after l7)")

    # 8. Update totalLessons for progress
    html = html.replace("var totalLessons = 7;", "var totalLessons = 8;", 1)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"  [DONE] Saved {filepath}")

if __name__ == '__main__':
    print("=== Building Gabriela Pires - Aula 8 ===")

    print("\n[1/2] Patching PROFESSOR file...")
    patch_file(PROF, is_aluno=False)

    print("\n[2/2] Patching ALUNO file...")
    patch_file(ALUNO, is_aluno=True)

    print("\n=== Build complete ===")
