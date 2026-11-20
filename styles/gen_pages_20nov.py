#!/usr/bin/env python3
"""Genera las páginas v249–v255 (reels del 20 nov 2026). Estilos 32–38 (4.º uso, nuevas paletas).
Uso: python3 gen_pages_20nov.py [n1 n2 ...]"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import gen_pages_16nov as g
from gen_pages_19nov import mk

BG_PIX = """ST.bg=t=>{ctx.fillStyle='#1b1038';ctx.fillRect(0,0,W,H);const r=rng(5);for(let i=0;i<70;i++){ctx.fillStyle='rgba(255,246,224,'+(.15+.5*Math.abs(Math.sin(t*2+i)))+')';const s=i%5?6:12;ctx.fillRect(Math.floor(r()*W/12)*12,Math.floor(r()*1400/12)*12+90,s,s)}
  ctx.fillStyle='#2a1a55';for(let x=0;x<W;x+=60){const h=120+((x*7)%5)*50;ctx.fillRect(x,1700-h,60,h)}ctx.fillStyle='#3bceac';ctx.fillRect(0,1700,W,12);
  ctx.strokeStyle='#ffd23f';ctx.lineWidth=12;ctx.strokeRect(20,20,W-40,H-40);ctx.fillStyle='#ffd23f';ctx.font='800 28px Inter';ctx.textAlign='left';ctx.fillText('NIVEL 1 · CRIPTO · 8 BITS',60,82);ctx.textAlign='center'};
ST.panel=(x,y,w,h,col)=>{ctx.save();ctx.fillStyle='#000';ctx.fillRect(x+10,y+10,w,h);ctx.fillStyle='#2a1a55';ctx.fillRect(x,y,w,h);ctx.lineWidth=8;ctx.strokeStyle=col;ctx.strokeRect(x,y,w,h);ctx.restore()};"""

BG_ISO = """ST.bg=t=>{ctx.fillStyle='#0f2a3a';ctx.fillRect(0,0,W,H);ctx.strokeStyle='rgba(120,200,230,.13)';ctx.lineWidth=2;for(let k=-20;k<30;k++){ctx.beginPath();ctx.moveTo(k*100,0);ctx.lineTo(k*100+1100,640);ctx.moveTo(k*100,0);ctx.lineTo(k*100-1100,640);ctx.stroke();ctx.beginPath();ctx.moveTo(k*100,1920);ctx.lineTo(k*100+1100,1280);ctx.moveTo(k*100,1920);ctx.lineTo(k*100-1100,1280);ctx.stroke()}
  const bs=[[170,1560,160,.5],[370,1520,140,.8],[570,1580,150,.35],[770,1500,160,1],[930,1560,120,.6]];bs.forEach(([x,y,w,v],i)=>{const h=(180+v*220)*(0.9+0.1*Math.sin(t*1.5+i));ctx.save();ctx.globalAlpha=.30;ctx.fillStyle=['#ff9f1c','#2ec4b6','#e71d36','#cbf3f0','#ff9f1c'][i];ctx.fillRect(x-w/2,y-h,w,h);ctx.fillStyle='#fff';ctx.beginPath();ctx.moveTo(x-w/2,y-h);ctx.lineTo(x,y-h-w*.28);ctx.lineTo(x+w/2,y-h);ctx.lineTo(x,y-h+w*.28);ctx.fill();ctx.restore()});
  ctx.strokeStyle='rgba(255,159,28,.55)';ctx.lineWidth=4;ctx.strokeRect(26,26,W-52,H-52);ctx.fillStyle='rgba(255,159,28,.9)';ctx.font='800 28px Inter';ctx.textAlign='left';ctx.fillText('CIUDAD ISOMÉTRICA · DERIVADOS 2025',50,80);ctx.textAlign='center'};
