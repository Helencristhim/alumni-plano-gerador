#!/usr/bin/env python3
import io

LISTEN = ("Hola, soy Carmen. Te llamo para invitarte a mi fiesta de cumpleanos. Es el sabado por la "
          "noche, a las nueve, en mi casa. Habra cena y musica. Despues, los que quieran, vamos a tomar "
          "una copa cerca. Dime si estas disponible, por favor. Si te apetece venir, trae a un amigo. "
          "Quedamos a las nueve. Espero verte. Un abrazo.")

PAIRS = [
 ("Quedar","aula17_quedar.mp3"),
 ("El plan","aula17_el_plan.mp3"),
 ("La invitacion","aula17_la_invitacion.mp3"),
 ("El cine","aula17_el_cine.mp3"),
 ("La cena","aula17_la_cena.mp3"),
 ("La copa","aula17_la_copa.mp3"),
 ("La fiesta","aula17_la_fiesta.mp3"),
 ("La entrada","aula17_la_entrada.mp3"),
 ("El cumpleanos","aula17_el_cumpleanos.mp3"),
 ("Disponible","aula17_disponible.mp3"),
 (LISTEN,"aula17_listening_carmen.mp3"),
 ("Diego, te apetece ir al cine el viernes?","aula17_dialogo_juliana_1.mp3"),
 ("Quedamos a las ocho? Yo compro las entradas.","aula17_dialogo_juliana_2.mp3"),
 ("Claro! Quedamos en la puerta del cine?","aula17_dialogo_juliana_3.mp3"),
 ("Me encantaria! A que hora quedamos?","aula17_dialogo_diego_1.mp3"),
 ("Perfecto. Y despues tomamos una copa?","aula17_dialogo_diego_2.mp3"),
 ("Genial! Hasta el viernes.","aula17_dialogo_diego_3.mp3"),
 ("Te apetece ir al cine?","aula17_te_apetece_cine.mp3"),
 ("Quedamos el sabado a las ocho.","aula17_quedamos_sabado_ocho.mp3"),
 ("Me encantaria, gracias.","aula17_me_encantaria_gracias.mp3"),
 ("Lo siento, no puedo hoy.","aula17_lo_siento_no_puedo_hoy.mp3"),
 ("Estas disponible el viernes?","aula17_estas_disponible_viernes.mp3"),
 ("Lo siento, no puedo. Quizas otro dia.","aula17_lo_siento_quizas_otro_dia.mp3"),
 ("[order-l17]","aula17_order_l17_ordering.mp3"),
]

def esc(s): return s.replace("\\","\\\\").replace('"','\\"')
block_comma = "\n".join('  "%s": "/audio/juliana-marques/%s",' % (esc(k), f) for k,f in PAIRS)
block_last = "\n".join('  "%s": "/audio/juliana-marques/%s"%s' % (esc(k), f, ("," if i < len(PAIRS)-1 else "")) for i,(k,f) in enumerate(PAIRS))

# anchor: aula16 last entry (order-l16)
base = "  \"[order-l16]\": \"/audio/juliana-marques/aula16_order_l16_ordering.mp3\""
for path in ["public/professor/juliana-marques.html","public/aluno/juliana-marques.html"]:
    p = "/home/dan/dev/work/better/wt-jul-a17/"+path
    h = io.open(p, encoding="utf-8").read()
    assert "aula17_" not in h, path+": aula17 already in audioMap"
    if h.count(base + ",") == 1:
        h = h.replace(base + ",", base + ",\n" + block_comma, 1)
    else:
        assert h.count(base) == 1, path+": aula16 last-entry anchor not unique"
        h = h.replace(base, base + ",\n" + block_last, 1)
    io.open(p,"w",encoding="utf-8").write(h)
    print(path, "injected", len(PAIRS), "entries")
