#!/usr/bin/env python3
import os, io, sys, json, time, urllib.request, urllib.error

ROOT = "/home/dan/dev/work/better/wt-juliana-a11"
OUT = os.path.join(ROOT, "public/audio/juliana-marques")
os.makedirs(OUT, exist_ok=True)

# load key from canonical .env.local
KEY = None
for envp in [os.path.join(ROOT, ".env.local"), "/home/dan/dev/work/better/alumni-plano-gerador/.env.local"]:
    if os.path.exists(envp):
        for line in io.open(envp):
            if line.startswith("ELEVENLABS_API_KEY"):
                KEY = line.split("=",1)[1].strip().strip('"').strip("'")
if not KEY:
    print("NO API KEY"); sys.exit(1)

GABY = "5vkxOzoz40FrElmLP4P7"        # F Peruvian = Juliana
JUAN = "rBqbBncz61jpuaOTI1GW"        # M Peruvian = Diego / male

# (audioMap_key, mp3_filename, tts_text_accented, voice)
ITEMS = [
 # vocab nouns (Gaby - protagonist gender)
 ("El banco","aula11_el_banco.mp3","El banco",GABY),
 ("La farmacia","aula11_la_farmacia.mp3","La farmacia",GABY),
 ("El supermercado","aula11_el_supermercado.mp3","El supermercado",GABY),
 ("La parada","aula11_la_parada.mp3","La parada",GABY),
 ("La plaza","aula11_la_plaza.mp3","La plaza",GABY),
 ("La esquina","aula11_la_esquina.mp3","La esquina",GABY),
 ("La cuadra","aula11_la_cuadra.mp3","La cuadra",GABY),
 ("El ayuntamiento","aula11_el_ayuntamiento.mp3","El ayuntamiento",GABY),
 ("La comisaria","aula11_la_comisaria.mp3","La comisaría",GABY),
 ("El quiosco","aula11_el_quiosco.mp3","El quiosco",GABY),
 # listening monologue (Diego = Juan)
 ("Hola, soy Diego. Mi barrio es muy practico. Hay un banco y una farmacia en la esquina. El supermercado esta al lado de mi edificio. Enfrente de la plaza hay un quiosco donde compro el periodico. El ayuntamiento esta entre el banco y la plaza. La parada del autobus esta a una cuadra. La comisaria esta un poco lejos, a cinco cuadras.",
   "aula11_listening_diego.mp3",
   "Hola, soy Diego. Mi barrio es muy práctico. Hay un banco y una farmacia en la esquina. El supermercado está al lado de mi edificio. Enfrente de la plaza hay un quiosco donde compro el periódico. El ayuntamiento está entre el banco y la plaza. La parada del autobús está a una cuadra. La comisaría está un poco lejos, a cinco cuadras.",
   JUAN),
 # dialogue Juliana (Gaby)
 ("Diego, hay un banco cerca de la oficina?","aula11_dialogo_juliana_1.mp3","Diego, ¿hay un banco cerca de la oficina?",GABY),
 ("Perfecto! Y donde esta la farmacia?","aula11_dialogo_juliana_2.mp3","¡Perfecto! ¿Y dónde está la farmacia?",GABY),
 ("Y el ayuntamiento? Esta lejos?","aula11_dialogo_juliana_3.mp3","¿Y el ayuntamiento? ¿Está lejos?",GABY),
 # dialogue Diego (Juan)
 ("Si, hay uno en la esquina, al lado del supermercado.","aula11_dialogo_diego_1.mp3","Sí, hay uno en la esquina, al lado del supermercado.",JUAN),
 ("Esta enfrente de la plaza, a dos cuadras de aqui.","aula11_dialogo_diego_2.mp3","Está enfrente de la plaza, a dos cuadras de aquí.",JUAN),
 ("No, esta cerca, entre el banco y la plaza.","aula11_dialogo_diego_3.mp3","No, está cerca, entre el banco y la plaza.",JUAN),
 # listening 2 loose sentences (alternate)
 ("Hay un banco en la esquina.","aula11_hay_banco_esquina.mp3","Hay un banco en la esquina.",GABY),
 ("La farmacia esta al lado del supermercado.","aula11_farmacia_lado_super.mp3","La farmacia está al lado del supermercado.",JUAN),
 ("La plaza esta enfrente del ayuntamiento.","aula11_plaza_enfrente_ayto.mp3","La plaza está enfrente del ayuntamiento.",GABY),
 ("La parada esta a dos cuadras de aqui.","aula11_parada_dos_cuadras.mp3","La parada está a dos cuadras de aquí.",JUAN),
 ("El quiosco esta entre el banco y la plaza.","aula11_quiosco_entre.mp3","El quiosco está entre el banco y la plaza.",GABY),
 # survival / speech / fill phrases
 ("Hay un banco por aqui?","aula11_hay_banco_por_aqui.mp3","¿Hay un banco por aquí?",GABY),
 ("Donde esta la farmacia?","aula11_donde_farmacia.mp3","¿Dónde está la farmacia?",JUAN),
 ("Esta al lado del supermercado.","aula11_esta_lado_super.mp3","Está al lado del supermercado.",GABY),
 ("Esta a dos cuadras de aqui.","aula11_esta_dos_cuadras.mp3","Está a dos cuadras de aquí.",JUAN),
 ("El quiosco esta al lado del banco.","aula11_quiosco_lado_banco.mp3","El quiosco está al lado del banco.",GABY),
 ("El ayuntamiento esta entre el banco y la plaza.","aula11_ayto_entre.mp3","El ayuntamiento está entre el banco y la plaza.",JUAN),
 # order audio (5 sentences in correct order)
 ("[order-l11]","aula11_order_l11_ordering.mp3",
   "¿Hay un banco cerca de la oficina? Sí, hay uno en la esquina, al lado del supermercado. ¡Perfecto! ¿Y dónde está la farmacia? Está enfrente de la plaza, a dos cuadras. Gracias. El ayuntamiento está entre el banco y la plaza, ¿verdad?",
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
