// Gabriela Pires — dados pedagógicos do Bloco 1 (Aulas 1-5)
// A1+, 15-16 anos, viagem Europa Fev/2027, foco séries pop + Paris

const studentInfo = {
  name: 'Gabriela Pires',
  shortName: 'Gabriela',
  slug: 'gabriela-pires',
  age: '15-16',
  city: 'São Paulo, SP',
  level: 'A1+ (Iniciante)',
  profession: 'Estudante do ensino médio',
  totalLessons: 48,
  blockLessons: 5,
  format: 'Presencial — 3x/semana — 60 min',
  travelDate: 'Fevereiro de 2027',
  travelDest: 'Europa (foco França)',
  promise: 'De "tentar falar com apoio do português" a "pedir o caminho em Paris sem travar" — em 48 aulas com as séries, celebridades e viagens que você já ama.',
  journeyFrom: 'Aluna que entende um pouco, tenta falar, mas ainda depende do português para quase tudo — e sabe que vai para a Europa em 2027.',
  journeyTo: 'Viajante que chega à França, se vira em inglês em situações reais de turismo, conta histórias, opina sobre filmes e se apresenta com confiança para quem quiser ouvir.',
  vitoria: 'Sentir-se independente e segura na França — pedir o caminho, fazer uma compra, contar de onde é e por que está viajando, tudo em inglês, sem travar.',
  stake: 'Chegar à Europa em fevereiro de 2027 sem conseguir se comunicar em situações básicas de viagem e perder a experiência por falta de autonomia linguística no momento em que mais importa.',
};

const lessonTitles = {
  1: 'Who Is Gabriela? — Diagnostic + Personal Introduction',
  2: 'Hello, Nice to Meet You! — Greetings, Introductions & the Alphabet',
  3: 'This Is My World — People, Places & Things Around Me',
  4: 'My Daily Life — Routines in São Paulo with the Present Simple',
  5: 'Do You Like It? — Likes, Dislikes & Pop Culture',
  6: 'Numbers, Time & Dates — Tools to Survive in Paris',
  7: 'Where Are You From? — Countries, Nationalities & the World',
  8: 'Can You Do That? — Abilities & Asking for Help',
  9: 'Where Is It? — Directions & Getting Around Paris',
  10: 'What Do You Look Like? — Describing People & Characters',
  11: "Let's Eat! — Food, Menus & Ordering at a Restaurant",
  12: 'Shopping in the City — Clothes, Prices & Choices',
  13: 'What Were You Doing? — Past Continuous & Yesterday',
  14: 'What Happened? — Past Simple & Storytelling',
  15: 'Have You Ever…? — Experiences & Present Perfect',
  16: "Tell Me About Your Plans! — Future with 'Going To'",
  17: 'Emergency Mode — Health & Asking for Help Abroad',
  18: "Let's Compare! — Comparative & Superlative Adjectives",
  19: 'Making Plans & Inviting People — Social English',
  20: 'Block 1 Review & Mid-Journey Milestone',
};

const lessonPromises = {
  1: 'Depois desta aula, você sabe se apresentar em inglês em qualquer lugar — escola, viagem, conhecendo gente nova.',
  2: 'Depois desta aula, você cumprimenta, soletra seu nome e sobrevive a um check-in de hotel em Paris.',
  3: 'Depois desta aula, você apresenta seu mundo — sua escola, suas coisas, sua cidade — para qualquer pessoa em inglês.',
  4: 'Depois desta aula, você conta seu dia inteiro em inglês — da hora que acorda até a hora que dorme.',
  5: 'Depois desta aula, você fala das suas séries, seus crushes e suas opiniões em inglês como uma fã de verdade.',
};

const lessonImages = {
  1: 'https://images.unsplash.com/photo-1531746020798-e6953c6e8e04?w=1200&q=80',
  2: 'https://images.unsplash.com/photo-1502602898657-3e91760cbb34?w=1200&q=80',
  3: 'https://images.unsplash.com/photo-1519677100203-a0e668c92439?w=1200&q=80',
  4: 'https://images.unsplash.com/photo-1554224155-6726b3ff858f?w=1200&q=80',
  5: 'https://images.unsplash.com/photo-1522202176988-66273c2fd55f?w=1200&q=80',
};

const lessonHeaderImages = {
  1: 'https://images.unsplash.com/photo-1531746020798-e6953c6e8e04?w=600&q=80',
  2: 'https://images.unsplash.com/photo-1502602898657-3e91760cbb34?w=600&q=80',
  3: 'https://images.unsplash.com/photo-1519677100203-a0e668c92439?w=600&q=80',
  4: 'https://images.unsplash.com/photo-1554224155-6726b3ff858f?w=600&q=80',
  5: 'https://images.unsplash.com/photo-1522202176988-66273c2fd55f?w=600&q=80',
};

const stampImages = {
  1: 'https://images.unsplash.com/photo-1543269664-7eef42226a21?w=200&q=80',
  2: 'https://images.unsplash.com/photo-1502602898657-3e91760cbb34?w=200&q=80',
  3: 'https://images.unsplash.com/photo-1519677100203-a0e668c92439?w=200&q=80',
  4: 'https://images.unsplash.com/photo-1554224155-6726b3ff858f?w=200&q=80',
  5: 'https://images.unsplash.com/photo-1522202176988-66273c2fd55f?w=200&q=80',
};

const stampLabels = {1: 'Intro', 2: 'Greet', 3: 'My World', 4: 'Routine', 5: 'Likes'};

