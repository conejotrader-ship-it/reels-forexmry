#!/usr/bin/env python3
"""Genera las páginas v270–v276 (reels del 23 nov 2026). Estilos 3,4,7,5,9,6,8 (nuevas paletas, 6.º uso).
Uso: python3 gen_pages_23nov.py [n1 n2 ...]"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import gen_pages_16nov as g
from gen_pages_19nov import mk

BG_NEON = """ST.bg=t=>{const g2=ctx.createLinearGradient(0,0,0,H);g2.addColorStop(0,'#05061a');g2.addColorStop(.6,'#120a3a');g2.addColorStop(1,'#1d0a4a');ctx.fillStyle=g2;ctx.fillRect(0,0,W,H);
  ctx.fillStyle='#b6ff3c';ctx.shadowColor='#b6ff3c';ctx.shadowBlur=40;ctx.beginPath();ctx.arc(540,1360,230,Math.PI,0);ctx.fill();ctx.shadowBlur=0;
  ctx.fillStyle='#120a3a';for(let i=0;i<6;i++)ctx.fillRect(300,1360-i*38-10,480,10+i*2);
  ctx.strokeStyle='rgba(168,85,247,.75)';ctx.lineWidth=3;const hz=1360,off=(t*90)%80;for(let i=0;i<14;i++){const y=hz+Math.pow((i*80+off)/1000,1.7)*620;ctx.beginPath();ctx.moveTo(0,y);ctx.lineTo(W,y);ctx.stroke()}
  for(let i=-10;i<=10;i++){ctx.beginPath();ctx.moveTo(540+i*40,hz);ctx.lineTo(540+i*260,H);ctx.stroke()}
  ctx.strokeStyle='#b6ff3c';ctx.lineWidth=5;ctx.shadowColor='#b6ff3c';ctx.shadowBlur=18;ctx.strokeRect(26,26,W-52,H-52);ctx.shadowBlur=0;
  ctx.fillStyle='#b6ff3c';ctx.font='800 28px Inter';ctx.textAlign='left';ctx.fillText('NEÓN · EVERGRANDE 2021',50,84);ctx.textAlign='center'};
ST.panel=(x,y,w,h,col)=>{ctx.save();ctx.fillStyle='rgba(8,6,32,.9)';RR(x,y,w,h,14);ctx.fill();ctx.shadowColor=col;ctx.shadowBlur=22;ctx.lineWidth=4;ctx.strokeStyle=col;RR(x,y,w,h,14);ctx.stroke();ctx.restore()};"""

BG_CHALK = """ST.bg=t=>{const g2=ctx.createLinearGradient(0,0,W,H);g2.addColorStop(0,'#26384a');g2.addColorStop(1,'#1a2733');ctx.fillStyle=g2;ctx.fillRect(0,0,W,H);
  const r=rng(3);ctx.save();ctx.globalAlpha=.06;ctx.fillStyle='#fff';for(let i=0;i<50;i++){ctx.beginPath();ctx.ellipse(r()*W,r()*H,50+r()*190,8+r()*24,r()*3,0,7);ctx.fill()}ctx.restore();
  ctx.fillStyle='#c9a46a';ctx.fillRect(0,0,W,30);ctx.fillRect(0,H-30,W,30);ctx.fillRect(0,0,30,H);ctx.fillRect(W-30,0,30,H);
  ctx.save();ctx.strokeStyle='rgba(255,255,255,.22)';ctx.lineWidth=3;ctx.setLineDash([10,16]);for(let y=200;y<1500;y+=140){ctx.beginPath();ctx.moveTo(60,y);ctx.lineTo(W-60,y);ctx.stroke()}ctx.restore();
  ctx.fillStyle='#fff3f0';ctx.fillRect(110,H-76,150,14);ctx.fillStyle='#ff8fab';ctx.fillRect(280,H-76,80,14);
  ctx.fillStyle='rgba(255,230,120,.95)';ctx.font='800 28px Inter';ctx.textAlign='left';ctx.fillText('PIZARRA · CHANDELIER EXIT',60,92);ctx.textAlign='center'};
