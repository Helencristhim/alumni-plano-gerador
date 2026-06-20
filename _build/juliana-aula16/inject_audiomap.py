#!/usr/bin/env python3
import io

LISTEN = ("Buenas tardes. Para la gripe le doy estas pastillas y este jarabe. Tome una pastilla "
          "cada doce horas, despues de comer. El jarabe es para la tos: una cucharada por la noche. "
          "Si tiene fiebre alta, mas de treinta y nueve grados, vaya al medico. Para el dolor de "
          "cabeza puede tomar paracetamol. Beba mucha agua y descanse. Estas pastillas no necesitan "
          "receta, pero el antibiotico si necesita receta del medico. Que se mejore pronto.")

PAIRS = [
 ("La receta","aula16_la_receta.mp3"),
 ("La pastilla","aula16_la_pastilla.mp3"),
 ("El jarabe","aula16_el_jarabe.mp3"),
 ("La fiebre","aula16_la_fiebre.mp3"),
 ("La tos","aula16_la_tos.mp3"),
 ("La gripe","aula16_la_gripe.mp3"),
 ("El mareo","aula16_el_mareo.mp3"),
 ("El termometro","aula16_el_termometro.mp3"),
 ("La venda","aula16_la_venda.mp3"),
 ("El farmaceutico","aula16_el_farmaceutico.mp3"),
 (LISTEN,"aula16_listening_farmaceutico.mp3"),
 ("Buenos dias. Me duele la garganta y tengo tos.","aula16_dialogo_juliana_1.mp3"),
 ("Si, treinta y ocho grados. Tiene algo para la tos?","aula16_dialogo_juliana_2.mp3"),
 ("Necesito receta?","aula16_dialogo_juliana_3.mp3"),
 ("Tiene fiebre tambien? Uso un termometro?","aula16_dialogo_farmaceutico_1.mp3"),
 ("Le recomiendo este jarabe. Una cucharada cada ocho horas.","aula16_dialogo_farmaceutico_2.mp3"),
 ("No, este no necesita receta. Que se mejore.","aula16_dialogo_farmaceutico_3.mp3"),
 ("Me duele la cabeza.","aula16_me_duele_cabeza.mp3"),
 ("Me duelen los oidos.","aula16_me_duelen_oidos.mp3"),
 ("Tengo dolor de garganta.","aula16_tengo_dolor_garganta.mp3"),
 ("Tiene algo para la fiebre?","aula16_algo_para_fiebre.mp3"),
 ("Tiene algo para la tos?","aula16_algo_para_tos.mp3"),
 ("Necesito algo para la fiebre.","aula16_necesito_algo_fiebre.mp3"),
 ("Me duele la garganta y tengo tos.","aula16_duele_garganta_tos.mp3"),
 ("Necesito una receta?","aula16_necesito_una_receta.mp3"),
 ("Tengo tos y un poco de fiebre.","aula16_tos_poco_fiebre.mp3"),
 ("Tengo fiebre y un poco de mareo.","aula16_fiebre_poco_mareo.mp3"),
 ("[order-l16]","aula16_order_l16_ordering.mp3"),
]

def esc(s): return s.replace("\\","\\\\").replace('"','\\"')
block_comma = "\n".join('  "%s": "/audio/juliana-marques/%s",' % (esc(k), f) for k,f in PAIRS)
block_last = "\n".join('  "%s": "/audio/juliana-marques/%s"%s' % (esc(k), f, ("," if i < len(PAIRS)-1 else "")) for i,(k,f) in enumerate(PAIRS))

# anchor: aula15 last entry (order-l15)
base = "  \"[order-l15]\": \"/audio/juliana-marques/aula15_order_l15_ordering.mp3\""
for path in ["public/professor/juliana-marques.html","public/aluno/juliana-marques.html"]:
    p = "/home/dan/dev/work/better/wt-jul-a16/"+path
    h = io.open(p, encoding="utf-8").read()
    assert "aula16_" not in h, path+": aula16 already in audioMap"
    if h.count(base + ",") == 1:
        h = h.replace(base + ",", base + ",\n" + block_comma, 1)
    else:
        assert h.count(base) == 1, path+": aula15 last-entry anchor not unique"
        h = h.replace(base, base + ",\n" + block_last, 1)
    io.open(p,"w",encoding="utf-8").write(h)
    print(path, "injected", len(PAIRS), "entries")
