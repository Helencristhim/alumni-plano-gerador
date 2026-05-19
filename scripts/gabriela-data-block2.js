// Gabriela Pires — dados do Bloco 2 (Aulas 21-25)
// Tema: futuro, aeroporto, voo, milestone, séries

const lessonPromises = {
  21: 'Depois desta aula, você projeta seu futuro em inglês — o que VAI acontecer em 2027 e o que você promete fazer.',
  22: 'Depois desta aula, você atravessa um aeroporto inteiro em Paris sem travar — check-in, segurança, embarque.',
  23: 'Depois desta aula, você sobrevive ao voo, à imigração e ao primeiro contato real com Paris em inglês.',
  24: 'Depois desta aula, você comprova: comparando hoje com a Aula 1, sabe quem virou — e o que ainda falta.',
  25: 'Depois desta aula, você defende sua série favorita com argumento, opinião e personagens descritos como crítica de TV.',
};

const lessonImages = {
  21: 'https://images.unsplash.com/photo-1523287562758-66c7fc58967f?w=1200&q=80',
  22: 'https://images.unsplash.com/photo-1436491865332-7a61a109cc05?w=1200&q=80',
  23: 'https://images.unsplash.com/photo-1503614472-8c93d56e92ce?w=1200&q=80',
  24: 'https://images.unsplash.com/photo-1521295121783-8a321d551ad2?w=1200&q=80',
  25: 'https://images.unsplash.com/photo-1522869635100-9f4c5e86aa37?w=1200&q=80',
};

const lessonHeaderImages = {
  21: 'https://images.unsplash.com/photo-1523287562758-66c7fc58967f?w=600&q=80',
  22: 'https://images.unsplash.com/photo-1436491865332-7a61a109cc05?w=600&q=80',
  23: 'https://images.unsplash.com/photo-1503614472-8c93d56e92ce?w=600&q=80',
  24: 'https://images.unsplash.com/photo-1521295121783-8a321d551ad2?w=600&q=80',
  25: 'https://images.unsplash.com/photo-1522869635100-9f4c5e86aa37?w=600&q=80',
};

const stampImages = {
  21: 'https://images.unsplash.com/photo-1523287562758-66c7fc58967f?w=200&q=80',
  22: 'https://images.unsplash.com/photo-1436491865332-7a61a109cc05?w=200&q=80',
  23: 'https://images.unsplash.com/photo-1503614472-8c93d56e92ce?w=200&q=80',
  24: 'https://images.unsplash.com/photo-1521295121783-8a321d551ad2?w=200&q=80',
  25: 'https://images.unsplash.com/photo-1522869635100-9f4c5e86aa37?w=200&q=80',
};

const stampLabels = {21: 'Future', 22: 'Airport', 23: 'Flight', 24: 'Halfway', 25: 'Series'};

const vocab = {
  21: [
    {word: 'will', pt: 'vai (futuro/promessa/decisão)', exA: '"I will study English every day."', exB: '"She will visit Paris in 2027."'},
    {word: "won't", pt: 'não vai (futuro negativo)', exA: '"I won\'t forget my passport."', exB: '"He won\'t miss the flight."'},
    {word: 'probably', pt: 'provavelmente', exA: '"It will probably rain in Paris."', exB: '"She probably won\'t answer."'},
    {word: 'maybe', pt: 'talvez', exA: '"Maybe I will live in France one day."', exB: '"Maybe she will join us."'},
    {word: 'definitely', pt: 'com certeza', exA: '"I will definitely visit the Louvre."', exB: '"She will definitely love the croissants."'},
    {word: 'I think', pt: 'eu acho (que)', exA: '"I think it will be amazing."', exB: '"I think she will say yes."'},
    {word: 'I hope', pt: 'eu espero', exA: '"I hope I will be fluent by 2027."', exB: '"I hope it will not be too cold."'},
    {word: 'I promise', pt: 'eu prometo', exA: '"I promise I will practice every day."', exB: '"I promise I won\'t be late."'},
    {word: 'exchange program', pt: 'programa de intercâmbio', exA: '"Maybe I will join an exchange program."', exB: '"The exchange program starts in September."'},
    {word: 'gap year', pt: 'ano sabático', exA: '"I might take a gap year after high school."', exB: '"A gap year sounds amazing."'},
  ],
  22: [
    {word: 'passport', pt: 'passaporte', exA: '"My passport is in my carry-on bag."', exB: '"May I see your passport, please?"'},
    {word: 'boarding pass', pt: 'cartão de embarque', exA: '"Here is my boarding pass."', exB: '"Please have your boarding pass ready."'},
    {word: 'check-in counter', pt: 'balcão de check-in', exA: '"The check-in counter is over there."', exB: '"Could you tell me where the check-in counter is?"'},
    {word: 'carry-on luggage', pt: 'bagagem de mão', exA: '"This is my carry-on luggage."', exB: '"Each passenger has one carry-on bag."'},
    {word: 'gate', pt: 'portão de embarque', exA: '"My flight leaves from gate B12."', exB: '"Where is gate 24, please?"'},
    {word: 'security checkpoint', pt: 'controle de segurança', exA: '"The security checkpoint is on the second floor."', exB: '"Please remove your shoes at the security checkpoint."'},
    {word: 'flight attendant', pt: 'comissário de bordo', exA: '"Could you ask the flight attendant?"', exB: '"The flight attendant brought us water."'},
    {word: 'delay', pt: 'atraso', exA: '"My flight has a one-hour delay."', exB: '"The delay was caused by bad weather."'},
    {word: 'window seat', pt: 'assento na janela', exA: '"I prefer a window seat."', exB: '"Could I have a window seat, please?"'},
    {word: 'aisle seat', pt: 'assento no corredor', exA: '"I would like an aisle seat."', exB: '"My grandmother always picks the aisle seat."'},
  ],
  23: [
    {word: 'turbulence', pt: 'turbulência', exA: '"The turbulence was a little scary."', exB: '"Please return to your seat during turbulence."'},
    {word: 'tray table', pt: 'mesa do avião', exA: '"Please put your tray table up."', exB: '"My tray table is broken."'},
    {word: 'recline', pt: 'reclinar', exA: '"Could I recline my seat?"', exB: '"I would like to recline a little."'},
    {word: 'landing', pt: 'pouso', exA: '"We are landing in 20 minutes."', exB: '"The landing was very smooth."'},
    {word: 'customs officer', pt: 'agente da alfândega', exA: '"The customs officer asked many questions."', exB: '"Please answer the customs officer in English."'},
    {word: 'immigration', pt: 'imigração', exA: '"Immigration was very fast today."', exB: '"Where is the immigration line?"'},
    {word: 'purpose of visit', pt: 'motivo da viagem', exA: '"What is the purpose of your visit?"', exB: '"My purpose of visit is tourism."'},
    {word: 'length of stay', pt: 'tempo de permanência', exA: '"What is your length of stay?"', exB: '"My length of stay is ten days."'},
    {word: "I'm here as a tourist", pt: 'estou aqui como turista', exA: '"I\'m here as a tourist."', exB: '"I am here as a tourist for ten days."'},
    {word: 'accommodation', pt: 'hospedagem', exA: '"My accommodation is a hotel in Paris."', exB: '"Where is your accommodation?"'},
  ],
  24: [
    {word: "I can", pt: 'eu consigo', exA: '"Now I can introduce myself in English."', exB: '"I can order food without help."'},
    {word: "I couldn't", pt: 'eu não conseguia', exA: '"Before, I couldn\'t order in English."', exB: '"In Aula 1, I couldn\'t make a full sentence."'},
    {word: "I've improved in", pt: 'eu melhorei em', exA: '"I\'ve improved in pronunciation."', exB: '"I\'ve improved in speaking with confidence."'},
    {word: "I'm still working on", pt: 'ainda estou trabalhando em', exA: '"I\'m still working on listening."', exB: '"I\'m still working on past simple."'},
    {word: 'confident', pt: 'confiante', exA: '"I feel confident with greetings."', exB: '"I am confident in role-plays."'},
    {word: 'progress', pt: 'progresso', exA: '"I am proud of my progress."', exB: '"My progress in speaking is huge."'},
    {word: 'goal', pt: 'meta', exA: '"My goal is to be fluent by 2027."', exB: '"What is your next goal, Gabriela?"'},
    {word: 'looking back', pt: 'olhando para trás', exA: '"Looking back, the first class felt scary."', exB: '"Looking back, I have learned so much."'},
    {word: 'achievement', pt: 'conquista', exA: '"This is a big achievement for me."', exB: '"My biggest achievement is speaking without fear."'},
    {word: 'milestone', pt: 'marco', exA: '"This class is an important milestone."', exB: '"Aula 24 is the halfway milestone."'},
  ],
  25: [
    {word: 'episode', pt: 'episódio', exA: '"The first episode hooked me immediately."', exB: '"This episode is the best of the season."'},
    {word: 'season', pt: 'temporada', exA: '"Season two is much better than season one."', exB: '"The new season comes out in October."'},
    {word: 'plot', pt: 'enredo', exA: '"The plot is full of surprises."', exB: '"I love a good plot twist."'},
    {word: 'character', pt: 'personagem', exA: '"Blair is the character who never gives up."', exB: '"Each character has a different style."'},
    {word: 'main character', pt: 'protagonista', exA: '"Serena is the main character of Gossip Girl."', exB: '"Who is the main character of Friends?"'},
    {word: 'villain', pt: 'vilão', exA: '"Chuck is sometimes the villain."', exB: '"Every good show needs a villain."'},
    {word: 'binge-watch', pt: 'maratonar', exA: '"I love to binge-watch on weekends."', exB: '"I binge-watched the whole season last night."'},
    {word: 'cliffhanger', pt: 'gancho', exA: '"Season finales always end with a cliffhanger."', exB: '"What a cliffhanger!"'},
    {word: 'I think', pt: 'eu acho', exA: '"I think Blair is the best character."', exB: '"I think this show is overrated."'},
    {word: 'in my opinion', pt: 'na minha opinião', exA: '"In my opinion, Friends is funnier."', exB: '"In my opinion, Rory is the smartest character."'},
  ],
};

