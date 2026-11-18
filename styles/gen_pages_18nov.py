#!/usr/bin/env python3
"""Genera las páginas v235–v241 (reels del 18 nov 2026) con la plantilla std/h0/b6 de gen_pages_16nov.
Estilos 18–24 (4.º uso, nuevas paletas). Uso: python3 gen_pages_18nov.py [n1 n2 ...]"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import gen_pages_16nov as g

def mk(est, pal, bg, C, txt, mu, acc, pn, dk, subBg, subStroke, subFill, ctaBg, ctaSub, ctaGlow, ctaAccent, ctaBtnText, ov, c1, c2, c3, covmu, btn, btxt, lt=None):
    return dict(est=est, uso='4.º', pal=pal, bg=bg, C=C, txt=txt, lt=lt or txt, mu=mu, acc=acc, pn=pn, dk=dk,
        sty=dict(subBg=subBg, subStroke=subStroke, subFill=subFill, ctaBg=ctaBg, ctaSub=ctaSub, ctaGlow=ctaGlow, ctaAccent=ctaAccent, ctaBtnText=ctaBtnText),
        cov=dict(ov=ov, c1=c1, c2=c2, c3=c3, mu=covmu, btn=btn, btxt=btxt))

BG_LIBRO = """ST.bg=t=>{ctx.fillStyle='#0c1119';ctx.fillRect(0,0,W,H);
  for(let i=0;i<14;i++){const y=1480+i*28;const w=60+((i*53+Math.floor(t*3+i))%9)*34;ctx.fillStyle='rgba(45,226,166,.16)';ctx.fillRect(W-40-w,y,w,20);ctx.fillStyle='rgba(255,93,115,.16)';ctx.fillRect(40,y,w*.9,20)}
  ctx.fillStyle='#131b28';ctx.fillRect(0,0,W,64);ctx.fillStyle='#2de2a6';ctx.font='800 26px Inter';ctx.textAlign='left';ctx.fillText('LIBRO DE ÓRDENES  ·  BID / ASK',24,42);ctx.textAlign='center';
  ctx.strokeStyle='rgba(138,151,171,.18)';ctx.lineWidth=2;for(let y=120;y<1400;y+=70){ctx.beginPath();ctx.moveTo(30,y);ctx.lineTo(W-30,y);ctx.stroke()}};
ST.panel=(x,y,w,h,col)=>{ctx.save();ctx.fillStyle='rgba(19,27,40,.95)';RR(x,y,w,h,10);ctx.fill();ctx.lineWidth=3;ctx.strokeStyle=col;RR(x,y,w,h,10);ctx.stroke();ctx.fillStyle=col;ctx.fillRect(x,y,12,h);ctx.restore()};"""

BG_CUADERNO = """ST.bg=t=>{ctx.fillStyle='#f2ead8';ctx.fillRect(0,0,W,H);ctx.strokeStyle='rgba(29,78,216,.22)';ctx.lineWidth=2;for(let y=110;y<H;y+=64){ctx.beginPath();ctx.moveTo(0,y);ctx.lineTo(W,y);ctx.stroke()}
  ctx.strokeStyle='rgba(194,65,12,.55)';ctx.lineWidth=4;ctx.beginPath();ctx.moveTo(90,0);ctx.lineTo(90,H);ctx.stroke();
  ctx.fillStyle='rgba(60,50,30,.35)';for(let i=0;i<12;i++){ctx.beginPath();ctx.arc(34,150+i*150,14,0,7);ctx.fill()}
  ctx.save();ctx.globalAlpha=.20;ctx.strokeStyle='#1d4ed8';ctx.lineWidth=6;ctx.beginPath();for(let i=0;i<=22;i++){const x=i*50,y=1700-Math.sin(i*.6+t*.6)*50-i*8;i?ctx.lineTo(x,y):ctx.moveTo(x,y)}ctx.stroke();ctx.restore()};