ST.panel=(x,y,w,h,col)=>{ctx.save();ctx.fillStyle='rgba(10,34,48,.95)';RR(x,y,w,h,14);ctx.fill();ctx.lineWidth=5;ctx.strokeStyle=col;RR(x,y,w,h,14);ctx.stroke();ctx.fillStyle=col;ctx.fillRect(x+16,y+h-10,w-32,6);ctx.restore()};"""

BG_LOW = """ST.bg=t=>{const g2=ctx.createLinearGradient(0,0,0,H);g2.addColorStop(0,'#1d1b3a');g2.addColorStop(.7,'#4a2545');g2.addColorStop(1,'#ff8a5b');ctx.fillStyle=g2;ctx.fillRect(0,0,W,H);
  const r=rng(9);const peaks=[];for(let i=0;i<=8;i++)peaks.push([i*135,1560-((i*5)%4)*90-(i>4?i*18:0)+Math.sin(t*.8+i)*14]);
  for(let i=0;i<8;i++){const [x1,y1]=peaks[i],[x2,y2]=peaks[i+1];ctx.fillStyle='rgba('+(40+i*16)+','+(20+i*6)+','+(70+i*9)+',.85)';ctx.beginPath();ctx.moveTo(x1,H);ctx.lineTo(x1,y1);ctx.lineTo((x1+x2)/2,Math.min(y1,y2)-90);ctx.lineTo(x2,y2);ctx.lineTo(x2,H);ctx.fill();ctx.fillStyle='rgba(255,209,102,.12)';ctx.beginPath();ctx.moveTo(x1,y1);ctx.lineTo((x1+x2)/2,Math.min(y1,y2)-90);ctx.lineTo((x1+x2)/2,y1+50);ctx.fill()}
  ctx.strokeStyle='rgba(255,209,102,.5)';ctx.lineWidth=4;ctx.strokeRect(26,26,W-52,H-52);ctx.fillStyle='rgba(255,209,102,.9)';ctx.font='800 28px Inter';ctx.textAlign='left';ctx.fillText('WYCKOFF · MONTAÑAS LOWPOLY',50,80);ctx.textAlign='center'};
ST.panel=(x,y,w,h,col)=>{ctx.save();ctx.fillStyle='rgba(29,27,58,.93)';ctx.beginPath();ctx.moveTo(x+24,y);ctx.lineTo(x+w,y);ctx.lineTo(x+w,y+h-24);ctx.lineTo(x+w-24,y+h);ctx.lineTo(x,y+h);ctx.lineTo(x,y+24);ctx.closePath();ctx.fill();ctx.lineWidth=5;ctx.strokeStyle=col;ctx.stroke();ctx.restore()};"""

BG_ACU = """ST.bg=t=>{ctx.fillStyle='#f6f0e4';ctx.fillRect(0,0,W,H);const r=rng(13);const cols=['#1f8a8a','#d9534f','#e0a526','#6a4c93'];ctx.save();for(let i=0;i<14;i++){ctx.globalAlpha=.10+.05*Math.sin(t*.7+i);ctx.fillStyle=cols[i%4];ctx.beginPath();ctx.ellipse(r()*W,r()*H,120+r()*260,90+r()*200,r()*3,0,7);ctx.fill()}ctx.restore();
  ctx.strokeStyle='#2b2b3a';ctx.lineWidth=5;ctx.setLineDash([2,12]);ctx.strokeRect(34,34,W-68,H-68);ctx.setLineDash([]);ctx.fillStyle='rgba(43,43,58,.75)';ctx.font='800 28px Inter';ctx.textAlign='left';ctx.fillText('ACUARELA · BEAR STEARNS 2008',64,92);ctx.textAlign='center'};
ST.panel=(x,y,w,h,col)=>{ctx.save();ctx.fillStyle='rgba(255,250,240,.96)';RR(x,y,w,h,22);ctx.fill();ctx.lineWidth=5;ctx.strokeStyle='#2b2b3a';RR(x,y,w,h,22);ctx.stroke();ctx.fillStyle=col;ctx.globalAlpha=.85;RR(x+14,y+14,12,h-28,6);ctx.fill();ctx.restore()};"""

BG_DECO = """ST.bg=t=>{ctx.fillStyle='#2a0a14';ctx.fillRect(0,0,W,H);ctx.save();ctx.translate(540,1620);ctx.strokeStyle='rgba(232,196,104,.35)';ctx.lineWidth=4;for(let i=-9;i<=9;i++){ctx.beginPath();ctx.moveTo(0,0);ctx.lineTo(Math.sin(i*.17+Math.sin(t*.5)*.03)*620,-Math.cos(i*.17)*620);ctx.stroke()}for(let k=1;k<5;k++){ctx.beginPath();ctx.arc(0,0,k*120,Math.PI,0);ctx.stroke()}ctx.restore();
  ctx.strokeStyle='#e8c468';ctx.lineWidth=6;ctx.strokeRect(30,30,W-60,H-60);ctx.lineWidth=2;ctx.strokeRect(50,50,W-100,H-100);ctx.fillStyle='#e8c468';ctx.font='800 28px Inter';ctx.textAlign='left';ctx.fillText('ART DÉCO · ACKMAN 2020',80,100);ctx.textAlign='center'};
