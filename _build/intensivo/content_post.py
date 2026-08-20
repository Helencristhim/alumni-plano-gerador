# -*- coding: utf-8 -*-
"""Post-class das seis aulas, no formato da REGUA.

O nucleo sao as CINCO LINHAS da aula: a aluna as reencontra completas (recap), as completa
uma vez (lacunas) e responde tres perguntas em voz alta com a resposta ao lado. Fala e
escrita sao opcionais e abrem sob demanda -- e a gravacao, que so pode aparecer AQUI, fica
no computador dela: nao sobe para lugar nenhum e nao chega ao professor.

Nenhum conjunto lexical novo entra no post-class.
"""

POST = {}

POST[1] = {
 'rotulo': 'Consolidar as cinco linhas', 'titulo': 'Your five lines',
 'intro_pt': ('Retoma o que aconteceu, recupera o ponto corrigido e conecta &agrave; aula 2. Nenhum conjunto lexical novo. '
              'O n&uacute;cleo s&atilde;o as cinco linhas; fala, escrita e recursos s&atilde;o opcionais e abrem sob demanda. '
              '&Eacute; aqui &mdash; e s&oacute; aqui &mdash; que a grava&ccedil;&atilde;o pode aparecer.'),
 'situacao': ('The president of Carestream, visiting from the United States, has just arrived at your office in '
              'S&atilde;o Paulo. You open the presentation.'),
 'fazendo': ('Saying five things: what the company does, how long it has worked, the three ways it works, who it works '
             'with, and what you are responsible for.'),
 'vocab': ['healthcare market', 'medical technology', 'to represent a brand', 'to distribute',
           'to provide technical services', 'to be responsible for'],
 'lacunas': [('Let me give you a short ', 'overview', ' of the company.'),
             ('We have been in the healthcare market ', 'for', ' 38 years.'),
             ('We ', 'represent', ' international brands, we distribute medical technology, and we provide technical services.'),
             ('We work with hospitals, clinics and specialized ', 'centers', ' in Brazil.'),
             ('I am ', 'responsible', ' for Corporate Management.')],
 'perguntas': [('How long has the company been in the market?',
                'We have been in the healthcare market for 38 years. &mdash; The number is 38. 1988 is the year the company started.'),
               ('What are the three ways the company works?',
                'We represent international brands, we distribute medical technology, and we provide technical services.'),
               ('He asks about response times for repairs. What do you say?',
                'I would need to confirm that &mdash; our technical team can give you more detail.')],
 'fala': 'Say your opening again, on your own. Use the five lines above.',
 'escrita': ('Write your opening as you would say it &mdash; five lines, one per function. This is the speech map you '
             'take into the room on 31 August.', 'Let me give you a short overview&hellip;'),
 'linha': ('Lesson 2 is the story of the company. Write down <strong>one date or one fact</strong> from the history you '
           'would like to be able to say in English.'),
}

POST[2] = {
 'rotulo': 'Consolidar a hist&oacute;ria', 'titulo': 'Your five lines',
 'intro_pt': ('Retoma os quatro marcos e a organiza&ccedil;&atilde;o de hoje, e conecta &agrave; aula 3. Nenhum conjunto '
              'lexical novo. Fala e escrita s&atilde;o opcionais.'),
 'situacao': 'The visitor knows what the company does, and asks how it started &mdash; and what you do there.',
 'fazendo': 'Telling the story in four moments, saying how the company is organized today, and where you sit in it.',
 'vocab': ['a sales representative', 'to allow someone to', 'to be organized into', 'to oversee',
           'an external audit', 'a milestone'],
 'lacunas': [('We started as a ', 'distributor', ' of Kodak film in 1988.'),
             ('In 1996, we became a sales ', 'representative', ' for GE Diagnostic Imaging.'),
             ('This ', 'allowed', ' us to represent other international brands.'),
             ('Today we are ', 'organized', ' into commercial, technical service and corporate areas.'),
             ('I ', 'oversee', ' Corporate Management.')],
 'perguntas': [('When did the company start, and how?',
                'We started as a distributor of Kodak film in 1988.'),
               ('What changed in 1996?',
                'In 1996 we became a sales representative for GE Diagnostic Imaging. This allowed us to represent other international brands.'),
               ('He asks how many people work in the service area. What do you say?',
                'That is with our technical team &mdash; [name] can give you more detail.')],
 'fala': 'Tell the story of the company again, on your own. Four moments, then how it is organized today.',
 'escrita': ('Write the one-sentence version of the story &mdash; where it started and what it is today. This is the version '
             'a visitor in a hurry will get.', 'We started in 1988 and today&hellip;'),
 'linha': ('Lesson 3 is the portfolio. Write down <strong>one product</strong> you are not sure how to say in English &mdash; '
           'we will place it in a category.'),
}