ST.panel=(x,y,w,h,col)=>{ctx.save();ctx.fillStyle='rgba(255,253,244,.96)';ctx.fillRect(x,y,w,h);ctx.lineWidth=3;ctx.strokeStyle='#1b1b1b';ctx.strokeRect(x,y,w,h);ctx.fillStyle=col;ctx.fillRect(x,y,14,h);ctx.fillStyle='rgba(255,230,120,.7)';ctx.fillRect(x+w-90,y-10,70,24);ctx.restore()};"""

BG_PIXEL = """ST.bg=t=>{ctx.fillStyle='#1b1038';ctx.fillRect(0,0,W,H);const r=rng(3);for(let i=0;i<70;i++){const x=Math.floor(r()*W/12)*12,y=Math.floor(r()*1500/12)*12;ctx.fillStyle=(i+Math.floor(t*2))%5?'rgba(255,255,255,.35)':'rgba(255,225,77,.7)';ctx.fillRect(x,y,12,12)}
  for(let x=0;x<W;x+=60){const h=60+((x/60*37)%5)*30;ctx.fillStyle='#2e7d4f';ctx.fillRect(x,1760-h+60,60,12);ctx.fillStyle='#6b4a2b';ctx.fillRect(x,1832-h+60,60,H)}
  ctx.fillStyle='#ffe14d';ctx.fillRect(40,36,48,48);ctx.fillStyle='#1b1038';ctx.fillRect(52,52,10,10);ctx.fillRect(68,52,10,10);
  ctx.strokeStyle='rgba(122,215,255,.5)';ctx.lineWidth=8;ctx.strokeRect(20,20,W-40,H-40)};
ST.panel=(x,y,w,h,col)=>{ctx.save();ctx.fillStyle='#2a1a55';ctx.fillRect(x,y,w,h);ctx.fillStyle='#000';ctx.fillRect(x+10,y+h,w,10);ctx.fillRect(x+w,y+10,10,h);ctx.lineWidth=8;ctx.strokeStyle=col;ctx.strokeRect(x,y,w,h);ctx.restore()};"""

BG_TIMELINE = """ST.bg=t=>{ctx.fillStyle='#06231c';ctx.fillRect(0,0,W,H);const g2=ctx.createRadialGradient(540,1000,100,540,1000,1300);g2.addColorStop(0,'rgba(110,231,183,.10)');g2.addColorStop(1,'rgba(0,0,0,0)');ctx.fillStyle=g2;ctx.fillRect(0,0,W,H);
  ctx.strokeStyle='#6ee7b7';ctx.lineWidth=6;ctx.beginPath();ctx.moveTo(0,1560);ctx.lineTo(W,1560);ctx.stroke();
  const off=(t*40)%120;for(let x=-120+off;x<W+120;x+=120){ctx.beginPath();ctx.moveTo(x,1540);ctx.lineTo(x,1580);ctx.stroke();ctx.fillStyle='rgba(246,196,83,.55)';ctx.beginPath();ctx.arc(x+60,1560,9,0,7);ctx.fill()}
  ctx.strokeStyle='rgba(246,196,83,.5)';ctx.lineWidth=4;ctx.strokeRect(26,26,W-52,H-52)};
ST.panel=(x,y,w,h,col)=>{ctx.save();ctx.fillStyle='rgba(6,35,28,.94)';RR(x,y,w,h,16);ctx.fill();ctx.lineWidth=5;ctx.strokeStyle=col;RR(x,y,w,h,16);ctx.stroke();ctx.fillStyle=col;ctx.beginPath();ctx.arc(x+26,y+26,10,0,7);ctx.fill();ctx.restore()};"""

BG_NOTICIERO = """ST.bg=t=>{const g2=ctx.createLinearGradient(0,0,0,H);g2.addColorStop(0,'#0a1a3a');g2.addColorStop(1,'#050d1f');ctx.fillStyle=g2;ctx.fillRect(0,0,W,H);
  ctx.fillStyle='#ffd400';ctx.fillRect(0,1640,W,90);ctx.fillStyle='#0a1a3a';ctx.font='900 40px Inter';ctx.textAlign='left';const tx=-((t*160)%900);for(let k=0;k<4;k++)ctx.fillText('ÚLTIMA HORA  ■  MERCADOS  ■  @forexmry  ■  ',tx+k*900,1700);ctx.textAlign='center';
  ctx.fillStyle='#ff4d4d';ctx.fillRect(40,40,230,56);ctx.fillStyle='#fff';ctx.font='900 32px Inter';ctx.fillText('EN VIVO',155,80);
  ctx.save();ctx.globalAlpha=.10;ctx.strokeStyle='#5ec8ff';ctx.lineWidth=3;for(let i=0;i<8;i++){ctx.beginPath();ctx.arc(900,300,80+i*70,0,7);ctx.stroke()}ctx.restore()};
