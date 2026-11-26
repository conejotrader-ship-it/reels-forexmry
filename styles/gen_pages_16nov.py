#!/usr/bin/env python3
"""Genera las páginas v221–v227 (reels del 16 nov 2026) con la plantilla std/h0/b6 sobre kit2/kit3.
Uso: python3 gen_pages_16nov.py [n1 n2 ...]  (por defecto todas)"""
import json, sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
EVB = [[6.2,"wipe"],[8.0,"ding"],[13.4,"wipe"],[15.2,"ding"],[20.4,"wipe"],[22.2,"ding"],[28.2,"wipe"],[30.0,"ding"],[35.0,"wipe"],[36.8,"ding"],[43.4,"wipe"],[45.2,"ding"],[51.0,"ding"],[52.2,"ding"],[53.4,"ding"],[54.6,"ding"],[56.2,"cta"]]
WIN = [(0.2,6.0),(6.4,13.4),(13.6,20.4),(20.6,28.2),(28.4,35.0),(35.2,43.4),(43.6,49.6)]
OUTRO = [49.8,55.9,"Sígueme @forexmry, activa las notificaciones, únete al grupo de Telegram y visita www.trustgoldmry.com","Sígueme, activa las notificaciones, únete a Telegram y visita trust gold eme erre ye punto com."]
CTA = [56.2,59.8,"Robot Trust Gold Mr. Y. Link en bio.","Robot Trust Gold, Míster Y. Link en bio."]

# ---------------- TEMAS (un fondo y un panel distintos por estilo) ----------------
def bg_pizarra():
    return """ST.bg=t=>{const g=ctx.createLinearGradient(0,0,W,H);g.addColorStop(0,'#14352c');g.addColorStop(1,'#0c241e');ctx.fillStyle=g;ctx.fillRect(0,0,W,H);
  const r=rng(7);ctx.save();ctx.globalAlpha=.07;ctx.fillStyle='#fff';for(let i=0;i<46;i++){ctx.beginPath();ctx.ellipse(r()*W,r()*H,60+r()*170,10+r()*26,r()*3,0,7);ctx.fill()}ctx.restore();
  ctx.fillStyle='#6b4423';ctx.fillRect(0,0,W,26);ctx.fillRect(0,H-26,W,26);ctx.fillRect(0,0,26,H);ctx.fillRect(W-26,0,26,H);
  ctx.save();ctx.strokeStyle='rgba(255,255,255,.28)';ctx.lineWidth=3;ctx.setLineDash([18,14]);ctx.strokeRect(50,50,W-100,H-100);ctx.restore();
  ctx.fillStyle='#e9e4d0';ctx.fillRect(120,H-70,140,14);ctx.fillStyle='#ff9f45';ctx.fillRect(280,H-70,90,14)};
ST.panel=(x,y,w,h,col)=>{ctx.save();ctx.fillStyle='rgba(8,28,22,.82)';RR(x,y,w,h,16);ctx.fill();ctx.setLineDash([22,10]);ctx.lineWidth=5;ctx.strokeStyle=col;RR(x,y,w,h,16);ctx.stroke();ctx.restore()};"""

def bg_dash():
    return """ST.bg=t=>{ctx.fillStyle='#0d1626';ctx.fillRect(0,0,W,H);ctx.strokeStyle='rgba(120,160,220,.10)';ctx.lineWidth=2;for(let x=0;x<=W;x+=90){ctx.beginPath();ctx.moveTo(x,0);ctx.lineTo(x,H);ctx.stroke()}for(let y=0;y<=H;y+=90){ctx.beginPath();ctx.moveTo(0,y);ctx.lineTo(W,y);ctx.stroke()}
  ctx.fillStyle='#16233b';ctx.fillRect(0,0,W,64);['#ff5f57','#febc2e','#28c840'].forEach((c,i)=>{ctx.fillStyle=c;ctx.beginPath();ctx.arc(40+i*34,32,10,0,7);ctx.fill()});
  ctx.save();ctx.globalAlpha=.16;ctx.strokeStyle='#38e1ff';ctx.lineWidth=6;ctx.beginPath();for(let i=0;i<=24;i++){const x=i*45,y=1700-Math.sin(i*.6+t*.8)*60-i*8;i?ctx.lineTo(x,y):ctx.moveTo(x,y)}ctx.stroke();ctx.restore()};
ST.panel=(x,y,w,h,col)=>{ctx.save();ctx.fillStyle='#16233b';RR(x,y,w,h,18);ctx.fill();ctx.fillStyle=col;RR(x,y+10,10,h-20,5);ctx.fill();ctx.lineWidth=2;ctx.strokeStyle='rgba(140,180,240,.35)';RR(x,y,w,h,18);ctx.stroke();ctx.restore()};"""

def bg_comic():
    return """ST.bg=t=>{ctx.fillStyle='#0b2a6f';ctx.fillRect(0,0,W,H);ctx.fillStyle='rgba(120,180,255,.22)';for(let y=0;y<H;y+=44)for(let x=((y/44)%2)*22;x<W;x+=44){ctx.beginPath();ctx.arc(x,y,9,0,7);ctx.fill()}
  ctx.save();ctx.translate(540,1000);ctx.fillStyle='rgba(255,214,10,.10)';for(let i=0;i<24;i++){ctx.rotate(Math.PI/12);ctx.beginPath();ctx.moveTo(0,0);ctx.lineTo(1500,-60);ctx.lineTo(1500,60);ctx.fill()}ctx.restore();
  ctx.lineWidth=14;ctx.strokeStyle='#fff';ctx.strokeRect(14,14,W-28,H-28)};
ST.panel=(x,y,w,h,col)=>{ctx.save();ctx.fillStyle='#000';RR(x+10,y+10,w,h,10);ctx.fill();ctx.fillStyle='#fff';RR(x,y,w,h,10);ctx.fill();ctx.fillStyle=col;ctx.fillRect(x,y,22,h);ctx.lineWidth=6;ctx.strokeStyle='#000';RR(x,y,w,h,10);ctx.stroke();ctx.restore()};"""

