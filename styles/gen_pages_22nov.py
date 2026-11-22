#!/usr/bin/env python3
"""Genera las páginas v263–v269 (reels del 22 nov 2026). Estilos 46,47,48,50,49 (5.º uso) y 1,2 (6.º uso), nuevas paletas.
Uso: python3 gen_pages_22nov.py [n1 n2 ...]"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import gen_pages_16nov as g
from gen_pages_19nov import mk

BG_VHS = """ST.bg=t=>{const g2=ctx.createLinearGradient(0,0,0,H);g2.addColorStop(0,'#160a2e');g2.addColorStop(1,'#2a0f3f');ctx.fillStyle=g2;ctx.fillRect(0,0,W,H);
  ctx.fillStyle='rgba(0,0,0,.22)';for(let y=0;y<H;y+=6)ctx.fillRect(0,y,W,2);
  const by=((t*160)%2100)-150;ctx.fillStyle='rgba(255,255,255,.07)';ctx.fillRect(0,by,W,90);ctx.fillStyle='rgba(255,60,160,.12)';ctx.fillRect(0,by+90,W,14);
  ctx.fillStyle='rgba(0,229,255,.9)';ctx.font='800 28px Inter';ctx.textAlign='left';ctx.fillText('▶ PLAY  ·  REPLAY SNB 2011',50,84);ctx.fillStyle='rgba(255,60,160,.95)';ctx.textAlign='right';ctx.fillText('SP  '+(Math.floor(t)%2?'●':'○')+' REC',W-50,84);ctx.textAlign='center';
  ctx.strokeStyle='rgba(0,229,255,.55)';ctx.lineWidth=4;ctx.strokeRect(26,26,W-52,H-52);
  const g3=ctx.createRadialGradient(540,960,500,540,960,1300);g3.addColorStop(0,'rgba(0,0,0,0)');g3.addColorStop(1,'rgba(0,0,0,.45)');ctx.fillStyle=g3;ctx.fillRect(0,0,W,H)};
ST.panel=(x,y,w,h,col)=>{ctx.save();ctx.fillStyle='rgba(22,10,46,.92)';RR(x,y,w,h,14);ctx.fill();ctx.fillStyle='rgba(255,60,160,.5)';ctx.fillRect(x-5,y+3,w,h);ctx.fillStyle='rgba(22,10,46,.96)';RR(x,y,w,h,14);ctx.fill();ctx.lineWidth=4;ctx.strokeStyle=col;RR(x,y,w,h,14);ctx.stroke();ctx.restore()};"""

BG_HEAT = """ST.bg=t=>{ctx.fillStyle='#10121c';ctx.fillRect(0,0,W,H);const s=72;
  for(let y=1;y<H/s;y++)for(let x=0;x<W/s+1;x++){const v=(Math.sin(x*.7+t*.9)+Math.cos(y*.5-t*.7)+Math.sin((x+y)*.35+t*.5))/3;const k=(v+1)/2;ctx.fillStyle=`hsla(${Math.round(200-k*190)},85%,55%,${.10+k*.16})`;ctx.fillRect(x*s,y*s,s-4,s-4)}
  ctx.strokeStyle='#ff9f1c';ctx.lineWidth=5;ctx.strokeRect(26,26,W-52,H-52);ctx.fillStyle='#ff9f1c';ctx.font='800 28px Inter';ctx.textAlign='left';ctx.fillText('MAPA DE CALOR · MFI 0–100',50,84);
  const gr=ctx.createLinearGradient(640,70,1030,70);gr.addColorStop(0,'hsl(200,85%,55%)');gr.addColorStop(.5,'hsl(100,85%,55%)');gr.addColorStop(1,'hsl(10,85%,55%)');ctx.fillStyle=gr;ctx.fillRect(700,62,320,20);ctx.textAlign='center'};
