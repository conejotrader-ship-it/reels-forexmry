#!/usr/bin/env python3
"""Genera las páginas v291–v297 (reels del 26 nov 2026). Estilos 24–30 (5.º uso, nuevas paletas por rotación de matiz).
Uso: python3 gen_pages_26nov.py [n1 n2 ...]"""
import os, sys, re, copy, colorsys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import gen_pages_16nov as g
for m in range(17, 26): __import__('gen_pages_%dnov' % m)

def rot(r, gg, b, deg):
    h, l, s = colorsys.rgb_to_hls(r/255, gg/255, b/255)
    if s < .15: return r, gg, b
    h = (h + deg/360) % 1
    if l > .25 and .62 <= h <= .80: h = (h + .2) % 1
    return tuple(round(x*255) for x in colorsys.hls_to_rgb(h, l, s))

def recolor(o, deg):
    def hx(m):
        v = m.group(1); r, gg, b = int(v[0:2],16), int(v[2:4],16), int(v[4:6],16)
        return '#%02x%02x%02x' % rot(r, gg, b, deg)
    def tri(m):
        r, gg, b = int(m.group(1)), int(m.group(2)), int(m.group(3))
        if max(r, gg, b) > 255: return m.group(0)
        return '%d,%d,%d' % rot(r, gg, b, deg)
    def f(s):
        s = re.sub(r'#([0-9a-fA-F]{6})\b', hx, s)
        s = re.sub(r'(?<![\d.])(\d{1,3}),(\d{1,3}),(\d{1,3})(?![\d.])', tri, s)
        return s
    if isinstance(o, str): return f(o)
    if isinstance(o, list): return [recolor(i, deg) for i in o]
    if isinstance(o, dict): return {k: recolor(v, deg) for k, v in o.items()}
    return o

DEG = {'split': 100, 'documental': 150, 'monitores': 75, 'reloj': 110, 'expediente': 140, 'radar': 160, 'velocimetro': 70}
for k, d in DEG.items():
    t = recolor(copy.deepcopy(g.THEMES[k]), d); t['uso'] = '5.º'
    g.THEMES[k] = t

R = []
exec(open(os.path.join(HERE, 'content_26nov.py'), encoding='utf-8').read())

if __name__ == '__main__':
    sel = [int(x) for x in sys.argv[1:]]
    for r in R:
        if sel and r['n'] not in sel: continue
        open(os.path.join(HERE, r['page'] + '.html'), 'w').write(g.build(r))
        print('ok', r['page'], r['scene'])