ST.panel=(x,y,w,h,col)=>{ctx.save();ctx.fillStyle='rgba(42,10,20,.95)';ctx.fillRect(x,y,w,h);ctx.lineWidth=4;ctx.strokeStyle=col;ctx.strokeRect(x,y,w,h);ctx.lineWidth=2;ctx.strokeRect(x+10,y+10,w-20,h-20);ctx.restore()};"""

BG_TELE = """ST.bg=t=>{ctx.fillStyle='#cfd8dc';ctx.fillRect(0,0,W,H);ctx.fillStyle='#b4c0c6';ctx.fillRect(0,0,W,120);const off=(t*120)%80;ctx.fillStyle='#1b2733';ctx.font='800 34px Inter';ctx.textAlign='left';ctx.fillText('CME  GC  +  ES  +  ZN  ·  TELETIPO  ·  INTERÉS ABIERTO',-off+30,76);ctx.textAlign='center';
  ctx.strokeStyle='rgba(27,39,51,.25)';ctx.lineWidth=2;for(let y=190;y<1500;y+=64){ctx.beginPath();ctx.moveTo(40,y);ctx.lineTo(W-40,y);ctx.stroke()}
  ctx.save();ctx.translate(860,1390);ctx.rotate(-.22);ctx.globalAlpha=.55;ctx.strokeStyle='#e4572e';ctx.lineWidth=8;ctx.strokeRect(-170,-50,340,100);ctx.fillStyle='#e4572e';ctx.font='900 50px Inter';ctx.fillText('ABIERTOS',0,16);ctx.restore()};
ST.panel=(x,y,w,h,col)=>{ctx.save();ctx.fillStyle='rgba(244,247,248,.97)';ctx.fillRect(x,y,w,h);ctx.lineWidth=3;ctx.strokeStyle='#1b2733';ctx.strokeRect(x,y,w,h);ctx.fillStyle=col;ctx.fillRect(x,y,14,h);ctx.restore()};"""

BG_CRT = """ST.bg=t=>{ctx.fillStyle='#0a0612';ctx.fillRect(0,0,W,H);ctx.fillStyle='rgba(199,125,255,.07)';for(let y=0;y<H;y+=6)ctx.fillRect(0,y,W,2);const by=((t*140)%H);const gr=ctx.createLinearGradient(0,by-120,0,by+120);gr.addColorStop(0,'rgba(199,125,255,0)');gr.addColorStop(.5,'rgba(199,125,255,.10)');gr.addColorStop(1,'rgba(199,125,255,0)');ctx.fillStyle=gr;ctx.fillRect(0,by-120,W,240);
  ctx.strokeStyle='rgba(199,125,255,.55)';ctx.lineWidth=5;RR(24,24,W-48,H-48,40);ctx.stroke();ctx.fillStyle='rgba(199,125,255,.9)';ctx.font='800 28px VT323, Inter';ctx.textAlign='left';ctx.fillText('C:\\\\MQL5\\\\EXPERTS> ORDERCHECK_',64,86);ctx.textAlign='center'};
