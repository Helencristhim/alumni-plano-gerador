#!/usr/bin/env python3
"""
Build Gabriela Pires - Aula 7: Where Are You From? — Countries, Nationalities & the World Around Gabriela
Inserts Pre-class, IN CLASS slides, Complementary, and audioMap into both professor and aluno files.
"""
import re, os

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROF = os.path.join(BASE, 'public', 'professor', 'gabriela-pires.html')
ALUNO = os.path.join(BASE, 'public', 'aluno', 'gabriela-pires.html')

# ============================================================
# AULA 7 AUDIO MAP ENTRIES
# ============================================================
AULA7_AUDIO = {
  "Country": "country",
  "Brazil is a big country.": "brazil_is_a_big_country",
  "Nationality": "nationality",
  "What is your nationality?": "what_is_your_nationality",
  "Brazilian": "brazilian",
  "I am Brazilian.": "i_am_brazilian",
  "French": "french",
  "She is French.": "she_is_french",
  "American": "american",
  "Blake Lively is American.": "blake_lively_is_american",
  "Language": "language",
  "I speak two languages.": "i_speak_two_languages",
  "Passport": "passport",
  "My passport is Brazilian.": "my_passport_is_brazilian",
  "International": "international",
  "Paris is an international city.": "paris_is_an_international_city",
  "Where are you from?": "where_are_you_from",
  "I am from Brazil.": "i_am_from_brazil",
  "Where is she from?": "where_is_she_from",
  "She is from France.": "she_is_from_france",
  "He is Australian.": "he_is_australian",
  "They are from Japan.": "they_are_from_japan",
  "What language do you speak?": "what_language_do_you_speak",
  "I speak Portuguese and English.": "i_speak_portuguese_and_english",
  "Hi! I am Gabriela. I am from Brazil.": "hi_i_am_gabriela_i_am_from_brazil",
  "Hey! I am Liam. I am from Australia.": "hey_i_am_liam_i_am_from_australia",
  "Nice to meet you! Where in Australia?": "nice_to_meet_you_where_in_australia",
  "I am from Sydney. And you? Where in Brazil?": "i_am_from_sydney_and_you_where_in_brazil",
  "I am from Sao Paulo. It is a huge city!": "i_am_from_sao_paulo_it_is_a_huge_city",
  "Cool! What languages do you speak?": "cool_what_languages_do_you_speak",
  "I speak Portuguese and I am learning English. What about you?": "i_speak_portuguese_and_i_am_learning_english",
  "I speak English and a little bit of French.": "i_speak_english_and_a_little_bit_of_french",
  "That is awesome! How long are you in Paris?": "that_is_awesome_how_long_are_you_in_paris",
  "Two weeks! This hostel is so international!": "two_weeks_this_hostel_is_so_international",
  "Gabriela is at a youth hostel in Paris. She meets travelers from many countries. Liam is from Australia. He is Australian. He speaks English and a little French. Yuki is from Japan. She is Japanese. She speaks Japanese and English. Marco is from Italy. He is Italian. He speaks Italian, English, and French. Gabriela is from Brazil. She is Brazilian. She speaks Portuguese and she is learning English. The hostel is very international. There are people from ten different countries.": "gabriela_hostel_listening_full",
  "Where is Liam from?": "where_is_liam_from",
  "What nationality is Yuki?": "what_nationality_is_yuki",
  "How many languages does Marco speak?": "how_many_languages_does_marco_speak",
  "Hi! My name is Sophie. I am from Canada. I am Canadian. I speak English and French.": "hi_my_name_is_sophie_i_am_from_canada",
  "Hello! I am Kenji. I am from Japan. I am Japanese. I speak Japanese and a little English.": "hello_i_am_kenji_i_am_from_japan",
  "Hey! I am Carlos. I am from Mexico. I am Mexican. I speak Spanish and English.": "hey_i_am_carlos_i_am_from_mexico",
  "I am from Sao Paulo, Brazil.": "i_am_from_sao_paulo_brazil",
  "I am Brazilian. I speak Portuguese.": "i_am_brazilian_i_speak_portuguese",
  "What is your nationality? Where are you from?": "what_is_your_nationality_where_are_you_from",
  "I speak Portuguese and I am learning English.": "i_speak_portuguese_and_i_am_learning_english_short",
  "This city is very international!": "this_city_is_very_international",
  "Hi, I am Gabriela. I am from Sao Paulo, Brazil. I am Brazilian. I speak Portuguese and I am learning English. My passport is Brazilian. I am in Paris for two weeks!": "hi_i_am_gabriela_full_intro",
  "Australia": "australia",
  "Japan": "japan",
  "Italy": "italy",
  "Canada": "canada",
  "Mexico": "mexico",
  "England": "england",
  "Ed Westwick is English.": "ed_westwick_is_english",
  "Australian": "australian",
  "Japanese": "japanese",
  "Italian": "italian",
  "Canadian": "canadian",
  "Mexican": "mexican",
  "English": "english_nationality",
}

# Build audioMap JS entries
def build_audiomap_entries():
    lines = []
    for phrase, slug in AULA7_AUDIO.items():
        escaped = phrase.replace("'", "\\'")
        lines.append(f'  "{escaped}": "/audio/gabriela-pires/{slug}.mp3?v=2"')
    return ',\n'.join(lines)

