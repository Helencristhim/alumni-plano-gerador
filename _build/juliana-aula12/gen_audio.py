#!/usr/bin/env python3
import os, io, sys, json, time, urllib.request, urllib.error

ROOT = "/home/dan/dev/work/better/wt-juliana-a12"
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

GABY = "5vkxOzoz40FrElmLP4P7"        # F Peruvian = Juliana / female
JUAN = "rBqbBncz61jpuaOTI1GW"        # M Peruvian = Diego / male

# (audioMap_key, mp3_filename, tts_text_accented, voice)
ITEMS = [
 # vocab cards (Gaby = protagonist female voice for word-cards)
 ("Seguir recto","aula12_seguir_recto.mp3","Seguir recto",GABY),
 ("Girar","aula12_girar.mp3","Girar",GABY),
 ("Doblar","aula12_doblar.mp3","Doblar",GABY),
 ("Cruzar","aula12_cruzar.mp3","Cruzar",GABY),
 ("El semaforo","aula12_el_semaforo.mp3","El semáforo",GABY),
 ("El cruce","aula12_el_cruce.mp3","El cruce",GABY),
 ("La avenida","aula12_la_avenida.mp3","La avenida",GABY),
 ("A la derecha","aula12_a_la_derecha.mp3","A la derecha",GABY),
 ("A la izquierda","aula12_a_la_izquierda.mp3","A la izquierda",GABY),
 ("Al final de","aula12_al_final_de.mp3","Al final de",GABY),
 # listening monologue (Diego = Juan)
 ("Hola, soy Diego. Para llegar a mi oficina es facil. Sal de la estacion y sigue recto por la avenida principal. Cruza la calle en el primer semaforo. Despues gira a la derecha en el cruce. Sigue una cuadra mas y dobla a la izquierda. Mi oficina esta al final de la calle, al lado de la farmacia. Son diez minutos a pie.",
   "aula12_listening_diego.mp3",
   "Hola, soy Diego. Para llegar a mi oficina es fácil. Sal de la estación y sigue recto por la avenida principal. Cruza la calle en el primer semáforo. Después gira a la derecha en el cruce. Sigue una cuadra más y dobla a la izquierda. Mi oficina está al final de la calle, al lado de la farmacia. Son diez minutos a pie.",
   JUAN),
 # dialogue Juliana (Gaby)
 ("Disculpe, como llego a la plaza?","aula12_dialogo_juliana_1.mp3","Disculpe, ¿cómo llego a la plaza?",GABY),
 ("Y despues cruzo la calle?","aula12_dialogo_juliana_2.mp3","¿Y después cruzo la calle?",GABY),
 ("Esta lejos?","aula12_dialogo_juliana_3.mp3","¿Está lejos?",GABY),
 # dialogue Diego (Juan)
 ("Sigue recto dos cuadras y gira a la derecha.","aula12_dialogo_diego_1.mp3","Sigue recto dos cuadras y gira a la derecha.",JUAN),
 ("Si, cruza en el semaforo. La plaza esta al final.","aula12_dialogo_diego_2.mp3","Sí, cruza en el semáforo. La plaza está al final.",JUAN),
 ("No, son cinco minutos. Buen camino!","aula12_dialogo_diego_3.mp3","No, son cinco minutos. ¡Buen camino!",JUAN),
 # listening 2 / loose direction sentences
 ("Sigue recto dos cuadras.","aula12_sigue_recto_dos.mp3","Sigue recto dos cuadras.",JUAN),
 ("Gira a la derecha en el semaforo.","aula12_gira_derecha_semaforo.mp3","Gira a la derecha en el semáforo.",GABY),
 ("Cruza la calle en el cruce.","aula12_cruza_cruce.mp3","Cruza la calle en el cruce.",JUAN),
 ("Dobla a la izquierda en la avenida.","aula12_dobla_izq_avenida.mp3","Dobla a la izquierda en la avenida.",GABY),
 ("Esta al final de la calle.","aula12_al_final_calle.mp3","Está al final de la calle.",JUAN),
 # order audio (correct sequence of the P1 exchange)
 ("[order-l12]","aula12_order_l12_ordering.mp3",
   "Disculpe, ¿cómo llego a la plaza? Sigue recto dos cuadras y gira a la derecha. ¿Y después cruzo la calle? Sí, cruza en el semáforo. La plaza está al final. Gracias. ¿Está lejos?",
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
            print("OK", fname, n, "bytes")
            ok+=1; break
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
