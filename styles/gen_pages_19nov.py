#!/usr/bin/env python3
"""Genera las páginas v242–v248 (reels del 19 nov 2026) con la plantilla std/h0/b6 de gen_pages_16nov.
Estilos 25–31 (4.º uso, nuevas paletas). Uso: python3 gen_pages_19nov.py [n1 n2 ...]"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import gen_pages_16nov as g

def mk(est, pal, bg, C, txt, mu, acc, pn, dk, subBg, subStroke, subFill, ctaBg, ctaSub, ctaGlow, ctaAccent, ctaBtnText, ov, c1, c2, c3, covmu, btn, btxt, lt=None):
    return dict(est=est, uso='4.º', pal=pal, bg=bg, C=C, txt=txt, lt=lt or txt, mu=mu, acc=acc, pn=pn, dk=dk,
        sty=dict(subBg=subBg, subStroke=subStroke, subFill=subFill, ctaBg=ctaBg, ctaSub=ctaSub, ctaGlow=ctaGlow, ctaAccent=ctaAccent, ctaBtnText=ctaBtnText),
        cov=dict(ov=ov, c1=c1, c2=c2, c3=c3, mu=covmu, btn=btn, btxt=btxt))

BG_DOC = """ST.bg=t=>{ctx.fillStyle='#0d0d0d';ctx.fillRect(0,0,W,H);const r=rng(7);for(let i=0;i<220;i++){ctx.fillStyle='rgba(255,255,255,'+(.03+r()*.05)+')';ctx.fillRect(r()*W,r()*H,2+r()*3,2+r()*3)}
  ctx.fillStyle='#1c1c1c';ctx.fillRect(0,0,64,H);ctx.fillRect(W-64,0,64,H);ctx.fillStyle='#0d0d0d';const off=(t*60)%90;for(let y=-90+off;y<H;y+=90){RR(18,y,28,48,6);ctx.fill();RR(W-46,y,28,48,6);ctx.fill()}
  ctx.strokeStyle='rgba(212,175,55,.55)';ctx.lineWidth=4;ctx.strokeRect(84,26,W-168,H-52);
  ctx.fillStyle='rgba(212,175,55,.8)';ctx.font='800 28px Inter';ctx.textAlign='left';ctx.fillText('DOCUMENTAL  ·  ARCHIVO',110,76);ctx.textAlign='center'};
ST.panel=(x,y,w,h,col)=>{ctx.save();ctx.fillStyle='rgba(20,20,20,.94)';ctx.fillRect(x,y,w,h);ctx.lineWidth=3;ctx.strokeStyle=col;ctx.strokeRect(x,y,w,h);ctx.fillStyle=col;ctx.fillRect(x,y,w,8);ctx.restore()};"""

BG_MON = """ST.bg=t=>{ctx.fillStyle='#070b12';ctx.fillRect(0,0,W,H);
  for(let k=0;k<3;k++){const x=40+k*340,y=1480;ctx.fillStyle='#0d1522';ctx.fillRect(x,y,320,200);ctx.strokeStyle='#27425f';ctx.lineWidth=4;ctx.strokeRect(x,y,320,200);
    ctx.strokeStyle=['#3ddc97','#4cc9f0','#ffb703'][k];ctx.lineWidth=4;ctx.beginPath();for(let i=0;i<=16;i++){const px=x+10+i*19,py=y+110-Math.sin(i*.7+t*1.2+k*2)*40-i*2;i?ctx.lineTo(px,py):ctx.moveTo(px,py)}ctx.stroke()}
  ctx.fillStyle='#0d1522';ctx.fillRect(0,0,W,64);ctx.fillStyle='#4cc9f0';ctx.font='800 26px Inter';ctx.textAlign='left';ctx.fillText('SALA DE OPERACIONES  ·  MONITOR 1/3',24,42);ctx.textAlign='center';
  ctx.strokeStyle='rgba(76,201,240,.12)';ctx.lineWidth=2;for(let y=120;y<1440;y+=80){ctx.beginPath();ctx.moveTo(30,y);ctx.lineTo(W-30,y);ctx.stroke()}};
