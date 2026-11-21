#!/usr/bin/env python3
"""Genera las páginas v256–v262 (reels del 21 nov 2026). Estilos 39–45 (nuevas paletas).
Uso: python3 gen_pages_21nov.py [n1 n2 ...]"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import gen_pages_16nov as g
from gen_pages_19nov import mk

def lbl(txt, col, x=60, y=84, al='left'):
    return f"ctx.fillStyle='{col}';ctx.font='800 28px Inter';ctx.textAlign='{al}';ctx.fillText('{txt}',{x},{y});ctx.textAlign='center'"

BG_HOLO = """ST.bg=t=>{const g2=ctx.createLinearGradient(0,0,0,H);g2.addColorStop(0,'#04122b');g2.addColorStop(1,'#0a2a55');ctx.fillStyle=g2;ctx.fillRect(0,0,W,H);
  ctx.strokeStyle='rgba(80,220,255,.14)';ctx.lineWidth=2;for(let y=120;y<H;y+=60){ctx.beginPath();ctx.moveTo(0,y);ctx.lineTo(W,y);ctx.stroke()}for(let x=0;x<W;x+=90){ctx.beginPath();ctx.moveTo(x,120);ctx.lineTo(x,H);ctx.stroke()}
  const sy=((t*200)%1700)+100;const gr=ctx.createLinearGradient(0,sy-60,0,sy+60);gr.addColorStop(0,'rgba(80,220,255,0)');gr.addColorStop(.5,'rgba(80,220,255,.22)');gr.addColorStop(1,'rgba(80,220,255,0)');ctx.fillStyle=gr;ctx.fillRect(0,sy-60,W,120);
  ctx.save();ctx.translate(540,1620);ctx.strokeStyle='rgba(80,220,255,.35)';ctx.lineWidth=4;for(let k=1;k<4;k++){ctx.beginPath();ctx.ellipse(0,0,k*120,k*40,0,0,7);ctx.stroke()}ctx.rotate(t*.6);ctx.beginPath();ctx.moveTo(0,0);ctx.lineTo(360,0);ctx.stroke();ctx.restore();
  ctx.strokeStyle='rgba(80,220,255,.6)';ctx.lineWidth=4;ctx.strokeRect(26,26,W-52,H-52);ctx.fillStyle='rgba(80,220,255,.9)';ctx.font='800 28px Inter';ctx.textAlign='left';ctx.fillText('HOLOGRAMA · GESTORES DE ACTIVOS',50,80);ctx.textAlign='center'};
ST.panel=(x,y,w,h,col)=>{ctx.save();ctx.fillStyle='rgba(6,26,56,.9)';RR(x,y,w,h,16);ctx.fill();ctx.lineWidth=4;ctx.strokeStyle=col;ctx.shadowColor=col;ctx.shadowBlur=18;RR(x,y,w,h,16);ctx.stroke();ctx.restore()};"""

BG_GLITCH = """ST.bg=t=>{ctx.fillStyle='#07060d';ctx.fillRect(0,0,W,H);const r=rng(21);
  for(let i=0;i<9;i++){const y=(r()*H+t*(60+i*20))%H,h=6+r()*30,dx=(Math.sin(t*9+i*3)*26);ctx.fillStyle=['rgba(255,0,153,.14)','rgba(0,240,255,.14)'][i%2];ctx.fillRect(dx,y,W,h)}
  ctx.strokeStyle='rgba(0,240,255,.10)';ctx.lineWidth=2;for(let x=0;x<W;x+=120){ctx.beginPath();ctx.moveTo(x,120);ctx.lineTo(x,H);ctx.stroke()}
  const j=Math.sin(t*14)>.92?14:0;ctx.strokeStyle='#ff0099';ctx.lineWidth=5;ctx.strokeRect(28+j,28,W-56,H-56);ctx.strokeStyle='#00f0ff';ctx.lineWidth=3;ctx.strokeRect(30-j,30,W-60,H-60);
  ctx.fillStyle='#00f0ff';ctx.font='800 28px Inter';ctx.textAlign='left';ctx.fillText('//SYS.MQL5 > COPYBUFFER_',60,86);ctx.textAlign='center'};
