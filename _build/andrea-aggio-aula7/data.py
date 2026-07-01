# -*- coding: utf-8 -*-
BG1 = "https://images.unsplash.com/photo-1521737711867-e3b97375f902?w=1400&q=80"
BG2 = "https://images.unsplash.com/photo-1600880292203-757bb62b4baf?w=1400&q=80"
BG3 = "https://images.unsplash.com/photo-1450101499163-c8848c66ca85?w=1400&q=80"

D = {
    'n': 7,
    'reading': False,
    'partner_name': 'miguel',
    'grammar_point_pt': "a linguagem de clarificacao: Would you mind + -ing, Do you mean...? e So you are saying...?",
    'chapter_tag': 'Listening',
    'title_h1': 'Listening and <span class="accent">Responding</span>',
    'title_sub': 'Understanding fast native speakers and clarifying in real time.',
    'short_title': 'Listening and Responding',
    'menu_title': 'Listening and Responding -- Native Speakers at Fairs',
    'menu_desc': 'Understanding fast native speakers and clarifying in real time',
    'bg_title': BG1, 'bg_vocab': BG2, 'bg_gram': BG3, 'bg_read': BG2,
    'bg_lesson_card': "https://images.unsplash.com/photo-1521737711867-e3b97375f902?w=600&q=80",
    'stamp_label': 'Active Listener',
    'stamp_img': "https://images.unsplash.com/photo-1531482615713-2afd69097998?w=200&q=80",
    'phases': ['Real-Time Listening', 'The Words of Clarification', 'Catch the Message',
               'The Code', 'Voices', 'Your Turn', 'Wrap-Up'],

    'warm_h2': 'From the <span class="accent">Follow-Up</span> to the Fair Floor',
    'warm_p': 'Last time you turned contacts into partners with warm follow-ups. Today we go back to the fair floor -- where people talk fast, accents vary, and you must understand in real time.',
    'warm_prompt': 'A buyer talks fast and you miss half of it. What do you say next?',
    'missions': [
        'Learn the words and phrases that keep a fast conversation under control.',
        'Master clarification language: ask to repeat, check meaning, and confirm.',
        'Handle a real fast-talking native speaker -- and never freeze.',
    ],

    'vocab_trans_h2': 'The Language of <span class="accent">Clarification</span>',
    'vocab': [
        ("To catch", "to hear and understand what someone says (captar/entender)", "Sorry, I did not catch that."),
        ("Connected speech", "the way words blend together in fast speech (fala conectada)", "Connected speech makes fast English hard to follow."),
        ("Native speaker", "a person whose first language is English (falante nativo)", "The buyer was a native speaker from Texas."),
        ("Accent", "the way people from a region pronounce words (sotaque)", "Her Australian accent was new to me."),
        ("To lose the thread", "to stop following a conversation (perder o fio)", "I lost the thread for a moment."),
        ("To follow along", "to understand while someone is speaking (acompanhar)", "I could follow along most of the time."),
        ("Filler word", "a small word like well that gives you thinking time (palavra de preenchimento)", "Filler words like well give you a second to think."),
        ("To paraphrase", "to repeat an idea in different words (parafrasear)", "Let me paraphrase what you just said."),
        ("To rephrase", "to say something in a different way (reformular)", "Could you rephrase the question?"),
        ("Background noise", "sounds that make listening harder (ruído de fundo)", "There was a lot of background noise at the booth."),
        ("The gist", "the general meaning of what someone said (a essência)", "I got the gist of the offer."),
        ("To speak up", "to talk more loudly and clearly (falar mais alto)", "Could you speak up a little, please?"),
    ],

    # ---- Grammar (IN CLASS discovery) ----
    'gram_trans_h2': 'Clarify Like a <span class="accent">Pro</span>',
    'gram_trans_sub': 'Would you mind...? &middot; Do you mean...? &middot; So you are saying...?',
    'gram_examples': [
        ("", "Would you mind repeating that?", '"<span class="accent" style="font-weight:700">Would you mind</span> repeating that?"'),
        ("", "Do you mean the group rate or the net rate?", '"<span style="color:#15803d;font-weight:700">Do you mean</span> the group rate or the net rate?"'),
        ("", "So you are saying the deadline is Friday, right?", '"<span style="color:#1d4ed8;font-weight:700">So you are saying</span> the deadline is Friday, right?"'),
    ],
    'gram_disc_q': 'Repeat, check meaning, or confirm -- what is each phrase doing?',
    'gram_table': [
        ("Would you mind + -ing?", "A polite request to repeat or slow down", "<strong>Would you mind</strong> <strong>repeating</strong> that?"),
        ("Do you mean...?", "Check which option the speaker means", "<strong>Do you mean</strong> today or tomorrow?"),
        ("So you are saying...?", "Confirm the message in your own words", "<strong>So you are saying</strong> it includes breakfast?"),
    ],
    'gram_rule_foot': "After 'Would you mind', use the -ing form (no 'to'): repeating, speaking, slowing down.",

    'lf_h2': 'Repeat, Check, or <span class="accent">Confirm?</span>',
    'lf_title': 'Repeat, check, or confirm?',
    'lf_items': [
        ["A", "", "Would you mind", " repeating that?", "soft"],
        ["B", "", "Do you mean", " the net rate or the group rate?", "soft"],
        ["C", "", "So you are saying", " the price includes breakfast?", "soft"],
        ["D", "", "Could you speak up", " a little, please?", "soft"],
    ],
    'lf_followup': "Notice: 'Would you mind + -ing' politely asks someone to repeat or slow down; 'Do you mean...?' checks which option; 'So you are saying...?' confirms the message in your own words.",

    'mistakes': [
        ("Would you mind to repeat that?", 'Would you mind <strong>repeating</strong> that?'),
        ("Please repeat more slow.", 'Would you mind <strong>speaking</strong> more slowly?'),
    ],
    'mistake_note': "After 'Would you mind', use the -ing form. To talk about speed, use the adverb 'slowly', not the adjective 'slow'.",

    # ---- Dialogue ----
    'dialogue_h2': 'The Fast <span class="accent">Buyer</span>',
    'dialogue': [
        ('miguel', 'arthur', "Hi Andrea, we run a small hotel group and we want to push our shoulder season and lock in some volume.",
         "Hi Andrea, we run a small hotel group and we want to push our shoulder season and lock in some volume."),
        ('andrea', 'ellen', "Sorry, I did not catch that last part. Would you mind repeating it?",
         "Sorry, I did not <span class=\"vocab-highlight\">catch</span> that last part. Would you mind repeating it?"),
        ('miguel', 'arthur', "Of course. We want more bookings in the quieter months. Is that clearer?",
         "Of course. We want more bookings in the quieter months. Is that clearer?"),
        ('andrea', 'ellen', "Much clearer, thank you. Your accent is new to me, so I want to follow along well.",
         "Much clearer, thank you. Your <span class=\"vocab-highlight\">accent</span> is new to me, so I want to <span class=\"vocab-highlight\">follow along</span> well."),
        ('miguel', 'arthur', "No problem. There is a lot of background noise here at the booth too.",
         "No problem. There is a lot of <span class=\"vocab-highlight\">background noise</span> here at the booth too."),
        ('andrea', 'ellen', "So you are saying you want a better rate for the low season. Do you mean for groups only?",
         "So you are saying you want a better rate for the low season. Do you mean for groups only?"),
        ('miguel', 'arthur', "Exactly. Groups of twenty or more. You got the gist perfectly.",
         "Exactly. Groups of twenty or more. You got the <span class=\"vocab-highlight\">gist</span> perfectly."),
        ('andrea', 'ellen', "Great. Let me paraphrase the plan so we are aligned, and then we can talk numbers.",
         "Great. Let me <span class=\"vocab-highlight\">paraphrase</span> the plan so we are aligned, and then we can talk numbers."),
    ],
    'comprehension': [
        ("1. What kind of business does Miguel run?", "A small hotel group."),
        ("2. What does he want more of in the quieter months?", "More bookings (higher volume)."),
        ("3. How big are the groups he mentions?", "Groups of twenty or more."),
    ],

    # ---- Listenings ----
    'listen1_h2': 'A Voicemail from <span class="accent">David</span>',
    'listen1_sub': 'He is calling from the fair floor. Sound first -- no text.',
    'listen1_qs': [
        ("1. Where is David calling from?", "The fair floor, with a lot of background noise."),
        ("2. What is the gist of his message?", "He wants to move fast on a group deal."),
        ("3. What does he ask Andrea to send?", "Her best group rate for the low season."),
    ],
    'listen2_h2': 'The Listening <span class="accent">Tips</span>',
    'listen2_sub': 'A short webinar on active listening. Sound first -- no text.',
    'listen2_qs': [
        ("1. What should you listen for first?", "The gist, not every single word."),
        ("2. What is normal to do if you lose the thread?", "Ask the person to slow down."),
        ("3. Why is asking for clarification good?", "It is a strength, not a weakness -- it shows you are engaged."),
    ],
    'listenings': [
        {'file': 'a7_listening_david.mp3', 'voice': 'arthur',
         'text': "Hi Andrea, it is David from the Lisbon office. Sorry, I am calling from the fair floor, so there is a lot of background noise. I will keep this quick. We loved your itineraries, and honestly, the gist is that we want to move fast on a group deal. I know my accent can be tricky on the phone, so if you miss anything, just call me back and I will happily rephrase. The main point: send me your best group rate for the low season, and let us set up a short call this week. Talk soon."},
        {'file': 'a7_listening_tips.mp3', 'voice': 'ellen',
         'text': "Welcome back to our language tips segment. Here is one skill that changes everything at an international fair: active listening. When a native speaker talks fast, do not panic. First, listen for the gist, not every single word. Second, if you lose the thread, it is completely normal to ask the person to slow down. A simple phrase like, would you mind repeating that, sounds professional and confident. Third, paraphrase what you heard to confirm it. When you say, so you are saying, you show that you are engaged. Remember, asking for clarification is a strength, not a weakness."},
    ],

    # ---- gapfill (IN CLASS) ----
    'gapfill_parts': [
        "At a busy fair, do not panic when a ", ["1"], " speaks fast. Try to ", ["2"],
        " and get the ", ["3"], ", not every word. If you ", ["4"],
        ", ask them to slow down or ", ["5"], " it in simpler words.",
    ],
    'gapfill_bank': ["native speaker", "follow along", "gist", "lose the thread", "rephrase"],
    'vocabnote': "Notice: 'Would you mind' is followed by the -ing form, not 'to': 'Would you mind repeating that?' To describe how someone speaks, use an adverb: speak slowly, speak clearly, speak up.",

    'bank_label_top': 'Clarify',
    'bank_label': 'Useful language for clarifying',
    'bank_items': [
        "Sorry, I did not catch that.",
        "Would you mind repeating that?",
        "Could you speak up a little, please?",
        "Do you mean today or this week?",
        "So you are saying the rate is for groups only?",
        "Let me paraphrase to make sure I understood.",
        "Could you rephrase that in simpler words?",
        "I got the gist, thank you.",
    ],

    # ---- Production ----
    'scenarios_h2': 'Clarify in <span class="accent">Real Time</span>',
    'scenario_items': [
        ["Scenario 1", "A supplier speaks very fast. Politely ask them to repeat, using 'Would you mind repeating that?'"],
        ["Scenario 2", "You are not sure which price the partner means. Check it with 'Do you mean...?'"],
        ["Scenario 3", "Confirm a deal you just heard by paraphrasing: 'So you are saying...?'"],
        ["Scenario 4", "The line is noisy and you cannot hear. Ask the person to speak up, then paraphrase to confirm."],
    ],
    'answerkey_list': [
        "Gap-fill: 1 = native speaker, 2 = follow along, 3 = gist, 4 = lose the thread, 5 = rephrase.",
        "Repeat (mind + -ing): 'Would you mind repeating the last part?'",
        "Check meaning: 'Do you mean the group rate or the net rate?'",
        "Confirm: 'So you are saying the offer is only for the low season, right?'",
    ],
    'answerkey_note': "After 'Would you mind', always use the -ing form: repeating, speaking, slowing down.",

    'roleplays': [
        {'h2': 'Ask Me to <span class="accent">Repeat</span>',
         'scenario': "A partner speaks quickly and you miss the price. Politely ask them to repeat and to slow down.",
         'keywords': ["Would you mind...?", "speak slowly", "catch"]},
        {'h2': 'Check the <span class="accent">Meaning</span>',
         'scenario': "A supplier gives you two options fast. Check which one they mean and confirm by paraphrasing.",
         'keywords': ["Do you mean...?", "So you are saying...", "gist"]},
        {'h2': 'Handle a <span class="accent">Fast Talker</span>',
         'scenario': "Have a full conversation with a fast native speaker at the fair. Miss something on purpose, ask for clarification, and paraphrase the deal to confirm you understood.",
         'keywords': []},
    ],

    'survival_h2': 'Clarify with <span class="accent">Confidence</span>',
    'survival': [
        ("Sorry, I did not catch that.", "Desculpe, não entendi essa parte."),
        ("Would you mind repeating that?", "Você se importaria de repetir?"),
        ("Could you speak more slowly, please?", "Você poderia falar mais devagar, por favor?"),
        ("Do you mean the group rate or the net rate?", "Você quer dizer a tarifa de grupo ou a tarifa líquida?"),
        ("So you are saying it is only for the low season?", "Então você está dizendo que é só para a baixa temporada?"),
    ],
    'learned': [
        "I can ask someone to repeat with 'Would you mind repeating that?'",
        "I can ask someone to speak more slowly or to speak up.",
        "I can check meaning with 'Do you mean...?'",
        "I can confirm a message with 'So you are saying...?'",
        "I know the words: catch, connected speech, native speaker, accent, follow along, gist, paraphrase, rephrase, background noise, speak up.",
    ],
    'badge_name': 'Active Listener Badge',
    'badge_p': 'You can follow fast native speakers and clarify with confidence now, Andrea.',
    'next_lesson': 'Midpoint Review -- How Far You Have Come',

    # ---- PRE-CLASS ----
    'preclass_title': 'Listening and Responding -- Understanding Native Speakers',
    'preclass_desc': "Understanding fast native speakers and clarifying in real time. Key words: to catch, connected speech, native speaker, accent, to lose the thread, to follow along, filler word, to paraphrase, to rephrase, background noise, the gist, to speak up. Structures: clarification language -- 'Would you mind + -ing?', 'Do you mean...?', and 'So you are saying...?' to check and confirm understanding.",
    'reading_h2': '',
    'context': ("At a crowded fair, Andrea meets David, a fast-talking buyer from Lisbon. His <strong>accent</strong> is new "
                "to her and the <strong>background noise</strong> is loud. For a second she starts to <strong>lose the "
                "thread</strong>. Instead of panicking, she smiles and says, '<strong>Would you mind repeating</strong> "
                "that?' David slows down. Andrea listens for the <strong>gist</strong>, not every word, so she can "
                "<strong>follow along</strong>. Then she checks the details: '<strong>Do you mean</strong> the group rate or "
                "the net rate?' Finally, she confirms in her own words: '<strong>So you are saying</strong> the offer is only "
                "for the low season?' David nods. By asking to <strong>rephrase</strong> and to <strong>paraphrase</strong>, "
                "Andrea never loses control of the conversation."),
    'context_quiz': [
        ("1. Why does Andrea say 'Would you mind repeating that?' instead of staying silent?",
         [("A", "To politely ask David to say it again so she does not lose the thread.", True),
          ("B", "Because she wants to change the subject.", False),
          ("C", "Because the deal is already finished.", False)]),
        ("2. 'So you are saying the offer is only for the low season?' is used to:",
         [("A", "make a complaint.", False),
          ("B", "confirm the message in her own words.", True),
          ("C", "end the conversation.", False)]),
        ("3. After 'Would you mind', the correct form is:",
         [("A", "the -ing form: 'Would you mind repeating that?'", True),
          ("B", "the base verb: 'Would you mind repeat that?'", False),
          ("C", "'to' + verb: 'Would you mind to repeat that?'", False)]),
    ],
    'tip_title': 'Clarifying and Checking Understanding',
    'tip_sub': "Como pedir para repetir e confirmar que você entendeu (explicação em inglês e português).",
    'tip_rows': [
        ("Would you mind + -ing?", "Pedido educado para repetir ou ir mais devagar. Politely ask to repeat or slow down.", "<strong>Would you mind repeating</strong> that?"),
        ("Do you mean...?", "Confere qual opção a pessoa quis dizer. Check which option the speaker means.", "<strong>Do you mean</strong> today or tomorrow?"),
        ("So you are saying...?", "Confirma a mensagem com suas palavras. Confirm the message in your own words.", "<strong>So you are saying</strong> it includes breakfast?"),
        ("Regra de ouro / Golden rule", "Depois de 'Would you mind', use o verbo com -ing, SEM 'to'. After 'Would you mind', use the -ing form, no 'to'.", "would you mind repeating (not <strong>to repeat</strong>)"),
    ],
    'fill': [
        ('"', "Would", "Dica: pedido super educado, 'Would you mind...?'", "Would you mind repeating that?", ' you mind repeating that?"'),
        ('"Would you mind ', "repeating", "Dica: forma -ing depois de 'mind'", "Would you mind repeating the last part?", ' the last part?"'),
        ('"', "Do", "Dica: checar qual opção, 'Do you mean...?'", "Do you mean the group rate?", ' you mean the group rate?"'),
        ('"So you ', "are", "Dica: confirmar com 'So you are saying...'", "So you are saying it is for groups only?", ' saying it is for groups only?"'),
        ('"Sorry, I did not ', "catch", "Dica: ouvir e entender", "Sorry, I did not catch that.", ' that."'),
        ('"Could you ', "speak", "Dica: falar mais alto/claro, 'speak up'", "Could you speak up a little, please?", ' up a little, please?"'),
    ],
    'order_intro': "Coloque os passos para lidar com um falante rápido na ordem correta.",
    'order': [
        "Listen for the gist, not every single word.",
        "If you lose the thread, ask them to slow down.",
        "Say 'Would you mind repeating that?' politely.",
        "Check the details with 'Do you mean...?'",
        "Paraphrase to confirm: 'So you are saying...?'",
    ],
    'speech': [
        ("Sorry, I did not catch that.", "Desculpe, não entendi."),
        ("Would you mind repeating that?", "Você se importaria de repetir?"),
        ("Could you speak more slowly, please?", "Você poderia falar mais devagar?"),
        ("Do you mean the group rate or the net rate?", "Você quer dizer a tarifa de grupo ou a líquida?"),
        ("So you are saying it is only for the low season?", "Então é só para a baixa temporada?"),
    ],
    'quiz': [
        ("A buyer speaks too fast and you miss the price. You say:",
         [("A", "Speak slow!", False),
          ("B", "Would you mind repeating that, please?", True),
          ("C", "Would you mind to repeat that?", False)]),
        ("You are not sure which rate the partner means. You ask:",
         [("A", "Do you mean the net rate or the group rate?", True),
          ("B", "You mean what?", False),
          ("C", "Repeat the rate.", False)]),
        ("You want to confirm what you heard. You say:",
         [("A", "I not understand.", False),
          ("B", "So you are saying the deal is only for the low season?", True),
          ("C", "So you saying the deal?", False)]),
        ("The line is noisy and the voice is low. You say:",
         [("A", "Could you speak up a little, please?", True),
          ("B", "Talk more loud!", False),
          ("C", "Speak up you please?", False)]),
    ],
    'think': "Imagine a native speaker is talking fast at a fair and you miss part of the price. Record a short reply: politely ask them to repeat or slow down, check which option they mean, and paraphrase to confirm you understood. Take your time.",

    'media': [
        ('series', 'Ted Lasso -- Season 1, Episode 1 (Apple TV)',
         'An American coach lands in England and must understand fast British English, slang, and strong accents in real time. Watch how he asks people to repeat, checks meaning, and never loses the thread. Connection to Lesson 7: real-time listening and clarification across accents.',
         'Tip: watch with English subtitles. Note 3 moments where a character asks for clarification or repeats to confirm.',
         'https://tv.apple.com/us/show/ted-lasso/umc.cmc.vtoh0mn0xn7t3c643xqonfzy'),
        ('podcast', 'All Ears English -- "How to Understand Fast Native Speakers"',
         'A podcast made for learners who struggle with connected speech and fast native English. The hosts explain linking, reductions, and exactly how to ask for repetition politely. Connection to Lesson 7: the clarification phrases you practiced today.',
         'Tip: listen twice. Write down 5 clarification phrases the hosts use to check understanding.',
         'https://www.allearsenglish.com/'),
        ('youtube', '"How to Ask Someone to Repeat -- Polite English" -- BBC Learning English',
         'A short, practical lesson on the exact language of clarification: Would you mind repeating that? Do you mean...? So you are saying...? Connection to Lesson 7: the phrases that keep a fast conversation under your control.',
         'Tip: pause after each example and say your own version out loud, once with each phrase.',
         'https://www.youtube.com/results?search_query=how+to+ask+someone+to+repeat+polite+english+bbc+learning'),
    ],
}
