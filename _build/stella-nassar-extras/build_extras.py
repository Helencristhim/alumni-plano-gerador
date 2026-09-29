#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Duas abas suplementares da Stella Nassar (hub imersivo, stella-nassar-anterior.html).

Pedido de 29/09/2026: depois de a Stella voltar ao material imersivo, o feedback da
professora pedia duas coisas que as aulas 3-12 nao cobrem:

  - escrita de E-MAIL e CARTA (o Writing Studio so tem ensaio e argumento);
  - SPEAKING com o vocabulario novo (os role-plays citam 1 a 5 das 15 palavras).

Decisao da Helen: nao mexer nas aulas, acrescentar abas. Este script gera os dois
snippets a partir dos dados abaixo; o insert_hub_extras.py os pendura nos DOIS hubs
imersivos. Sem JS novo: checklist salva pelo saveState() global, a resposta-modelo abre
num <details> nativo, a gravacao usa startFreeRecording() e o audio usa speakText().

Travas conferidas antes de gravar (ver memoria gerador-hub-abas-suplementares):
  - nenhum think-card novo repete os 40 primeiros caracteres de um think-card existente;
  - as abas entram DEPOIS do Writing Studio, entao o indice dos checklists existentes
    (o saveState guarda checklist por posicao) nao muda;
  - nenhuma frase de audio repete chave do audioMap.

USO: python3 _build/stella-nassar-extras/build_extras.py
"""
import html
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
RAIZ = os.path.abspath(os.path.join(AQUI, '..', '..'))


def esc(t):
    # quote=False: apostrofo literal (senao &#x27; e o data-speak nao casa com o audioMap).
    return html.escape(t, quote=False).replace('"', '&quot;')


# ------------------------------------------------------------------ dados: e-mails e cartas
MAIL = [
    (3, 'LIGHT AND SHADOW', 'E-mail · 150-200 words',
     'You are taking an online summer seminar on Baroque art. Write to the coordinator, Ms. Carter, '
     'proposing a ten-minute presentation on the pivotal moment in Caravaggio\'s The Calling of Saint '
     'Matthew, and ask for a high-resolution image of the painting.',
     ['chiaroscuro', 'raking light', 'pivotal', 'heighten', 'stark', 'unflinching', 'naturalism', 'provocative'],
     ['A subject line that says exactly what you are proposing',
      'A polite request, not a demand (Would it be possible... / I would be grateful if...)',
      'One sentence that shows why the painting matters to you'],
     """Subject: Presentation proposal: The Calling of Saint Matthew

Dear Ms. Carter,

I hope you are well. I am one of the students in the online summer seminar on Baroque art, and I would like to propose a short presentation for next week's session.

My idea is to focus on the pivotal moment in Caravaggio's The Calling of Saint Matthew: the instant the beam of raking light reaches Matthew. I want to show how the stark contrast of chiaroscuro heightens the drama, and why his unflinching naturalism was so provocative in 1600.

Would it be possible to have a ten-minute slot? I would also be grateful if you could share a high-resolution image, so that the group can see the details on screen.

Thank you for considering my proposal. I am happy to adapt it to the seminar's plan.

Best regards,
Stella Nassar"""),
    (4, 'THE PERSONAL ESSAY I', 'Letter of application · 180-220 words',
     'A summer writing workshop for teenagers asks applicants for a short letter introducing themselves. '
     'Write it. Open with a real moment, not with a list of achievements.',
     ['grapple with', 'linger', 'inchoate', 'crystallize', 'vignette', 'resonate', 'tentative', 'elusive'],
     ['A formal greeting and Yours sincerely at the end',
      'The first paragraph shows a moment; it does not declare a passion',
      'A clear sentence saying what you hope to learn'],
     """Dear Members of the Selection Committee,

I am writing to apply for a place in the Young Writers' Summer Workshop. I am fourteen years old, I live in Brazil, and English has been part of my life since I was three.

Last spring, standing in front of a painting for almost an hour, I began to grapple with a question I still cannot answer: why do some images linger for years while others vanish in a minute? My interest in writing was inchoate before that afternoon; it crystallized when I tried to describe what I had seen and failed.

I am applying because I want to learn how to turn that kind of vignette into an essay that resonates with readers. My attempts so far are tentative, but I would welcome the chance to work with writers who can show me what I am missing.

Thank you for your time and consideration.

Yours sincerely,
Stella Nassar"""),
    (5, 'WHO OWNS ART?', 'E-mail · 150-200 words',
     'Your history teacher, Mr. Brooks, is choosing the topic for next month\'s class debate. Write to him '
     'proposing the Parthenon Sculptures. Present both sides fairly, with hedges, before saying why it would work.',
     ['restitution', 'repatriation', 'provenance', 'patrimony', 'stewardship', 'contested', 'arguably', 'concede'],
     ['Both sides presented before your own view',
      'At least two hedges (arguably, it seems, purportedly...)',
      'A concrete offer at the end (a reading list, a format, a timing)'],
     """Subject: Debate topic proposal

