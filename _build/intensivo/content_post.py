# -*- coding: utf-8 -*-
"""Post-class das seis aulas. Opcional por desenho: ela escolhe o que fizer sentido.

Tres partes fixas: a recapitulacao (referencia rapida), uma fala gravada (90 segundos) e
uma escrita curta. A quarta e a ponte: UMA linha para trazer para a aula seguinte -- na
aula 6 ela vira a linha para levar para a reuniao.
"""

POST = {}

POST[1] = {
 'recap': [('Situation', 'The president of Carestream arrives at the head office in S&atilde;o Paulo on 31 August. You open the presentation, with the CEO in the room.'),
           ('What you did', 'Opened the meeting in four moves: welcome, name and role, what the company does, what your area covers.'),
           ('Key language', '<em>Welcome to&hellip;</em> &middot; <em>I am Rita Rodrigues, Corporate Management Director.</em> &middot; <em>We distribute medical technology&hellip;</em> &middot; <em>My area covers&hellip;</em> &middot; <em>I would need to confirm that detail.</em>'),
           ('Key vocabulary', '<em>distribute</em> &middot; <em>medical technology</em> &middot; <em>nationwide</em> &middot; <em>corporate management</em> &middot; <em>business processes</em> &middot; <em>to represent a brand</em>')],
 'exemplos': ['&ldquo;Welcome to Imagem Healthcare Solutions. I am Rita Rodrigues, Corporate Management Director.&rdquo;',
              '&ldquo;We distribute medical technology to hospitals and clinics nationwide.&rdquo;',
              '&ldquo;My area covers IT, HR, quality, corporate controlling and business processes.&rdquo;'],
 'fala': ('Someone you have never met walks into your office and you have forty seconds before they sit down. Open the meeting.',
          ['welcome the visitor to the company;', 'say your name and your role;',
           'say what the company does, in one sentence;', 'say what your area covers.']),
 'escrita': ('Write your four moves as you would say them &mdash; one line each. This is the map you will have in front of you on 31 August.',
             'Welcome to&hellip;'),
 'linha': 'Lesson 2 is about the company&rsquo;s history and how it is organised today. Write down <strong>one date or one fact</strong> from the history you would like to be able to say in English.',
}

POST[2] = {
 'recap': [('Situation', 'The visitor knows what the company does and asks where it came from &mdash; and what you do there.'),
           ('What you did', 'Told 38 years in four moments, said where you sit, and forwarded what belongs to another area.'),
           ('Key language', '<em>We started in 1988.</em> &middot; <em>We became a sales representative for GE in 1996.</em> &middot; <em>From 2016 we added&hellip;</em> &middot; <em>We are a team of nine.</em> &middot; <em>Service is a different area, with its own director.</em>'),
           ('Key vocabulary', '<em>a sales representative</em> &middot; <em>to expand</em> &middot; <em>governance</em> &middot; <em>external audit</em> &middot; <em>a board</em> &middot; <em>a business unit</em>')],
 'exemplos': ['&ldquo;We started in 1988, distributing Kodak film.&rdquo;',
              '&ldquo;In 1996 we became a sales representative for GE Diagnostic Imaging.&rdquo;',
              '&ldquo;I lead Corporate Management &mdash; IT, HR, quality, controlling and business processes, with a team of nine.&rdquo;'],
 'fala': ('A visitor asks: &ldquo;How did the company start, and what do you do here?&rdquo; You have about a minute.',
          ['four moments, not thirteen;', 'one sentence for what changed between 1988 and today;',
           'what your area covers;', 'one thing you would forward, and to whom.']),
 'escrita': ('Write the one-sentence version of the history &mdash; where it started and what it is today. This is the version a visitor in a hurry will get.',
             'We started in 1988 and today&hellip;'),
 'linha': 'Lesson 3 is the portfolio. Write down <strong>one product</strong> you are not sure how to say in English &mdash; we will place it in a category.',
}

POST[3] = {
 'recap': [('Situation', 'The president of Carestream wants to know where his products sit inside what you carry.'),
           ('What you did', 'Presented four categories with one example each, named the partners, and refused a share number.'),
           ('Key language', '<em>We work with four main areas.</em> &middot; <em>Our largest area is diagnostic imaging.</em> &middot; <em>For example&hellip;</em> &middot; <em>We also represent international brands.</em> &middot; <em>I would need to confirm that detail.</em>'),
           ('Key vocabulary', '<em>diagnostic imaging</em> &middot; <em>advanced surgical technology</em> &middot; <em>hospital care</em> &middot; <em>cardiology and cardiac rhythm</em> &middot; <em>to represent</em>')],
 'exemplos': ['&ldquo;We work with four main areas. Diagnostic imaging, for example X-ray and ultrasound.&rdquo;',
              '&ldquo;We represent Medtronic, Carestream, GE, Guerbet and others.&rdquo;',
              '&ldquo;This year we started Carestream XR operations.&rdquo;'],
 'fala': ('A visitor says: &ldquo;Walk me through what you carry.&rdquo; You have about a minute, and he knows imaging well.',
          ['the four categories, in the order that serves him;', 'one example each &mdash; and then stop;',
           'the partners, including his own company;', 'what you would forward.']),
 'escrita': ('Write the four categories with one example each. Four lines, nothing more &mdash; the discipline is the point.',
             'We work with four main areas.'),
 'linha': 'Lesson 4 is coverage and service. Write down <strong>one question</strong> about support you think the visitor will ask.',
}