const matching = {
  21: [
    {word: 'will', correct: 'vai (futuro)', distractors: ['já foi', 'pode']},
    {word: "won't", correct: 'não vai', distractors: ['nunca foi', 'pode não']},
    {word: 'probably', correct: 'provavelmente', distractors: ['certamente', 'nunca']},
    {word: 'maybe', correct: 'talvez', distractors: ['sempre', 'já']},
    {word: 'definitely', correct: 'com certeza', distractors: ['talvez', 'raramente']},
    {word: 'I hope', correct: 'eu espero', distractors: ['eu prometo', 'eu acho']},
    {word: 'I promise', correct: 'eu prometo', distractors: ['eu duvido', 'eu acho']},
    {word: 'exchange program', correct: 'programa de intercâmbio', distractors: ['ano sabático', 'bolsa de estudo']},
  ],
  22: [
    {word: 'passport', correct: 'passaporte', distractors: ['visto', 'cartão']},
    {word: 'boarding pass', correct: 'cartão de embarque', distractors: ['cartão de visita', 'comprovante']},
    {word: 'gate', correct: 'portão de embarque', distractors: ['fila', 'esteira']},
    {word: 'security checkpoint', correct: 'controle de segurança', distractors: ['imigração', 'esteira']},
    {word: 'flight attendant', correct: 'comissário de bordo', distractors: ['piloto', 'agente']},
    {word: 'delay', correct: 'atraso', distractors: ['cancelamento', 'pontualidade']},
    {word: 'window seat', correct: 'assento na janela', distractors: ['assento no corredor', 'classe executiva']},
    {word: 'carry-on luggage', correct: 'bagagem de mão', distractors: ['bagagem despachada', 'bagagem perdida']},
  ],
  23: [
    {word: 'turbulence', correct: 'turbulência', distractors: ['decolagem', 'pouso']},
    {word: 'tray table', correct: 'mesa do avião', distractors: ['poltrona', 'cinto de segurança']},
    {word: 'recline', correct: 'reclinar', distractors: ['levantar', 'deitar']},
    {word: 'landing', correct: 'pouso', distractors: ['decolagem', 'voo']},
    {word: 'customs officer', correct: 'agente da alfândega', distractors: ['piloto', 'recepcionista']},
    {word: 'immigration', correct: 'imigração', distractors: ['embarque', 'esteira']},
    {word: 'purpose of visit', correct: 'motivo da viagem', distractors: ['endereço', 'tempo de estadia']},
    {word: 'accommodation', correct: 'hospedagem', distractors: ['transporte', 'alimentação']},
  ],
  24: [
    {word: 'I can', correct: 'eu consigo', distractors: ['eu queria', 'eu vou']},
    {word: "I couldn't", correct: 'eu não conseguia', distractors: ['eu não vou', 'eu não quero']},
    {word: "I've improved in", correct: 'eu melhorei em', distractors: ['eu pretendo', 'eu duvido']},
    {word: 'confident', correct: 'confiante', distractors: ['nervoso', 'tímido']},
    {word: 'progress', correct: 'progresso', distractors: ['retrocesso', 'desafio']},
    {word: 'goal', correct: 'meta', distractors: ['medo', 'erro']},
    {word: 'achievement', correct: 'conquista', distractors: ['fracasso', 'tentativa']},
    {word: 'milestone', correct: 'marco', distractors: ['tropeço', 'rotina']},
  ],
  25: [
    {word: 'episode', correct: 'episódio', distractors: ['temporada', 'enredo']},
    {word: 'season', correct: 'temporada', distractors: ['episódio', 'cena']},
    {word: 'plot', correct: 'enredo', distractors: ['personagem', 'temporada']},
    {word: 'main character', correct: 'protagonista', distractors: ['vilão', 'figurante']},
    {word: 'villain', correct: 'vilão', distractors: ['herói', 'protagonista']},
    {word: 'binge-watch', correct: 'maratonar', distractors: ['acelerar', 'pular']},
    {word: 'cliffhanger', correct: 'gancho', distractors: ['final feliz', 'introdução']},
    {word: 'in my opinion', correct: 'na minha opinião', distractors: ['na verdade', 'sem dúvida']},
  ],
};

const fillIn = {
  21: [
    {sentence: '"I ___ definitely visit the Louvre in Paris."', answer: 'will', hint: 'Hint: the modal that expresses a future decision or promise', phrase: 'I will definitely visit the Louvre in Paris.'},
    {sentence: '"I ___ forget my passport — I promise!"', answer: "won't", hint: 'Hint: the contraction of "will not"', phrase: "I won't forget my passport — I promise!"},
    {sentence: '"It will ___ rain in Paris in February."', answer: 'probably', hint: 'Hint: an adverb that means "more likely than not"', phrase: 'It will probably rain in Paris in February.'},
    {sentence: '"___ I will live in France one day."', answer: 'Maybe', hint: 'Hint: a word that expresses uncertainty about the future', phrase: 'Maybe I will live in France one day.'},
    {sentence: '"I ___ I will be fluent by my trip in 2027."', answer: 'hope', hint: 'Hint: to wish for something positive in the future', phrase: 'I hope I will be fluent by my trip in 2027.'},
    {sentence: '"I ___ I will study English every single day."', answer: 'promise', hint: 'Hint: to give your word that you will do something', phrase: 'I promise I will study English every single day.'},
  ],
  22: [
    {sentence: '"Could I see your ___ , please?"', answer: 'passport', hint: 'Hint: the official document that proves your identity in international travel', phrase: 'Could I see your passport, please?'},
    {sentence: '"Here is my ___ — I am in seat 24A."', answer: 'boarding pass', hint: 'Hint: the document that allows you to enter the plane', phrase: 'Here is my boarding pass — I am in seat 24A.'},
    {sentence: '"Excuse me, where is ___ B12?"', answer: 'gate', hint: 'Hint: the place where you enter the plane', phrase: 'Excuse me, where is gate B12?'},
    {sentence: '"I prefer a ___ seat — I love to look outside."', answer: 'window', hint: 'Hint: the type of seat that lets you see the clouds', phrase: 'I prefer a window seat — I love to look outside.'},
    {sentence: '"My flight has a one-hour ___ ."', answer: 'delay', hint: 'Hint: when something happens later than expected', phrase: 'My flight has a one-hour delay.'},
    {sentence: '"This is my ___ — I will not check it in."', answer: 'carry-on luggage', hint: 'Hint: the small bag you take with you on the plane', phrase: 'This is my carry-on luggage — I will not check it in.'},
  ],
  23: [
    {sentence: '"Please put your ___ table up — we are landing soon."', answer: 'tray', hint: 'Hint: the small table in front of your seat on the plane', phrase: 'Please put your tray table up — we are landing soon.'},
    {sentence: '"Could I ___ my seat a little, please?"', answer: 'recline', hint: 'Hint: to push your seat backwards', phrase: 'Could I recline my seat a little, please?'},
    {sentence: '"We are ___ in 20 minutes — please return to your seat."', answer: 'landing', hint: 'Hint: when the plane touches the ground', phrase: 'We are landing in 20 minutes — please return to your seat.'},
    {sentence: '"What is the ___ of your visit, please?"', answer: 'purpose', hint: 'Hint: the reason WHY you are visiting a country', phrase: 'What is the purpose of your visit, please?'},
    {sentence: '"I am here as a ___ for ten days."', answer: 'tourist', hint: 'Hint: a person who visits a place for fun, not work', phrase: 'I am here as a tourist for ten days.'},
    {sentence: '"My ___ is a small hotel in Paris."', answer: 'accommodation', hint: 'Hint: where you stay during your trip', phrase: 'My accommodation is a small hotel in Paris.'},
  ],
  24: [
    {sentence: '"In Aula 1, I ___ even say my name in English."', answer: "couldn't", hint: 'Hint: the past form of "cannot" — it shows ability you did not have', phrase: "In Aula 1, I couldn't even say my name in English."},
    {sentence: '"Now I ___ introduce myself with confidence."', answer: 'can', hint: 'Hint: the modal verb that shows present ability', phrase: 'Now I can introduce myself with confidence.'},
    {sentence: '"I am very ___ when I speak about my routine."', answer: 'confident', hint: 'Hint: an adjective that means feeling sure of yourself', phrase: 'I am very confident when I speak about my routine.'},
    {sentence: '"I am proud of my ___ in pronunciation."', answer: 'progress', hint: 'Hint: the noun that means moving forward and getting better', phrase: 'I am proud of my progress in pronunciation.'},
    {sentence: '"My biggest ___ is speaking in English without fear."', answer: 'achievement', hint: 'Hint: something difficult that you accomplished', phrase: 'My biggest achievement is speaking in English without fear.'},
    {sentence: '"My next ___ is to handle a full conversation in Paris."', answer: 'goal', hint: 'Hint: a future target you want to reach', phrase: 'My next goal is to handle a full conversation in Paris.'},
  ],
  25: [
    {sentence: '"My favorite ___ of Friends is the one in the embassy."', answer: 'episode', hint: 'Hint: one part of a series — about 22 minutes for Friends', phrase: 'My favorite episode of Friends is the one in the embassy.'},
    {sentence: '"___ two of Gossip Girl is much better than season one."', answer: 'Season', hint: 'Hint: a group of episodes released together (10–22 episodes)', phrase: 'Season two of Gossip Girl is much better than season one.'},
    {sentence: '"The ___ of Notting Hill is so romantic."', answer: 'plot', hint: 'Hint: the main story of a movie or TV show', phrase: 'The plot of Notting Hill is so romantic.'},
    {sentence: '"Blair is the ___ who has the best style."', answer: 'character', hint: 'Hint: a person inside a story', phrase: 'Blair is the character who has the best style.'},
    {sentence: '"On weekends, I love to ___ -watch series in bed."', answer: 'binge', hint: 'Hint: to watch many episodes one after another', phrase: 'On weekends, I love to binge-watch series in bed.'},
    {sentence: '"In my ___ , Rory is the most relatable character."', answer: 'opinion', hint: 'Hint: what you personally think about something', phrase: 'In my opinion, Rory is the most relatable character.'},
  ],
};

