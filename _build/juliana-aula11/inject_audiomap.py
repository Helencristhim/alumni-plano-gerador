#!/usr/bin/env python3
import io, importlib.util, sys

# reuse ITEMS from gen_audio
spec = importlib.util.spec_from_file_location("gen", "/home/dan/dev/work/better/wt-juliana-a11/_build/juliana-aula11/gen_audio.py")
# avoid running tts: we just need ITEMS; gen_audio runs at import -> guard by not importing.
# Instead, redefine the key->file mapping here (must match gen_audio).
PAIRS = [
 ("El banco","aula11_el_banco.mp3"),
 ("La farmacia","aula11_la_farmacia.mp3"),
 ("El supermercado","aula11_el_supermercado.mp3"),
 ("La parada","aula11_la_parada.mp3"),
 ("La plaza","aula11_la_plaza.mp3"),
 ("La esquina","aula11_la_esquina.mp3"),
 ("La cuadra","aula11_la_cuadra.mp3"),
 ("El ayuntamiento","aula11_el_ayuntamiento.mp3"),
 ("La comisaria","aula11_la_comisaria.mp3"),
 ("El quiosco","aula11_el_quiosco.mp3"),
 ("Hola, soy Diego. Mi barrio es muy practico. Hay un banco y una farmacia en la esquina. El supermercado esta al lado de mi edificio. Enfrente de la plaza hay un quiosco donde compro el periodico. El ayuntamiento esta entre el banco y la plaza. La parada del autobus esta a una cuadra. La comisaria esta un poco lejos, a cinco cuadras.","aula11_listening_diego.mp3"),
 ("Diego, hay un banco cerca de la oficina?","aula11_dialogo_juliana_1.mp3"),
 ("Perfecto! Y donde esta la farmacia?","aula11_dialogo_juliana_2.mp3"),
 ("Y el ayuntamiento? Esta lejos?","aula11_dialogo_juliana_3.mp3"),
 ("Si, hay uno en la esquina, al lado del supermercado.","aula11_dialogo_diego_1.mp3"),
 ("Esta enfrente de la plaza, a dos cuadras de aqui.","aula11_dialogo_diego_2.mp3"),
 ("No, esta cerca, entre el banco y la plaza.","aula11_dialogo_diego_3.mp3"),
 ("Hay un banco en la esquina.","aula11_hay_banco_esquina.mp3"),
 ("La farmacia esta al lado del supermercado.","aula11_farmacia_lado_super.mp3"),
 ("La plaza esta enfrente del ayuntamiento.","aula11_plaza_enfrente_ayto.mp3"),
 ("La parada esta a dos cuadras de aqui.","aula11_parada_dos_cuadras.mp3"),
 ("El quiosco esta entre el banco y la plaza.","aula11_quiosco_entre.mp3"),
 ("Hay un banco por aqui?","aula11_hay_banco_por_aqui.mp3"),
 ("Donde esta la farmacia?","aula11_donde_farmacia.mp3"),
 ("Esta al lado del supermercado.","aula11_esta_lado_super.mp3"),
 ("Esta a dos cuadras de aqui.","aula11_esta_dos_cuadras.mp3"),
 ("El quiosco esta al lado del banco.","aula11_quiosco_lado_banco.mp3"),
 ("El ayuntamiento esta entre el banco y la plaza.","aula11_ayto_entre.mp3"),
 ("[order-l11]","aula11_order_l11_ordering.mp3"),
]

def esc(s): return s.replace("\\","\\\\").replace('"','\\"')
block = "\n".join('  "%s": "/audio/juliana-marques/%s",' % (esc(k), f) for k,f in PAIRS)

for path in ["public/professor/juliana-marques.html","public/aluno/juliana-marques.html"]:
    p = "/home/dan/dev/work/better/wt-juliana-a11/"+path
    h = io.open(p, encoding="utf-8").read()
    assert "aula11_" not in h, path+": aula11 already in audioMap"
    anchor = '  "[order-l10]": "/audio/juliana-marques/aula10_order_l10_ordering.mp3",'
    assert h.count(anchor)==1, path+": order-l10 anchor not unique"
    h = h.replace(anchor, anchor + "\n" + block, 1)
    io.open(p,"w",encoding="utf-8").write(h)
    print(path, "injected", len(PAIRS), "entries")
