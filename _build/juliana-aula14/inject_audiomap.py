#!/usr/bin/env python3
import io

LISTEN = ("Buenas noches y bienvenida. Hoy tenemos un menu del dia muy rico. "
          "De primero, una sopa de verduras o una ensalada. De segundo, puede pedir pollo asado "
          "o pescado al horno. La bebida esta incluida: agua, refresco o una copa de vino. "
          "De postre, tenemos flan o fruta fresca. El menu completo cuesta quince euros. "
          "Le recomiendo el pescado, esta muy fresco hoy. Cuando termine, le traigo la cuenta.")

PAIRS = [
 ("La carta","aula14_la_carta.mp3"),
 ("El plato","aula14_el_plato.mp3"),
 ("El postre","aula14_el_postre.mp3"),
 ("La bebida","aula14_la_bebida.mp3"),
 ("La cuenta","aula14_la_cuenta.mp3"),
 ("El camarero","aula14_el_camarero.mp3"),
 ("Pedir","aula14_pedir.mp3"),
 ("Recomendar","aula14_recomendar.mp3"),
 ("La mesa","aula14_la_mesa.mp3"),
 ("La reserva","aula14_la_reserva.mp3"),
 (LISTEN,"aula14_listening_camarero.mp3"),
 ("Buenas noches. Tengo una reserva a las ocho.","aula14_dialogo_juliana_1.mp3"),
 ("Queria el plato del dia. Que me recomienda?","aula14_dialogo_juliana_2.mp3"),
 ("Para mi, agua, por favor. Y de postre, un flan.","aula14_dialogo_juliana_3.mp3"),
 ("Perfecto. Aqui tiene la carta. Que va a pedir?","aula14_dialogo_camarero_1.mp3"),
 ("Le recomiendo el pescado. Y de beber?","aula14_dialogo_camarero_2.mp3"),
 ("Muy bien. Enseguida le traigo todo.","aula14_dialogo_camarero_3.mp3"),
 ("Una mesa para dos, por favor.","aula14_mesa_para_dos.mp3"),
 ("Queria el plato del dia.","aula14_queria_plato_dia.mp3"),
 ("Que me recomienda?","aula14_que_me_recomienda.mp3"),
 ("Para mi, agua, por favor.","aula14_para_mi_agua.mp3"),
 ("La cuenta, por favor.","aula14_la_cuenta_por_favor.mp3"),
 ("Me trae la carta?","aula14_me_trae_carta.mp3"),
 ("Me gustaria un postre.","aula14_me_gustaria_postre.mp3"),
 ("Me trae la cuenta, por favor?","aula14_me_trae_cuenta.mp3"),
 ("Que me recomienda de la carta?","aula14_recomienda_carta.mp3"),
 ("[order-l14]","aula14_order_l14_ordering.mp3"),
]

def esc(s): return s.replace("\\","\\\\").replace('"','\\"')
block_comma = "\n".join('  "%s": "/audio/juliana-marques/%s",' % (esc(k), f) for k,f in PAIRS)
block_last = "\n".join('  "%s": "/audio/juliana-marques/%s"%s' % (esc(k), f, ("," if i < len(PAIRS)-1 else "")) for i,(k,f) in enumerate(PAIRS))

base = "  \"Tienes que hacer transbordo.\": \"/audio/juliana-marques/aula13_tienes_que_transbordo.mp3\""
for path in ["public/professor/juliana-marques.html","public/aluno/juliana-marques.html"]:
    p = "/home/dan/dev/work/better/wt-juliana-g-a14/"+path
    h = io.open(p, encoding="utf-8").read()
    assert "aula14_" not in h, path+": aula14 already in audioMap"
    if h.count(base + ",") == 1:
        h = h.replace(base + ",", base + ",\n" + block_comma, 1)
    else:
        assert h.count(base) == 1, path+": aula13 last-entry anchor not unique"
        h = h.replace(base, base + ",\n" + block_last, 1)
    io.open(p,"w",encoding="utf-8").write(h)
    print(path, "injected", len(PAIRS), "entries")