// VOCABULÁRIO — usado em pre-class (frase A) e material professor (frase B, diferente)
const vocab = {
  1: [
    {word: 'name', pt: 'nome', exA: '"My name is Gabriela."', exB: '"What is your name?"'},
    {word: 'live', pt: 'morar', exA: '"I live in São Paulo."', exB: '"She lives near the school."'},
    {word: 'student', pt: 'estudante', exA: '"I am a student."', exB: '"My friend is a high school student."'},
    {word: 'hobby', pt: 'hobby / passatempo', exA: '"My favorite hobby is watching series."', exB: '"What is your hobby?"'},
    {word: 'travel', pt: 'viajar / viagem', exA: '"I want to travel to France."', exB: '"My family loves to travel in the summer."'},
    {word: 'dream', pt: 'sonho', exA: '"My dream is to visit Paris."', exB: '"She has a big dream."'},
    {word: 'favorite', pt: 'favorito', exA: '"My favorite series is Gossip Girl."', exB: '"His favorite color is blue."'},
    {word: 'learn', pt: 'aprender', exA: '"I want to learn English."', exB: '"They learn fast at school."'},
  ],
  2: [
    {word: 'hello', pt: 'olá', exA: '"Hello! How are you?"', exB: '"Hello, my name is Gabriela."'},
    {word: 'good morning', pt: 'bom dia', exA: '"Good morning, teacher."', exB: '"Good morning! Did you sleep well?"'},
    {word: 'nice to meet you', pt: 'prazer em conhecer', exA: '"Nice to meet you, Sarah."', exB: '"Nice to meet you too!"'},
    {word: 'spell', pt: 'soletrar', exA: '"Can you spell your name?"', exB: '"How do you spell that?"'},
    {word: 'last name', pt: 'sobrenome', exA: '"My last name is Pires."', exB: '"What is your last name, please?"'},
    {word: 'how are you', pt: 'como você está', exA: '"How are you today?"', exB: '"Hi Sarah, how are you?"'},
    {word: 'fine', pt: 'bem', exA: '"I am fine, thank you."', exB: '"She is fine today."'},
    {word: 'goodbye', pt: 'tchau', exA: '"Goodbye! See you tomorrow."', exB: '"Goodbye, have a nice day!"'},
  ],
  3: [
    {word: 'this', pt: 'este / esta', exA: '"This is my phone."', exB: '"This is my best friend."'},
    {word: 'that', pt: 'aquele / aquela', exA: '"That is my school."', exB: '"That is the Eiffel Tower!"'},
    {word: 'these', pt: 'estes / estas', exA: '"These are my books."', exB: '"These are my new sneakers."'},
    {word: 'those', pt: 'aqueles / aquelas', exA: '"Those are my classmates."', exB: '"Those are my old photos."'},
    {word: 'friend', pt: 'amigo / amiga', exA: '"This is my best friend."', exB: '"My friend is from Rio."'},
    {word: 'family', pt: 'família', exA: '"My family lives in São Paulo."', exB: '"I love my family."'},
    {word: 'school', pt: 'escola', exA: '"My school is on Paulista Avenue."', exB: '"School starts at seven."'},
    {word: 'neighborhood', pt: 'bairro', exA: '"My neighborhood is quiet."', exB: '"This neighborhood has many cafes."'},
  ],
  4: [
    {word: 'wake up', pt: 'acordar', exA: '"I wake up at seven."', exB: '"She wakes up early every day."'},
    {word: 'have breakfast', pt: 'tomar café da manhã', exA: '"I have breakfast at home."', exB: '"He has breakfast with his family."'},
    {word: 'go to school', pt: 'ir para a escola', exA: '"I go to school by bus."', exB: '"My sister goes to school at eight."'},
    {word: 'study', pt: 'estudar', exA: '"I study English every day."', exB: '"She studies a lot for the test."'},
    {word: 'watch', pt: 'assistir', exA: '"I watch series at night."', exB: '"Rory watches a movie every weekend."'},
    {word: 'always', pt: 'sempre', exA: '"I always have breakfast."', exB: '"She always studies in the morning."'},
    {word: 'usually', pt: 'geralmente', exA: '"I usually take the metro."', exB: '"He usually wakes up late."'},
    {word: 'never', pt: 'nunca', exA: '"I never skip breakfast."', exB: '"She never misses class."'},
  ],
  5: [
    {word: 'love', pt: 'amar / adorar', exA: '"I love Gossip Girl."', exB: '"She loves romantic movies."'},
    {word: 'like', pt: 'gostar', exA: '"I like Friends."', exB: '"Do you like coffee?"'},
    {word: "don't like", pt: 'não gostar', exA: '"I don\'t like horror movies."', exB: '"He doesn\'t like spicy food."'},
    {word: 'hate', pt: 'odiar', exA: '"I hate Mondays."', exB: '"She hates waking up early."'},
    {word: 'series', pt: 'série', exA: '"My favorite series is Friends."', exB: '"That series has six seasons."'},
    {word: 'character', pt: 'personagem', exA: '"Blair is my favorite character."', exB: '"That character is so funny."'},
    {word: 'celebrity', pt: 'celebridade', exA: '"Blake Lively is a famous celebrity."', exB: '"He is a celebrity in Brazil."'},
    {word: 'obsessed with', pt: 'obcecada por', exA: '"I am obsessed with Gilmore Girls."', exB: '"She is obsessed with that song."'},
  ],
};

const matching = {
  1: [
    {word: 'name', correct: 'nome', distractors: ['amigo', 'sonho']},
    {word: 'live', correct: 'morar', distractors: ['aprender', 'viajar']},
    {word: 'student', correct: 'estudante', distractors: ['professor', 'estrangeiro']},
    {word: 'hobby', correct: 'hobby / passatempo', distractors: ['trabalho', 'matéria']},
    {word: 'travel', correct: 'viajar', distractors: ['estudar', 'morar']},
    {word: 'dream', correct: 'sonho', distractors: ['plano', 'medo']},
    {word: 'favorite', correct: 'favorito', distractors: ['popular', 'famoso']},
    {word: 'learn', correct: 'aprender', distractors: ['ensinar', 'estudar']},
  ],
  2: [
    {word: 'hello', correct: 'olá', distractors: ['tchau', 'obrigado']},
    {word: 'good morning', correct: 'bom dia', distractors: ['boa noite', 'boa tarde']},
    {word: 'nice to meet you', correct: 'prazer em conhecer', distractors: ['até logo', 'desculpe']},
    {word: 'spell', correct: 'soletrar', distractors: ['gritar', 'cantar']},
    {word: 'last name', correct: 'sobrenome', distractors: ['apelido', 'nome próprio']},
    {word: 'fine', correct: 'bem', distractors: ['ruim', 'cansado']},
    {word: 'how are you', correct: 'como você está', distractors: ['quem é você', 'onde você está']},
    {word: 'goodbye', correct: 'tchau', distractors: ['oi', 'desculpe']},
  ],
  3: [
    {word: 'this', correct: 'este / esta', distractors: ['aquele', 'estes']},
    {word: 'that', correct: 'aquele / aquela', distractors: ['este', 'aqueles']},
    {word: 'these', correct: 'estes / estas', distractors: ['aqueles', 'este']},
    {word: 'those', correct: 'aqueles / aquelas', distractors: ['estes', 'aquele']},
    {word: 'friend', correct: 'amigo', distractors: ['inimigo', 'parente']},
    {word: 'family', correct: 'família', distractors: ['amigo', 'turma']},
    {word: 'school', correct: 'escola', distractors: ['casa', 'cidade']},
    {word: 'neighborhood', correct: 'bairro', distractors: ['cidade', 'rua']},
  ],
  4: [
    {word: 'wake up', correct: 'acordar', distractors: ['dormir', 'descansar']},
    {word: 'have breakfast', correct: 'tomar café da manhã', distractors: ['jantar', 'almoçar']},
    {word: 'go to school', correct: 'ir para a escola', distractors: ['voltar para casa', 'sair para passear']},
    {word: 'study', correct: 'estudar', distractors: ['ensinar', 'descansar']},
    {word: 'watch', correct: 'assistir', distractors: ['ouvir', 'ler']},
    {word: 'always', correct: 'sempre', distractors: ['nunca', 'às vezes']},
    {word: 'usually', correct: 'geralmente', distractors: ['raramente', 'nunca']},
    {word: 'never', correct: 'nunca', distractors: ['sempre', 'agora']},
  ],
  5: [
    {word: 'love', correct: 'adorar', distractors: ['odiar', 'detestar']},
    {word: 'like', correct: 'gostar', distractors: ['precisar', 'odiar']},
    {word: "don't like", correct: 'não gostar', distractors: ['adorar', 'querer']},
    {word: 'hate', correct: 'odiar', distractors: ['amar', 'gostar']},
    {word: 'series', correct: 'série', distractors: ['filme', 'episódio']},
    {word: 'character', correct: 'personagem', distractors: ['ator', 'celebridade']},
    {word: 'celebrity', correct: 'celebridade', distractors: ['personagem', 'fã']},
    {word: 'obsessed with', correct: 'obcecada por', distractors: ['cansada de', 'aliviada com']},
  ],
};