ST.panel=(x,y,w,h,col)=>{ctx.save();ctx.fillStyle='rgba(13,21,34,.95)';ctx.fillRect(x,y,w,h);ctx.lineWidth=4;ctx.strokeStyle=col;ctx.strokeRect(x,y,w,h);ctx.fillStyle=col;ctx.fillRect(x,y,w,26);ctx.restore()};"""

BG_RELOJ = """ST.bg=t=>{ctx.fillStyle='#10141f';ctx.fillRect(0,0,W,H);ctx.save();ctx.translate(540,1560);ctx.globalAlpha=.22;ctx.strokeStyle='#f2c14e';ctx.lineWidth=8;ctx.beginPath();ctx.arc(0,0,250,0,7);ctx.stroke();
  for(let i=0;i<12;i++){ctx.rotate(Math.PI/6);ctx.beginPath();ctx.moveTo(0,-230);ctx.lineTo(0,-200);ctx.stroke()}
  ctx.rotate(t*.9);ctx.lineWidth=10;ctx.beginPath();ctx.moveTo(0,0);ctx.lineTo(0,-190);ctx.stroke();ctx.restore();
  ctx.strokeStyle='rgba(242,193,78,.5)';ctx.lineWidth=4;ctx.strokeRect(26,26,W-52,H-52);ctx.fillStyle='rgba(242,193,78,.7)';ctx.font='800 28px Inter';ctx.textAlign='left';ctx.fillText('CUENTA REGRESIVA',50,80);ctx.textAlign='center'};
ST.panel=(x,y,w,h,col)=>{ctx.save();ctx.fillStyle='rgba(16,20,31,.94)';RR(x,y,w,h,18);ctx.fill();ctx.lineWidth=5;ctx.strokeStyle=col;RR(x,y,w,h,18);ctx.stroke();ctx.restore()};"""

BG_EXP = """ST.bg=t=>{ctx.fillStyle='#d9c8a0';ctx.fillRect(0,0,W,H);ctx.fillStyle='#c9b78a';ctx.fillRect(0,0,W,120);ctx.fillStyle='#b5a176';RR(60,10,360,100,14);ctx.fill();ctx.fillStyle='#3b2f1e';ctx.font='900 38px Inter';ctx.textAlign='left';ctx.fillText('EXPEDIENTE · BOLSAS',84,74);ctx.textAlign='center';
  ctx.save();ctx.translate(880,1620);ctx.rotate(-.25);ctx.globalAlpha=.55;ctx.strokeStyle='#b3261e';ctx.lineWidth=8;ctx.strokeRect(-150,-50,300,100);ctx.fillStyle='#b3261e';ctx.font='900 54px Inter';ctx.fillText('RANKING',0,18);ctx.restore();
  ctx.strokeStyle='rgba(59,47,30,.25)';ctx.lineWidth=2;for(let y=170;y<1500;y+=70){ctx.beginPath();ctx.moveTo(40,y);ctx.lineTo(W-40,y);ctx.stroke()}};
ST.panel=(x,y,w,h,col)=>{ctx.save();ctx.fillStyle='rgba(255,250,235,.97)';ctx.fillRect(x,y,w,h);ctx.lineWidth=3;ctx.strokeStyle='#3b2f1e';ctx.strokeRect(x,y,w,h);ctx.fillStyle=col;ctx.fillRect(x,y,14,h);ctx.restore()};"""

BG_RADAR = """ST.bg=t=>{ctx.fillStyle='#04120a';ctx.fillRect(0,0,W,H);ctx.save();ctx.translate(540,1560);for(let i=1;i<=4;i++){ctx.strokeStyle='rgba(80,255,150,.22)';ctx.lineWidth=3;ctx.beginPath();ctx.arc(0,0,i*65,0,7);ctx.stroke()}
  ctx.strokeStyle='rgba(80,255,150,.18)';ctx.beginPath();ctx.moveTo(-270,0);ctx.lineTo(270,0);ctx.moveTo(0,-270);ctx.lineTo(0,270);ctx.stroke();
  const a=t*1.6;const gr=ctx.createConicGradient?ctx.createConicGradient(a,0,0):null;if(gr){gr.addColorStop(0,'rgba(80,255,150,.35)');gr.addColorStop(.12,'rgba(80,255,150,0)');gr.addColorStop(1,'rgba(80,255,150,0)');ctx.fillStyle=gr;ctx.beginPath();ctx.arc(0,0,260,0,7);ctx.fill()}ctx.restore();
  ctx.strokeStyle='rgba(80,255,150,.45)';ctx.lineWidth=4;ctx.strokeRect(26,26,W-52,H-52);ctx.fillStyle='rgba(80,255,150,.8)';ctx.font='800 28px Inter';ctx.textAlign='left';ctx.fillText('RADAR  ·  4 ENTORNOS',50,80);ctx.textAlign='center'};
