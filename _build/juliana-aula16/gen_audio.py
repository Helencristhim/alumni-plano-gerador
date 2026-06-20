#!/usr/bin/env python3
import os, io, sys, json, time, urllib.request, urllib.error

ROOT = "/home/dan/dev/work/better/wt-jul-a16"
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
JUAN = "rBqbBncz61jpuaOTI1GW"   # M Peruvian = Farmaceutico / male

LISTEN = ("Buenas tardes. Para la gripe le doy estas pastillas y este jarabe. Tome una pastilla "
          "cada doce horas, despues de comer. El jarabe es para la tos: una cucharada por la noche. "
          "Si tiene fiebre alta, mas de treinta y nueve grados, vaya al medico. Para el dolor de "
          "cabeza puede tomar paracetamol. Beba mucha agua y descanse. Estas pastillas no necesitan "
          "receta, pero el antibiotico si necesita receta del medico. Que se mejore pronto.")
LISTEN_TTS = ("Buenas tardes. Para la gripe le doy estas pastillas y este jarabe. Tome una pastilla "
          "cada doce horas, después de comer. El jarabe es para la tos: una cucharada por la noche. "
          "Si tiene fiebre alta, más de treinta y nueve grados, vaya al médico. Para el dolor de "
          "cabeza puede tomar paracetamol. Beba mucha agua y descanse. Estas pastillas no necesitan "
          "receta, pero el antibiótico sí necesita receta del médico. Que se mejore pronto.")

ITEMS = [
 # vocab cards (Gaby)
 ("La receta","aula16_la_receta.mp3","La receta",GABY),
 ("La pastilla","aula16_la_pastilla.mp3","La pastilla",GABY),
 ("El jarabe","aula16_el_jarabe.mp3","El jarabe",GABY),
 ("La fiebre","aula16_la_fiebre.mp3","La fiebre",GABY),
 ("La tos","aula16_la_tos.mp3","La tos",GABY),
 ("La gripe","aula16_la_gripe.mp3","La gripe",GABY),
 ("El mareo","aula16_el_mareo.mp3","El mareo",GABY),
 ("El termometro","aula16_el_termometro.mp3","El termómetro",GABY),
 ("La venda","aula16_la_venda.mp3","La venda",GABY),
 ("El farmaceutico","aula16_el_farmaceutico.mp3","El farmacéutico",GABY),
 # listening monologue (Farmaceutico = Juan)
 (LISTEN,"aula16_listening_farmaceutico.mp3",LISTEN_TTS,JUAN),
 # dialogue Juliana (Gaby)
 ("Buenos dias. Me duele la garganta y tengo tos.","aula16_dialogo_juliana_1.mp3","Buenos días. Me duele la garganta y tengo tos.",GABY),
 ("Si, treinta y ocho grados. Tiene algo para la tos?","aula16_dialogo_juliana_2.mp3","Sí, treinta y ocho grados. ¿Tiene algo para la tos?",GABY),
 ("Necesito receta?","aula16_dialogo_juliana_3.mp3","¿Necesito receta?",GABY),
 # dialogue Farmaceutico (Juan)
 ("Tiene fiebre tambien? Uso un termometro?","aula16_dialogo_farmaceutico_1.mp3","¿Tiene fiebre también? ¿Usó un termómetro?",JUAN),
 ("Le recomiendo este jarabe. Una cucharada cada ocho horas.","aula16_dialogo_farmaceutico_2.mp3","Le recomiendo este jarabe. Una cucharada cada ocho horas.",JUAN),
 ("No, este no necesita receta. Que se mejore.","aula16_dialogo_farmaceutico_3.mp3","No, este no necesita receta. Que se mejore.",JUAN),
 # loose phrases (listening 2 / fill / survival)
 ("Me duele la cabeza.","aula16_me_duele_cabeza.mp3","Me duele la cabeza.",GABY),
 ("Me duelen los oidos.","aula16_me_duelen_oidos.mp3","Me duelen los oídos.",GABY),
 ("Tengo dolor de garganta.","aula16_tengo_dolor_garganta.mp3","Tengo dolor de garganta.",GABY),
 ("Tiene algo para la fiebre?","aula16_algo_para_fiebre.mp3","¿Tiene algo para la fiebre?",JUAN),
 ("Tiene algo para la tos?","aula16_algo_para_tos.mp3","¿Tiene algo para la tos?",GABY),
 ("Necesito algo para la fiebre.","aula16_necesito_algo_fiebre.mp3","Necesito algo para la fiebre.",GABY),
 ("Me duele la garganta y tengo tos.","aula16_duele_garganta_tos.mp3","Me duele la garganta y tengo tos.",GABY),
 ("Necesito una receta?","aula16_necesito_una_receta.mp3","¿Necesito una receta?",JUAN),
 ("Tengo tos y un poco de fiebre.","aula16_tos_poco_fiebre.mp3","Tengo tos y un poco de fiebre.",GABY),
 ("Tengo fiebre y un poco de mareo.","aula16_fiebre_poco_mareo.mp3","Tengo fiebre y un poco de mareo.",GABY),
 # order audio (correct sequence)
 ("[order-l16]","aula16_order_l16_ordering.mp3",
   "Buenos días. Me duele la garganta y tengo tos. ¿Tiene fiebre también? Sí, un poco. ¿Tiene algo para la tos? Le recomiendo este jarabe, una cucharada cada ocho horas. Gracias. ¿Necesito receta?",
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
