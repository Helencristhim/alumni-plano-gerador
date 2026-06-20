#!/usr/bin/env python3
import io

PAIRS = [
 ("Seguir recto","aula12_seguir_recto.mp3"),
 ("Girar","aula12_girar.mp3"),
 ("Doblar","aula12_doblar.mp3"),
 ("Cruzar","aula12_cruzar.mp3"),
 ("El semaforo","aula12_el_semaforo.mp3"),
 ("El cruce","aula12_el_cruce.mp3"),
 ("La avenida","aula12_la_avenida.mp3"),
 ("A la derecha","aula12_a_la_derecha.mp3"),
 ("A la izquierda","aula12_a_la_izquierda.mp3"),
 ("Al final de","aula12_al_final_de.mp3"),
 ("Hola, soy Diego. Para llegar a mi oficina es facil. Sal de la estacion y sigue recto por la avenida principal. Cruza la calle en el primer semaforo. Despues gira a la derecha en el cruce. Sigue una cuadra mas y dobla a la izquierda. Mi oficina esta al final de la calle, al lado de la farmacia. Son diez minutos a pie.","aula12_listening_diego.mp3"),
 ("Disculpe, como llego a la plaza?","aula12_dialogo_juliana_1.mp3"),
 ("Y despues cruzo la calle?","aula12_dialogo_juliana_2.mp3"),
 ("Esta lejos?","aula12_dialogo_juliana_3.mp3"),
 ("Sigue recto dos cuadras y gira a la derecha.","aula12_dialogo_diego_1.mp3"),
 ("Si, cruza en el semaforo. La plaza esta al final.","aula12_dialogo_diego_2.mp3"),
 ("No, son cinco minutos. Buen camino!","aula12_dialogo_diego_3.mp3"),
 ("Sigue recto dos cuadras.","aula12_sigue_recto_dos.mp3"),
 ("Gira a la derecha en el semaforo.","aula12_gira_derecha_semaforo.mp3"),
 ("Cruza la calle en el cruce.","aula12_cruza_cruce.mp3"),
 ("Dobla a la izquierda en la avenida.","aula12_dobla_izq_avenida.mp3"),
 ("Esta al final de la calle.","aula12_al_final_calle.mp3"),
 ("[order-l12]","aula12_order_l12_ordering.mp3"),
]

def esc(s): return s.replace("\\","\\\\").replace('"','\\"')
# block where every entry ends with a comma (used when anchor already has more entries after it)
block_comma = "\n".join('  "%s": "/audio/juliana-marques/%s",' % (esc(k), f) for k,f in PAIRS)
# block where the LAST entry has no trailing comma (used when anchor is the final audioMap entry)
block_last = "\n".join('  "%s": "/audio/juliana-marques/%s"%s' % (esc(k), f, ("," if i < len(PAIRS)-1 else "")) for i,(k,f) in enumerate(PAIRS))

base = "  \"[order-l11]\": \"/audio/juliana-marques/aula11_order_l11_ordering.mp3\""
for path in ["public/professor/juliana-marques.html","public/aluno/juliana-marques.html"]:
    p = "/home/dan/dev/work/better/wt-juliana-a12/"+path
    h = io.open(p, encoding="utf-8").read()
    assert "aula12_" not in h, path+": aula12 already in audioMap"
    if h.count(base + ",") == 1:        # not the last entry: comma follows
        h = h.replace(base + ",", base + ",\n" + block_comma, 1)
    else:                                # last audioMap entry: no trailing comma
        assert h.count(base) == 1, path+": order-l11 anchor not unique"
        h = h.replace(base, base + ",\n" + block_last, 1)
    io.open(p,"w",encoding="utf-8").write(h)
    print(path, "injected", len(PAIRS), "entries")