const fillIn = {
  1: [
    {sentence: '"My ___ is Gabriela Pires."', answer: 'name', hint: 'Hint: the word people use to call you', phrase: 'My name is Gabriela Pires.'},
    {sentence: '"I ___ in São Paulo."', answer: 'live', hint: 'Hint: the verb that means to have your home in a place', phrase: 'I live in São Paulo.'},
    {sentence: '"I am a ___ at high school."', answer: 'student', hint: 'Hint: someone who learns at school', phrase: 'I am a student at high school.'},
    {sentence: '"My ___ is to visit Paris in 2027."', answer: 'dream', hint: 'Hint: something you really hope will happen', phrase: 'My dream is to visit Paris in 2027.'},
    {sentence: '"I want to ___ English to talk in France."', answer: 'learn', hint: 'Hint: to get new knowledge or a new skill', phrase: 'I want to learn English to talk in France.'},
    {sentence: '"My ___ series is Gossip Girl."', answer: 'favorite', hint: 'Hint: the one you love the most', phrase: 'My favorite series is Gossip Girl.'},
  ],
  2: [
    {sentence: '"___ ! How are you today?"', answer: 'Hello', hint: 'Hint: a friendly word to start a conversation', phrase: 'Hello! How are you today?'},
    {sentence: '"Good ___ , teacher."', answer: 'morning', hint: 'Hint: the part of the day before lunch', phrase: 'Good morning, teacher.'},
    {sentence: '"Can you ___ your last name, please?"', answer: 'spell', hint: 'Hint: to say each letter of a word', phrase: 'Can you spell your last name, please?'},
    {sentence: '"My ___ name is Pires — P-I-R-E-S."', answer: 'last', hint: 'Hint: the family name that comes after your first name', phrase: 'My last name is Pires.'},
    {sentence: '"I am ___ , thank you. And you?"', answer: 'fine', hint: 'Hint: the standard polite answer to "How are you?"', phrase: 'I am fine, thank you. And you?'},
    {sentence: '"Nice to ___ you, Sarah."', answer: 'meet', hint: 'Hint: the verb you use when you see someone for the first time', phrase: 'Nice to meet you, Sarah.'},
  ],
  3: [
    {sentence: '"___ is my phone."', answer: 'This', hint: 'Hint: use this word for something near you', phrase: 'This is my phone.'},
    {sentence: '"___ is my school over there."', answer: 'That', hint: 'Hint: use this word for something far from you', phrase: 'That is my school over there.'},
    {sentence: '"___ are my new sneakers."', answer: 'These', hint: 'Hint: the plural of "this"', phrase: 'These are my new sneakers.'},
    {sentence: '"My best ___ is called Helena."', answer: 'friend', hint: 'Hint: a person you really like and trust', phrase: 'My best friend is called Helena.'},
    {sentence: '"My ___ has four people."', answer: 'family', hint: 'Hint: your parents and siblings together', phrase: 'My family has four people.'},
    {sentence: '"My ___ is in Vila Mariana."', answer: 'neighborhood', hint: 'Hint: the area of the city where you live', phrase: 'My neighborhood is in Vila Mariana.'},
  ],
  4: [
    {sentence: '"I ___ up at seven o\'clock."', answer: 'wake', hint: 'Hint: to stop sleeping in the morning', phrase: 'I wake up at seven o\'clock.'},
    {sentence: '"I have ___ before school."', answer: 'breakfast', hint: 'Hint: the first meal of the day', phrase: 'I have breakfast before school.'},
    {sentence: '"I ___ to school by metro."', answer: 'go', hint: 'Hint: to move from one place to another', phrase: 'I go to school by metro.'},
    {sentence: '"I ___ English every day."', answer: 'study', hint: 'Hint: to read and practice to learn something', phrase: 'I study English every day.'},
    {sentence: '"I ___ have breakfast — every single day."', answer: 'always', hint: 'Hint: 100 percent of the time', phrase: 'I always have breakfast.'},
    {sentence: '"I ___ skip class — never, ever."', answer: 'never', hint: 'Hint: 0 percent of the time', phrase: 'I never skip class.'},
  ],
  5: [
    {sentence: '"I ___ Gossip Girl — it is my favorite."', answer: 'love', hint: 'Hint: a strong word for liking something a lot', phrase: 'I love Gossip Girl.'},
    {sentence: '"I don\'t ___ horror movies — they scare me."', answer: 'like', hint: 'Hint: the verb for enjoying something a normal amount', phrase: "I don't like horror movies."},
    {sentence: '"I ___ Mondays — they are so boring."', answer: 'hate', hint: 'Hint: a strong word for not liking at all', phrase: 'I hate Mondays.'},
    {sentence: '"My favorite ___ is Friends."', answer: 'series', hint: 'Hint: a TV show with many episodes and seasons', phrase: 'My favorite series is Friends.'},
    {sentence: '"Blair is my favorite ___ in Gossip Girl."', answer: 'character', hint: 'Hint: a person inside a story or series', phrase: 'Blair is my favorite character in Gossip Girl.'},
    {sentence: '"I am ___ with Gilmore Girls — I watched it three times!"', answer: 'obsessed', hint: 'Hint: when you cannot stop thinking about something', phrase: 'I am obsessed with Gilmore Girls.'},
  ],
};

const multipleChoice = {
  1: [
    {q: 'You meet a French girl in Paris in 2027. The best way to start is:', options: ['"My is Gabriela."', '"Hi! My name is Gabriela. I am from Brazil."', '"Gabriela. Brazil. School."', '"I have 16 years."'], correct: 1},
    {q: 'Which sentence about your age is correct in English?', options: ['"I have 16 years."', '"I am 16 year."', '"I am 16 years old."', '"My age have 16."'], correct: 2},
  ],
  2: [
    {q: 'A hotel receptionist in Paris asks: "Can you spell your last name?" The best answer is:', options: ['"My last name is Pires."', '"P-I-R-E-S."', '"Pires is my family."', '"I do not spell, sorry."'], correct: 1},
    {q: 'Which is the correct response to "Nice to meet you"?', options: ['"Nice to meet you too."', '"Yes, please."', '"You\'re welcome."', '"I am fine."'], correct: 0},
  ],
  3: [
    {q: 'You point to your phone in your hand. The correct word is:', options: ['"That is my phone."', '"Those is my phone."', '"This is my phone."', '"These is my phone."'], correct: 2},
    {q: 'You point to two old photos far away on a shelf. The correct word is:', options: ['"This is my photos."', '"Those are my photos."', '"That is my photos."', '"These are my photos."'], correct: 1},
  ],
  4: [
    {q: 'Which sentence uses third person -s correctly?', options: ['"My sister wake up at six."', '"My sister wakes up at six."', '"My sister waking up at six."', '"My sister wake ups at six."'], correct: 1},
    {q: 'You skip breakfast 0% of the time. The best word is:', options: ['"I sometimes skip breakfast."', '"I always skip breakfast."', '"I never skip breakfast."', '"I usually skip breakfast."'], correct: 2},
  ],
  5: [
    {q: 'You watch Friends every single day and you cannot stop. The best sentence is:', options: ['"I don\'t like Friends."', '"I am obsessed with Friends."', '"I hate Friends."', '"Friends is okay."'], correct: 1},
    {q: 'Someone asks "Do you like horror movies?" You hate them. The best answer is:', options: ['"Yes, I like."', '"No, I don\'t like."', '"No, I don\'t like horror movies."', '"I am not horror movies."'], correct: 2},
  ],
};

const ordering = {
  1: {
    title: 'Put this self-introduction in order',
    items: [
      {order: 1, text: '"Hi! My name is Gabriela Pires."'},
      {order: 2, text: '"I am 16 years old, and I am from São Paulo, Brazil."'},
      {order: 3, text: '"I am a student at high school."'},
      {order: 4, text: '"My favorite hobby is watching series like Gossip Girl."'},
      {order: 5, text: '"My dream is to travel to France in 2027!"'},
    ],
  },
  2: {
    title: 'Put this hotel check-in dialogue in order',
    items: [
      {order: 1, text: '"Good evening! Can I have your name, please?"'},
      {order: 2, text: '"Good evening. My name is Gabriela Pires."'},
      {order: 3, text: '"Can you spell your last name?"'},
      {order: 4, text: '"Yes — P-I-R-E-S."'},
      {order: 5, text: '"Perfect. Welcome to Paris, Gabriela!"'},
    ],
  },
  3: {
    title: 'Put this "presenting my world" tour in order',
    items: [
      {order: 1, text: '"This is my school in São Paulo."'},
      {order: 2, text: '"That is my best friend Helena over there."'},
      {order: 3, text: '"These are my classmates in the picture."'},
      {order: 4, text: '"Those are my favorite books on the shelf."'},
      {order: 5, text: '"This is my world — I love it."'},
    ],
  },
  4: {
    title: 'Put this morning routine in order',
    items: [
      {order: 1, text: '"I wake up at seven o\'clock."'},
      {order: 2, text: '"I have breakfast with my family."'},
      {order: 3, text: '"I take the metro to school."'},
      {order: 4, text: '"I study and have classes until four."'},
      {order: 5, text: '"At night, I always watch a series before sleeping."'},
    ],
  },
  5: {
    title: 'Put this fan-talk in order',
    items: [
      {order: 1, text: '"My favorite series is Gossip Girl."'},
      {order: 2, text: '"I am obsessed with Blair Waldorf — she is so smart."'},
      {order: 3, text: '"I don\'t like Chuck Bass in season one — he is mean."'},
      {order: 4, text: '"I also love Friends because it makes me laugh."'},
      {order: 5, text: '"What about you? What do you like to watch?"'},
    ],
  },
};