ST.panel=(x,y,w,h,col)=>{ctx.save();ctx.fillStyle='rgba(7,6,13,.94)';ctx.fillRect(x,y,w,h);ctx.fillStyle='#ff0099';ctx.globalAlpha=.5;ctx.fillRect(x-6,y+4,w,h);ctx.globalAlpha=1;ctx.fillStyle='rgba(7,6,13,.96)';ctx.fillRect(x,y,w,h);ctx.lineWidth=4;ctx.strokeStyle=col;ctx.strokeRect(x,y,w,h);ctx.restore()};"""

BG_XRAY = """ST.bg=t=>{ctx.fillStyle='#04070c';ctx.fillRect(0,0,W,H);
  const gr=ctx.createRadialGradient(540,1000,100,540,1000,1100);gr.addColorStop(0,'rgba(190,230,255,.20)');gr.addColorStop(1,'rgba(4,7,12,0)');ctx.fillStyle=gr;ctx.fillRect(0,0,W,H);
  ctx.strokeStyle='rgba(200,235,255,.16)';ctx.lineWidth=3;ctx.save();ctx.translate(540,1560);for(let i=0;i<9;i++){ctx.beginPath();ctx.moveTo(-300+i*8,-200-i*10);ctx.bezierCurveTo(-120,-300-i*12,120,-100,300-i*8,-220);ctx.stroke()}for(let k=0;k<14;k++){ctx.beginPath();ctx.moveTo(-290+k*42,-60);ctx.lineTo(-290+k*42,90);ctx.stroke()}ctx.restore();
  const sy=((t*180)%1600)+140;ctx.fillStyle='rgba(120,255,200,.35)';ctx.fillRect(40,sy,W-80,6);const g3=ctx.createLinearGradient(0,sy-100,0,sy);g3.addColorStop(0,'rgba(120,255,200,0)');g3.addColorStop(1,'rgba(120,255,200,.12)');ctx.fillStyle=g3;ctx.fillRect(40,sy-100,W-80,100);
  ctx.strokeStyle='rgba(200,235,255,.5)';ctx.lineWidth=4;ctx.strokeRect(26,26,W-52,H-52);ctx.fillStyle='rgba(200,235,255,.9)';ctx.font='800 28px Inter';ctx.textAlign='left';ctx.fillText('RAYOS X · POR DENTRO DE UN ETF DE ORO',50,80);ctx.textAlign='center'};
ST.panel=(x,y,w,h,col)=>{ctx.save();ctx.fillStyle='rgba(8,16,26,.9)';RR(x,y,w,h,10);ctx.fill();ctx.lineWidth=4;ctx.strokeStyle=col;RR(x,y,w,h,10);ctx.stroke();ctx.fillStyle=col;ctx.globalAlpha=.18;ctx.fillRect(x+10,y+10,w-20,h-20);ctx.restore()};"""

BG_DOM = """ST.bg=t=>{ctx.fillStyle='#f3ead9';ctx.fillRect(0,0,W,H);ctx.fillStyle='#e6d8bd';ctx.fillRect(0,1560,W,360);
  const n=12;for(let i=0;i<n;i++){const fall=Math.max(0,Math.min(1,(t*.5-i*.35)%5));const ang=Math.min(1,fall*2)*1.2;ctx.save();ctx.translate(80+i*84,1700);ctx.rotate(ang*(i%2?1:1));ctx.fillStyle=['#d1495b','#2a6f97','#edae49'][i%3];ctx.globalAlpha=.8;ctx.fillRect(-18,-130,36,130);ctx.fillStyle='#fff';for(let d=0;d<3;d++){ctx.beginPath();ctx.arc(0,-100+d*30,5,0,7);ctx.fill()}ctx.restore()}
  ctx.strokeStyle='#1f1a2e';ctx.lineWidth=6;ctx.strokeRect(30,30,W-60,H-60);ctx.fillStyle='#1f1a2e';ctx.font='800 28px Inter';ctx.textAlign='left';ctx.fillText('DOMINÓ EN CADENA · FTX 2022',60,86);ctx.textAlign='center'};