const multipleChoice = {
  21: [
    {q: 'You see dark clouds in Paris and your friend asks if it will rain. The most natural answer is:', options: ['"It rains."', '"Yes, it raining."', '"Yes, it will probably rain."', '"It rained yesterday."'], correct: 2},
    {q: 'You want to make a strong promise about studying English. The best sentence is:', options: ['"I am studying every day."', '"I promise I will study every day."', '"I would study every day."', '"I studied every day."'], correct: 1},
  ],
  22: [
    {q: 'You arrive at the airport and need to drop off your suitcase. You go to:', options: ['"The gate."', '"The customs."', '"The check-in counter."', '"The boarding pass."'], correct: 2},
    {q: 'A flight attendant asks if you want a window seat or aisle seat. You like to look outside. You answer:', options: ['"I would like an aisle seat, please."', '"I would like a window seat, please."', '"I would like a delay, please."', '"I would like a passport, please."'], correct: 1},
  ],
  23: [
    {q: 'During the flight, you feel hot. The most polite way to ask is:', options: ['"Bring me water!"', '"Could you bring me some water, please?"', '"Water now."', '"You bring water?"'], correct: 1},
    {q: 'A customs officer asks "What is the purpose of your visit?". The best answer is:', options: ['"I have a passport."', '"My name is Gabriela."', '"I\'m here as a tourist for ten days."', '"I do not know."'], correct: 2},
  ],
  24: [
    {q: 'Looking back from Aula 1 to Aula 24, the most accurate self-statement is:', options: ['"I am the same as Aula 1."', '"In Aula 1, I couldn\'t introduce myself. Now I can."', '"I will speak Portuguese."', '"I have not changed."'], correct: 1},
    {q: 'You want to celebrate progress without arrogance. The best phrase is:', options: ['"I am perfect now."', '"I am proud of my progress and I am still working on listening."', '"I have nothing left to learn."', '"I do not need more classes."'], correct: 1},
  ],
  25: [
    {q: 'You describe Blair Waldorf to a French friend. The best sentence using a relative clause is:', options: ['"Blair is the smart girl."', '"Blair is a character who is ambitious and stylish."', '"Blair: ambitious. Stylish."', '"Blair, ambitious girl, stylish."'], correct: 1},
    {q: 'You want to give an opinion about Friends without sounding aggressive. The best opener is:', options: ['"Friends is the best, period."', '"In my opinion, Friends is funnier than Gossip Girl."', '"You are wrong about Friends."', '"Friends — you understand nothing."'], correct: 1},
  ],
};

const ordering = {
  21: {
    title: 'Put this 2027 prediction speech in order',
    items: [
      {order: 1, text: '"In February 2027, I will fly to Paris with my family."'},
      {order: 2, text: '"I think it will probably be cold and a little rainy."'},
      {order: 3, text: '"I will visit the Louvre and the Eiffel Tower for sure."'},
      {order: 4, text: '"I won\'t speak Portuguese — only English and a little French!"'},
      {order: 5, text: '"I promise I will practice every day until then."'},
    ],
  },
  22: {
    title: 'Put this airport check-in dialogue in order',
    items: [
      {order: 1, text: '"Good morning! May I see your passport, please?"'},
      {order: 2, text: '"Yes, here is my passport. I am flying to Paris."'},
      {order: 3, text: '"Do you have any luggage to check in?"'},
      {order: 4, text: '"Yes, this one. And this is my carry-on bag."'},
      {order: 5, text: '"Perfect. Here is your boarding pass. Your gate is B12."'},
    ],
  },
  23: {
    title: 'Put this immigration interview in order',
    items: [
      {order: 1, text: '"Bonjour. May I see your passport, please?"'},
      {order: 2, text: '"Of course. Here it is."'},
      {order: 3, text: '"What is the purpose of your visit?"'},
      {order: 4, text: '"I\'m here as a tourist for ten days."'},
      {order: 5, text: '"Where is your accommodation?"'},
      {order: 6, text: '"I am staying at a small hotel in Paris."'},
      {order: 7, text: '"Welcome to France. Have a great trip!"'},
    ],
  },
  24: {
    title: 'Put this halfway-point self-reflection in order',
    items: [
      {order: 1, text: '"Looking back at Aula 1, I was very nervous."'},
      {order: 2, text: '"At first, I couldn\'t even say my name in English."'},
      {order: 3, text: '"Now I can introduce myself with confidence."'},
      {order: 4, text: '"I am still working on listening to fast English."'},
      {order: 5, text: '"My next goal is to survive Paris in English in 2027."'},
    ],
  },
  25: {
    title: 'Put this Gossip Girl show recommendation in order',
    items: [
      {order: 1, text: '"Have you ever watched Gossip Girl?"'},
      {order: 2, text: '"It\'s a show that takes place in New York."'},
      {order: 3, text: '"The main character is Serena, who is rich and famous."'},
      {order: 4, text: '"Blair is the character who has the best style and is so dramatic."'},
      {order: 5, text: '"In my opinion, you should definitely binge-watch the first season!"'},
    ],
  },
};