# ============================================================
# AULA 7 PRE-CLASS HTML
# ============================================================
PRECLASS_HTML = '''<div class="lesson-card" id="ex-lesson-7">
  <div class="lesson-header" onclick="toggleLesson(this)">
    <div class="lesson-header-img" style="background-image:url('https://images.unsplash.com/photo-1502602898657-3e91760cbb34?w=600&q=80')"></div>
    <div class="lesson-header-content">
      <div class="lesson-number">Aula 07 &mdash; Pre-class</div>
      <h3>Where Are You From? &mdash; Countries, Nationalities &amp; the World Around Gabriela</h3>
      <div class="lesson-desc">Depois desta aula, voc&ecirc; consegue se apresentar dizendo de onde &eacute;, sua nacionalidade e que idiomas fala &mdash; tudo que precisa ao conhecer viajantes em Paris.</div>
      <div class="lesson-progress-mini"><div class="mini-bar"><div class="mini-bar-fill" data-lesson-progress="7" style="width:0%"></div></div><span class="mini-percent" data-lesson-pct="7">0%</span></div>
    </div>
    <div class="expand-icon">&#9660;</div>
  </div>
  <div class="lesson-body">
    <p style="font-size:0.85rem;color:var(--text-mid);margin-bottom:1.5rem;"><strong style="color:var(--accent);">Objetivo:</strong> Ao final desta aula, Gabriela ser&aacute; capaz de dizer de onde &eacute;, perguntar a nacionalidade dos outros e falar sobre idiomas &mdash; perfeito para o hostel em Paris.</p>

    <!-- ===== STAGE 1.1: VOCABULARY CARDS ===== -->
    <div class="exercise-section">
      <div class="section-header-row">
        <h4>Vocabul&aacute;rio <span class="badge badge-vocab">Vocabulary</span></h4>
        <button class="listen-all-btn" onclick="listenAllVocab(this)">&#9654; Ouvir todos</button>
      </div>
      <p class="microcopy">Olha a palavra, a tradu&ccedil;&atilde;o e o exemplo juntos. Toca em Ouvir &mdash; o som ajuda muito a mem&oacute;ria.</p>

      <div class="vocab-card">
        <div class="vocab-word">Country</div>
        <div class="vocab-translation">pa&iacute;s</div>
        <div class="vocab-example">&ldquo;Brazil is a big <strong>country</strong>.&rdquo;</div>
        <button class="audio-btn" onclick="speakText('Brazil is a big country.', this)">&#9654; Ouvir</button>
      </div>
      <div class="vocab-card">
        <div class="vocab-word">Nationality</div>
        <div class="vocab-translation">nacionalidade</div>
        <div class="vocab-example">&ldquo;What is your <strong>nationality</strong>?&rdquo;</div>
        <button class="audio-btn" onclick="speakText('What is your nationality?', this)">&#9654; Ouvir</button>
      </div>
      <div class="vocab-card">
        <div class="vocab-word">Brazilian</div>
        <div class="vocab-translation">brasileiro/a</div>
        <div class="vocab-example">&ldquo;I am <strong>Brazilian</strong>.&rdquo;</div>
        <button class="audio-btn" onclick="speakText('I am Brazilian.', this)">&#9654; Ouvir</button>
      </div>
      <div class="vocab-card">
        <div class="vocab-word">French</div>
        <div class="vocab-translation">franc&ecirc;s/francesa</div>
        <div class="vocab-example">&ldquo;She is <strong>French</strong>.&rdquo;</div>
        <button class="audio-btn" onclick="speakText('She is French.', this)">&#9654; Ouvir</button>
      </div>
      <div class="vocab-card">
        <div class="vocab-word">American</div>
        <div class="vocab-translation">americano/a</div>
        <div class="vocab-example">&ldquo;Blake Lively is <strong>American</strong>.&rdquo;</div>
        <button class="audio-btn" onclick="speakText('Blake Lively is American.', this)">&#9654; Ouvir</button>
      </div>
      <div class="vocab-card">
        <div class="vocab-word">Language</div>
        <div class="vocab-translation">idioma / l&iacute;ngua</div>
        <div class="vocab-example">&ldquo;I speak two <strong>languages</strong>.&rdquo;</div>
        <button class="audio-btn" onclick="speakText('I speak two languages.', this)">&#9654; Ouvir</button>
      </div>
      <div class="vocab-card">
        <div class="vocab-word">Passport</div>
        <div class="vocab-translation">passaporte</div>
        <div class="vocab-example">&ldquo;My <strong>passport</strong> is Brazilian.&rdquo;</div>
        <button class="audio-btn" onclick="speakText('My passport is Brazilian.', this)">&#9654; Ouvir</button>
      </div>
      <div class="vocab-card">
        <div class="vocab-word">International</div>
        <div class="vocab-translation">internacional</div>
        <div class="vocab-example">&ldquo;Paris is an <strong>international</strong> city.&rdquo;</div>
        <button class="audio-btn" onclick="speakText('Paris is an international city.', this)">&#9654; Ouvir</button>
      </div>
    </div>

    <!-- ===== STAGE 1.2: MATCHING ===== -->
    <div class="exercise-section">
      <h4>V2. Match the words <span class="badge badge-vocab">Matching</span></h4>
      <p class="microcopy">Fa&ccedil;a um de cada vez. Errou? Leia a explica&ccedil;&atilde;o com calma &mdash; &eacute; a&iacute; que voc&ecirc; aprende de verdade.</p>
      <div class="match-grid" id="match-l7">
        <div class="match-row" data-answer="pa&iacute;s">
          <span class="match-word">Country</span>
          <select onchange="checkMatch(this)">
            <option value="">Select...</option>
            <option value="nacionalidade">nacionalidade</option>
            <option value="passaporte">passaporte</option>
            <option value="pa&iacute;s">pa&iacute;s</option>
            <option value="idioma">idioma</option>
            <option value="internacional">internacional</option>
          </select>
        </div>
        <div class="match-row" data-answer="nacionalidade">
          <span class="match-word">Nationality</span>
          <select onchange="checkMatch(this)">
            <option value="">Select...</option>
            <option value="americano/a">americano/a</option>
            <option value="nacionalidade">nacionalidade</option>
            <option value="franc&ecirc;s">franc&ecirc;s</option>
            <option value="pa&iacute;s">pa&iacute;s</option>
            <option value="brasileiro/a">brasileiro/a</option>
          </select>
        </div>
        <div class="match-row" data-answer="brasileiro/a">
          <span class="match-word">Brazilian</span>
          <select onchange="checkMatch(this)">
            <option value="">Select...</option>
            <option value="internacional">internacional</option>
            <option value="brasileiro/a">brasileiro/a</option>
            <option value="passaporte">passaporte</option>
            <option value="nacionalidade">nacionalidade</option>
            <option value="idioma">idioma</option>
          </select>
        </div>
        <div class="match-row" data-answer="franc&ecirc;s">
          <span class="match-word">French</span>
          <select onchange="checkMatch(this)">
            <option value="">Select...</option>
            <option value="pa&iacute;s">pa&iacute;s</option>
            <option value="americano/a">americano/a</option>
            <option value="franc&ecirc;s">franc&ecirc;s</option>
            <option value="brasileiro/a">brasileiro/a</option>
            <option value="passaporte">passaporte</option>
          </select>
        </div>
        <div class="match-row" data-answer="americano/a">
          <span class="match-word">American</span>
          <select onchange="checkMatch(this)">
            <option value="">Select...</option>
            <option value="idioma">idioma</option>
            <option value="internacional">internacional</option>
            <option value="pa&iacute;s">pa&iacute;s</option>
            <option value="americano/a">americano/a</option>
            <option value="franc&ecirc;s">franc&ecirc;s</option>
          </select>
        </div>
        <div class="match-row" data-answer="idioma">
          <span class="match-word">Language</span>
          <select onchange="checkMatch(this)">
            <option value="">Select...</option>
            <option value="passaporte">passaporte</option>
            <option value="brasileiro/a">brasileiro/a</option>
            <option value="idioma">idioma</option>
            <option value="americano/a">americano/a</option>
            <option value="nacionalidade">nacionalidade</option>
          </select>
        </div>
        <div class="match-row" data-answer="passaporte">
          <span class="match-word">Passport</span>
          <select onchange="checkMatch(this)">
            <option value="">Select...</option>
            <option value="franc&ecirc;s">franc&ecirc;s</option>
            <option value="passaporte">passaporte</option>
            <option value="internacional">internacional</option>
            <option value="pa&iacute;s">pa&iacute;s</option>
            <option value="idioma">idioma</option>
          </select>
        </div>
        <div class="match-row" data-answer="internacional">
          <span class="match-word">International</span>
          <select onchange="checkMatch(this)">
            <option value="">Select...</option>
            <option value="brasileiro/a">brasileiro/a</option>
            <option value="nacionalidade">nacionalidade</option>
            <option value="americano/a">americano/a</option>
            <option value="internacional">internacional</option>
            <option value="pa&iacute;s">pa&iacute;s</option>
          </select>
        </div>
      </div>
      <button class="verify-all-btn" onclick="verifyAllMatches('match-l7')">Check Answers</button>
    </div>

    <!-- ===== STAGE 1.3: GRAMMAR IN CONTEXT ===== -->
    <div class="exercise-section">
      <h4>Stage 1.2: Grammar in Context <span class="badge badge-practice">Grammar</span></h4>
      <p class="microcopy">Leia o texto com calma. As palavras em negrito s&atilde;o do vocabul&aacute;rio de hoje.</p>
      <div class="context-text" style="background:var(--accent-dim);border:1px solid rgba(212,50,106,0.15);border-radius:8px;padding:1.2rem;margin-bottom:1.2rem;line-height:1.9;font-size:0.95rem;">
        Gabriela <strong>is from</strong> Brazil. She <strong>is Brazilian</strong>. She speaks Portuguese and she is learning English. At the hostel in Paris, she meets Liam. He <strong>is from</strong> Australia. He <strong>is Australian</strong>. He speaks English and a little <strong>French</strong>. There is also Yuki. She <strong>is from</strong> Japan. She <strong>is Japanese</strong>. The hostel is very <strong>international</strong> &mdash; there are people from ten different <strong>countries</strong>! Gabriela shows her <strong>passport</strong> at the reception. &ldquo;What <strong>nationality</strong>?&rdquo; asks the receptionist. &ldquo;I am <strong>Brazilian</strong>,&rdquo; says Gabriela. &ldquo;Welcome! You speak good English!&rdquo; &ldquo;Thank you! I am learning. What <strong>languages</strong> do people speak here?&rdquo; &ldquo;English, French, Japanese, Italian... It is truly <strong>international</strong>!&rdquo;
      </div>
      <div class="quiz-item">
        <div class="quiz-question">Where is Liam from?</div>
        <div class="quiz-options">
          <div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> France</div>
          <div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> Australia</div>
          <div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> Japan</div>
        </div>
      </div>
      <div class="quiz-item">
        <div class="quiz-question">What is Gabriela&rsquo;s nationality?</div>
        <div class="quiz-options">
          <div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> French</div>
          <div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> American</div>
          <div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">C</span> Brazilian</div>
        </div>
      </div>
      <div class="quiz-item">
        <div class="quiz-question">How is the hostel described?</div>
        <div class="quiz-options">
          <div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> International</div>
          <div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> Small</div>
          <div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> French only</div>
        </div>
      </div>
    </div>

    <!-- ===== STAGE 1.4: GRAMMAR TIP ===== -->
    <div class="exercise-section">
      <h4>Grammar Tip <span class="badge badge-practice">Grammar</span></h4>
      <div style="background:var(--accent-dim);border:1px solid rgba(212,50,106,0.15);border-radius:8px;padding:1.2rem;margin-bottom:1rem;">
        <p style="font-weight:700;color:var(--accent);margin-bottom:0.8rem;font-size:1rem;">Talking About Origin &amp; Nationality / Falando sobre origem e nacionalidade</p>
        <table style="width:100%;border-collapse:collapse;font-size:0.9rem;">
          <tr style="border-bottom:1px solid var(--border);"><td style="padding:0.5rem;font-weight:600;">Pergunta</td><td style="padding:0.5rem;"><strong>Where are you from?</strong></td><td style="padding:0.5rem;color:var(--text-dim);">De onde voc&ecirc; &eacute;?</td></tr>
          <tr style="border-bottom:1px solid var(--border);"><td style="padding:0.5rem;font-weight:600;">Pa&iacute;s</td><td style="padding:0.5rem;">I am <strong>from Brazil</strong>.</td><td style="padding:0.5rem;color:var(--text-dim);">Eu sou do Brasil.</td></tr>
          <tr style="border-bottom:1px solid var(--border);"><td style="padding:0.5rem;font-weight:600;">Nacionalidade</td><td style="padding:0.5rem;">I am <strong>Brazilian</strong>.</td><td style="padding:0.5rem;color:var(--text-dim);">Eu sou brasileira.</td></tr>
          <tr style="border-bottom:1px solid var(--border);"><td style="padding:0.5rem;font-weight:600;">3a pessoa</td><td style="padding:0.5rem;">She <strong>is</strong> French. / He <strong>is from</strong> Australia.</td><td style="padding:0.5rem;color:var(--text-dim);">Ela &eacute; francesa. / Ele &eacute; da Austr&aacute;lia.</td></tr>
          <tr style="border-bottom:1px solid var(--border);"><td style="padding:0.5rem;font-weight:600;">Idioma</td><td style="padding:0.5rem;">I <strong>speak</strong> Portuguese and English.</td><td style="padding:0.5rem;color:var(--text-dim);">Eu falo portugu&ecirc;s e ingl&ecirc;s.</td></tr>
          <tr><td style="padding:0.5rem;font-weight:600;">Plural</td><td style="padding:0.5rem;">They <strong>are from</strong> Japan.</td><td style="padding:0.5rem;color:var(--text-dim);">Eles s&atilde;o do Jap&atilde;o.</td></tr>
        </table>
      </div>
      <div style="background:var(--accent-dim);border:1px solid rgba(212,50,106,0.15);border-radius:8px;padding:1.2rem;">
        <p style="font-weight:700;color:var(--accent);margin-bottom:0.8rem;font-size:1rem;">Countries &amp; Nationalities / Pa&iacute;ses e nacionalidades</p>
        <table style="width:100%;border-collapse:collapse;font-size:0.88rem;">
          <tr style="border-bottom:1px solid var(--border);"><th style="padding:0.4rem;text-align:left;">Country</th><th style="padding:0.4rem;text-align:left;">Nationality</th><th style="padding:0.4rem;text-align:left;">Celebridade</th></tr>
          <tr style="border-bottom:1px solid var(--border);"><td style="padding:0.4rem;">Brazil</td><td style="padding:0.4rem;">Brazilian</td><td style="padding:0.4rem;color:var(--text-dim);">Gabriela!</td></tr>
          <tr style="border-bottom:1px solid var(--border);"><td style="padding:0.4rem;">France</td><td style="padding:0.4rem;">French</td><td style="padding:0.4rem;color:var(--text-dim);">Lily Collins (Emily in Paris)</td></tr>
          <tr style="border-bottom:1px solid var(--border);"><td style="padding:0.4rem;">USA</td><td style="padding:0.4rem;">American</td><td style="padding:0.4rem;color:var(--text-dim);">Blake Lively (Gossip Girl)</td></tr>
          <tr style="border-bottom:1px solid var(--border);"><td style="padding:0.4rem;">England</td><td style="padding:0.4rem;">English</td><td style="padding:0.4rem;color:var(--text-dim);">Ed Westwick (Gossip Girl)</td></tr>
          <tr style="border-bottom:1px solid var(--border);"><td style="padding:0.4rem;">Australia</td><td style="padding:0.4rem;">Australian</td><td style="padding:0.4rem;color:var(--text-dim);">Chris Hemsworth</td></tr>
          <tr style="border-bottom:1px solid var(--border);"><td style="padding:0.4rem;">Japan</td><td style="padding:0.4rem;">Japanese</td><td style="padding:0.4rem;color:var(--text-dim);">Marie Kondo</td></tr>
          <tr style="border-bottom:1px solid var(--border);"><td style="padding:0.4rem;">Italy</td><td style="padding:0.4rem;">Italian</td><td style="padding:0.4rem;color:var(--text-dim);">Monica Bellucci</td></tr>
          <tr><td style="padding:0.4rem;">Canada</td><td style="padding:0.4rem;">Canadian</td><td style="padding:0.4rem;color:var(--text-dim);">Ryan Reynolds</td></tr>
        </table>
        <p style="font-size:0.82rem;line-height:1.7;margin-top:0.8rem;color:var(--text-mid);"><strong>Dica importante:</strong> Em ingl&ecirc;s, nacionalidades N&Atilde;O mudam para feminino/masculino. &ldquo;Brazilian&rdquo; = ele E ela. Diferente do portugu&ecirc;s (brasileiro/brasileira).</p>
      </div>
    </div>

    <!-- ===== STAGE 1.5: FILL-IN-THE-BLANK ===== -->
    <div class="exercise-section">
      <h4>P1. Complete with the correct word <span class="badge badge-practice">Practice</span></h4>
      <p class="microcopy">Fa&ccedil;a um de cada vez. Errou? Leia a dica com calma.</p>

      <div class="fill-blank-item">
        <div class="fill-blank-sentence">
          &ldquo;Where are you
          <input class="blank-input" data-answer="from" data-hint="Hint: the preposition used with origin" data-phrase="Where are you from?" placeholder="___">
          ?&rdquo;
        </div>
        <button class="check-btn" onclick="checkBlank(this)">Check</button>
        <button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button>
      </div>

      <div class="fill-blank-item">
        <div class="fill-blank-sentence">
          &ldquo;I am
          <input class="blank-input" data-answer="Brazilian" data-alt="brazilian" data-hint="Hint: the nationality of someone from Brazil" data-phrase="I am Brazilian." placeholder="___">
          .&rdquo;
        </div>
        <button class="check-btn" onclick="checkBlank(this)">Check</button>
        <button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button>
      </div>

      <div class="fill-blank-item">
        <div class="fill-blank-sentence">
          &ldquo;Blake Lively is
          <input class="blank-input" data-answer="American" data-alt="american" data-hint="Hint: the nationality of someone from the USA" data-phrase="Blake Lively is American." placeholder="___">
          .&rdquo;
        </div>
        <button class="check-btn" onclick="checkBlank(this)">Check</button>
        <button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button>
      </div>

      <div class="fill-blank-item">
        <div class="fill-blank-sentence">
          &ldquo;I speak two
          <input class="blank-input" data-answer="languages" data-hint="Hint: Portuguese and English are two..." data-phrase="I speak two languages." placeholder="___">
          .&rdquo;
        </div>
        <button class="check-btn" onclick="checkBlank(this)">Check</button>
        <button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button>
      </div>

      <div class="fill-blank-item">
        <div class="fill-blank-sentence">
          &ldquo;My
          <input class="blank-input" data-answer="passport" data-hint="Hint: the document you show at the airport" data-phrase="My passport is Brazilian." placeholder="___">
          is Brazilian.&rdquo;
        </div>
        <button class="check-btn" onclick="checkBlank(this)">Check</button>
        <button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button>
      </div>
    </div>

    <!-- ===== STAGE 2: ORDERING ===== -->
    <div class="exercise-section">
      <h4>P2. Put in order <span class="badge badge-order">Order</span></h4>
      <p class="microcopy">Coloque as frases na ordem correta para formar uma conversa no hostel.</p>
      <div class="order-container" id="order-l7">
        <div class="order-item" draggable="true" data-order="4" onclick="selectOrderItem(this,'order-l7')">
          <span class="order-num">?</span>
          <span class="order-text">&ldquo;I am from Sydney. And you?&rdquo;</span>
          <span class="order-arrows">
            <button class="arrow-btn" onclick="moveItem(this,-1,'order-l7')">&#9650;</button>
            <button class="arrow-btn" onclick="moveItem(this,1,'order-l7')">&#9660;</button>
          </span>
        </div>
        <div class="order-item" draggable="true" data-order="2" onclick="selectOrderItem(this,'order-l7')">
          <span class="order-num">?</span>
          <span class="order-text">&ldquo;I am from Australia!&rdquo;</span>
          <span class="order-arrows">
            <button class="arrow-btn" onclick="moveItem(this,-1,'order-l7')">&#9650;</button>
            <button class="arrow-btn" onclick="moveItem(this,1,'order-l7')">&#9660;</button>
          </span>
        </div>
        <div class="order-item" draggable="true" data-order="5" onclick="selectOrderItem(this,'order-l7')">
          <span class="order-num">?</span>
          <span class="order-text">&ldquo;I am from S&atilde;o Paulo, Brazil!&rdquo;</span>
          <span class="order-arrows">
            <button class="arrow-btn" onclick="moveItem(this,-1,'order-l7')">&#9650;</button>
            <button class="arrow-btn" onclick="moveItem(this,1,'order-l7')">&#9660;</button>
          </span>
        </div>
        <div class="order-item" draggable="true" data-order="1" onclick="selectOrderItem(this,'order-l7')">
          <span class="order-num">?</span>
          <span class="order-text">&ldquo;Hi! Where are you from?&rdquo;</span>
          <span class="order-arrows">
            <button class="arrow-btn" onclick="moveItem(this,-1,'order-l7')">&#9650;</button>
            <button class="arrow-btn" onclick="moveItem(this,1,'order-l7')">&#9660;</button>
          </span>
        </div>
        <div class="order-item" draggable="true" data-order="3" onclick="selectOrderItem(this,'order-l7')">
          <span class="order-num">?</span>
          <span class="order-text">&ldquo;Cool! Where in Australia?&rdquo;</span>
          <span class="order-arrows">
            <button class="arrow-btn" onclick="moveItem(this,-1,'order-l7')">&#9650;</button>
            <button class="arrow-btn" onclick="moveItem(this,1,'order-l7')">&#9660;</button>
          </span>
        </div>
      </div>
      <button class="verify-all-btn" onclick="checkOrder('order-l7')">Check Order</button>
    </div>

    <!-- ===== STAGE 3: PRONUNCIATION ===== -->
    <div class="exercise-section">
      <h4>S1. Read aloud <span class="badge badge-speak">Speaking</span></h4>
      <p class="microcopy">Toque em Ouvir, repita, depois grave e compare. O objetivo &eacute; praticar, n&atilde;o ser perfeito.</p>

      <div class="speech-card" data-phrase="Where are you from?">
        <div class="speech-phrase">Where are you from?</div>
        <div class="speech-translation">De onde voc&ecirc; &eacute;?</div>
        <div class="speech-controls">
          <button class="btn btn-listen" onclick="speakPhrase(this)">&#9654; Ouvir</button>
          <button class="btn btn-record" onclick="startRecording(this)">&#9679; Gravar</button>
          <button class="btn btn-stop" onclick="stopRecording(this)">&#9632; Parar</button>
        </div>
        <div class="speech-result"></div>
      </div>

      <div class="speech-card" data-phrase="I am from Sao Paulo, Brazil.">
        <div class="speech-phrase">I am from S&atilde;o Paulo, Brazil.</div>
        <div class="speech-translation">Eu sou de S&atilde;o Paulo, Brasil.</div>
        <div class="speech-controls">
          <button class="btn btn-listen" onclick="speakPhrase(this)">&#9654; Ouvir</button>
          <button class="btn btn-record" onclick="startRecording(this)">&#9679; Gravar</button>
          <button class="btn btn-stop" onclick="stopRecording(this)">&#9632; Parar</button>
        </div>
        <div class="speech-result"></div>
      </div>

      <div class="speech-card" data-phrase="I am Brazilian. I speak Portuguese.">
        <div class="speech-phrase">I am Brazilian. I speak Portuguese.</div>
        <div class="speech-translation">Eu sou brasileira. Eu falo portugu&ecirc;s.</div>
        <div class="speech-controls">
          <button class="btn btn-listen" onclick="speakPhrase(this)">&#9654; Ouvir</button>
          <button class="btn btn-record" onclick="startRecording(this)">&#9679; Gravar</button>
          <button class="btn btn-stop" onclick="stopRecording(this)">&#9632; Parar</button>
        </div>
        <div class="speech-result"></div>
      </div>

      <div class="speech-card" data-phrase="I speak Portuguese and I am learning English.">
        <div class="speech-phrase">I speak Portuguese and I am learning English.</div>
        <div class="speech-translation">Eu falo portugu&ecirc;s e estou aprendendo ingl&ecirc;s.</div>
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
        <div class="quiz-question">Someone at the hostel asks: &ldquo;Where are you from?&rdquo; What do you say?</div>
        <div class="quiz-options">
          <div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> &ldquo;I from Brazil.&rdquo;</div>
          <div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> &ldquo;I am from Brazil.&rdquo;</div>
          <div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> &ldquo;My from is Brazil.&rdquo;</div>
        </div>
      </div>

      <div class="quiz-item">
        <div class="quiz-question">You want to know someone&rsquo;s nationality. What do you ask?</div>
        <div class="quiz-options">
          <div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> &ldquo;What country you?&rdquo;</div>
          <div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> &ldquo;Where are you from?&rdquo;</div>
          <div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> &ldquo;You are from where?&rdquo;</div>
        </div>
      </div>

      <div class="quiz-item">
        <div class="quiz-question">Ed Westwick is from England. What is his nationality?</div>
        <div class="quiz-options">
          <div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> American</div>
          <div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> English</div>
          <div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> Australian</div>
        </div>
      </div>

      <div class="quiz-item">
        <div class="quiz-question">Someone says: &ldquo;I speak Japanese and English.&rdquo; They are probably from...</div>
        <div class="quiz-options">
          <div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> France</div>
          <div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> Japan</div>
          <div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> Italy</div>
        </div>
      </div>
    </div>

    <!-- ===== STAGE 5: THINK ===== -->
    <div class="exercise-section">
      <h4>T1. Think and respond <span class="badge badge-think">Reflection</span></h4>
      <p class="microcopy">Aqui n&atilde;o tem resposta certa &mdash; &eacute; pra voc&ecirc; pensar em ingl&ecirc;s. Toque no microfone e responde como vier.</p>
      <div class="think-card">
        <div style="font-size:0.92rem;color:var(--text);margin-bottom:1rem;line-height:1.8;">You arrive at a youth hostel in Paris. Introduce yourself to a new traveler. Say: your name, where you are from, your nationality, what languages you speak, and how long you are in Paris.</div>
        <div class="speech-card" data-phrase="Hi, I am Gabriela. I am from Sao Paulo, Brazil. I am Brazilian. I speak Portuguese and I am learning English. My passport is Brazilian. I am in Paris for two weeks!" style="background:var(--accent-dim);border:1px solid rgba(212,50,106,0.25);">
          <div style="font-size:0.72rem;font-weight:600;text-transform:uppercase;letter-spacing:1.5px;color:var(--accent);margin-bottom:0.5rem;">Sugest&atilde;o de resposta</div>
          <div class="speech-phrase" style="font-size:1.05rem;">&ldquo;Hi, I am Gabriela. I am from S&atilde;o Paulo, Brazil. I am Brazilian. I speak Portuguese and I am learning English. My passport is Brazilian. I am in Paris for two weeks!&rdquo;</div>
          <div class="speech-translation">Oi, eu sou a Gabriela. Eu sou de S&atilde;o Paulo, Brasil. Eu sou brasileira. Eu falo portugu&ecirc;s e estou aprendendo ingl&ecirc;s. Meu passaporte &eacute; brasileiro. Estou em Paris por duas semanas!</div>
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
      <h4>Survival Card &mdash; Lesson 7: Countries &amp; Nationalities</h4>
      <div class="survival-phrase"><span class="sp-num">1</span><span class="sp-en">Where are you from?</span><span class="sp-pt">De onde voc&ecirc; &eacute;?</span><button class="btn btn-listen" onclick="speakText('Where are you from?', this)">&#9654;</button></div>
      <div class="survival-phrase"><span class="sp-num">2</span><span class="sp-en">I am from S&atilde;o Paulo, Brazil.</span><span class="sp-pt">Eu sou de S&atilde;o Paulo, Brasil.</span><button class="btn btn-listen" onclick="speakText('I am from Sao Paulo, Brazil.', this)">&#9654;</button></div>
      <div class="survival-phrase"><span class="sp-num">3</span><span class="sp-en">I am Brazilian. I speak Portuguese.</span><span class="sp-pt">Eu sou brasileira. Eu falo portugu&ecirc;s.</span><button class="btn btn-listen" onclick="speakText('I am Brazilian. I speak Portuguese.', this)">&#9654;</button></div>
      <div class="survival-phrase"><span class="sp-num">4</span><span class="sp-en">What is your nationality?</span><span class="sp-pt">Qual &eacute; a sua nacionalidade?</span><button class="btn btn-listen" onclick="speakText('What is your nationality?', this)">&#9654;</button></div>
      <div class="survival-phrase"><span class="sp-num">5</span><span class="sp-en">This city is very international!</span><span class="sp-pt">Esta cidade &eacute; muito internacional!</span><button class="btn btn-listen" onclick="speakText('This city is very international!', this)">&#9654;</button></div>
    </div>

  </div>
</div>'''