ST.panel=(x,y,w,h,col)=>{ctx.save();ctx.fillStyle='rgba(10,6,18,.95)';RR(x,y,w,h,12);ctx.fill();ctx.lineWidth=4;ctx.strokeStyle=col;RR(x,y,w,h,12);ctx.stroke();ctx.fillStyle=col;ctx.globalAlpha=.25;ctx.fillRect(x+8,y+8,w-16,10);ctx.restore()};"""

g.THEMES.update({
 'pixel8': mk(32, 'pixel-art 8 bits violeta noche con amarillo, menta y rosa', BG_PIX, ["#ffd23f","#3bceac","#ff6b9d","#ffffff"], '#fff6e0', '#a99bd6', '#ffd23f', '#2a1a55', '#1b1038',
   "rgba(27,16,56,.96)","#ffd23f","#fff6e0","#1b1038","#fff6e0","#ffd23f","#ffd23f","#1b1038",'rgba(27,16,56,.88)',0,1,2,'#a99bd6',0,'#1b1038'),
 'iso': mk(33, 'ciudad isométrica azul petróleo con edificios naranja, turquesa y rojo', BG_ISO, ["#ff9f1c","#2ec4b6","#e71d36","#cbf3f0"], '#eaf7f8', '#8fb4bd', '#ff9f1c', '#0a2230', '#0f2a3a',
   "rgba(10,34,48,.96)","#ff9f1c","#eaf7f8","#0f2a3a","#eaf7f8","#ff9f1c","#ff9f1c","#0f2a3a",'rgba(10,34,48,.88)',0,1,2,'#8fb4bd',0,'#0f2a3a'),
 'lowpoly': mk(34, 'cordillera lowpoly al atardecer violeta con cielo coral y dorado', BG_LOW, ["#ff8a5b","#ffd166","#06d6a0","#ffffff"], '#fff4e6', '#c9b6d9', '#ffd166', '#1d1b3a', '#1d1b3a',
   "rgba(29,27,58,.96)","#ffd166","#fff4e6","#1d1b3a","#fff4e6","#ffd166","#ffd166","#1d1b3a",'rgba(29,27,58,.88)',1,0,2,'#c9b6d9',0,'#1d1b3a'),
 'acuarela': mk(35, 'acuarela con manchas turquesa, coral, ocre y violeta sobre papel crema', BG_ACU, ["#d9534f","#1f8a8a","#c98a10","#6a4c93"], '#2b2b3a', '#6e6a60', '#d9534f', '#fffaf0', '#f6f0e4',
   "rgba(255,250,240,.97)","#d9534f","#2b2b3a","#2b2b3a","#fffaf0","#d9534f","#d9534f","#fffaf0",'rgba(255,250,240,.93)',1,0,3,'#6e6a60',0,'#fffaf0'),
 'deco': mk(36, 'art déco burdeos con abanico dorado y marco doble', BG_DECO, ["#e8c468","#f4e3b2","#d1495b","#ffffff"], '#f8ecd0', '#c5a9a0', '#e8c468', '#2a0a14', '#2a0a14',
   "rgba(42,10,20,.96)","#e8c468","#f8ecd0","#2a0a14","#f8ecd0","#e8c468","#e8c468","#2a0a14",'rgba(42,10,20,.88)',0,1,2,'#c5a9a0',0,'#2a0a14'),
 'teletipo': mk(37, 'cinta de teletipo gris azulado con sello naranja y tinta marino', BG_TELE, ["#e4572e","#17697a","#6a4c93","#1b2733"], '#1b2733', '#546a76', '#e4572e', '#f4f7f8', '#cfd8dc',
   "rgba(244,247,248,.97)","#e4572e","#1b2733","#1b2733","#f4f7f8","#e4572e","#e4572e","#f4f7f8",'rgba(244,247,248,.93)',0,1,2,'#546a76',0,'#f4f7f8'),
 'crt': mk(38, 'monitor CRT violeta fósforo sobre negro con líneas de barrido y cian', BG_CRT, ["#c77dff","#4cf0e0","#ffb347","#ffffff"], '#f1e4ff', '#9a84b8', '#c77dff', '#0a0612', '#0a0612',
   "rgba(10,6,18,.96)","#c77dff","#f1e4ff","#0a0612","#f1e4ff","#c77dff","#c77dff","#0a0612",'rgba(10,6,18,.88)',0,1,2,'#9a84b8',0,'#0a0612'),
})

R = []
exec(open(os.path.join(HERE, 'content_20nov.py'), encoding='utf-8').read())

if __name__ == '__main__':
    sel = [int(x) for x in sys.argv[1:]]
    for r in R:
        if sel and r['n'] not in sel: continue
        open(os.path.join(HERE, r['page'] + '.html'), 'w').write(g.build(r))
        print('ok', r['page'], r['scene'])