def bg_mt5():
    return """ST.bg=t=>{ctx.fillStyle='#0a0d12';ctx.fillRect(0,0,W,H);ctx.strokeStyle='rgba(255,255,255,.07)';ctx.lineWidth=2;for(let y=120;y<H;y+=120){ctx.beginPath();ctx.setLineDash([3,8]);ctx.moveTo(0,y);ctx.lineTo(W,y);ctx.stroke()}ctx.setLineDash([]);
  ctx.fillStyle='#1c2430';ctx.fillRect(0,0,W,70);ctx.fillStyle='#8fa3bf';ctx.font='700 28px Inter';ctx.textAlign='left';ctx.fillText('MetaTrader 5 · Experts',24,44);
  const r=rng(11);let p=1500;for(let i=0;i<24;i++){const o=p,c=p+(r()-.5)*90;p=c;const x=40+i*43,up=c>o;ctx.globalAlpha=.20;ctx.strokeStyle=ctx.fillStyle=up?'#00c853':'#ff5252';ctx.lineWidth=3;ctx.beginPath();ctx.moveTo(x,o-40);ctx.lineTo(x,o+40);ctx.stroke();ctx.fillRect(x-10,Math.min(o,c)+0,20,Math.abs(c-o)+6);ctx.globalAlpha=1}
  ctx.textAlign='center'};
ST.panel=(x,y,w,h,col)=>{ctx.save();ctx.fillStyle='rgba(18,26,38,.94)';RR(x,y,w,h,8);ctx.fill();ctx.fillStyle='#1c2430';ctx.fillRect(x,y,w,8);ctx.lineWidth=3;ctx.strokeStyle=col;RR(x,y,w,h,8);ctx.stroke();ctx.restore()};"""

def bg_suelo():
    return """ST.bg=t=>{const g=ctx.createLinearGradient(0,0,0,H);g.addColorStop(0,'#052a2e');g.addColorStop(1,'#031518');ctx.fillStyle=g;ctx.fillRect(0,0,W,H);
  const pts=[];for(let i=0;i<=20;i++)pts.push([i*54,1250-Math.sin(i*.55)*70-i*14+Math.sin(i*1.7)*26]);ctx.save();ctx.beginPath();pts.forEach(([x,y],i)=>i?ctx.lineTo(x,y):ctx.moveTo(x,y));ctx.lineTo(W,H);ctx.lineTo(0,H);ctx.closePath();const fg=ctx.createLinearGradient(0,1000,0,H);fg.addColorStop(0,'rgba(80,230,190,.28)');fg.addColorStop(1,'rgba(80,230,190,0)');ctx.fillStyle=fg;ctx.fill();
  ctx.beginPath();pts.forEach(([x,y],i)=>i?ctx.lineTo(x,y):ctx.moveTo(x,y));ctx.strokeStyle='#4fe3c1';ctx.lineWidth=6;ctx.stroke();ctx.restore();
  ctx.save();ctx.strokeStyle='rgba(255,196,77,.35)';ctx.lineWidth=3;ctx.setLineDash([16,12]);[1000,1120].forEach(y=>{ctx.beginPath();ctx.moveTo(0,y);ctx.lineTo(W,y);ctx.stroke()});ctx.restore();ctx.fillStyle='#4fe3c1';ctx.fillRect(0,0,W,8)};
ST.panel=(x,y,w,h,col)=>{ctx.save();ctx.fillStyle='rgba(3,28,32,.88)';RR(x,y,w,h,20);ctx.fill();ctx.lineWidth=5;ctx.strokeStyle=col;RR(x,y,w,h,20);ctx.stroke();ctx.restore()};"""

def bg_barras():
    return """ST.bg=t=>{const g=ctx.createLinearGradient(0,0,0,H);g.addColorStop(0,'#241338');g.addColorStop(1,'#150a24');ctx.fillStyle=g;ctx.fillRect(0,0,W,H);
  const hs=[.35,.6,.45,.8,.55,.95,.7];ctx.save();ctx.globalAlpha=.14;hs.forEach((v,i)=>{ctx.fillStyle=['#ff6f59','#2ec4b6','#ffbf3c','#c77dff','#6ea8ff','#ff6f59','#2ec4b6'][i];const h=v*620+Math.sin(t*1.2+i)*18;ctx.fillRect(40+i*148,H-h-40,120,h)});ctx.restore();
  ctx.strokeStyle='rgba(255,255,255,.10)';ctx.lineWidth=2;for(let y=H-40;y>200;y-=140){ctx.beginPath();ctx.moveTo(30,y);ctx.lineTo(W-30,y);ctx.stroke()}};
ST.panel=(x,y,w,h,col)=>{ctx.save();ctx.fillStyle='rgba(36,19,56,.9)';RR(x,y,w,h,18);ctx.fill();ctx.fillStyle=col;ctx.fillRect(x,y+h-12,w,12);ctx.lineWidth=4;ctx.strokeStyle=col;RR(x,y,w,h,18);ctx.stroke();ctx.restore()};"""

def bg_billete():
    return """ST.bg=t=>{ctx.fillStyle='#f3ead3';ctx.fillRect(0,0,W,H);ctx.save();ctx.strokeStyle='rgba(122,28,60,.20)';ctx.lineWidth=2;for(let k=0;k<22;k++){ctx.beginPath();for(let x=0;x<=W;x+=12){const y=H*.5+Math.sin(x*.012+k*.5+t*.2)*(300+k*18)*Math.cos(k*.3);x?ctx.lineTo(x,y):ctx.moveTo(x,y)}ctx.stroke()}ctx.restore();
  ctx.lineWidth=10;ctx.strokeStyle='#7a1c3c';ctx.strokeRect(22,22,W-44,H-44);ctx.lineWidth=3;ctx.strokeStyle='#1f3a5f';ctx.strokeRect(44,44,W-88,H-88);
  ctx.save();ctx.globalAlpha=.10;ctx.fillStyle='#1f3a5f';ctx.beginPath();ctx.arc(540,520,330,0,7);ctx.fill();ctx.restore()};
ST.panel=(x,y,w,h,col)=>{ctx.save();ctx.fillStyle='rgba(255,252,242,.95)';RR(x,y,w,h,12);ctx.fill();ctx.lineWidth=5;ctx.strokeStyle=col;RR(x,y,w,h,12);ctx.stroke();ctx.lineWidth=2;ctx.strokeStyle='rgba(31,58,95,.5)';RR(x+8,y+8,w-16,h-16,8);ctx.stroke();ctx.restore()};"""