Dear Mr. Brooks,

I would like to suggest a topic for our class debate next month: should the Parthenon Sculptures return to Athens?

I think it works well because both sides have strong arguments. Greece presents the sculptures as national patrimony and asks for repatriation, while the British Museum argues that its stewardship has made them accessible to millions. The provenance is purportedly based on a permit from 1801 that has never been found, so the legitimacy of the removal remains contested.

Arguably, the most interesting part is that both positions have become entrenched. To keep the debate fair, each team could be asked to concede one point to the other side before its conclusion.

Please let me know if you think this could work. I can prepare a short reading list.

Kind regards,
Stella"""),
    (6, 'THE WHY US SUPPLEMENT', 'Formal letter · 180-220 words',
     'You are starting to research art history programs in the United States. Write to a college admissions '
     'office asking three specific questions about the program before planning a campus visit.',
     ['curatorial', 'archival', 'seminar-based', 'mentorship', 'foster', 'interdisciplinary', 'distinctive', 'trajectory'],
     ['Yours faithfully (you do not know the name of the reader)',
      'Three questions that could only be asked about THIS program',
      'No prestigious, world-class or passion'],
     """Dear Admissions Office,

I am a ninth-grade student from Brazil, and I am beginning to research undergraduate programs in art history. I am writing to ask for information about your program before planning a campus visit.

I am particularly interested in the object-based teaching described on your website. Could you tell me whether first-year students have access to curatorial projects in the campus museum, or whether these are reserved for seniors? I would also like to know if the seminar-based courses include archival research with original documents.

Finally, I would be grateful to learn more about the mentorship program. Your website mentions that it fosters close collaboration between students and faculty, and I would like to understand how this works in practice.

Thank you very much for your help. I look forward to hearing from you.

Yours faithfully,
Stella Nassar"""),
    (7, 'FROM IMPRESSIONISM TO MODERNISM', 'Informal e-mail · 150-200 words',
     'Your friend Maya is visiting the Orsay Museum in Paris next week. Write her an informal e-mail with '
     'your three best tips. Friendly register, but still precise.',
     ['brushwork', 'dissolve', 'en plein air', 'fleeting', 'deride', 'audacious', 'precursor', 'avant-garde'],
     ['An informal greeting and sign-off (Hi / Love, Cheers...)',
      'The difficult words sound natural, not like an essay',
      'One tip Maya could not find in a guidebook'],
     """Subject: Orsay tips!!

Hi Maya,

So jealous that you are going to the Orsay Museum! Here are my tips, in order of importance.

First, go straight to the Monet rooms before the crowds arrive. Stand close to the paintings and look at the brushwork: it looks like quick, messy strokes. Then walk back a few meters and watch everything dissolve into water and fog. It is honestly magic.

Second, remember that these painters were derided at first. Critics called the canvases unfinished sketches, so it was an audacious decision to exhibit them at all. Knowing that makes the rooms feel different.

Last, find Manet's paintings. He is often seen as a precursor of everything that came after, and you can actually feel him breaking the rules.

Send me photos, and tell me which painting you would steal.

Love,
Stella"""),
    (8, 'ADMISSIONS INTERVIEW I', 'Thank-you e-mail · 120-160 words',
     'Yesterday you had an admissions interview with Mr. Hale. Write a short thank-you e-mail that mentions '
     'one specific moment of the conversation.',
     ['elaborate', 'follow-up question', 'anecdote', 'rapport', 'composure', 'candid', 'succinct', 'authenticity'],
     ['Sent the day after: short and warm, not a second interview',
      'One specific moment from the conversation, not a general thank you',
      'Formal but personal: Dear Mr. Hale / Best regards'],
     """Subject: Thank you for our conversation

Dear Mr. Hale,

Thank you very much for taking the time to interview me yesterday. I really enjoyed our conversation, especially when you asked me to elaborate on the painting I described at the beginning.

Your follow-up question about the museum guard made me think about my story in a new way, and I realized that the anecdote says more about my curiosity than I had noticed. I also appreciated how quickly you built rapport; I was nervous at first, but your questions helped me keep my composure.

To be candid, I left the room thinking of better answers to one or two questions, which I suppose is a good sign that the conversation made me think.

Thank you again for your time and advice.

Best regards,
Stella Nassar"""),
    (9, 'BRAZIL ON THE WORLD STAGE', 'Letter to the editor · 180-220 words',
     'Your school magazine published an article about the new art history elective, which goes from '
     'Impressionism to Picasso. Write a letter to the editor arguing that the course should include '
     'Brazilian modernism.',
     ['peripheral', 'provincial', 'cosmopolitan', 'vernacular', 'reclaim', 'exoticize', 'hybridity', 'emblematic'],
     ['Opens by naming the article you are answering',
      'One clear argument, supported by one example (Tarsila, Abaporu...)',
      'A short final sentence that a reader will remember'],
     """To the Editor,

