#!/usr/bin/env python3
import io

LISTEN = ("Hola, soy Diego. Tengo muchos planes para el futuro. El proximo mes voy a empezar un curso "
          "de ingles. El proximo ano pienso mudarme a una ciudad mas grande para trabajar. Tambien voy "
          "a ahorrar dinero para viajar a Europa. Mi meta principal es conseguir un ascenso en mi empresa. "
          "Espero lograr todo esto pronto. Y tu, que planes tienes?")

PAIRS = [
 ("Manana","aula19_manana.mp3"),
 ("El proximo","aula19_el_proximo.mp3"),
 ("El futuro","aula19_el_futuro.mp3"),
 ("La meta","aula19_la_meta.mp3"),
 ("El objetivo","aula19_el_objetivo.mp3"),
 ("Pienso","aula19_pienso.mp3"),
 ("Espero","aula19_espero.mp3"),
 ("Quiero","aula19_quiero.mp3"),
 ("Ahorrar","aula19_ahorrar.mp3"),
 ("Mudarse","aula19_mudarse.mp3"),
 (LISTEN,"aula19_listening_diego.mp3"),
 ("Juliana, que vas a hacer el proximo ano?","aula19_dialogo_diego_1.mp3"),
 ("Que bien! Y algun viaje?","aula19_dialogo_diego_2.mp3"),
 ("Cual es tu meta principal?","aula19_dialogo_diego_3.mp3"),
 ("Voy a estudiar mas espanol y quiero un ascenso.","aula19_dialogo_juliana_1.mp3"),
 ("Si, pienso viajar a Peru. Voy a ahorrar dinero.","aula19_dialogo_juliana_2.mp3"),
 ("Mi objetivo es hablar espanol con fluidez. Lo voy a lograr!","aula19_dialogo_juliana_3.mp3"),
 ("Manana voy a estudiar.","aula19_manana_voy_estudiar.mp3"),
 ("El proximo ano voy a viajar.","aula19_proximo_ano_viajar.mp3"),
 ("Pienso aprender a programar.","aula19_pienso_aprender_programar.mp3"),
 ("Quiero conseguir un ascenso.","aula19_quiero_ascenso.mp3"),
 ("Mi meta es hablar espanol bien.","aula19_meta_hablar_bien.mp3"),
 ("[order-l19]","aula19_order_l19_ordering.mp3"),
]

def esc(s): return s.replace("\\","\\\\").replace('"','\\"')
block_comma = "\n".join('  "%s": "/audio/juliana-marques/%s",' % (esc(k), f) for k,f in PAIRS)
block_last = "\n".join('  "%s": "/audio/juliana-marques/%s"%s' % (esc(k), f, ("," if i < len(PAIRS)-1 else "")) for i,(k,f) in enumerate(PAIRS))

base = "  \"[order-l18]\": \"/audio/juliana-marques/aula18_order_l18_ordering.mp3\""
for path in ["public/professor/juliana-marques.html","public/aluno/juliana-marques.html"]:
    p = "/home/dan/dev/work/better/wt-jul-a19/"+path
    h = io.open(p, encoding="utf-8").read()
    assert "aula19_" not in h, path+": aula19 already in audioMap"
    if h.count(base + ",") == 1:
        h = h.replace(base + ",", base + ",\n" + block_comma, 1)
    else:
        assert h.count(base) == 1, path+": aula18 last-entry anchor not unique"
        h = h.replace(base, base + ",\n" + block_last, 1)
    io.open(p,"w",encoding="utf-8").write(h)
    print(path, "injected", len(PAIRS), "entries")