THEMES = {
 'pizarra': dict(est=4, uso='5.º', pal='pizarra verde con tiza blanca, naranja, celeste y lila', bg=bg_pizarra(),
   C=["#ffb15e","#8fd8ff","#e7c6ff","#f4f1e2"], txt='#f4f1e2', lt='#f4f1e2', mu='#b7c7bd', acc='#ffb15e', pn='#10302a', dk='#0c241e',
   sty=dict(subBg="rgba(8,28,22,.96)",subStroke="#ffb15e",subFill="#fff",ctaBg="#0c241e",ctaSub="#f4f1e2",ctaGlow="#ffb15e",ctaAccent="#ffb15e",ctaBtnText="#0c241e"),
   cov=dict(ov='rgba(8,28,22,.84)',c1=2,c2=0,c3=1,mu='#b7c7bd',btn=0,btxt='#0c241e')),
 'dash': dict(est=7, uso='5.º', pal='panel oscuro azul con tarjetas cian, lima y rosa', bg=bg_dash(),
   C=["#38e1ff","#b6f23a","#ff7ab8","#ffffff"], txt='#ffffff', lt='#ffffff', mu='#8ea6c9', acc='#38e1ff', pn='#16233b', dk='#0d1626',
   sty=dict(subBg="rgba(13,22,38,.96)",subStroke="#38e1ff",subFill="#fff",ctaBg="#0d1626",ctaSub="#fff",ctaGlow="#38e1ff",ctaAccent="#38e1ff",ctaBtnText="#0d1626"),
   cov=dict(ov='rgba(13,22,38,.86)',c1=0,c2=1,c3=2,mu='#8ea6c9',btn=1,btxt='#0d1626')),
 'comic': dict(est=6, uso='5.º', pal='azul cobalto con tramado, estallidos amarillos y paneles blancos', bg=bg_comic(),
   C=["#ffd60a","#ff5a36","#4cc9f0","#ffffff"], txt='#111111', lt='#ffffff', mu='#cfe0ff', acc='#ffd60a', pn='#ffffff', dk='#0b2a6f',
   sty=dict(subBg="rgba(255,255,255,.97)",subStroke="#000",subFill="#111",ctaBg="#0b2a6f",ctaSub="#fff",ctaGlow="#ffd60a",ctaAccent="#ffd60a",ctaBtnText="#0b2a6f"),
   cov=dict(ov='rgba(11,42,111,.88)',c1=0,c2=1,c3=2,mu='#cfe0ff',btn=0,btxt='#0b2a6f')),
 'mt5': dict(est=5, uso='5.º', pal='terminal MT5 oscuro con velas verdes y rojas tenues', bg=bg_mt5(),
   C=["#00e676","#4da3ff","#ff5252","#ffd740"], txt='#e6edf7', lt='#e6edf7', mu='#8fa3bf', acc='#00e676', pn='#121a26', dk='#0a0d12',
   sty=dict(subBg="rgba(10,13,18,.96)",subStroke="#00e676",subFill="#e6edf7",ctaBg="#0a0d12",ctaSub="#e6edf7",ctaGlow="#00e676",ctaAccent="#00e676",ctaBtnText="#0a0d12"),
   cov=dict(ov='rgba(10,13,18,.88)',c1=0,c2=3,c3=1,mu='#8fa3bf',btn=2,btxt='#fff')),
 'suelo': dict(est=8, uso='5.º', pal='verde petróleo con línea menta, niveles ámbar y suelo degradado', bg=bg_suelo(),
   C=["#4fe3c1","#ffc44d","#ff7a7a","#ffffff"], txt='#ffffff', lt='#ffffff', mu='#8fc9c0', acc='#4fe3c1', pn='#031c20', dk='#031518',
   sty=dict(subBg="rgba(3,21,24,.96)",subStroke="#4fe3c1",subFill="#fff",ctaBg="#031518",ctaSub="#fff",ctaGlow="#4fe3c1",ctaAccent="#4fe3c1",ctaBtnText="#031518"),
   cov=dict(ov='rgba(3,21,24,.86)',c1=1,c2=0,c3=3,mu='#8fc9c0',btn=1,btxt='#031518')),
 'barras': dict(est=10, uso='5.º', pal='violeta oscuro con barras terracota, turquesa, mostaza y lila', bg=bg_barras(),
   C=["#ff6f59","#2ec4b6","#ffbf3c","#c77dff"], txt='#ffffff', lt='#ffffff', mu='#b9a6d6', acc='#ffbf3c', pn='#241338', dk='#150a24',
   sty=dict(subBg="rgba(21,10,36,.96)",subStroke="#ffbf3c",subFill="#fff",ctaBg="#150a24",ctaSub="#fff",ctaGlow="#ffbf3c",ctaAccent="#ffbf3c",ctaBtnText="#150a24"),
   cov=dict(ov='rgba(21,10,36,.86)',c1=2,c2=0,c3=1,mu='#b9a6d6',btn=2,btxt='#150a24')),
 'billete': dict(est=9, uso='5.º', pal='billete crema con guilloche burdeos y marco azul marino', bg=bg_billete(),
   C=["#7a1c3c","#1f3a5f","#a35d00","#1f3a5f"], txt='#1d1a14', lt='#1d1a14', mu='#5b5543', acc='#7a1c3c', pn='#fffcf2', dk='#f3ead3',
   sty=dict(subBg="rgba(255,252,242,.97)",subStroke="#7a1c3c",subFill="#1d1a14",ctaBg="#22121c",ctaSub="#f4efe2",ctaGlow="#e3a93f",ctaAccent="#e3a93f",ctaBtnText="#22121c"),
   cov=dict(ov='rgba(255,252,242,.90)',c1=0,c2=1,c3=2,mu='#5b5543',btn=0,btxt='#fffcf2')),
}