ST.panel=(x,y,w,h,col)=>{ctx.save();ctx.fillStyle='rgba(4,18,10,.94)';RR(x,y,w,h,10);ctx.fill();ctx.lineWidth=4;ctx.strokeStyle=col;RR(x,y,w,h,10);ctx.stroke();ctx.restore()};"""

BG_VEL = """ST.bg=t=>{ctx.fillStyle='#14110f';ctx.fillRect(0,0,W,H);ctx.save();ctx.translate(540,1580);ctx.lineWidth=36;for(let i=0;i<3;i++){ctx.strokeStyle=['rgba(61,220,151,.30)','rgba(255,196,61,.30)','rgba(255,92,92,.30)'][i];ctx.beginPath();ctx.arc(0,0,220,Math.PI+i*Math.PI/3,Math.PI+(i+1)*Math.PI/3);ctx.stroke()}
  ctx.strokeStyle='rgba(255,255,255,.35)';ctx.lineWidth=10;ctx.beginPath();const a=Math.PI*1.5+Math.sin(t*.8)*.9;ctx.moveTo(0,0);ctx.lineTo(Math.cos(a)*190,Math.sin(a)*190);ctx.stroke();ctx.restore();
  ctx.strokeStyle='rgba(255,196,61,.5)';ctx.lineWidth=4;ctx.strokeRect(26,26,W-52,H-52);ctx.fillStyle='rgba(255,196,61,.8)';ctx.font='800 28px Inter';ctx.textAlign='left';ctx.fillText('VENCIMIENTO  ·  FUTUROS GC',50,80);ctx.textAlign='center'};
ST.panel=(x,y,w,h,col)=>{ctx.save();ctx.fillStyle='rgba(28,22,18,.95)';RR(x,y,w,h,16);ctx.fill();ctx.lineWidth=5;ctx.strokeStyle=col;RR(x,y,w,h,16);ctx.stroke();ctx.restore()};"""

BG_SEM = """ST.bg=t=>{ctx.fillStyle='#0b0f14';ctx.fillRect(0,0,W,H);ctx.save();ctx.translate(540,1560);ctx.fillStyle='#161d27';RR(-70,-140,140,280,26);ctx.fill();const on=Math.floor(t*.7)%3;['#ff4d4d','#ffd23f','#3ddc97'].forEach((c,i)=>{ctx.globalAlpha=i===on?.9:.18;ctx.fillStyle=c;ctx.beginPath();ctx.arc(0,-90+i*90,34,0,7);ctx.fill()});ctx.restore();
  ctx.strokeStyle='rgba(61,220,151,.45)';ctx.lineWidth=4;ctx.strokeRect(26,26,W-52,H-52);ctx.fillStyle='rgba(61,220,151,.85)';ctx.font='800 28px Inter';ctx.textAlign='left';ctx.fillText('ROBOTS  ·  MQL5  ·  CRITERIO',50,80);ctx.textAlign='center'};
