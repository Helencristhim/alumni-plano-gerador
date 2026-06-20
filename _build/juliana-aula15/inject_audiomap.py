#!/usr/bin/env python3
import io

LISTEN = ("Buenos dias y bienvenida a nuestra tienda. Hoy tenemos muchas ofertas. "
          "Todas las camisas tienen un descuento del veinte por ciento. Los pantalones cuestan "
          "treinta euros, pero esta semana cuestan solo veinte. Si compra dos prendas, la segunda "
          "tiene un descuento del cincuenta por ciento. El probador esta al fondo, a la derecha. "
          "Puede pagar en efectivo o con tarjeta en la caja. Si no le queda bien la talla, "
          "puede cambiar la prenda en una semana.")

PAIRS = [
 ("La talla","aula15_la_talla.mp3"),
 ("El probador","aula15_el_probador.mp3"),
 ("La caja","aula15_la_caja.mp3"),
 ("El efectivo","aula15_el_efectivo.mp3"),
 ("La tarjeta","aula15_la_tarjeta.mp3"),
 ("La prenda","aula15_la_prenda.mp3"),
 ("El descuento","aula15_el_descuento.mp3"),
 ("La tienda","aula15_la_tienda.mp3"),
 ("El dependiente","aula15_el_dependiente.mp3"),
 ("El escaparate","aula15_el_escaparate.mp3"),
 (LISTEN,"aula15_listening_dependiente.mp3"),
 ("Hola. Vi esta camisa en el escaparate. La tiene en talla M?","aula15_dialogo_juliana_1.mp3"),
 ("Me queda bien. Cuanto cuesta?","aula15_dialogo_juliana_2.mp3"),
 ("Perfecto! Me la llevo. Puedo pagar con tarjeta?","aula15_dialogo_juliana_3.mp3"),
 ("Si, aqui tiene. El probador esta al fondo a la derecha.","aula15_dialogo_dependiente_1.mp3"),
 ("Cuesta treinta euros, pero hoy tiene un descuento del veinte por ciento.","aula15_dialogo_dependiente_2.mp3"),
 ("Por supuesto. Pase por la caja, por favor.","aula15_dialogo_dependiente_3.mp3"),
 ("Cuanto cuesta esta camisa?","aula15_cuanto_cuesta_camisa.mp3"),
 ("Queria probarme esta falda.","aula15_queria_probarme_falda.mp3"),
 ("Tiene esta prenda en talla M?","aula15_tiene_prenda_talla.mp3"),
 ("Puedo pagar con tarjeta?","aula15_puedo_pagar_tarjeta.mp3"),
 ("Donde esta el probador?","aula15_donde_probador.mp3"),
 ("Cuanto cuestan estos zapatos?","aula15_cuanto_cuestan_zapatos.mp3"),
 ("Tiene esta camisa en talla M?","aula15_tiene_camisa_talla_m.mp3"),
 ("Puedo probarme esta falda?","aula15_puedo_probarme_falda.mp3"),
 ("Cuanto cuesta?","aula15_cuanto_cuesta.mp3"),
 ("Tiene un descuento?","aula15_tiene_descuento.mp3"),
 ("Tiene esta camisa en otra talla?","aula15_camisa_otra_talla.mp3"),
 ("[order-l15]","aula15_order_l15_ordering.mp3"),
]

def esc(s): return s.replace("\\","\\\\").replace('"','\\"')
block_comma = "\n".join('  "%s": "/audio/juliana-marques/%s",' % (esc(k), f) for k,f in PAIRS)
block_last = "\n".join('  "%s": "/audio/juliana-marques/%s"%s' % (esc(k), f, ("," if i < len(PAIRS)-1 else "")) for i,(k,f) in enumerate(PAIRS))

# anchor: aula14 last entry (order-l14)
base = "  \"[order-l14]\": \"/audio/juliana-marques/aula14_order_l14_ordering.mp3\""
for path in ["public/professor/juliana-marques.html","public/aluno/juliana-marques.html"]:
    p = "/home/dan/dev/work/better/wt-jul-a15/"+path
    h = io.open(p, encoding="utf-8").read()
    assert "aula15_" not in h, path+": aula15 already in audioMap"
    if h.count(base + ",") == 1:
        h = h.replace(base + ",", base + ",\n" + block_comma, 1)
    else:
        assert h.count(base) == 1, path+": aula14 last-entry anchor not unique"
        h = h.replace(base, base + ",\n" + block_last, 1)
    io.open(p,"w",encoding="utf-8").write(h)
    print(path, "injected", len(PAIRS), "entries")