# ============================================================
# AULA 7 IN CLASS SLIDES HTML (29 slides, data-slide 176-204)
# ============================================================
SLIDES_HTML = '''
<!-- ================ LESSON 7: WHERE ARE YOU FROM? ================ -->

<!-- SLIDE 176: L7 CHAPTER 1 - THE DREAM -->
<div class="slide slide-image" data-slide="176" data-phase="1" data-lesson="7" data-teacher="<strong>Abertura (2 min):</strong> 'Welcome back, Gabriela! Last class: numbers, time, and dates. Today: WHERE ARE YOU FROM? Countries, nationalities, and languages! Imagine: you arrive at a hostel in Paris and meet travelers from all over the world. How do you introduce yourself?' Tom animado e acolhedor." style="background-image:url('https://images.unsplash.com/photo-1502602898657-3e91760cbb34?w=600&q=80')">
  <div class="slide-inner">
    <div class="chapter-label">Chapter 1 &mdash; The Dream</div>
    <h1 class="slide-title">Where Are You <span class="accent">From</span>?</h1>
    <p class="slide-subtitle">Countries, nationalities &amp; the world around Gabriela</p>
  </div>
</div>

<!-- SLIDE 177: L7 WARM-UP CALLBACK -->
<div class="slide slide-dark" data-slide="177" data-phase="1" data-lesson="7" data-teacher="<strong>Callback Aula 6 (3 min):</strong> Perguntas r&aacute;pidas usando time/dates da aula anterior. 'What time is it now?' 'When is your flight to Paris?' 'How much is a ticket to the Louvre?' Depois: 'You know times and dates. Now you need one more thing: how to INTRODUCE YOURSELF to people from other countries!' Ponte natural para o tema.">
  <div class="slide-inner">
    <div class="chapter-label">Warm-up</div>
    <h2 class="slide-heading">Quick <span class="accent">Callback</span></h2>
    <div class="warm-questions">
      <div class="warm-q">What time is it right now? Say it in English!</div>
      <div class="warm-q">When is your flight to Paris?</div>
      <div class="warm-q">Now imagine: you arrive at the hostel. Someone says &ldquo;Hi!&rdquo; &mdash; what is the FIRST thing they ask you?</div>
    </div>
  </div>
</div>

<!-- SLIDE 178: L7 CHAPTER 2 TRANSITION -->
<div class="slide slide-image" data-slide="178" data-phase="2" data-lesson="7" data-teacher="<strong>Transi&ccedil;&atilde;o (10s):</strong> 'Let us pack the words you need to talk about countries and nationalities!' Avance." style="background-image:url('https://images.unsplash.com/photo-1502602898657-3e91760cbb34?w=600&q=80')">
  <div class="slide-inner">
    <div class="chapter-label">Chapter 2</div>
    <h1 class="slide-title">Packing <span class="accent">Words</span></h1>
    <p class="slide-subtitle">Your nationality vocabulary for the hostel</p>
  </div>
</div>

<!-- SLIDE 179: L7 VOCAB CARDS 1-4 -->
<div class="slide slide-light" data-slide="179" data-phase="2" data-lesson="7" data-teacher="<strong>Vocabul&aacute;rio (8 min):</strong> ANTES de clicar, leia a pista: 'What word do you think this is?' DEPOIS de revelar, toque audio 2x. Drill: country /KUN-tree/ &mdash; stress na 1a. nationality /na-shuh-NA-luh-tee/ &mdash; stress na 3a s&iacute;laba. Brazilian /bruh-ZI-lee-un/ &mdash; stress no ZI. French /french/ &mdash; 1 s&iacute;laba, som do 'fr'. Drill cada 3x.">
  <div class="slide-inner">
    <h2 class="slide-heading">Identity <span class="accent">Words</span></h2>
    <div class="vocab-grid">
      <div class="vocab-card" onclick="this.classList.toggle('revealed')">
        <div class="card-icon" style="background:linear-gradient(135deg,#059669,#10b981)">
          <svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="1.5"><circle cx="12" cy="12" r="10"/><path d="M2 12h20M12 2a15.3 15.3 0 014 10 15.3 15.3 0 01-4 10 15.3 15.3 0 01-4-10 15.3 15.3 0 014-10z"/></svg>
          <div class="card-hint">A nation &mdash; Brazil, France, Japan...</div>
        </div>
        <div class="card-body">
          <div class="card-word">Country</div>
          <div class="card-def">A nation with borders and a government</div>
          <div class="card-example">&ldquo;Brazil is a big <strong>country</strong>.&rdquo;</div>
          <div class="card-audio"><button class="audio-btn-sm" onclick="event.stopPropagation();speakText('Brazil is a big country.',this)"><svg viewBox="0 0 24 24"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M19.07 4.93a10 10 0 010 14.14M15.54 8.46a5 5 0 010 7.07"/></svg> Listen</button></div>
        </div>
      </div>
      <div class="vocab-card" onclick="this.classList.toggle('revealed')">
        <div class="card-icon" style="background:linear-gradient(135deg,#7c3aed,#a855f7)">
          <svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="1.5"><rect x="3" y="4" width="18" height="16" rx="2"/><path d="M7 8h10M7 12h6"/></svg>
          <div class="card-hint">Brazilian, French, American...</div>
        </div>
        <div class="card-body">
          <div class="card-word">Nationality</div>
          <div class="card-def">The country where you were born or belong to</div>
          <div class="card-example">&ldquo;What is your <strong>nationality</strong>?&rdquo;</div>
          <div class="card-audio"><button class="audio-btn-sm" onclick="event.stopPropagation();speakText('What is your nationality?',this)"><svg viewBox="0 0 24 24"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M19.07 4.93a10 10 0 010 14.14M15.54 8.46a5 5 0 010 7.07"/></svg> Listen</button></div>
        </div>
      </div>
      <div class="vocab-card" onclick="this.classList.toggle('revealed')">
        <div class="card-icon" style="background:linear-gradient(135deg,#009739,#FEDD00)">
          <svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="1.5"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
          <div class="card-hint">Someone from Brazil is...</div>
        </div>
        <div class="card-body">
          <div class="card-word">Brazilian</div>
          <div class="card-def">From Brazil (same for he and she!)</div>
          <div class="card-example">&ldquo;I am <strong>Brazilian</strong>.&rdquo;</div>
          <div class="card-audio"><button class="audio-btn-sm" onclick="event.stopPropagation();speakText('I am Brazilian.',this)"><svg viewBox="0 0 24 24"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M19.07 4.93a10 10 0 010 14.14M15.54 8.46a5 5 0 010 7.07"/></svg> Listen</button></div>
        </div>
      </div>
      <div class="vocab-card" onclick="this.classList.toggle('revealed')">
        <div class="card-icon" style="background:linear-gradient(135deg,#002395,#ED2939)">
          <svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="1.5"><path d="M4 15s1-1 4-1 5 2 8 2 4-1 4-1V3s-1 1-4 1-5-2-8-2-4 1-4 1z"/><line x1="4" y1="22" x2="4" y2="15"/></svg>
          <div class="card-hint">The nationality and language of France</div>
        </div>
        <div class="card-body">
          <div class="card-word">French</div>
          <div class="card-def">From France; also the language spoken there</div>
          <div class="card-example">&ldquo;She is <strong>French</strong>.&rdquo;</div>
          <div class="card-audio"><button class="audio-btn-sm" onclick="event.stopPropagation();speakText('She is French.',this)"><svg viewBox="0 0 24 24"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M19.07 4.93a10 10 0 010 14.14M15.54 8.46a5 5 0 010 7.07"/></svg> Listen</button></div>
        </div>
      </div>
    </div>
    <div class="vocab-counter"><span id="vc7a">0</span> / 4 words</div>
  </div>
</div>

<!-- SLIDE 180: L7 VOCAB CARDS 5-8 -->
<div class="slide slide-light" data-slide="180" data-phase="2" data-lesson="7" data-teacher="<strong>Vocabul&aacute;rio (6 min):</strong> American /uh-ME-ri-kun/ &mdash; stress no ME. language /LANG-gwij/ &mdash; 2 s&iacute;labas, n&atilde;o 3! passport /PAS-port/ &mdash; 2 s&iacute;labas iguais. international /in-ter-NA-shuh-nul/ &mdash; stress no NA. Drill cada 3x. Pergunte: 'Blake Lively is...?' &rarr; 'American!' 'Ed Westwick is...?' &rarr; 'English!'">
  <div class="slide-inner">
    <h2 class="slide-heading">World <span class="accent">Words</span></h2>
    <div class="vocab-grid">
      <div class="vocab-card" onclick="this.classList.toggle('revealed')">
        <div class="card-icon" style="background:linear-gradient(135deg,#3C3B6E,#B22234)">
          <svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="1.5"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></svg>
          <div class="card-hint">Blake Lively and Jennifer Aniston are...</div>
        </div>
        <div class="card-body">
          <div class="card-word">American</div>
          <div class="card-def">From the United States of America</div>
          <div class="card-example">&ldquo;Blake Lively is <strong>American</strong>.&rdquo;</div>
          <div class="card-audio"><button class="audio-btn-sm" onclick="event.stopPropagation();speakText('Blake Lively is American.',this)"><svg viewBox="0 0 24 24"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M19.07 4.93a10 10 0 010 14.14M15.54 8.46a5 5 0 010 7.07"/></svg> Listen</button></div>
        </div>
      </div>
      <div class="vocab-card" onclick="this.classList.toggle('revealed')">
        <div class="card-icon" style="background:linear-gradient(135deg,#0891b2,#06b6d4)">
          <svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="1.5"><path d="M4 19.5A2.5 2.5 0 016.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 014 19.5v-15A2.5 2.5 0 016.5 2z"/></svg>
          <div class="card-hint">Portuguese, English, French are...</div>
        </div>
        <div class="card-body">
          <div class="card-word">Language</div>
          <div class="card-def">A system of communication (Portuguese, English...)</div>
          <div class="card-example">&ldquo;I speak two <strong>languages</strong>.&rdquo;</div>
          <div class="card-audio"><button class="audio-btn-sm" onclick="event.stopPropagation();speakText('I speak two languages.',this)"><svg viewBox="0 0 24 24"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M19.07 4.93a10 10 0 010 14.14M15.54 8.46a5 5 0 010 7.07"/></svg> Listen</button></div>
        </div>
      </div>
      <div class="vocab-card" onclick="this.classList.toggle('revealed')">
        <div class="card-icon" style="background:linear-gradient(135deg,#1e3a5f,#003080)">
          <svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="1.5"><rect x="2" y="4" width="20" height="16" rx="2"/><path d="M12 4v16M2 12h20"/><circle cx="12" cy="12" r="3"/></svg>
          <div class="card-hint">The document you show at the airport</div>
        </div>
        <div class="card-body">
          <div class="card-word">Passport</div>
          <div class="card-def">An official travel document with your photo</div>
          <div class="card-example">&ldquo;My <strong>passport</strong> is Brazilian.&rdquo;</div>
          <div class="card-audio"><button class="audio-btn-sm" onclick="event.stopPropagation();speakText('My passport is Brazilian.',this)"><svg viewBox="0 0 24 24"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M19.07 4.93a10 10 0 010 14.14M15.54 8.46a5 5 0 010 7.07"/></svg> Listen</button></div>
        </div>
      </div>
      <div class="vocab-card" onclick="this.classList.toggle('revealed')">
        <div class="card-icon" style="background:linear-gradient(135deg,#be185d,#ec4899)">
          <svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="1.5"><circle cx="12" cy="12" r="10"/><path d="M2 12h20M12 2a15.3 15.3 0 014 10 15.3 15.3 0 01-4 10 15.3 15.3 0 01-4-10 15.3 15.3 0 014-10z"/><line x1="2" y1="8" x2="22" y2="8"/><line x1="2" y1="16" x2="22" y2="16"/></svg>
          <div class="card-hint">Many countries, many people = very...</div>
        </div>
        <div class="card-body">
          <div class="card-word">International</div>
          <div class="card-def">Involving many countries or nationalities</div>
          <div class="card-example">&ldquo;Paris is an <strong>international</strong> city.&rdquo;</div>
          <div class="card-audio"><button class="audio-btn-sm" onclick="event.stopPropagation();speakText('Paris is an international city.',this)"><svg viewBox="0 0 24 24"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M19.07 4.93a10 10 0 010 14.14M15.54 8.46a5 5 0 010 7.07"/></svg> Listen</button></div>
        </div>
      </div>
    </div>
    <div class="vocab-counter"><span id="vc7b">0</span> / 4 words</div>
  </div>
</div>

<!-- SLIDE 181: L7 PRONUNCIATION DRILL -->
<div class="slide slide-light" data-slide="181" data-phase="2" data-lesson="7" data-teacher="<strong>Pron&uacute;ncia (4 min):</strong> Drill de pron&uacute;ncia. Foco: Brazilian /bruh-ZIL-ee-un/ &mdash; stress no ZIL, n&atilde;o no BRA. nationality /na-shuh-NA-luh-tee/ &mdash; 5 s&iacute;labas! French /french/ &mdash; som do FR, l&aacute;bios n&atilde;o fecham. international /in-ter-NA-shuh-nul/ &mdash; stress no NA. Repita 3x cada com Gabriela.">
  <div class="slide-inner">
    <h2 class="slide-heading">Say It <span class="accent">Right</span></h2>
    <div class="pron-grid">
      <div class="pron-item" onclick="speakText('Country',this)">
        <div class="pron-word">Country</div>
        <div class="pron-stress"><span class="pron-syl stressed">COUN</span><span class="pron-syl">try</span></div>
        <div class="pron-audio"><button class="audio-btn-sm" onclick="event.stopPropagation();speakText('Country',this)"><svg viewBox="0 0 24 24"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M19.07 4.93a10 10 0 010 14.14"/></svg> Listen</button></div>
      </div>
      <div class="pron-item" onclick="speakText('Brazilian',this)">
        <div class="pron-word">Brazilian</div>
        <div class="pron-stress"><span class="pron-syl">bra</span><span class="pron-syl stressed">ZIL</span><span class="pron-syl">ian</span></div>
        <div class="pron-audio"><button class="audio-btn-sm" onclick="event.stopPropagation();speakText('Brazilian',this)"><svg viewBox="0 0 24 24"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M19.07 4.93a10 10 0 010 14.14"/></svg> Listen</button></div>
      </div>
      <div class="pron-item" onclick="speakText('Nationality',this)">
        <div class="pron-word">Nationality</div>
        <div class="pron-stress"><span class="pron-syl">na</span><span class="pron-syl">tion</span><span class="pron-syl stressed">AL</span><span class="pron-syl">i</span><span class="pron-syl">ty</span></div>
        <div class="pron-audio"><button class="audio-btn-sm" onclick="event.stopPropagation();speakText('Nationality',this)"><svg viewBox="0 0 24 24"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M19.07 4.93a10 10 0 010 14.14"/></svg> Listen</button></div>
      </div>
      <div class="pron-item" onclick="speakText('American',this)">
        <div class="pron-word">American</div>
        <div class="pron-stress"><span class="pron-syl">a</span><span class="pron-syl stressed">MER</span><span class="pron-syl">i</span><span class="pron-syl">can</span></div>
        <div class="pron-audio"><button class="audio-btn-sm" onclick="event.stopPropagation();speakText('American',this)"><svg viewBox="0 0 24 24"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M19.07 4.93a10 10 0 010 14.14"/></svg> Listen</button></div>
      </div>
      <div class="pron-item" onclick="speakText('Passport',this)">
        <div class="pron-word">Passport</div>
        <div class="pron-stress"><span class="pron-syl stressed">PASS</span><span class="pron-syl">port</span></div>
        <div class="pron-audio"><button class="audio-btn-sm" onclick="event.stopPropagation();speakText('Passport',this)"><svg viewBox="0 0 24 24"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M19.07 4.93a10 10 0 010 14.14"/></svg> Listen</button></div>
      </div>
      <div class="pron-item" onclick="speakText('International',this)">
        <div class="pron-word">International</div>
        <div class="pron-stress"><span class="pron-syl">in</span><span class="pron-syl">ter</span><span class="pron-syl stressed">NA</span><span class="pron-syl">tion</span><span class="pron-syl">al</span></div>
        <div class="pron-audio"><button class="audio-btn-sm" onclick="event.stopPropagation();speakText('International',this)"><svg viewBox="0 0 24 24"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M19.07 4.93a10 10 0 010 14.14"/></svg> Listen</button></div>
      </div>
    </div>
  </div>
</div>

<!-- SLIDE 182: L7 CHAPTER 3 TRANSITION -->
<div class="slide slide-image" data-slide="182" data-phase="3" data-lesson="7" data-teacher="<strong>Transi&ccedil;&atilde;o (10s):</strong> 'Words packed! Now let us crack the NATIONALITY CODE!' Avance." style="background-image:url('https://images.unsplash.com/photo-1502602898657-3e91760cbb34?w=600&q=80')">
  <div class="slide-inner">
    <div class="chapter-label">Chapter 3</div>
    <h1 class="slide-title">The <span class="accent">Code</span></h1>
    <p class="slide-subtitle">How to talk about origin like a native</p>
  </div>
</div>

<!-- SLIDE 183: L7 GRAMMAR DISCOVERY -->
<div class="slide slide-light" data-slide="183" data-phase="3" data-lesson="7" data-teacher="<strong>Grammar Discovery (5 min):</strong> Mostre as 4 frases. Pergunte: 'Look at the pink words. What pattern do you see?' Espere. Se n&atilde;o perceber: 'We use I AM / SHE IS / THEY ARE + FROM + country. Or: I AM / SHE IS + nationality. In English, the nationality is the SAME for he and she!' Discovery method.">
  <div class="slide-inner">
    <h2 class="slide-heading">Spot the <span class="accent">Pattern</span></h2>
    <div class="grammar-sentences">
      <div class="grammar-sentence"><strong>I am from</strong> Brazil. <strong>I am</strong> Brazilian.</div>
      <div class="grammar-sentence"><strong>She is from</strong> France. <strong>She is</strong> French.</div>
      <div class="grammar-sentence"><strong>He is from</strong> Australia. <strong>He is</strong> Australian.</div>
      <div class="grammar-sentence"><strong>They are from</strong> Japan. <strong>They are</strong> Japanese.</div>
    </div>
    <p style="text-align:center;margin-top:1.5rem;font-size:1.1rem;color:var(--text);">What do the <span class="accent-bold">pink words</span> have in common?</p>
    <div style="text-align:center;margin-top:1rem;">
      <button class="btn-primary" onclick="this.nextElementSibling.classList.toggle('show');this.style.display='none'">Reveal the Rule</button>
      <div class="grammar-table-wrap">
        <table class="grammar-table">
          <tr><th>Subject</th><th>Country</th><th>Nationality</th></tr>
          <tr><td>I</td><td><strong>am from</strong> Brazil</td><td><strong>am</strong> Brazilian</td></tr>
          <tr><td>You</td><td><strong>are from</strong> France</td><td><strong>are</strong> French</td></tr>
          <tr><td>He / She</td><td><strong>is from</strong> Australia</td><td><strong>is</strong> Australian</td></tr>
          <tr><td>They</td><td><strong>are from</strong> Japan</td><td><strong>are</strong> Japanese</td></tr>
        </table>
        <p style="font-size:.85rem;margin-top:.8rem;color:var(--text-mid);">Question: <strong>Where are you from?</strong> / <strong>What is your nationality?</strong></p>
      </div>
    </div>
  </div>
</div>

<!-- SLIDE 184: L7 COMMON MISTAKE -->
<div class="slide slide-light" data-slide="184" data-phase="3" data-lesson="7" data-teacher="<strong>Common Mistake (3 min):</strong> 'Em portugu&ecirc;s: brasileiro/brasileira. Em ingl&ecirc;s: Brazilian para TODOS. E NUNCA 'I am Brazil' &mdash; Brazil &eacute; o pa&iacute;s, Brazilian &eacute; a pessoa. E sempre AM/IS/ARE + FROM &mdash; nunca 'I from Brazil' sem o verbo.' Drill: 'I AM from Brazil.' 3x.">
  <div class="slide-inner">
    <h2 class="slide-heading">Common <span class="accent">Mistake</span></h2>
    <div class="mistake-card">
      <div class="mistake-item mistake-wrong">
        <div class="mistake-icon"><svg viewBox="0 0 24 24" fill="none" stroke="#dc2626"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg></div>
        &ldquo;I from Brazil.&rdquo;
      </div>
      <div class="mistake-item mistake-right">
        <div class="mistake-icon"><svg viewBox="0 0 24 24" fill="none" stroke="#16a34a"><polyline points="20 6 9 17 4 12"/></svg></div>
        &ldquo;<strong>I am from</strong> Brazil.&rdquo; &mdash; Always use AM/IS/ARE
      </div>
    </div>
    <div class="mistake-card" style="margin-top:1rem;">
      <div class="mistake-item mistake-wrong">
        <div class="mistake-icon"><svg viewBox="0 0 24 24" fill="none" stroke="#dc2626"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg></div>
        &ldquo;I am Brazil.&rdquo;
      </div>
      <div class="mistake-item mistake-right">
        <div class="mistake-icon"><svg viewBox="0 0 24 24" fill="none" stroke="#16a34a"><polyline points="20 6 9 17 4 12"/></svg></div>
        &ldquo;<strong>I am Brazilian</strong>.&rdquo; &mdash; Use the nationality, not the country name
      </div>
    </div>
    <div class="mistake-card" style="margin-top:1rem;">
      <div class="mistake-item mistake-wrong">
        <div class="mistake-icon"><svg viewBox="0 0 24 24" fill="none" stroke="#dc2626"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg></div>
        &ldquo;She is Francesa.&rdquo; (mixing Portuguese)
      </div>
      <div class="mistake-item mistake-right">
        <div class="mistake-icon"><svg viewBox="0 0 24 24" fill="none" stroke="#16a34a"><polyline points="20 6 9 17 4 12"/></svg></div>
        &ldquo;<strong>She is French</strong>.&rdquo; &mdash; No gender change in English!
      </div>
    </div>
  </div>
</div>

<!-- SLIDE 185: L7 GRAMMAR PRACTICE -->
<div class="slide slide-light" data-slide="185" data-phase="3" data-lesson="7" data-teacher="<strong>Grammar Practice (4 min):</strong> Clique cada item para revelar. Use celebridades que Gabriela conhece! 'Blake Lively is...?' Ela diz, voc&ecirc; confirma. Foco em AM/IS/ARE + nationality vs FROM + country.">
  <div class="slide-inner">
    <h2 class="slide-heading">Say the <span class="accent">Nationality</span></h2>
    <div class="fill-grid">
      <div class="fill-item" onclick="this.classList.toggle('revealed')">
        <div class="fill-text">Blake Lively (USA) &rarr; <span class="fill-blank">???</span><span class="fill-answer">She is American. She is from the USA.</span></div>
      </div>
      <div class="fill-item" onclick="this.classList.toggle('revealed')">
        <div class="fill-text">Ed Westwick (England) &rarr; <span class="fill-blank">???</span><span class="fill-answer">He is English. He is from England.</span></div>
      </div>
      <div class="fill-item" onclick="this.classList.toggle('revealed')">
        <div class="fill-text">Chris Hemsworth (Australia) &rarr; <span class="fill-blank">???</span><span class="fill-answer">He is Australian. He is from Australia.</span></div>
      </div>
      <div class="fill-item" onclick="this.classList.toggle('revealed')">
        <div class="fill-text">Lily Collins (England) &rarr; <span class="fill-blank">???</span><span class="fill-answer">She is English. She is from England.</span></div>
      </div>
      <div class="fill-item" onclick="this.classList.toggle('revealed')">
        <div class="fill-text">Jennifer Aniston (USA) &rarr; <span class="fill-blank">???</span><span class="fill-answer">She is American. She is from the USA.</span></div>
      </div>
      <div class="fill-item" onclick="this.classList.toggle('revealed')">
        <div class="fill-text">Gabriela Pires (Brazil) &rarr; <span class="fill-blank">???</span><span class="fill-answer">She is Brazilian. She is from Brazil.</span></div>
      </div>
    </div>
  </div>
</div>

<!-- SLIDE 186: L7 CHAPTER 4 TRANSITION -->
<div class="slide slide-image" data-slide="186" data-phase="4" data-lesson="7" data-teacher="<strong>Transi&ccedil;&atilde;o (10s):</strong> 'Now imagine: you arrive at the Paris hostel. You sit in the lounge and someone says Hi...' Avance." style="background-image:url('https://images.unsplash.com/photo-1502602898657-3e91760cbb34?w=600&q=80')">
  <div class="slide-inner">
    <div class="chapter-label">Chapter 4</div>
    <h1 class="slide-title">Getting <span class="accent">There</span></h1>
    <p class="slide-subtitle">Gabriela meets a traveler at the hostel</p>
  </div>
</div>

<!-- SLIDE 187: L7 DIALOGUE LINE-BY-LINE -->
<div class="slide slide-dark" data-slide="187" data-phase="4" data-lesson="7" data-teacher="<strong>Di&aacute;logo (8 min):</strong> Clique Next Line para cada fala. Professor l&ecirc; Liam (voz masculina Arthur), Gabriela l&ecirc; suas falas. Vocabul&aacute;rio da aula em destaque rosa. Foco em 'I am from', nationality, languages. Depois pergunte: 'Where is Liam from? What languages does he speak?'">
  <div class="slide-inner">
    <h2 class="slide-heading" style="color:#fff">At the <span class="accent">Hostel</span></h2>
    <div class="dialogue-box" id="dial7">
      <div class="dialogue-line" data-voice="ellen" style="opacity:0;transform:translateY(10px)">
        <div class="avatar" style="background:var(--accent)">G</div>
        <div class="bubble"><strong>Gabriela:</strong> Hi! I am Gabriela. I am <strong>from</strong> Brazil.<br><button class="audio-btn-sm" onclick="speakText('Hi! I am Gabriela. I am from Brazil.',this)"><svg viewBox="0 0 24 24"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/></svg> Listen</button></div>
      </div>
      <div class="dialogue-line" data-voice="arthur" style="opacity:0;transform:translateY(10px)">
        <div class="avatar" style="background:var(--navy)">L</div>
        <div class="bubble"><strong>Liam:</strong> Hey! I am Liam. I am <strong>from</strong> Australia.<br><button class="audio-btn-sm" onclick="speakText('Hey! I am Liam. I am from Australia.',this)"><svg viewBox="0 0 24 24"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/></svg> Listen</button></div>
      </div>
      <div class="dialogue-line" data-voice="ellen" style="opacity:0;transform:translateY(10px)">
        <div class="avatar" style="background:var(--accent)">G</div>
        <div class="bubble"><strong>Gabriela:</strong> Nice to meet you! Where in Australia?<br><button class="audio-btn-sm" onclick="speakText('Nice to meet you! Where in Australia?',this)"><svg viewBox="0 0 24 24"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/></svg> Listen</button></div>
      </div>
      <div class="dialogue-line" data-voice="arthur" style="opacity:0;transform:translateY(10px)">
        <div class="avatar" style="background:var(--navy)">L</div>
        <div class="bubble"><strong>Liam:</strong> I am from Sydney. And you? Where in Brazil?<br><button class="audio-btn-sm" onclick="speakText('I am from Sydney. And you? Where in Brazil?',this)"><svg viewBox="0 0 24 24"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/></svg> Listen</button></div>
      </div>
      <div class="dialogue-line" data-voice="ellen" style="opacity:0;transform:translateY(10px)">
        <div class="avatar" style="background:var(--accent)">G</div>
        <div class="bubble"><strong>Gabriela:</strong> I am from Sao Paulo. It is a huge city!<br><button class="audio-btn-sm" onclick="speakText('I am from Sao Paulo. It is a huge city!',this)"><svg viewBox="0 0 24 24"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/></svg> Listen</button></div>
      </div>
      <div class="dialogue-line" data-voice="arthur" style="opacity:0;transform:translateY(10px)">
        <div class="avatar" style="background:var(--navy)">L</div>
        <div class="bubble"><strong>Liam:</strong> Cool! What <strong>languages</strong> do you speak?<br><button class="audio-btn-sm" onclick="speakText('Cool! What languages do you speak?',this)"><svg viewBox="0 0 24 24"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/></svg> Listen</button></div>
      </div>
      <div class="dialogue-line" data-voice="ellen" style="opacity:0;transform:translateY(10px)">
        <div class="avatar" style="background:var(--accent)">G</div>
        <div class="bubble"><strong>Gabriela:</strong> I speak Portuguese and I am learning English. What about you?<br><button class="audio-btn-sm" onclick="speakText('I speak Portuguese and I am learning English. What about you?',this)"><svg viewBox="0 0 24 24"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/></svg> Listen</button></div>
      </div>
      <div class="dialogue-line" data-voice="arthur" style="opacity:0;transform:translateY(10px)">
        <div class="avatar" style="background:var(--navy)">L</div>
        <div class="bubble"><strong>Liam:</strong> I speak English and a little bit of <strong>French</strong>.<br><button class="audio-btn-sm" onclick="speakText('I speak English and a little bit of French.',this)"><svg viewBox="0 0 24 24"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/></svg> Listen</button></div>
      </div>
      <div class="dialogue-line" data-voice="ellen" style="opacity:0;transform:translateY(10px)">
        <div class="avatar" style="background:var(--accent)">G</div>
        <div class="bubble"><strong>Gabriela:</strong> That is awesome! How long are you in Paris?<br><button class="audio-btn-sm" onclick="speakText('That is awesome! How long are you in Paris?',this)"><svg viewBox="0 0 24 24"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/></svg> Listen</button></div>
      </div>
      <div class="dialogue-line" data-voice="arthur" style="opacity:0;transform:translateY(10px)">
        <div class="avatar" style="background:var(--navy)">L</div>
        <div class="bubble"><strong>Liam:</strong> Two weeks! This hostel is so <strong>international</strong>!<br><button class="audio-btn-sm" onclick="speakText('Two weeks! This hostel is so international!',this)"><svg viewBox="0 0 24 24"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/></svg> Listen</button></div>
      </div>
    </div>
    <div style="text-align:center;margin-top:1rem;">
      <button class="btn-primary" onclick="var lines=document.querySelectorAll('#dial7 .dialogue-line');var shown=document.querySelectorAll('#dial7 .dialogue-line[style*=\\'opacity: 1\\']').length||document.querySelectorAll('#dial7 .dialogue-line.shown').length;lines.forEach(function(l,i){if(i<=shown){l.style.opacity='1';l.style.transform='translateY(0)';l.classList.add('shown')}})">Next Line</button>
    </div>
  </div>
</div>

<!-- SLIDE 188: L7 COMPREHENSION -->
<div class="slide slide-dark" data-slide="188" data-phase="4" data-lesson="7" data-teacher="<strong>Comprehension (3 min):</strong> Pergunte SEM mostrar respostas. Depois clique para revelar. Se Gabriela acertar, celebre! Foco: compreens&atilde;o do que LIAM disse.">
  <div class="slide-inner">
    <h2 class="slide-heading" style="color:#fff">Did You <span class="accent">Catch</span> That?</h2>
    <div class="comp-questions">
      <div class="comp-q" onclick="this.classList.toggle('revealed')">
        <div class="q-text">Where is Liam from?</div>
        <div class="q-answer">Australia (Sydney)</div>
      </div>
      <div class="comp-q" onclick="this.classList.toggle('revealed')">
        <div class="q-text">What languages does Liam speak?</div>
        <div class="q-answer">English and a little bit of French</div>
      </div>
      <div class="comp-q" onclick="this.classList.toggle('revealed')">
        <div class="q-text">How long is Liam in Paris?</div>
        <div class="q-answer">Two weeks</div>
      </div>
    </div>
  </div>
</div>

<!-- SLIDE 189: L7 LISTENING 1 -->
<div class="slide slide-dark" data-slide="189" data-phase="4" data-lesson="7" data-teacher="<strong>Listening 1 (4 min):</strong> Toque o &aacute;udio PRIMEIRO. Gabriela ouve SEM texto. Depois pergunte: 'Where is Liam from? What nationality is Yuki? How many languages does Marco speak?' Toque novamente se preciso. Foco em extra&ccedil;&atilde;o de informa&ccedil;&atilde;o sobre nacionalidade.">
  <div class="slide-inner">
    <h2 class="slide-heading" style="color:#fff">Listen <span class="accent">First</span></h2>
    <p style="color:rgba(255,255,255,.6);text-align:center;margin-bottom:1.5rem;">Close your eyes and listen. What countries and nationalities do you hear?</p>
    <div style="display:flex;flex-direction:column;align-items:center;gap:1rem;">
      <div style="width:200px;height:60px;background:rgba(255,255,255,.06);border-radius:30px;display:flex;align-items:center;justify-content:center;">
        <button class="btn-primary" onclick="speakText('Gabriela is at a youth hostel in Paris. She meets travelers from many countries. Liam is from Australia. He is Australian. He speaks English and a little French. Yuki is from Japan. She is Japanese. She speaks Japanese and English. Marco is from Italy. He is Italian. He speaks Italian, English, and French. Gabriela is from Brazil. She is Brazilian. She speaks Portuguese and she is learning English. The hostel is very international. There are people from ten different countries.',this)" style="border-radius:30px;padding:.8rem 2rem;">
          <svg viewBox="0 0 24 24" width="20" height="20" fill="none" stroke="currentColor" stroke-width="2"><polygon points="5 3 19 12 5 21 5 3"/></svg>
          &nbsp;Play
        </button>
      </div>
    </div>
    <div class="comp-questions" style="margin-top:2rem;">
      <div class="comp-q" onclick="this.classList.toggle('revealed')">
        <div class="q-text">Where is Liam from?</div>
        <div class="q-answer">Australia</div>
      </div>
      <div class="comp-q" onclick="this.classList.toggle('revealed')">
        <div class="q-text">What nationality is Yuki?</div>
        <div class="q-answer">Japanese</div>
      </div>
      <div class="comp-q" onclick="this.classList.toggle('revealed')">
        <div class="q-text">How many languages does Marco speak?</div>
        <div class="q-answer">Three (Italian, English, and French)</div>
      </div>
    </div>
  </div>
</div>

<!-- SLIDE 190: L7 LISTENING 2 -->
<div class="slide slide-dark" data-slide="190" data-phase="4" data-lesson="7" data-teacher="<strong>Listening 2 (3 min):</strong> 3 pessoas se apresentam. Toque primeiro sem texto. Perguntas: 'Where is Sophie from? What is Kenji&rsquo;s nationality? What language does Carlos speak?'">
  <div class="slide-inner">
    <h2 class="slide-heading" style="color:#fff">Listen <span class="accent">Again</span></h2>
    <p style="color:rgba(255,255,255,.6);text-align:center;margin-bottom:1.5rem;">Three travelers introduce themselves. Listen and answer.</p>
    <div style="display:flex;flex-direction:column;align-items:center;gap:.5rem;">
      <button class="btn-primary" onclick="speakText('Hi! My name is Sophie. I am from Canada. I am Canadian. I speak English and French.',this)" style="border-radius:30px;padding:.6rem 1.5rem;font-size:.85rem;"><svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2"><polygon points="5 3 19 12 5 21 5 3"/></svg> &nbsp;Person 1</button>
      <button class="btn-primary" onclick="speakText('Hello! I am Kenji. I am from Japan. I am Japanese. I speak Japanese and a little English.',this)" style="border-radius:30px;padding:.6rem 1.5rem;font-size:.85rem;"><svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2"><polygon points="5 3 19 12 5 21 5 3"/></svg> &nbsp;Person 2</button>
      <button class="btn-primary" onclick="speakText('Hey! I am Carlos. I am from Mexico. I am Mexican. I speak Spanish and English.',this)" style="border-radius:30px;padding:.6rem 1.5rem;font-size:.85rem;"><svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2"><polygon points="5 3 19 12 5 21 5 3"/></svg> &nbsp;Person 3</button>
    </div>
    <div class="comp-questions" style="margin-top:1.5rem;">
      <div class="comp-q" onclick="this.classList.toggle('revealed')">
        <div class="q-text">Where is Sophie from?</div>
        <div class="q-answer">Canada (she is Canadian)</div>
      </div>
      <div class="comp-q" onclick="this.classList.toggle('revealed')">
        <div class="q-text">What is Kenji&rsquo;s nationality?</div>
        <div class="q-answer">Japanese (he is from Japan)</div>
      </div>
      <div class="comp-q" onclick="this.classList.toggle('revealed')">
        <div class="q-text">What languages does Carlos speak?</div>
        <div class="q-answer">Spanish and English</div>
      </div>
    </div>
  </div>
</div>

<!-- SLIDE 191: L7 ARTIFACT - TRAVEL PROFILE CARD -->
<div class="slide slide-light" data-slide="191" data-phase="4" data-lesson="7" data-teacher="<strong>Artefato (3 min):</strong> 'Look! This is Gabriela&rsquo;s Travel Profile Card &mdash; like a passport for the hostel!' Pergunte: 'What is Gabriela&rsquo;s nationality? What languages does she speak? Where is she from?' Gabriela responde usando o vocabul&aacute;rio da aula.">
  <div class="slide-inner">
    <h2 class="slide-heading">Gabriela&rsquo;s Travel <span class="accent">Profile Card</span></h2>
    <div style="background:#fff;border-radius:16px;overflow:hidden;max-width:420px;margin:0 auto;box-shadow:0 20px 60px rgba(0,0,0,.1);border:2px solid var(--accent)">
      <div style="background:linear-gradient(135deg,var(--accent),#1e5fa0);color:#fff;padding:1.2rem 1.5rem;display:flex;align-items:center;gap:1rem">
        <div style="width:50px;height:50px;border-radius:50%;background:rgba(255,255,255,.2);display:flex;align-items:center;justify-content:center;font-size:1.5rem;font-weight:800;">G</div>
        <div>
          <div style="font-weight:700;font-size:1.1rem;letter-spacing:.5px;">TRAVEL PROFILE</div>
          <div style="font-size:.7rem;opacity:.7;text-transform:uppercase;letter-spacing:2px;">Youth Hostel Paris</div>
        </div>
      </div>
      <div style="padding:1.2rem 1.5rem;">
        <div style="display:grid;grid-template-columns:auto 1fr;gap:.5rem 1rem;font-size:.9rem;line-height:1.7;">
          <strong style="color:var(--accent)">Name</strong><span>Gabriela Pires</span>
          <strong style="color:var(--accent)">From</strong><span>S&atilde;o Paulo, <strong>Brazil</strong></span>
          <strong style="color:var(--accent)">Nationality</strong><span><strong>Brazilian</strong></span>
          <strong style="color:var(--accent)">Languages</strong><span>Portuguese, English (learning)</span>
          <strong style="color:var(--accent)">Passport</strong><span>Brazilian</span>
          <strong style="color:var(--accent)">Age</strong><span>16</span>
          <strong style="color:var(--accent)">In Paris</strong><span>2 weeks (Feb 2027)</span>
        </div>
      </div>
      <div style="background:var(--accent-dim);padding:.8rem 1.5rem;font-size:.78rem;color:var(--text-mid);text-align:center;border-top:1px solid var(--border);">
        Fun fact: Paris hostels have travelers from 50+ countries!
      </div>
    </div>
  </div>
</div>

<!-- SLIDE 192: L7 CHAPTER 5 TRANSITION -->
<div class="slide slide-image" data-slide="192" data-phase="5" data-lesson="7" data-teacher="<strong>Transi&ccedil;&atilde;o (10s):</strong> 'Time to practice! Show me you can talk about countries and nationalities!' Avance." style="background-image:url('https://images.unsplash.com/photo-1502602898657-3e91760cbb34?w=600&q=80')">
  <div class="slide-inner">
    <div class="chapter-label">Chapter 5</div>
    <h1 class="slide-title"><span class="accent">Practice</span></h1>
    <p class="slide-subtitle">Countries, nationalities, and languages in action</p>
  </div>
</div>

<!-- SLIDE 193: L7 QUICK FIRE -->
<div class="slide slide-light" data-slide="193" data-phase="5" data-lesson="7" data-teacher="<strong>Quick Fire (6 min):</strong> Uma pergunta por vez. Gabriela responde ORALMENTE primeiro, depois clique Show Answer. Se travar: 'Start with I AM...' ou 'Start with SHE IS...' Score: 6 acertos = confetti!">
  <div class="slide-inner">
    <h2 class="slide-heading">Quick <span class="accent">Fire</span></h2>
    <div id="qf7" style="min-height:200px;">
      <div class="qf-item" data-qf="1" style="display:block;">
        <p style="font-size:1.2rem;text-align:center;margin-bottom:1rem;">Someone asks: <strong>&ldquo;Where are you from?&rdquo;</strong> What do you say?</p>
        <div style="text-align:center;">
          <button class="btn-secondary" onclick="this.nextElementSibling.style.display='block';this.style.display='none'">Show Answer</button>
          <p style="display:none;font-size:1.1rem;color:var(--accent);font-weight:700;">I am from Brazil. / I am from Sao Paulo, Brazil.</p>
        </div>
      </div>
      <div class="qf-item" data-qf="2" style="display:none;">
        <p style="font-size:1.2rem;text-align:center;margin-bottom:1rem;">Blake Lively is from the USA. What is her <strong>nationality</strong>?</p>
        <div style="text-align:center;">
          <button class="btn-secondary" onclick="this.nextElementSibling.style.display='block';this.style.display='none'">Show Answer</button>
          <p style="display:none;font-size:1.1rem;color:var(--accent);font-weight:700;">She is American.</p>
        </div>
      </div>
      <div class="qf-item" data-qf="3" style="display:none;">
        <p style="font-size:1.2rem;text-align:center;margin-bottom:1rem;">You want to know where someone is from. What do you ask?</p>
        <div style="text-align:center;">
          <button class="btn-secondary" onclick="this.nextElementSibling.style.display='block';this.style.display='none'">Show Answer</button>
          <p style="display:none;font-size:1.1rem;color:var(--accent);font-weight:700;">Where are you from?</p>
        </div>
      </div>
      <div class="qf-item" data-qf="4" style="display:none;">
        <p style="font-size:1.2rem;text-align:center;margin-bottom:1rem;">Ed Westwick is from England. What is his nationality?</p>
        <div style="text-align:center;">
          <button class="btn-secondary" onclick="this.nextElementSibling.style.display='block';this.style.display='none'">Show Answer</button>
          <p style="display:none;font-size:1.1rem;color:var(--accent);font-weight:700;">He is English.</p>
        </div>
      </div>
      <div class="qf-item" data-qf="5" style="display:none;">
        <p style="font-size:1.2rem;text-align:center;margin-bottom:1rem;">You speak Portuguese and you are learning English. Say it!</p>
        <div style="text-align:center;">
          <button class="btn-secondary" onclick="this.nextElementSibling.style.display='block';this.style.display='none'">Show Answer</button>
          <p style="display:none;font-size:1.1rem;color:var(--accent);font-weight:700;">I speak Portuguese and I am learning English.</p>
        </div>
      </div>
      <div class="qf-item" data-qf="6" style="display:none;">
        <p style="font-size:1.2rem;text-align:center;margin-bottom:1rem;">Chris Hemsworth is from Australia. Complete: He is ___.</p>
        <div style="text-align:center;">
          <button class="btn-secondary" onclick="this.nextElementSibling.style.display='block';this.style.display='none'">Show Answer</button>
          <p style="display:none;font-size:1.1rem;color:var(--accent);font-weight:700;">He is Australian.</p>
        </div>
      </div>
    </div>
    <div style="text-align:center;margin-top:1rem;">
      <span id="qf7score" style="font-weight:700;color:var(--accent);">1 / 6</span>
      <button class="btn-primary" style="margin-left:1rem;" onclick="var items=document.querySelectorAll('#qf7 .qf-item');var cur=0;items.forEach(function(it,i){if(it.style.display==='block')cur=i});if(cur<items.length-1){items[cur].style.display='none';items[cur+1].style.display='block';document.getElementById('qf7score').textContent=(cur+2)+' / 6';}">Next Question</button>
    </div>
  </div>
</div>

<!-- SLIDE 194: L7 SPOT THE ERROR -->
<div class="slide slide-light" data-slide="194" data-phase="5" data-lesson="7" data-teacher="<strong>Spot the Error (4 min):</strong> Gabriela identifica o erro PRIMEIRO. Depois clique para revelar. Foco: I AM FROM (n&atilde;o I FROM), nationality (n&atilde;o country name), no gender change.">
  <div class="slide-inner">
    <h2 class="slide-heading">Spot the <span class="accent">Error</span></h2>
    <div style="display:flex;flex-direction:column;gap:.8rem;">
      <div class="error-card" onclick="this.classList.toggle('revealed')" style="background:#fff;border:1px solid #e8e4df;border-radius:10px;padding:1rem 1.2rem;cursor:pointer;transition:all .3s;">
        <div class="error-wrong" style="font-size:1rem;color:var(--danger);text-decoration:line-through;">&ldquo;I from Brazil.&rdquo;</div>
        <div class="error-correct" style="display:none;font-size:1rem;color:var(--success);font-weight:700;margin-top:.5rem;">&ldquo;I am from Brazil.&rdquo; &mdash; Never forget AM/IS/ARE!</div>
      </div>
      <div class="error-card" onclick="this.classList.toggle('revealed')" style="background:#fff;border:1px solid #e8e4df;border-radius:10px;padding:1rem 1.2rem;cursor:pointer;transition:all .3s;">
        <div class="error-wrong" style="font-size:1rem;color:var(--danger);text-decoration:line-through;">&ldquo;I am Brazil.&rdquo;</div>
        <div class="error-correct" style="display:none;font-size:1rem;color:var(--success);font-weight:700;margin-top:.5rem;">&ldquo;I am Brazilian.&rdquo; &mdash; Use the nationality, not the country!</div>
      </div>
      <div class="error-card" onclick="this.classList.toggle('revealed')" style="background:#fff;border:1px solid #e8e4df;border-radius:10px;padding:1rem 1.2rem;cursor:pointer;transition:all .3s;">
        <div class="error-wrong" style="font-size:1rem;color:var(--danger);text-decoration:line-through;">&ldquo;She is Americana.&rdquo;</div>
        <div class="error-correct" style="display:none;font-size:1rem;color:var(--success);font-weight:700;margin-top:.5rem;">&ldquo;She is American.&rdquo; &mdash; No gender change in English!</div>
      </div>
      <div class="error-card" onclick="this.classList.toggle('revealed')" style="background:#fff;border:1px solid #e8e4df;border-radius:10px;padding:1rem 1.2rem;cursor:pointer;transition:all .3s;">
        <div class="error-wrong" style="font-size:1rem;color:var(--danger);text-decoration:line-through;">&ldquo;Where you from?&rdquo;</div>
        <div class="error-correct" style="display:none;font-size:1rem;color:var(--success);font-weight:700;margin-top:.5rem;">&ldquo;Where are you from?&rdquo; &mdash; Questions need ARE!</div>
      </div>
    </div>
  </div>
</div>

<!-- SLIDE 195: L7 CELEBRITY NATIONALITY GAME -->
<div class="slide slide-light" data-slide="195" data-phase="5" data-lesson="7" data-teacher="<strong>Celebrity Game (4 min):</strong> Mostre os nomes. Gabriela diz: 'He/She is [nationality]. He/She is from [country].' Foco em flu&ecirc;ncia e velocidade. 10 segundos por celebridade. Se travar: d&ecirc; a primeira palavra.">
  <div class="slide-inner">
    <h2 class="slide-heading">Celebrity <span class="accent">Nationalities</span></h2>
    <p style="text-align:center;font-size:.9rem;color:var(--text-mid);margin-bottom:1.5rem;">Say: &ldquo;He/She is [nationality]. He/She is from [country].&rdquo;</p>
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:1rem;margin-top:1rem;">
      <div style="background:#fff;border:1px solid #e8e4df;border-radius:10px;padding:1rem;text-align:center;">
        <div style="font-weight:800;font-size:1.1rem;color:var(--accent);">Jennifer Aniston</div>
        <div style="font-size:.8rem;color:var(--text-dim);">(Friends)</div>
      </div>
      <div style="background:#fff;border:1px solid #e8e4df;border-radius:10px;padding:1rem;text-align:center;">
        <div style="font-weight:800;font-size:1.1rem;color:var(--accent);">Ed Westwick</div>
        <div style="font-size:.8rem;color:var(--text-dim);">(Gossip Girl)</div>
      </div>
      <div style="background:#fff;border:1px solid #e8e4df;border-radius:10px;padding:1rem;text-align:center;">
        <div style="font-weight:800;font-size:1.1rem;color:var(--accent);">Chris Hemsworth</div>
        <div style="font-size:.8rem;color:var(--text-dim);">(Thor)</div>
      </div>
      <div style="background:#fff;border:1px solid #e8e4df;border-radius:10px;padding:1rem;text-align:center;">
        <div style="font-weight:800;font-size:1.1rem;color:var(--accent);">Lily Collins</div>
        <div style="font-size:.8rem;color:var(--text-dim);">(Emily in Paris)</div>
      </div>
      <div style="background:#fff;border:1px solid #e8e4df;border-radius:10px;padding:1rem;text-align:center;">
        <div style="font-weight:800;font-size:1.1rem;color:var(--accent);">Ryan Reynolds</div>
        <div style="font-size:.8rem;color:var(--text-dim);">(Deadpool)</div>
      </div>
      <div style="background:#fff;border:1px solid #e8e4df;border-radius:10px;padding:1rem;text-align:center;">
        <div style="font-weight:800;font-size:1.1rem;color:var(--accent);">Monica Bellucci</div>
        <div style="font-size:.8rem;color:var(--text-dim);">(Matrix, Bond)</div>
      </div>
    </div>
  </div>
</div>

<!-- SLIDE 196: L7 CHAPTER 6 TRANSITION -->
<div class="slide slide-image" data-slide="196" data-phase="6" data-lesson="7" data-teacher="<strong>Transi&ccedil;&atilde;o (10s):</strong> 'From guided to free &mdash; show what you learned!' Avance." style="background-image:url('https://images.unsplash.com/photo-1502602898657-3e91760cbb34?w=600&q=80')">
  <div class="slide-inner">
    <div class="chapter-label">Chapter 6</div>
    <h1 class="slide-title">Your <span class="accent">Turn</span></h1>
    <p class="slide-subtitle">From guided to free &mdash; show what you learned</p>
  </div>
</div>

<!-- SLIDE 197: L7 ROLE-PLAY GUIDED -->
<div class="slide slide-dark" data-slide="197" data-phase="6" data-lesson="7" data-teacher="<strong>Role-play Guided (5 min):</strong> Professor = Sophie (Canadian traveler). Gabriela se apresenta usando keywords vis&iacute;veis. CCQ: 'How do you ask where someone is from?' &rarr; 'Where are you from?' Se travar: modele a frase e ela repete.">
  <div class="slide-inner">
    <h2 class="slide-heading" style="color:#fff">Role-Play: <span class="accent">Guided</span></h2>
    <div class="roleplay-card" style="background:linear-gradient(135deg,rgba(212,50,106,.15),rgba(212,50,106,.05));border:1px solid rgba(212,50,106,.3);border-radius:12px;padding:1.5rem;">
      <div style="display:flex;align-items:center;gap:.8rem;margin-bottom:1rem;">
        <svg viewBox="0 0 24 24" width="32" height="32" fill="none" stroke="var(--accent)" stroke-width="1.5"><circle cx="12" cy="12" r="10"/><path d="M2 12h20M12 2a15.3 15.3 0 014 10 15.3 15.3 0 01-4 10 15.3 15.3 0 01-4-10 15.3 15.3 0 014-10z"/></svg>
        <div>
          <div style="font-weight:700;font-size:1.1rem;color:#fff;">Hostel Lounge &mdash; Meeting Sophie</div>
          <div style="font-size:.8rem;color:rgba(255,255,255,.6);">Teacher = Sophie (Canadian) &middot; Gabriela = herself</div>
        </div>
      </div>
      <p style="color:rgba(255,255,255,.8);font-size:.9rem;margin-bottom:1rem;">Introduce yourself: say your name, where you are from, your nationality, and what languages you speak.</p>
      <div style="display:flex;flex-wrap:wrap;gap:.4rem;">
        <span style="padding:.3rem .8rem;border:1px solid var(--accent);border-radius:20px;font-size:.82rem;color:var(--accent);">Gabriela</span>
        <span style="padding:.3rem .8rem;border:1px solid var(--accent);border-radius:20px;font-size:.82rem;color:var(--accent);">Sao Paulo</span>
        <span style="padding:.3rem .8rem;border:1px solid var(--accent);border-radius:20px;font-size:.82rem;color:var(--accent);">Brazilian</span>
        <span style="padding:.3rem .8rem;border:1px solid var(--accent);border-radius:20px;font-size:.82rem;color:var(--accent);">Portuguese</span>
        <span style="padding:.3rem .8rem;border:1px solid var(--accent);border-radius:20px;font-size:.82rem;color:var(--accent);">learning English</span>
      </div>
    </div>
  </div>
</div>

<!-- SLIDE 198: L7 ROLE-PLAY SEMI-FREE -->
<div class="slide slide-dark" data-slide="198" data-phase="6" data-lesson="7" data-teacher="<strong>Role-play Semi-free (5 min):</strong> Professor = Kenji (Japanese traveler). MENOS keywords. Gabriela pergunta de onde ele &eacute;, que l&iacute;nguas fala, e responde sobre si mesma. Se travar em 5s, d&ecirc; 1 palavra de pista. Elogie flu&ecirc;ncia.">
  <div class="slide-inner">
    <h2 class="slide-heading" style="color:#fff">Role-Play: <span class="accent">Semi-Free</span></h2>
    <div class="roleplay-card" style="background:linear-gradient(135deg,rgba(0,48,128,.15),rgba(0,48,128,.05));border:1px solid rgba(0,48,128,.3);border-radius:12px;padding:1.5rem;">
      <div style="display:flex;align-items:center;gap:.8rem;margin-bottom:1rem;">
        <svg viewBox="0 0 24 24" width="32" height="32" fill="none" stroke="var(--accent)" stroke-width="1.5"><path d="M17 21v-2a4 4 0 00-4-4H5a4 4 0 00-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 00-3-3.87M16 3.13a4 4 0 010 7.75"/></svg>
        <div>
          <div style="font-weight:700;font-size:1.1rem;color:#fff;">Hostel Kitchen &mdash; Meeting Kenji</div>
          <div style="font-size:.8rem;color:rgba(255,255,255,.6);">Less help this time!</div>
        </div>
      </div>
      <p style="color:rgba(255,255,255,.8);font-size:.9rem;margin-bottom:1rem;">Ask Kenji where he is from, his nationality, and what languages he speaks. Then introduce yourself.</p>
      <div style="display:flex;flex-wrap:wrap;gap:.4rem;">
        <span style="padding:.3rem .8rem;border:1px solid rgba(255,255,255,.3);border-radius:20px;font-size:.82rem;color:rgba(255,255,255,.5);">where...from?</span>
        <span style="padding:.3rem .8rem;border:1px solid rgba(255,255,255,.3);border-radius:20px;font-size:.82rem;color:rgba(255,255,255,.5);">languages</span>
      </div>
    </div>
  </div>
</div>

<!-- SLIDE 199: L7 ROLE-PLAY FREE -->
<div class="slide slide-dark" data-slide="199" data-phase="6" data-lesson="7" data-teacher="<strong>Role-play Free (5 min):</strong> Professor = viajante misterioso (n&atilde;o revele de onde &eacute;). ZERO keywords. Gabriela faz PERGUNTAS para descobrir a nacionalidade do viajante. Delayed feedback: anote erros e corrija DEPOIS. Elogie muito &mdash; ela est&aacute; no n&iacute;vel m&aacute;ximo da aula.">
  <div class="slide-inner">
    <h2 class="slide-heading" style="color:#fff">Role-Play: <span class="accent">Free</span></h2>
    <div class="roleplay-card" style="background:linear-gradient(135deg,rgba(22,163,74,.12),rgba(22,163,74,.04));border:1px solid rgba(22,163,74,.3);border-radius:12px;padding:1.5rem;">
      <div style="display:flex;align-items:center;gap:.8rem;margin-bottom:1rem;">
        <svg viewBox="0 0 24 24" width="32" height="32" fill="none" stroke="#16a34a" stroke-width="1.5"><circle cx="12" cy="12" r="10"/><path d="M9.09 9a3 3 0 015.83 1c0 2-3 3-3 3M12 17h.01"/></svg>
        <div>
          <div style="font-weight:700;font-size:1.1rem;color:#fff;">Mystery Traveler at the Hostel Bar</div>
          <div style="font-size:.8rem;color:rgba(255,255,255,.6);">No keywords &mdash; you are on your own!</div>
        </div>
      </div>
      <p style="color:rgba(255,255,255,.8);font-size:.9rem;">A new traveler sits next to you. Find out: their name, country, nationality, and languages. Then introduce yourself completely.</p>
    </div>
  </div>
</div>

<!-- SLIDE 200: L7 CHAPTER 7 TRANSITION -->
<div class="slide slide-image" data-slide="200" data-phase="7" data-lesson="7" data-teacher="<strong>Transi&ccedil;&atilde;o (10s):</strong> 'Amazing work today! Let us wrap up.' Avance." style="background-image:url('https://images.unsplash.com/photo-1502602898657-3e91760cbb34?w=600&q=80')">
  <div class="slide-inner">
    <div class="chapter-label">Chapter 7</div>
    <h1 class="slide-title">Wrap-<span class="accent">Up</span></h1>
    <p class="slide-subtitle">Your nationality survival kit for Paris</p>
  </div>
</div>

<!-- SLIDE 201: L7 SURVIVAL CARD -->
<div class="slide slide-dark" data-slide="201" data-phase="7" data-lesson="7" data-teacher="<strong>Survival Card (2 min):</strong> Leia cada frase com Gabriela. Toque audio. Ela repete 2x cada. Estas 5 frases s&atilde;o as que ela PRECISA para se apresentar no hostel.">
  <div class="slide-inner">
    <h2 class="slide-heading" style="color:#fff">Survival <span class="accent">Card</span></h2>
    <div style="display:flex;flex-direction:column;gap:.6rem;margin-top:1.5rem;">
      <div class="survival-item-ic" style="display:flex;align-items:center;gap:1rem;background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.1);border-radius:10px;padding:.8rem 1rem;">
        <span style="color:var(--accent);font-weight:800;font-size:1.1rem;">1</span>
        <span style="flex:1;font-size:.95rem;">Where are you from?</span>
        <button class="audio-btn-sm" onclick="speakText('Where are you from?',this)"><svg viewBox="0 0 24 24"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/></svg> Listen</button>
      </div>
      <div class="survival-item-ic" style="display:flex;align-items:center;gap:1rem;background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.1);border-radius:10px;padding:.8rem 1rem;">
        <span style="color:var(--accent);font-weight:800;font-size:1.1rem;">2</span>
        <span style="flex:1;font-size:.95rem;">I am from Sao Paulo, Brazil.</span>
        <button class="audio-btn-sm" onclick="speakText('I am from Sao Paulo, Brazil.',this)"><svg viewBox="0 0 24 24"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/></svg> Listen</button>
      </div>
      <div class="survival-item-ic" style="display:flex;align-items:center;gap:1rem;background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.1);border-radius:10px;padding:.8rem 1rem;">
        <span style="color:var(--accent);font-weight:800;font-size:1.1rem;">3</span>
        <span style="flex:1;font-size:.95rem;">I am Brazilian. I speak Portuguese.</span>
        <button class="audio-btn-sm" onclick="speakText('I am Brazilian. I speak Portuguese.',this)"><svg viewBox="0 0 24 24"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/></svg> Listen</button>
      </div>
      <div class="survival-item-ic" style="display:flex;align-items:center;gap:1rem;background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.1);border-radius:10px;padding:.8rem 1rem;">
        <span style="color:var(--accent);font-weight:800;font-size:1.1rem;">4</span>
        <span style="flex:1;font-size:.95rem;">What is your nationality?</span>
        <button class="audio-btn-sm" onclick="speakText('What is your nationality?',this)"><svg viewBox="0 0 24 24"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/></svg> Listen</button>
      </div>
      <div class="survival-item-ic" style="display:flex;align-items:center;gap:1rem;background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.1);border-radius:10px;padding:.8rem 1rem;">
        <span style="color:var(--accent);font-weight:800;font-size:1.1rem;">5</span>
        <span style="flex:1;font-size:.95rem;">I speak Portuguese and I am learning English.</span>
        <button class="audio-btn-sm" onclick="speakText('I speak Portuguese and I am learning English.',this)"><svg viewBox="0 0 24 24"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/></svg> Listen</button>
      </div>
    </div>
  </div>
</div>

<!-- SLIDE 202: L7 CHECKLIST -->
<div class="slide slide-dark" data-slide="202" data-phase="7" data-lesson="7" data-teacher="<strong>What I Learned (2 min):</strong> Gabriela leia cada item em voz alta. Se disser 'sim, eu sei fazer isso' para TODAS &mdash; a li&ccedil;&atilde;o est&aacute; dominada. Marque os checks juntos. 5/5 = aula conclu&iacute;da no sistema.">
  <div class="slide-inner">
    <h2 class="slide-heading" style="color:#fff">What I <span class="accent">Learned</span></h2>
    <ul class="checklist" id="checklist-7" style="list-style:none;display:flex;flex-direction:column;gap:.6rem;margin-top:1.5rem;">
      <li style="display:flex;align-items:center;gap:.8rem;background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.1);border-radius:8px;padding:.7rem 1rem;cursor:pointer;" onclick="this.querySelector('input').click()">
        <input type="checkbox" onchange="toggleChecklist(this)" style="width:20px;height:20px;accent-color:var(--accent);">
        <span style="font-size:.9rem;">I can ask &ldquo;Where are you from?&rdquo; and answer about myself.</span>
      </li>
      <li style="display:flex;align-items:center;gap:.8rem;background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.1);border-radius:8px;padding:.7rem 1rem;cursor:pointer;" onclick="this.querySelector('input').click()">
        <input type="checkbox" onchange="toggleChecklist(this)" style="width:20px;height:20px;accent-color:var(--accent);">
        <span style="font-size:.9rem;">I can say my nationality and where I am from (I am Brazilian / I am from Brazil).</span>
      </li>
      <li style="display:flex;align-items:center;gap:.8rem;background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.1);border-radius:8px;padding:.7rem 1rem;cursor:pointer;" onclick="this.querySelector('input').click()">
        <input type="checkbox" onchange="toggleChecklist(this)" style="width:20px;height:20px;accent-color:var(--accent);">
        <span style="font-size:.9rem;">I can talk about what languages I speak.</span>
      </li>
      <li style="display:flex;align-items:center;gap:.8rem;background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.1);border-radius:8px;padding:.7rem 1rem;cursor:pointer;" onclick="this.querySelector('input').click()">
        <input type="checkbox" onchange="toggleChecklist(this)" style="width:20px;height:20px;accent-color:var(--accent);">
        <span style="font-size:.9rem;">I know the vocabulary: country, nationality, Brazilian, French, American, language, passport, international.</span>
      </li>
      <li style="display:flex;align-items:center;gap:.8rem;background:rgba(255,255,255,.06);border:1px solid rgba(255,255,255,.1);border-radius:8px;padding:.7rem 1rem;cursor:pointer;" onclick="this.querySelector('input').click()">
        <input type="checkbox" onchange="toggleChecklist(this)" style="width:20px;height:20px;accent-color:var(--accent);">
        <span style="font-size:.9rem;">I can introduce myself to travelers at the hostel in Paris.</span>
      </li>
    </ul>
  </div>
</div>

<!-- SLIDE 203: L7 BADGE -->
<div class="slide slide-dark" data-slide="203" data-phase="7" data-lesson="7" data-teacher="<strong>Badge (1 min):</strong> 'You earned your World Traveler Stamp!' Confetti. Energia alta. Preview: pr&oacute;xima aula sobre descri&ccedil;&atilde;o de pessoas e lugares. Diga o homework ORALMENTE: 1) Criar Travel Profile Cards para 3 celebridades (como o de Gabriela). 2) Assistir 10 min de Friends ou Gossip Girl e anotar 3 vezes que algu&eacute;m menciona nacionalidade ou pa&iacute;s. 3) Praticar se apresentar no espelho em 30 segundos.">
  <div class="slide-inner">
    <div class="badge-card">
      <div class="badge-icon">
        <div class="sparkles"><div class="sparkle"></div><div class="sparkle"></div><div class="sparkle"></div><div class="sparkle"></div><div class="sparkle"></div><div class="sparkle"></div></div>
        <div class="badge-circle"><svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M2 12h20M12 2a15.3 15.3 0 014 10 15.3 15.3 0 01-4 10 15.3 15.3 0 01-4-10 15.3 15.3 0 014-10z"/></svg></div>
      </div>
      <h2 class="slide-heading">World Traveler <span class="accent">Stamp</span>!</h2>
      <p style="color:rgba(255,255,255,.7);font-size:1rem">Day 7: Countries, Nationalities &amp; the World &mdash; Complete</p>
    </div>
  </div>
</div>

<!-- SLIDE 204: L7 CLOSING -->
<div class="slide slide-dark" data-slide="204" data-phase="7" data-lesson="7" data-teacher="<strong>Fechamento (1 min):</strong> 'Pr&oacute;xima aula: descrevendo pessoas e lugares! See you!' Diga o homework ORALMENTE.">
  <div class="slide-inner" style="text-align:center">
    <div class="chapter-label">Coming Up Next</div>
    <h2 class="slide-heading">Lesson 8: <span class="accent">What Does It Look Like?</span></h2>
    <p style="color:rgba(255,255,255,.6);font-size:1rem;margin-top:1rem">Describing people, places, and things around you</p>
    <p style="color:rgba(255,255,255,.4);font-size:.85rem;margin-top:2rem">Day 7 &mdash; Complete</p>
  </div>
</div>
'''

