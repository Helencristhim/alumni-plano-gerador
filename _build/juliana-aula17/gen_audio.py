#!/usr/bin/env python3
import os, io, sys, json, time, urllib.request, urllib.error

ROOT = "/home/dan/dev/work/better/wt-jul-a17"
OUT = os.path.join(ROOT, "public/audio/juliana-marques")
os.makedirs(OUT, exist_ok=True)

KEY = os.environ.get("ELEVENLABS_API_KEY")
if not KEY:
    for envp in [os.path.join(ROOT, ".env.local"), "/home/dan/dev/work/better/alumni-plano-gerador/.env.local"]:
        if os.path.exists(envp):
            for line in io.open(envp):
                if line.startswith("ELEVENLABS_API_KEY"):
                    KEY = line.split("=",1)[1].strip().strip('"').strip("'")
if not KEY:
    print("NO API KEY"); sys.exit(1)

GABY = "5vkxOzoz40FrElmLP4P7"   # F Peruvian = Juliana / Carmen / female
JUAN = "rBqbBncz61jpuaOTI1GW"   # M Peruvian = Diego / male

LISTEN = ("Hola, soy Carmen. Te llamo para invitarte a mi fiesta de cumpleanos. Es el sabado por la "
          "noche, a las nueve, en mi casa. Habra cena y musica. Despues, los que quieran, vamos a tomar "
          "una copa cerca. Dime si estas disponible, por favor. Si te apetece venir, trae a un amigo. "
          "Quedamos a las nueve. Espero verte. Un abrazo.")
LISTEN_TTS = ("Hola, soy Carmen. Te llamo para invitarte a mi fiesta de cumpleaños. Es el sábado por la "
          "noche, a las nueve, en mi casa. Habrá cena y música. Después, los que quieran, vamos a tomar "
          "una copa cerca. Dime si estás disponible, por favor. Si te apetece venir, trae a un amigo. "
          "Quedamos a las nueve. Espero verte. Un abrazo.")

ITEMS = [
 # vocab cards (Gaby)
 ("Quedar","aula17_quedar.mp3","Quedar",GABY),
 ("El plan","aula17_el_plan.mp3","El plan",GABY),
 ("La invitacion","aula17_la_invitacion.mp3","La invitación",GABY),
 ("El cine","aula17_el_cine.mp3","El cine",GABY),
 ("La cena","aula17_la_cena.mp3","La cena",GABY),
 ("La copa","aula17_la_copa.mp3","La copa",GABY),
 ("La fiesta","aula17_la_fiesta.mp3","La fiesta",GABY),
 ("La entrada","aula17_la_entrada.mp3","La entrada",GABY),
 ("El cumpleanos","aula17_el_cumpleanos.mp3","El cumpleaños",GABY),
 ("Disponible","aula17_disponible.mp3","Disponible",GABY),
 # listening monologue (Carmen = Gaby, female)
 (LISTEN,"aula17_listening_carmen.mp3",LISTEN_TTS,GABY),
 # dialogue Juliana (Gaby)
 ("Diego, te apetece ir al cine el viernes?","aula17_dialogo_juliana_1.mp3","Diego, ¿te apetece ir al cine el viernes?",GABY),
 ("Quedamos a las ocho? Yo compro las entradas.","aula17_dialogo_juliana_2.mp3","¿Quedamos a las ocho? Yo compro las entradas.",GABY),
 ("Claro! Quedamos en la puerta del cine?","aula17_dialogo_juliana_3.mp3","¡Claro! ¿Quedamos en la puerta del cine?",GABY),
 # dialogue Diego (Juan)
 ("Me encantaria! A que hora quedamos?","aula17_dialogo_diego_1.mp3","¡Me encantaría! ¿A qué hora quedamos?",JUAN),
 ("Perfecto. Y despues tomamos una copa?","aula17_dialogo_diego_2.mp3","Perfecto. ¿Y después tomamos una copa?",JUAN),
 ("Genial! Hasta el viernes.","aula17_dialogo_diego_3.mp3","¡Genial! Hasta el viernes.",JUAN),
 # loose phrases (listening 2 / fill / survival / speech)
 ("Te apetece ir al cine?","aula17_te_apetece_cine.mp3","¿Te apetece ir al cine?",GABY),
 ("Quedamos el sabado a las ocho.","aula17_quedamos_sabado_ocho.mp3","Quedamos el sábado a las ocho.",JUAN),
 ("Me encantaria, gracias.","aula17_me_encantaria_gracias.mp3","Me encantaría, gracias.",GABY),
 ("Lo siento, no puedo hoy.","aula17_lo_siento_no_puedo_hoy.mp3","Lo siento, no puedo hoy.",JUAN),
 ("Estas disponible el viernes?","aula17_estas_disponible_viernes.mp3","¿Estás disponible el viernes?",GABY),
 ("Lo siento, no puedo. Quizas otro dia.","aula17_lo_siento_quizas_otro_dia.mp3","Lo siento, no puedo. Quizás otro día.",GABY),
 # order audio (correct sequence)
 ("[order-l17]","aula17_order_l17_ordering.mp3",
   "¿Te apetece ir al cine el viernes? ¡Me encantaría! ¿A qué hora quedamos? ¿Quedamos a las ocho? Perfecto. ¿Dónde quedamos? En la puerta del cine. ¡Hasta el viernes!",
   GABY),
]

def tts(text, voice, out_path):
    url = "https://api.elevenlabs.io/v1/text-to-speech/%s" % voice
    body = json.dumps({
        "text": text,
        "model_id": "eleven_multilingual_v2",
        "voice_settings": {"stability":0.5,"similarity_boost":0.75,"style":0.0,"use_speaker_boost":True}
    }).encode("utf-8")
    req = urllib.request.Request(url, data=body, method="POST", headers={
        "xi-api-key": KEY, "Content-Type":"application/json", "Accept":"audio/mpeg"})
    with urllib.request.urlopen(req, timeout=120) as r:
        data = r.read()
    with open(out_path, "wb") as f:
        f.write(data)
    return len(data)

ok=0; fail=0
for key, fname, text, voice in ITEMS:
    out = os.path.join(OUT, fname)
    if os.path.exists(out) and os.path.getsize(out) > 1000:
        print("skip", fname); ok+=1; continue
    for attempt in range(3):
        try:
            n = tts(text, voice, out)
            print("OK", fname, n, "bytes"); ok+=1; break
        except urllib.error.HTTPError as e:
            print("HTTP", e.code, fname, e.read()[:200])
            if e.code==429: time.sleep(10)
            else: time.sleep(3)
        except Exception as e:
            print("ERR", fname, e); time.sleep(3)
    else:
        fail+=1
    time.sleep(0.4)

print("DONE ok=%d fail=%d total=%d" % (ok, fail, len(ITEMS)))