POST[4] = {
 'recap': [('Situation', 'The visitor is deciding whether to expand XR operations with you, and asks who installs and who maintains.'),
           ('What you did', 'Answered coverage and service as one answer, gave the number you own, and forwarded response time.'),
           ('Key language', '<em>Our head office and distribution centre are in S&atilde;o Paulo.</em> &middot; <em>We have teams in several states.</em> &middot; <em>We have our own service team &mdash; thirty technicians.</em> &middot; <em>I would need to confirm our response time.</em>'),
           ('Key vocabulary', '<em>a distribution centre</em> &middot; <em>a branch</em> &middot; <em>in-house</em> &middot; <em>applications support</em> &middot; <em>response time</em> &middot; <em>maintenance</em>')],
 'exemplos': ['&ldquo;We have our own service team &mdash; thirty technicians, coordinators and applications support.&rdquo;',
              '&ldquo;We have teams in several states, and a logistics branch in Santa Catarina for imports.&rdquo;',
              '&ldquo;I would need to confirm our response time.&rdquo;'],
 'fala': ('A visitor asks: &ldquo;If we expand with you, who installs it and who keeps it running?&rdquo;',
          ['start with the half he is really asking about;', 'the number you own &mdash; thirty technicians;',
           'where the company is, without reading a map;', 'the one thing you would confirm later.']),
 'escrita': ('Write the two halves as one answer: where the company is, and who keeps the equipment running. Five lines at most.',
             'We have our own service team&hellip;'),
 'linha': 'Lesson 5 is the numbers. Before the lesson, <strong>confirm with Thomaz</strong> which figures are authorised for this meeting &mdash; and write down anything that is not.',
}

POST[5] = {
 'recap': [('Situation', 'The results slide is on the screen and the visitor is already reading it.'),
           ('What you did', 'Gave each chart one sentence, said the opportunities as possibilities, and refused a figure you were never given.'),
           ('Key language', '<em>Net income grew about twenty per cent last year.</em> &middot; <em>The first two months are ahead of last year.</em> &middot; <em>Carestream has grown from eighteen to thirty-eight per cent of our partner mix.</em> &middot; <em>That is a possibility, not a commitment.</em>'),
           ('Key vocabulary', '<em>net income</em> &middot; <em>to grow by</em> &middot; <em>the same period last year</em> &middot; <em>partner mix</em> &middot; <em>recurring revenue</em> &middot; <em>a commitment</em>')],
 'exemplos': ['&ldquo;Net income grew about twenty per cent from 2024 to 2025.&rdquo;',
              '&ldquo;Carestream has grown from eighteen to thirty-eight per cent of our partner mix.&rdquo;',
              '&ldquo;We see potential for Midea in Brazil &mdash; that is a possibility, not a commitment.&rdquo;'],
 'fala': ('A visitor says: &ldquo;Give me the headline on last year, and where you see this going.&rdquo; He will ask one question you cannot answer.',
          ['one sentence for the growth;', 'one sentence for what it means for him;',
           'one opportunity, said as a possibility;', 'the refusal, said calmly &mdash; and then keep going.']),
 'escrita': ('Write one sentence for each chart. Three sentences. If a fourth appears, it is probably a number being read aloud.',
             'Net income grew&hellip;'),
 'linha': 'Lesson 6 is the whole meeting. Write down <strong>the block that still worries you</strong> &mdash; we start there.',
}

POST[6] = {
 'recap': [('Situation', 'The full meeting, with interruptions &mdash; the same shape as 31 August.'),
           ('What you did', 'Ran five blocks in order, came back after each interruption, and closed the meeting yourself.'),
           ('Key language', '<em>Of course &mdash; let me come back to that.</em> &middot; <em>Thomaz can give you more detail on that.</em> &middot; <em>I would need to confirm that detail.</em>'),
           ('Key vocabulary', 'Everything from lessons 1 to 5. Nothing new entered today.')],
 'exemplos': ['&ldquo;Welcome to Imagem Healthcare Solutions. I am Rita Rodrigues, Corporate Management Director.&rdquo;',
              '&ldquo;Of course &mdash; let me come back to that. So: where the company operates.&rdquo;',
              '&ldquo;I would need to confirm that detail.&rdquo;'],
 'fala': ('The meeting itself. Run the five blocks once, out loud, with your slides in front of you &mdash; as you will on Monday.',
          ['welcome and who you are;', 'where the company came from and what it sells;',
           'where it operates and who keeps it running;', 'how last year went;',
           'and one line for anything you do not have.']),
 'escrita': ('Write the five opening lines, one per block. This is the map you take into the room on 31 August &mdash; print it, or keep it beside your slides.',
             'Welcome to&hellip;'),
 'linha': 'On 31 August you will have the same slides and the same map in front of you. Nothing in that room will be new.',
}
