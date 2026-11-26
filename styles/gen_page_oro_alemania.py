#!/usr/bin/env python3
"""Reel de prueba (26 nov 2026, 18:00): Alemania repatria 674 t de oro (Bundesbank 2013–2017).
Estilo 51 (nuevo): fotografía cinematográfica generada con IA (Higgsfield) + datos en paneles de vidrio.
Primera página con la tarjeta final "Robot Trust Gold Mr. Y" y carátula con persona/foto.
Uso: python3 gen_page_oro_alemania.py  -> v298_foto_oro_alemania.html"""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import gen_pages_16nov as g

def js(o): return json.dumps(o, ensure_ascii=False)

SUBS = [
 ("Alemania trajo a casa 674 toneladas de oro desde Nueva York y París.",
  "Alemania trajo a casa seiscientas setenta y cuatro toneladas de oro desde Nueva York y París."),
 ("En 2013 anunció el plan: 374 toneladas desde París y 300 desde Nueva York.",
  "En dos mil trece anunció el plan: trescientas setenta y cuatro toneladas desde París y trescientas desde Nueva York."),
 ("En la Guerra Fría se guardó lejos, por temor a que cayera en manos soviéticas. Con el euro, París ya no hacía falta.",
  "En la Guerra Fría se guardó lejos, por temor a que cayera en manos soviéticas. Con el euro, París ya no hacía falta."),
 ("Fueron 53.780 lingotes, ≈ 27.900 millones de dólares según CNBC. La ruta fue secreta.",
  "Fueron cincuenta y tres mil setecientos ochenta lingotes: unos veintisiete mil novecientos millones de dólares. La ruta fue secreta."),
 ("En Fráncfort revisaron autenticidad, pureza y peso: cero irregularidades. Terminó ≈ 3 años antes.",
  "En Fráncfort revisaron autenticidad, pureza y peso: cero irregularidades. Y terminó tres años antes."),
 ("Hoy tiene 3.350 t: 1.710 en Fráncfort, 1.236 en Nueva York y 404 en Londres. Fuentes: Bundesbank y CNBC.",
  "Hoy tiene tres mil trescientas cincuenta toneladas: mil setecientas diez en Fráncfort, mil doscientas treinta y seis en Nueva York y cuatrocientas cuatro en Londres."),
 ("Para tu robot: saber dónde está tu dinero también es gestionar el riesgo. Contenido educativo.",
  "Para tu robot: saber dónde está tu dinero también es gestionar el riesgo. Contenido educativo."),
]
subs = [[a, b, v, s] for (a, b), (v, s) in zip(g.WIN, SUBS)] + [g.OUTRO, g.CTA]
ev = [[0.3, "rise", 2.4], [3.0, "down"], [3.6, "hit"]] + g.EVB
SPEC = dict(name='OroAlemania', hook='¿POR QUÉ ALEMANIA SACÓ 674 TONELADAS DE ORO DE NUEVA YORK Y PARÍS?',
            dur=60, cta=56, bpm=96, mus="soft", prog=[[45, "m"], [41, "M"], [43, "M"], [40, "m"]], ev=ev, subs=subs)
GOLD, DK = '#ffc83d', '#0b0d12'
STY = dict(subFont="800 42px Inter", ctaFontS="800 50px Inter", ctaFontL="900 104px Inter",
           subBg="rgba(8,9,14,.88)", subStroke=GOLD, subFill="#fff", ctaBg=DK, ctaSub="#f4efe2",
           ctaGlow=GOLD, ctaAccent=GOLD, ctaBtnText=DK)
C = [GOLD, "#6fd6ff", "#ff8a5c", "#ffffff"]