const pronunciation = {
  21: [
    {phrase: 'I will definitely visit Paris in February 2027.', pt: 'Eu vou com certeza visitar Paris em fevereiro de 2027.'},
    {phrase: "I won't forget my passport — I promise!", pt: 'Eu não vou esquecer meu passaporte — eu prometo!'},
    {phrase: "I think it will probably rain, but I won't mind.", pt: 'Eu acho que provavelmente vai chover, mas eu não vou me importar.'},
  ],
  22: [
    {phrase: 'May I see your boarding pass, please?', pt: 'Posso ver seu cartão de embarque, por favor?'},
    {phrase: 'I would like a window seat, please.', pt: 'Eu gostaria de um assento na janela, por favor.'},
    {phrase: 'Excuse me, where is gate B12?', pt: 'Com licença, onde fica o portão B12?'},
  ],
  23: [
    {phrase: 'Could you bring me a blanket, please?', pt: 'Você poderia me trazer um cobertor, por favor?'},
    {phrase: "I'm here as a tourist for ten days.", pt: 'Estou aqui como turista por dez dias.'},
    {phrase: 'My accommodation is a small hotel in Paris.', pt: 'Minha hospedagem é um pequeno hotel em Paris.'},
  ],
  24: [
    {phrase: "In Aula 1, I couldn't even introduce myself. Now I can.", pt: 'Na Aula 1, eu nem conseguia me apresentar. Agora eu consigo.'},
    {phrase: "I'm proud of my progress and I'm still working on listening.", pt: 'Estou orgulhosa do meu progresso e ainda estou trabalhando na escuta.'},
    {phrase: 'My next goal is to survive Paris in English in 2027.', pt: 'Minha próxima meta é sobreviver em Paris em inglês em 2027.'},
  ],
  25: [
    {phrase: 'Blair is the character who has the best style.', pt: 'Blair é a personagem que tem o melhor estilo.'},
    {phrase: 'Friends is a show that takes place in New York.', pt: 'Friends é uma série que se passa em Nova York.'},
    {phrase: 'In my opinion, you should definitely binge-watch it.', pt: 'Na minha opinião, você deveria com certeza maratonar.'},
  ],
};

const thinkAboutIt = {
  21: {
    question: 'Imagine it is December 2026 — Paris is two months away. Speak directly to your future self in English: what WILL you do every day until February? What WON\'T you do? What do you HOPE will happen in Paris? Use will, won\'t, probably, maybe, I hope, I promise.',
    suggestion: 'Future Gabriela, I will study English every day. I won\'t skip class. I will probably watch one episode of Friends every night in English. I hope I will be fluent enough to make a French friend. I promise I will not be afraid to try.',
    suggestionPt: 'Gabriela do futuro, eu vou estudar inglês todo dia. Eu não vou faltar à aula. Eu provavelmente vou assistir um episódio de Friends toda noite em inglês. Eu espero estar fluente o suficiente para fazer uma amiga francesa. Eu prometo que não vou ter medo de tentar.',
  },
  22: {
    question: 'Imagine you are at Guarulhos airport on the day of your trip to Paris. Tell the story of the next 4 hours in English — from arriving at the airport, checking in, going through security, to boarding the plane. Use the airport vocabulary as if you are narrating in real time.',
    suggestion: 'I am at the airport now. I go to the check-in counter and show my passport. The agent gives me my boarding pass. My gate is B12. I have one carry-on bag. After security, I walk to the gate. The flight attendant says it\'s time to board.',
    suggestionPt: 'Estou no aeroporto agora. Vou ao balcão de check-in e mostro meu passaporte. A agente me dá meu cartão de embarque. Meu portão é o B12. Tenho uma bagagem de mão. Depois da segurança, ando até o portão. O comissário diz que é hora de embarcar.',
  },
  23: {
    question: 'You just landed at Charles de Gaulle airport in Paris. The customs officer is asking you questions in English. Answer all of them — in full sentences, with confidence: name, nationality, purpose of visit, length of stay, where you are staying. This is the moment.',
    suggestion: 'Good morning. My name is Gabriela Pires. I am Brazilian. I am here as a tourist for ten days. I am staying at a small hotel in Montmartre. This is my first time in France and I am very excited.',
    suggestionPt: 'Bom dia. Meu nome é Gabriela Pires. Sou brasileira. Estou aqui como turista por dez dias. Estou hospedada em um pequeno hotel em Montmartre. É minha primeira vez na França e estou muito animada.',
  },
  24: {
    question: 'It\'s the halfway point of your program — Aula 24 of 48. Imagine your Aula 1 self is in the room with you. Tell her three things she WILL achieve, three things she will improve at, and one thing she should be proud of starting today. Speak to her in English.',
    suggestion: 'Hi, Aula 1 Gabriela. You will introduce yourself in English by Aula 5. You will tell stories in English by Aula 14. You will land in Paris in 2027 ready to talk. You will improve at listening, at speaking without translating, and at making jokes in English. Be proud — you started, and that is the hardest part.',
    suggestionPt: 'Oi, Gabriela da Aula 1. Você vai conseguir se apresentar em inglês até a Aula 5. Você vai contar histórias em inglês até a Aula 14. Você vai chegar em Paris em 2027 pronta para conversar. Você vai melhorar na escuta, em falar sem traduzir e em fazer piada em inglês. Tenha orgulho — você começou, e essa é a parte mais difícil.',
  },
  25: {
    question: 'A French friend in Paris asks "What show should I watch this weekend?" Recommend one of YOUR favorite series in English — describe the plot, the main characters using relative clauses (who/that), and your opinion. Make her want to watch it.',
    suggestion: 'You should watch Gossip Girl — it\'s a show that takes place in New York. The main character is Serena, who is glamorous but kind. Blair is the character who has the best style and is so dramatic. In my opinion, the first season is the best — definitely binge-watch it.',
    suggestionPt: 'Você deveria assistir Gossip Girl — é uma série que se passa em Nova York. A protagonista é a Serena, que é glamorosa mas gentil. A Blair é a personagem que tem o melhor estilo e é super dramática. Na minha opinião, a primeira temporada é a melhor — maratona com certeza.',
  },
};

const survivalCards = {
  21: [
    {en: 'I will definitely visit the Louvre.', pt: 'Eu vou com certeza visitar o Louvre.'},
    {en: "I won't forget my passport.", pt: 'Eu não vou esquecer meu passaporte.'},
    {en: 'I think it will probably rain in Paris.', pt: 'Eu acho que provavelmente vai chover em Paris.'},
    {en: 'I hope I will be fluent by 2027.', pt: 'Eu espero estar fluente até 2027.'},
    {en: 'I promise I will practice every day.', pt: 'Eu prometo que vou praticar todo dia.'},
  ],
  22: [
    {en: 'May I see your passport, please?', pt: 'Posso ver seu passaporte, por favor?'},
    {en: 'Where is gate B12, please?', pt: 'Onde fica o portão B12, por favor?'},
    {en: 'I would like a window seat.', pt: 'Eu gostaria de um assento na janela.'},
    {en: 'My flight has a one-hour delay.', pt: 'Meu voo tem uma hora de atraso.'},
    {en: 'This is my carry-on luggage.', pt: 'Esta é minha bagagem de mão.'},
  ],
  23: [
    {en: 'Could you bring me a blanket, please?', pt: 'Você poderia me trazer um cobertor, por favor?'},
    {en: "I'm here as a tourist for ten days.", pt: 'Estou aqui como turista por dez dias.'},
    {en: 'My accommodation is a hotel in Paris.', pt: 'Minha hospedagem é um hotel em Paris.'},
    {en: 'Could I recline my seat, please?', pt: 'Posso reclinar meu assento, por favor?'},
    {en: 'We are landing in 20 minutes.', pt: 'Vamos pousar em 20 minutos.'},
  ],
  24: [
    {en: "In Aula 1, I couldn't introduce myself.", pt: 'Na Aula 1, eu não conseguia me apresentar.'},
    {en: "Now I can speak English with confidence.", pt: 'Agora eu consigo falar inglês com confiança.'},
    {en: "I'm proud of my progress.", pt: 'Estou orgulhosa do meu progresso.'},
    {en: "I'm still working on listening.", pt: 'Ainda estou trabalhando na escuta.'},
    {en: 'My next goal is Paris 2027.', pt: 'Minha próxima meta é Paris 2027.'},
  ],
  25: [
    {en: 'Friends is a show that takes place in New York.', pt: 'Friends é uma série que se passa em Nova York.'},
    {en: 'Blair is the character who has the best style.', pt: 'Blair é a personagem que tem o melhor estilo.'},
    {en: 'In my opinion, season two is the best.', pt: 'Na minha opinião, a segunda temporada é a melhor.'},
    {en: 'You should definitely binge-watch it.', pt: 'Você deveria com certeza maratonar.'},
    {en: 'The plot is full of surprises.', pt: 'O enredo é cheio de surpresas.'},
  ],
};

