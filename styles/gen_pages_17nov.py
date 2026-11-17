#!/usr/bin/env python3
"""Genera las páginas v228–v234 (reels del 17 nov 2026) con la plantilla std/h0/b6 de gen_pages_16nov sobre kit2/kit3.
Estilos 11–17 (5.º uso, nuevas paletas). Uso: python3 gen_pages_17nov.py [n1 n2 ...]  (por defecto todas)"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import gen_pages_16nov as g

def mk(est, pal, bg, C, txt, mu, acc, pn, dk, subBg, subStroke, subFill, ctaBg, ctaSub, ctaGlow, ctaAccent, ctaBtnText, ov, c1, c2, c3, covmu, btn, btxt, lt=None):
    return dict(est=est, uso='5.º', pal=pal, bg=bg, C=C, txt=txt, lt=lt or txt, mu=mu, acc=acc, pn=pn, dk=dk,
        sty=dict(subBg=subBg, subStroke=subStroke, subFill=subFill, ctaBg=ctaBg, ctaSub=ctaSub, ctaGlow=ctaGlow, ctaAccent=ctaAccent, ctaBtnText=ctaBtnText),
        cov=dict(ov=ov, c1=c1, c2=c2, c3=c3, mu=covmu, btn=btn, btxt=btxt))

BG_AMBAR = """ST.bg=t=>{ctx.fillStyle='#0b0700';ctx.fillRect(0,0,W,H);
  const g=ctx.createRadialGradient(540,900,100,540,900,1250);g.addColorStop(0,'rgba(255,176,0,.12)');g.addColorStop(1,'rgba(0,0,0,0)');ctx.fillStyle=g;ctx.fillRect(0,0,W,H);
  ctx.fillStyle='rgba(255,176,0,.05)';for(let y=0;y<H;y+=6)ctx.fillRect(0,y,W,2);
  ctx.fillStyle='#1a1200';ctx.fillRect(0,0,W,64);ctx.fillStyle='#ffb000';ctx.font='800 26px Inter';ctx.textAlign='left';ctx.fillText('TERMINAL DE MERCADOS  >_',24,42);ctx.textAlign='center';
  ctx.save();ctx.globalAlpha=.20;ctx.strokeStyle='#ffb000';ctx.lineWidth=5;ctx.beginPath();for(let i=0;i<=22;i++){const x=i*50,y=1720-Math.sin(i*.7+t*.6)*50-i*10;i?ctx.lineTo(x,y):ctx.moveTo(x,y)}ctx.stroke();ctx.restore();
  ctx.save();ctx.strokeStyle='rgba(255,176,0,.35)';ctx.lineWidth=4;ctx.strokeRect(24,90,W-48,H-150);ctx.restore()};
ST.panel=(x,y,w,h,col)=>{ctx.save();ctx.fillStyle='rgba(22,14,0,.93)';RR(x,y,w,h,4);ctx.fill();ctx.lineWidth=3;ctx.strokeStyle=col;RR(x,y,w,h,4);ctx.stroke();ctx.fillStyle=col;ctx.fillRect(x,y,14,h);ctx.restore()};"""

BG_PERIODICO = """ST.bg=t=>{ctx.fillStyle='#e8dcc0';ctx.fillRect(0,0,W,H);const r=rng(5);ctx.save();ctx.globalAlpha=.10;ctx.fillStyle='#6b5530';for(let i=0;i<260;i++){ctx.fillRect(r()*W,r()*H,2+r()*5,2+r()*5)}ctx.restore();
  ctx.fillStyle='#1a1510';ctx.fillRect(40,60,W-80,8);ctx.fillRect(40,78,W-80,3);ctx.fillRect(40,H-90,W-80,4);
  ctx.save();ctx.globalAlpha=.16;ctx.fillStyle='#1a1510';for(let c=0;c<3;c++){for(let y=1620;y<1800;y+=18){ctx.fillRect(60+c*335,y,300-((y*7)%60),5)}}ctx.restore();
  ctx.fillStyle='#1a1510';ctx.font='900 30px Inter';ctx.textAlign='center';ctx.fillText('EL DIARIO DEL MERCADO · EDICIÓN ESPECIAL',540,44);ctx.textAlign='center'};
ST.panel=(x,y,w,h,col)=>{ctx.save();ctx.fillStyle='#f6eed8';ctx.fillRect(x,y,w,h);ctx.lineWidth=4;ctx.strokeStyle='#1a1510';ctx.strokeRect(x,y,w,h);ctx.fillStyle=col;ctx.fillRect(x,y,16,h);ctx.lineWidth=1.5;ctx.strokeRect(x+6,y+6,w-12,h-12);ctx.restore()};"""

BG_SUIZO = """ST.bg=t=>{ctx.fillStyle='#f4f4f0';ctx.fillRect(0,0,W,H);ctx.strokeStyle='rgba(17,17,17,.08)';ctx.lineWidth=2;for(let x=60;x<W;x+=120){ctx.beginPath();ctx.moveTo(x,0);ctx.lineTo(x,H);ctx.stroke()}for(let y=60;y<H;y+=120){ctx.beginPath();ctx.moveTo(0,y);ctx.lineTo(W,y);ctx.stroke()}
  ctx.fillStyle='#e30613';ctx.fillRect(0,0,W,40);ctx.fillRect(0,H-40,W,40);ctx.fillStyle='#111';ctx.fillRect(0,40,W,10);
  ctx.save();ctx.fillStyle='#e30613';ctx.globalAlpha=.9;ctx.beginPath();ctx.arc(960,1700+Math.sin(t)*10,70,0,7);ctx.fill();ctx.restore();ctx.fillStyle='#111';ctx.fillRect(60,1690,300,12);ctx.fillRect(60,1720,180,12)};