const pronunciation = {
  1: [
    {phrase: 'Hi, my name is Gabriela. I am from São Paulo.', pt: 'Oi, meu nome é Gabriela. Sou de São Paulo.'},
    {phrase: 'I am 16 years old and I am a student.', pt: 'Tenho 16 anos e sou estudante.'},
    {phrase: 'My dream is to travel to France in 2027.', pt: 'Meu sonho é viajar para a França em 2027.'},
  ],
  2: [
    {phrase: 'Hello! Nice to meet you. My name is Gabriela.', pt: 'Olá! Prazer em conhecer. Meu nome é Gabriela.'},
    {phrase: 'My last name is Pires. P-I-R-E-S.', pt: 'Meu sobrenome é Pires. P-I-R-E-S.'},
    {phrase: 'How are you today? I am fine, thank you.', pt: 'Como você está hoje? Estou bem, obrigada.'},
  ],
  3: [
    {phrase: 'This is my phone and that is my school.', pt: 'Este é meu celular e aquela é minha escola.'},
    {phrase: 'These are my friends from school.', pt: 'Estes são meus amigos da escola.'},
    {phrase: 'My family lives in São Paulo, Brazil.', pt: 'Minha família mora em São Paulo, Brasil.'},
  ],
  4: [
    {phrase: 'I wake up at seven and I have breakfast.', pt: 'Eu acordo às sete e tomo café da manhã.'},
    {phrase: 'I always study English in the evening.', pt: 'Eu sempre estudo inglês à noite.'},
    {phrase: 'On weekdays, I never skip school.', pt: 'Em dias de semana, eu nunca falto à escola.'},
  ],
  5: [
    {phrase: 'I love Gossip Girl. Blair is my favorite character.', pt: 'Eu adoro Gossip Girl. Blair é meu personagem favorito.'},
    {phrase: 'I do not like horror movies. I prefer comedies.', pt: 'Eu não gosto de filmes de terror. Prefiro comédias.'},
    {phrase: 'I am obsessed with Friends. I have seen it many times.', pt: 'Sou obcecada por Friends. Já vi muitas vezes.'},
  ],
};

const thinkAboutIt = {
  1: {
    question: 'Imagine you are at the airport in Paris in February 2027. A French girl your age sits next to you and says: "Hi! Where are you from?" How would you answer? Record your answer — there is no right or wrong here.',
    suggestion: "Hi! I am Gabriela. I am from Brazil — from São Paulo. I am 16 years old and I am a student. This is my first time in France. What about you?",
    suggestionPt: 'Oi! Eu sou a Gabriela. Sou do Brasil — de São Paulo. Tenho 16 anos e sou estudante. É minha primeira vez na França. E você?',
  },
  2: {
    question: 'You arrive at a small hotel in Montmartre. The receptionist says: "Good evening! Welcome. Can I have your name?" How do you answer the full check-in conversation? Record everything you would say.',
    suggestion: "Good evening! My name is Gabriela Pires. P-I-R-E-S. I have a reservation. Nice to meet you.",
    suggestionPt: 'Boa noite! Meu nome é Gabriela Pires. P-I-R-E-S. Tenho uma reserva. Prazer em conhecer.',
  },
  3: {
    question: 'A French exchange student is visiting your school in São Paulo. Show her around for one minute — what is your school, your classroom, your favorite spot? Use this, that, these, those.',
    suggestion: "Hi! Welcome to my school. This is my classroom — these are my classmates. That is the cafeteria over there. Those are my friends from the music club. This is my favorite place — the library.",
    suggestionPt: 'Oi! Bem-vinda à minha escola. Esta é minha sala — estes são meus colegas. Aquela é a cantina ali. Aqueles são meus amigos do clube de música. Este é meu lugar favorito — a biblioteca.',
  },
  4: {
    question: 'A new friend in Paris asks: "What does a normal day in São Paulo look like for you?" Tell your full day — morning, afternoon, evening — with frequency adverbs.',
    suggestion: "I usually wake up at seven. I always have breakfast with my family. I go to school by metro. I study until four in the afternoon. I usually study English at home. At night, I always watch a series — usually Gossip Girl or Friends.",
    suggestionPt: 'Geralmente acordo às sete. Sempre tomo café com a família. Vou para a escola de metrô. Estudo até as quatro da tarde. Geralmente estudo inglês em casa. À noite, sempre assisto uma série — geralmente Gossip Girl ou Friends.',
  },
  5: {
    question: 'A French girl asks: "What series and music do you love? Tell me everything!" Talk about your top 3 favorites and why. Use love, like, hate, obsessed.',
    suggestion: "I am obsessed with Gossip Girl. I love Blair Waldorf because she is smart and stylish. I also love Friends — it is so funny. I do not like horror movies, but I love romantic comedies. What about you?",
    suggestionPt: 'Sou obcecada por Gossip Girl. Amo a Blair Waldorf porque ela é inteligente e estilosa. Também adoro Friends — é muito engraçada. Não gosto de filmes de terror, mas adoro comédias românticas. E você?',
  },
};

const survivalCards = {
  1: [
    {en: 'Hi! My name is Gabriela.', pt: 'Oi! Meu nome é Gabriela.'},
    {en: 'I am from São Paulo, Brazil.', pt: 'Sou de São Paulo, Brasil.'},
    {en: 'I am 16 years old.', pt: 'Tenho 16 anos.'},
    {en: 'I am a student.', pt: 'Sou estudante.'},
    {en: 'My dream is to visit France in 2027.', pt: 'Meu sonho é visitar a França em 2027.'},
  ],
  2: [
    {en: 'Hello! Nice to meet you.', pt: 'Olá! Prazer em conhecer.'},
    {en: 'How are you? — I am fine, thank you.', pt: 'Como você está? — Estou bem, obrigada.'},
    {en: 'My last name is Pires. P-I-R-E-S.', pt: 'Meu sobrenome é Pires. P-I-R-E-S.'},
    {en: 'Can you spell that, please?', pt: 'Pode soletrar, por favor?'},
    {en: 'Goodbye! Have a nice day.', pt: 'Tchau! Tenha um bom dia.'},
  ],
  3: [
    {en: 'This is my best friend.', pt: 'Esta é minha melhor amiga.'},
    {en: 'That is my school over there.', pt: 'Aquela é minha escola ali.'},
    {en: 'These are my classmates.', pt: 'Estes são meus colegas.'},
    {en: 'My family lives in São Paulo.', pt: 'Minha família mora em São Paulo.'},
    {en: 'My neighborhood is quiet and safe.', pt: 'Meu bairro é tranquilo e seguro.'},
  ],
  4: [
    {en: 'I wake up at seven o\'clock.', pt: 'Eu acordo às sete.'},
    {en: 'I always have breakfast.', pt: 'Eu sempre tomo café da manhã.'},
    {en: 'I go to school by metro.', pt: 'Vou para a escola de metrô.'},
    {en: 'I usually study English at night.', pt: 'Geralmente estudo inglês à noite.'},
    {en: 'I never skip class.', pt: 'Eu nunca falto à aula.'},
  ],
  5: [
    {en: 'I love Gossip Girl.', pt: 'Eu adoro Gossip Girl.'},
    {en: 'I don\'t like horror movies.', pt: 'Eu não gosto de filmes de terror.'},
    {en: 'I am obsessed with Friends.', pt: 'Sou obcecada por Friends.'},
    {en: 'My favorite character is Blair.', pt: 'Meu personagem favorito é a Blair.'},
    {en: 'What about you? What do you like?', pt: 'E você? Do que você gosta?'},
  ],
};