ST.panel=(x,y,w,h,col)=>{ctx.save();ctx.fillStyle='rgba(8,22,52,.94)';ctx.fillRect(x,y,w,h);ctx.fillStyle=col;ctx.fillRect(x,y,w,10);ctx.lineWidth=2;ctx.strokeStyle='rgba(94,200,255,.5)';ctx.strokeRect(x,y,w,h);ctx.restore()};"""

BG_MAPA = """ST.bg=t=>{ctx.fillStyle='#0b1d2e';ctx.fillRect(0,0,W,H);const blobs=[[260,520,230,150],[330,820,120,170],[700,540,170,120],[760,860,110,160],[900,1010,130,70],[820,380,200,90]];
  blobs.forEach(([cx,cy,rx,ry],bi)=>{for(let y=cy-ry;y<cy+ry;y+=22)for(let x=cx-rx;x<cx+rx;x+=22){const d=((x-cx)/rx)**2+((y-cy)/ry)**2;if(d<1){ctx.fillStyle='rgba(76,201,240,'+(.14+.10*Math.sin(t*1.4+x*.02+y*.02+bi))+')';ctx.beginPath();ctx.arc(x,y,5,0,7);ctx.fill()}}});
  ctx.save();ctx.strokeStyle='rgba(255,183,3,.45)';ctx.lineWidth=4;ctx.setLineDash([14,12]);ctx.lineDashOffset=-t*40;ctx.beginPath();ctx.moveTo(260,520);ctx.quadraticCurveTo(540,200,820,380);ctx.stroke();ctx.beginPath();ctx.moveTo(820,380);ctx.quadraticCurveTo(900,700,760,860);ctx.stroke();ctx.restore();
  ctx.strokeStyle='rgba(6,214,160,.45)';ctx.lineWidth=3;ctx.strokeRect(26,26,W-52,H-52)};
ST.panel=(x,y,w,h,col)=>{ctx.save();ctx.fillStyle='rgba(11,29,46,.93)';RR(x,y,w,h,14);ctx.fill();ctx.lineWidth=4;ctx.strokeStyle=col;RR(x,y,w,h,14);ctx.stroke();ctx.fillStyle=col;ctx.beginPath();ctx.arc(x+w-30,y+30,10,0,7);ctx.fill();ctx.restore()};"""

BG_SPLIT = """ST.bg=t=>{const m=540+Math.sin(t*.5)*40;ctx.fillStyle='#13294b';ctx.fillRect(0,0,m,H);ctx.fillStyle='#3b0f2e';ctx.fillRect(m,0,W-m,H);
  ctx.fillStyle='#ffd166';ctx.fillRect(m-6,0,12,H);ctx.font='900 34px Inter';ctx.textAlign='center';ctx.fillStyle='rgba(255,209,102,.8)';ctx.fillText('ANTES',m/2,1790);ctx.fillText('DESPUÉS',m+(W-m)/2,1790);
  ctx.save();ctx.globalAlpha=.12;ctx.fillStyle='#06d6a0';for(let i=0;i<6;i++){const h=120+i*60+Math.sin(t+i)*20;ctx.fillRect(40+i*80,1700-h,56,h)}ctx.fillStyle='#ef476f';for(let i=0;i<6;i++){const h=120+(5-i)*60+Math.sin(t+i)*20;ctx.fillRect(m+60+i*80,1700-h,56,h)}ctx.restore();
  ctx.strokeStyle='rgba(255,209,102,.5)';ctx.lineWidth=4;ctx.strokeRect(26,26,W-52,H-52)};