ST.panel=(x,y,w,h,col)=>{ctx.save();ctx.fillStyle='rgba(16,18,28,.93)';RR(x,y,w,h,12);ctx.fill();ctx.lineWidth=4;ctx.strokeStyle=col;RR(x,y,w,h,12);ctx.stroke();ctx.restore()};"""

BG_BUB = """ST.bg=t=>{const g2=ctx.createLinearGradient(0,0,0,H);g2.addColorStop(0,'#e8f4ff');g2.addColorStop(1,'#d3ecff');ctx.fillStyle=g2;ctx.fillRect(0,0,W,H);const r=rng(5);
  for(let i=0;i<26;i++){const R=30+r()*110,bx=r()*W,by=r()*H,ph=r()*6;const x=bx+Math.sin(t*.6+ph)*40,y=((by-t*(30+R*.3))%(H+300)+H+300)%(H+300)-150,rr=R*(1+.06*Math.sin(t*1.4+ph));
    ctx.fillStyle=['rgba(32,120,220,.12)','rgba(255,120,60,.12)','rgba(40,180,140,.13)'][i%3];ctx.beginPath();ctx.arc(x,y,rr,0,7);ctx.fill();ctx.strokeStyle='rgba(255,255,255,.7)';ctx.lineWidth=3;ctx.beginPath();ctx.arc(x-rr*.25,y-rr*.25,rr*.55,3.5,4.6);ctx.stroke()}
  ctx.strokeStyle='#0b3d73';ctx.lineWidth=6;ctx.strokeRect(30,30,W-60,H-60);ctx.fillStyle='#0b3d73';ctx.font='800 28px Inter';ctx.textAlign='left';ctx.fillText('BURBUJAS · MAYORES BANCOS 2025',60,86);ctx.textAlign='center'};
ST.panel=(x,y,w,h,col)=>{ctx.save();ctx.fillStyle='rgba(255,255,255,.95)';RR(x,y,w,h,30);ctx.fill();ctx.lineWidth=5;ctx.strokeStyle=col;RR(x,y,w,h,30);ctx.stroke();ctx.restore()};"""

BG_WB = """ST.bg=t=>{ctx.fillStyle='#fbfaf4';ctx.fillRect(0,0,W,H);ctx.fillStyle='rgba(0,0,0,.05)';ctx.fillRect(0,0,W,120);
  ctx.strokeStyle='rgba(30,60,120,.10)';ctx.lineWidth=2;for(let y=180;y<1500;y+=90){ctx.beginPath();ctx.moveTo(40,y);ctx.lineTo(W-40,y);ctx.stroke()}
  ctx.save();ctx.translate(540,1640);ctx.strokeStyle='rgba(214,40,57,.35)';ctx.lineWidth=7;ctx.lineCap='round';ctx.beginPath();const k=Math.min(1,(t%6)/3);for(let i=0;i<=40*k;i++){const x=-420+i*21,y=-Math.abs(Math.sin(i*.4))*40;i?ctx.lineTo(x,y):ctx.moveTo(x,y)}ctx.stroke();ctx.restore();
  ctx.strokeStyle='#2b2b2b';ctx.lineWidth=8;ctx.strokeRect(30,30,W-60,H-60);ctx.fillStyle='#d62839';ctx.font='800 28px Inter';ctx.textAlign='left';ctx.fillText('PIZARRA · MQL5 · VOLUMEN DEL LOTE',60,86);ctx.textAlign='center'};