ST.panel=(x,y,w,h,col)=>{ctx.save();ctx.fillStyle='#fff';ctx.fillRect(x,y,w,h);ctx.fillStyle=col;ctx.fillRect(x,y,18,h);ctx.fillStyle='#111';ctx.fillRect(x,y+h-6,w,6);ctx.restore()};"""

BG_LINGOTES = """ST.bg=t=>{const g=ctx.createLinearGradient(0,0,0,H);g.addColorStop(0,'#17120a');g.addColorStop(1,'#080604');ctx.fillStyle=g;ctx.fillRect(0,0,W,H);
  ctx.fillStyle='rgba(255,204,51,.05)';for(let x=0;x<W;x+=120)ctx.fillRect(x,0,3,H);
  const bar=(x,y,w,h)=>{ctx.save();const gg=ctx.createLinearGradient(x,y,x,y+h);gg.addColorStop(0,'#ffe08a');gg.addColorStop(.5,'#e6a817');gg.addColorStop(1,'#8c6410');ctx.fillStyle=gg;ctx.beginPath();ctx.moveTo(x+30,y);ctx.lineTo(x+w-30,y);ctx.lineTo(x+w,y+h);ctx.lineTo(x,y+h);ctx.closePath();ctx.fill();ctx.fillStyle='rgba(255,255,255,.25)';ctx.fillRect(x+40,y+8,w-80,6);ctx.restore()};
  ctx.save();ctx.globalAlpha=.55;for(let r=0;r<3;r++)for(let c=0;c<4-r;c++)bar(110+c*240+r*120,1640-r*70,220,62);ctx.restore();
  ctx.save();ctx.strokeStyle='rgba(255,204,51,.30)';ctx.lineWidth=4;ctx.strokeRect(26,26,W-52,H-52);ctx.restore()};
ST.panel=(x,y,w,h,col)=>{ctx.save();ctx.fillStyle='rgba(22,16,6,.93)';RR(x,y,w,h,14);ctx.fill();ctx.lineWidth=5;ctx.strokeStyle=col;RR(x,y,w,h,14);ctx.stroke();ctx.fillStyle=col;ctx.globalAlpha=.9;ctx.fillRect(x+18,y+h-10,w-36,5);ctx.restore()};"""

BG_SUMIE = """ST.bg=t=>{ctx.fillStyle='#efe9dc';ctx.fillRect(0,0,W,H);const r=rng(9);ctx.save();ctx.globalAlpha=.05;ctx.fillStyle='#000';for(let i=0;i<500;i++)ctx.fillRect(r()*W,r()*H,1+r()*3,1+r()*3);ctx.restore();
  ctx.save();ctx.globalAlpha=.16;ctx.fillStyle='#1a1a1a';ctx.beginPath();ctx.moveTo(0,1500);for(let x=0;x<=W;x+=30)ctx.lineTo(x,1480-Math.sin(x*.012+1)*70-Math.sin(x*.03)*28);ctx.lineTo(W,H);ctx.lineTo(0,H);ctx.fill();
  ctx.globalAlpha=.10;ctx.beginPath();ctx.moveTo(0,1620);for(let x=0;x<=W;x+=30)ctx.lineTo(x,1600-Math.sin(x*.02+3)*60);ctx.lineTo(W,H);ctx.lineTo(0,H);ctx.fill();ctx.restore();
  ctx.save();ctx.strokeStyle='rgba(26,26,26,.55)';ctx.lineWidth=14;ctx.lineCap='round';ctx.beginPath();ctx.moveTo(60,70);ctx.bezierCurveTo(320,40,700,100,1020,60);ctx.stroke();ctx.restore();
  ctx.fillStyle='#b3202a';ctx.fillRect(930,1640,70,70);ctx.fillStyle='#efe9dc';ctx.font='900 40px Inter';ctx.textAlign='center';ctx.fillText('金',965,1688)};
ST.panel=(x,y,w,h,col)=>{ctx.save();ctx.fillStyle='rgba(250,246,236,.94)';RR(x,y,w,h,10);ctx.fill();ctx.lineWidth=4;ctx.strokeStyle='#1a1a1a';ctx.beginPath();ctx.moveTo(x+8,y+4);ctx.lineTo(x+w-8,y+8);ctx.lineTo(x+w-4,y+h-6);ctx.lineTo(x+6,y+h-4);ctx.closePath();ctx.stroke();ctx.fillStyle=col;ctx.fillRect(x+8,y+10,12,h-20);ctx.restore()};"""

BG_BLUEPRINT = """ST.bg=t=>{ctx.fillStyle='#0b3a6b';ctx.fillRect(0,0,W,H);ctx.strokeStyle='rgba(160,225,255,.13)';ctx.lineWidth=1.5;for(let x=0;x<=W;x+=36){ctx.beginPath();ctx.moveTo(x,0);ctx.lineTo(x,H);ctx.stroke()}for(let y=0;y<=H;y+=36){ctx.beginPath();ctx.moveTo(0,y);ctx.lineTo(W,y);ctx.stroke()}
  ctx.strokeStyle='rgba(160,225,255,.30)';ctx.lineWidth=2.5;for(let x=0;x<=W;x+=180){ctx.beginPath();ctx.moveTo(x,0);ctx.lineTo(x,H);ctx.stroke()}for(let y=0;y<=H;y+=180){ctx.beginPath();ctx.moveTo(0,y);ctx.lineTo(W,y);ctx.stroke()}
  ctx.save();ctx.strokeStyle='#7fe3ff';ctx.lineWidth=5;ctx.strokeRect(30,30,W-60,H-60);ctx.setLineDash([16,10]);ctx.globalAlpha=.5;ctx.strokeRect(50,50,W-100,H-100);ctx.restore();
  ctx.save();ctx.globalAlpha=.30;ctx.strokeStyle='#7fe3ff';ctx.lineWidth=4;ctx.beginPath();for(let i=0;i<=22;i++){const x=i*50,y=1700-Math.sin(i*.6+t*.7)*60-i*9;i?ctx.lineTo(x,y):ctx.moveTo(x,y)}ctx.stroke();ctx.restore();
  ctx.fillStyle='#7fe3ff';ctx.font='800 24px Inter';ctx.textAlign='right';ctx.fillText('PLANO · ESC. 1:1 · @forexmry',W-70,H-70);ctx.textAlign='center'};