ST.panel=(x,y,w,h,col)=>{ctx.save();ctx.fillStyle='rgba(12,14,30,.93)';RR(x,y,w,h,14);ctx.fill();ctx.lineWidth=5;ctx.strokeStyle=col;RR(x,y,w,h,14);ctx.stroke();ctx.restore()};"""

g.THEMES.update({
 'libro': mk(18, 'libro de órdenes grafito con escalera de bids verdes y asks rosados', BG_LIBRO, ["#2de2a6","#ff5d73","#ffd24a","#ffffff"], '#e8eef7', '#8a97ab', '#2de2a6', '#131b28', '#0c1119',
   "rgba(12,17,25,.96)","#2de2a6","#e8eef7","#0c1119","#e8eef7","#2de2a6","#2de2a6","#0c1119",'rgba(12,17,25,.88)',2,0,1,'#8a97ab',0,'#0c1119'),
 'cuaderno': mk(19, 'cuaderno de papel crema con tinta azul, margen rojo y marcador amarillo', BG_CUADERNO, ["#1d4ed8","#c2410c","#047857","#7c2d12"], '#1b1b1b', '#5a5648', '#1d4ed8', '#fffdf4', '#f2ead8',
   "rgba(255,253,244,.97)","#1d4ed8","#1b1b1b","#10243f","#f6f1e3","#f5c542","#f5c542","#10243f",'rgba(255,253,244,.93)',1,0,2,'#5a5648',0,'#fffdf4'),
 'pixel': mk(20, 'pixel-art de 8 bits morado con estrellas, pasto y bloques amarillo, menta y rosa', BG_PIXEL, ["#ffe14d","#5ef2a0","#ff6bd6","#7ad7ff"], '#ffffff', '#b9a8e8', '#ffe14d', '#2a1a55', '#1b1038',
   "rgba(27,16,56,.97)","#ffe14d","#ffffff","#1b1038","#ffffff","#ffe14d","#ffe14d","#1b1038",'rgba(27,16,56,.90)',0,2,1,'#b9a8e8',1,'#1b1038'),
 'timeline': mk(21, 'línea de tiempo verde bosque con eje menta e hitos dorados', BG_TIMELINE, ["#f6c453","#6ee7b7","#fb7185","#ffffff"], '#ffffff', '#8cc9b2', '#f6c453', '#06231c', '#06231c',
   "rgba(6,35,28,.97)","#f6c453","#ffffff","#06231c","#ffffff","#f6c453","#f6c453","#06231c",'rgba(6,35,28,.88)',0,1,2,'#8cc9b2',0,'#06231c'),
 'noticiero': mk(22, 'noticiero azul noche con cinta amarilla de última hora y sello rojo', BG_NOTICIERO, ["#ffd400","#ff4d4d","#5ec8ff","#ffffff"], '#ffffff', '#9db4d9', '#ffd400', '#0a1a3a', '#050d1f',
   "rgba(5,13,31,.97)","#ffd400","#ffffff","#050d1f","#ffffff","#ffd400","#ffd400","#050d1f",'rgba(5,13,31,.88)',0,1,2,'#9db4d9',0,'#050d1f'),
 'mapa': mk(23, 'mapa de puntos azul marino con rutas doradas y acentos turquesa', BG_MAPA, ["#ffb703","#06d6a0","#4cc9f0","#ffffff"], '#ffffff', '#8fb3cc', '#ffb703', '#0b1d2e', '#0b1d2e',
   "rgba(11,29,46,.97)","#ffb703","#ffffff","#0b1d2e","#ffffff","#ffb703","#ffb703","#0b1d2e",'rgba(11,29,46,.88)',0,1,2,'#8fb3cc',1,'#0b1d2e'),
 'split': mk(24, 'pantalla dividida azul y granate con barras verdes y rosadas', BG_SPLIT, ["#ffd166","#06d6a0","#ef476f","#ffffff"], '#ffffff', '#b8b4cc', '#ffd166', '#0c0e1e', '#0c0e1e',
   "rgba(12,14,30,.97)","#ffd166","#ffffff","#0c0e1e","#ffffff","#ffd166","#ffd166","#0c0e1e",'rgba(12,14,30,.88)',0,1,2,'#b8b4cc',0,'#0c0e1e'),
})

R = []
exec(open(os.path.join(HERE, 'content_18nov.py'), encoding='utf-8').read())

if __name__ == '__main__':
    sel = [int(x) for x in sys.argv[1:]]
    for r in R:
        if sel and r['n'] not in sel: continue
        open(os.path.join(HERE, r['page'] + '.html'), 'w').write(g.build(r))
        print('ok', r['page'], r['scene'])
