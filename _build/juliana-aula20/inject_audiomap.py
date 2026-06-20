#!/usr/bin/env python3
import io

LISTEN = ("Hola, soy Diego. Ayer fue un dia muy completo. Por la manana fui de compras y "
          "compre una camisa en una tienda del centro. Despues comi en un restaurante: pedi la "
          "carta y pague la cuenta con tarjeta. Por la tarde tome el metro para volver a casa. "
          "Manana voy a descansar, pero el proximo mes pienso empezar un curso de espanol. Mi "
          "meta es hablar con fluidez. Y tu, que hiciste ayer y que vas a hacer manana?")

PAIRS = [
 ("Ayer fui de compras.","aula20_ayer_fui_compras.mp3"),
 ("Comi en un restaurante.","aula20_comi_restaurante.mp3"),
 ("Pague la cuenta con tarjeta.","aula20_pague_cuenta_tarjeta.mp3"),
 ("Tome el metro al centro.","aula20_tome_metro_centro.mp3"),
 ("Manana voy a descansar.","aula20_manana_descansar.mp3"),
 ("El proximo mes voy a viajar.","aula20_proximo_mes_viajar.mp3"),
 ("Pienso estudiar mas espanol.","aula20_pienso_estudiar.mp3"),
 ("Mi meta es hablar con fluidez.","aula20_meta_fluidez.mp3"),
 (LISTEN,"aula20_listening_diego.mp3"),
 ("Juliana, que hiciste el fin de semana pasado?","aula20_dialogo_diego_1.mp3"),
 ("Que rico! Y que vas a hacer el proximo ano?","aula20_dialogo_diego_2.mp3"),
 ("Tu espanol ha mejorado mucho. Felicidades!","aula20_dialogo_diego_3.mp3"),
 ("Fui de compras y comi en un restaurante nuevo.","aula20_dialogo_juliana_1.mp3"),
 ("Voy a viajar a Peru. Pienso practicar mi espanol alli.","aula20_dialogo_juliana_2.mp3"),
 ("Gracias! Aprendi mucho en este curso.","aula20_dialogo_juliana_3.mp3"),
 ("Donde esta la farmacia, por favor?","aula20_donde_farmacia.mp3"),
 ("Me gustaria reservar una mesa.","aula20_reservar_mesa.mp3"),
 ("Cuanto cuesta esta camisa?","aula20_cuanto_cuesta_camisa.mp3"),
 ("Te apetece quedar el sabado?","aula20_te_apetece_quedar.mp3"),
 ("Ayer visite a mi familia.","aula20_ayer_visite_familia.mp3"),
 ("Manana voy a empezar un curso.","aula20_manana_empezar_curso.mp3"),
 ("[order-l20]","aula20_order_l20_ordering.mp3"),
]

def esc(s): return s.replace("\\","\\\\").replace('"','\\"')
block_comma = "\n".join('  "%s": "/audio/juliana-marques/%s",' % (esc(k), f) for k,f in PAIRS)
block_last = "\n".join('  "%s": "/audio/juliana-marques/%s"%s' % (esc(k), f, ("," if i < len(PAIRS)-1 else "")) for i,(k,f) in enumerate(PAIRS))

base = "  \"[order-l19]\": \"/audio/juliana-marques/aula19_order_l19_ordering.mp3\""
for path in ["public/professor/juliana-marques.html","public/aluno/juliana-marques.html"]:
    p = "/home/dan/dev/work/better/wt-jul-a20/"+path
    h = io.open(p, encoding="utf-8").read()
    assert "aula20_" not in h, path+": aula20 already in audioMap"
    if h.count(base + ",") == 1:
        h = h.replace(base + ",", base + ",\n" + block_comma, 1)
    else:
        assert h.count(base) == 1, path+": aula19 last-entry anchor not unique"
        h = h.replace(base, base + ",\n" + block_last, 1)
    io.open(p,"w",encoding="utf-8").write(h)
    print(path, "injected", len(PAIRS), "entries")