const grammarTips = {
  1: 'Verb to be + personal info: <strong>I am</strong> Gabriela. <strong>I am</strong> from São Paulo. <strong>I am</strong> 16 years old. (Em inglês usamos "I am" com idade — não "I have", como em português.)',
  2: 'Greeting + spelling: para soletrar em inglês, dizemos cada letra com pronúncia americana. <strong>P-I-R-E-S</strong> em inglês: "pee-eye-arr-ee-ess". Praticar o alfabeto é essencial para hotéis e aeroportos.',
  3: 'Demonstrativos: <strong>this</strong> (perto, singular), <strong>that</strong> (longe, singular), <strong>these</strong> (perto, plural), <strong>those</strong> (longe, plural). Em português é mais flexível — em inglês a regra é fixa.',
  4: 'Present simple — terceira pessoa: na 3ª pessoa singular (he/she/it), o verbo ganha um <strong>-s</strong>: <em>She wake<strong>s</strong> up early. He watch<strong>es</strong> Gossip Girl.</em>',
  5: 'Like / love / hate + noun ou + verb-ing: <em>I love series. I love watching series. I don\'t like horror movies.</em> Para perguntar: <em>Do you like…?</em> Resposta: <em>Yes, I do / No, I don\'t.</em>',
};

const lessonObjectives = {
  1: 'Ao final desta aula, Gabriela será capaz de se apresentar em inglês — nome, idade, cidade, escola, hobby e sonho — em uma fala de 30 a 60 segundos com confiança.',
  2: 'Ao final desta aula, Gabriela será capaz de cumprimentar, soletrar nome e sobrenome e fazer um check-in de hotel simulado em inglês.',
  3: 'Ao final desta aula, Gabriela será capaz de descrever pessoas, lugares e objetos do seu dia a dia usando this/that/these/those + artigos.',
  4: 'Ao final desta aula, Gabriela será capaz de descrever sua rotina diária em inglês com 8 a 10 frases usando present simple e advérbios de frequência.',
  5: 'Ao final desta aula, Gabriela será capaz de expressar gostos, desgostos e opiniões sobre séries e celebridades em inglês com 5 a 8 frases.',
};

const homework = {
  1: [
    'Grave um áudio de 60 segundos em inglês: nome, idade, cidade, escola, 2 hobbies e uma frase sobre o sonho da viagem para a França.',
    'Escreva seu "My Profile Card" no caderno: Name / Age / City / School / Hobbies / Dream Trip / Favorite Series.',
    'Assista os primeiros 5 minutos de Friends S01E01 com legendas em inglês. Anote 3 palavras ou frases que você entendeu.',
  ],
  2: [
    'Pratique soletrar em inglês: seu nome completo, o nome da sua melhor amiga e o nome do seu café favorito em São Paulo. Grave um áudio.',
    'Escreva 8 frases usando "to be": 4 sobre você, 2 sobre um personagem de Friends, 2 frases negativas.',
    'Assista um vídeo no YouTube: "English Alphabet Pronunciation" (versão americana, ~5 min). Anote as 3 letras que mais soam diferentes do português.',
  ],
  3: [
    'Tire 5 fotos do seu dia em São Paulo (sala, mochila, escola, almoço…) e escreva 1 frase em inglês para cada usando "this is" ou "these are".',
    'Escreva 10 frases no caderno — 5 afirmativas, 3 negativas, 2 perguntas — com to be + demonstrativos + artigos.',
    'Assista uma cena de Gossip Girl (S01) e conte quantas vezes ouve "this" ou "that". Anote o número.',
  ],
  4: [
    'Escreva sua rotina completa em inglês — 10 frases, misturando sempre/geralmente/às vezes/nunca. Inclua manhã, tarde e noite.',
    'Grave um áudio de 90 segundos: "This is my day in São Paulo." Descreva sua rotina como se estivesse contando para uma amiga estrangeira.',
    'Assista a primeira cena de café da manhã de Gilmore Girls. Anote 3 verbos de rotina em inglês que você ouviu.',
  ],
  5: [
    'Escreva sua "My Favorites List" em inglês: série favorita (3 frases), filme favorito (3 frases), celebridade favorita (3 frases).',
    'Grave um áudio de 60 segundos: "My top 3 favorite series and why." Fala natural, sem ler.',
    'Assista 10 minutos de Friends com legenda em inglês. Conte quantas vezes ouve "I like", "I love" ou "I don\'t like". Escreva as frases.',
  ],
};

const ccqs = {
  1: [
    {q: 'Em "I am 16 years old", usamos to BE ou to HAVE?', a: 'To be — em inglês não dizemos "I have 16 years".'},
    {q: 'Quando alguém diz "I am from São Paulo", está falando do passado ou do presente?', a: 'Do presente — "from" indica origem, sempre presente.'},
    {q: 'É correto dizer "My name Gabriela" sem o "is"?', a: 'Não. To be é obrigatório: "My name IS Gabriela".'},
    {q: '"Dream" é um sonho enquanto se dorme ou um objetivo de vida?', a: 'Pode ser os dois — em "My dream is to visit Paris" é objetivo.'},
    {q: 'Após "I am a", qual a próxima palavra esperada?', a: 'Substantivo (student, teacher, fan…).'},
  ],
  2: [
    {q: 'Em "Nice to meet you", quando se usa essa frase?', a: 'Apenas no primeiro encontro com a pessoa — não em todos os encontros.'},
    {q: 'Para soletrar a letra "I" em inglês, dizemos /ai/ ou /i/?', a: '/ai/ — como em "eye". Cuidado, é diferente do português.'},
    {q: 'Qual a diferença entre "first name" e "last name"?', a: 'First name = primeiro nome. Last name = sobrenome.'},
    {q: 'Quando alguém pergunta "How are you?" no contexto de cumprimento, queremos uma resposta longa?', a: 'Não — é cumprimento. Resposta curta: "Fine, thank you."'},
    {q: 'Em "Good evening", em que parte do dia se usa?', a: 'Da noitinha em diante (depois das 18h, mais ou menos).'},
  ],
  3: [
    {q: 'Vou apontar para meu próprio celular na minha mão. Uso "this" ou "that"?', a: 'This — está perto, comigo.'},
    {q: 'Vou falar dos meus colegas que estão na minha frente. Uso "these" ou "those"?', a: 'These — estão perto, plural.'},
    {q: 'Em "She is my friend", trocamos "She" por "He" se a pessoa for…?', a: 'Homem.'},
    {q: 'Por que dizemos "a student" e não "an student"?', a: 'Porque "student" começa com som de consoante (/st/).'},
    {q: 'Quando uso "the" e quando uso "a/an"?', a: '"The" para algo específico/já mencionado; "a/an" para a primeira menção, indefinido.'},
  ],
  4: [
    {q: 'Em "She wakes up", por que tem o "s" em "wakes"?', a: 'Porque é 3ª pessoa singular (he/she/it) no present simple.'},
    {q: 'Qual é a ordem de frequência: always, usually, sometimes, never?', a: 'Always (100%) > usually (80%) > sometimes (50%) > never (0%).'},
    {q: 'Em "I never skip class", preciso de "do not"?', a: 'Não — "never" já é negativo. Não se diz "I do not never skip".'},
    {q: 'Onde colocamos os advérbios de frequência (always/usually/never)?', a: 'Antes do verbo principal: "I always have breakfast".'},
    {q: 'Em "On weekdays, I study", "weekdays" significa…?', a: 'Dias de semana (segunda a sexta).'},
  ],
  5: [
    {q: 'Qual é a diferença entre "I like" e "I love"?', a: '"Love" é mais forte que "like". "Hate" é o oposto de "love".'},
    {q: 'Após "like" ou "love", uso "to + verb" ou "verb-ing"?', a: 'Os dois funcionam, mas "verb-ing" é mais comum: "I like watching".'},
    {q: 'Em "I don\'t like horror movies", por que tem "don\'t"?', a: 'Porque é negativo: "do not" → "don\'t".'},
    {q: 'A palavra "obsessed" significa gostar pouco ou muito?', a: 'Muito — é gostar a ponto de não conseguir parar de pensar.'},
    {q: 'Qual a diferença entre "character" e "celebrity"?', a: 'Character = personagem (na ficção). Celebrity = celebridade real.'},
  ],
};