ST.panel=(x,y,w,h,col)=>{ctx.save();ctx.fillStyle='rgba(255,255,255,.98)';RR(x,y,w,h,10);ctx.fill();ctx.lineWidth=5;ctx.strokeStyle='#2b2b2b';RR(x,y,w,h,10);ctx.stroke();ctx.strokeStyle=col;ctx.lineWidth=8;ctx.beginPath();ctx.moveTo(x+14,y+h-14);ctx.lineTo(x+w-14,y+h-14);ctx.stroke();ctx.restore()};"""

BG_CAM = """ST.bg=t=>{const g2=ctx.createLinearGradient(0,0,0,H);g2.addColorStop(0,'#0b1d2a');g2.addColorStop(1,'#14394d');ctx.fillStyle=g2;ctx.fillRect(0,0,W,H);
  const off=(t*140)%200;ctx.strokeStyle='rgba(120,220,255,.12)';ctx.lineWidth=2;for(let y=-200+off;y<H;y+=200){ctx.beginPath();ctx.moveTo(0,y);ctx.lineTo(W,y);ctx.stroke()}for(let x=0;x<W;x+=180){ctx.beginPath();ctx.moveTo(x,0);ctx.lineTo(x,H);ctx.stroke()}
  ctx.strokeStyle='rgba(255,196,61,.28)';ctx.lineWidth=18;ctx.beginPath();for(let i=0;i<=24;i++){const x=-60+i*60,y=((i*263)%700)+300+((t*140)%0)-off*0;i?ctx.lineTo(x,(y+off*3)%1900):ctx.moveTo(x,y)}ctx.stroke();
  ctx.strokeStyle='#ffc43d';ctx.lineWidth=5;ctx.strokeRect(26,26,W-52,H-52);ctx.fillStyle='#ffc43d';ctx.font='800 28px Inter';ctx.textAlign='left';ctx.fillText('CÁMARA · DENTRO DEL MARGEN CME',50,84);ctx.textAlign='center'};
ST.panel=(x,y,w,h,col)=>{ctx.save();ctx.fillStyle='rgba(8,24,34,.92)';RR(x,y,w,h,16);ctx.fill();ctx.lineWidth=4;ctx.strokeStyle=col;RR(x,y,w,h,16);ctx.stroke();ctx.restore()};"""

BG_CAND = """ST.bg=t=>{ctx.fillStyle='#08191b';ctx.fillRect(0,0,W,H);const r=rng(11);
  for(let i=0;i<22;i++){const x=40+i*47,base=1500-(i*38)%500,hh=60+r()*160,up=r()>.45,ph=t*.8+i*.5;const o=base+Math.sin(ph)*30;ctx.strokeStyle=up?'rgba(255,170,60,.28)':'rgba(190,150,255,.28)';ctx.lineWidth=4;ctx.beginPath();ctx.moveTo(x,o-hh);ctx.lineTo(x,o+hh);ctx.stroke();ctx.fillStyle=up?'rgba(255,170,60,.22)':'rgba(190,150,255,.22)';ctx.fillRect(x-14,o-hh*.5,28,hh)}
  ctx.strokeStyle='#ffaa3c';ctx.lineWidth=5;ctx.strokeRect(26,26,W-52,H-52);ctx.fillStyle='#ffaa3c';ctx.font='800 28px Inter';ctx.textAlign='left';ctx.fillText('VELAS · JOHN TEMPLETON 1939',50,84);ctx.textAlign='center'};
ST.panel=(x,y,w,h,col)=>{ctx.save();ctx.fillStyle='rgba(8,25,27,.93)';RR(x,y,w,h,12);ctx.fill();ctx.lineWidth=4;ctx.strokeStyle=col;RR(x,y,w,h,12);ctx.stroke();ctx.restore()};"""

BG_INFO = """ST.bg=t=>{ctx.fillStyle='#fff3dc';ctx.fillRect(0,0,W,H);
  const cs=['#ff6b6b','#4ecdc4','#ffd166','#6c5ce7'];for(let i=0;i<8;i++){const x=(i%2)*560+Math.sin(t*.5+i)*14,y=1380+Math.floor(i/2)*130;ctx.fillStyle=cs[i%4];ctx.globalAlpha=.22;RR(x+30,y,470,100,22);ctx.fill();ctx.globalAlpha=1}
  ctx.fillStyle='#1d1d3b';ctx.fillRect(0,0,W,110);ctx.fillStyle='#ffd166';ctx.font='800 30px Inter';ctx.textAlign='left';ctx.fillText('INFOGRAFÍA · CHINA 2016',50,70);ctx.textAlign='center';
  ctx.strokeStyle='#1d1d3b';ctx.lineWidth=6;ctx.strokeRect(30,30,W-60,H-60)};
