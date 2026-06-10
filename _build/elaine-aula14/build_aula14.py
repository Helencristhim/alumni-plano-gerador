#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build standalone Aula 11 (Elaine) — Paying the Bill. Splices authored content into the
proven aula9 scaffold (CSS+JS verbatim). Mirrors build_aula10.py. Outputs prof+aluno+generator."""
import os, re, json

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
PROF_SCAFFOLD  = os.path.join(ROOT, 'public', 'professor', 'elaine-mieko-pinho-aula9.html')
ALUNO_SCAFFOLD = os.path.join(ROOT, 'public', 'aluno', 'elaine-mieko-pinho-aula9.html')
PROF_OUT  = os.path.join(ROOT, 'public', 'professor', 'elaine-mieko-pinho-aula14.html')
ALUNO_OUT = os.path.join(ROOT, 'public', 'aluno', 'elaine-mieko-pinho-aula14.html')
GEN_OUT   = os.path.join(ROOT, 'scripts', 'generate-elaine-aula14-audio.js')
SLUG = 'elaine-mieko-pinho'

def read(p):
    with open(p, encoding='utf-8') as f: return f.read()

slides   = read(os.path.join(HERE, 'slides.html'))
preclass = read(os.path.join(HERE, 'preclass.html'))
compl    = read(os.path.join(HERE, 'complementary.html'))
phrases  = json.loads(read(os.path.join(HERE, 'phrases.json')))
N = len(re.findall(r'data-slide="\d+"', slides)); assert N == 28

def replace_between(s, start, end, new_inner):
    i = s.index(start); j = s.index(end, i + len(start))
    return s[:i] + start + '\n' + new_inner + '\n' + end + s[j + len(end):]
def must(s, old, new):
    assert old in s, 'anchor missing: %.40s' % old
    return s.replace(old, new, 1)

AUDIOMAP = 'var audioMap = {\n' + ',\n'.join(
    '  %s: %s' % (json.dumps(p['key'], ensure_ascii=False), json.dumps('/audio/%s/' % SLUG + p['file'], ensure_ascii=False))
    for p in phrases) + '\n}'

AUDIT = '''<!--
SCENARIO FIT — Aula 14
Can-do: "I can use the subway and the bus: ask the line, buy a ticket, find the platform."
Gramatica-alvo: "Which + noun + goes to...?"; "Where is the nearest + place?"; "Do I need to + verb?"; "How do I get to...?" (revisao L13).
Vocab-alvo: subway, bus, ticket, stop, platform, line, transfer, schedule.
Cenario escolhido: estacao de metro/onibus em New York, comprando bilhete e achando a plataforma.
Por que elicita o alvo: pegar transporte OBRIGA o aluno a perguntar a linha, o preco do bilhete e sobre baldeacao. >70% dos itens-alvo elicitados.

CONTINUIDADE — Aula 14
Itens novos: subway, bus, ticket, stop, platform, line, transfer, schedule; "Which... goes to...?", "Where is the nearest...?", "Do I need to...?".
Itens revisados (L13): "Where is...?", "How do I get to...?", left/right, across the street.
Callback no warm-up (slide 2): retoma ATIVAMENTE 2 itens da Aula 13 — o aluno ouve e repete "Where is the museum?" e "How do I get to the station?", e faz a ponte: o lugar e longe, agora precisa do metro ou onibus.
-->
'''

def build(scaffold, badge_is_aluno):
    h = scaffold
    h = must(h, 'Aula 9 | Restaurant Basics', 'Aula 14 | Public Transportation')
    i = h.index('var audioMap = {'); j = h.index('};', i)
    h = h[:i] + AUDIOMAP + h[j+1:]
    stamp9 = '<div class="stamp" id="stamp9" data-label="Restaurant" style="background-image:url(\'https://images.unsplash.com/photo-1414235077428-338989a2e8c0?w=200&q=80\')"></div>'
    extra = ('\n<div class="stamp" id="stamp10" data-label="Allergies" style="background-image:url(\'https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?w=200&q=80\')"></div>'
             '\n<div class="stamp" id="stamp11" data-label="Paying" style="background-image:url(\'https://images.unsplash.com/photo-1554224155-6726b3ff858f?w=200&q=80\')"></div>'
             '\n<div class="stamp" id="stamp12" data-label="Cafe" style="background-image:url(\'https://images.unsplash.com/photo-1501339847302-ac426a4a7cbb?w=200&q=80\')"></div>'
             '\n<div class="stamp" id="stamp13" data-label="Directions" style="background-image:url(\'https://images.unsplash.com/photo-1502920514313-52581002a659?w=200&q=80\')"></div>'
             '\n<div class="stamp" id="stamp14" data-label="Transport" style="background-image:url(\'https://images.unsplash.com/photo-1556122071-e404eaedb77f?w=200&q=80\')"></div>')
    h = must(h, stamp9, stamp9 + extra)
    h = must(h, '<body>\n', '<body>\n' + AUDIT)
    pre_start = '<div class="tab-content active" id="tab-exercises">' if 'active" id="tab-exercises"' in h else '<div class="tab-content" id="tab-exercises">'
    h = replace_between(h, pre_start, '</div><!-- /tab-exercises -->', preclass)
    h = replace_between(h, '<div class="tab-content" id="tab-complementary">', '</div><!-- /tab-complementary -->', compl)
    if not badge_is_aluno:
        MENU = ('  <h3 style="font-family:\'Cormorant Garamond\',serif;font-size:1.3rem;margin-bottom:1rem">IN CLASS &mdash; Aula 14</h3>\n'
                '  <div style="display:flex;flex-direction:column;gap:1rem">\n'
                '    <div style="display:flex;align-items:center;gap:1rem;padding:1.2rem;background:rgba(255,255,255,.5);backdrop-filter:blur(8px);border:1px solid rgba(200,200,190,.5);border-radius:10px;cursor:pointer;transition:all .3s" onclick="startLesson(1,28)" onmouseover="this.style.borderColor=\'var(--accent)\'" onmouseout="this.style.borderColor=\'rgba(200,200,190,.5)\'">\n'
                '      <div style="width:48px;height:48px;background:var(--accent);border-radius:8px;display:flex;align-items:center;justify-content:center;color:#fff;font-weight:700;font-size:1.1rem">11</div>\n'
                '      <div><div style="font-weight:600;font-size:.95rem">Public Transportation</div><div style="font-size:.8rem;color:var(--text-dim)">Subway, bus &amp; tickets -- 28 slides</div></div>\n'
                '    </div>\n  </div>\n')
        h = replace_between(h, '<div class="tab-content" id="tab-inclass">', '<!-- ========== TAB 4: COMPLEMENTARES ========== -->', MENU + '</div>\n\n')
        h = replace_between(h, '<div class="slides-container" id="slidesContainer">', '</div><!-- /slides-container -->', slides)
        h = must(h, 'var dialogueLine = 0;', 'var dialogueLine = 1;')
        h = must(h, "    if (dialogueLine >= 8) {\n      document.getElementById('nextLineBtn').textContent = 'Dialogue Complete';",
                    "    if (dialogueLine >= 12) {\n      document.getElementById('nextLineBtn').textContent = 'Dialogue Complete';")
    return h

with open(PROF_OUT, 'w', encoding='utf-8') as f: f.write(build(read(PROF_SCAFFOLD), False))
with open(ALUNO_OUT, 'w', encoding='utf-8') as f: f.write(build(read(ALUNO_SCAFFOLD), True))

gen_phrases = ',\n'.join('  { text: %s, file: %s, voice: %s }' % (
    json.dumps(p['text'], ensure_ascii=False), json.dumps(p['file']), json.dumps(p['voice'])) for p in phrases)
GEN = '''#!/usr/bin/env node
const fs=require('fs'),path=require('path');
const API='https://api.elevenlabs.io/v1/text-to-speech';
const V={arthur:'sfJopaWaOtauCD3HKX6Q',ellen:'BIvP0GN1cAtSRTxNHnWS',josh:'TxGEqnHWrfWFTfGW9XjX',rachel:'21m00Tcm4TlvDq8ikWAM',domi:'AZnzlk1XvdvUeBnXmlld',bella:'EXAVITQu4vr4xnSDxMaL'};
const KEY=process.env.ELEVENLABS_API_KEY, OUT=path.join(__dirname,'..','public','audio','%SLUG%');
if(!KEY){console.error('Set ELEVENLABS_API_KEY');process.exit(1);} if(!fs.existsSync(OUT))fs.mkdirSync(OUT,{recursive:true});
const phrases=[\n%P%\n];
async function gen(t,f,v){const fp=path.join(OUT,f); if(fs.existsSync(fp))return{s:1};
  const r=await fetch(`${API}/${v}`,{method:'POST',headers:{'xi-api-key':KEY,'Content-Type':'application/json'},body:JSON.stringify({text:t,model_id:'eleven_multilingual_v2',voice_settings:{stability:0.5,similarity_boost:0.75,style:0,use_speaker_boost:true}})});
  if(!r.ok)throw new Error(r.status+' '+t.slice(0,30)); fs.writeFileSync(fp,Buffer.from(await r.arrayBuffer())); return{s:0};}
(async()=>{let g=0,s=0,e=0;for(const p of phrases){try{const r=await gen(p.text,p.file,V[p.voice]);if(r.s){s++;}else{g++;await new Promise(x=>setTimeout(x,300));}}catch(x){e++;console.error(x.message);}}console.log(`done ${g} gen, ${s} skip, ${e} err`);})();
'''
GEN = GEN.replace('%SLUG%', SLUG).replace('%P%', gen_phrases)
with open(GEN_OUT, 'w', encoding='utf-8') as f: f.write(GEN)
print('OK aula11 standalone built; audioMap keys', len(phrases))
