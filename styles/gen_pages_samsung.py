#!/usr/bin/env python3
"""Genera la página v302 (lista viral n.º 2: Samsung Securities 2018, pedido en vivo el 26 nov 2026). Estilo 34 (6.º uso, paleta nueva por rotación de matiz).
Lleva clips animados (render_anim.py) y carátula con foto (make_photo_cover.py).
Uso: python3 gen_pages_samsung.py"""
import os, sys, copy
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import gen_pages_26nov as G
g = G.g
t = G.recolor(copy.deepcopy(g.THEMES['lowpoly']), 150); t['uso'] = '6.º'
g.THEMES['lowpoly'] = t
g.THEMES['lowpoly']['bg'] = g.THEMES['lowpoly']['bg'].replace('WYCKOFF · MONTAÑAS LOWPOLY', 'ERRORES ÉPICOS · SEÚL 2018')
R = []
exec(open(os.path.join(HERE, 'content_samsung.py'), encoding='utf-8').read())
if __name__ == '__main__':
    for r in R:
        open(os.path.join(HERE, r['page'] + '.html'), 'w').write(g.build(r))
        print('ok', r['page'], r['scene'])