# ---------------- CONTENIDO ----------------
# bloque: (cabecera, grande, tamaño, subtítulo, tam_sub, [3 tarjetas], fuente, texto_visible_sub, texto_hablado_sub)
R = []
R.append(dict(n=221, scene=291, slug='plata_2011', page='v221_pizarra_plata_2011', theme='pizarra', hora='2026-11-16_0600', bpm=108, prog=[[45,"m"],[41,"M"],[48,"m"],[43,"M"]],
 name='Plata2011', hook='ABRIL 2011: LA PLATA TOCA US$ 49,85 Y EL CME SUBE LOS MÁRGENES',
 H0=dict(l='PLATA · COMEX · 2011',b='US$ 49,85',s=190,u='MÁXIMO DE 31 AÑOS, 28 DE ABRIL',c=['Abril de 2011','Y luego el CME cambió las reglas']),
 B=[("EL CONTEXTO","+57 %",270,"la plata en 2011 hasta el 29 de abril",38,["Más del doble en un año","Contrato COMEX de 5.000 onzas","Margen inicial ≈ US$ 11.745"],"fuente: Nasdaq; Financial Express (cifras aprox.)"),
    ("LAS ALZAS","5 ALZAS",190,"del margen en pocas semanas (CME)",38,["Inicial ≈ 11.745 → 12.825","Luego ≈ 14.513 y ≈ 16.200","Al final ≈ US$ 21.600"],"fuente: Institutional Investor; Benzinga; fechas difieren"),
    ("EL COSTO","+84 %",270,"el margen inicial: de ≈ 11.745 a ≈ 21.600",36,["Más capital por cada contrato","Menos apalancamiento disponible","Cifras aproximadas"],"fuente: Financial Express"),
    ("LA CAÍDA","−30 %",270,"de 49,85 (28 abr.) a 34,95 (5 may.)",38,["Bloomberg: −19 % en tres sesiones","Mayor caída de tres días desde 1983","SLV: ≈ −22 % en cinco días"],"fuente: Nasdaq; Bloomberg; Benzinga"),
    ("LAS CAUSAS","MÁRGENES + VENTA",80,"según Bloomberg: alzas de margen y venta de inversores",34,["Fechas de cada alza: fuentes difieren","No hay acusación probada en las fuentes","Cifras aproximadas"],"fuente: Bloomberg; Nasdaq")],
 END=("El margen puede cambiar de golpe","Deja siempre un colchón"),
 subs=[("El 28 de abril de 2011 la plata tocó 49,85 dólares y el CME empezó a subir los márgenes de sus futuros.","El veintiocho de abril de dos mil once la plata tocó cuarenta y nueve coma ochenta y cinco dólares y el CME empezó a subir los márgenes de sus futuros."),
  ("La plata subía ≈ 57 % en el año. Cada contrato de 5.000 onzas exigía ≈ US$ 11.745 de margen inicial.","La plata subía cerca de cincuenta y siete por ciento en el año. Cada contrato de cinco mil onzas exigía cerca de once mil setecientos cuarenta y cinco dólares de margen."),
  ("Hubo 5 alzas de margen en pocas semanas: de ≈ 11.745 a ≈ 21.600 dólares. Las fechas exactas difieren según la fuente.","Hubo cinco alzas de margen en pocas semanas: de cerca de once mil setecientos a cerca de veintiún mil seiscientos dólares. Las fechas exactas difieren según la fuente."),
  ("Eso es ≈ 84 % más de capital por contrato, lo que reduce el apalancamiento disponible de cada operador.","Eso es cerca de ochenta y cuatro por ciento más de capital por contrato, lo que reduce el apalancamiento disponible de cada operador."),
  ("El 5 de mayo cerró en 34,95: ≈ −30 %. Bloomberg: −19 % en tres sesiones.","El cinco de mayo cerró en treinta y cuatro coma noventa y cinco: cerca de menos treinta por ciento. Bloomberg: menos diecinueve por ciento en tres sesiones."),
  ("Bloomberg atribuyó la caída a las alzas de margen y a la venta de inversores. Fuentes: Nasdaq y Bloomberg. Educativo.","Bloomberg atribuyó la caída a las alzas de margen y a la venta de inversores. Fuentes: Nasdaq y Bloomberg. Contenido educativo."),
  ("Para tu robot: el margen exigido puede cambiar de golpe. Deja siempre un colchón de capital.","Para tu robot: el margen exigido puede cambiar de golpe. Deja siempre un colchón de capital.")],
 cover=("PLATA · ABRIL 2011","−30 %","TRAS 5 ALZAS DE MARGEN","de US$ 49,85 a 34,95 en una semana","VER QUÉ PASÓ →")))

R.append(dict(n=222, scene=292, slug='williams_r', page='v222_dashboard_williams_r', theme='dash', hora='2026-11-16_0930', bpm=118, prog=[[40,"m"],[36,"M"],[43,"m"],[38,"M"]],
 name='WilliamsR', hook='WILLIAMS %R: DOS UMBRALES, −20 Y −80, Y UNA TRAMPA',
 H0=dict(l='INDICADORES · WILLIAMS %R',b='−20 / −80',s=190,u='LOS DOS UMBRALES DEL OSCILADOR',c=['Rango de 0 a −100','Creado por Larry Williams']),
 B=[("QUIÉN LO CREÓ","≈ 1979",270,"en un libro de Larry Williams (StoneX)",38,["Trading Commodities, Windsor Books","Mide el cierre dentro del rango","Periodo habitual: 14"],"fuente: StoneX (año de una sola fuente); StockCharts"),
    ("LA FÓRMULA","0 A −100",190,"(máx. alto − cierre) ÷ (máx. alto − mín. bajo) × −100",30,["Máximo y mínimo de 14 velas","0 a −20: sobrecompra","−80 a −100: sobreventa"],"fuente: StockCharts"),
    ("EJEMPLO ILUSTRATIVO","−20",270,"máx. 2.100, mín. 2.000, cierre 2.080 (ilustrativo)",34,["(2.100 − 2.080) ÷ (2.100 − 2.000)","= 0,20 × −100 = −20","Justo en el umbral de sobrecompra"],"datos ilustrativos; aritmética propia"),
    ("PRIMO DEL ESTOCÁSTICO","%K − 100",150,"es el estocástico rápido, invertido",38,["Mismo cálculo, otra escala","Si %K = 80, entonces %R = −20","El %R no lleva suavizado interno"],"fuente: StockCharts; StoneX"),
    ("LA TRAMPA","SOBRECOMPRA",110,"no es señal de venta en tendencias fuertes",36,["Puede quedarse ahí mucho tiempo","Cruce de −50: pista de momentum","Confirma con otras herramientas"],"fuente: StockCharts; StoneX")],
 END=("Un umbral no es una señal","Pruébalo en backtest"),
 subs=[("Williams %R tiene dos umbrales, −20 y −80, y una trampa que muchos pasan por alto.","Williams porciento erre tiene dos umbrales, menos veinte y menos ochenta, y una trampa que muchos pasan por alto."),
  ("Lo creó Larry Williams; StoneX lo ubica en un libro de 1979. Mide dónde cierra el precio dentro de su rango reciente.","Lo creó Larry Williams; StoneX lo ubica en un libro de mil novecientos setenta y nueve. Mide dónde cierra el precio en su rango."),
  ("Se calcula con el máximo y el mínimo de 14 velas. Va de 0 a −100: sobrecompra sobre −20, sobreventa bajo −80.","Se calcula con el máximo y el mínimo de catorce velas. Va de cero a menos cien: sobrecompra sobre menos veinte, sobreventa bajo menos ochenta."),
  ("Ejemplo ilustrativo: máximo 2.100, mínimo 2.000, cierre 2.080. El resultado es −20, justo en sobrecompra.","Ejemplo ilustrativo: máximo dos mil cien, mínimo dos mil, cierre dos mil ochenta. El resultado es menos veinte, justo en sobrecompra."),
  ("Es el estocástico rápido invertido: %R = %K − 100. Si el estocástico marca 80, el %R marca −20.","Es el estocástico rápido invertido: erre igual a ka menos cien. Si el estocástico marca ochenta, el erre marca menos veinte."),
  ("En tendencias fuertes puede quedarse sobrecomprado mucho tiempo. Úsalo con otras herramientas. Fuentes: StockCharts; StoneX. Educativo.","En tendencias fuertes puede quedarse sobrecomprado mucho tiempo. Úsalo con otras herramientas. Fuentes: StockCharts y StoneX. Contenido educativo."),
  ("Para tu robot: un umbral no es una señal. Pruébalo en un backtest antes de usarlo.","Para tu robot: un umbral no es una señal. Pruébalo en un backtest antes de usarlo.")],
 cover=("WILLIAMS %R","−20","EL UMBRAL QUE ENGAÑA","sobrecompra no siempre es señal de venta","VER LA TRAMPA →")))

