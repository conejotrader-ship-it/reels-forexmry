#!/usr/bin/env python3
"""Genera las páginas v277–v283 (reels del 24 nov 2026). Estilos 12,16,10,11,13,15,14 (nuevas paletas, 6.º/7.º uso).
Uso: python3 gen_pages_24nov.py [n1 n2 ...]"""
import os, sys, copy
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import gen_pages_16nov as g
import gen_pages_17nov as g17
from gen_pages_17nov import mk

def sw(s, pairs):
    for a, b in pairs:
        assert a in s, a
        s = s.replace(a, b)
    return s

BG_PER = sw(g17.BG_PERIODICO, [("#e8dcc0","#dde3e8"),("#6b5530","#46525e"),("#f6eed8","#f2f5f7"),("EL DIARIO DEL MERCADO · EDICIÓN ESPECIAL","LA GACETA DE LOS BONOS · EDICIÓN 1994")])
BG_BLU = sw(g17.BG_BLUEPRINT, [("#0b3a6b","#0a4a3f"),("160,225,255","170,255,220"),("#7fe3ff","#7dffd0"),("rgba(6,40,80,.92)","rgba(4,48,40,.92)"),("PLANO · ESC. 1:1 · @forexmry","PLANO · KAMA · @forexmry")])
BG_BAR = sw(g.bg_barras(), [("#241338","#0e2a1f"),("#150a24","#07170f"),("'#ff6f59','#2ec4b6','#ffbf3c','#c77dff','#6ea8ff','#ff6f59','#2ec4b6'","'#f4a261','#2a9d8f','#e9c46a','#e76f51','#8ecae6','#f4a261','#2a9d8f'"),("rgba(36,19,56,.9)","rgba(14,42,31,.9)")])
BG_AMB = sw(g17.BG_AMBAR, [("#0b0700","#0e0503"),("255,176,0","255,128,40"),("#ffb000","#ff8a2a"),("#1a1200","#1f0b04"),("rgba(22,14,0,.93)","rgba(26,10,4,.93)"),("TERMINAL DE MERCADOS  >_","TERMINAL · ÍNDICE DE ÚLCERA  >_")])
BG_SUI = sw(g17.BG_SUIZO, [("#e30613","#0057b8"),("#f4f4f0","#eef1f5")])
BG_SUM = sw(g17.BG_SUMIE, [("#efe9dc","#e8eee6"),("#b3202a","#1f4e79")])
BG_LIN = sw(g17.BG_LINGOTES, [("#17120a","#1c1008"),("'#ffe08a'","'#ffd9a0'"),("'#e6a817'","'#d98a2b'"),("'#8c6410'","'#7a4310'"),("255,204,51","255,170,70"),("rgba(22,16,6,.93)","rgba(26,14,6,.93)")])

TH = {
 'periodico': mk(12, 'periódico gris azulado con tinta, óxido y azul marino', BG_PER, ["#b5451b","#12355b","#5c5c14","#2b2b2b"], '#16181c', '#4c5560', '#b5451b', '#f2f5f7', '#16181c',
   "rgba(242,245,247,.97)","#b5451b","#16181c","#16181c","#f2f5f7","#e0a030","#e0a030","#16181c",'rgba(242,245,247,.92)',0,1,2,'#4c5560',1,'#f2f5f7'),
 'blueprint': mk(16, 'plano verde azulado con cuadrícula menta y cotas', BG_BLU, ["#7dffd0","#ffffff","#ffd166","#ff9f6b"], '#e8fff6', '#9fe0c8', '#7dffd0', '#04302a', '#04302a',
   "rgba(4,48,40,.97)","#7dffd0","#e8fff6","#04302a","#e8fff6","#7dffd0","#7dffd0","#04302a",'rgba(4,48,40,.88)',0,2,3,'#9fe0c8',2,'#04302a'),
 'ambar': mk(11, 'terminal naranja rojizo sobre negro con barrido de fósforo', BG_AMB, ["#ff8a2a","#ffd166","#ff5a5f","#ffe9d0"], '#ffd9b8', '#c0804a', '#ff8a2a', '#1f0b04', '#0e0503',
   "rgba(14,5,3,.96)","#ff8a2a","#ffd9b8","#0e0503","#ffd9b8","#ff8a2a","#ff8a2a","#0e0503",'rgba(14,5,3,.88)',0,2,3,'#c0804a',1,'#0e0503'),
 'suizo': mk(13, 'retícula suiza gris claro con azul cobalto y negro', BG_SUI, ["#0057b8","#111111","#ff6b00","#c8102e"], '#111111', '#555555', '#0057b8', '#ffffff', '#111111',
   "rgba(255,255,255,.97)","#0057b8","#111111","#111111","#ffffff","#4da3ff","#4da3ff","#ffffff",'rgba(255,255,255,.93)',0,1,2,'#555555',0,'#ffffff'),
 'sumie': mk(15, 'papel verdoso con pinceladas de tinta y sello índigo', BG_SUM, ["#1f4e79","#1a1a1a","#8a6d1f","#1f4e79"], '#1a1a1a', '#55594c', '#1f4e79', '#f6f9f3', '#1a1a1a',
   "rgba(246,249,243,.97)","#1f4e79","#1a1a1a","#1a1a1a","#f6f9f3","#e3a93f","#e3a93f","#1a1a1a",'rgba(246,249,243,.92)',0,1,2,'#55594c',0,'#f6f9f3'),
 'lingotes': mk(14, 'mina oscura con barras de oro cobrizo', BG_LIN, ["#ffb347","#e07a1f","#ffe0a8","#9fd3c7"], '#fff1dc', '#cfae84', '#ffb347', '#1a0f06', '#080604',
   "rgba(10,6,3,.96)","#ffb347","#fff1dc","#080604","#fff1dc","#ffb347","#ffb347","#080604",'rgba(10,6,3,.88)',0,2,3,'#cfae84',0,'#080604'),
}
b = copy.deepcopy(g.THEMES['barras'])
b.update(pal='verde bosque con barras ocre, turquesa, arena y coral', bg=BG_BAR, C=["#f4a261","#2a9d8f","#e9c46a","#e76f51"], mu='#a9cdb8', acc='#e9c46a', pn='#0e2a1f', dk='#07170f')
b['sty'].update(subBg="rgba(7,23,15,.96)", subStroke="#e9c46a", ctaBg="#07170f", ctaGlow="#e9c46a", ctaAccent="#e9c46a", ctaBtnText="#07170f")
b['cov'].update(ov='rgba(7,23,15,.86)', mu='#a9cdb8', btxt='#07170f')
TH['barras'] = b
for k, v in TH.items(): v['uso'] = '6.º' if k in ('barras','periodico','blueprint','ambar','suizo','sumie','lingotes') else v.get('uso')
g.THEMES.update(TH)

R = []
exec(open(os.path.join(HERE, 'content_24nov.py'), encoding='utf-8').read())

if __name__ == '__main__':
    sel = [int(x) for x in sys.argv[1:]]
    for r in R:
        if sel and r['n'] not in sel: continue
        open(os.path.join(HERE, r['page'] + '.html'), 'w').write(g.build(r))
        print('ok', r['page'], r['scene'])
