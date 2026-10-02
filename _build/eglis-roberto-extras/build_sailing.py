# -*- coding: utf-8 -*-
"""Aba suplementar do Eglis Roberto: Sailing English.

Promessa da consultoria de 02/10/2026: ele e velejador, no time de vela se fala muito ingles, e ha
vagas de tripulacao na Europa (Mediterraneo), nos EUA e no Caribe. 'E tao importante isso para mim,
eu me sinto mais confiante em conseguir um emprego.' Tudo em ingles na tela (B1+). So chama funcoes
que ja existem no hub (toggleLesson, speakText, speakPhrase, startRecording, stopRecording,
startFreeRecording, stopFreeRecording). Sem fill-in, matching nem quiz: nada que o loadState
restaure por texto e possa colidir com as aulas."""
import os
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
from sail_helpers import card_open, CARD_CLOSE, section, speech, free, listen_btn, transcript, tab, rule_box, table, bullets  # noqa: E402


def words(rows):
    return table(['Word', 'What it means', 'Example'], rows)


# (titulo, imagem, sotaque, texto modelo, quadro de palavras, frases para repetir, pedido de gravacao)
CARDS = [
    ('The Boat', 'photo-1540946485063-a40da27545f8', 'british_m',
     "Welcome aboard. Before we sail, let me show you the boat. The front is the bow, and the back is the stern. "
     "When you look forward, port is on your left and starboard is on your right. The mast holds the sails, and the boom is the long pole at the bottom of the mainsail. "
     "Watch your head when the boom moves. Under the water we have the keel, which keeps us upright, and the rudder, which steers. "
     "I will be at the helm, in the cockpit. Any questions?",
     [('Bow / stern', 'the front / the back of the boat', 'Put the fenders near the bow.'),
      ('Port / starboard', 'the left / the right side, looking forward', 'There is a ferry on our starboard side.'),
      ('Mast / boom', 'the tall pole / the low pole that holds the bottom of the mainsail', 'Mind the boom!'),
      ('Hull / keel', 'the body of the boat / the heavy fin under the water', 'The hull is fiberglass.'),
      ('Rudder / helm', 'the part that steers / the wheel or tiller you steer with', 'Can you take the helm for ten minutes?'),
      ('Cockpit / deck', 'the space where the crew sits / the flat surface you walk on', 'Clip on before you go on deck.')],
     ["Port is on the left when you look forward.", "Mind the boom when we turn.",
      "Can you take the helm for a few minutes?", "I'll go forward to the bow."],
     'You are giving a tour of your boat to a new crew member. In one minute, show them the boat from the bow to the stern.'),

    ('Lines and Sails', 'photo-1500514966906-fe245eea9344', 'us_m',
     "On a boat, a rope is not called a rope. It is a line, and every line has a name. A halyard pulls a sail up. "
     "A sheet controls the angle of a sail. We have a mainsail and a jib, or a bigger genoa on some boats. "
     "To pull a line tight, you put it around a winch and turn the handle. When it is tight, you make it fast on a cleat. "
     "If the wind gets strong, we reef the main, which means we make it smaller.",
     [('A line', 'any rope on a boat', 'Coil that line and hang it up.'),
      ('A halyard', 'the line that pulls a sail up the mast', 'Pull the main halyard.'),
      ('A sheet', 'the line that controls the angle of a sail', 'Ease the jib sheet a little.'),
      ('Mainsail / jib / genoa', 'the big sail behind the mast / the sail in front / a bigger front sail', 'We sailed with only the genoa.'),
      ('A winch', 'a drum with a handle that helps you pull a line', 'Put two turns on the winch.'),
      ('A cleat', 'a metal piece where you tie a line', 'Make it fast on the cleat.'),
      ('To hoist / to reef', 'to pull a sail up / to make a sail smaller in strong wind', 'Let us reef before the wind gets stronger.')],
     ["Pull the main halyard, please.", "Put two turns on the winch.",
      "Make it fast on the cleat.", "We should reef before it gets dark."],
     'Explain to a friend who has never sailed the difference between a halyard and a sheet, and why we reef. Thirty seconds.'),

    ('Commands on Deck', 'photo-1528154291023-a6525fabe5b4', 'british_m',
     "On deck, every command has an answer. When I want to tack, I call: ready about. You prepare your sheet, and you answer: ready. "
     "Then I call: lee-ho, and I turn the boat through the wind. To gybe, it is the same: prepare to gybe, ready, gybe-ho. "
     "If I say ease the sheet, you let it out a little. If I say trim, you pull it in. Never be quiet on deck. "
     "If you are not ready, say so. A loud question is better than a silent mistake.",
     [('Ready about!', 'get ready, we are going to tack (turn the bow through the wind)', 'Ready about! / Ready!'),
      ('Lee-ho! / Helm&rsquo;s a-lee!', 'we are tacking now (British / American)', 'Lee-ho! Release the jib sheet.'),
      ('Prepare to gybe! / Gybe-ho!', 'get ready / we are turning the stern through the wind now', 'Prepare to gybe! Watch the boom.'),
      ('Ease / trim', 'to let a sheet out / to pull it in', 'Ease the main a little.'),
      ('Make fast', 'tie the line so it does not move', 'Make fast the bow line.'),
      ('Fend off!', 'push the boat away from another boat or the dock', 'Fend off at the stern!')],
     ["Ready about!", "Ready!", "Ease the main a little.", "Sorry, I'm not ready yet. Give me five seconds."],
     'You are the skipper. Give the commands for a tack, and then for a gybe, with the answers of the crew. Say them clearly and loudly.'),

    ('Wind, Weather and Points of Sail', 'photo-1559827260-dc66d52bef19', 'us_f',
     "Good morning, crew. Here is the forecast. The wind is from the northeast, fifteen to twenty knots, with gusts of twenty-five in the afternoon. "
     "There is a swell of about two meters. In the morning we will sail close-hauled, so the boat will heel quite a lot. "
     "After the point, we turn and we will be on a broad reach, which is much more comfortable. "
     "There is a small chance of a squall later, so we will reef early and keep the life jackets on.",
     [('Upwind / close-hauled', 'sailing as close to the wind as possible', 'Close-hauled, the boat heels a lot.'),
      ('Beam reach / broad reach', 'the wind from the side / from behind the side', 'A broad reach is the most comfortable.'),
      ('Downwind / running', 'sailing with the wind behind you', 'Running downwind, watch the boom.'),
      ('A knot', 'one nautical mile per hour (and also a tie in a line)', 'We are doing seven knots.'),
      ('A gust / a squall', 'a sudden strong wind / a short storm with strong wind and rain', 'A squall hit us at midnight.'),
      ('A swell', 'long waves that come from far away', 'The swell was two meters.'),
      ('To heel', 'to lean to one side because of the wind', 'Do not worry, all sailboats heel.')],
     ["The wind is from the northeast, fifteen knots.", "We'll be close-hauled all morning.",
      "There's a squall coming. Let's reef now.", "The swell is bigger than the forecast said."],
     'Give the weather briefing for tomorrow to your crew: the wind, the waves, the point of sail and one safety decision. One minute.'),

    ('Radio and Safety', 'photo-1505228395891-9a51e7e86bf6', 'british_m',
     "Channel sixteen on the VHF radio is for calling and for emergencies. There are three levels of call. "
     "Mayday, three times, is for grave and immediate danger to the boat or to a person. Pan-Pan, three times, is urgent but not a danger to life. "
     "Securite, three times, is safety information, like a navigation warning. For names and letters, use the phonetic alphabet: alpha, bravo, charlie. "
     "And if somebody falls into the water, shout: man overboard, point at the person, and never stop pointing.",
     [('VHF / channel 16', 'the marine radio / the channel for calling and emergencies', 'Call the marina on channel sixteen.'),
      ('Mayday', 'grave and immediate danger to the boat or to a life', 'Mayday, Mayday, Mayday.'),
      ('Pan-Pan', 'urgent, but no immediate danger to life', 'Pan-Pan: our engine has failed.'),
      ('Securite', 'safety information for other boats', 'Securite: a container is floating at this position.'),
      ('Man overboard!', 'a person has fallen into the water', 'Man overboard! Keep pointing!'),
      ('Life jacket / harness', 'the vest that keeps you up in the water / the strap that clips you to the boat', 'At night, harness on and clipped in.'),
      ('Over / out', 'I have finished, please answer / the conversation has ended', 'Thank you, over.')],
     ["Mayday, Mayday, Mayday. This is sailing yacht Blue Wind.", "Our position is two miles south of the harbor.",
      "We have four people on board. Over.", "Man overboard! I'm pointing at him!"],
     'Practice a Mayday call with your boat name: who you are, where you are, what is wrong, how many people, and what you need. Clear and slow.'),

    ('In the Marina', 'photo-1567899378494-47b22a2ae96a', 'us_m',
     "Arriving at a marina is often the most stressful part of the day. First, call the marina office on the radio and ask for a berth for the night. "
     "They will tell you the pontoon and the number. Before you come in, put the fenders out on both sides and prepare the bow and stern lines. "
     "When you come alongside, one person steps off with a line, never jumps. Then we tie up, check the lines, and go to the office to pay. "
     "And the first question after that is always the same: where is the fuel dock?",
     [('A berth', 'a place for a boat in a marina', 'Do you have a berth for one night?'),
      ('A pontoon / a dock', 'the floating walkway / the place where boats tie up', 'You are on pontoon C, number 12.'),
      ('Fenders', 'soft cushions that protect the hull', 'Fenders out on both sides.'),
      ('Mooring lines', 'the lines that tie the boat to the dock', 'Prepare the bow and stern lines.'),
      ('To come alongside', 'to bring the boat next to a dock or another boat', 'We are coming alongside now.'),
      ('To tie up', 'to secure the boat with lines', 'Tie up and check the lines.'),
      ('The fuel dock', 'the place where boats buy fuel', 'The fuel dock closes at six.')],
     ["Marina, this is sailing yacht Blue Wind. Do you have a berth for one night?", "Fenders out on both sides, please.",
      "Step off with the bow line. Don't jump.", "Excuse me, what time does the fuel dock close?"],
     'Call the marina office on the radio and ask for a berth for two nights for a twelve-meter boat. Then ask about water and fuel.'),

    ('Life on Board', 'photo-1534447677768-be436bb09401', 'us_f',
     "On a delivery, the boat never stops, so the crew works in watches. I am usually on watch from midnight to four, with one other person. "
     "We check the course, the wind and the other ships, and we write everything in the log. Off watch, you sleep in your bunk, even in the day. "
     "Everybody cooks in the galley, and everybody cleans the head, which is the toilet. Stow everything after you use it, because the boat moves all the time. "
     "And if you feel seasick, tell the skipper early. It happens to everybody.",
     [('A watch / to be on watch', 'a period of duty on deck / to be the person responsible now', 'I am on watch from midnight to four.'),
      ('A night watch', 'a watch during the night', 'My first night watch was beautiful.'),
      ('The log', 'the book where you write the course, the wind and events', 'Write the position in the log every hour.'),
      ('A bunk', 'a bed on a boat', 'My bunk was in the bow, and it moved a lot.'),
      ('The galley / the head', 'the kitchen / the toilet on a boat', 'Dinner is ready in the galley.'),
      ('To stow', 'to put something away safely', 'Stow your bag before we leave.'),
      ('Seasick', 'feeling sick because of the movement of the boat', 'I was seasick for the first two days.')],
     ["I'm on watch from midnight to four.", "Can you write our position in the log?",
      "Stow everything before we set off.", "I feel a bit seasick. Can I stay on deck?"],
     'Describe twenty-four hours on a delivery: your watch, what you do on watch, where you sleep, and who cooks. One minute.'),

    ('The Crew Interview', 'photo-1569263979104-865ab7cd8d13', 'british_m',
     "So, you want to join us for the delivery to the Caribbean. Let me ask you a few questions. How much sailing experience do you have, "
     "and how many sea miles have you done? Have you ever done night watches, or an ocean crossing? Do you have any certificates, "
     "like an RYA course or STCW basic safety? How do you deal with living in a small space with five people for three weeks? "
     "And finally, why do you want to do this? Take your time. I am not looking for a perfect answer. I am looking for an honest one.",
     [('Sea miles', 'the distance you have sailed, often written in a logbook', 'I have done about three thousand sea miles.'),
      ('A delivery', 'taking a boat from one place to another for the owner', 'It is a delivery from Mallorca to Antigua.'),
      ('An ocean crossing', 'sailing across an ocean, many days without land', 'I have never done an ocean crossing yet.'),
      ('Competent Crew / Day Skipper', 'two RYA sailing courses, from the British Royal Yachting Association', 'I am planning to do my Day Skipper.'),
      ('STCW basic safety', 'the safety training that professional yacht crew need', 'Professional crew need STCW basic safety.'),
      ('A crew member / a deckhand', 'a person who works on the boat / a crew member who works on deck', 'They are looking for a deckhand for the season.'),
      ('An EU passport', 'a passport from the European Union, useful to work on boats in Europe', 'I have an Italian passport, so I can work in the EU.')],
     ["I have been sailing for many years, mostly racing with my team.",
      "I have done night watches, but I have never done an ocean crossing.",
      "I'm used to living in small spaces. I backpacked for two months and walked the Camino.",
      "I have an Italian passport, so I can work on boats in Europe."],
     'Answer the skipper&rsquo;s three hardest questions, recorded, one minute each: your experience, how you live in a small space with strangers, and why you want to do this.'),

    ('Sea Stories at the Marina Bar', 'photo-1534008897995-27a23e859048', 'us_m',
     "The best part of a sailing day often happens after it, at the bar of the marina. Everybody has a story. "
     "Last summer we were sailing to an island off the coast when a squall hit us. The forecast had said ten knots, and suddenly we had thirty. "
     "We had not reefed, so the boat was heeling like crazy. Somebody was making sandwiches in the galley, and they all ended up on the floor. "
     "We reefed, we survived, and we laughed about it for a week. So, what is your best sea story?",
     [('To get caught in', 'to be in bad weather that you did not expect', 'We got caught in a storm off the coast.'),
      ('Off the coast', 'in the sea, near the land', 'We anchored off the coast of Croatia.'),
      ('To anchor', 'to drop the anchor and stay in one place', 'We anchored in a quiet bay for the night.'),
      ('A close call', 'a dangerous moment that almost became an accident', 'That was a close call.'),
      ('Flat calm', 'no wind and no waves at all', 'It was flat calm, so we used the engine.'),
      ('To beat (upwind)', 'to sail against the wind for a long time', 'We beat upwind for six hours.')],
     ["We got caught in a squall off the coast.", "The forecast had said ten knots.",
      "That was a close call.", "So, what's your best sea story?"],
     'Tell your best sea story at the marina bar, in about one minute: where you were, what was happening, what had happened before, and how it ended.'),
]

