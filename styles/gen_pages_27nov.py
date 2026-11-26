#!/usr/bin/env python3
"""Genera las páginas v299–v301 (primeros reels de la LISTA VIRAL, 27 nov 2026). Estilos 31–33 (5.º uso, paletas nuevas por rotación de matiz).
Llevan clips animados (render_anim.py) y carátulas con foto (make_photo_cover.py).
Uso: python3 gen_pages_27nov.py [n1 n2 ...]"""
import os, sys, copy
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import gen_pages_26nov as G
g = G.g
DEG = {'semaforo': 120, 'iso': 150, 'pixel8': 60}
for k, d in DEG.items():
    t = G.recolor(copy.deepcopy(g.THEMES[k]), d); t['uso'] = '5.º'
    g.THEMES[k] = t
# rótulos de esquina de usos anteriores -> rótulos de la lista viral
LAB = {'semaforo': ('ROBOTS  ·  MQL5  ·  CRITERIO', 'ERRORES ÉPICOS  ·  TRADING'),
       'iso': ('CIUDAD ISOMÉTRICA · DERIVADOS 2025', 'ORO CURIOSO · NUEVA YORK'),
       'pixel8': ('NIVEL 1 · CRIPTO · 8 BITS', 'INDICADORES RAROS · 8 BITS')}
for k, (a, b) in LAB.items():
    g.THEMES[k]['bg'] = g.THEMES[k]['bg'].replace(a, b)

R = []
exec(open(os.path.join(HERE, 'content_27nov.py'), encoding='utf-8').read())

if __name__ == '__main__':
    sel = [int(x) for x in sys.argv[1:]]
    for r in R:
        if sel and r['n'] not in sel: continue
        open(os.path.join(HERE, r['page'] + '.html'), 'w').write(g.build(r))
        print('ok', r['page'], r['scene'])
