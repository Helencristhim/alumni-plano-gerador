# -*- coding: utf-8 -*-
import random
random.seed(707)

vocab = [
    ("Affordable", "cheap enough for most people to buy or pay for", "This apartment is more affordable than the other one."),
    ("Peaceful", "calm and quiet, without noise or trouble", "The countryside is more peaceful than the city center."),
    ("Modern", "new and using the latest style or ideas", "Her kitchen is more modern than mine."),
    ("Reasonable", "fair and sensible, especially about a price", "The rent here is very reasonable for the area."),
    ("Efficient", "working well without wasting time or energy", "The subway is a more efficient way to travel than the bus."),
    ("Similar", "almost the same as something else", "The two neighborhoods are quite similar."),
    ("Comfortable", "giving a pleasant and relaxed feeling", "This sofa is more comfortable than that old chair."),
    ("Option", "one of the things you can choose", "Renting is a good option for a small family."),
    ("Advantage", "a good point that helps you or makes something better", "One advantage of this area is the quiet at night."),
    ("Drawback", "a disadvantage or a small problem with something", "The main drawback is the long trip to work."),
    ("To compare", "to look at two things to see how they are the same or different", "Let us compare the two apartments before we decide."),
    ("To prefer", "to like one thing more than another", "I prefer the quieter neighborhood."),
]

match_defs = {
    "Affordable": "cheap enough for most people to buy",
    "Peaceful": "calm and quiet, with no noise",
    "Modern": "new and in the latest style",
    "Reasonable": "fair and sensible, especially a price",
    "Efficient": "working well without wasting your time",
    "Similar": "almost the same as something else",
    "Comfortable": "giving a pleasant, relaxed feeling",
    "Option": "one of the things you can choose",
    "Advantage": "a good point that helps you",
    "Drawback": "a disadvantage or small problem",
    "To compare": "to look at how things are the same or different",
    "To prefer": "to like one thing more than another",
}
all_defs = [match_defs[w] for w, _, _ in vocab]

# --- Vocab cards ---
vc = []
for w, d, ex in vocab:
    vc.append(
        f'        <div class="vocab-card-pc"><div class="vocab-card-content"><div class="vocab-card-header"><span class="vocab-card-word">{w}</span><span class="vocab-card-dot"> -- </span><span class="vocab-card-def">{d}</span></div><div class="vocab-card-example">"{ex}"</div></div><button class="audio-btn" onclick="speakText(\'{w}\',this)">Listen</button></div>'
    )
vocab_cards = "\n".join(vc)

# --- Matching (shuffled; correct option never at same row index) ---
rows = []
for i, (w, _, _) in enumerate(vocab):
    ans = match_defs[w]
    opts = all_defs[:]
    while True:
        random.shuffle(opts)
        if opts.index(ans) != i:
            break
    opt_html = '<option value="">Select...</option>' + "".join(
        f'<option value="{o}">{o}</option>' for o in opts
    )
    rows.append(
        f'        <div class="match-row" data-answer="{ans}"><span class="match-word" style="flex:0 0 150px">{w}</span><select style="flex:1;width:100%" onchange="checkMatch(this)">{opt_html}</select></div>'
    )
match_rows = "\n".join(rows)