ST.panel=(x,y,w,h,col)=>{ctx.save();ctx.fillStyle='rgba(16,22,30,.95)';RR(x,y,w,h,12);ctx.fill();ctx.lineWidth=4;ctx.strokeStyle=col;RR(x,y,w,h,12);ctx.stroke();ctx.fillStyle=col;ctx.beginPath();ctx.arc(x+w-34,y+34,12,0,7);ctx.fill();ctx.restore()};"""

g.THEMES.update({
 'documental': mk(25, 'documental en blanco y negro con perforaciones, grano y acento dorado', BG_DOC, ["#d4af37","#f5e6b0","#ff6b57","#ffffff"], '#f2efe6', '#a8a393', '#d4af37', '#141414', '#0d0d0d',
   "rgba(13,13,13,.96)","#d4af37","#f2efe6","#0d0d0d","#f2efe6","#d4af37","#d4af37","#0d0d0d",'rgba(13,13,13,.88)',2,1,0,'#a8a393',0,'#0d0d0d'),
 'monitores': mk(26, 'sala de operaciones azul medianoche con monitores y líneas cian, verde y ámbar', BG_MON, ["#4cc9f0","#3ddc97","#ffb703","#ffffff"], '#e6f1fb', '#8fa7bd', '#4cc9f0', '#0d1522', '#070b12',
   "rgba(7,11,18,.96)","#4cc9f0","#e6f1fb","#070b12","#e6f1fb","#4cc9f0","#4cc9f0","#070b12",'rgba(7,11,18,.88)',0,1,2,'#8fa7bd',0,'#070b12'),
 'reloj': mk(27, 'cuenta regresiva azul noche con reloj gigante y trazos dorados', BG_RELOJ, ["#f2c14e","#7bdff2","#ff6b6b","#ffffff"], '#f4f1e8', '#9aa3b5', '#f2c14e', '#10141f', '#10141f',
   "rgba(16,20,31,.96)","#f2c14e","#f4f1e8","#10141f","#f4f1e8","#f2c14e","#f2c14e","#10141f",'rgba(16,20,31,.88)',0,1,2,'#9aa3b5',0,'#10141f'),
 'expediente': mk(28, 'expediente de papel manila con pestaña y sello rojo', BG_EXP, ["#b3261e","#1d4ed8","#0f766e","#3b2f1e"], '#2b2114', '#6b5a3c', '#b3261e', '#fffaeb', '#d9c8a0',
   "rgba(255,250,235,.97)","#b3261e","#2b2114","#2b2114","#fffaeb","#b3261e","#b3261e","#fffaeb",'rgba(255,250,235,.93)',0,1,2,'#6b5a3c',0,'#fffaeb'),
 'radar': mk(29, 'radar verde fósforo sobre negro con barrido y cuatro cuadrantes', BG_RADAR, ["#50ff96","#b6ff6b","#ff9f43","#ffffff"], '#e4ffee', '#7fbf9a', '#50ff96', '#04120a', '#04120a',
   "rgba(4,18,10,.96)","#50ff96","#e4ffee","#04120a","#e4ffee","#50ff96","#50ff96","#04120a",'rgba(4,18,10,.88)',0,1,2,'#7fbf9a',0,'#04120a'),
 'velocimetro': mk(30, 'velocímetro marrón oscuro con arco verde, ámbar y rojo', BG_VEL, ["#ffc43d","#3ddc97","#ff5c5c","#ffffff"], '#fff3dc', '#b5a68c', '#ffc43d', '#1c1612', '#14110f',
   "rgba(20,17,15,.96)","#ffc43d","#fff3dc","#14110f","#fff3dc","#ffc43d","#ffc43d","#14110f",'rgba(20,17,15,.88)',0,1,2,'#b5a68c',0,'#14110f'),
 'semaforo': mk(31, 'semáforo grafito con luces roja, ámbar y verde', BG_SEM, ["#3ddc97","#ffd23f","#ff4d4d","#ffffff"], '#eaf3ee', '#8aa398', '#3ddc97', '#10161e', '#0b0f14',
   "rgba(11,15,20,.96)","#3ddc97","#eaf3ee","#0b0f14","#eaf3ee","#3ddc97","#3ddc97","#0b0f14",'rgba(11,15,20,.88)',0,1,2,'#8aa398',0,'#0b0f14'),
})

R = []
exec(open(os.path.join(HERE, 'content_19nov.py'), encoding='utf-8').read())

if __name__ == '__main__':
    sel = [int(x) for x in sys.argv[1:]]
    for r in R:
        if sel and r['n'] not in sel: continue
        open(os.path.join(HERE, r['page'] + '.html'), 'w').write(g.build(r))
        print('ok', r['page'], r['scene'])
