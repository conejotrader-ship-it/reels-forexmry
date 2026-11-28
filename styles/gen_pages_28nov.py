#!/usr/bin/env python3
"""Genera las páginas v308–v314 (reels del 28 nov 6:00, 9:30, 13:00, 16:30, 20:00, 23:30 y 29 nov 3:00; lista viral). Estilos 42, 45, 43, 41, 40, 46, 44 (6.º uso, paletas nuevas)."""
import os, sys, copy
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import gen_pages_26nov as G
g = G.g
for k, deg, a, b in [('domino', 60, 'DOMINÓ EN CADENA · FTX 2022', 'ERROR ÉPICO · TUIT FALSO 2013'),
    ('book', 130, 'ENCICLOPEDIA · RECORTE DE AGOSTO 2011', 'ENCICLOPEDIA · ÍNDICE BIG MAC'),
    ('coaster', 210, 'MONTAÑA RUSA · ONDAS DE ELLIOTT', 'MONTAÑA RUSA · EL BARCO DEL ORO'),
    ('rayosx', 280, 'RAYOS X · POR DENTRO DE UN ETF DE ORO', 'RAYOS X · EL DISCO PERDIDO'),
    ('glitch', 320, '//SYS.MQL5 > COPYBUFFER_', '//LATENCIA > CHICAGO_NY_'),
    ('vhs', 30, '▶ PLAY  ·  REPLAY SNB 2011', '▶ PLAY  ·  BOWIE BONDS 1997'),
    ('chess', 170, 'AJEDREZ · LA JUGADA DE BURRY', 'AJEDREZ · LA JUGADA DE FORT KNOX')]:
    t = G.recolor(copy.deepcopy(g.THEMES[k]), deg); t['uso'] = '6.º'
    assert a in t['bg'], k
    t['bg'] = t['bg'].replace(a, b)
    if k == 'domino': t['C'] = ['#9a7b00', '#972a59', '#2a7d0a', '#2e1a29']
    g.THEMES[k] = t
R = []
exec(open(os.path.join(HERE, 'content_28nov.py'), encoding='utf-8').read())
if __name__ == '__main__':
    sel = [int(x) for x in sys.argv[1:]]
    for r in R:
        if sel and r['n'] not in sel: continue
        open(os.path.join(HERE, r['page'] + '.html'), 'w').write(g.build(r))
        print('ok', r['page'], r['scene'])
