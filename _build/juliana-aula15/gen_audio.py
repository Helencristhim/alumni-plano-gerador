#!/usr/bin/env python3
import os, io, sys, json, time, urllib.request, urllib.error

ROOT = "/home/dan/dev/work/better/wt-jul-a15"
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
JUAN = "rBqbBncz61jpuaOTI1GW"   # M Peruvian = Dependiente / male

LISTEN = ("Buenos dias y bienvenida a nuestra tienda. Hoy tenemos muchas ofertas. "
          "Todas las camisas tienen un descuento del veinte por ciento. Los pantalones cuestan "
          "treinta euros, pero esta semana cuestan solo veinte. Si compra dos prendas, la segunda "
          "tiene un descuento del cincuenta por ciento. El probador esta al fondo, a la derecha. "
          "Puede pagar en efectivo o con tarjeta en la caja. Si no le queda bien la talla, "
          "puede cambiar la prenda en una semana.")
LISTEN_TTS = ("Buenos días y bienvenida a nuestra tienda. Hoy tenemos muchas ofertas. "
          "Todas las camisas tienen un descuento del veinte por ciento. Los pantalones cuestan "
          "treinta euros, pero esta semana cuestan solo veinte. Si compra dos prendas, la segunda "
          "tiene un descuento del cincuenta por ciento. El probador está al fondo, a la derecha. "
          "Puede pagar en efectivo o con tarjeta en la caja. Si no le queda bien la talla, "
          "puede cambiar la prenda en una semana.")

ITEMS = [
 # vocab cards (Gaby)
 ("La talla","aula15_la_talla.mp3","La talla",GABY),
 ("El probador","aula15_el_probador.mp3","El probador",GABY),
 ("La caja","aula15_la_caja.mp3","La caja",GABY),
 ("El efectivo","aula15_el_efectivo.mp3","El efectivo",GABY),
 ("La tarjeta","aula15_la_tarjeta.mp3","La tarjeta",GABY),
 ("La prenda","aula15_la_prenda.mp3","La prenda",GABY),
 ("El descuento","aula15_el_descuento.mp3","El descuento",GABY),
 ("La tienda","aula15_la_tienda.mp3","La tienda",GABY),
 ("El dependiente","aula15_el_dependiente.mp3","El dependiente",GABY),
 ("El escaparate","aula15_el_escaparate.mp3","El escaparate",GABY),
 # listening monologue (Dependiente = Juan)
 (LISTEN,"aula15_listening_dependiente.mp3",LISTEN_TTS,JUAN),
 # dialogue Juliana (Gaby)
 ("Hola. Vi esta camisa en el escaparate. La tiene en talla M?","aula15_dialogo_juliana_1.mp3","Hola. Vi esta camisa en el escaparate. ¿La tiene en talla M?",GABY),
 ("Me queda bien. Cuanto cuesta?","aula15_dialogo_juliana_2.mp3","Me queda bien. ¿Cuánto cuesta?",GABY),
 ("Perfecto! Me la llevo. Puedo pagar con tarjeta?","aula15_dialogo_juliana_3.mp3","¡Perfecto! Me la llevo. ¿Puedo pagar con tarjeta?",GABY),
 # dialogue Dependiente (Juan)
 ("Si, aqui tiene. El probador esta al fondo a la derecha.","aula15_dialogo_dependiente_1.mp3","Sí, aquí tiene. El probador está al fondo a la derecha.",JUAN),
 ("Cuesta treinta euros, pero hoy tiene un descuento del veinte por ciento.","aula15_dialogo_dependiente_2.mp3","Cuesta treinta euros, pero hoy tiene un descuento del veinte por ciento.",JUAN),
 ("Por supuesto. Pase por la caja, por favor.","aula15_dialogo_dependiente_3.mp3","Por supuesto. Pase por la caja, por favor.",JUAN),
 # loose phrases (listening 2)
 ("Cuanto cuesta esta camisa?","aula15_cuanto_cuesta_camisa.mp3","¿Cuánto cuesta esta camisa?",GABY),
 ("Queria probarme esta falda.","aula15_queria_probarme_falda.mp3","Quería probarme esta falda.",GABY),
 ("Tiene esta prenda en talla M?","aula15_tiene_prenda_talla.mp3","¿Tiene esta prenda en talla M?",GABY),
 ("Puedo pagar con tarjeta?","aula15_puedo_pagar_tarjeta.mp3","¿Puedo pagar con tarjeta?",GABY),
 ("Donde esta el probador?","aula15_donde_probador.mp3","¿Dónde está el probador?",GABY),
 # survival / fill extras
 ("Cuanto cuestan estos zapatos?","aula15_cuanto_cuestan_zapatos.mp3","¿Cuánto cuestan estos zapatos?",GABY),
 ("Tiene esta camisa en talla M?","aula15_tiene_camisa_talla_m.mp3","¿Tiene esta camisa en talla M?",GABY),
 ("Puedo probarme esta falda?","aula15_puedo_probarme_falda.mp3","¿Puedo probarme esta falda?",GABY),
 ("Cuanto cuesta?","aula15_cuanto_cuesta.mp3","¿Cuánto cuesta?",GABY),
 ("Tiene un descuento?","aula15_tiene_descuento.mp3","¿Tiene un descuento?",GABY),
 ("Tiene esta camisa en otra talla?","aula15_camisa_otra_talla.mp3","¿Tiene esta camisa en otra talla?",GABY),
 # order audio (correct sequence)
 ("[order-l15]","aula15_order_l15_ordering.mp3",
   "Hola. ¿Tiene esta camisa en talla M? Sí, aquí tiene. El probador está al fondo. Me queda bien. ¿Cuánto cuesta? Cuesta treinta euros, con un descuento del veinte por ciento. ¡Perfecto! ¿Puedo pagar con tarjeta?",
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