I read with interest last month's article on the new art history elective, and I would like to suggest one change: the course should include Brazilian modernism.

At the moment, the syllabus moves from Impressionism to Picasso as if modern art happened only in Paris. This treats Brazil as peripheral, even provincial, when artists like Tarsila do Amaral created something genuinely new. Her training was cosmopolitan, but she reclaimed a vernacular iconography that foreign painters had often exoticized.

Including her work would also show students that hybridity is not a weakness but a strength. Abaporu became emblematic of a whole movement and inspired a manifesto that is still discussed today.

We study in Brazil. It seems strange to learn the history of art as if we were not part of it.

Sincerely,
Stella Nassar, 9th grade"""),
    (10, 'THE PERSONAL ESSAY II', 'E-mail · 120-180 words',
     'Send your revised personal essay to Mr. Brooks. In the e-mail, explain what you cut and why, and ask '
     'one precise question about the new version.',
     ['ruthless', 'excise', 'pare down', 'redundant', 'superfluous', 'extraneous', 'crisp', 'distill'],
     ['Says what is attached and the new word count',
      'Explains at least two cuts, with the reason for each',
      'Ends with ONE precise question, not please give me feedback'],
     """Subject: Revised personal essay (650 words)

Dear Mr. Brooks,

Please find attached the revised version of my personal essay. It is now 650 words, down from 812.

Following your comments, I was ruthless with the introduction: I excised the first paragraph, which was redundant, and started directly with the scene in the museum. I also pared down the middle section, where several sentences were verbose or superfluous, and I replaced two cases of circumlocution with simpler verbs.

The hardest decision was to cut the paragraph about the bus ride. I liked it, but it was extraneous to the main idea. I think the essay is crisper now, and the ending arrives sooner.

I would be grateful if you could tell me whether the final paragraph still distills the idea clearly.

Thank you,
Stella"""),
    (11, 'ART IN THE AGE OF ALGORITHMS', 'Letter to the editor · 180-220 words',
     'A newspaper\'s youth section published an article claiming that AI will soon make human artists '
     'obsolete. Write a letter to the editor with a calibrated, polite disagreement.',
     ['generative', 'obsolete', 'derivative', 'replicate', 'authorship', 'disruptive', 'ambivalent', 'aura'],
     ['States the article\'s claim fairly before disagreeing',
      'At least one rhetorical question or understatement',
      'Admits one point on the other side'],
     """Dear Editor,

In your article The End of the Artist, the writer argues that generative programs will soon make human artists obsolete. As a student who wants to study art history, I would like to offer a different view.

First, most AI images are derivative: they replicate styles learned from a dataset of human work. That does not mean they are worthless, but it raises serious questions about authorship and originality.

Second, history suggests caution. Photography was also called disruptive, and yet did it make painting obsolete? It pushed painters in new directions, and it seems at least possible that AI will do the same.

I admit that I feel ambivalent. These tools are impressive, but an image on a screen has none of the aura of an object made by a person, and I doubt audiences will stop caring about that.

Yours sincerely,
Stella Nassar"""),
    (12, 'MOCK INTERVIEW AND PORTFOLIO REVIEW', 'E-mail · 150-200 words',
     'Write to your art teacher asking whether she would write a recommendation letter for a summer art '
     'history program in the United States. Make it easy for her to say yes, or no.',
     ['portfolio', 'milestone', 'hindsight', 'cumulative', 'synthesis', 'versatility', 'culmination', 'nuance'],
     ['The request is clear in the first paragraph',
      'Everything she needs is listed: portfolio, program, deadline',
      'A sentence that makes it easy to say no'],
     """Subject: Recommendation letter request

Dear Ms. Ribeiro,

I hope you are well. I am writing to ask whether you would be willing to write a recommendation letter for my application to a summer art history program in the United States.

This year has been an important milestone for me. I have put together a small portfolio with a formal analysis, an argument essay and my personal statement, and in hindsight I can see how much your class shaped it. The progress was cumulative, and the portfolio is really a synthesis of it: the habit of looking slowly that you taught me runs through every piece.

If you agree, I will send you the portfolio, the program description and the deadline, which is November 15. I completely understand if you are too busy at this time of year.

Thank you very much for considering my request.