# ============================================================
# COMPLEMENTARY CONTENT FOR AULA 7
# ============================================================
COMPLEMENTARY_HTML = '''
<h3 style="font-family:'Cormorant Garamond',serif;font-size:1.3rem;font-weight:600;color:var(--accent);margin:2rem 0 1rem;">Aula 7 &mdash; Countries, Nationalities &amp; the World</h3>
<div class="media-grid" style="margin-bottom:2rem;">
  <div class="media-card-wrapper" data-media="l7-series">
    <label class="media-check"><input type="checkbox" onchange="toggleMediaDone(this)"></label>
    <div class="media-card">
      <div class="media-thumb series"></div>
      <div class="media-info">
        <div class="media-type">S&eacute;rie</div>
        <h5>Gossip Girl &mdash; S01E01 (HBO Max)</h5>
        <p>Serena volta de viagem e todos perguntam de onde ela veio. Preste aten&ccedil;&atilde;o em como os personagens se apresentam e falam sobre lugares.</p>
        <div class="media-tip">Foco: anote toda vez que algu&eacute;m diz de onde &eacute; ou menciona um pa&iacute;s/cidade.</div>
      </div>
    </div>
  </div>
  <div class="media-card-wrapper" data-media="l7-youtube">
    <label class="media-check"><input type="checkbox" onchange="toggleMediaDone(this)"></label>
    <div class="media-card">
      <div class="media-thumb youtube"></div>
      <div class="media-info">
        <div class="media-type">YouTube</div>
        <h5>Countries and Nationalities in English &mdash; English with Lucy</h5>
        <p>V&iacute;deo did&aacute;tico sobre como dizer pa&iacute;ses e nacionalidades corretamente. Pron&uacute;ncia clara e exemplos visuais.</p>
        <div class="media-tip">Assista 1x e anote 5 nacionalidades novas que voc&ecirc; n&atilde;o conhecia em ingl&ecirc;s.</div>
      </div>
    </div>
  </div>
  <div class="media-card-wrapper" data-media="l7-podcast">
    <label class="media-check"><input type="checkbox" onchange="toggleMediaDone(this)"></label>
    <div class="media-card">
      <div class="media-thumb podcast"></div>
      <div class="media-info">
        <div class="media-type">Atividade</div>
        <h5>Travel Profile Cards &mdash; 3 celebridades</h5>
        <p>Crie Travel Profile Cards (como o da Gabriela) para 3 celebridades: escreva nome, pa&iacute;s, nacionalidade, idiomas.</p>
        <div class="media-tip">Use o formato: Name / From / Nationality / Languages. Traga para a pr&oacute;xima aula!</div>
      </div>
    </div>
  </div>
</div>'''