const grammarTips = {
  21: 'Future com <strong>will</strong>: usado para predições, promessas e decisões espontâneas. Estrutura: <em>I will + verbo base</em>. Negativa: <em>I won\'t (= will not)</em>. Diferença para "going to" (Aula 16): <em>going to</em> é plano já decidido; <em>will</em> é decisão na hora ou previsão. Ex: "Look at the clouds! It will rain."',
  22: 'Pedidos polidos no aeroporto: <strong>May I…?</strong> e <strong>Could you…?</strong>. Mais formais que "Can I". Estrutura: <em>May I + verbo</em> / <em>Could you + verbo</em>. Imperativo para instruções: <em>"Please remove your shoes"</em>, <em>"Place your bag on the belt"</em>. Em aeroporto, o registro polido é o padrão.',
  23: 'Present continuous para ações <strong>agora</strong>: <em>"We are landing now"</em>, <em>"The captain is speaking"</em>. Estrutura: <em>am/is/are + verbo-ing</em>. Útil para narrar o que está acontecendo. Para pedidos polidos no avião: <em>Could you + verbo</em> + <em>please</em>.',
  24: 'Auto-avaliação reflexiva: contraste <strong>passado x presente</strong> com <em>"I couldn\'t … but now I can …"</em>. Frases de progresso: <em>"I\'ve improved in …"</em>, <em>"I\'m still working on …"</em>, <em>"My next goal is to …"</em>. Sem auto-crítica destrutiva — celebre o quanto avançou.',
  25: 'Relative clauses com <strong>who</strong> (pessoas) e <strong>that</strong> (coisas): <em>"Blair is a character WHO is ambitious"</em>, <em>"Friends is a show THAT is funny"</em>. Linguagem de opinião: <em>"I think…"</em>, <em>"In my opinion…"</em>, <em>"What I love about it is…"</em>. Para recomendar: <em>"You should watch…"</em>.',
};

const lessonObjectives = {
  21: 'Ao final desta aula, Gabriela será capaz de fazer 5+ predições e 3+ promessas em inglês sobre 2027 usando will, won\'t, probably, maybe, I hope e I promise — sem tradução do PT.',
  22: 'Ao final desta aula, Gabriela será capaz de atravessar um cenário completo de aeroporto (check-in, segurança, portão) em inglês — usando May I, Could you, e o vocabulário operacional de viagem.',
  23: 'Ao final desta aula, Gabriela será capaz de responder a uma entrevista de imigração e a um voo inteiro em inglês, com 8+ frases naturais, sem precisar pedir tradução.',
  24: 'Ao final desta aula, Gabriela será capaz de descrever seu próprio progresso comparando Aula 1 com Aula 24, identificando 3 ganhos concretos e 2 pontos de atenção em inglês.',
  25: 'Ao final desta aula, Gabriela será capaz de descrever uma série favorita usando 4+ relative clauses com who/that, dar opinião com 3+ marcadores ("I think", "in my opinion") e recomendar a alguém em 4+ frases.',
};

const homework = {
  21: [
    'Escreva um parágrafo de 8-10 frases: "My 2027 Predictions" — o que VAI e o que NÃO VAI acontecer na sua viagem a Paris. Use will, won\'t, probably, maybe, I think, I hope.',
    'Grave 90 segundos de áudio: "A message to my future host family in France" — apresente-se e diga 3 coisas que VAI fazer e 2 que NÃO VAI fazer durante a estadia.',
    'Assista 5 minutos de qualquer série em inglês com legenda EN e anote 5 frases com "will" ou "won\'t".',
  ],
  22: [
    'Pesquise no YouTube: "airport announcements English" — ouça 2 anúncios reais e escreva 5 frases que você entendeu.',
    'Pratique sozinha o diálogo completo de check-in (passageira + agente). Grave os DOIS papéis em um áudio de 2-3 minutos.',
    'Faça uma "Airport Vocab List" de 15 palavras-chave em inglês com tradução em PT.',
  ],
  23: [
    'Escreva uma página de diário em inglês (8-10 frases) intitulada: "Today I arrived in Paris" — narre seu primeiro dia. Use past simple + present perfect ("I have finally arrived!").',
    'Encontre no YouTube 1 vídeo de entrevista real de imigração em inglês e anote 3 perguntas feitas pelo agente.',
    'Liste 10 frases que você precisa saber para sobreviver a um voo + chegada em inglês.',
  ],
  24: [
    'Re-grave seu áudio baseline da Aula 1 (60-90 segundos) e compare com o original. Escreva 5 frases em inglês: "In Aula 1, I couldn\'t … but now I can …".',
    'Revise seu caderno de vocabulário das Aulas 1-23. Marque 10 palavras 100% confiantes e 5 que precisam mais prática.',
    'Defina 3 metas pessoais para o Bloco 3 em inglês: "By Aula 48, I will be able to …".',
  ],
  25: [
    'Escolha 1 episódio de Friends ou Gossip Girl. Assista 10 minutos com legenda EN e escreva uma mini-resenha de 6-8 frases em inglês: enredo, 1 personagem com relative clause (who/that) e sua opinião.',
    'Liste 5 palavras NOVAS em inglês que você ouviu no episódio.',
    'Grave 60 segundos de áudio: "Why you should watch [sua série favorita]" — use no mínimo 3 relative clauses + 2 expressões de opinião.',
  ],
};

const ccqs = {
  21: [
    {q: '"I will visit Paris" — é plano definido ou predição/decisão?', a: 'Will = predição ou decisão espontânea. Para plano já decidido com data, use "going to".'},
    {q: '"I won\'t go" — won\'t é a contração de quê?', a: 'Will not. "I won\'t" = "I will not".'},
    {q: '"It will probably rain" — qual o nível de certeza?', a: 'Médio-alto. "Probably" = mais provável que sim.'},
    {q: 'Em "I hope I will be fluent", quem está fluente: você agora ou no futuro?', a: 'No futuro. "I hope" + "I will" projeta um desejo no futuro.'},
    {q: '"I promise I will study" — é mais forte que "I will study"?', a: 'Sim. "I promise" + "I will" reforça compromisso pessoal.'},
  ],
  22: [
    {q: '"May I see your passport?" é mais formal ou menos formal que "Can I"?', a: 'Mais formal. May é o registro padrão de aeroporto/hotel/restaurante de alto nível.'},
    {q: 'Em "Could you open your bag, please?", quem age — eu ou a outra pessoa?', a: 'A outra pessoa. "Could you" pede ação ao interlocutor; "Could I" pede permissão para mim.'},
    {q: '"Carry-on" e "checked baggage" — qual delas vai com você na cabine?', a: 'Carry-on (bagagem de mão). Checked = despachada.'},
    {q: '"My flight is delayed" significa o quê?', a: 'Meu voo está atrasado.'},
    {q: 'Por que "Could you" é mais polido que "Open the bag"?', a: 'Imperativo direto soa rude. "Could you" + please é o registro educado padrão.'},
  ],
  23: [
    {q: '"We are landing in 20 minutes" — está acontecendo agora ou já aconteceu?', a: 'Acontecendo agora. Present continuous = ação em andamento.'},
    {q: '"Could I recline my seat?" pede o quê — permissão ou ação dos outros?', a: 'Permissão para mim. "Could I" = pode eu? "Could you" = você poderia?'},
    {q: '"What is the purpose of your visit?" — o agente quer saber o quê?', a: 'O motivo da viagem (turismo, trabalho, estudo, família).'},
    {q: '"I am here as a tourist" responde qual pergunta?', a: 'A pergunta sobre purpose of visit (motivo da viagem).'},
    {q: '"Length of stay" significa o quê?', a: 'Quanto tempo você vai ficar no país. Resposta: "ten days", "two weeks".'},
  ],
  24: [
    {q: '"I couldn\'t" é o passado de quê?', a: 'De "I can\'t". Mostra habilidade que você não tinha antes.'},
    {q: 'Por que dizer "I couldn\'t … but now I can …" e não só "I can …"?', a: 'O contraste mostra progresso. "Now" sozinho não dá perspectiva da jornada.'},
    {q: '"I\'ve improved in" usa qual tempo verbal?', a: 'Present perfect. Ação que começou no passado e continua relevante agora.'},
    {q: '"I\'m still working on" — o que isso comunica?', a: 'Humildade + transparência. Reconhece que algo continua em desenvolvimento.'},
    {q: 'Por que celebrar progresso em vez de mirar perfeição?', a: 'Em A1+, perfeição é destrutiva. Progresso é o critério real de sucesso pedagógico.'},
  ],
  25: [
    {q: 'Em "Blair is a character WHO is ambitious", o "who" se refere a quem?', a: 'A pessoa anterior — Blair. "Who" descreve pessoas; "that" descreve coisas.'},
    {q: 'Em "Friends is a show THAT is funny", "that" se refere a quê?', a: 'À série Friends. "That" para coisas/séries/objetos.'},
    {q: '"I think" e "In my opinion" significam a mesma coisa?', a: 'Sim — ambos introduzem opinião pessoal. "In my opinion" é levemente mais formal.'},
    {q: '"Binge-watch" significa o quê?', a: 'Maratonar — assistir muitos episódios seguidos.'},
    {q: '"You should watch it" é uma ordem ou uma recomendação?', a: 'Recomendação forte. "Should" = é uma boa ideia, mas você decide.'},
  ],
};