R.append(dict(n=223, scene=293, slug='fondos_soberanos', page='v223_comic_fondos_soberanos', theme='comic', hora='2026-11-16_1300', bpm=124, prog=[[43,"M"],[38,"m"],[45,"M"],[40,"m"]],
 name='FondosSoberanos', hook='RANKING: EL MAYOR FONDO SOBERANO DEL MUNDO MANEJA US$ 1,76 BILLONES',
 H0=dict(l='RANKING · FONDOS SOBERANOS',b='1,76 BILLONES',s=130,u='DE DÓLARES: EL Nº 1 ES NORUEGA',c=['Datos de Global SWF, jul. 2025','Cifras aproximadas']),
 B=[("N.º 1: NORUEGA","US$ 1,76 B",190,"billones de dólares (NBIM, Global SWF)",38,["Ley del fondo en 1990","Primer depósito en 1996","Primera inversión en acciones: 1998"],"fuente: NBIM; Global SWF vía Zawya"),
    ("N.º 2 Y N.º 3: CHINA","1,41 · 1,33",190,"SAFE IC y CIC, billones de dólares",38,["SAFE IC: ≈ US$ 1,41 billones","CIC: ≈ US$ 1,33 billones","Dos fondos chinos en el podio"],"fuente: Global SWF vía Zawya"),
    ("N.º 4: ARABIA SAUDITA","1,15",270,"PIF, billones de dólares",38,["Public Investment Fund","≈ US$ 1,15 billones","Cifra aproximada"],"fuente: Global SWF vía Zawya"),
    ("N.º 5: ABU DABI","1,11",270,"ADIA, billones de dólares",38,["Abu Dhabi Investment Authority","≈ US$ 1,11 billones","Los cinco suman ≈ US$ 6,8 billones"],"fuente: Global SWF vía Zawya; suma propia"),
    ("EL ALCANCE","≈ 1,5 %",270,"de las acciones cotizadas del mundo, en manos de Noruega",32,["Promedio, según NBIM","Acciones, renta fija, inmobiliario e infraestructura","El ranking cambia según la fuente"],"fuente: NBIM")],
 END=("Hay actores gigantes","No los sigas a ciegas"),
 subs=[("El mayor fondo soberano del mundo maneja ≈ US$ 1,76 billones: el de Noruega, según Global SWF.","El mayor fondo soberano del mundo maneja cerca de uno coma setenta y seis billones de dólares: el de Noruega, según Global SWF."),
  ("Noruega creó el fondo en 1990, depositó en 1996 y compró acciones por primera vez en 1998.","Noruega creó el fondo en mil novecientos noventa, depositó en mil novecientos noventa y seis y compró acciones por primera vez en mil novecientos noventa y ocho."),
  ("Los puestos 2 y 3 son chinos: SAFE IC con ≈ 1,41 billones y CIC con ≈ 1,33.","Los puestos dos y tres son chinos: SAFE IC con cerca de uno coma cuarenta y uno billones y CIC con uno coma treinta y tres."),
  ("Cuarto, el PIF de Arabia Saudita con ≈ 1,15 billones. Quinto, ADIA de Abu Dabi con ≈ 1,11 billones.","Cuarto, el PIF de Arabia Saudita con cerca de uno coma quince billones. Quinto, ADIA de Abu Dabi con cerca de uno coma once billones."),
  ("Los cinco suman ≈ 6,8 billones de dólares. Noruega posee en promedio ≈ 1,5 % de las acciones cotizadas del mundo.","Los cinco suman cerca de seis coma ocho billones de dólares. Noruega posee en promedio cerca de uno coma cinco por ciento de las acciones cotizadas del mundo."),
  ("El orden cambia según la fuente y la fecha. Fuentes: NBIM y Global SWF vía Zawya. Contenido educativo.","El orden cambia según la fuente y la fecha. Fuentes: NBIM y Global SWF vía Zawya. Contenido educativo."),
  ("Para tu robot: hay actores gigantes en el mercado. No los sigas a ciegas.","Para tu robot: hay actores gigantes en el mercado. No los sigas a ciegas.")],
 cover=("RANKING · FONDOS SOBERANOS","1,76","BILLONES DE DÓLARES","el fondo más grande del mundo, jul. 2025","VER EL RANKING →")))

R.append(dict(n=224, scene=294, slug='retcodes_mql5', page='v224_terminal_retcodes_mql5', theme='mt5', hora='2026-11-16_1630', bpm=112, prog=[[38,"m"],[34,"M"],[41,"m"],[36,"M"]],
 name='RetcodesMQL5', hook='TU ROBOT ENVÍA UNA ORDEN: ORDERSEND DEVUELVE TRUE, ¿Y AHORA?',
 H0=dict(l='ROBOTS · MQL5 · ORDERSEND',b='10009',s=230,u='TRADE_RETCODE_DONE: SOLICITUD COMPLETADA',c=['OrderSend devuelve true ≠ ejecutado','Hay que leer result.retcode']),
 B=[("EL ENGAÑO DEL TRUE","true ≠ OK",190,"solo indica una comprobación básica de estructuras",34,["La doc. de MQL5 lo dice expresamente","Analiza los campos de result","Mira primero result.retcode"],"fuente: documentación oficial de MQL5"),
    ("ERRORES DE PRECIO","10004",270,"REQUOTE: el precio cambió",40,["10020 PRICE_CHANGED: precios cambiaron","10006 REJECT: solicitud rechazada","10024 TOO_MANY_REQUESTS: muy frecuentes"],"fuente: MQL5, códigos de retorno"),
    ("ERRORES DE PARÁMETROS","10016",270,"INVALID_STOPS: stops inválidos",40,["10014 INVALID_VOLUME: volumen inválido","10030 INVALID_FILL: tipo de llenado","10019 NO_MONEY: fondos insuficientes"],"fuente: MQL5, códigos de retorno"),
    ("MERCADO Y CONEXIÓN","10018",270,"MARKET_CLOSED: mercado cerrado",40,["10017 TRADE_DISABLED: comercio desactivado","10031 CONNECTION: sin conexión al servidor","Descripciones de la doc. oficial"],"fuente: MQL5, códigos de retorno"),
    ("ANTES DE ENVIAR","OrderCheck",130,"valida fondos y parámetros sin enviar la orden",36,["Devuelve margen, margen libre y equity","Su true tampoco garantiza ejecución","Si falla: GetLastError()"],"fuente: documentación oficial de MQL5")],
 END=("Lee siempre el retcode","Valida antes de enviar"),
 subs=[("Tu robot envía una orden y OrderSend devuelve true. Eso no significa que se ejecutó.","Tu robot envía una orden y OrderSend devuelve true. Eso no significa que se ejecutó."),
  ("Según MQL5, el true solo indica que la comprobación básica de estructuras salió bien. Hay que leer result.retcode.","Según MQL cinco, el true solo indica que la comprobación básica de estructuras salió bien. Hay que leer result punto retcode."),
  ("Errores de precio: 10004 requote, 10020 precios cambiaron, 10006 solicitud rechazada y 10024 solicitudes demasiado frecuentes.","Errores de precio: diez mil cuatro requote, diez mil veinte precios cambiaron, diez mil seis solicitud rechazada y diez mil veinticuatro solicitudes demasiado frecuentes."),
  ("De parámetros: 10016 stops inválidos, 10014 volumen inválido, 10030 tipo de llenado inválido y 10019 fondos insuficientes.","De parámetros: diez mil dieciséis stops inválidos, diez mil catorce volumen inválido, diez mil treinta tipo de llenado inválido y diez mil diecinueve fondos insuficientes."),
  ("De mercado: 10018 mercado cerrado, 10017 comercio desactivado y 10031 sin conexión. El éxito es 10009.","De mercado: diez mil dieciocho mercado cerrado, diez mil diecisiete comercio desactivado y diez mil treinta y uno sin conexión. El éxito es diez mil nueve."),
  ("OrderCheck valida fondos y parámetros antes de enviar. Fuente: documentación oficial de MQL5. Contenido educativo.","OrderCheck valida fondos y parámetros antes de enviar. Fuente: documentación oficial de MQL cinco. Contenido educativo."),
  ("Para tu robot: lee siempre el retcode y valida antes de enviar.","Para tu robot: lee siempre el retcode y valida antes de enviar.")],
 cover=("ROBOTS · MQL5","10009","EL CÓDIGO DE ÉXITO","OrderSend devuelve true, pero ¿se ejecutó?","VER LOS CÓDIGOS →")))

