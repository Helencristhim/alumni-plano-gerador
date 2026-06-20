#!/usr/bin/env python3
import os, io, sys, json, time, urllib.request, urllib.error

ROOT = "/home/dan/dev/work/better/wt-juliana-g-a13"
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

LISTEN = ("Hola, soy Diego. Para llegar al congreso es facil en transporte publico. "
          "Toma el metro en la estacion de tu hotel, en la linea roja. Tienes que hacer transbordo "
          "en la estacion central a la linea azul. Sube al tren del anden numero tres. "
          "Te bajas en la cuarta parada. El billete cuesta dos euros. Despues sales de la estacion "
          "y el centro de congresos esta enfrente. Son veinte minutos en total.")
LISTEN_TTS = ("Hola, soy Diego. Para llegar al congreso es fácil en transporte público. "
          "Toma el metro en la estación de tu hotel, en la línea roja. Tienes que hacer transbordo "
          "en la estación central a la línea azul. Sube al tren del andén número tres. "
          "Te bajas en la cuarta parada. El billete cuesta dos euros. Después sales de la estación "
          "y el centro de congresos está enfrente. Son veinte minutos en total.")

# (audioMap_key, mp3_filename, tts_text_accented, voice)
ITEMS = [
 # vocab cards (Gaby)
 ("El billete","aula13_el_billete.mp3","El billete",GABY),
 ("La estacion","aula13_la_estacion.mp3","La estación",GABY),
 ("Hacer transbordo","aula13_hacer_transbordo.mp3","Hacer transbordo",GABY),
 ("La linea","aula13_la_linea.mp3","La línea",GABY),
 ("Bajarse","aula13_bajarse.mp3","Bajarse",GABY),
 ("Subirse","aula13_subirse.mp3","Subirse",GABY),
 ("El anden","aula13_el_anden.mp3","El andén",GABY),
 ("El conductor","aula13_el_conductor.mp3","El conductor",GABY),
 ("La tarifa","aula13_la_tarifa.mp3","La tarifa",GABY),
 ("Ida y vuelta","aula13_ida_y_vuelta.mp3","Ida y vuelta",GABY),
 # listening monologue (Diego = Juan)
 (LISTEN,"aula13_listening_diego.mp3",LISTEN_TTS,JUAN),
 # dialogue Juliana (Gaby)
 ("Disculpe, que linea va al centro?","aula13_dialogo_juliana_1.mp3","Disculpe, ¿qué línea va al centro?",GABY),
 ("Tengo que hacer transbordo?","aula13_dialogo_juliana_2.mp3","¿Tengo que hacer transbordo?",GABY),
 ("Cuanto cuesta el billete?","aula13_dialogo_juliana_3.mp3","¿Cuánto cuesta el billete?",GABY),
 # dialogue Diego (Juan)
 ("La linea roja. Tienes que subir en este anden.","aula13_dialogo_diego_1.mp3","La línea roja. Tienes que subir en este andén.",JUAN),
 ("Si, en la estacion central. Te bajas y cambias de linea.","aula13_dialogo_diego_2.mp3","Sí, en la estación central. Te bajas y cambias de línea.",JUAN),
 ("La tarifa es de dos euros. Buen viaje!","aula13_dialogo_diego_3.mp3","La tarifa es de dos euros. ¡Buen viaje!",JUAN),
 # listening 2 / loose instruction sentences
 ("Toma la linea roja en la estacion.","aula13_toma_linea_roja.mp3","Toma la línea roja en la estación.",JUAN),
 ("Tienes que hacer transbordo en la estacion central.","aula13_transbordo_central.mp3","Tienes que hacer transbordo en la estación central.",GABY),
 ("Sube al tren del anden tres.","aula13_sube_anden_tres.mp3","Sube al tren del andén tres.",JUAN),
 ("Bajate en la cuarta parada.","aula13_bajate_cuarta.mp3","Bájate en la cuarta parada.",GABY),
 ("El billete cuesta dos euros.","aula13_billete_dos_euros.mp3","El billete cuesta dos euros.",JUAN),
 # survival / pronunciation extra keys
 ("Tengo que hacer transbordo.","aula13_tengo_que_transbordo.mp3","Tengo que hacer transbordo.",GABY),
 ("Me bajo en la proxima parada.","aula13_me_bajo_proxima.mp3","Me bajo en la próxima parada.",GABY),
 ("Voy al trabajo en metro.","aula13_voy_trabajo_metro.mp3","Voy al trabajo en metro.",GABY),
 ("Que linea va al centro?","aula13_que_linea_centro.mp3","¿Qué línea va al centro?",GABY),
 # order audio (correct sequence)
 ("[order-l13]","aula13_order_l13_ordering.mp3",
   "Disculpe, ¿qué línea va al centro? La línea roja. Tienes que subir en este andén. ¿Tengo que hacer transbordo? Sí, en la estación central. Te bajas y cambias de línea. Gracias. ¿Cuánto cuesta el billete?",
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
