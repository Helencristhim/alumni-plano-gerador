#!/usr/bin/env python3
import io

LISTEN = ("Hola, soy Diego. El fin de semana pasado lo pase muy bien. El sabado fui a la playa con unos "
          "amigos. Comimos pescado y nadamos un poco. Por la tarde, vi un partido de futbol en un bar. El "
          "domingo visite un museo en el centro y despues camine por el parque. Por la noche cene en casa "
          "con mi familia y descanse. Manana te cuento mas. Un abrazo.")

PAIRS = [
 ("Ayer","aula18_ayer.mp3"),
 ("Anoche","aula18_anoche.mp3"),
 ("El fin de semana pasado","aula18_fin_semana_pasado.mp3"),
 ("La playa","aula18_la_playa.mp3"),
 ("El museo","aula18_el_museo.mp3"),
 ("Fui","aula18_fui.mp3"),
 ("Comi","aula18_comi.mp3"),
 ("Visite","aula18_visite.mp3"),
 ("Vi","aula18_vi.mp3"),
 ("Hice","aula18_hice.mp3"),
 (LISTEN,"aula18_listening_diego.mp3"),
 ("Juliana, que hiciste el fin de semana?","aula18_dialogo_diego_1.mp3"),
 ("Que bien! Y el domingo?","aula18_dialogo_diego_2.mp3"),
 ("Hiciste algo mas?","aula18_dialogo_diego_3.mp3"),
 ("El sabado fui a la playa y comi pescado.","aula18_dialogo_juliana_1.mp3"),
 ("El domingo visite un museo y vi una exposicion.","aula18_dialogo_juliana_2.mp3"),
 ("Por la noche descanse en casa. Fue un buen fin de semana!","aula18_dialogo_juliana_3.mp3"),
 ("Ayer fui al cine.","aula18_ayer_fui_cine.mp3"),
 ("Comi en un restaurante.","aula18_comi_restaurante.mp3"),
 ("El sabado visite un museo.","aula18_sabado_visite_museo.mp3"),
 ("Vi una pelicula muy buena.","aula18_vi_pelicula_buena.mp3"),
 ("El domingo hice deporte.","aula18_domingo_hice_deporte.mp3"),
 ("[order-l18]","aula18_order_l18_ordering.mp3"),
]

def esc(s): return s.replace("\\","\\\\").replace('"','\\"')
block_comma = "\n".join('  "%s": "/audio/juliana-marques/%s",' % (esc(k), f) for k,f in PAIRS)
block_last = "\n".join('  "%s": "/audio/juliana-marques/%s"%s' % (esc(k), f, ("," if i < len(PAIRS)-1 else "")) for i,(k,f) in enumerate(PAIRS))

# anchor: aula17 last entry (order-l17)
base = "  \"[order-l17]\": \"/audio/juliana-marques/aula17_order_l17_ordering.mp3\""
for path in ["public/professor/juliana-marques.html","public/aluno/juliana-marques.html"]:
    p = "/home/dan/dev/work/better/wt-jul-a18/"+path
    h = io.open(p, encoding="utf-8").read()
    assert "aula18_" not in h, path+": aula18 already in audioMap"
    if h.count(base + ",") == 1:
        h = h.replace(base + ",", base + ",\n" + block_comma, 1)
    else:
        assert h.count(base) == 1, path+": aula17 last-entry anchor not unique"
        h = h.replace(base, base + ",\n" + block_last, 1)
    io.open(p,"w",encoding="utf-8").write(h)
    print(path, "injected", len(PAIRS), "entries")