# ============================================================
# IN CLASS MENU CARD
# ============================================================
INCLASS_MENU_CARD = '''
<div class="inclass-lesson-card" onclick="startLesson(7)">
  <div class="ilc-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M2 12h20M12 2a15.3 15.3 0 014 10 15.3 15.3 0 01-4 10 15.3 15.3 0 01-4-10 15.3 15.3 0 014-10z"/></svg></div>
  <div class="ilc-info">
    <div class="ilc-number">Lesson 07</div>
    <div class="ilc-title">Where Are You From?</div>
    <div class="ilc-desc">Countries, nationalities &amp; languages &mdash; hostel life &mdash; 60 min &mdash; 29 slides</div>
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
    else:
        # Try the aula 6 first entry as marker
        marker2 = '"O\'clock"'
        if marker2 in html:
            html = html.replace(marker2, audio_entries + ',\n  ' + marker2)
        else:
            # Try finding audioMap opening
            am_match = re.search(r'const audioMap\s*=\s*\{', html)
            if am_match:
                insert_pos = am_match.end()
                html = html[:insert_pos] + '\n' + audio_entries + ',\n' + html[insert_pos:]
                print(f"  [OK] Inserted audioMap entries after opening brace")

    # 2. Replace Aula 7 placeholder in Pre-class
    # Try regex approach for the placeholder
    pattern = r'<div class="lesson-card">\s*<div class="lesson-header"[^>]*onclick="toggleLesson\(this\)">\s*<div class="lesson-header-img"[^>]*opacity:0\.35[^>]*></div>\s*<div class="lesson-header-content">\s*<div class="lesson-number">Aula 07[^<]*</div>'
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
                    print(f"  [OK] Replaced Aula 7 placeholder via regex")
                    found_end = True
                    break
            i += 1
        if not found_end:
            print("  [WARN] Could not find end of Aula 7 placeholder")
    else:
        # Try alternate patterns
        alt_patterns = [
            r'Aula 07[^<]*Pre-class.*?Where Are You From\?.*?opacity:0\.35',
            r'Aula 07.*?Countries,\s*Nationalities.*?opacity:0\.35',
            r'Aula 07.*?Conte[uú]do ser[aá] adicionado'
        ]
        found = False
        for alt_pat in alt_patterns:
            alt_match = re.search(alt_pat, html, re.DOTALL)
            if alt_match:
                # Find the lesson-card div start before this match
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
                                print(f"  [OK] Replaced Aula 7 placeholder via alt pattern")
                                found = True
                                break
                        i += 1
                if found:
                    break
        if not found:
            print("  [WARN] Could not find Aula 7 placeholder - may need manual insertion")

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
        old_ranges = "var lessonRanges = {1:[1,28], 2:[29,55], 3:[56,85], 4:[86,115], 5:[116,146], 6:[147,175]};"
        new_ranges = "var lessonRanges = {1:[1,28], 2:[29,55], 3:[56,85], 4:[86,115], 5:[116,146], 6:[147,175], 7:[176,204]};"
        if old_ranges in html:
            html = html.replace(old_ranges, new_ranges)
            print(f"  [OK] Updated lessonRanges")
        else:
            print("  [WARN] Could not find lessonRanges to update")

    # 5. Update totalSlides
    if not is_aluno:
        if 'var totalSlides = 175;' in html:
            html = html.replace('var totalSlides = 175;', 'var totalSlides = 204;')
            print(f"  [OK] Updated totalSlides to 204")
        else:
            print("  [WARN] Could not find totalSlides = 175 to update")

    # 6. Add IN CLASS menu card (after startLesson(6) card)
    if not is_aluno:
        menu_marker = 'onclick="startLesson(6)"'
        if menu_marker in html:
            # Find the end of the lesson 6 card div
            idx = html.index(menu_marker)
            # Find closing </div> of that card (3 levels deep typically)
            search_from = idx
            # Find the parent inclass-lesson-card div
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
                            print(f"  [OK] Added IN CLASS menu card after Lesson 6")
                            break
                    i += 1
            else:
                print("  [WARN] Could not find Lesson 6 menu card container")
        else:
            # Try alternate: insert before the placeholder div at bottom of inclass tab
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
        # Try after aula 6 complementary
        comp_marker2 = 'Aula 6'
        # Find last occurrence of aula 6 in complementary section
        comp_marker3 = 'data-media="l6-podcast"'
        if comp_marker3 in html:
            idx = html.index(comp_marker3)
            # Find the end of the media-grid div after this
            grid_end = html.find('</div>', idx)
            # Find the closing of media-grid (go up a few levels)
            search_pos = idx
            for _ in range(5):
                search_pos = html.find('</div>', search_pos + 6)
            if search_pos > 0:
                html = html[:search_pos + 6] + '\n' + COMPLEMENTARY_HTML + html[search_pos + 6:]
                print(f"  [OK] Added Complementary content (after l6)")

    # 8. Update totalLessons for progress
    html = html.replace("var totalLessons = 6;", "var totalLessons = 7;", 1)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"  [DONE] Saved {filepath}")

if __name__ == '__main__':
    print("=== Building Gabriela Pires - Aula 7 ===")

    print("\n[1/2] Patching PROFESSOR file...")
    patch_file(PROF, is_aluno=False)

    print("\n[2/2] Patching ALUNO file...")
    patch_file(ALUNO, is_aluno=True)

    print("\n=== Build complete ===")
