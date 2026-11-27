#!/usr/bin/env python3
"""Genera las páginas v304–v307 (reels del 27 nov 16:30, 20:00, 23:30 y 28 nov 3:00; lista viral). Estilos 36–39 (nuevas paletas)."""
import os, sys, copy
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import gen_pages_26nov as G
g = G.g
for k, deg, a, b in [('deco', 40, 'ART DÉCO · ACKMAN 2020', 'PERSONAJES · FLORIDA 2010'),
    ('teletipo', 170, 'ZN  ·  TELETIPO  ·  INTERÉS ABIERTO', 'ROBOTS Y EA  ·  LONDRES 2012'),
    ('crt', 200, 'C:\\\\MQL5\\\\EXPERTS> ORDERCHECK_', 'C:\\\\MERCADOS> VW_2008_'),
    ('holo', 120, 'HOLOGRAMA · GESTORES DE ACTIVOS', 'ERRORES ÉPICOS · FRÁNCFORT 2015')]:
    t = G.recolor(copy.deepcopy(g.THEMES[k]), deg); t['uso'] = '5.º'
    assert a in t['bg'], k
    t['bg'] = t['bg'].replace(a, b)
    g.THEMES[k] = t
R = []
exec(open(os.path.join(HERE, 'content_27nov_noche.py'), encoding='utf-8').read())
if __name__ == '__main__':
    for r in R:
        open(os.path.join(HERE, r['page'] + '.html'), 'w').write(g.build(r))
        print('ok', r['page'], r['scene'])