R.append(dict(n=225, scene=295, slug='triple_witching', page='v225_linea_triple_witching', theme='suelo', hora='2026-11-16_2000', bpm=116, prog=[[42,"m"],[38,"M"],[45,"m"],[40,"M"]],
 name='TripleWitching', hook='CUATRO VIERNES AL AÑO VENCEN OPCIONES Y FUTUROS A LA VEZ',
 H0=dict(l='MECÁNICA · VENCIMIENTOS',b='3.er VIERNES',s=150,u='MAR · JUN · SEP · DIC',c=['Opciones y futuros vencen el mismo día','Se llama «triple witching»']),
 B=[("QUÉ VENCE","3 A LA VEZ",190,"contratos que expiran el mismo día",38,["Opciones sobre acciones","Futuros sobre índices","Opciones sobre índices"],"fuente: Investopedia"),
    ("CUÁNDO","4 VECES",270,"al año: tercer viernes de mar., jun., sep. y dic.",34,["2026: 20 mar, 19 jun, 18 sep, 18 dic","Antes eran cuatro: futuros de acciones","Dejaron de operar en EE. UU. en 2020"],"fuente: Investopedia"),
    ("POR QUÉ SUBE EL VOLUMEN","HORA FINAL",130,"se cierran, ruedan o compensan posiciones",38,["Última hora antes de las 16:00 ET","Arbitrajistas operan desajustes","Más volumen no implica más volatilidad"],"fuente: Investopedia"),
    ("EL REBALANCEO","S&P 500",190,"cambia su composición el mismo día",38,["Cambios anunciados ≈ 5 días hábiles antes","≈ US$ 250.000 M en acciones afectadas","Opciones por > US$ 5 billones vencían"],"fuente: CME (Piper Sandler); cifras aprox."),
    ("CIFRAS RECIENTES","≈ US$ 7,1 B",190,"de interés abierto venció el 19 dic. 2025 (Citi)",34,["Volumen > 26.000 M de acciones","≈ 50 % sobre su promedio de 12 meses","20 jun. 2025: ≈ US$ 6,5 billones"],"fuente: Swissinfo; cifras aproximadas")],
 END=("Los vencimientos mueven el volumen","Revisa el calendario antes de operar"),
 subs=[("Cuatro viernes al año vencen a la vez opciones sobre acciones, futuros e índices.","Cuatro viernes al año vencen a la vez opciones sobre acciones, futuros e índices."),
  ("Vencen opciones sobre acciones, futuros sobre índices y opciones sobre índices, el mismo día.","Vencen opciones sobre acciones, futuros sobre índices y opciones sobre índices, el mismo día."),
  ("Es el tercer viernes de marzo, junio, septiembre y diciembre. En 2026: 20 de marzo, 19 de junio, 18 de septiembre y 18 de diciembre.","Es el tercer viernes de marzo, junio, septiembre y diciembre. En dos mil veintiséis: veinte de marzo, diecinueve de junio, dieciocho de septiembre y dieciocho de diciembre."),
  ("Quien tiene posiciones que vencen las cierra o las rueda, sobre todo en la última hora. Más volumen no implica más volatilidad.","Quien tiene posiciones que vencen las cierra o las rueda, sobre todo al final. Más volumen no implica más volatilidad."),
  ("Ese día el S&P 500 también rebalancea. CME citó ≈ US$ 250.000 M en acciones afectadas en un rebalanceo reciente.","Ese día el S&P quinientos también rebalancea. CME citó cerca de doscientos cincuenta mil millones de dólares en acciones afectadas."),
  ("El 19 de dic. de 2025 vencieron ≈ 7,1 billones de dólares, según Citi. Fuentes: Investopedia, CME. Educativo.","El diecinueve de diciembre de dos mil veinticinco vencieron cerca de siete coma uno billones de dólares. Fuentes: Investopedia y CME. Educativo."),
  ("Para tu robot: los vencimientos mueven el volumen. Revisa el calendario antes de operar.","Para tu robot: los vencimientos mueven el volumen. Revisa el calendario antes de operar.")],
 cover=("MAR · JUN · SEP · DIC","3 EN 1","TRIPLE WITCHING","vencen opciones y futuros el mismo día","VER CÓMO FUNCIONA →")))