const obstacles = {
  21: [
    {label: 'Confusão will × going to', text: 'Provável que use "going to" para tudo, ou misture os dois. Drillar: pré-decidido com data = going to; predição/decisão na hora = will.'},
    {label: '"Won\'t" pronúncia', text: 'Contração /woʊnt/ — pode soar como "want" /wɑnt/. Confunde sentido. Drill par mínimo: "I want" vs. "I won\'t".'},
    {label: 'Esquecer "will" no futuro', text: 'Vai dizer "I study tomorrow" sem o will. Reforço: pra falar do futuro, sempre tem um marcador (will, going to, present continuous + tempo).'},
    {label: '"I hope" + "will"', text: 'Pode dizer "I hope I am fluent". Correto: "I hope I will be fluent". Hope projeta para o futuro.'},
  ],
  22: [
    {label: 'May vs. Can no aeroporto', text: 'Vai usar "Can I…?" no check-in. Não está errado, mas "May I…?" é o registro adequado em aeroporto. Drillar.'},
    {label: 'Pronúncia de "luggage"', text: '/ˈlʌɡɪdʒ/ — pode dizer "lu-GA-gi" influenciada pelo PT. Som /ʌ/ + /dʒ/. Drill 5x.'},
    {label: 'Gate confundido com "porta"', text: 'Tradução literal "porta" pode confundir. Reforço: gate = portão de embarque específico (B12, A24).'},
    {label: '"Window" vs. "aisle"', text: 'Pode confundir os dois. Visual: window = janela (para olhar fora); aisle = corredor (para levantar fácil).'},
  ],
  23: [
    {label: 'Pronúncia de "turbulence"', text: '/ˈtɜrbjələns/ — palavra longa, pode quebrar o ritmo. Drill devagar e depois rápido.'},
    {label: '"Customs" no plural', text: 'Sempre plural ("customs", "the customs officer"). Não dizer "the custom".'},
    {label: 'Hesitação na pergunta de imigração', text: 'Provável travar em "purpose of visit". Drill como chunk fixo: "I\'m here as a tourist for [X] days."'},
    {label: 'Confusão "where are you staying"', text: 'Pode responder com cidade ("Paris"). Querem o tipo de acomodação ("at a hotel", "at a friend\'s house").'},
  ],
  24: [
    {label: 'Auto-crítica excessiva', text: 'Adolescente perfeccionista pode minimizar progresso. Reforçar: cada frase em inglês HOJE é prova de progresso.'},
    {label: '"I couldn\'t" pronunciação', text: '/ˈkʊdənt/ — som /ʊ/ não vogal portuguesa. Drill par: could /kʊd/ vs. cool /kuːl/.'},
    {label: 'Comparação injusta com nativos', text: 'Pode comparar-se com fluent speakers e desanimar. Reforço: a comparação é com Gabriela da Aula 1, não com nativo.'},
    {label: 'Confusão present perfect', text: '"I have improved" pode virar "I improved" (past simple). Reforço: improvement é processo até agora — present perfect.'},
  ],
  25: [
    {label: 'Esquecer "who"/"that"', text: 'Pode dizer "Blair is character is ambitious". Sem o "who", a frase quebra. Drill: pessoa = WHO, coisa = THAT.'},
    {label: '"In my opinion" como anúncio', text: 'Pode anunciar opinião como verdade absoluta ("Friends is THE BEST show"). Modular: "In my opinion, Friends is funnier than…".'},
    {label: 'Pronúncia "binge"', text: '/bɪndʒ/ — som /dʒ/ no final pode virar /ʒi/. Drill: binge /bɪndʒ/ vs. binger.'},
    {label: 'Trocar "season" por "saison"', text: 'Influência do francês/PT. Reforço: SEA-son /ˈsiːzən/, não "saisão".'},
  ],
};

const dialogues = {
  21: {
    title: 'Promising and predicting — A call to her future host family',
    context: 'Gabriela video-calls her future French host family in November 2026, three months before the trip. She introduces herself and shares her predictions and promises.',
    lines: [
      {speaker: 'HOST', name: 'Mme Dubois — host mom', side: 'staff', text: 'Hello Gabriela! We are so happy to meet you before your trip. So, what are your plans?'},
      {speaker: 'GAB', name: 'Gabriela', side: 'you', text: 'Hi! I\'m so happy too. I will arrive in February 2027. I think it will probably be cold!'},
      {speaker: 'HOST', name: 'Mme Dubois', side: 'staff', text: 'Yes, very cold. What will you definitely visit?'},
      {speaker: 'GAB', name: 'Gabriela', side: 'you', text: 'I will definitely visit the Louvre and the Eiffel Tower. Maybe I will go to Versailles too.'},
      {speaker: 'HOST', name: 'Mme Dubois', side: 'staff', text: 'Wonderful! And what won\'t you do?'},
      {speaker: 'GAB', name: 'Gabriela', side: 'you', text: 'I won\'t speak Portuguese — only English and a little French! I promise I will practice every day.'},
      {speaker: 'HOST', name: 'Mme Dubois', side: 'staff', text: 'I love that. We will be ready for you!'},
      {speaker: 'GAB', name: 'Gabriela', side: 'you', text: 'Thank you. I hope it will be the best trip of my life.'},
    ],
  },
  22: {
    title: 'Full airport check-in at Guarulhos',
    context: 'It is the morning of the trip to Paris. Gabriela arrives at Guarulhos International Airport (São Paulo) and goes to the check-in counter for her flight to Charles de Gaulle.',
    lines: [
      {speaker: 'AGT', name: 'Check-in agent', side: 'staff', text: 'Good morning! May I see your passport, please?'},
      {speaker: 'GAB', name: 'Gabriela', side: 'you', text: 'Good morning. Yes, here is my passport.'},
      {speaker: 'AGT', name: 'Agent', side: 'staff', text: 'Thank you. You\'re flying to Paris Charles de Gaulle. Do you have any luggage to check in?'},
      {speaker: 'GAB', name: 'Gabriela', side: 'you', text: 'Yes, this big one. And this is my carry-on luggage.'},
      {speaker: 'AGT', name: 'Agent', side: 'staff', text: 'Perfect. Window seat or aisle seat?'},
      {speaker: 'GAB', name: 'Gabriela', side: 'you', text: 'Window seat, please. I love to look outside.'},
      {speaker: 'AGT', name: 'Agent', side: 'staff', text: 'Here is your boarding pass. Your gate is B12. Boarding starts at 9:30.'},
      {speaker: 'GAB', name: 'Gabriela', side: 'you', text: 'Thank you so much. Where is the security checkpoint, please?'},
      {speaker: 'AGT', name: 'Agent', side: 'staff', text: 'Straight ahead, on your right. Have a great flight!'},
      {speaker: 'GAB', name: 'Gabriela', side: 'you', text: 'Thank you, goodbye!'},
    ],
  },
  23: {
    title: 'Immigration interview at Charles de Gaulle airport',
    context: 'After the long flight, Gabriela arrives at Charles de Gaulle. The customs officer asks the standard arrival questions in English.',
    lines: [
      {speaker: 'OFF', name: 'Customs officer', side: 'staff', text: 'Bonjour. Good morning. May I see your passport, please?'},
      {speaker: 'GAB', name: 'Gabriela', side: 'you', text: 'Good morning. Of course — here it is.'},
      {speaker: 'OFF', name: 'Officer', side: 'staff', text: 'Thank you. What is the purpose of your visit?'},
      {speaker: 'GAB', name: 'Gabriela', side: 'you', text: 'I\'m here as a tourist.'},
      {speaker: 'OFF', name: 'Officer', side: 'staff', text: 'And how long will you be staying?'},
      {speaker: 'GAB', name: 'Gabriela', side: 'you', text: 'Ten days, please.'},
      {speaker: 'OFF', name: 'Officer', side: 'staff', text: 'Where is your accommodation?'},
      {speaker: 'GAB', name: 'Gabriela', side: 'you', text: 'I\'m staying at a small hotel in Montmartre.'},
      {speaker: 'OFF', name: 'Officer', side: 'staff', text: 'Anything to declare?'},
      {speaker: 'GAB', name: 'Gabriela', side: 'you', text: 'No, nothing to declare.'},
      {speaker: 'OFF', name: 'Officer', side: 'staff', text: 'Welcome to France. Have a wonderful trip!'},
      {speaker: 'GAB', name: 'Gabriela', side: 'you', text: 'Thank you! Merci!'},
    ],
  },
  24: {
    title: 'Halfway-point reflection — Gabriela talks to her teacher',
    context: 'It is Aula 24, the halfway milestone. Teacher and Gabriela sit together and talk about the journey so far. Gabriela does not need a script — this is a real conversation.',
    lines: [
      {speaker: 'TCH', name: 'Teacher', side: 'staff', text: 'Gabriela, looking back at Aula 1 — what couldn\'t you do then that you can do now?'},
      {speaker: 'GAB', name: 'Gabriela', side: 'you', text: 'In Aula 1, I couldn\'t even introduce myself. Now I can talk about my routine, my dreams, my favorite series.'},
      {speaker: 'TCH', name: 'Teacher', side: 'staff', text: 'Amazing. What are you most proud of?'},
      {speaker: 'GAB', name: 'Gabriela', side: 'you', text: 'I\'m proud that I can speak without translating from Portuguese sometimes. It\'s slow, but it happens.'},
      {speaker: 'TCH', name: 'Teacher', side: 'staff', text: 'That is HUGE. What are you still working on?'},
      {speaker: 'GAB', name: 'Gabriela', side: 'you', text: 'I\'m still working on listening to fast English. And on past tenses — they confuse me.'},
      {speaker: 'TCH', name: 'Teacher', side: 'staff', text: 'Both will improve in Block 3. What is your next goal?'},
      {speaker: 'GAB', name: 'Gabriela', side: 'you', text: 'My next goal is to survive Paris in English in February 2027. Without help. Without fear.'},
      {speaker: 'TCH', name: 'Teacher', side: 'staff', text: 'You will. I promise.'},
    ],
  },
  25: {
    title: 'Recommending a series to a French exchange student',
    context: 'In her imagined Paris stay, Gabriela meets Léa, a French girl her age. They are sharing series recommendations.',
    lines: [
      {speaker: 'LEA', name: 'Léa — French friend', side: 'staff', text: 'Gabriela, I need a new series for the weekend. Recommend something!'},
      {speaker: 'GAB', name: 'Gabriela', side: 'you', text: 'Have you ever watched Gossip Girl?'},
      {speaker: 'LEA', name: 'Léa', side: 'staff', text: 'No! What is it about?'},
      {speaker: 'GAB', name: 'Gabriela', side: 'you', text: 'It\'s a show that takes place in New York. The main character is Serena, who is rich and glamorous.'},
      {speaker: 'LEA', name: 'Léa', side: 'staff', text: 'Sounds good. Tell me about another character.'},
      {speaker: 'GAB', name: 'Gabriela', side: 'you', text: 'Blair is the character who has the best style. She is dramatic and ambitious. In my opinion, she is the best.'},
      {speaker: 'LEA', name: 'Léa', side: 'staff', text: 'And the plot?'},
      {speaker: 'GAB', name: 'Gabriela', side: 'you', text: 'The plot is full of drama, romance and surprises. Every episode ends with a cliffhanger!'},
      {speaker: 'LEA', name: 'Léa', side: 'staff', text: 'I\'m sold! How many seasons?'},
      {speaker: 'GAB', name: 'Gabriela', side: 'you', text: 'Six seasons — perfect for a binge-watch weekend. You should definitely start tonight.'},
    ],
  },
};