const obstacles = {
  1: [
    {label: 'Idade com "have"', text: 'Gabriela vai dizer "I have 16 years" — interferência do português. Corrigir imediatamente: "In English we say I AM 16 years old. We use BE, not HAVE."'},
    {label: 'Falta de "I am"', text: '"I student" sem o "am". Drilling: "I AM a student" — sempre o to be antes do substantivo.'},
    {label: 'Pronúncia de "from"', text: 'Pode dizer "ehfrom" ou "fróm" forte. O som correto é /frəm/ (schwa fraco).'},
    {label: 'Trocar PT no meio', text: 'Quando travar, vai puxar para o português. Pedir: "Try just one word in English. Even one word."'},
  ],
  2: [
    {label: 'Letra "I"', text: 'Em português "I" soa /i/. Em inglês é /ai/ — drilling extensivo: "P-I-R-E-S = pee-eye-arr-ee-ess".'},
    {label: 'Letras E vs I', text: 'E = /ee/, I = /ai/. São facilmente confundidas. Usar pares mínimos: "B-E-E" vs "B-I-G".'},
    {label: 'Letra "G"', text: 'Em português é /jê/, em inglês é /jee/. Letra "J" em inglês é /jay/. Drilling especial.'},
    {label: '"How are you" como pergunta literal', text: 'Pode tentar dar resposta longa explicando como está. Ensinar: cumprimento ritual, resposta curta basta.'},
  ],
  3: [
    {label: 'Confusão this/that', text: 'Em português "este/esse" é flexível. Em inglês this = perto, that = longe — regra firme. Usar gestos físicos.'},
    {label: 'Plural de "this"', text: 'Pode dizer "thises" ou repetir "this". Plural correto = "these". Drill com objetos físicos.'},
    {label: 'Artigo + país', text: 'Pode dizer "the Brazil". Em inglês: just "Brazil" (sem artigo). Mas "the United States" tem.'},
    {label: '"My family are"', text: 'Pode usar "are" pluralizando. Em American English: "My family IS" (singular coletivo).'},
  ],
  4: [
    {label: 'Esquecer o -s na 3ª pessoa', text: 'Vai dizer "She wake up" sem -s. Drilling: "She wake-S, he study-IES". Apontar para o -s no quadro.'},
    {label: 'Posição do advérbio', text: 'Pode dizer "I have always breakfast". Correto: "I always have breakfast" (advérbio antes do verbo).'},
    {label: 'Pronúncia de "wake"', text: 'Som /weik/. Pode falar "uake" ou "uéik" forte. Drilling com pares: wake/take/make.'},
    {label: 'Tradução de "café da manhã"', text: '"Coffee of the morning" — não. É "breakfast" — palavra única. Drillar como chunk.'},
  ],
  5: [
    {label: '"I am like"', text: 'Pode dizer "I am like horror movies" (interferência). Correto: "I LIKE horror movies" — like é verbo, não adjetivo.'},
    {label: 'Negativa', text: '"I no like" → corrigir para "I don\'t like". DON\'T sempre antes do verbo no negativo.'},
    {label: 'Pronúncia de "obsessed"', text: '/əb-SEST/ — três sílabas, stress no meio. Não /ob-ses-sé-do/.'},
    {label: '"Do you like…?" sem auxiliar', text: 'Pode perguntar "You like Friends?" sem "do". Drill: "DO YOU like…?" sempre com "do".'},
  ],
};

const dialogues = {
  1: {
    title: 'Meeting Sarah at the airport in Paris (Feb 2027)',
    context: 'Gabriela meets a French girl her age at Charles de Gaulle airport. They are waiting at the baggage claim.',
    lines: [
      {speaker: 'SAR', name: 'Sarah — French student', side: 'staff', text: 'Hi there! Are you from Brazil? I see your bag.'},
      {speaker: 'GAB', name: 'Gabriela', side: 'you', text: 'Hi! Yes, I am from Brazil. My name is Gabriela. What is your name?'},
      {speaker: 'SAR', name: 'Sarah', side: 'staff', text: 'Nice to meet you, Gabriela. I am Sarah. I am from Lyon, France. How old are you?'},
      {speaker: 'GAB', name: 'Gabriela', side: 'you', text: 'I am 16 years old. I am a student. This is my first time in France.'},
      {speaker: 'SAR', name: 'Sarah', side: 'staff', text: 'Wow, welcome! Why did you come to France?'},
      {speaker: 'GAB', name: 'Gabriela', side: 'you', text: 'My dream is to travel and learn English. I love series and Paris!'},
      {speaker: 'SAR', name: 'Sarah', side: 'staff', text: 'That is so cool. I love series too. We are going to be great friends!'},
    ],
  },
  2: {
    title: 'Hotel check-in in Montmartre',
    context: 'Gabriela arrives at a small hotel in Paris. She speaks to the receptionist.',
    lines: [
      {speaker: 'REC', name: 'Receptionist', side: 'staff', text: 'Good evening! Welcome to Hotel Montmartre. Can I have your name, please?'},
      {speaker: 'GAB', name: 'Gabriela', side: 'you', text: 'Good evening. My name is Gabriela Pires. I have a reservation.'},
      {speaker: 'REC', name: 'Receptionist', side: 'staff', text: 'Pires. Can you spell your last name for me?'},
      {speaker: 'GAB', name: 'Gabriela', side: 'you', text: 'Yes — P-I-R-E-S. Pires.'},
      {speaker: 'REC', name: 'Receptionist', side: 'staff', text: 'Perfect. And how do you spell your first name? Gabriela.'},
      {speaker: 'GAB', name: 'Gabriela', side: 'you', text: 'G-A-B-R-I-E-L-A. Gabriela.'},
      {speaker: 'REC', name: 'Receptionist', side: 'staff', text: 'Wonderful. Welcome to Paris, Gabriela! How are you today?'},
      {speaker: 'GAB', name: 'Gabriela', side: 'you', text: 'I am fine, thank you. A little tired, but very happy. Goodbye!'},
    ],
  },
  3: {
    title: 'Showing my world to a French exchange student',
    context: 'Gabriela gives a tour of her school in São Paulo to her new French friend Sarah.',
    lines: [
      {speaker: 'GAB', name: 'Gabriela', side: 'you', text: 'Welcome to my school, Sarah! This is the main entrance.'},
      {speaker: 'SAR', name: 'Sarah', side: 'staff', text: 'It is beautiful! And what is that big building over there?'},
      {speaker: 'GAB', name: 'Gabriela', side: 'you', text: 'That is the gym. We have classes there twice a week. These are my classmates from history class.'},
      {speaker: 'SAR', name: 'Sarah', side: 'staff', text: 'Nice to meet you all! And what about those students in red shirts?'},
      {speaker: 'GAB', name: 'Gabriela', side: 'you', text: 'Those are my friends from the music club. This is my best friend, Helena.'},
      {speaker: 'SAR', name: 'Sarah', side: 'staff', text: 'Hi Helena! Gabriela, where is your favorite place at school?'},
      {speaker: 'GAB', name: 'Gabriela', side: 'you', text: 'Come this way! This is the library. I love it. I always study here after class.'},
    ],
  },
  4: {
    title: 'A normal day in São Paulo',
    context: 'Sarah, the French friend, asks Gabriela about her daily routine on a video call.',
    lines: [
      {speaker: 'SAR', name: 'Sarah', side: 'staff', text: 'Tell me, Gabriela, what does your day look like?'},
      {speaker: 'GAB', name: 'Gabriela', side: 'you', text: 'I usually wake up at seven. I always have breakfast with my family — coffee and bread.'},
      {speaker: 'SAR', name: 'Sarah', side: 'staff', text: 'Coffee at seven? Wow! And then?'},
      {speaker: 'GAB', name: 'Gabriela', side: 'you', text: 'Then I go to school by metro. I have classes from eight to four. I usually study with Helena.'},
      {speaker: 'SAR', name: 'Sarah', side: 'staff', text: 'And in the afternoon?'},
      {speaker: 'GAB', name: 'Gabriela', side: 'you', text: 'I get home around five. I sometimes go to the park. I always do my homework.'},
      {speaker: 'SAR', name: 'Sarah', side: 'staff', text: 'And the evening? Do you watch series?'},
      {speaker: 'GAB', name: 'Gabriela', side: 'you', text: 'Of course! I always watch a series before sleeping. I never go to bed without one episode.'},
    ],
  },
  5: {
    title: 'Talking about favorites with Sarah',
    context: 'Sarah and Gabriela compare their favorite series and celebrities on a video call.',
    lines: [
      {speaker: 'SAR', name: 'Sarah', side: 'staff', text: 'Gabriela, what is your favorite series? Tell me everything!'},
      {speaker: 'GAB', name: 'Gabriela', side: 'you', text: 'Oh, easy! I love Gossip Girl. I am obsessed with Blair Waldorf.'},
      {speaker: 'SAR', name: 'Sarah', side: 'staff', text: 'Blair! Why Blair?'},
      {speaker: 'GAB', name: 'Gabriela', side: 'you', text: 'She is so smart and stylish. I love her style. I do not like Chuck in season one — he is mean.'},
      {speaker: 'SAR', name: 'Sarah', side: 'staff', text: 'I agree! What about other series?'},
      {speaker: 'GAB', name: 'Gabriela', side: 'you', text: 'I also love Friends because it makes me laugh. I hate horror movies. They scare me too much.'},
      {speaker: 'SAR', name: 'Sarah', side: 'staff', text: 'Same for me! Do you like French series?'},
      {speaker: 'GAB', name: 'Gabriela', side: 'you', text: 'Yes, I want to watch more. What do you recommend?'},
    ],
  },
};