R.append(dict(n=226, scene=296, slug='julian_robertson', page='v226_barras_julian_robertson', theme='barras', hora='2026-11-16_2330', bpm=110, prog=[[39,"m"],[35,"M"],[42,"m"],[37,"M"]],
 name='JulianRobertson', hook='JULIAN ROBERTSON GANÓ 31,7 % ANUAL NETO DURANTE 18 AÑOS',
 H0=dict(l='PERSONA · JULIAN ROBERTSON',b='31,7 %',s=190,u='RETORNO ANUAL NETO, 1980–1998',c=['Tiger Management','Contra 12,7 % del S&P 500']),
 B=[("EL INICIO","US$ 8,8 M",190,"capital inicial de Tiger en 1980, Nueva York",34,["Nació el 25 de junio de 1932","Fundó Tiger en 1980","Fuentes: ≈ 8 a 8,8 millones"],"fuente: Fortune; InvestmentNews; Wikipedia"),
    ("EL AUGE","US$ 22.000 M",130,"activos máximos, mediados de 1998",38,["Retorno anual ≈ 32 % neto","S&P 500: ≈ 12,7 % anual","Cifras reportadas, no auditadas"],"fuente: Fortune; InvestmentNews"),
    ("LA CAÍDA","−71 %",270,"de US$ 21.000 M a 6.000 M en 18 meses (cálculo propio)",32,["Pérdidas y retiros de inversores","Apuesta equivocada con el yen (1998)","Pérdidas en US Airways"],"fuente: Fortune; Wikipedia"),
    ("EL CIERRE","MARZO 2000",130,"cerró sus seis fondos Tiger",38,["Carta: no tiene sentido exponer","a los inversores a un mercado","que dice no entender"],"fuente: Fortune; Wikipedia (cita parafraseada)"),
    ("LOS TIGER CUBS","6",270,"discípulos que fundaron sus propios fondos",36,["Lone Pine · Viking · Maverick","Tiger Global · Blue Ridge","Tiger Asia (luego Archegos)"],"fuente: Fortune")],
 END=("Sé honesto con tu límite","Opera lo que entiendes"),
 subs=[("Julian Robertson ganó ≈ 31,7 % anual neto entre 1980 y 1998.","Julian Robertson ganó cerca de treinta y uno coma siete por ciento anual neto entre mil novecientos ochenta y noventa y ocho."),
  ("Fundó Tiger Management en 1980, en Nueva York, con ≈ US$ 8,8 millones. Nació en 1932.","Fundó Tiger Management en mil novecientos ochenta, en Nueva York, con cerca de ocho coma ocho millones de dólares. Nació en mil novecientos treinta y dos."),
  ("A mediados de 1998 llegó a ≈ US$ 22.000 millones en activos. Son cifras reportadas, no auditadas.","A mediados de mil novecientos noventa y ocho llegó a cerca de veintidós mil millones de dólares en activos. Son cifras reportadas, no auditadas."),
  ("En 18 meses los activos cayeron de ≈ 21.000 a ≈ 6.000 millones. Influyeron los retiros, el yen y US Airways.","En dieciocho meses los activos cayeron de cerca de veintiún mil a cerca de seis mil millones. Influyeron los retiros, el yen y US Airways."),
  ("En marzo de 2000 cerró sus fondos. Escribió que no tenía sentido exponer a los inversores a un mercado que no entendía.","En marzo de dos mil cerró sus fondos. Escribió que no tenía sentido exponer a los inversores a un mercado que no entendía."),
  ("Sus discípulos, los Tiger Cubs, fundaron fondos propios. Fuentes: Fortune, InvestmentNews. Contenido educativo.","Sus discípulos, los Tiger Cubs, fundaron fondos propios. Fuentes: Fortune e InvestmentNews. Contenido educativo."),
  ("Para tu robot: sé honesto con tu límite. Opera solo lo que entiendes.","Para tu robot: sé honesto con tu límite. Opera solo lo que entiendes.")],
 cover=("TIGER MANAGEMENT","31,7 %","Y LUEGO CERRÓ TODO","Julian Robertson, 1980–2000","VER SU HISTORIA →")))

R.append(dict(n=227, scene=297, slug='oro_marzo_2020', page='v227_billete_oro_marzo_2020', theme='billete', hora='2026-11-17_0300', bpm=106, prog=[[43,"m"],[39,"M"],[46,"m"],[41,"M"]],
 name='OroMarzo2020', hook='MARZO 2020: EL ORO TOCÓ 1.703 DÓLARES Y CAYÓ A 1.451 EN SEMANAS',
 H0=dict(l='ORO · MARZO 2020 · COVID',b='≈ −15 %',s=210,u='DE US$ 1.703 A US$ 1.451',c=['Spot, máx. y mín. de marzo','Cálculo propio, cifras aprox.']),
 B=[("EL MÁXIMO","US$ 1.702,56",150,"9 de marzo: máximo desde 2012 (Reuters)",36,["Pánico por el coronavirus","El refugio, en plena subida","Máx. mensual ≈ US$ 1.703"],"fuente: Reuters vía Investing.com"),
    ("LA LIQUIDACIÓN","≈ −US$ 250",150,"del máximo al mínimo de marzo",38,["Peor semana desde 1983 (Bloomberg)","Margin calls y rescates de fondos","Se vende lo que tiene liquidez"],"fuente: Bloomberg; FXStreet; ii.co.uk"),
    ("EL DÓLAR","LIQUIDEZ",190,"demanda de dólares y dólar en máximos",38,["CTA pasaban a neto vendedores","Subía el costo de swaps en dólares","Fuentes: FXStreet, AJ Bell, Schroders"],"fuente: FXStreet; ii.co.uk"),
    ("FUTUROS VS. FÍSICO","COMEX > LONDRES",80,"los futuros cotizaron con prima por temor a no poder entregar",30,["Refinerías suizas pararon el 23 mar.","Valcambi, PAMP y Argor-Heraeus","≈ 1.500 t/año, ≈ un tercio de la oferta"],"fuente: Mining.com; Mining Weekly"),
    ("LA RECUPERACIÓN","US$ 2.000",190,"primera vez sobre 2.000: 4 de agosto de 2020",38,["Spot: 2.000,58 ese día","Cinco meses tras el mínimo","Cifras aproximadas"],"fuente: Al Jazeera")],
 END=("El refugio también cae","Cuida el margen en pánicos"),
 subs=[("En marzo de 2020 el oro pasó de ≈ 1.703 a ≈ 1.451 dólares en pocas semanas.","En marzo de dos mil veinte el oro pasó de mil setecientos tres a mil cuatrocientos cincuenta y uno dólares en pocas semanas."),
  ("El 9 de marzo tocó 1.702,56, su máximo desde 2012, según Reuters. El pánico del coronavirus lo impulsaba.","El nueve de marzo tocó mil setecientos dos coma cincuenta y seis, su máximo desde dos mil doce, según Reuters. El pánico del coronavirus lo impulsaba."),
  ("Bloomberg habló de su peor semana desde 1983. Los margin calls y los rescates de fondos obligaron a vender.","Bloomberg habló de su peor semana desde mil novecientos ochenta y tres. Los margin calls y los rescates de fondos obligaron a vender."),
  ("Había demanda de dólares y el dólar estaba en máximos. Se vendía lo que tenía liquidez, incluido el oro.","Había demanda de dólares y el dólar estaba en máximos. Se vendía lo que tenía liquidez, incluido el oro."),
  ("Los futuros de COMEX cotizaron con prima sobre Londres. Tres refinerías suizas pararon el 23 de marzo.","Los futuros de COMEX cotizaron con prima sobre Londres. Tres refinerías suizas pararon el veintitrés de marzo."),
  ("El 4 de agosto de 2020 superó 2.000 por primera vez. Fuentes: Reuters, Bloomberg, Mining.com. Educativo.","El cuatro de agosto de dos mil veinte superó dos mil por primera vez. Fuentes: Reuters, Bloomberg y Mining punto com. Contenido educativo."),
  ("Para tu robot: el refugio también puede caer en un pánico. Cuida el margen.","Para tu robot: el refugio también puede caer en un pánico. Cuida el margen.")],
 cover=("ORO · MARZO 2020","−15 %","EL REFUGIO TAMBIÉN CAE","de 1.703 a 1.451 en pocas semanas","VER QUÉ PASÓ →")))

