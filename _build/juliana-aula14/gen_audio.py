#!/usr/bin/env python3
import os, io, sys, json, time, urllib.request, urllib.error

ROOT = "/home/dan/dev/work/better/wt-juliana-g-a14"
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
JUAN = "rBqbBncz61jpuaOTI1GW"   # M Peruvian = Camarero / male

LISTEN = ("Buenas noches y bienvenida. Hoy tenemos un menu del dia muy rico. "
          "De primero, una sopa de verduras o una ensalada. De segundo, puede pedir pollo asado "
          "o pescado al horno. La bebida esta incluida: agua, refresco o una copa de vino. "
          "De postre, tenemos flan o fruta fresca. El menu completo cuesta quince euros. "
          "Le recomiendo el pescado, esta muy fresco hoy. Cuando termine, le traigo la cuenta.")
LISTEN_TTS = ("Buenas noches y bienvenida. Hoy tenemos un menú del día muy rico. "
          "De primero, una sopa de verduras o una ensalada. De segundo, puede pedir pollo asado "
          "o pescado al horno. La bebida está incluida: agua, refresco o una copa de vino. "
          "De postre, tenemos flan o fruta fresca. El menú completo cuesta quince euros. "
          "Le recomiendo el pescado, está muy fresco hoy. Cuando termine, le traigo la cuenta.")

ITEMS = [
 # vocab cards (Gaby)
 ("La carta","aula14_la_carta.mp3","La carta",GABY),
 ("El plato","aula14_el_plato.mp3","El plato",GABY),
 ("El postre","aula14_el_postre.mp3","El postre",GABY),
 ("La bebida","aula14_la_bebida.mp3","La bebida",GABY),
 ("La cuenta","aula14_la_cuenta.mp3","La cuenta",GABY),
 ("El camarero","aula14_el_camarero.mp3","El camarero",GABY),
 ("Pedir","aula14_pedir.mp3","Pedir",GABY),
 ("Recomendar","aula14_recomendar.mp3","Recomendar",GABY),
 ("La mesa","aula14_la_mesa.mp3","La mesa",GABY),
 ("La reserva","aula14_la_reserva.mp3","La reserva",GABY),
 # listening monologue (Camarero = Juan)
 (LISTEN,"aula14_listening_camarero.mp3",LISTEN_TTS,JUAN),
 # dialogue Juliana (Gaby)
 ("Buenas noches. Tengo una reserva a las ocho.","aula14_dialogo_juliana_1.mp3","Buenas noches. Tengo una reserva a las ocho.",GABY),
 ("Queria el plato del dia. Que me recomienda?","aula14_dialogo_juliana_2.mp3","Quería el plato del día. ¿Qué me recomienda?",GABY),
 ("Para mi, agua, por favor. Y de postre, un flan.","aula14_dialogo_juliana_3.mp3","Para mí, agua, por favor. Y de postre, un flan.",GABY),
 # dialogue Camarero (Juan)
 ("Perfecto. Aqui tiene la carta. Que va a pedir?","aula14_dialogo_camarero_1.mp3","Perfecto. Aquí tiene la carta. ¿Qué va a pedir?",JUAN),
 ("Le recomiendo el pescado. Y de beber?","aula14_dialogo_camarero_2.mp3","Le recomiendo el pescado. ¿Y de beber?",JUAN),
 ("Muy bien. Enseguida le traigo todo.","aula14_dialogo_camarero_3.mp3","Muy bien. Enseguida le traigo todo.",JUAN),
 # loose phrases (listening 2)
 ("Una mesa para dos, por favor.","aula14_mesa_para_dos.mp3","Una mesa para dos, por favor.",GABY),
 ("Queria el plato del dia.","aula14_queria_plato_dia.mp3","Quería el plato del día.",GABY),
 ("Que me recomienda?","aula14_que_me_recomienda.mp3","¿Qué me recomienda?",GABY),
 ("Para mi, agua, por favor.","aula14_para_mi_agua.mp3","Para mí, agua, por favor.",GABY),
 ("La cuenta, por favor.","aula14_la_cuenta_por_favor.mp3","La cuenta, por favor.",GABY),
 # survival / fill extras
 ("Me trae la carta?","aula14_me_trae_carta.mp3","¿Me trae la carta?",GABY),
 ("Me gustaria un postre.","aula14_me_gustaria_postre.mp3","Me gustaría un postre.",GABY),
 ("Me trae la cuenta, por favor?","aula14_me_trae_cuenta.mp3","¿Me trae la cuenta, por favor?",GABY),
 ("Que me recomienda de la carta?","aula14_recomienda_carta.mp3","¿Qué me recomienda de la carta?",GABY),
 # order audio (correct sequence)
 ("[order-l14]","aula14_order_l14_ordering.mp3",
   "Buenas noches. Tengo una reserva a las ocho. Perfecto. Aquí tiene la carta. ¿Qué va a pedir? Quería el plato del día. ¿Qué me recomienda? Le recomiendo el pescado. ¿Y de beber? Para mí, agua. Y de postre, un flan.",
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