const oralDrills = {
  21: [
    {pt: '"Faça uma predição sobre o tempo em Paris em fevereiro."', en: '"It will probably be cold in Paris in February."'},
    {pt: '"Faça uma promessa sobre estudo de inglês."', en: '"I promise I will study English every day."'},
    {pt: '"Diga algo que você NÃO VAI fazer em Paris."', en: '"I won\'t speak Portuguese in Paris."'},
    {pt: '"Use \'maybe\' para algo que talvez aconteça em 2027."', en: '"Maybe I will live in France one day."'},
    {pt: '"Use \'definitely\' para algo certo."', en: '"I will definitely visit the Louvre."'},
    {pt: '"Use \'I hope\' para um desejo."', en: '"I hope I will make a French friend."'},
    {pt: '"Use \'I think\' para uma opinião sobre o futuro."', en: '"I think it will be the best trip of my life."'},
    {pt: '"Em uma frase, prometa que NÃO VAI esquecer algo importante."', en: '"I promise I won\'t forget my passport."'},
  ],
  22: [
    {pt: '"Cumprimente o agente e peça para ver passaporte (papel: agente)."', en: '"Good morning! May I see your passport, please?"'},
    {pt: '"Diga que tem uma bagagem para despachar e uma de mão."', en: '"I have one suitcase to check in and this carry-on bag."'},
    {pt: '"Peça assento na janela educadamente."', en: '"Could I have a window seat, please?"'},
    {pt: '"Pergunte onde fica o portão B12."', en: '"Excuse me, where is gate B12?"'},
    {pt: '"Diga que seu voo tem uma hora de atraso."', en: '"My flight has a one-hour delay."'},
    {pt: '"Peça para alguém repetir o número do portão (educado)."', en: '"Could you repeat the gate number, please?"'},
    {pt: '"No security: peça licença e pergunte se precisa tirar os sapatos."', en: '"Excuse me, do I need to remove my shoes?"'},
    {pt: '"Encerre o check-in agradecendo educadamente."', en: '"Thank you so much. Have a great day!"'},
  ],
  23: [
    {pt: '"Peça um cobertor à comissária educadamente."', en: '"Could you bring me a blanket, please?"'},
    {pt: '"Pergunte se tem opção vegetariana."', en: '"Excuse me, is there a vegetarian option?"'},
    {pt: '"Peça permissão para reclinar o assento."', en: '"Could I recline my seat, please?"'},
    {pt: '"Diga que tem turbulência e está um pouco assustada."', en: '"There\'s some turbulence and I\'m a little scared."'},
    {pt: '"Responda ao agente: motivo da viagem."', en: '"I\'m here as a tourist."'},
    {pt: '"Responda: tempo de permanência (10 dias)."', en: '"I\'ll be staying for ten days."'},
    {pt: '"Responda: onde está hospedada (hotel em Paris)."', en: '"I\'m staying at a hotel in Paris."'},
    {pt: '"Responda: nada a declarar."', en: '"I have nothing to declare."'},
  ],
  24: [
    {pt: '"Diga 1 coisa que NÃO conseguia fazer na Aula 1."', en: '"In Aula 1, I couldn\'t introduce myself."'},
    {pt: '"Diga 1 coisa que CONSEGUE fazer agora."', en: '"Now I can talk about my routine in English."'},
    {pt: '"Cite 1 área em que você melhorou."', en: '"I\'ve improved in pronunciation."'},
    {pt: '"Cite 1 área em que ainda está trabalhando."', en: '"I\'m still working on listening."'},
    {pt: '"Diga uma conquista da qual se orgulha."', en: '"I\'m proud that I can speak without fear."'},
    {pt: '"Defina sua próxima meta concreta."', en: '"My next goal is to handle Paris in English in 2027."'},
    {pt: '"Faça uma frase com \'looking back\'."', en: '"Looking back, the first class felt impossible."'},
    {pt: '"Resuma seu progresso em 1 frase para sua mãe."', en: '"Mom, in 24 classes, I went from zero to a real conversation."'},
  ],
  25: [
    {pt: '"Use \'who\' para descrever Blair."', en: '"Blair is the character who has the best style."'},
    {pt: '"Use \'that\' para descrever Friends."', en: '"Friends is a show that takes place in New York."'},
    {pt: '"Diga sua opinião usando \'in my opinion\'."', en: '"In my opinion, Gossip Girl is the best teen show."'},
    {pt: '"Recomende uma série usando \'You should\'."', en: '"You should definitely watch Gilmore Girls."'},
    {pt: '"Descreva o protagonista usando \'main character\' e \'who\'."', en: '"The main character is Rory, who is smart and ambitious."'},
    {pt: '"Diga algo sobre maratonar séries."', en: '"I love to binge-watch series on weekends."'},
    {pt: '"Comente um final de temporada usando \'cliffhanger\'."', en: '"The season finale ends with a huge cliffhanger!"'},
    {pt: '"Em 2 frases, convença sua amiga francesa a assistir Gossip Girl."', en: '"You should watch Gossip Girl. It\'s a show that has drama, fashion and the best plot twists."'},
  ],
};