ST.panel=(x,y,w,h,col)=>{ctx.save();ctx.fillStyle='rgba(6,40,80,.92)';ctx.fillRect(x,y,w,h);ctx.lineWidth=3;ctx.strokeStyle=col;ctx.strokeRect(x,y,w,h);ctx.fillStyle=col;[[x,y],[x+w,y],[x,y+h],[x+w,y+h]].forEach(([a,b])=>{ctx.fillRect(a-7,b-7,14,14)});ctx.restore()};"""

BG_PAPERCUT = """ST.bg=t=>{const g=ctx.createLinearGradient(0,0,0,H);g.addColorStop(0,'#0f4c5c');g.addColorStop(1,'#0a2f3a');ctx.fillStyle=g;ctx.fillRect(0,0,W,H);
  const hill=(base,amp,ph,col,sh)=>{ctx.save();ctx.shadowColor='rgba(0,0,0,.45)';ctx.shadowBlur=sh;ctx.shadowOffsetY=-6;ctx.fillStyle=col;ctx.beginPath();ctx.moveTo(0,H);for(let x=0;x<=W;x+=20)ctx.lineTo(x,base-Math.sin(x*.006+ph)*amp-Math.sin(x*.017+ph*2)*amp*.35);ctx.lineTo(W,H);ctx.closePath();ctx.fill();ctx.restore()};
  ctx.save();ctx.fillStyle='#ffb703';ctx.beginPath();ctx.arc(880,1420,90,0,7);ctx.fill();ctx.fillStyle='rgba(255,183,3,.20)';ctx.beginPath();ctx.arc(880,1420,130,0,7);ctx.fill();ctx.restore();hill(1380+Math.sin(t*.4)*6,90,0.5,'#1b6b7a',18);hill(1500,80,2,'#fb8500',20);hill(1600,70,4,'#ffb703',22);hill(1720,60,1,'#8ecae6',24);
};
ST.panel=(x,y,w,h,col)=>{ctx.save();ctx.shadowColor='rgba(0,0,0,.5)';ctx.shadowBlur=18;ctx.shadowOffsetY=8;ctx.fillStyle='rgba(2,48,71,.94)';RR(x,y,w,h,22);ctx.fill();ctx.restore();ctx.save();ctx.lineWidth=6;ctx.strokeStyle=col;RR(x,y,w,h,22);ctx.stroke();ctx.restore()};"""

g.THEMES.update({
 'ambar': mk(11, 'terminal ámbar sobre negro con barrido de fósforo', BG_AMBAR, ["#ffb000","#ff7a1a","#ffd966","#fff1c9"], '#ffd98a', '#b98a2c', '#ffb000', '#1a1200', '#0b0700',
   "rgba(11,7,0,.96)","#ffb000","#ffd98a","#0b0700","#ffd98a","#ffb000","#ffb000","#0b0700",'rgba(11,7,0,.88)',0,2,3,'#b98a2c',1,'#0b0700'),
 'periodico': mk(12, 'periódico de época sepia con tinta, burdeos y azul', BG_PERIODICO, ["#8b1a1a","#1d3557","#7a5a12","#2b2b2b"], '#1a1510', '#5a4d36', '#8b1a1a', '#f6eed8', '#1a1510',
   "rgba(246,238,216,.97)","#8b1a1a","#1a1510","#1a1510","#f6eed8","#c9a227","#c9a227","#1a1510",'rgba(246,238,216,.92)',0,1,2,'#5a4d36',1,'#f6eed8'),
 'suizo': mk(13, 'retícula suiza blanca con rojo y negro', BG_SUIZO, ["#e30613","#111111","#ff6b00","#0b57d0"], '#111111', '#555555', '#e30613', '#ffffff', '#111111',
   "rgba(255,255,255,.97)","#e30613","#111111","#111111","#ffffff","#ff4d57","#ff4d57","#ffffff",'rgba(255,255,255,.93)',0,1,2,'#555555',0,'#ffffff'),
 'lingotes': mk(14, 'bóveda negra con lingotes de oro', BG_LINGOTES, ["#ffcc33","#e6a817","#ffe08a","#c8d0d8"], '#fff6dc', '#c9b27a', '#ffcc33', '#16100a', '#080604',
   "rgba(8,6,4,.96)","#ffcc33","#fff6dc","#080604","#fff6dc","#ffcc33","#ffcc33","#080604",'rgba(8,6,4,.88)',0,2,3,'#c9b27a',0,'#080604'),
 'sumie': mk(15, 'papel de arroz con pinceladas de tinta y sello rojo', BG_SUMIE, ["#b3202a","#1a1a1a","#3d5a73","#b3202a"], '#1a1a1a', '#5b5648', '#b3202a', '#faf6ec', '#1a1a1a',
   "rgba(250,246,236,.97)","#b3202a","#1a1a1a","#1a1a1a","#faf6ec","#e3a93f","#e3a93f","#1a1a1a",'rgba(250,246,236,.92)',0,1,2,'#5b5648',0,'#faf6ec'),
 'blueprint': mk(16, 'plano azul con cuadrícula cian y cotas', BG_BLUEPRINT, ["#7fe3ff","#ffffff","#ffd166","#9be564"], '#e8f6ff', '#9cc7e6', '#7fe3ff', '#062850', '#062850',
   "rgba(6,40,80,.97)","#7fe3ff","#e8f6ff","#062850","#e8f6ff","#7fe3ff","#7fe3ff","#062850",'rgba(6,40,80,.88)',0,2,3,'#9cc7e6',2,'#062850'),
 'papercut': mk(17, 'capas de papel recortado turquesa, naranja y ámbar', BG_PAPERCUT, ["#ffb703","#8ecae6","#fb8500","#ffffff"], '#ffffff', '#a8d4de', '#ffb703', '#023047', '#0a2f3a',
   "rgba(2,48,71,.97)","#ffb703","#ffffff","#0a2f3a","#ffffff","#ffb703","#ffb703","#0a2f3a",'rgba(2,48,71,.88)',0,1,2,'#a8d4de',0,'#023047'),
})

R = []
# ---------------------------------------------------------------- 1. Credit Suisse
R.append(dict(n=228, scene=298, slug='credit_suisse_at1', page='v228_ambar_credit_suisse_at1', theme='ambar', hora='2026-11-17_0600', bpm=104, prog=[[45,"m"],[41,"M"],[48,"m"],[43,"M"]],
 name='CreditSuisseAT1', hook='19 MARZO 2023: CHF 16.000 M EN BONOS AT1 DE CREDIT SUISSE VALEN CERO',
 H0=dict(l='CREDIT SUISSE · UBS · 2023',b='CHF 16.000 M',s=170,u='EN BONOS AT1, ANULADOS A CERO',c=['19 de marzo de 2023 (domingo)','Los accionistas sí recibieron acciones']),
 B=[("EL ACUERDO","CHF 3.000 M",190,"lo que UBS pagó en acciones por Credit Suisse",36,["Anunciado el 19 de marzo de 2023","≈ US$ 3.200 M, todo en acciones","≈ CHF 0,76 por acción"],"fuente: Fortune (Bloomberg); Wikipedia"),
    ("LOS BONOS AT1","CHF 16.000 M",160,"≈ US$ 17.000 M anulados por completo",38,["Con autorización de FINMA, el regulador","Valor final: cero","Deuda de capital de alto riesgo"],"fuente: Fortune (Bloomberg); Wikipedia"),
    ("LA SORPRESA","BONOS < ACCIONES",90,"los bonistas perdieron todo; los accionistas, no",36,["Lo habitual: pierden primero las acciones","Aquí los AT1 se anularon antes","Un gestor: «no tiene sentido»"],"fuente: Fortune (Bloomberg)"),
    ("LA ACCIÓN","−59 %",270,"de CHF 1,86 (17 mar.) a 0,76 (19 mar.), cálculo propio",34,["Cayó hasta 31 % el 15 de marzo","SNB: línea de emergencia de CHF 50.000 M","Cifras aproximadas"],"fuente: Wikipedia; cálculo propio"),
    ("EL DOMINGO","GAP",300,"se anunció con el mercado cerrado",38,["19 de marzo de 2023 fue domingo","El lunes el precio puede abrir con salto","Un stop no garantiza el precio de salida"],"fuente: calendario; Fortune")],
 END=("Un domingo puede mover el lunes","Cuida el riesgo de gap"),
 subs=[("El 19 de marzo de 2023, UBS compró Credit Suisse y ≈ CHF 16.000 millones en bonos valieron cero.","El diecinueve de marzo de dos mil veintitrés, UBS compró Credit Suisse y dieciséis mil millones de francos en bonos valieron cero."),
  ("UBS pagó CHF 3.000 millones en acciones, ≈ US$ 3.200 millones, por todo Credit Suisse.","UBS pagó tres mil millones de francos suizos en acciones, cerca de tres mil doscientos millones de dólares."),
  ("Los bonos AT1, ≈ CHF 16.000 millones, se anularon con autorización del regulador suizo, FINMA.","Los bonos AT1, cerca de dieciséis mil millones de francos, se anularon con autorización del regulador suizo."),
  ("Lo normal es que pierdan primero los accionistas. Aquí recibieron acciones de UBS y los bonistas, cero.","Lo normal es que pierdan primero los accionistas. Aquí recibieron acciones de UBS y los bonistas, cero."),
  ("La acción pasó de CHF 1,86 a 0,76 entre el 17 y el 19 de marzo: ≈ −59 %, cálculo propio.","La acción pasó de uno coma ochenta y seis a cero coma setenta y seis francos del diecisiete al diecinueve de marzo."),
  ("Se anunció un domingo, con el mercado cerrado. Un stop no garantiza el precio si hay salto. Fuentes: Fortune y Wikipedia. Educativo.","Se anunció un domingo, con el mercado cerrado. Un stop no garantiza el precio si hay un salto. Fuentes: Fortune y Wikipedia. Contenido educativo."),
  ("Para tu robot: un domingo puede mover el lunes. Cuida el riesgo de gap.","Para tu robot: un domingo puede mover el lunes. Cuida el riesgo de gap.")],
 cover=("UN DOMINGO · 19 MAR. 2023","CHF 16.000 M","DE BONOS, A CERO","mientras los accionistas recibían acciones de UBS","VER QUÉ PASÓ →")))

# ---------------------------------------------------------------- 2. OBV
R.append(dict(n=229, scene=299, slug='obv_granville', page='v229_periodico_obv_granville', theme='periodico', hora='2026-11-17_0930', bpm=112, prog=[[40,"m"],[36,"M"],[43,"m"],[38,"M"]],
 name='OBVGranville', hook='OBV: EL VOLUMEN QUE SUMA O RESTA SEGÚN EL CIERRE DE CADA DÍA',
 H0=dict(l='INDICADORES · OBV',b='+ / −',s=300,u='VOLUMEN ACUMULADO SEGÚN EL CIERRE',c=['Lo popularizó Joe Granville','En su libro de 1963']),
 B=[("QUIÉN LO POPULARIZÓ","1963",270,"Granville, «New Key to Stock Market Profits»",34,["Antes: «continuous volume» (Woods y Vignola)","Idea: el volumen se mueve antes","Es un indicador acumulado"],"fuente: StockCharts; Wikipedia"),
    ("LA REGLA","SUMA / RESTA",110,"según el cierre frente al cierre anterior",38,["Cierre sube: + volumen del día","Cierre baja: − volumen del día","Cierre igual: no cambia"],"fuente: StockCharts"),
    ("EJEMPLO ILUSTRATIVO","170",270,"desde 0: volúmenes 100 y 150 al alza, 80 a la baja",32,["0 + 100 = 100","100 + 150 = 250","250 − 80 = 170"],"datos ilustrativos; aritmética propia"),
    ("DIVERGENCIAS","OBV vs PRECIO",90,"si no coinciden, puede venir un giro",38,["OBV sube y el precio baja: alcista","OBV baja y el precio sube: bajista","Es un aviso, no una certeza"],"fuente: StockCharts"),
    ("CAUTELAS","SU TENDENCIA",130,"la cifra absoluta del OBV no importa",36,["Depende del punto de partida","Un pico de volumen lo desajusta","En forex spot suele ser volumen de ticks"],"fuente: StockCharts; Wikipedia; nota propia")],
 END=("El volumen confirma, no decide","Pruébalo en un backtest"),
 subs=[("El OBV suma o resta el volumen según el cierre de cada día.","El O be uve suma o resta el volumen según el cierre de cada día."),
  ("Lo popularizó Joe Granville en su libro de 1963. Antes se llamaba «continuous volume».","Lo popularizó Joe Granville en su libro de mil novecientos sesenta y tres. Antes se llamaba volumen continuo."),
  ("Si el cierre sube, suma el volumen del día; si baja, lo resta; si es igual, no cambia.","Si el cierre sube, suma el volumen del día; si baja, lo resta; si es igual, no cambia."),
  ("Ejemplo ilustrativo: volúmenes 100 y 150 al alza y 80 a la baja dan un OBV de 170.","Ejemplo ilustrativo: volúmenes de cien y ciento cincuenta al alza y ochenta a la baja dan un O be uve de ciento setenta."),
  ("Si el OBV sube y el precio baja, hay divergencia alcista; al revés, bajista. Es un aviso, no una certeza.","Si el O be uve sube y el precio baja, hay divergencia alcista; al revés, bajista. Es un aviso, no una certeza."),
  ("Importa su tendencia, no su cifra. Fuentes: StockCharts y Wikipedia. Contenido educativo, no es asesoría.","Importa su tendencia, no su cifra. Fuentes: StockCharts y Wikipedia. Contenido educativo."),
  ("Para tu robot: el volumen confirma, no decide. Pruébalo en un backtest.","Para tu robot: el volumen confirma, no decide. Pruébalo en un backtest.")],
 cover=("INDICADOR OBV","1963","EL VOLUMEN QUE SUMA Y RESTA","la regla de Granville en 3 pasos","VER CÓMO →")))

# ---------------------------------------------------------------- 3. Tenedores de Treasuries
R.append(dict(n=230, scene=300, slug='tenedores_treasuries', page='v230_suizo_tenedores_treasuries', theme='suizo', hora='2026-11-17_1300', bpm=120, prog=[[43,"m"],[39,"M"],[46,"m"],[41,"M"]],
 name='TenedoresTreasuries', hook='AGOSTO 2026: JAPÓN SIGUE PRIMERO CON US$ 1,07 BILLONES EN TREASURIES',
 H0=dict(l='TESORO DE EE. UU. · AGOSTO 2026',b='US$ 9,33 BILL.',s=190,u='TOTAL EN MANOS EXTRANJERAS',c=['Ranking por país de custodia','Datos del Tesoro (TIC, Tabla 5)']),
 B=[("N.º 1 · JAPÓN","1.068",270,"miles de millones de US$ (≈ 1,07 billones)",36,["Cayó desde 1.239 en febrero","≈ −14 % en seis meses (cálculo propio)","Sigue siendo el mayor"],"fuente: Tesoro de EE. UU. (TIC, Tabla 5); Wolf Street"),
    ("N.º 2 · REINO UNIDO","1.010",270,"miles de millones de US$ (1.009,5)",36,["Subió desde 897 en febrero","Solo ≈ 59.000 M por debajo de Japón","Centro financiero: país de custodia"],"fuente: TIC, Tabla 5; Wolf Street"),
    ("N.º 3 · CHINA","591",270,"miles de millones de US$ (China continental)",36,["Eran ≈ 618 en julio de 2026","≈ 700 en agosto de 2025","≈ −16 % en un año (cálculo propio)"],"fuente: TIC, Tabla 5; 24/7 Wall St"),
    ("N.º 4 Y N.º 5","BÉLGICA · CANADÁ",80,"490,5 y 464,6 miles de millones de US$",36,["Bélgica: ≈ 490","Canadá: ≈ 465","6.º: Islas Caimán, 463,0"],"fuente: TIC, Tabla 5"),
    ("LA ADVERTENCIA","CUSTODIA",200,"es país de custodia, no dueño final",38,["Bélgica o Caimán: centros financieros","Pueden guardar bonos de otros","Se cita que Caimán está subestimado"],"fuente: TIC; Wolf Street")],
 END=("Las cifras cambian cada mes","Contrasta siempre la fecha del dato"),
 subs=[("En agosto de 2026, Japón seguía primero con ≈ US$ 1,07 billones en bonos del Tesoro de EE. UU.","En agosto de dos mil veintiséis, Japón seguía primero con un billón sesenta y ocho mil millones de dólares en bonos del Tesoro."),
  ("Japón: ≈ 1.068 miles de millones de dólares, ≈ −14 % frente a los 1.239 de febrero (cálculo propio).","Japón tiene un billón sesenta y ocho mil millones de dólares, cerca de catorce por ciento menos que en febrero."),
  ("Reino Unido: ≈ 1.010 miles de millones, a solo ≈ 59.000 millones de Japón.","El Reino Unido tiene un billón diez mil millones, a solo cincuenta y nueve mil millones de Japón."),
  ("China continental: ≈ 591 miles de millones, ≈ −16 % frente a los ≈ 700 de agosto de 2025.","China continental tiene quinientos noventa y un mil millones, cerca de dieciséis por ciento menos que hace un año."),
  ("Bélgica ≈ 490 y Canadá ≈ 465 miles de millones. Total extranjero: ≈ US$ 9,33 billones.","Bélgica tiene cuatrocientos noventa mil millones y Canadá cuatrocientos sesenta y cinco. El total extranjero es de nueve coma tres tres billones."),
  ("Es país de custodia, no dueño final. Fuentes: Tesoro de EE. UU. y Wolf Street. Contenido educativo.","Es el país de custodia, no el dueño final. Fuentes: Tesoro de Estados Unidos y Wolf Street. Contenido educativo, no es asesoría."),
  ("Para tu robot: las cifras cambian cada mes. Contrasta siempre la fecha del dato.","Para tu robot: las cifras cambian cada mes. Contrasta siempre la fecha del dato.")],
 cover=("TESORO DE EE. UU. · AGO. 2026","US$ 1,07","BILLONES · JAPÓN LIDERA","ranking de los 5 mayores tenedores extranjeros","VER EL RANKING →")))

# ---------------------------------------------------------------- 4. MQL5 modos de llenado
R.append(dict(n=231, scene=301, slug='modos_llenado_mql5', page='v231_lingotes_modos_llenado_mql5', theme='lingotes', hora='2026-11-17_1630', bpm=116, prog=[[41,"m"],[45,"M"],[48,"m"],[43,"M"]],
 name='ModosLlenadoMQL5', hook='MQL5: FOK, IOC O RETURN: CÓMO SE LLENA LA ORDEN DE TU ROBOT',
 H0=dict(l='ROBOTS · MQL5 · type_filling',b='FOK·IOC·RETURN',s=130,u='TRES MODOS DE LLENADO',c=['Campo type_filling de la solicitud','Documentación oficial de MQL5']),
 B=[("FOK · FILL OR KILL","TODO O NADA",150,"solo se ejecuta el volumen completo",38,["Sin todo el volumen, no se ejecuta","Puede juntar varias ofertas","No hay llenado parcial"],"fuente: documentación oficial de MQL5"),
    ("IOC · IMMEDIATE OR CANCEL","LO DISPONIBLE",140,"toma el máximo volumen disponible, ya",36,["Ejecuta dentro de los límites pedidos","Lo que no se llena, se cancela","Permite llenado parcial"],"fuente: documentación oficial de MQL5"),
    ("RETURN","SIGUE EN COLA",150,"el resto no se cancela: se sigue procesando",36,["Con llenado parcial, queda el resto","Siempre disponible, salvo ejecución a mercado","No se permite en ejecución a mercado"],"fuente: documentación oficial de MQL5"),
    ("¿CUÁL SOPORTA?","SYMBOL_FILLING_MODE",80,"banderas del símbolo para FOK e IOC",38,["Se lee con SymbolInfoInteger()","RETURN no es bandera: depende del modo","El bróker define el modo de ejecución"],"fuente: documentación oficial de MQL5"),
    ("PENDIENTES","RETURN",270,"las órdenes pendientes usan RETURN",38,["No se ejecutan al enviarlas","Sirve sin importar el tipo de ejecución","Lee el modo antes de enviar a mercado"],"fuente: documentación oficial de MQL5")],
 END=("Elige un modo que el símbolo permita","Léelo del símbolo, no lo supongas"),
 subs=[("Tu robot en MQL5 debe elegir cómo se llena su orden: FOK, IOC o RETURN.","Tu robot en eme ele cinco debe elegir cómo se llena su orden: efe o ka, i o ce, o return."),
  ("FOK, Fill or Kill: se ejecuta todo el volumen pedido o no se ejecuta nada.","Efe o ka significa todo o nada: se ejecuta todo el volumen pedido o no se ejecuta nada."),
  ("IOC, Immediate or Cancel: toma el máximo volumen disponible y cancela el resto.","I o ce toma el máximo volumen disponible dentro de los límites y cancela el resto."),
  ("RETURN: si el llenado es parcial, el resto sigue en proceso. No se permite en ejecución a mercado.","Return: si el llenado es parcial, el resto no se cancela y sigue en proceso. No se permite en ejecución a mercado."),
  ("El símbolo indica qué admite en SYMBOL_FILLING_MODE. Léelo con SymbolInfoInteger antes de enviar.","El símbolo indica qué admite en symbol filling mode. Léelo con symbol info integer antes de enviar la orden."),
  ("Las pendientes usan RETURN. Fuente: documentación oficial de MQL5. Contenido educativo, no es asesoría.","Las pendientes usan return. Fuente: documentación oficial de eme ele cinco. Contenido educativo."),
  ("Para tu robot: elige un modo que el símbolo permita y léelo, no lo supongas.","Para tu robot: elige un modo que el símbolo permita y léelo, no lo supongas.")],
 cover=("ROBOTS · MQL5","FOK·IOC","¿Y RETURN?","tres modos para llenar la orden de tu robot","VER LOS 3 MODOS →")))

# ---------------------------------------------------------------- 5. Repo sept. 2019
R.append(dict(n=232, scene=302, slug='repo_2019', page='v232_sumie_repo_2019', theme='sumie', hora='2026-11-17_2000', bpm=100, prog=[[38,"m"],[43,"M"],[41,"m"],[36,"M"]],
 name='Repo2019', hook='17 SEPT. 2019: LA TASA SOFR PASÓ DE 2,43 % A 5,25 % EN UN DÍA',
 H0=dict(l='MERCADO DE REPO · EE. UU.',b='2,43 → 5,25 %',s=150,u='LA TASA SOFR EN UN SOLO DÍA',c=['16 y 17 de septiembre de 2019','Intervino la Fed de Nueva York']),
 B=[("¿QUÉ ES UN REPO?","PRÉSTAMO",200,"a corto plazo, garantizado con valores",38,["Se vende un bono y se recompra","En esencia: un préstamo con garantía","Su tasa mide el costo de una noche"],"fuente: Wikipedia; Chicago Fed"),
    ("EL SALTO","5,25 %",270,"SOFR el 17 de sept., desde 2,43 % el día anterior",36,["Algunas operaciones: 9 % a 10 %","Rango de la Fed: 2,00 %–2,25 %","Tasa efectiva: 2,30 %"],"fuente: Wikipedia; Chicago Fed (9 % vs 10 %: fuentes difieren)"),
    ("LAS CAUSAS","> US$ 100.000 M",110,"salieron de cuentas en pocos días por impuestos",34,["Liquidación de Treasuries: ≈ US$ 54.000 M","Reservas bancarias ≈ US$ 1,4 billones","Nivel más bajo desde 2011–2012"],"fuente: Wikipedia; Chicago Fed"),
    ("LA RESPUESTA","US$ 75.000 M",150,"oferta de repo overnight de la Fed de Nueva York",36,["17 sept.: se tomaron US$ 53.000 M","18 sept.: se tomaron los 75.000 M","Operaciones diarias hasta el 10 de oct."],"fuente: Wikipedia; Chicago Fed"),
    ("LA LECCIÓN","LIQUIDEZ",230,"las tasas pueden saltar sin que la Fed las mueva",36,["Fed funds seguía en 2,00 %–2,25 %","El 19 sept. el rango bajó a 1,75 %–2,00 %","El dinero de corto plazo también tiene riesgo"],"fuente: Chicago Fed; Wikipedia")],
 END=("La liquidez puede secarse un día","Cuida el apalancamiento"),
 subs=[("El 17 de septiembre de 2019, la tasa SOFR saltó de 2,43 % a 5,25 % en un solo día.","El diecisiete de septiembre de dos mil diecinueve, la tasa de repo saltó de dos coma cuarenta y tres a cinco coma veinticinco por ciento."),
  ("Un repo es un préstamo a corto plazo garantizado con valores, como bonos del Tesoro.","Un repo es un préstamo a corto plazo garantizado con valores, como bonos del Tesoro."),
  ("Algunas operaciones llegaron a entre 9 % y 10 % según la fuente, con la tasa de la Fed en 2,00–2,25 %.","Algunas operaciones llegaron a entre nueve y diez por ciento, con la tasa de la Fed entre dos y dos coma veinticinco."),
  ("Hubo pago de impuestos corporativos, liquidación de Treasuries por ≈ US$ 54.000 millones y reservas bancarias en mínimos.","Hubo pago de impuestos corporativos, liquidación de bonos del Tesoro por cincuenta y cuatro mil millones y reservas bancarias bajas."),
  ("La Fed de Nueva York ofreció hasta US$ 75.000 millones. Se tomaron 53.000 el 17 de septiembre.","La Fed de Nueva York ofreció hasta setenta y cinco mil millones. Se tomaron cincuenta y tres mil el diecisiete de septiembre."),
  ("La liquidez de corto plazo también puede secarse. Fuentes: Wikipedia y Chicago Fed. Contenido educativo, no es asesoría.","La liquidez de corto plazo también puede secarse. Fuentes: Wikipedia y Chicago Fed. Contenido educativo."),
  ("Para tu robot: la liquidez puede secarse en un día. Cuida el apalancamiento.","Para tu robot: la liquidez puede secarse en un día. Cuida el apalancamiento.")],
 cover=("REPO · 17 SEPT. 2019","5,25 %","EN UN SOLO DÍA","más del doble de un día para otro; la Fed intervino","VER QUÉ PASÓ →")))

# ---------------------------------------------------------------- 6. Larry Williams
R.append(dict(n=233, scene=303, slug='larry_williams', page='v233_blueprint_larry_williams', theme='blueprint', hora='2026-11-17_2330', bpm=110, prog=[[40,"m"],[43,"M"],[36,"m"],[41,"M"]],
 name='LarryWilliams', hook='LARRY WILLIAMS: US$ 10.000 A ≈ US$ 1,1 MILLONES EN 12 MESES, EN 1987',
 H0=dict(l='PERSONAS · LARRY WILLIAMS · 1987',b='≈ +11.000 %',s=200,u='EN UN CONCURSO DE FUTUROS',c=['Capital inicial: US$ 10.000','Cifras según Wikipedia y Benzinga']),
 B=[("EL CONCURSO","12 MESES",190,"Robbins World Cup de futuros, 1987",36,["Capital inicial: US$ 10.000","Terminó cerca de US$ 1,1 millones","Cifra citada: 11.376 % (otra: ≈ 11.000 %)"],"fuente: Wikipedia (espejo); Benzinga; las cifras difieren"),
    ("EL CAMINO","−66 %",270,"caída desde el pico, según su propio relato",34,["Llegó a ≈ US$ 2,2 millones","Cayó a ≈ US$ 750.000","Terminó en ≈ US$ 1,1 millones"],"fuente: Benzinga (entrevista); −66 % cálculo propio"),
    ("SU ESTILO ENTONCES","AGRESIVO",190,"él mismo lo llamó manejo de dinero «agresivo»",34,["Mucho capital en casi cada apuesta","Su operación promedio: 12 a 15 días","No es un modelo para copiar"],"fuente: Benzinga (entrevista)"),
    ("SUS HERRAMIENTAS","%R",300,"Williams %R, Ultimate Oscillator e índices COT",36,["Libro de 1979 sobre materias primas","Autor de ≈ 11 libros","Williams %R: ≈ 1966 (una sola fuente)"],"fuente: Wikipedia (espejo); Complete Trader's Edge"),
    ("LA LECCIÓN","RIESGO",270,"un resultado extremo vino con una caída extrema",36,["El pasado no garantiza nada","Un concurso no es una cuenta real","Mide la caída, no solo la ganancia"],"análisis propio")],
 END=("Mira la caída máxima, no solo la ganancia","Prueba tu robot en demo"),
 subs=[("En 1987, Larry Williams convirtió US$ 10.000 en ≈ US$ 1,1 millones en un concurso de 12 meses.","En mil novecientos ochenta y siete, Larry Williams convirtió diez mil dólares en cerca de un millón cien mil en un concurso de doce meses."),
  ("Fue el Robbins World Cup de futuros. Las fuentes dan entre ≈ 11.000 % y 11.376 % de retorno.","Fue el Robbins World Cup de futuros. Las fuentes hablan de más de once mil por ciento de retorno."),
  ("Según su relato, llegó a ≈ US$ 2,2 millones, cayó a ≈ 750.000 y cerró en ≈ 1,1 millones: ≈ −66 % en el camino.","Según su relato, llegó a dos coma dos millones, cayó a setecientos cincuenta mil y cerró en cerca de un millón cien mil: menos sesenta y seis por ciento en el camino."),
  ("Él mismo describió un manejo de dinero muy agresivo, con mucho capital en casi cada apuesta.","Él mismo describió un manejo de dinero muy agresivo, con mucho capital en casi cada apuesta."),
  ("Creó herramientas como Williams %R y el Ultimate Oscillator, y escribió ≈ 11 libros.","Creó herramientas como Williams porciento erre y el Ultimate Oscillator, y escribió cerca de once libros."),
  ("Un concurso no es una cuenta real y el pasado no garantiza nada. Fuentes: Wikipedia y Benzinga. Contenido educativo.","Un concurso no es una cuenta real y el pasado no garantiza nada. Fuentes: Wikipedia y Benzinga. Contenido educativo, no es asesoría."),
  ("Para tu robot: mira la caída máxima, no solo la ganancia.","Para tu robot: mira la caída máxima, no solo la ganancia.")],
 cover=("LARRY WILLIAMS · 1987","−66 %","EN EL CAMINO A +11.000 %","de US$ 10.000 a ≈ 1,1 M, con una caída de dos tercios","VER LA HISTORIA →")))

# ---------------------------------------------------------------- 7. Sumitomo cobre 1996
R.append(dict(n=234, scene=304, slug='sumitomo_cobre_1996', page='v234_papercut_sumitomo_cobre_1996', theme='papercut', hora='2026-11-18_0300', bpm=106, prog=[[41,"m"],[45,"M"],[43,"m"],[38,"M"]],
 name='SumitomoCobre', hook='JUNIO 1996: SUMITOMO ANUNCIA US$ 1.800 M DE PÉRDIDAS EN COBRE',
 H0=dict(l='SUMITOMO · COBRE · LME · 1996',b='US$ 1.800 M',s=170,u='PÉRDIDAS ANUNCIADAS EL 13 DE JUNIO',c=['Un solo operador: Yasuo Hamanaka','Operaciones no autorizadas ≈ 10 años']),
 B=[("EL OPERADOR","≈ 10 AÑOS",190,"de operaciones no autorizadas con cobre",36,["Yasuo Hamanaka, jefe de cobre","Contratos de cobre en la LME","Registros falsificados"],"fuente: Wikipedia; Maclean's (Canadian Encyclopedia)"),
    ("LA POSICIÓN","93 %",300,"de los warrants de cobre de la LME (24 nov. 1995)",34,["Intentó controlar el mercado","Apodo: «Mr. Five Per Cent»","La cifra del 93 % es de una sola fuente"],"fuente: Wikipedia; Maclean's"),
    ("LA CAÍDA","−36 %",270,"el cobre: de ≈ 2.800 (mayo) a ≈ 1.800 (25 jun. 1996)",32,["Cálculo propio sobre cifras de Wikipedia","La fuente no indica unidades","Maclean's: −11 % en una semana"],"fuente: Wikipedia; Maclean's"),
    ("LAS PÉRDIDAS","US$ 2.600 M",150,"cifra final según Wikipedia (Maclean's: 2.400)",34,["Anuncio inicial: US$ 1.800 M","Más ≈ US$ 200 M por demandas","Acuerdo con la CFTC: US$ 150 M"],"fuente: Wikipedia; Maclean's; Fed (18 sep. 1996)"),
    ("EL FINAL","8 AÑOS",270,"de cárcel: Tokio, 1997, fraude y falsificación",34,["No lo condenaron por manipular el mercado","Una persona concentró demasiado poder","Faltó control de riesgo interno"],"fuente: Wikipedia")],
 END=("Una posición sin límites es un riesgo","Pon límites a tu robot"),
 subs=[("En junio de 1996, Sumitomo anunció pérdidas de ≈ US$ 1.800 millones por un operador de cobre.","En junio de mil novecientos noventa y seis, Sumitomo anunció pérdidas de mil ochocientos millones de dólares por un operador de cobre."),
  ("Yasuo Hamanaka, jefe de cobre, hizo operaciones no autorizadas cerca de diez años y falsificó registros.","Yasuo Hamanaka, jefe de cobre, hizo operaciones no autorizadas durante cerca de diez años y falsificó registros."),
  ("En noviembre de 1995 llegó a tener el 93 % de los warrants de cobre de la LME, según Wikipedia.","En noviembre de mil novecientos noventa y cinco llegó a tener el noventa y tres por ciento de los warrants de cobre de la bolsa de Londres, según Wikipedia."),
  ("El cobre cayó de ≈ 2.800 a ≈ 1.800 entre mayo y el 25 de junio de 1996: ≈ −36 %, cálculo propio.","El cobre cayó de dos mil ochocientos a mil ochocientos entre mayo y el veinticinco de junio de mil novecientos noventa y seis: cerca de treinta y seis por ciento."),
  ("Las pérdidas finales fueron ≈ US$ 2.600 millones según Wikipedia; Maclean's habló de 2.400. Cifras aproximadas.","Las pérdidas finales fueron de unos dos mil seiscientos millones de dólares según Wikipedia; Maclean's habló de dos mil cuatrocientos. Cifras aproximadas."),
  ("En 1997 lo condenaron en Tokio a 8 años por fraude y falsificación. Fuentes: Wikipedia y Maclean's. Educativo.","En mil novecientos noventa y siete lo condenaron en Tokio a ocho años por fraude y falsificación. Fuentes: Wikipedia y Maclean's. Contenido educativo."),
  ("Para tu robot: una posición sin límites es un riesgo. Ponle límites.","Para tu robot: una posición sin límites es un riesgo. Ponle límites.")],
 cover=("SUMITOMO · 1996","US$ 1.800 M","UN SOLO OPERADOR DE COBRE","la pérdida que salió a la luz en junio de 1996","VER QUÉ PASÓ →")))

if __name__ == '__main__':
    sel = [int(x) for x in sys.argv[1:]]
    for r in R:
        if sel and r['n'] not in sel: continue
        open(os.path.join(HERE, r['page'] + '.html'), 'w').write(g.build(r))
        print('ok', r['page'], r['scene'])