ST.panel=(x,y,w,h,col)=>{ctx.save();ctx.fillStyle='#000';ctx.globalAlpha=.18;ctx.fillRect(x+8,y+8,w,h);ctx.globalAlpha=1;ctx.fillStyle='#fffaf0';ctx.fillRect(x,y,w,h);ctx.lineWidth=5;ctx.strokeStyle='#1f1a2e';ctx.strokeRect(x,y,w,h);ctx.fillStyle=col;ctx.fillRect(x,y,16,h);ctx.restore()};"""

BG_COASTER = """ST.bg=t=>{const g2=ctx.createLinearGradient(0,0,0,H);g2.addColorStop(0,'#2b1055');g2.addColorStop(1,'#d9487d');ctx.fillStyle=g2;ctx.fillRect(0,0,W,H);
  ctx.strokeStyle='#ffd23f';ctx.lineWidth=14;ctx.beginPath();for(let x=-20;x<=W+20;x+=20){const y=1640-Math.sin(x*.012+t*.8)*120-Math.sin(x*.031)*50;x<=-20?ctx.moveTo(x,y):ctx.lineTo(x,y)}ctx.stroke();
  ctx.lineWidth=5;for(let x=0;x<=W;x+=60){const y=1640-Math.sin(x*.012+t*.8)*120-Math.sin(x*.031)*50;ctx.beginPath();ctx.moveTo(x,y+7);ctx.lineTo(x-10,y+150);ctx.stroke()}
  const cx=((t*220)%1200)-60;const cy=1640-Math.sin(cx*.012+t*.8)*120-Math.sin(cx*.031)*50;ctx.fillStyle='#fff';ctx.fillRect(cx-34,cy-44,68,34);ctx.fillStyle='#2b1055';ctx.beginPath();ctx.arc(cx-16,cy-8,9,0,7);ctx.arc(cx+16,cy-8,9,0,7);ctx.fill();
  ctx.strokeStyle='#ffd23f';ctx.lineWidth=5;ctx.strokeRect(26,26,W-52,H-52);ctx.fillStyle='#ffd23f';ctx.font='800 28px Inter';ctx.textAlign='left';ctx.fillText('MONTAÑA RUSA · ONDAS DE ELLIOTT',50,80);ctx.textAlign='center'};
ST.panel=(x,y,w,h,col)=>{ctx.save();ctx.fillStyle='rgba(43,16,85,.92)';RR(x,y,w,h,26);ctx.fill();ctx.lineWidth=5;ctx.strokeStyle=col;RR(x,y,w,h,26);ctx.stroke();ctx.restore()};"""

BG_CHESS = """ST.bg=t=>{ctx.fillStyle='#efe6d2';ctx.fillRect(0,0,W,H);const s=90;for(let y=0;y<H/s;y++)for(let x=0;x<W/s+1;x++){if((x+y)%2){ctx.fillStyle='rgba(60,90,70,.16)';ctx.fillRect(x*s,y*s,s,s)}}
  ctx.save();ctx.translate(900,1680);ctx.fillStyle='#1d3a2c';ctx.globalAlpha=.55;ctx.beginPath();ctx.arc(0,-150+Math.sin(t*1.5)*6,34,0,7);ctx.fill();ctx.beginPath();ctx.moveTo(-40,0);ctx.lineTo(-24,-120);ctx.lineTo(24,-120);ctx.lineTo(40,0);ctx.closePath();ctx.fill();ctx.fillRect(-50,0,100,18);ctx.restore();
  ctx.strokeStyle='#1d3a2c';ctx.lineWidth=8;ctx.strokeRect(30,30,W-60,H-60);ctx.fillStyle='#1d3a2c';ctx.font='800 28px Inter';ctx.textAlign='left';ctx.fillText('AJEDREZ · LA JUGADA DE BURRY',60,86);ctx.textAlign='center'};
ST.panel=(x,y,w,h,col)=>{ctx.save();ctx.fillStyle='rgba(255,252,243,.97)';ctx.fillRect(x,y,w,h);ctx.lineWidth=5;ctx.strokeStyle='#1d3a2c';ctx.strokeRect(x,y,w,h);ctx.fillStyle=col;ctx.fillRect(x,y+h-12,w,12);ctx.restore()};"""

BG_BOOK = """ST.bg=t=>{ctx.fillStyle='#e9dcc0';ctx.fillRect(0,0,W,H);ctx.fillStyle='#d8c7a2';ctx.fillRect(W/2-3,0,6,H);
  ctx.strokeStyle='rgba(90,60,30,.16)';ctx.lineWidth=2;for(let y=180;y<1500;y+=54){ctx.beginPath();ctx.moveTo(70,y);ctx.lineTo(500,y);ctx.moveTo(580,y);ctx.lineTo(1010,y);ctx.stroke()}
  const k=(t*.35)%1;ctx.save();ctx.translate(540,1700);ctx.fillStyle='rgba(120,80,40,.22)';ctx.beginPath();ctx.moveTo(0,0);ctx.quadraticCurveTo(250*(1-k),-60-110*Math.sin(k*3.1),460*(1-k)+10,-30);ctx.lineTo(460*(1-k)+10,100);ctx.lineTo(0,100);ctx.fill();ctx.restore();
  ctx.strokeStyle='#5a3a1e';ctx.lineWidth=8;ctx.strokeRect(30,30,W-60,H-60);ctx.fillStyle='#5a3a1e';ctx.font='800 28px Inter';ctx.textAlign='left';ctx.fillText('ENCICLOPEDIA · RECORTE DE AGOSTO 2011',60,86);ctx.textAlign='center'};