POST[3] = {
 'rotulo': 'Consolidar o portf&oacute;lio', 'titulo': 'Your five lines',
 'intro_pt': ('Retoma as quatro categorias, os parceiros e a recusa da participa&ccedil;&atilde;o, e conecta &agrave; aula 4. '
              'Nenhum conjunto lexical novo.'),
 'situacao': 'The president of Carestream asks you to walk him through what the company carries.',
 'fazendo': 'Presenting four categories with one example each, naming the brands, and passing on what is not yours.',
 'vocab': ['a portfolio', 'to cover', 'a solution', 'to be used for', 'diagnostic imaging', 'a category'],
 'lacunas': [('Our portfolio ', 'covers', ' four main areas.'),
             ('Diagnostic ', 'imaging', ' &mdash; for example, X-ray and ultrasound.'),
             ('This solution is ', 'used', ' for diagnosis in hospitals and clinics.'),
             ('We ', 'represent', ' international brands, including Carestream.'),
             ('Our technical team can provide more ', 'detail', '.')],
 'perguntas': [('What does your portfolio cover?',
                'Our portfolio covers four main areas: diagnostic imaging, advanced surgical technology, hospital care, and cardiology.'),
               ('Give one example from imaging.',
                'X-ray and ultrasound, for example. This solution is used for diagnosis in hospitals and clinics.'),
               ('He asks which partner is the biggest. What do you say?',
                'I would need to confirm that &mdash; our commercial team can give you more detail.')],
 'fala': 'Present the portfolio again, on your own. Four categories, one example each.',
 'escrita': ('Write the four categories with one example each. Four lines, nothing more &mdash; the discipline is the point.',
             'Our portfolio covers four main areas.'),
 'linha': ('Lesson 4 is coverage and service. Write down <strong>one question</strong> about support you think the visitor '
           'will ask.'),
}

POST[4] = {
 'rotulo': 'Consolidar cobertura e servi&ccedil;o', 'titulo': 'Your five lines',
 'intro_pt': ('Retoma a resposta em duas metades e o benef&iacute;cio operacional, e conecta &agrave; aula 5. Nenhum conjunto '
              'lexical novo.'),
 'situacao': 'The visitor is deciding whether to expand with you, and asks who installs and who maintains.',
 'fazendo': 'Answering coverage and service as one answer, with the in-house team as the operational benefit.',
 'vocab': ['headquarters', 'a distribution centre', 'a branch', 'in-house', 'applications support', 'maintenance'],
 'lacunas': [('Our ', 'headquarters', ' is in S&atilde;o Paulo.'),
             ('We operate ', 'directly', ' in several states.'),
             ('Our service team ', 'includes', ' technicians, coordinators and applications support.'),
             ('The team is ', 'in-house', ', not outsourced.'),
             ('I would need to ', 'confirm', ' that detail.')],
 'perguntas': [('Where does the company operate?',
                'Our headquarters and distribution centre are in S&atilde;o Paulo, and we operate directly in several states.'),
               ('Who installs and maintains the equipment?',
                'Our service team is in-house: technicians, coordinators and applications support. We install it, we train your people, and we maintain it.'),
               ('He asks how fast you respond to a service call. What do you say?',
                'I would need to confirm that detail.')],
 'fala': 'Answer the support question again, on your own. Service first, then coverage.',
 'escrita': ('Write the two halves as one answer: where the company is, and who keeps the equipment running. Five lines at most.',
             'Our service team is in-house&hellip;'),
 'linha': ('Lesson 5 is the numbers. Before the lesson, <strong>confirm with Thomaz</strong> which figures are authorised '
           'for this meeting &mdash; and write down anything that is not.'),
}