const errorCorrection = {
  21: [
    {wrong: '"I will to study every day."', right: '"I will study every day." (after will, no "to")'},
    {wrong: '"I no will go to Paris."', right: '"I won\'t go to Paris." or "I will not go to Paris."'},
    {wrong: '"It probably will rain."', right: '"It will probably rain." (probably between will and verb)'},
    {wrong: '"I think will rain in Paris."', right: '"I think it will rain in Paris." (need subject "it")'},
    {wrong: '"I promise study English."', right: '"I promise I will study English." (need "I will")'},
  ],
  22: [
    {wrong: '"Where is the gate?"', right: 'OK — but more polite: "Excuse me, where is the gate, please?"'},
    {wrong: '"I want a window."', right: '"I would like a window seat, please." (more polite + "seat")'},
    {wrong: '"I have a luggages."', right: '"I have luggage." (luggage is uncountable — no "a", no "s")'},
    {wrong: '"My flight is delay."', right: '"My flight is delayed." or "My flight has a delay."'},
    {wrong: '"Can you give me my pass?"', right: '"Could I have my boarding pass, please?" (polite register)'},
  ],
  23: [
    {wrong: '"I am here as tourist."', right: '"I\'m here as a tourist." (need article "a")'},
    {wrong: '"I stay ten days."', right: '"I\'ll be staying for ten days." (use future continuous + "for")'},
    {wrong: '"My accommodation is a Paris."', right: '"My accommodation is in Paris." or "...a hotel in Paris."'},
    {wrong: '"Can I to recline?"', right: '"Could I recline my seat, please?" (no "to" after modal)'},
    {wrong: '"We landing now."', right: '"We are landing now." (present continuous needs "to be")'},
  ],
  24: [
    {wrong: '"In Aula 1, I no can introduce."', right: '"In Aula 1, I couldn\'t introduce myself."'},
    {wrong: '"I have improve in pronunciation."', right: '"I\'ve improved in pronunciation." (present perfect form)'},
    {wrong: '"I still working on listening."', right: '"I\'m still working on listening." (need "am")'},
    {wrong: '"My next goal is be fluent."', right: '"My next goal is to be fluent." (need "to" + verb)'},
    {wrong: '"I am proud my progress."', right: '"I am proud of my progress." (need "of")'},
  ],
  25: [
    {wrong: '"Blair is character is ambitious."', right: '"Blair is a character who is ambitious." (need "a" and "who")'},
    {wrong: '"Friends is show that funny."', right: '"Friends is a show that is funny." (need "a" and "is" after that)'},
    {wrong: '"In my opinion Friends best."', right: '"In my opinion, Friends is the best." (need verb + article)'},
    {wrong: '"You should to watch."', right: '"You should watch it." (no "to" after should + need object)'},
    {wrong: '"I am binge-watch the series."', right: '"I am binge-watching the series." (need -ing form)'},
  ],
};

const productionScenarios = {
  21: [
    {label: 'Stage 1 — Guided', text: 'Gabriela faz 5 predições sobre Paris 2027 com modelo na tela: "I will… I won\'t… I think… I hope… I promise…". Professor sopra próxima palavra se travar.'},
    {label: 'Stage 2 — Semi-free', text: 'Sem modelo. Gabriela escreve 8 frases sobre o futuro próximo (1 ano até a viagem) usando will/won\'t + advérbios. Lê em voz alta.'},
    {label: 'Stage 3 — Free role-play', text: 'Cenário: videocall com a futura host family francesa. Professor é Mme Dubois. 4 minutos de conversa: predições, promessas, dúvidas. Sem script. Feedback retardado: 3 positivos + 2 melhorias.'},
  ],
  22: [
    {label: 'Stage 1 — Guided', text: 'Encenação check-in com modelo da tela. Professor é o agente. Gabriela usa frases-âncora com pista visual.'},
    {label: 'Stage 2 — Semi-free', text: 'Cenário security checkpoint. Sem script. Apenas pistas: "remove shoes", "laptop out", "any liquids". Gabriela navega o controle.'},
    {label: 'Stage 3 — Free role-play', text: 'Cenário: aeroporto inteiro de Guarulhos a Paris. 4 trechos consecutivos: 1) check-in, 2) security, 3) gate (pergunta a outro passageiro sobre atraso), 4) dentro do avião pedindo algo à comissária. Cada trecho 1-2 min.'},
  ],
  23: [
    {label: 'Stage 1 — Guided', text: 'Pedidos no avião (água, cobertor, banheiro) com modelo "Could you/Could I + verbo + please". Professor é a comissária.'},
    {label: 'Stage 2 — Semi-free', text: 'Imigração com pistas mínimas: name, purpose, length, accommodation, declare. Sem script. Professor é o customs officer.'},
    {label: 'Stage 3 — Free role-play', text: 'Cenário: Gabriela acabou de pousar em CDG. Em 5 min, ela passa pela imigração e depois pede direção para a saída de táxi. Dois interlocutores diferentes (officer + airport staff).'},
  ],
  24: [
    {label: 'Stage 1 — Guided', text: 'Auto-avaliação estruturada — Gabriela completa 6 frases: "In Aula 1, I couldn\'t…", "Now I can…", "I\'ve improved in…", "I\'m still working on…", "I\'m proud of…", "My next goal is…".'},
    {label: 'Stage 2 — Semi-free', text: 'Conversa com a teacher de 4 min. Sem perguntas pré-definidas. Apenas tópico: "Tell me your journey from Aula 1 to today".'},
    {label: 'Stage 3 — Free role-play', text: 'Gravação "Progress Report Video" — 2 minutos diretos para a câmera, sem teacher. Tópico livre, mas precisa cobrir: 3 conquistas, 2 áreas de melhoria, 1 meta. Sem script. Feedback após.'},
  ],
  25: [
    {label: 'Stage 1 — Guided', text: 'Descreva 3 personagens com relative clauses (who/that). Modelo na tela. Professor confirma cada estrutura.'},
    {label: 'Stage 2 — Semi-free', text: 'Mini-resenha de série favorita (3 min) sem script. Pistas: enredo, 2 personagens, opinião, recomendação. Use "I think" e "in my opinion".'},
    {label: 'Stage 3 — Free role-play', text: 'Encontro com Léa francesa: 4 min, Gabriela recomenda Gossip Girl. Léa cria objeções ("não gosto de drama", "é muito longa"). Gabriela responde defendendo. Improvisação total.'},
  ],
};

const checklistItems = {
  21: [
    'Sei usar will/won\'t para predições e promessas em inglês.',
    'Sei a diferença entre will (espontâneo/predição) e going to (planejado).',
    'Sei posicionar advérbios (probably, definitely, maybe) corretamente.',
    'Sei usar "I think", "I hope", "I promise" no contexto de futuro.',
    'Fiz role-play com a host family francesa em inglês.',
    'Sei pronunciar "won\'t" sem confundir com "want".',
    'Já gravei minhas previsões para 2027 em áudio.',
    'Homework assigned e entendido.',
  ],
  22: [
    'Sei o vocabulário operacional do aeroporto (passport, gate, boarding pass…).',
    'Sei usar "May I…?" e "Could you…?" em registro polido.',
    'Sei pedir assento na janela ou corredor.',
    'Sei perguntar onde fica o gate corretamente.',
    'Sei reportar atraso de voo em inglês.',
    'Fiz simulação de check-in completa em inglês.',
    'Atravessei security checkpoint sem precisar mudar para o português.',
    'Homework assigned e entendido.',
  ],
  23: [
    'Sei pedir educadamente coisas dentro do avião à comissária.',
    'Respondo a pergunta "purpose of visit" em chunk fixo.',
    'Sei dizer "length of stay" com o número de dias.',
    'Sei o que é "accommodation" e como responder onde estou hospedada.',
    'Fiz simulação de imigração completa em inglês — sem travar.',
    'Sei pronunciar "turbulence", "customs", "accommodation".',
    'Já encarei mentalmente o cenário de chegada em CDG e estou preparada.',
    'Homework assigned e entendido.',
  ],
  24: [
    'Sei contrastar "I couldn\'t" (passado) com "I can" (agora) em inglês.',
    'Sei usar "I\'ve improved in" e "I\'m still working on" sobre meu próprio progresso.',
    'Defini 3 metas concretas e mensuráveis para o Bloco 3.',
    'Comparei minha gravação da Aula 1 com a de hoje e identifiquei diferenças.',
    'Listei 10 palavras 100% confiantes e 5 que precisam mais prática.',
    'Reconheço minhas conquistas sem auto-crítica destrutiva.',
    'Estou comprometida em chegar em Paris 2027 pronta.',
    'Homework assigned e entendido.',
  ],
  25: [
    'Sei usar "who" para descrever pessoas em inglês.',
    'Sei usar "that" para descrever séries, filmes e coisas.',
    'Uso "I think" e "in my opinion" para introduzir opinião em inglês.',
    'Sei recomendar uma série com argumento ("You should…").',
    'Sei o vocabulário de séries: episode, season, plot, main character, villain, binge-watch, cliffhanger.',
    'Fiz role-play recomendando série para uma amiga francesa em inglês.',
    'Sei diferenciar "character" (ficção) de "celebrity" (real).',
    'Homework assigned e entendido.',
  ],
};

module.exports = {
  lessonPromises, lessonImages, lessonHeaderImages, stampImages, stampLabels,
  vocab, matching, fillIn, multipleChoice, ordering, pronunciation, thinkAboutIt, survivalCards,
  grammarTips, lessonObjectives, homework, ccqs, obstacles, dialogues, oralDrills, errorCorrection,
  productionScenarios, checklistItems,
};