ST.panel=(x,y,w,h,col)=>{ctx.save();ctx.fillStyle='rgba(250,243,226,.98)';ctx.fillRect(x,y,w,h);ctx.lineWidth=4;ctx.strokeStyle='#5a3a1e';ctx.strokeRect(x,y,w,h);ctx.fillStyle=col;ctx.fillRect(x,y,w,10);ctx.restore()};"""

def dark(est, pal, bg, C, acc, pn, dk, mu='#9db4d0', txt='#eef6ff', ov=None):
    return mk(est, pal, bg, C, txt, mu, acc, pn, dk,
      f"rgba(8,12,22,.96)", acc, txt, dk, txt, acc, acc, dk, ov or 'rgba(6,10,20,.88)', 0,1,2, mu, 0, dk)
def light(est, pal, bg, C, txt, mu, acc, dk, paper):
    return mk(est, pal, bg, C, txt, mu, acc, '#fffaf0', paper, "rgba(255,252,243,.97)", acc, txt, txt, '#fffaf0', acc, acc, '#fffaf0', 'rgba(255,252,243,.93)', 0,1,2, mu, 0, '#fffaf0')

TH = {
 'holo': dark(39,'holograma azul marino con cian eléctrico, lima y blanco',BG_HOLO,["#4cf0ff","#b6ff3b","#ff9ef5","#ffffff"],'#4cf0ff','#061a38','#04122b','#8fb7d8'),
 'glitch': dark(40,'glitch cyberpunk negro con magenta y cian',BG_GLITCH,["#00f0ff","#ff0099","#f7ff00","#ffffff"],'#00f0ff','#07060d','#07060d','#a79bc9'),
 'rayosx': dark(41,'escáner de rayos X negro azulado con blanco hueso y verde menta',BG_XRAY,["#c9ecff","#78ffc8","#ffd27a","#ffffff"],'#78ffc8','#08101a','#04070c','#8aa6bb'),
 'domino': light(42,'dominó en cadena sobre crema con rojo, azul y ocre',BG_DOM,["#d1495b","#2a6f97","#c98a10","#1f1a2e"],'#1f1a2e','#5e5668','#d1495b','#1f1a2e','#f3ead9'),
 'coaster': dark(43,'montaña rusa violeta a rosa con riel amarillo',BG_COASTER,["#ffd23f","#7df9ff","#ffffff","#ff9ec7"],'#ffd23f','#2b1055','#2b1055','#d7bfe8'),
 'chess': light(44,'tablero de ajedrez crema con verde bosque, rojo y oro',BG_CHESS,["#1d6b4a","#b3261e","#b8860b","#1d3a2c"],'#1d3a2c','#5b6b60','#b3261e','#1d3a2c','#efe6d2'),
 'book': light(45,'enciclopedia antigua en papel sepia con tinta marrón, azul y granate',BG_BOOK,["#8b1e3f","#1f5f8b","#b8860b","#5a3a1e"],'#3b2614','#7a6548','#8b1e3f','#5a3a1e','#e9dcc0'),
}
for k,v in TH.items(): v['uso'] = '5.º'
g.THEMES.update(TH)

R = []
exec(open(os.path.join(HERE, 'content_21nov.py'), encoding='utf-8').read())

if __name__ == '__main__':
    sel = [int(x) for x in sys.argv[1:]]
    for r in R:
        if sel and r['n'] not in sel: continue
        open(os.path.join(HERE, r['page'] + '.html'), 'w').write(g.build(r))
        print('ok', r['page'], r['scene'])