ST.panel=(x,y,w,h,col)=>{ctx.save();ctx.fillStyle='rgba(255,255,255,.97)';RR(x,y,w,h,24);ctx.fill();ctx.lineWidth=5;ctx.strokeStyle='#1d1d3b';RR(x,y,w,h,24);ctx.stroke();ctx.fillStyle=col;RR(x,y,18,h,10);ctx.fill();ctx.restore()};"""

def dark(est, pal, bg, C, acc, pn, dk, mu='#9db4d0', txt='#eef6ff', ov=None):
    return mk(est, pal, bg, C, txt, mu, acc, pn, dk,
      "rgba(8,12,22,.96)", acc, txt, dk, txt, acc, acc, dk, ov or 'rgba(6,10,20,.88)', 0,1,2, mu, 0, dk)
def light(est, pal, bg, C, txt, mu, acc, dk, paper):
    return mk(est, pal, bg, C, txt, mu, acc, '#fffaf0', paper, "rgba(255,252,243,.97)", acc, txt, txt, '#fffaf0', acc, acc, '#fffaf0', 'rgba(255,252,243,.93)', 0,1,2, mu, 0, '#fffaf0')

TH = {
 'vhs': dark(46,'televisión VHS ciruela con magenta y cian de cinta',BG_VHS,["#00e5ff","#ff3ca0","#ffe14d","#ffffff"],'#00e5ff','#160a2e','#160a2e','#c4a9e6'),
 'calor': dark(47,'mapa de calor azul-verde-rojo sobre grafito con naranja',BG_HEAT,["#ff9f1c","#5be37d","#4cc9f0","#ffffff"],'#ff9f1c','#10121c','#10121c','#9aa4c0'),
 'burbujas': light(48,'burbujas celestes con azul marino, naranja y verde',BG_BUB,["#0b5cad","#e8590c","#1f9d76","#0b3d73"],'#0b3d73','#4f6d8f','#e8590c','#0b3d73','#e8f4ff'),
 'pizarrab': light(50,'pizarra blanca con marcadores rojo, azul y verde',BG_WB,["#d62839","#1d5bd6","#18926a","#2b2b2b"],'#2b2b2b','#6b6b6b','#d62839','#2b2b2b','#fbfaf4'),
 'camara': dark(49,'cámara descendente azul petróleo con ámbar',BG_CAM,["#ffc43d","#6be4ff","#ff7a90","#ffffff"],'#ffc43d','#0b1d2a','#0b1d2a','#9cc3d4'),
 'velas': dark(1,'velas ámbar y lila sobre verde petróleo casi negro',BG_CAND,["#ffaa3c","#c3a0ff","#5be3c1","#ffffff"],'#ffaa3c','#08191b','#08191b','#9ac2c0'),
 'info': light(2,'infografía crema con tarjetas coral, turquesa, amarillo y violeta',BG_INFO,["#e0453f","#1aa39a","#6c5ce7","#1d1d3b"],'#1d1d3b','#5e5b7a','#e0453f','#1d1d3b','#fff3dc'),
}
for k,v in TH.items(): v['uso'] = '6.º' if v['est'] in (1,2) else '5.º'
g.THEMES.update(TH)

R = []
exec(open(os.path.join(HERE, 'content_22nov.py'), encoding='utf-8').read())

if __name__ == '__main__':
    sel = [int(x) for x in sys.argv[1:]]
    for r in R:
        if sel and r['n'] not in sel: continue
        open(os.path.join(HERE, r['page'] + '.html'), 'w').write(g.build(r))
        print('ok', r['page'], r['scene'])