POST[5] = {
 'rotulo': 'Consolidar os n&uacute;meros', 'titulo': 'Your five lines',
 'intro_pt': ('Retoma uma mensagem por gr&aacute;fico, a oportunidade dita como oportunidade e a recusa, e conecta &agrave; '
              'simula&ccedil;&atilde;o. Nenhum conjunto lexical novo.'),
 'situacao': 'The results slide is on the screen, and the visitor is already reading it.',
 'fazendo': 'Giving each chart one message, one number, one comparison &mdash; and two opportunities, said as opportunities.',
 'vocab': ['net income', 'to increase from&hellip; to&hellip;', 'to account for', 'partner mix',
           'an opportunity', 'a commitment'],
 'lacunas': [('Net income ', 'increased', ' from 87.7 to 105.6 million reais.'),
             ('That is ', 'about', ' twenty per cent.'),
             ('Carestream ', 'accounts', ' for thirty-eight per cent of our partner mix.'),
             ('One ', 'opportunity', ' is the Midea portfolio in Brazil.'),
             ('I would need to ', 'confirm', ' that figure.')],
 'perguntas': [('How did last year go?',
                'Net income increased from 87.7 to 105.6 million reais &mdash; about twenty per cent.'),
               ('How much of the business is Carestream?',
                'Carestream accounts for thirty-eight per cent of our partner mix, against eighteen per cent in 2024.'),
               ('He asks what your recurring revenue is. What do you say?',
                'I would need to confirm that figure.')],
 'fala': 'Give the results again, on your own. One message per chart, then one opportunity.',
 'escrita': ('Write one sentence for each chart. Three sentences. If a fourth appears, it is probably a number being '
             'read aloud.', 'Net income increased&hellip;'),
 'linha': ('Lesson 6 is the whole meeting. Write down <strong>the block that still worries you</strong> &mdash; we start there.'),
}

POST[6] = {
 'rotulo': 'Consolidar a reuni&atilde;o', 'titulo': 'Your five blocks',
 'intro_pt': ('Fecha o intensivo. Nenhum conjunto lexical novo, e nada a preparar depois disto: o que ela leva para '
              '31/08 s&atilde;o os cinco blocos e os movimentos de reparo.'),
 'situacao': 'The full meeting, with interruptions &mdash; the same shape as 31 August.',
 'fazendo': 'Running five blocks in order, coming back after each interruption, and closing the meeting yourself.',
 'vocab': ['Could you repeat that?', 'If I understood correctly&hellip;', 'Let me check the slide.',
           '[Name] can provide more detail.', 'I would need to confirm that.', 'Let me come back to that.'],
 'lacunas': [('Let me give you a short ', 'overview', ' of the company.'),
             ('We started as a ', 'distributor', ' of Kodak film in 1988.'),
             ('Our portfolio ', 'covers', ' four main areas.'),
             ('Our ', 'headquarters', ' is in S&atilde;o Paulo, and our service team is in-house.'),
             ('Net income ', 'increased', ' from 87.7 to 105.6 million reais.')],
 'perguntas': [('He interrupts in the middle of the portfolio block. What do you say?',
                'Of course. Let me come back to that &mdash; so, our portfolio covers four main areas.'),
               ('He asks who decides on new partnerships.',
                'Thomaz decides on new partnerships &mdash; he can give you more detail on that.'),
               ('He asks two questions at once, quickly.',
                'Could you repeat that? &mdash; or: If I understood correctly, you are asking about&hellip;')],
 'fala': 'Run the five blocks once, out loud, with your slides in front of you &mdash; as you will on Monday.',
 'escrita': ('Write the five opening lines, one per block. This is the map you take into the room on 31 August &mdash; '
             'print it, or keep it beside your slides.', 'Let me give you a short overview&hellip;'),
 'linha': ('On 31 August you will have the same slides and the same speech maps in front of you. Nothing in that room '
           'will be new.'),
}
