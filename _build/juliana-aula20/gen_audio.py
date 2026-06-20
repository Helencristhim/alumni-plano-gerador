#!/usr/bin/env python3
import os, io, sys, json, time, urllib.request, urllib.error

ROOT = "/home/dan/dev/work/better/wt-jul-a20"
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

GABY = "5vkxOzoz40FrElmLP4P7"   # F Peruvian = Juliana / female
JUAN = "rBqbBncz61jpuaOTI1GW"   # M Peruvian = Diego / male

# Listening monologue: Diego narrates a full day mixing PAST + FUTURE (review of 18+19),
# plus the city/shopping/restaurant arc (review of 11-14).
LISTEN = ("Hola, soy Diego. Ayer fue un dia muy completo. Por la manana fui de compras y "
          "compre una camisa en una tienda del centro. Despues comi en un restaurante: pedi la "
          "carta y pague la cuenta con tarjeta. Por la tarde tome el metro para volver a casa. "
          "Manana voy a descansar, pero el proximo mes pienso empezar un curso de espanol. Mi "
          "meta es hablar con fluidez. Y tu, que hiciste ayer y que vas a hacer manana?")
LISTEN_TTS = ("Hola, soy Diego. Ayer fue un día muy completo. Por la mañana fui de compras y "
          "compré una camisa en una tienda del centro. Después comí en un restaurante: pedí la "
          "carta y pagué la cuenta con tarjeta. Por la tarde tomé el metro para volver a casa. "
          "Mañana voy a descansar, pero el próximo mes pienso empezar un curso de español. Mi "
          "meta es hablar con fluidez. ¿Y tú, qué hiciste ayer y qué vas a hacer mañana?")

ITEMS = [
 # review "vocab" cards = mixed-tense / arc connectors (Gaby). New audioMap keys.
 ("Ayer fui de compras.","aula20_ayer_fui_compras.mp3","Ayer fui de compras.",GABY),
 ("Comi en un restaurante.","aula20_comi_restaurante.mp3","Comí en un restaurante.",GABY),
 ("Pague la cuenta con tarjeta.","aula20_pague_cuenta_tarjeta.mp3","Pagué la cuenta con tarjeta.",GABY),
 ("Tome el metro al centro.","aula20_tome_metro_centro.mp3","Tomé el metro al centro.",GABY),
 ("Manana voy a descansar.","aula20_manana_descansar.mp3","Mañana voy a descansar.",GABY),
 ("El proximo mes voy a viajar.","aula20_proximo_mes_viajar.mp3","El próximo mes voy a viajar.",GABY),
 ("Pienso estudiar mas espanol.","aula20_pienso_estudiar.mp3","Pienso estudiar más español.",GABY),
 ("Mi meta es hablar con fluidez.","aula20_meta_fluidez.mp3","Mi meta es hablar con fluidez.",GABY),
 # listening monologue (Diego = Juan, male)
 (LISTEN,"aula20_listening_diego.mp3",LISTEN_TTS,JUAN),
 # dialogue Diego (Juan) — asks about Juliana's whole journey, past + future
 ("Juliana, que hiciste el fin de semana pasado?","aula20_dialogo_diego_1.mp3","Juliana, ¿qué hiciste el fin de semana pasado?",JUAN),
 ("Que rico! Y que vas a hacer el proximo ano?","aula20_dialogo_diego_2.mp3","¡Qué rico! ¿Y qué vas a hacer el próximo año?",JUAN),
 ("Tu espanol ha mejorado mucho. Felicidades!","aula20_dialogo_diego_3.mp3","Tu español ha mejorado mucho. ¡Felicidades!",JUAN),
 # dialogue Juliana (Gaby)
 ("Fui de compras y comi en un restaurante nuevo.","aula20_dialogo_juliana_1.mp3","Fui de compras y comí en un restaurante nuevo.",GABY),
 ("Voy a viajar a Peru. Pienso practicar mi espanol alli.","aula20_dialogo_juliana_2.mp3","Voy a viajar a Perú. Pienso practicar mi español allí.",GABY),
 ("Gracias! Aprendi mucho en este curso.","aula20_dialogo_juliana_3.mp3","¡Gracias! Aprendí mucho en este curso.",GABY),
 # loose phrases (listening 2 / survival / speech) — recombined review
 ("Donde esta la farmacia, por favor?","aula20_donde_farmacia.mp3","¿Dónde está la farmacia, por favor?",GABY),
 ("Me gustaria reservar una mesa.","aula20_reservar_mesa.mp3","Me gustaría reservar una mesa.",JUAN),
 ("Cuanto cuesta esta camisa?","aula20_cuanto_cuesta_camisa.mp3","¿Cuánto cuesta esta camisa?",GABY),
 ("Te apetece quedar el sabado?","aula20_te_apetece_quedar.mp3","¿Te apetece quedar el sábado?",JUAN),
 ("Ayer visite a mi familia.","aula20_ayer_visite_familia.mp3","Ayer visité a mi familia.",GABY),
 ("Manana voy a empezar un curso.","aula20_manana_empezar_curso.mp3","Mañana voy a empezar un curso.",JUAN),
 # order audio (correct sequence: a full day past -> future)
 ("[order-l20]","aula20_order_l20_ordering.mp3",
   "Ayer fui de compras por la mañana. Después comí en un restaurante y pagué la cuenta. Por la tarde tomé el metro a casa. Mañana voy a descansar. El próximo mes pienso empezar un curso de español.",
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
