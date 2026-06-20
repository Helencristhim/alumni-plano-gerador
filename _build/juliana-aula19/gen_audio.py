#!/usr/bin/env python3
import os, io, sys, json, time, urllib.request, urllib.error

ROOT = "/home/dan/dev/work/better/wt-jul-a19"
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

LISTEN = ("Hola, soy Diego. Tengo muchos planes para el futuro. El proximo mes voy a empezar un curso "
          "de ingles. El proximo ano pienso mudarme a una ciudad mas grande para trabajar. Tambien voy "
          "a ahorrar dinero para viajar a Europa. Mi meta principal es conseguir un ascenso en mi empresa. "
          "Espero lograr todo esto pronto. Y tu, que planes tienes?")
LISTEN_TTS = ("Hola, soy Diego. Tengo muchos planes para el futuro. El próximo mes voy a empezar un curso "
          "de inglés. El próximo año pienso mudarme a una ciudad más grande para trabajar. También voy "
          "a ahorrar dinero para viajar a Europa. Mi meta principal es conseguir un ascenso en mi empresa. "
          "Espero lograr todo esto pronto. ¿Y tú, qué planes tienes?")

ITEMS = [
 # vocab cards (Gaby)
 ("Manana","aula19_manana.mp3","Mañana",GABY),
 ("El proximo","aula19_el_proximo.mp3","El próximo",GABY),
 ("El futuro","aula19_el_futuro.mp3","El futuro",GABY),
 ("La meta","aula19_la_meta.mp3","La meta",GABY),
 ("El objetivo","aula19_el_objetivo.mp3","El objetivo",GABY),
 ("Pienso","aula19_pienso.mp3","Pienso",GABY),
 ("Espero","aula19_espero.mp3","Espero",GABY),
 ("Quiero","aula19_quiero.mp3","Quiero",GABY),
 ("Ahorrar","aula19_ahorrar.mp3","Ahorrar",GABY),
 ("Mudarse","aula19_mudarse.mp3","Mudarse",GABY),
 # listening monologue (Diego = Juan, male)
 (LISTEN,"aula19_listening_diego.mp3",LISTEN_TTS,JUAN),
 # dialogue Diego (Juan)
 ("Juliana, que vas a hacer el proximo ano?","aula19_dialogo_diego_1.mp3","Juliana, ¿qué vas a hacer el próximo año?",JUAN),
 ("Que bien! Y algun viaje?","aula19_dialogo_diego_2.mp3","¡Qué bien! ¿Y algún viaje?",JUAN),
 ("Cual es tu meta principal?","aula19_dialogo_diego_3.mp3","¿Cuál es tu meta principal?",JUAN),
 # dialogue Juliana (Gaby)
 ("Voy a estudiar mas espanol y quiero un ascenso.","aula19_dialogo_juliana_1.mp3","Voy a estudiar más español y quiero un ascenso.",GABY),
 ("Si, pienso viajar a Peru. Voy a ahorrar dinero.","aula19_dialogo_juliana_2.mp3","Sí, pienso viajar a Perú. Voy a ahorrar dinero.",GABY),
 ("Mi objetivo es hablar espanol con fluidez. Lo voy a lograr!","aula19_dialogo_juliana_3.mp3","Mi objetivo es hablar español con fluidez. ¡Lo voy a lograr!",GABY),
 # loose phrases (listening 2 / survival / speech)
 ("Manana voy a estudiar.","aula19_manana_voy_estudiar.mp3","Mañana voy a estudiar.",GABY),
 ("El proximo ano voy a viajar.","aula19_proximo_ano_viajar.mp3","El próximo año voy a viajar.",JUAN),
 ("Pienso aprender a programar.","aula19_pienso_aprender_programar.mp3","Pienso aprender a programar.",GABY),
 ("Quiero conseguir un ascenso.","aula19_quiero_ascenso.mp3","Quiero conseguir un ascenso.",JUAN),
 ("Mi meta es hablar espanol bien.","aula19_meta_hablar_bien.mp3","Mi meta es hablar español bien.",GABY),
 # order audio (correct sequence)
 ("[order-l19]","aula19_order_l19_ordering.mp3",
   "Mañana voy a estudiar español. El próximo mes voy a empezar un curso. El próximo año pienso viajar a Perú. Voy a ahorrar dinero para el viaje. Mi meta es hablar español con fluidez.",
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