body = ''
for i, (title, img, acc, text, rows, lines, prompt) in enumerate(CARDS, 1):
    body += card_open(f'sl-card-{i}', img, f'Sailing English {i:02d}', title,
                      'A short model from a real situation on a boat, the words you need, and your own recording.')
    body += section('Step 1: Listen to the model', 'badge-quiz', 'Listening',
                    'Listen twice with the transcript closed. Then open it and read along.',
                    listen_btn(text, acc) + transcript(text))
    body += section('Step 2: The words', 'badge-vocab', 'Vocabulary',
                    'Read the words and the examples out loud.', words(rows))
    body += section('Step 3: Say it like the crew', 'badge-speak', 'Speaking',
                    'Listen, then record each sentence. Clear and calm: on deck, clear is more important than fast.',
                    ''.join(speech(l) for l in lines))
    body += section('Step 4: Your turn', 'badge-think', 'Recording', 'Record your answer. Then listen once and record it again.',
                    free(f'sl-free-{i}', prompt))
    body += CARD_CLOSE

SAILING = tab('sailing', 'Sailing English',
    'You told us that sailing is important to you, and that a crew job in the Mediterranean, the United States or the Caribbean '
    'needs English. This tab is for that: the boat, the lines, the commands, the weather, the radio, the marina, life on board, '
    'the crew interview and the stories at the bar. One card a day. Every card has a model to listen to, the words, and your own recording.',
    rule_box('How to use this tab.', 'Do the cards in order the first time. Say every sentence out loud, even the commands: '
             'on deck, nobody reads. Before a real interview, do card 8 three days in a row.') + body +
    bullets('Before a real crew job', [
        'Have your sailing experience in one sentence: how many years, what kind of sailing, and the longest trip.',
        'Know your sea miles, roughly. Skippers ask.',
        'Check which certificates the job asks for. Professional yacht crew usually need STCW basic safety and a medical certificate.',
        'Say your Italian passport early: it makes it easier to work on boats in Europe.',
        'Prepare one good sea story. At the interview and at the bar, it is the thing people remember.',
    ]))

open(os.path.join(AQUI, 'sailing.html'), 'w', encoding='utf-8').write(SAILING)
print('sailing.html', len(SAILING), 'cards', len(CARDS))