TEMPLATE = f'''<div class="lesson-card" id="ex-lesson-7">
  <div class="lesson-header" onclick="toggleLesson(this)">
    <div class="lesson-header-img" style="background-image:url('https://images.unsplash.com/photo-1560518883-ce09059eeffa?w=600&q=80')"></div>
    <div class="lesson-header-content">
      <div class="lesson-number">Lesson 07 -- Pre-class</div>
      <h3>Comparing Things</h3>
      <div class="lesson-desc">Comparing places, habits, and options. Key words: affordable, peaceful, modern, reasonable, efficient, similar, comfortable, option, advantage, drawback, to compare, to prefer. Structure: comparatives and superlatives (short adjectives with -er / -est, long adjectives with more / the most, irregular good-better-best and bad-worse-worst, and as ... as for equal things).</div>
      <div class="lesson-progress-mini"><div class="mini-bar"><div class="mini-bar-fill" data-lesson-progress="7" style="width:0%"></div></div><span class="mini-percent" data-lesson-pct="7">0%</span></div>
    </div>
    <div class="expand-icon">&#9660;</div>
  </div>
  <div class="lesson-body">

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.1: Vocabulary Cards</h4><span class="badge badge-vocab">Vocabulary</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Listen to each word and read the example. Tap Listen to hear it.</p>
      <div class="vocab-cards">
{vocab_cards}
      </div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.2: Matching</h4><span class="badge badge-practice">Practice</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Match each word with the correct definition.</p>
      <div class="match-grid" id="match-l7">
{match_rows}
      </div>
      <button class="verify-all-btn" onclick="verifyAllMatches('match-l7')">Check Answers</button>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.3: Grammar in Context</h4><span class="badge badge-vocab">GRAMMAR</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Read the text and answer the questions.</p>
      <div style="background:var(--bg-elevated);border:1px solid var(--border);border-radius:10px;padding:1.2rem;margin-bottom:1.2rem;line-height:1.7;font-size:.9rem">
        <p>Ana Paula wants to move, so she decided to <strong>compare</strong> two apartments. The first one is <strong>more affordable</strong> than the second, and the rent is very <strong>reasonable</strong>. It is also in a <strong>more peaceful</strong> neighborhood, which is a big <strong>advantage</strong> for her. The second apartment is <strong>bigger</strong> and <strong>more modern</strong>, but it is also <strong>more expensive</strong> and less <strong>comfortable</strong>. The two kitchens are quite <strong>similar</strong>, but the first building has a <strong>more efficient</strong> elevator. The main <strong>drawback</strong> of the first apartment is the long trip to the hospital. In the end, she thinks the first one is <strong>the best option</strong>, because she <strong>prefers</strong> a quiet home to a fancy one.</p>
      </div>
      <div class="quiz-item"><div class="quiz-question">1. Why do we say "more affordable" and not "affordabler"?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> Long adjectives use "more" instead of "-er".</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> "Affordable" has no comparative form.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "More" is only used with nouns.</div></div></div>
      <div class="quiz-item"><div class="quiz-question">2. In "the first one is the best option", why "the best"?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> It compares only two things.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> It is the superlative of "good", and it is the top of the group.</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "Best" is the comparative of "good".</div></div></div>
      <div class="quiz-item"><div class="quiz-question">3. Which sentence compares the two apartments correctly?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "The second apartment is more bigger than the first."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> "The second apartment is bigger than the first."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "The second apartment is the bigger than the first."</div></div></div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.4: Grammar Tip -- Comparatives and Superlatives</h4><span class="badge badge-vocab">GRAMMAR</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem">How to compare two things (comparative) and point to the top of a group (superlative).</p>
      <div style="overflow-x:auto"><table style="width:100%;border-collapse:collapse;font-size:.85rem;background:var(--bg-card);border:1px solid var(--border);border-radius:8px;overflow:hidden">
        <thead><tr style="background:var(--accent);color:#fff"><th style="padding:.7rem;text-align:left">Type</th><th style="padding:.7rem;text-align:left">Comparative (2 things)</th><th style="padding:.7rem;text-align:left">Superlative (the top)</th></tr></thead>
        <tbody>
          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">Short adjective<br>(cheap, quiet)</td><td style="padding:.6rem">adjective + <strong>-er</strong> + than<br><em>cheaper than, quieter than</em></td><td style="padding:.6rem">the + adjective + <strong>-est</strong><br><em>the cheapest, the quietest</em></td></tr>
          <tr style="border-bottom:1px solid var(--border);background:var(--bg-elevated)"><td style="padding:.6rem;font-weight:600">Long adjective<br>(modern, affordable)</td><td style="padding:.6rem"><strong>more</strong> + adjective + than<br><em>more modern than</em></td><td style="padding:.6rem"><strong>the most</strong> + adjective<br><em>the most modern</em></td></tr>
          <tr style="border-bottom:1px solid var(--border)"><td style="padding:.6rem;font-weight:600">Irregular</td><td style="padding:.6rem">good &rarr; <strong>better than</strong>; bad &rarr; <strong>worse than</strong></td><td style="padding:.6rem">good &rarr; <strong>the best</strong>; bad &rarr; <strong>the worst</strong></td></tr>
          <tr><td style="padding:.6rem;font-weight:600">Equal</td><td style="padding:.6rem" colspan="2">Use <strong>as ... as</strong> when two things are the same: "This apartment is <strong>as modern as</strong> that one."</td></tr>
        </tbody>
      </table></div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 1.5: Fill in the Blank</h4><span class="badge badge-practice">Practice</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Complete each sentence. Tap Listen to hear the whole sentence.</p>
      <div class="fill-blank-item"><div class="fill-blank-sentence">"This apartment is <input class="blank-input" data-answer="cheaper" data-hint="Hint: short adjective -- cheap + er" data-phrase="This apartment is cheaper than the other one." placeholder="___"> than the other one."</div><button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button><button class="check-btn" onclick="checkBlank(this)">Check</button></div>
      <div class="fill-blank-item"><div class="fill-blank-sentence">"The subway is <input class="blank-input" data-answer="more efficient" data-hint="Hint: long adjective -- more + efficient" data-phrase="The subway is more efficient than the bus." placeholder="___"> than the bus."</div><button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button><button class="check-btn" onclick="checkBlank(this)">Check</button></div>
      <div class="fill-blank-item"><div class="fill-blank-sentence">"For me, this is the <input class="blank-input" data-answer="most affordable" data-hint="Hint: superlative of a long adjective -- the most + affordable" data-phrase="For me, this is the most affordable option of all." placeholder="___"> option of all."</div><button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button><button class="check-btn" onclick="checkBlank(this)">Check</button></div>
      <div class="fill-blank-item"><div class="fill-blank-sentence">"The countryside is <input class="blank-input" data-answer="more peaceful" data-hint="Hint: long adjective -- more + peaceful" data-phrase="The countryside is more peaceful than the city." placeholder="___"> than the city."</div><button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button><button class="check-btn" onclick="checkBlank(this)">Check</button></div>
      <div class="fill-blank-item"><div class="fill-blank-sentence">"Her apartment is the <input class="blank-input" data-answer="best" data-hint="Hint: irregular superlative of good" data-phrase="Her apartment is the best in the building." placeholder="___"> in the building."</div><button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button><button class="check-btn" onclick="checkBlank(this)">Check</button></div>
      <div class="fill-blank-item"><div class="fill-blank-sentence">"This sofa is <input class="blank-input" data-answer="as comfortable as" data-hint="Hint: equal -- as + comfortable + as" data-phrase="This sofa is as comfortable as the old one." placeholder="___"> the old one."</div><button class="listen-blank-btn" onclick="listenBlank(this)">Listen</button><button class="check-btn" onclick="checkBlank(this)">Check</button></div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 2: Put the Comparison in Order</h4><span class="badge badge-order">Order</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Put the steps of comparing two options in the correct order. Tap Listen to hear the full description.</p>
      <button class="btn btn-listen" onclick="speakText('[order-l7]', this)" style="margin-bottom:1rem;display:inline-flex;align-items:center;gap:.4rem;padding:.55rem 1.2rem;background:var(--accent);color:#fff;border:none;border-radius:8px;font-size:.85rem;font-weight:600;cursor:pointer"><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M15.54 8.46a5 5 0 0 1 0 7.07"/><path d="M19.07 4.93a10 10 0 0 1 0 14.14"/></svg> Listen</button>
      <div class="order-container" id="order-l7">
        <div class="order-item" draggable="true" data-order="3" onclick="selectOrderItem(this,'order-l7')"><span class="order-num">?</span><span class="order-text">Compare another feature, like the size or the location.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l7')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l7')">&#9660;</button></span></div>
        <div class="order-item" draggable="true" data-order="5" onclick="selectOrderItem(this,'order-l7')"><span class="order-num">?</span><span class="order-text">Say which one you prefer and give your final choice.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l7')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l7')">&#9660;</button></span></div>
        <div class="order-item" draggable="true" data-order="1" onclick="selectOrderItem(this,'order-l7')"><span class="order-num">?</span><span class="order-text">Name the two options you want to compare.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l7')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l7')">&#9660;</button></span></div>
        <div class="order-item" draggable="true" data-order="4" onclick="selectOrderItem(this,'order-l7')"><span class="order-num">?</span><span class="order-text">Say which option is the best and explain why.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l7')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l7')">&#9660;</button></span></div>
        <div class="order-item" draggable="true" data-order="2" onclick="selectOrderItem(this,'order-l7')"><span class="order-num">?</span><span class="order-text">Compare their price with a comparative like cheaper or more expensive.</span><span class="order-arrows"><button class="arrow-btn" onclick="moveItem(this,-1,'order-l7')">&#9650;</button><button class="arrow-btn" onclick="moveItem(this,1,'order-l7')">&#9660;</button></span></div>
      </div>
      <button class="verify-all-btn" onclick="checkOrder('order-l7')">Check Order</button>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 3: Pronunciation</h4><span class="badge badge-speak">Speaking</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Listen to each sentence, then record yourself saying it.</p>
      <div class="speech-card" data-phrase="This apartment is cheaper than the other one.">
        <div class="speech-phrase">This apartment is cheaper than the other one.</div>
        <div class="speech-controls"><button class="btn btn-listen" onclick="speakPhrase(this)">&#9654; Listen</button><button class="btn btn-record" onclick="startRecording(this)">&#9679; Record</button><button class="btn btn-stop" onclick="stopRecording(this)" style="display:none">&#9632; Stop</button></div>
        <div class="speech-result"></div>
      </div>
      <div class="speech-card" data-phrase="The park is the most peaceful place in the city.">
        <div class="speech-phrase">The park is the most peaceful place in the city.</div>
        <div class="speech-controls"><button class="btn btn-listen" onclick="speakPhrase(this)">&#9654; Listen</button><button class="btn btn-record" onclick="startRecording(this)">&#9679; Record</button><button class="btn btn-stop" onclick="stopRecording(this)" style="display:none">&#9632; Stop</button></div>
        <div class="speech-result"></div>
      </div>
      <div class="speech-card" data-phrase="I prefer the more modern kitchen.">
        <div class="speech-phrase">I prefer the more modern kitchen.</div>
        <div class="speech-controls"><button class="btn btn-listen" onclick="speakPhrase(this)">&#9654; Listen</button><button class="btn btn-record" onclick="startRecording(this)">&#9679; Record</button><button class="btn btn-stop" onclick="stopRecording(this)" style="display:none">&#9632; Stop</button></div>
        <div class="speech-result"></div>
      </div>
      <div class="speech-card" data-phrase="Renting is a better option for us right now.">
        <div class="speech-phrase">Renting is a better option for us right now.</div>
        <div class="speech-controls"><button class="btn btn-listen" onclick="speakPhrase(this)">&#9654; Listen</button><button class="btn btn-record" onclick="startRecording(this)">&#9679; Record</button><button class="btn btn-stop" onclick="stopRecording(this)" style="display:none">&#9632; Stop</button></div>
        <div class="speech-result"></div>
      </div>
      <div class="speech-card" data-phrase="The two neighborhoods are quite similar.">
        <div class="speech-phrase">The two neighborhoods are quite similar.</div>
        <div class="speech-controls"><button class="btn btn-listen" onclick="speakPhrase(this)">&#9654; Listen</button><button class="btn btn-record" onclick="startRecording(this)">&#9679; Record</button><button class="btn btn-stop" onclick="stopRecording(this)" style="display:none">&#9632; Stop</button></div>
        <div class="speech-result"></div>
      </div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 4: Situational Quiz</h4><span class="badge badge-quiz">Quiz</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Choose the best answer for each real situation.</p>
      <div class="quiz-item"><div class="quiz-question">A friend asks you to compare two cafes. You say:</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "This cafe is more cheaper than that one."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> "This cafe is cheaper than that one."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "This cafe is the cheaper than that one."</div></div></div>
      <div class="quiz-item"><div class="quiz-question">You want to say one gym is number one of all. You say:</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> "This is the most modern gym in the area."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> "This is the more modern gym in the area."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "This is most modern gym in the area."</div></div></div>
      <div class="quiz-item"><div class="quiz-question">You compare working from home and going to the office. Which is correct?</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">A</span> "Working from home is gooder than the office."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">B</span> "Working from home is better than going to the office."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "Working from home is more better than the office."</div></div></div>
      <div class="quiz-item"><div class="quiz-question">You want to say two options are the same. You say:</div><div class="quiz-options"><div class="quiz-option" onclick="selectQuiz(this)" data-correct="true"><span class="option-letter">A</span> "The first plan is as reasonable as the second one."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">B</span> "The first plan is as reasonable than the second one."</div><div class="quiz-option" onclick="selectQuiz(this)" data-correct="false"><span class="option-letter">C</span> "The first plan is so reasonable as the second one."</div></div></div>
    </div>

    <div class="exercise-section">
      <div class="section-header-row"><h4>Stage 5: Free Production</h4><span class="badge badge-think">Reflection</span></div>
      <p style="font-size:.82rem;color:var(--text-dim);margin-bottom:.8rem;font-style:italic">Record yourself answering the question below. There is no right or wrong answer.</p>
      <div class="think-card">
        <div class="think-question">A friend asks you to help them choose between two neighborhoods, two apartments, or two ways to travel to work. Compare the two options: say which one is more affordable, which one has a better location, and which one you prefer and why. Use comparatives and superlatives. Take your time.</div>
        <div class="speech-controls"><button class="btn btn-record" onclick="startFreeRecording(this)">&#9679; Record</button><button class="btn btn-stop" onclick="stopFreeRecording(this)" style="display:none">&#9632; Stop</button></div>
        <div id="think-result-7"></div>
      </div>
    </div>

    <div class="survival-card">
      <h4>Survival Card -- Lesson 7</h4>
      <div class="survival-phrase"><span class="sp-num">1</span><span class="sp-en">This apartment is more affordable than the other one.</span><button class="btn btn-listen" onclick="speakText('This apartment is more affordable than the other one.',this)">&#9835;</button></div>
      <div class="survival-phrase"><span class="sp-num">2</span><span class="sp-en">The subway is more efficient than the bus.</span><button class="btn btn-listen" onclick="speakText('The subway is more efficient than the bus.',this)">&#9835;</button></div>
      <div class="survival-phrase"><span class="sp-num">3</span><span class="sp-en">I think this is the best option for us.</span><button class="btn btn-listen" onclick="speakText('I think this is the best option for us.',this)">&#9835;</button></div>
      <div class="survival-phrase"><span class="sp-num">4</span><span class="sp-en">The main drawback is the long trip to work.</span><button class="btn btn-listen" onclick="speakText('The main drawback is the long trip to work.',this)">&#9835;</button></div>
      <div class="survival-phrase"><span class="sp-num">5</span><span class="sp-en">I prefer the quieter and more peaceful neighborhood.</span><button class="btn btn-listen" onclick="speakText('I prefer the quieter and more peaceful neighborhood.',this)">&#9835;</button></div>
    </div>

  </div>
</div>
'''

open("_build/ana-paula-porto-de-oliveira-fornazari-aula7/preclass.html", "w", encoding="utf-8").write(TEMPLATE)
print("wrote preclass.html")
