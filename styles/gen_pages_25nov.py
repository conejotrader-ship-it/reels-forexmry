#!/usr/bin/env python3
"""Genera las páginas v284–v290 (reels del 25 nov 2026). Estilos 17–23 (nuevas paletas, 5.º uso).
Uso: python3 gen_pages_25nov.py [n1 n2 ...]"""
import os, sys, re, copy
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import gen_pages_16nov as g
import gen_pages_17nov, gen_pages_18nov  # registran temas 17–24 en g.THEMES

def recolor(o, m):
    rx = re.compile('|'.join(re.escape(k) for k in sorted(m, key=len, reverse=True)))
    f = lambda s: rx.sub(lambda x: m[x.group(0)], s)
    if isinstance(o, str): return f(o)
    if isinstance(o, list): return [recolor(i, m) for i in o]
    if isinstance(o, dict): return {k: recolor(v, m) for k, v in o.items()}
    return o

MAPS = {
 'papercut': {'#0f4c5c':'#3a1c5c','#0a2f3a':'#22103a','#1b6b7a':'#6a3d9a','#ffb703':'#ff9ecb','255,183,3':'255,158,203','#fb8500':'#f4845f','#8ecae6':'#9bf6ff','rgba(2,48,71':'rgba(34,16,58','#023047':'#22103a','#a8d4de':'#d5c2f0'},
 'libro': {'#0c1119':'#1a0f08','#131b28':'#2a1a10','#2de2a6':'#ffb454','45,226,166':'255,180,84','#ff5d73':'#5ec8ff','255,93,115':'94,200,255','#e8eef7':'#fdf3e6','#8a97ab':'#b9a48c','rgba(12,17,25':'rgba(26,15,8','138,151,171':'185,164,140','rgba(19,27,40':'rgba(42,26,16'},
 'cuaderno': {'#f2ead8':'#e6f0e6','#1d4ed8':'#0f766e','29,78,216':'15,118,110','#c2410c':'#be185d','194,65,12':'190,24,93','#fffdf4':'#fbfff8','#f6f1e3':'#f4faf2','#10243f':'#0b2e2b','#047857':'#6d28d9','#7c2d12':'#831843','rgba(255,253,244':'rgba(251,255,248'},
 'pixel': {'#1b1038':'#0f2a1e','#2a1a55':'#173d2b','#ffe14d':'#ff9f43','255,225,77':'255,159,67','#5ef2a0':'#7ad7ff','#ff6bd6':'#ff6b6b','#b9a8e8':'#a8d8b9','122,215,255':'255,225,77','#7ad7ff':'#ffe14d','rgba(27,16,56':'rgba(15,42,30'},
 'timeline': {'#06231c':'#1c0a2e','#6ee7b7':'#ff9ecb','110,231,183':'255,158,203','#f6c453':'#7ae7ff','246,196,83':'122,231,255','#fb7185':'#ffd166','#8cc9b2':'#c9a8e8','rgba(6,35,28':'rgba(28,10,46'},
 'noticiero': {'#0a1a3a':'#1a0a2a','#050d1f':'#0d0517','#ffd400':'#00e0c6','#ff4d4d':'#ff3b8a','#5ec8ff':'#ffd400','94,200,255':'255,212,0','rgba(8,22,52':'rgba(26,10,42','rgba(5,13,31':'rgba(13,5,23','#9db4d9':'#c9a8e8'},
 'mapa': {'#0b1d2e':'#2b0f1a','#ffb703':'#7ae7ff','255,183,3':'122,231,255','#06d6a0':'#ffd166','6,214,160':'255,209,102','#4cc9f0':'#ff7aa8','76,201,240':'255,122,168','#8fb3cc':'#d9a8b8','rgba(11,29,46':'rgba(43,15,26'},
}
for k, m in MAPS.items():
    t = recolor(copy.deepcopy(g.THEMES[k]), m); t['uso'] = '5.º'
    g.THEMES[k] = t

R = []
exec(open(os.path.join(HERE, 'content_25nov.py'), encoding='utf-8').read())

if __name__ == '__main__':
    sel = [int(x) for x in sys.argv[1:]]
    for r in R:
        if sel and r['n'] not in sel: continue
        open(os.path.join(HERE, r['page'] + '.html'), 'w').write(g.build(r))
        print('ok', r['page'], r['scene'])