Best wishes,
Stella"""),
]

# ------------------------------------------------------------------ dados: speaking
# (aula, titulo, [15 palavras], [(pergunta, resposta-modelo) x6])
SPEAK = [
    (3, 'LIGHT AND SHADOW',
     ['chiaroscuro', 'tenebrism', 'raking light', 'penumbra', 'foreshortening', 'pentimento', 'altarpiece',
      'commission', 'naturalism', 'stark', 'unflinching', 'heighten', 'illuminate', 'provocative', 'pivotal'],
     [('Pick a scene from a film or series that uses light the way Caravaggio does. Describe it.',
       "The last episode of my favorite series has a kitchen scene at night that is pure chiaroscuro. One lamp illuminates the mother's face while everyone else stays in the penumbra, so the conversation feels much more intimate."),
      ("Why was Caravaggio's naturalism so provocative in his time?",
       'His naturalism was provocative because he painted saints with dirty feet and tired faces. People expected holy figures to look perfect, and his unflinching realism made the sacred look ordinary.'),
      ('What is the pivotal moment in The Calling of Saint Matthew, and how does the light heighten it?',
       'The pivotal moment is the instant Matthew realizes he is being chosen. A beam of raking light crosses the wall toward him, and that stark contrast heightens the tension of a single gesture.'),
      ('Explain the difference between chiaroscuro and tenebrism to a friend who has never heard either word.',
       'Chiaroscuro is simply the contrast between light and dark. Tenebrism is chiaroscuro pushed to an extreme, where most of the canvas is almost black and only a few figures are lit, like actors on a stage.'),
      ('If an X-ray found a pentimento under a famous painting, what would it tell us?',
       'A pentimento shows that the artist changed his mind. It turns a finished masterpiece back into a decision, and I find that exciting, because you can actually see the thinking.'),
      ('Would you rather see a painting in the church it was commissioned for, or in a museum? Why?',
       'I would rather see it where it was commissioned. In a museum an altarpiece becomes an object on a white wall, but in the chapel the real light and the architecture heighten everything the artist planned.')]),
    (4, 'THE PERSONAL ESSAY I',
     ['inchoate', 'crystallize', 'grapple with', 'reckon with', 'interrogate', 'precipitate', 'vignette',
      'in medias res', 'epiphany', 'linger', 'belie', 'coax', 'elusive', 'tentative', 'resonate'],
     [('Describe a moment when one of your interests began to crystallize.',
       'My interest in art history was inchoate for years. It only crystallized when a museum guide asked me what I saw in a painting, and I talked for ten minutes without noticing the time.'),
      ('Tell a memory in medias res, as if it were the first line of an essay.',
       'The alarm was already ringing when I realized the painting was upside down. That is how I would open, in medias res, and only then explain that I was helping at a school exhibition.'),
      ('Why do readers distrust essays built around a single epiphany?',
       'Because real change is rarely sudden. An essay built around one perfect epiphany sounds invented, while a small vignette that lingers and grows over time feels honest and resonates much more.'),
      ('Talk about a problem you are still grappling with.',
       'I am still grappling with how to balance school and everything I want to learn outside it. I have not solved it, and I think an essay that interrogates the problem is better than one that pretends it is solved.'),
      ('Describe someone whose calm appearance belied what they were really feeling.',
       'Before her recital, my best friend looked completely relaxed, but her calm smile belied how nervous she was. Afterwards she admitted that her hands had been shaking the whole time.'),
      ('What idea has been elusive for you, and how did you finally catch it?',
       'The idea of voice in writing was elusive for me. My first attempts were tentative and generic, and it took a teacher who patiently coaxed stories out of me to understand what she meant.')]),
    (5, 'WHO OWNS ART?',
     ['restitution', 'repatriation', 'provenance', 'patrimony', 'stewardship', 'custodian', 'deaccession',
      'contested', 'irrevocable', 'ostensibly', 'purportedly', 'arguably', 'concede', 'legitimacy', 'entrenched'],
     [('Summarize the Parthenon Sculptures debate in under a minute, fairly.',
       'The sculptures were removed from Athens in the early 1800s and are now in London. Greece asks for repatriation as national patrimony, while the museum sees itself as a custodian, and the legitimacy of the removal is still contested.'),
      ("Take the museum's side, then concede one point to the other side.",
       'Arguably, the museum has shown excellent stewardship, and millions of people see the sculptures for free. I have to concede, though, that good care does not answer the question of who should own them.'),
      ('Why does provenance matter when a museum acquires an object?',
       'Provenance tells you whether an object was sold, stolen or taken during a war. A museum that ignores it may buy something that another country will claim later, and the scandal can be enormous.'),
      ('Should museums ever deaccession objects? Give a hedged answer.',
       'In some cases, perhaps. If an object was clearly taken illegally, deaccessioning it seems fair, but it is not a decision to make lightly, because it is often irrevocable and sets a precedent.'),
      ('Why do positions in a debate like this become so entrenched?',
       'Both sides have repeated the same arguments for two centuries, so their positions are entrenched. Any change now feels like losing rather than compromising, and that makes a real conversation almost impossible.'),
      ('Should restitution also be discussed in Brazilian museums?',
       'I think so, although I would need to research it first. Restitution is usually discussed as a European problem, but arguably it concerns our museums too, and the provenance of some objects deserves a closer look.')]),
    (6, 'THE WHY US SUPPLEMENT',
     ['interdisciplinary', 'seminar-based', 'archival', 'curatorial', 'conservation', 'mentorship', 'rigor',
      'fascination', 'preoccupation', 'devotion', 'cultivate', 'foster', 'immerse', 'distinctive', 'trajectory'],
     [('Describe your ideal art history program in three specific features.',
       'It would be seminar-based, so that we discuss instead of just taking notes. It would offer archival research with real documents, and it would let students take on curatorial projects in a campus museum.'),
      ('What is the difference between a fascination and a preoccupation? Give an example.',
       'A fascination attracts you, but you can put it aside. A preoccupation follows you everywhere. Color started as a fascination for me and became a preoccupation when I began noticing it in every room.'),
      ('How have you cultivated your eye for art so far?',
       'I have cultivated it slowly: by drawing, by visiting museums with a notebook, and by comparing how different painters solve the same problem. Nobody taught me a method; the habit built itself.'),
      ('Why is an interdisciplinary program attractive to you, or not?',
       'It attracts me because art history touches chemistry, history and technology. Conservation, for example, is completely interdisciplinary, and I love the idea of studying a painting with both a microscope and a book.'),
      ('What kind of mentorship would help you most in the next three years?',
       "I would like a mentor who asks difficult questions instead of giving answers. The right mentorship would foster independence and help me see my own trajectory, not simply follow someone else's."),
      ('Complete this sentence in your own way: what is distinctive about me is...',
       'What is distinctive about me is that I look at art like a detective. I immerse myself in one small detail, a hand or a shadow, and I build the whole story from there.')]),
    (7, 'FROM IMPRESSIONISM TO MODERNISM',
     ['en plein air', 'brushwork', 'fleeting', 'ephemeral', 'spontaneity', 'dissolve', 'flatness', 'avant-garde',
      'rupture', 'deride', 'precursor', 'lineage', 'canon', 'audacious', 'reappraisal'],
     [('Why did the Impressionists paint en plein air?',
       'They painted en plein air because they wanted to catch fleeting effects of light that disappear in minutes. You cannot paint a sunrise from memory in a studio and keep the same spontaneity.'),
      ('Describe the brushwork of a painting you know, first up close and then from far away.',
       'Up close, the brushwork in a Monet looks almost careless, just quick strokes of color. From across the room the strokes dissolve into water and fog, and suddenly the painting makes sense.'),
      ('Critics derided the Impressionists. What was derided once and is respected now?',
       'Graphic novels were derided as entertainment for kids for decades. Now some of them are studied at universities, which is a reappraisal very similar to what happened to Impressionism.'),
      ('Was Impressionism a rupture or an evolution? Take a side.',
       'I think it was more of a rupture. Exhibiting outside the official Salon was an audacious decision, and the avant-garde defined itself precisely by breaking the rules of academic painting.'),
      ('Who would you name as a precursor of the music or art you like today?',
       'For the music I like, I would say the Beatles were a precursor of almost everything. You can trace a lineage from their studio experiments to the pop albums my friends listen to now.'),
      ('Should the canon change? And who decides what enters it?',
       'It should change, because a small group of critics and museums decided it. Works that were once rejected are now at its center, which shows that the canon was never a neutral list.')]),
    (8, 'ADMISSIONS INTERVIEW I',
     ['articulate', 'anecdote', 'rapport', 'candid', 'digress', 'elaborate', 'succinct', 'poise', 'rehearsed',
      'segue', 'composure', 'authenticity', 'follow-up question', 'self-deprecating', 'earnest'],
     [('Tell me about yourself in under 45 seconds, using one anecdote.',
       'I am fourteen, I live in Brazil, and I want to study art history. The best way to explain why is an anecdote: last year I spent a whole afternoon in front of one painting, and the guard finally asked if I was okay.'),
      ('Give a candid answer: what is one of your weaknesses?',
       'To be candid, I sometimes digress when I am excited about a topic. I have learned to give a succinct answer first and then offer to elaborate if the other person is interested.'),
      ('How can you keep your composure if you lose your train of thought?',
       'I pause, smile and say something like: let me start that again. Poise is not about never making mistakes; it is about recovering calmly, and a short pause sounds more thoughtful than a rehearsed answer.'),
      ('Why does a rehearsed answer often sound less convincing?',
       'A rehearsed answer sounds like a speech, not a conversation. Interviewers value authenticity, and it is hard to build rapport with someone who is clearly reciting a text from memory.'),
      ('Use a segue: move from a question about school to a story about art.',
       'School is where I learned discipline, which is actually a good segue to how I study paintings. I go back to the same one several times, and every visit I notice something new.'),
      ('Tell a short, self-deprecating story that still shows something good about you.',
       'On my first museum trip alone I got so absorbed that I missed the last train home and had to call my mom. It was embarrassing, but it shows how earnest my curiosity is.')]),
    (9, 'BRAZIL ON THE WORLD STAGE',
     ['vernacular', 'cosmopolitan', 'hybridity', 'emblematic', 'iconography', 'exoticize', 'reclaim',
      'peripheral', 'provincial', 'disproportionate', 'centennial', 'polemic', 'homage', 'syncretic', 'manifesto'],
     [('Explain Abaporu to an American classmate who has never seen it.',
       'It is a painting of a strange figure with a tiny head and a disproportionate foot, sitting next to a cactus under a sun. It became emblematic of Brazilian modernism and even inspired a manifesto.'),
      ('Was Tarsila imitating European art, or doing something new?',
       'Her training was cosmopolitan, but her subject was Brazil. Critics now speak of hybridity rather than imitation: she used Cubist structure to paint vernacular colors and a Brazilian iconography.'),
      ('What does it mean to exoticize a culture? Give an example from films or ads.',
       'It means presenting a culture as colorful and strange for outsiders. Many foreign films exoticize Brazil with beaches, carnival and danger, as if nothing ordinary ever happened here.'),
      ('Is Brazil still treated as peripheral in the story of modern art?',
       'Less than before, but yes. Big museums are only now rehanging their collections to include artists like Tarsila, which suggests that the idea of Brazil as peripheral, or provincial, is slowly changing.'),
      ('What would a manifesto for artists of your generation say?',
       'It would say that we refuse to choose between local and global. Our culture is syncretic by nature, and we want to reclaim our own images instead of letting others define them.'),
      ('How would you pay homage to an artist you admire?',
       "I would pay homage by borrowing one element, like Tarsila's palette, and using it to paint something from my own life. A good homage is a conversation with the artist, not a copy.")]),
    (10, 'THE PERSONAL ESSAY II',
     ['redundant', 'verbose', 'pare down', 'tighten', 'excise', 'superfluous', 'economy', 'circumlocution',
      'crisp', 'streamline', 'distill', 'extraneous', 'padding', 'cumbersome', 'ruthless'],
     [('Describe your writing habits: are you more verbose or more concise?',
       'I am naturally verbose. My first drafts are full of padding, so I have learned to be ruthless in the second draft and excise anything that does not move the idea forward.'),
      ('Give an example of circumlocution, and then say it simply.',
       'Due to the fact that it was raining is circumlocution. Because it rained says the same thing in three words, and it sounds much crisper.'),
      ('What is the hardest thing for you to cut from an essay, and why?',
       'The hardest thing to cut is a sentence I love that is extraneous. It feels like losing part of myself, but the paragraph almost always becomes stronger without it.'),
      ('Is economy of language the same as brevity?',
       'No. Brevity is only about length, but economy means that every word is necessary. A long paragraph can have perfect economy, and a short one can still be full of superfluous words.'),
      ('Distill your personal essay into a single sentence.',
       'If I distill my essay, it says that I learned to look at art slowly, and that looking slowly changed the way I see everything else.'),
      ('Advise a friend whose essay is two hundred words too long.',
       'First, pare down the introduction, because it is usually redundant. Then streamline the middle and cut every adjective that repeats an idea. Only remove whole paragraphs after the sentences are already tight.')]),
    (11, 'ART IN THE AGE OF ALGORITHMS',
     ['authorship', 'generative', 'derivative', 'originality', 'commodify', 'spectacle', 'iconoclastic',
      'autonomy', 'dataset', 'replicate', 'obsolete', 'aura', 'connoisseurship', 'disruptive', 'ambivalent'],
     [('Can an image made by a generative program be called art?',
       'I feel ambivalent. The image can be beautiful, but authorship is unclear, because the program learned from a dataset of human work. I would call it a tool that produces art, not an artist.'),
      ('Is AI-generated art derivative?',
       'Often, yes. It replicates the styles it was trained on, so the result can be derivative. But originality has never meant creating from nothing, so the real question is how the person using it transforms the material.'),
      ('Will AI make human artists obsolete?',
       'I doubt it. Photography did not make painting obsolete; it freed painting to do other things. AI is disruptive, but it may push artists toward work that a machine cannot replicate.'),
      ('What do people mean by the aura of an original work of art?',
       'The aura is the presence you feel in front of the real object: its size, its surface, its history. A reproduction on a phone may be perfect, but it loses that aura completely.'),
      ('Was shredding a painting at an auction a work of art, or just a spectacle?',
       'It was both. The stunt was iconoclastic and mocked the market, but the market immediately commodified it, and the shredded painting became more valuable. That irony is the real artwork.'),
      ('Would you trust a machine with connoisseurship, deciding whether a painting is authentic?',
       'As one tool among others, yes. Connoisseurship once relied only on the trained eye, and a machine can see patterns we miss, but the final decision should stay with people who can take responsibility for it.')]),
    (12, 'MOCK INTERVIEW AND PORTFOLIO REVIEW',
     ['portfolio', 'retrospective', 'synthesis', 'culmination', 'benchmark', 'milestone', 'cumulative',
      'consolidate', 'nuance', 'versatility', 'calibrate', 'rehang', 'narrative arc', 'hindsight', 'unflagging'],
     [('Looking back at this program, what was your biggest milestone?',
       'My biggest milestone was finishing the personal essay. In hindsight, it was the moment when all the separate skills, reading, writing and speaking, came together in a single piece.'),
      ('Describe your portfolio as if you were presenting it to an interviewer.',
       'My portfolio includes a formal analysis, an argument about the Parthenon Sculptures, two supplements and my personal essay. Together they show versatility, from academic writing to a much more personal voice.'),
      ('What does it mean to say that learning is cumulative?',
       'It means that each lesson adds to the one before. Nothing was dramatic on its own, but the effect is cumulative, and today I can calibrate my claims in a way I simply could not at the start.'),
      ('Which nuance of English do you notice now that you did not notice before?',
       'I notice the difference between hedging and being vague. I used to think careful language sounded weak, and now I see the nuance: a calibrated claim is actually stronger.'),
      ('What would you like to consolidate in the next few months?',
       'I want to consolidate my reading of dense texts, because reading was my benchmark on the Cambridge exam. I also want to keep writing short pieces, so that my voice stays natural.'),
      ('Tell the narrative arc of your year so far in four sentences.',
       'At the start, my interest in art was intense but unfocused. Then I began to read and write about it seriously. The turning point was the essay. Now I know exactly what I want to study.')]),
]

# ------------------------------------------------------------------ html
CARD = 'background:var(--bg-card);border:1px solid var(--border);border-radius:10px;padding:1rem 1.2rem;margin-bottom:1rem'
LABEL = 'font-size:.72rem;font-weight:700;letter-spacing:.06em;color:var(--accent)'
CHIP = ('display:inline-block;background:var(--bg-elevated);border:1px solid var(--accent);border-radius:999px;'
        'padding:.15rem .6rem;font-size:.78rem;margin:.15rem .2rem .15rem 0;color:var(--accent)')
CHECK_LI = ('<li style="list-style:none"><label style="display:flex;align-items:flex-start;gap:.5rem;font-size:.82rem;'
            'margin:.3rem 0;cursor:pointer"><input type="checkbox" onchange="this.closest(\'li\').classList.toggle'
            '(\'checked\',this.checked);saveState()" style="margin-top:.2rem"><span>%s</span></label></li>')
SUMMARY = ('font-size:.82rem;font-weight:600;color:var(--accent);cursor:pointer;padding:.4rem 0')


def checklist(itens):
    return ('<ul class="checklist" style="padding:0;margin:.4rem 0 0">'
            + ''.join(CHECK_LI % esc(i) for i in itens) + '</ul>')


def chips(ws):
    return '<div style="margin:.4rem 0 .2rem">' + ''.join('<span style="%s">%s</span>' % (CHIP, esc(w)) for w in ws) + '</div>'


def mail_html():
    out = ['<!-- ========== TAB: E-MAILS & LETTERS (aditivo, 29/09/2026) ========== -->',
           '<div class="tab-content" id="tab-mail">',
           '<h3 style="font-family:\'Cormorant Garamond\',serif;font-size:1.2rem;margin-bottom:1rem">E-mails &amp; Letters</h3>',
           '<p style="font-size:.85rem;color:var(--text-dim);margin-bottom:1rem">The writing you will actually send. '
           'One e-mail or letter per lesson, from Lesson 3 on, using the words of that lesson. Write it in your '
           'Writing Studio Google Doc under a heading with the lesson number, tick the checklist before you share '
           'it, and open the model only after you have written your own version.</p>',
           '<div style="%s;border-left:4px solid var(--accent)">' % CARD,
           '  <div style="font-weight:600;font-size:.9rem;margin-bottom:.5rem">E-mail or letter? Four things change</div>',
           '  <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:.7rem;font-size:.82rem">',
           '    <div><strong style="color:var(--accent)">Subject line</strong><br>An e-mail needs one that says what it is about. A letter has none.</div>',
           '    <div><strong style="color:var(--accent)">Register</strong><br>Dear Mr. Hale / Best regards is formal. Hi Maya / Love is friendly. Never mix them.</div>',
           '    <div><strong style="color:var(--accent)">Sign-off</strong><br>Yours sincerely when you know the name; Yours faithfully when you do not.</div>',
           '    <div><strong style="color:var(--accent)">Length</strong><br>Say it once. A reader should never have to scroll to find the request.</div>',
           '  </div>',
           '</div>']
    for n, titulo, genero, tarefa, palavras, itens, modelo in MAIL:
        corpo = ''.join('<p style="margin:0 0 .6rem">%s</p>' % esc(p).replace('\n', '<br>')
                        for p in modelo.split('\n\n'))
        out += ['<div class="ws-brief" style="%s">' % CARD,
                '  <div style="display:flex;justify-content:space-between;align-items:baseline;gap:.8rem;flex-wrap:wrap">',
                '    <div style="%s">LESSON %02d &middot; %s</div>' % (LABEL, n, esc(titulo)),
                '    <div style="font-size:.75rem;color:var(--text-dim)">%s</div>' % esc(genero).replace(' · ', ' &middot; '),
                '  </div>',
                '  <p style="font-size:.88rem;line-height:1.6;margin:.6rem 0 .3rem">%s</p>' % esc(tarefa),
                '  <div style="font-size:.75rem;color:var(--text-dim);margin-top:.4rem">Use at least five of these words:</div>',
                '  ' + chips(palavras),
                '  ' + checklist(itens + ['At least five of the words above, each one used correctly']),
                '  <details style="margin-top:.6rem;border-top:1px solid var(--border);padding-top:.4rem">',
                '    <summary style="%s">See a model, after you write yours</summary>' % SUMMARY,
                '    <div style="font-size:.84rem;line-height:1.6;background:var(--bg-elevated);border-radius:8px;padding:.8rem 1rem;margin-top:.4rem">%s</div>' % corpo,
                '  </details>',
                '</div>']
    out.append('</div><!-- /tab-mail -->')
    return '\n'.join(out) + '\n'


def speak_html():
    out = ['<!-- ========== TAB: SPEAK WITH THE WORDS (aditivo, 29/09/2026) ========== -->',
           '<div class="tab-content" id="tab-speakw">',
           '<h3 style="font-family:\'Cormorant Garamond\',serif;font-size:1.2rem;margin-bottom:1rem">Speak with the Words</h3>',
           '<p style="font-size:.85rem;color:var(--text-dim);margin-bottom:1rem">Six questions per lesson that you can '
           'only answer well with that lesson\'s words. Answer out loud and record yourself, then open the model and '
           'listen. Across the six answers, try to use at least five of the fifteen words, naturally, the way you '
           'would in a real conversation. Your teacher can also use these in class.</p>']
    for n, titulo, palavras, perguntas in SPEAK:
        out += ['<div style="%s">' % CARD,
                '  <div style="%s">LESSON %02d &middot; %s</div>' % (LABEL, n, esc(titulo)),
                '  ' + chips(palavras)]
        for i, (q, m) in enumerate(perguntas, 1):
            out += ['  <div class="think-card" style="margin:.7rem 0 0">',
                    '    <div class="think-question">%d. %s</div>' % (i, esc(q)),
                    '    <div class="speech-controls">',
                    '      <button class="btn btn-record" onclick="startFreeRecording(this)">&#9679; Record</button>',
                    '      <button class="btn btn-stop" onclick="stopFreeRecording(this)">&#9632; Stop</button>',
                    '    </div>',
                    '    <div id="think-result-sw%d-%d"></div>' % (n, i),
                    '    <details style="margin-top:.4rem">',
                    '      <summary style="%s">Model answer</summary>' % SUMMARY,
                    '      <div style="display:flex;gap:.6rem;align-items:flex-start;font-size:.84rem;line-height:1.6;background:var(--bg-elevated);border-radius:8px;padding:.7rem .9rem;margin-top:.3rem">',
                    '        <span style="flex:1">%s</span>' % esc(m),
                    '        <button class="audio-btn" data-speak="%s" onclick="speakText(this.dataset.speak,this)">Listen</button>' % esc(m),
                    '      </div>',
                    '    </details>',
                    '  </div>']
        out += ['  ' + checklist(['I recorded all six answers',
                                  'I used at least five of the fifteen words',
                                  'I compared at least two of my answers with the models']),
                '</div>']
    out.append('</div><!-- /tab-speakw -->')
    return '\n'.join(out) + '\n'


def confere():
    erros = []
    for n, _, palavras, perguntas in SPEAK:
        if len(perguntas) != 6 or len(palavras) != 15:
            erros.append('aula %d: %d perguntas, %d palavras' % (n, len(perguntas), len(palavras)))
        usadas = {w for w in palavras for _, m in perguntas if w.lower() in m.lower()}
        if len(usadas) < 8:
            erros.append('aula %d: modelos usam so %d palavras da aula' % (n, len(usadas)))
    for n, _, _, _, palavras, _, modelo in MAIL:
        usadas = [w for w in palavras if w.lower() in modelo.lower()]
        if len(usadas) < 5:
            erros.append('aula %d (mail): modelo usa so %d palavras' % (n, len(usadas)))
    todo = ' '.join(m for *_, ps in SPEAK for _, m in ps) + ' '.join(x[6] for x in MAIL)
    if re.search(r'[à-ÿ]', todo):
        erros.append('acento no conteudo (o detector de portugues reprova): %s'
                     % sorted(set(re.findall(r'\w*[à-ÿ]\w*', todo))))
    if '"' in ''.join(m for *_, ps in SPEAK for _, m in ps):
        erros.append('aspas duplas numa resposta-modelo (quebra o data-speak)')
    return erros


if __name__ == '__main__':
    e = confere()
    if e:
        sys.exit('RECUSADO:\n  ' + '\n  '.join(e))
    open(os.path.join(AQUI, 'mail.html'), 'w', encoding='utf-8').write(mail_html())
    open(os.path.join(AQUI, 'speak.html'), 'w', encoding='utf-8').write(speak_html())
    print('mail.html  : %d propostas' % len(MAIL))
    print('speak.html : %d aulas x 6 perguntas = %d' % (len(SPEAK), 6 * len(SPEAK)))