const oralDrills = {
  1: [
    {pt: '"Diga seu nome em inglês."', en: '"My name is Gabriela."'},
    {pt: '"Diga sua idade."', en: '"I am 16 years old."'},
    {pt: '"Diga sua cidade."', en: '"I am from São Paulo."'},
    {pt: '"Diga sua profissão atual."', en: '"I am a student."'},
    {pt: '"Diga seu hobby favorito."', en: '"My favorite hobby is watching series."'},
    {pt: '"Diga seu sonho."', en: '"My dream is to visit France."'},
    {pt: '"Diga sua série favorita."', en: '"My favorite series is Gossip Girl."'},
    {pt: '"Faça sua apresentação completa em 30 segundos."', en: '"Hi! My name is Gabriela. I am 16 and I am from São Paulo. My dream is Paris."'},
  ],
  2: [
    {pt: '"Cumprimente alguém de manhã."', en: '"Good morning! How are you?"'},
    {pt: '"Diga que prazer em conhecer."', en: '"Nice to meet you."'},
    {pt: '"Pergunte como soletra o nome."', en: '"How do you spell your name?"'},
    {pt: '"Soletre seu sobrenome."', en: '"P-I-R-E-S."'},
    {pt: '"Responda como você está."', en: '"I am fine, thank you."'},
    {pt: '"Pergunte como soletra (educadamente)."', en: '"Can you spell that, please?"'},
    {pt: '"Diga tchau educadamente."', en: '"Goodbye! Have a nice day."'},
    {pt: '"Apresente-se com sobrenome para um recepcionista."', en: '"Good evening. My name is Gabriela Pires. P-I-R-E-S."'},
  ],
  3: [
    {pt: '"Aponte para seu celular."', en: '"This is my phone."'},
    {pt: '"Aponte para um prédio longe."', en: '"That is the school over there."'},
    {pt: '"Mostre seus tênis novos."', en: '"These are my new sneakers."'},
    {pt: '"Mostre fotos antigas longe."', en: '"Those are my old photos."'},
    {pt: '"Apresente sua melhor amiga."', en: '"This is my best friend, Helena."'},
    {pt: '"Diga onde sua família mora."', en: '"My family lives in São Paulo."'},
    {pt: '"Diga onde fica sua escola."', en: '"My school is on Paulista Avenue."'},
    {pt: '"Descreva seu bairro."', en: '"My neighborhood is quiet and safe."'},
  ],
  4: [
    {pt: '"Diga a hora que você acorda."', en: '"I wake up at seven o\'clock."'},
    {pt: '"Diga o que você toma de café."', en: '"I always have breakfast with my family."'},
    {pt: '"Diga como vai para a escola."', en: '"I go to school by metro."'},
    {pt: '"Diga uma matéria que estuda diariamente."', en: '"I study English every day."'},
    {pt: '"Diga o que você faz no fim da tarde."', en: '"I usually do my homework after class."'},
    {pt: '"Diga uma série que assiste à noite."', en: '"I watch Gossip Girl at night."'},
    {pt: '"Diga algo que NUNCA faz."', en: '"I never skip school."'},
    {pt: '"Faça um resumo de 5 frases do seu dia."', en: '"I wake up at seven. I have breakfast. I go to school. I study. I watch series."'},
  ],
  5: [
    {pt: '"Diga sua série favorita."', en: '"My favorite series is Gossip Girl."'},
    {pt: '"Diga um personagem que você ama."', en: '"I love Blair Waldorf."'},
    {pt: '"Diga algo que NÃO gosta."', en: '"I do not like horror movies."'},
    {pt: '"Diga algo que você ODEIA."', en: '"I hate Mondays."'},
    {pt: '"Diga uma série pela qual é obcecada."', en: '"I am obsessed with Friends."'},
    {pt: '"Pergunte se a pessoa gosta de algo."', en: '"Do you like Gossip Girl?"'},
    {pt: '"Responda negativamente uma pergunta."', en: '"No, I do not like horror movies."'},
    {pt: '"Faça um top 3 dos seus favoritos."', en: '"My top three are Gossip Girl, Friends, and Gilmore Girls."'},
  ],
};