ST.panel=(x,y,w,h,col)=>{ctx.save();ctx.fillStyle='rgba(18,30,42,.86)';RR(x,y,w,h,16);ctx.fill();ctx.setLineDash([16,10]);ctx.lineWidth=5;ctx.strokeStyle=col;RR(x,y,w,h,16);ctx.stroke();ctx.restore()};"""

BG_DASH = """ST.bg=t=>{ctx.fillStyle='#eef2f7';ctx.fillRect(0,0,W,H);
  ctx.fillStyle='#14213d';ctx.fillRect(0,0,W,120);ctx.fillStyle='#fca311';ctx.font='800 30px Inter';ctx.textAlign='left';ctx.fillText('PANEL · FONDOS DE COBERTURA (LCH)',50,74);
  for(let i=0;i<3;i++){ctx.fillStyle=['#fca311','#2ec4b6','#e63946'][i];ctx.beginPath();ctx.arc(W-150+i*44,60,12,0,7);ctx.fill()}
  ctx.fillStyle='rgba(20,33,61,.07)';for(let i=0;i<6;i++){const x=40+(i%2)*520,y=1380+Math.floor(i/2)*150+Math.sin(t*.6+i)*6;RR(x,y,480,120,18);ctx.fill()}
  ctx.strokeStyle='#14213d';ctx.lineWidth=6;ctx.strokeRect(30,30,W-60,H-60);ctx.textAlign='center'};
ST.panel=(x,y,w,h,col)=>{ctx.save();ctx.fillStyle='rgba(255,255,255,.97)';RR(x,y,w,h,22);ctx.fill();ctx.lineWidth=4;ctx.strokeStyle='#14213d';RR(x,y,w,h,22);ctx.stroke();ctx.fillStyle=col;RR(x,y,16,h,8);ctx.fill();ctx.restore()};"""

BG_MT5 = """ST.bg=t=>{ctx.fillStyle='#ffffff';ctx.fillRect(0,0,W,H);
  ctx.strokeStyle='#e3e8ee';ctx.lineWidth=2;for(let y=140;y<H;y+=120){ctx.beginPath();ctx.moveTo(0,y);ctx.lineTo(W,y);ctx.stroke()}for(let x=0;x<W;x+=120){ctx.beginPath();ctx.moveTo(x,140);ctx.lineTo(x,H);ctx.stroke()}
  const r=rng(9);for(let i=0;i<20;i++){const x=40+i*52,o=1500-(i*37)%420+Math.sin(t*.7+i)*20,hh=40+r()*110,up=r()>.5;ctx.strokeStyle=up?'rgba(34,120,200,.35)':'rgba(220,90,30,.35)';ctx.lineWidth=4;ctx.beginPath();ctx.moveTo(x,o-hh);ctx.lineTo(x,o+hh);ctx.stroke();ctx.fillStyle=up?'rgba(34,120,200,.3)':'rgba(220,90,30,.3)';ctx.fillRect(x-13,o-hh*.5,26,hh)}
  ctx.fillStyle='#2b3a55';ctx.fillRect(0,0,W,110);ctx.fillStyle='#fff';ctx.font='800 28px Inter';ctx.textAlign='left';ctx.fillText('MetaTrader 5 · Editor · EA_Securus.mq5',40,68);ctx.fillStyle='#ffb703';ctx.fillRect(W-130,48,80,16);
  ctx.strokeStyle='#2b3a55';ctx.lineWidth=5;ctx.strokeRect(26,26,W-52,H-52);ctx.textAlign='center'};