def js(o): return json.dumps(o, ensure_ascii=False)

def build(r):
    th = THEMES[r['theme']]
    subs = []
    for (a, b), (vis, spk) in zip(WIN, r['subs']):
        subs.append([a, b, vis, spk])
    subs.append(OUTRO); subs.append(CTA)
    ev = [[0.3,"rise",2.4],[3.0,"down"],[3.6,"hit"]] + EVB
    spec = dict(name=r['name'], hook=r['hook'], dur=60, cta=56, bpm=r['bpm'], mus="soft", prog=r['prog'], ev=ev, subs=subs)
    sty = dict(subFont="800 42px Inter", ctaFontS="800 50px Inter", ctaFontL="900 104px Inter", **th['sty'])
    C = th['C']
    blocks = []
    starts = [6.4, 13.6, 20.6, 28.4, 35.2]
    for i, (hd, big, bsz, sub, ssz, cards, src) in enumerate(r['B']):
        blocks.append(f"function b{i+1}(t,al){{std(t,al,{starts[i]},{js(hd)},C[{(i+1)%3}],{js(big)},{bsz},C[{i%3}],{js(sub)},{ssz},{js(cards)},{js(src)})}}")
    e1, e2 = r['END']
    cv = r['cover']; cc = th['cov']
    ctop, cbig, cmid, csmall, cbtn = cv
    page = f"""<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{{font-family:Inter;font-weight:800;src:url(node_modules/@fontsource/inter/files/inter-latin-800-normal.woff2)}}
@font-face{{font-family:Inter;font-weight:900;src:url(node_modules/@fontsource/inter/files/inter-latin-900-normal.woff2)}}
html,body{{margin:0;background:#000}}canvas{{display:block;width:1080px;height:1920px}}
</style></head><body><canvas id="c"></canvas><script src="common.js"></script><script>
// Estilo {th['est']} ({th['uso']} uso) — {th['pal']} — tema: {r['name']} (60 s).
const SPEC={js(spec)};
const STY={js(sty)};
const DK=STY.ctaBg,ACC=STY.ctaAccent,FAM='Inter';
window.FONTS=['900 40px Inter','800 40px Inter'];
</script><script src="kit2.js"></script><script src="kit3.js"></script><script>
const C={js(C)};
let PRE=t=>{{}},POST=t=>{{}};
Object.assign(ST,{{txt:{js(th['txt'])},mu:{js(th['mu'])},acc:{js(th['acc'])},pn:{js(th['pn'])},c:C}});
ST.lt={js(th['lt'])};
{th['bg']}
function fz(txt,sz,maxW){{ctx.save();ctx.font=`900 ${{sz}}px Inter`;const w=ctx.measureText(fx(txt)).width;ctx.restore();return w>maxW?Math.floor(sz*maxW/w):sz}}
function hd(t,t0,s,col){{Lb(s,540,175,fz(s,52,960),col,eout(prog(t,t0,t0+.5)))}}
function cds(t,a,cards,y0=720){{cards.forEach((s,i)=>card(t,a+2.8+i*1.4,y0+i*180,i<2?150:120,C[i%3],s,null,fz(s,40,850)))}}
function std(t,al,a,h,hc,big,bsz,bc,sub,ssz,cards,src){{ctx.save();ctx.globalAlpha=al;hd(t,a+.1,h,hc);bigNum(t,a+.6,540,470,big,fz(big,bsz,900),bc);Lb(sub,540,620,fz(sub,ssz,980),ST.lt||ST.txt,eout(prog(t,a+1.6,a+2.2)));cds(t,a,cards);if(src)Lb(src,540,1290,28,ST.mu,eout(prog(t,a+6.0,a+6.6)));ctx.restore()}}
function h0(t,al){{ctx.save();ctx.globalAlpha=al;Lb(H0.l,540,380,fz(H0.l,38,960),C[1],eout(prog(t,.2,.8)));bigNum(t,.6,540,640,H0.b,fz(H0.b,H0.s,900),C[0]);Lb(H0.u,540,860,fz(H0.u,40,960),C[2],eout(prog(t,1.6,2.2)));card(t,3.0,990,130,C[1],H0.c[0],null,fz(H0.c[0],40,850));card(t,4.2,1140,120,C[2],H0.c[1],null,fz(H0.c[1],40,850));ctx.restore()}}
const H0={js(r['H0'])};
{chr(10).join(blocks)}
function b6(t,a){{endBlock(t,a,43.6,{js(e1)},{js(e2)},C[0],C[1])}}
function cover(){{ST.bg(3);PRE(0);ctx.fillStyle={js(cc['ov'])};ctx.fillRect(30,230,1020,850);Lb({js(ctop)},540,300,fz({js(ctop)},56,940),C[{cc['c2']}],1);Lb({js(cbig)},540,610,fz({js(cbig)},330,960),C[{cc['c1']}],1);Lb({js(cmid)},540,830,fz({js(cmid)},66,960),C[{cc['c3']}],1);Lb({js(csmall)},540,960,fz({js(csmall)},34,960),{js(cc['mu'])},1);coverBtn({js(cbtn)},C[{cc['btn']}],{js(cc['btxt'])});POST(0)}}
function draw(t){{PRE(t);drawBlocks(t,[[0,6.0,h0],[6.4,13.4,b1],[13.6,20.4,b2],[20.6,28.2,b3],[28.4,35.0,b4],[35.2,43.4,b5],[43.6,49.6,b6]]);POST(t)}}
</script></body></html>
"""
    return page

if __name__ == '__main__':
    sel = [int(x) for x in sys.argv[1:]]
    for r in R:
        if sel and r['n'] not in sel: continue
        open(os.path.join(HERE, r['page'] + '.html'), 'w').write(build(r))
        print('ok', r['page'], r['scene'])