page = f"""<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{{font-family:Inter;font-weight:800;src:url(node_modules/@fontsource/inter/files/inter-latin-800-normal.woff2)}}
@font-face{{font-family:Inter;font-weight:900;src:url(node_modules/@fontsource/inter/files/inter-latin-900-normal.woff2)}}
html,body{{margin:0;background:#000}}canvas{{display:block;width:1080px;height:1920px}}
</style></head><body><canvas id="c"></canvas><script src="common.js"></script><script>
// Estilo 51 (nuevo, 1.er uso) — fotografía cinematográfica IA con paneles de vidrio y acento dorado — tema: Alemania repatria su oro (60 s).
const SPEC={js(SPEC)};
const STY={js(STY)};
const DK=STY.ctaBg,ACC=STY.ctaAccent,FAM='Inter';
window.FONTS=['900 40px Inter','800 40px Inter'];
</script><script src="img_oro_alemania.js"></script><script src="kit2.js"></script><script src="kit3.js"></script><script>
// __ready solo cuando también cargaron las fotos
let _kr=false;const _imgs=[IMG_A,IMG_B,IMG_C];
Object.defineProperty(window,'__ready',{{configurable:true,get:()=>_kr&&_imgs.every(i=>i.complete&&i.naturalWidth>0),set:v=>{{_kr=v}}}});
const C={js(C)};
Object.assign(ST,{{txt:'#ffffff',mu:'#cfd3dc',acc:ACC,pn:'rgba(10,12,18,.74)',c:C}});
ST.panel=(x,y,w,h,col)=>{{ctx.save();ctx.fillStyle='rgba(10,12,18,.72)';RR(x,y,w,h,22);ctx.fill();ctx.lineWidth=4;ctx.strokeStyle=col;RR(x,y,w,h,22);ctx.stroke();
  ctx.fillStyle=col;RR(x,y+16,10,h-32,5);ctx.fill();ctx.restore()}};
// foto a pantalla completa con zoom lento (Ken Burns) anclado en (ax,ay)
function photo(img,z,ax,ay,a){{if(a<=0)return;ctx.save();ctx.globalAlpha=a;ctx.translate(ax,ay);ctx.scale(z,z);ctx.translate(-ax,-ay);ctx.drawImage(img,0,0,W,H);ctx.restore()}}
// segmentos de fondo: [inicio, fin, imagen, zoom inicial, zoom final, ancla x, ancla y]
const SEG=[[0,13.5,IMG_A,1.14,1.0,540,1250],[13.5,28.3,IMG_B,1.0,1.12,300,1300],[28.3,35.1,IMG_C,1.04,1.14,560,900],[35.1,43.5,IMG_A,1.25,1.32,540,1200],[43.5,60,IMG_C,1.1,1.16,540,900]];
ST.bg=t=>{{ctx.fillStyle=DK;ctx.fillRect(0,0,W,H);
  for(const [a,b,img,z0,z1,ax,ay] of SEG){{const al=Math.min(clamp((t-a+.5)/.5),clamp((b-t+.5)/.5));if(al<=0)continue;photo(img,lerp(z0,z1,prog(t,a,b)),ax,ay,al)}}
  let gr=ctx.createLinearGradient(0,0,0,880);gr.addColorStop(0,'rgba(5,6,10,.92)');gr.addColorStop(.7,'rgba(5,6,10,.62)');gr.addColorStop(1,'rgba(5,6,10,0)');ctx.fillStyle=gr;ctx.fillRect(0,0,W,880);
  gr=ctx.createLinearGradient(0,1250,0,H);gr.addColorStop(0,'rgba(5,6,10,0)');gr.addColorStop(1,'rgba(5,6,10,.8)');ctx.fillStyle=gr;ctx.fillRect(0,1250,W,H-1250);
  // grano y viñeta de cine
  const r=rng(Math.floor(t*30)+3);ctx.save();ctx.globalAlpha=.05;ctx.fillStyle='#fff';for(let i=0;i<220;i++)ctx.fillRect(r()*W,r()*H,2,2);ctx.restore();
  const v=ctx.createRadialGradient(540,960,600,540,960,1250);v.addColorStop(0,'rgba(0,0,0,0)');v.addColorStop(1,'rgba(0,0,0,.45)');ctx.fillStyle=v;ctx.fillRect(0,0,W,H)}};
// texto con sombra para leer sobre la foto
function S(s,x,y,sz,col,a=1,al='center'){{if(a<=0)return;T(fx(s),x,y,{{font:`900 ${{sz}}px Inter`,fill:col,a,align:al,glow:'rgba(0,0,0,.95)',gb:22}})}}
function fz(txt,sz,maxW){{ctx.save();ctx.font=`900 ${{sz}}px Inter`;const w=ctx.measureText(fx(txt)).width;ctx.restore();return w>maxW?Math.floor(sz*maxW/w):sz}}
function chip(s,y,col,a){{if(a<=0)return;ctx.save();ctx.globalAlpha*=a;ctx.font='900 34px Inter';const w=ctx.measureText(s).width+56;RR(540-w/2,y-30,w,60,30);ctx.fillStyle=col;ctx.fill();ctx.restore();T(s,540,y+1,{{font:'900 34px Inter',fill:DK,a}})}}
function bigS(t,t0,y,txt,sz,col){{pop(t,t0,540,y,()=>T(fx(txt),0,0,{{font:`900 ${{fz(txt,sz,960)}}px Inter`,fill:col,glow:'rgba(0,0,0,.95)',gb:30}}))}}
function blk(t,al,a,h,big,bsz,bc,sub,cards,src){{ctx.save();ctx.globalAlpha=al;chip(h,170,C[1],eout(prog(t,a+.1,a+.6)));bigS(t,a+.6,360,big,bsz,bc);
  S(sub,540,505,fz(sub,40,980),'#fff',eout(prog(t,a+1.6,a+2.2)));
  cards.forEach((s,i)=>card(t,a+2.8+i*1.4,590+i*145,120,C[(i+2)%4==3?0:(i+2)%4],s,null,fz(s,40,850)));
  if(src)S(src,540,1405,26,'#e6e6ee',eout(prog(t,a+6.0,a+6.6)));ctx.restore()}}
function h0(t,al){{ctx.save();ctx.globalAlpha=al;chip('ALEMANIA · 2013–2017',200,C[1],eout(prog(t,.2,.7)));
  bigS(t,.6,420,'674 t',280,ACC);S('DE ORO DE VUELTA A CASA',540,610,fz('DE ORO DE VUELTA A CASA',64,980),'#fff',eout(prog(t,1.6,2.2)));
  S('desde Nueva York y París',540,690,44,C[1],eout(prog(t,2.4,3.0)));ctx.restore()}}
function b1(t,al){{blk(t,al,6.4,'EL PLAN','2013',300,ACC,'16 de enero: la Bundesbank anuncia el traslado',['374 t desde París (todo lo que había)','300 t desde Nueva York · meta: 2020'],'fuente: Deutsche Bundesbank (comunicado de 2013)')}}
function b2(t,al){{blk(t,al,13.6,'¿POR QUÉ ESTABA FUERA?','GUERRA FRÍA',170,ACC,'temor a que cayera en manos soviéticas',['París: para cambiarlo por francos','Con el euro, ese motivo desapareció'],'fuente: CNBC (2017); Deutsche Bundesbank (2013)')}}
function b3(t,al){{blk(t,al,20.6,'EL TRASLADO','53.780',280,ACC,'lingotes llevados a Fráncfort',['≈ US$ 27.900 M (CNBC, 2017)','Rutas y fechas: secretas por seguridad'],'fuente: CNBC, 23 de agosto de 2017')}}
function b4(t,al){{blk(t,al,28.4,'LA REVISIÓN','0',380,ACC,'irregularidades en autenticidad, pureza y peso',['Revisado a fondo en Fráncfort','Terminó en 2017: ≈ 3 años antes'],'fuente: Deutsche Bundesbank (comunicado de 2017)')}}
function b5(t,al){{const a=35.2;ctx.save();ctx.globalAlpha=al;chip('¿DÓNDE ESTÁ HOY?',170,C[1],eout(prog(t,a+.1,a+.6)));bigS(t,a+.6,360,'3.350 t',260,ACC);
  S('reservas de oro de Alemania al 31 dic 2025',540,505,fz('reservas de oro de Alemania al 31 dic 2025',40,980),'#fff',eout(prog(t,a+1.6,a+2.2)));
  ctx.save();ctx.globalAlpha*=eout(prog(t,a+2.4,a+2.9));ST.panel(60,570,960,470,C[1]);ctx.restore();
  barsH(t,a+2.8,[['Fráncfort',1710/1710*.62,ACC,'1.710 t · 51 %'],['Nueva York',1236/1710*.62,C[1],'1.236 t · 37 %'],['Londres',404/1710*.62,C[2],'404 t · 12 %']],110,610,820,140,40);
  S('fuente: Bundesbank (cifras clave 2025); % = cálculo propio',540,1405,26,'#e6e6ee',eout(prog(t,a+6.0,a+6.6)));ctx.restore()}}
function b6(t,a){{endBlock(t,a,43.6,'Saber dónde está tu oro importa','Elige un bróker regulado',C[0],C[1])}}
function cover(){{ST.bg(0);photo(IMG_A,1.06,540,1300,1);
  let gr=ctx.createLinearGradient(0,0,0,1000);gr.addColorStop(0,'rgba(5,6,10,.9)');gr.addColorStop(.75,'rgba(5,6,10,.55)');gr.addColorStop(1,'rgba(5,6,10,0)');ctx.fillStyle=gr;ctx.fillRect(0,0,W,1000);
  chip('HISTORIA REAL · 2013–2017',270,C[1],1);
  S('¿POR QUÉ ALEMANIA',540,385,fz('¿POR QUÉ ALEMANIA',84,980),'#fff',1);S('SACÓ SU ORO?',540,485,fz('SACÓ SU ORO?',104,980),ACC,1);
  T('674 t',540,690,{{font:'900 270px Inter',fill:ACC,glow:'rgba(0,0,0,1)',gb:40,stroke:'rgba(0,0,0,.55)',lw:10}});
  S('DE NUEVA YORK Y PARÍS',540,860,fz('DE NUEVA YORK Y PARÍS',58,980),'#fff',1);
  coverBtn('VER LA HISTORIA →',ACC,DK)}}
function draw(t){{drawBlocks(t,[[0,6.0,h0],[6.4,13.4,b1],[13.6,20.4,b2],[20.6,28.2,b3],[28.4,35.0,b4],[35.2,43.4,b5],[43.6,49.6,b6]])}}
</script></body></html>
"""
open(os.path.join(HERE, 'v298_foto_oro_alemania.html'), 'w').write(page)
print('ok v298_foto_oro_alemania 368')