const errorCorrection = {
  1: [
    {wrong: '"I have 16 years."', right: '"I am 16 years old."'},
    {wrong: '"My name Gabriela."', right: '"My name is Gabriela."'},
    {wrong: '"I student in school."', right: '"I am a student at high school."'},
    {wrong: '"I from Brazil."', right: '"I am from Brazil."'},
    {wrong: '"My dream visit France."', right: '"My dream is to visit France."'},
  ],
  2: [
    {wrong: '"Good morning, my name Gabriela."', right: '"Good morning, my name is Gabriela."'},
    {wrong: '"Nice meet you."', right: '"Nice to meet you."'},
    {wrong: '"How are you? — Fine."', right: '"How are you? — I am fine, thank you."'},
    {wrong: '"My last name is Pires. P-I-R-E-S." (lendo letra por letra em português)', right: '"P-I-R-E-S" pronunciado "pee-eye-arr-ee-ess".'},
    {wrong: '"You can spell?"', right: '"Can you spell that, please?"'},
  ],
  3: [
    {wrong: '"This is my friends."', right: '"These are my friends."'},
    {wrong: '"That are my classmates over there."', right: '"Those are my classmates over there."'},
    {wrong: '"My family are big."', right: '"My family is big."'},
    {wrong: '"I work in a Centauro."', right: '"I work at Centauro." (não, em geral: artigo correto)'},
    {wrong: '"I live in the Brazil."', right: '"I live in Brazil."'},
  ],
  4: [
    {wrong: '"My sister wake up early."', right: '"My sister wakes up early."'},
    {wrong: '"I have always breakfast."', right: '"I always have breakfast."'},
    {wrong: '"I no skip class."', right: '"I never skip class."'},
    {wrong: '"She study English on weekends."', right: '"She studies English on weekends."'},
    {wrong: '"I go school by metro."', right: '"I go to school by metro."'},
  ],
  5: [
    {wrong: '"I am like Friends."', right: '"I like Friends."'},
    {wrong: '"I no like horror movies."', right: '"I do not like horror movies."'},
    {wrong: '"My favorite serie is Gossip Girl."', right: '"My favorite series is Gossip Girl."'},
    {wrong: '"You like Friends?"', right: '"Do you like Friends?"'},
    {wrong: '"I am obsess Friends."', right: '"I am obsessed with Friends."'},
  ],
};

const productionScenarios = {
  1: [
    {label: 'Stage 1 — Guided', text: 'Gabriela lê o modelo da apresentação na tela e preenche com seus dados. Professor corrige em tempo real. Repetir 2x até fluir.'},
    {label: 'Stage 2 — Semi-free', text: 'Sem o modelo. Apenas palavras-chave: name, age, city, school, hobby, dream, favorite. Gabriela produz sua apresentação. Notar erros para feedback final.'},
    {label: 'Stage 3 — Free role-play', text: 'Simulação completa: professor faz "Sarah, French girl at the airport in Paris". Aperto de mão, troca de apresentações, 3 minutos de conversa natural. Feedback retardado depois — 3 positivos, 2 melhorias.'},
  ],
  2: [
    {label: 'Stage 1 — Guided', text: 'Cenário: aeroporto de check-in. Professor é o atendente. Lê linha por linha do diálogo modelo, Gabriela responde com scaffolding visual.'},
    {label: 'Stage 2 — Semi-free', text: 'Cenário: hotel em Paris. Sem o modelo. Gabriela conduz o check-in completo, soletrando nome e sobrenome. 5 trocas mínimo.'},
    {label: 'Stage 3 — Free role-play', text: 'Cenário: cafeteria em Paris. Gabriela cumprimenta, se apresenta, soletra o nome para reservar a mesa, pergunta como a pessoa se chama, soletra de volta. Despedida natural.'},
  ],
  3: [
    {label: 'Stage 1 — Guided', text: 'Cenário: visita de Sarah à escola de Gabriela. Diálogo modelo na tela. Gabriela lê suas falas com scaffolding visual.'},
    {label: 'Stage 2 — Semi-free', text: 'Cenário: tour pelo bairro de Gabriela. Sem modelo. Apenas pistas: school, friends, neighborhood, family, favorite place.'},
    {label: 'Stage 3 — Free role-play', text: 'Cenário: Gabriela mostra fotos do celular de "this/that/these/those" para uma amiga estrangeira. 4 fotos, 4 frases mínimo, com perguntas e respostas.'},
  ],
  4: [
    {label: 'Stage 1 — Guided', text: 'Gabriela narra sua manhã (wake up → breakfast → school) com timeline visual na tela. Professor sopra advérbios.'},
    {label: 'Stage 2 — Semi-free', text: 'Sem timeline. Apenas relógios marcando 7h, 12h, 18h, 22h. Gabriela narra o dia inteiro.'},
    {label: 'Stage 3 — Free role-play', text: 'Sarah liga em videocall e pergunta: "What does your day look like?" Gabriela conta o dia inteiro. Sarah faz 3 follow-up questions.'},
  ],
  5: [
    {label: 'Stage 1 — Guided', text: 'Gabriela faz reações rápidas: professor mostra capa de série/filme, Gabriela reage com "I love…" / "I hate…" / "I am obsessed with…".'},
    {label: 'Stage 2 — Semi-free', text: 'Sem imagens. Gabriela lista TOP 3 séries favoritas e justifica cada uma com 2 frases.'},
    {label: 'Stage 3 — Free role-play', text: 'Cenário: Gabriela conhece outra fã de séries em Paris. Conversa de 3 minutos sobre séries, personagens favoritos, opiniões fortes. Pergunta de volta: "What about you?"'},
  ],
};

const checklistItems = {
  1: [
    'Sei me apresentar com nome, idade, cidade e escola.',
    'Sei usar o verbo to be (I am) com idade e origem.',
    'Sei contar meu hobby e meu sonho da viagem.',
    'Já fiz role-play com a "Sarah em Paris".',
    'Gravei meu áudio baseline de 60 segundos.',
    'Sei dizer "I am a student" sem esquecer o "am".',
    'Já entendo que em inglês uso "I AM 16", não "I have 16".',
    'Homework assigned e entendido.',
  ],
  2: [
    'Sei cumprimentar com Hello / Good morning / Good evening.',
    'Sei soletrar meu nome e sobrenome em inglês.',
    'Já conheço as letras que mais confundem (E, I, G, J, R).',
    'Sei dizer "Nice to meet you" e "How are you, fine thank you".',
    'Fiz check-in de hotel completo em inglês.',
    'Sei dizer "Goodbye" e "Have a nice day".',
    'Sei que letra "I" em inglês é /ai/, não /i/.',
    'Homework assigned e entendido.',
  ],
  3: [
    'Sei usar this / that / these / those corretamente.',
    'Sei apresentar pessoas, lugares e objetos do meu dia.',
    'Sei usar artigos a / an / the no básico.',
    'Sei o plural de this (these) e of that (those).',
    'Fiz tour da minha escola em inglês.',
    'Sei dizer "My family lives in São Paulo" sem "the Brazil".',
    'Sei diferenciar "this is my friend" de "that is the school over there".',
    'Homework assigned e entendido.',
  ],
  4: [
    'Sei descrever minha rotina manhã, tarde e noite em inglês.',
    'Sei usar always, usually, sometimes, never.',
    'Sei colocar -s no verbo na 3ª pessoa singular.',
    'Sei posicionar advérbio antes do verbo principal.',
    'Já contei meu dia inteiro em inglês para alguém.',
    'Sei dizer "I go TO school by metro" — com "to".',
    'Sei dizer "She wakeS up", "He studieS" — com -s.',
    'Homework assigned e entendido.',
  ],
  5: [
    'Sei usar love, like, don\'t like, hate.',
    'Sei dizer "I am obsessed with…" para coisas que amo demais.',
    'Sei perguntar "Do you like…?" e responder "Yes, I do / No, I don\'t".',
    'Já falei das minhas séries favoritas em inglês para alguém.',
    'Sei diferenciar character (personagem) de celebrity (celebridade).',
    'Sei dizer "I LIKE" sem "I AM LIKE" (interferência do PT).',
    'Sei usar -ing depois de like/love (I like watching…).',
    'Homework assigned e entendido.',
  ],
};

module.exports = {
  studentInfo, lessonTitles, lessonPromises, lessonImages, lessonHeaderImages, stampImages, stampLabels,
  vocab, matching, fillIn, multipleChoice, ordering, pronunciation, thinkAboutIt, survivalCards,
  grammarTips, lessonObjectives, homework, ccqs, obstacles, dialogues, oralDrills, errorCorrection,
  productionScenarios, checklistItems,
};