ST.panel=(x,y,w,h,col)=>{ctx.save();ctx.fillStyle='rgba(255,255,255,.97)';ctx.fillRect(x,y,w,h);ctx.lineWidth=3;ctx.strokeStyle='#2b3a55';ctx.strokeRect(x,y,w,h);ctx.fillStyle=col;ctx.fillRect(x,y,w,10);ctx.restore()};"""

BG_BILL = """ST.bg=t=>{ctx.fillStyle='#d8e8cf';ctx.fillRect(0,0,W,H);
  ctx.strokeStyle='rgba(30,90,60,.16)';ctx.lineWidth=2;for(let k=0;k<26;k++){ctx.beginPath();for(let x=0;x<=W;x+=18){const y=100+k*72+Math.sin(x*.012+k*.5+t*.4)*28;x?ctx.lineTo(x,y):ctx.moveTo(x,y)}ctx.stroke()}
  ctx.strokeStyle='rgba(180,140,40,.35)';ctx.lineWidth=3;for(let k=0;k<5;k++){ctx.beginPath();ctx.ellipse(540,1530,160+k*55,100+k*38,0,0,7);ctx.stroke()}
  ctx.strokeStyle='#1e5a3c';ctx.lineWidth=10;ctx.strokeRect(34,34,W-68,H-68);ctx.lineWidth=3;ctx.strokeRect(58,58,W-116,H-116);
  ctx.fillStyle='#1e5a3c';ctx.font='800 28px Inter';ctx.textAlign='left';ctx.fillText('BILLETE · ARBITRAJE TRIANGULAR',84,112);ctx.textAlign='center'};
ST.panel=(x,y,w,h,col)=>{ctx.save();ctx.fillStyle='rgba(250,252,244,.96)';RR(x,y,w,h,10);ctx.fill();ctx.lineWidth=4;ctx.strokeStyle='#1e5a3c';RR(x,y,w,h,10);ctx.stroke();ctx.lineWidth=2;ctx.strokeStyle=col;RR(x+8,y+8,w-16,h-16,6);ctx.stroke();ctx.restore()};"""

BG_COMIC = """ST.bg=t=>{ctx.fillStyle='#ffe8b0';ctx.fillRect(0,0,W,H);
  ctx.fillStyle='rgba(230,57,70,.22)';for(let y=0;y<H;y+=44)for(let x=((y/44)%2)*22;x<W;x+=44){ctx.beginPath();ctx.arc(x,y,9+4*Math.sin((x+y)*.01+t),0,7);ctx.fill()}
  ctx.fillStyle='#e63946';ctx.beginPath();ctx.moveTo(0,0);ctx.lineTo(W,0);ctx.lineTo(W,96);ctx.lineTo(0,122);ctx.fill();
  ctx.fillStyle='#fff';ctx.font='900 34px Inter';ctx.textAlign='left';ctx.fillText('¡CÓMIC! · PETER LYNCH',50,92);
  ctx.strokeStyle='#111';ctx.lineWidth=10;ctx.strokeRect(30,30,W-60,H-60);ctx.textAlign='center'};
ST.panel=(x,y,w,h,col)=>{ctx.save();ctx.fillStyle='#111';RR(x+8,y+8,w,h,12);ctx.fill();ctx.fillStyle='#fff';RR(x,y,w,h,12);ctx.fill();ctx.lineWidth=5;ctx.strokeStyle='#111';RR(x,y,w,h,12);ctx.stroke();ctx.fillStyle=col;ctx.fillRect(x+10,y+h-18,w-20,8);ctx.restore()};"""

BG_LINE = """ST.bg=t=>{const g2=ctx.createLinearGradient(0,0,0,H);g2.addColorStop(0,'#0f1020');g2.addColorStop(1,'#1c1030');ctx.fillStyle=g2;ctx.fillRect(0,0,W,H);
  ctx.strokeStyle='rgba(255,255,255,.06)';ctx.lineWidth=2;for(let y=160;y<H;y+=130){ctx.beginPath();ctx.moveTo(0,y);ctx.lineTo(W,y);ctx.stroke()}
  const k=Math.min(1,(t%8)/4);ctx.beginPath();for(let i=0;i<=60*k;i++){const x=i*18,y=1420+(i<30?-i*6:-180+(i-30)*14)+Math.sin(i*.9)*10;i?ctx.lineTo(x,y):ctx.moveTo(x,y)}
  ctx.strokeStyle='#ff5d73';ctx.lineWidth=8;ctx.shadowColor='#ff5d73';ctx.shadowBlur=20;ctx.stroke();ctx.shadowBlur=0;
  const fl=ctx.createLinearGradient(0,1620,0,H);fl.addColorStop(0,'rgba(255,93,115,.35)');fl.addColorStop(1,'rgba(255,93,115,0)');ctx.fillStyle=fl;ctx.fillRect(0,1620,W,300);ctx.fillStyle='#ff5d73';ctx.fillRect(0,1616,W,6);
  ctx.strokeStyle='#ff5d73';ctx.lineWidth=5;ctx.strokeRect(26,26,W-52,H-52);ctx.fillStyle='#ff5d73';ctx.font='800 28px Inter';ctx.textAlign='left';ctx.fillText('LÍNEA · FLASH CRASH DEL YEN 2019',50,84);ctx.textAlign='center'};
