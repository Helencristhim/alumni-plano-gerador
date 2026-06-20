#!/usr/bin/env python3
import os, io, sys, json, time, urllib.request, urllib.error

ROOT = "/home/dan/dev/work/better/wt-jul-a18"
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

LISTEN = ("Hola, soy Diego. El fin de semana pasado lo pase muy bien. El sabado fui a la playa con unos "
          "amigos. Comimos pescado y nadamos un poco. Por la tarde, vi un partido de futbol en un bar. El "
          "domingo visite un museo en el centro y despues camine por el parque. Por la noche cene en casa "
          "con mi familia y descanse. Manana te cuento mas. Un abrazo.")
LISTEN_TTS = ("Hola, soy Diego. El fin de semana pasado lo pasé muy bien. El sábado fui a la playa con unos "
          "amigos. Comimos pescado y nadamos un poco. Por la tarde, vi un partido de fútbol en un bar. El "
          "domingo visité un museo en el centro y después caminé por el parque. Por la noche cené en casa "
          "con mi familia y descansé. Mañana te cuento más. Un abrazo.")

ITEMS = [
 # vocab cards (Gaby)
 ("Ayer","aula18_ayer.mp3","Ayer",GABY),
 ("Anoche","aula18_anoche.mp3","Anoche",GABY),
 ("El fin de semana pasado","aula18_fin_semana_pasado.mp3","El fin de semana pasado",GABY),
 ("La playa","aula18_la_playa.mp3","La playa",GABY),
 ("El museo","aula18_el_museo.mp3","El museo",GABY),
 ("Fui","aula18_fui.mp3","Fui",GABY),
 ("Comi","aula18_comi.mp3","Comí",GABY),
 ("Visite","aula18_visite.mp3","Visité",GABY),
 ("Vi","aula18_vi.mp3","Vi",GABY),
 ("Hice","aula18_hice.mp3","Hice",GABY),
 # listening monologue (Diego = Juan, male)
 (LISTEN,"aula18_listening_diego.mp3",LISTEN_TTS,JUAN),
 # dialogue Diego (Juan)
 ("Juliana, que hiciste el fin de semana?","aula18_dialogo_diego_1.mp3","Juliana, ¿qué hiciste el fin de semana?",JUAN),
 ("Que bien! Y el domingo?","aula18_dialogo_diego_2.mp3","¡Qué bien! ¿Y el domingo?",JUAN),
 ("Hiciste algo mas?","aula18_dialogo_diego_3.mp3","¿Hiciste algo más?",JUAN),
 # dialogue Juliana (Gaby)
 ("El sabado fui a la playa y comi pescado.","aula18_dialogo_juliana_1.mp3","El sábado fui a la playa y comí pescado.",GABY),
 ("El domingo visite un museo y vi una exposicion.","aula18_dialogo_juliana_2.mp3","El domingo visité un museo y vi una exposición.",GABY),
 ("Por la noche descanse en casa. Fue un buen fin de semana!","aula18_dialogo_juliana_3.mp3","Por la noche descansé en casa. ¡Fue un buen fin de semana!",GABY),
 # loose phrases (listening 2 / fill / survival / speech)
 ("Ayer fui al cine.","aula18_ayer_fui_cine.mp3","Ayer fui al cine.",GABY),
 ("Comi en un restaurante.","aula18_comi_restaurante.mp3","Comí en un restaurante.",JUAN),
 ("El sabado visite un museo.","aula18_sabado_visite_museo.mp3","El sábado visité un museo.",GABY),
 ("Vi una pelicula muy buena.","aula18_vi_pelicula_buena.mp3","Vi una película muy buena.",JUAN),
 ("El domingo hice deporte.","aula18_domingo_hice_deporte.mp3","El domingo hice deporte.",GABY),
 # order audio (correct sequence)
 ("[order-l18]","aula18_order_l18_ordering.mp3",
   "El sábado fui a la playa. Allí comí pescado fresco. El domingo visité un museo. Vi una exposición muy bonita. Por la noche descansé en casa.",
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
