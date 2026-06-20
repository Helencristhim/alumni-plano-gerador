#!/usr/bin/env python3
import io

LISTEN = ("Hola, soy Diego. Para llegar al congreso es facil en transporte publico. "
          "Toma el metro en la estacion de tu hotel, en la linea roja. Tienes que hacer transbordo "
          "en la estacion central a la linea azul. Sube al tren del anden numero tres. "
          "Te bajas en la cuarta parada. El billete cuesta dos euros. Despues sales de la estacion "
          "y el centro de congresos esta enfrente. Son veinte minutos en total.")

PAIRS = [
 ("El billete","aula13_el_billete.mp3"),
 ("La estacion","aula13_la_estacion.mp3"),
 ("Hacer transbordo","aula13_hacer_transbordo.mp3"),
 ("La linea","aula13_la_linea.mp3"),
 ("Bajarse","aula13_bajarse.mp3"),
 ("Subirse","aula13_subirse.mp3"),
 ("El anden","aula13_el_anden.mp3"),
 ("El conductor","aula13_el_conductor.mp3"),
 ("La tarifa","aula13_la_tarifa.mp3"),
 ("Ida y vuelta","aula13_ida_y_vuelta.mp3"),
 (LISTEN,"aula13_listening_diego.mp3"),
 ("Disculpe, que linea va al centro?","aula13_dialogo_juliana_1.mp3"),
 ("Tengo que hacer transbordo?","aula13_dialogo_juliana_2.mp3"),
 ("Cuanto cuesta el billete?","aula13_dialogo_juliana_3.mp3"),
 ("La linea roja. Tienes que subir en este anden.","aula13_dialogo_diego_1.mp3"),
 ("Si, en la estacion central. Te bajas y cambias de linea.","aula13_dialogo_diego_2.mp3"),
 ("La tarifa es de dos euros. Buen viaje!","aula13_dialogo_diego_3.mp3"),
 ("Toma la linea roja en la estacion.","aula13_toma_linea_roja.mp3"),
 ("Tienes que hacer transbordo en la estacion central.","aula13_transbordo_central.mp3"),
 ("Sube al tren del anden tres.","aula13_sube_anden_tres.mp3"),
 ("Bajate en la cuarta parada.","aula13_bajate_cuarta.mp3"),
 ("El billete cuesta dos euros.","aula13_billete_dos_euros.mp3"),
 ("Tengo que hacer transbordo.","aula13_tengo_que_transbordo.mp3"),
 ("Me bajo en la proxima parada.","aula13_me_bajo_proxima.mp3"),
 ("Voy al trabajo en metro.","aula13_voy_trabajo_metro.mp3"),
 ("Que linea va al centro?","aula13_que_linea_centro.mp3"),
 ("[order-l13]","aula13_order_l13_ordering.mp3"),
]

def esc(s): return s.replace("\\","\\\\").replace('"','\\"')
block_comma = "\n".join('  "%s": "/audio/juliana-marques/%s",' % (esc(k), f) for k,f in PAIRS)
block_last = "\n".join('  "%s": "/audio/juliana-marques/%s"%s' % (esc(k), f, ("," if i < len(PAIRS)-1 else "")) for i,(k,f) in enumerate(PAIRS))

base = "  \"[order-l12]\": \"/audio/juliana-marques/aula12_order_l12_ordering.mp3\""
for path in ["public/professor/juliana-marques.html","public/aluno/juliana-marques.html"]:
    p = "/home/dan/dev/work/better/wt-juliana-g-a13/"+path
    h = io.open(p, encoding="utf-8").read()
    assert "aula13_" not in h, path+": aula13 already in audioMap"
    if h.count(base + ",") == 1:        # not the last entry: comma follows
        h = h.replace(base + ",", base + ",\n" + block_comma, 1)
    else:                                # last audioMap entry: no trailing comma
        assert h.count(base) == 1, path+": order-l12 anchor not unique"
        h = h.replace(base, base + ",\n" + block_last, 1)
    io.open(p,"w",encoding="utf-8").write(h)
    print(path, "injected", len(PAIRS), "entries")