ST.panel=(x,y,w,h,col)=>{ctx.save();ctx.fillStyle='rgba(15,16,32,.93)';RR(x,y,w,h,14);ctx.fill();ctx.lineWidth=4;ctx.strokeStyle=col;RR(x,y,w,h,14);ctx.stroke();ctx.restore()};"""

def dark(est, pal, bg, C, acc, pn, dk, mu='#9db4d0', txt='#eef6ff'):
    return mk(est, pal, bg, C, txt, mu, acc, pn, dk,
      "rgba(8,12,22,.96)", acc, txt, dk, txt, acc, acc, dk, 'rgba(6,10,20,.88)', 0,1,2, mu, 0, dk)
def light(est, pal, bg, C, txt, mu, acc, dk, paper):
    return mk(est, pal, bg, C, txt, mu, acc, '#fffaf0', paper, "rgba(255,252,243,.97)", acc, txt, txt, '#fffaf0', acc, acc, '#fffaf0', 'rgba(255,252,243,.93)', 0,1,2, mu, 0, '#fffaf0')

TH = {
 'neon': dark(3,'neón lima y violeta eléctrico sobre azul noche, sol lima con rejilla',BG_NEON,["#b6ff3c","#ff4fd8","#38e1ff","#ffffff"],'#b6ff3c','#05061a','#05061a','#b8a9e8'),
 'tiza': dark(4,'pizarra azul pizarra con tiza rosa, amarilla, menta y blanca',BG_CHALK,["#ff8fab","#ffe066","#7ee8c7","#fff3f0"],'#ffe066','#1a2733','#1a2733','#b4c4d4','#fff3f0'),
 'dash': light(7,'panel claro azul marino con tarjetas ámbar, turquesa y rojo',BG_DASH,["#e08a00","#14a89a","#d62839","#14213d"],'#14213d','#52607a','#e08a00','#14213d','#eef2f7'),
 'mt5': light(5,'editor MT5 claro con velas azul y naranja tenues',BG_MT5,["#1f6fc4","#d9531e","#2a9d6f","#2b3a55"],'#2b3a55','#5b6b84','#1f6fc4','#2b3a55','#ffffff'),
 'billete': light(9,'billete verde dólar con guilloche, marco verde y óvalo dorado',BG_BILL,["#1e5a3c","#b8860b","#8a2b2b","#1e5a3c"],'#1c3a2a','#4f6b5a','#b8860b','#1e5a3c','#d8e8cf'),
 'comic': light(6,'cómic crema con tramado rojo, paneles blancos y tinta negra',BG_COMIC,["#e63946","#1d3557","#d98100","#111111"],'#111111','#5a4a3a','#e63946','#e63946','#ffe8b0'),
 'linea': dark(8,'noche violeta con línea coral que cae y suelo degradado',BG_LINE,["#ff5d73","#ffd166","#5ad1ff","#ffffff"],'#ff5d73','#0f1020','#0f1020','#b0a8d0'),
}
for k,v in TH.items(): v['uso'] = '6.º'
g.THEMES.update(TH)

R = []
exec(open(os.path.join(HERE, 'content_23nov.py'), encoding='utf-8').read())

if __name__ == '__main__':
    sel = [int(x) for x in sys.argv[1:]]
    for r in R:
        if sel and r['n'] not in sel: continue
        open(os.path.join(HERE, r['page'] + '.html'), 'w').write(g.build(r))
        print('ok', r['page'], r['scene'])
