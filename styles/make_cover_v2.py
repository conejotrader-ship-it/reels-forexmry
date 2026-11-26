#!/usr/bin/env python3
"""Carátulas v2 (decisión de Cristian, 26 nov 2026): más llamativas, variadas y basadas en datos de CTR.
Uso: python3 make_cover_v2.py <spec.json> <salida.jpg> [--preview vista.jpg]

Plantillas ("tpl"), todas con lo importante en la zona segura y = 420–1500 (recorte 3:4 de la cuadrícula y 1:1 antiguo):
  cifra          foto + cifra gigante + 2–4 palabras ("la cifra que duele")
  antes_despues  foto oscurecida + tarjeta ANTES (verde) → tarjeta DESPUÉS (roja)
  grafico        foto + gráfico de velas estilizado con desplome, círculo y flecha rojos
  interfaz       foto desenfocada + ventana genérica (orden, alerta) con el dato marcado en rojo ("recreación")
  objeto         foto de un objeto héroe + cifra y 2–3 palabras, mucho espacio vacío (letra serif)
  vs             pantalla dividida: foto a la izquierda, gráfico dibujado a la derecha, insignia VS
  pregunta       foto + pregunta en 2 líneas (letra a mano) + círculo y flecha hacia un punto de la foto
  robot          Robot Trust Gold Mr. Y con halo dorado + cifra o pregunta
  sello          foto + cifra + sello diagonal ("QUEBRÓ", "MITO", "ERROR")
Campos comunes del spec: tpl, photo (ruta), serie (ERROR ÉPICO | ORO CURIOSO | ROBOTS Y EA | PERSONAJES | MERCADOS RAROS | INDICADORES RAROS | HISTORIA),
  big, line, small (opcional), cta (texto del botón, p. ej. "VER LA HISTORIA"), acc (color de acento opcional), focus_y (0–1, encuadre de la foto).
Específicos: antes_despues {a_label, a_val, b_label, b_val}; grafico {} ; interfaz {title, rows:[[etiqueta, valor, marcar]], stamp};
  vs {left, right, chart:"up"|"down"}; pregunta {q1, q2, cx, cy, r}; sello {stamp}.
Reglas: big ≤ 2 bloques (una cifra cuenta como palabra), line ≤ 5 palabras, palabras con tensión ("perdió", "error", "quebró"),
  cara seria con la boca cerrada mirando a cámara, un solo foco, fondo oscuro + 1 acento."""
import sys, os, base64, io, json
from PIL import Image, ImageDraw
from playwright.sync_api import sync_playwright
HERE = os.path.dirname(os.path.abspath(__file__))
spec = json.load(open(sys.argv[1], encoding='utf-8')); out = sys.argv[2]
prev = sys.argv[sys.argv.index('--preview') + 1] if '--preview' in sys.argv else None
SPEC_DIR = os.path.dirname(os.path.abspath(sys.argv[1]))

def b64img(path, size=None, fmt='JPEG'):
    p = path if os.path.isabs(path) else os.path.join(SPEC_DIR, path)
    im = Image.open(p)
    im = im.convert('RGBA' if fmt == 'PNG' else 'RGB')
    if size: im = im.resize(size, Image.LANCZOS)
    b = io.BytesIO(); im.save(b, fmt, **({'quality': 90} if fmt == 'JPEG' else {}))
    return f'data:image/{fmt.lower()};base64,' + base64.b64encode(b.getvalue()).decode()

photo = b64img(spec['photo']) if spec.get('photo') else ''
robot = b64img(os.path.join(HERE, 'robot_trust_gold.png'), fmt='PNG') if spec['tpl'] == 'robot' else ''
FONT = 'node_modules/@fontsource'
html = f"""<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{{font-family:Inter;font-weight:700;src:url({FONT}/inter/files/inter-latin-700-normal.woff2)}}
@font-face{{font-family:Inter;font-weight:800;src:url({FONT}/inter/files/inter-latin-800-normal.woff2)}}
@font-face{{font-family:Inter;font-weight:900;src:url({FONT}/inter/files/inter-latin-900-normal.woff2)}}
@font-face{{font-family:Playfair;font-weight:900;src:url({FONT}/playfair-display/files/playfair-display-latin-900-normal.woff2)}}
@font-face{{font-family:Marker;font-weight:400;src:url({FONT}/permanent-marker/files/permanent-marker-latin-400-normal.woff2)}}
@font-face{{font-family:Typer;font-weight:400;src:url({FONT}/special-elite/files/special-elite-latin-400-normal.woff2)}}
html,body{{margin:0;background:#000}}</style></head><body><canvas id="c" width="1080" height="1920"></canvas><script>
const P={json.dumps(spec, ensure_ascii=False)};
const cv=document.getElementById('c'),ctx=cv.getContext('2d'),W=1080,H=1920;
const SERIES={{'ERROR ÉPICO':'#ff3b30','ORO CURIOSO':'#ffc83d','ROBOTS Y EA':'#35e0ff','PERSONAJES':'#c79bff','MERCADOS RAROS':'#ff8a3d','HISTORIA':'#3ddc84','INDICADORES RAROS':'#ff5fa2'}};
const SC=SERIES[P.serie]||'#ffc83d', ACC=P.acc||SC, RED='#ff2d2d', GREEN='#2ee07a';
function font(w,sz,f){{return w+' '+sz+'px '+(f||'Inter')}}
function fit(s,sz,maxW,w,f){{ctx.font=font(w||900,sz,f);const m=ctx.measureText(s).width;return m>maxW?Math.floor(sz*maxW/m):sz}}
function T(s,x,y,sz,col,o={{}}){{const w=o.w||900,f=o.f||'Inter';sz=fit(s,sz,o.maxW||960,w,f);ctx.save();ctx.font=font(w,sz,f);ctx.textAlign=o.align||'center';ctx.textBaseline='middle';
  if(o.shadow!==false){{ctx.shadowColor='rgba(0,0,0,.95)';ctx.shadowBlur=o.blur||30;ctx.shadowOffsetY=6}}
  if(o.stroke!==false){{ctx.lineJoin='round';ctx.lineWidth=Math.max(6,sz*.07);ctx.strokeStyle=o.strokeCol||'rgba(0,0,0,.85)';ctx.strokeText(s,x,y)}}
  ctx.shadowColor='transparent';ctx.fillStyle=col;ctx.fillText(s,x,y);ctx.restore();return sz}}
function RR(x,y,w,h,r){{ctx.beginPath();ctx.roundRect(x,y,w,h,r)}}
function cover(img,x,y,w,h,fy){{const s=Math.max(w/img.width,h/img.height),iw=img.width*s,ih=img.height*s;ctx.save();ctx.beginPath();ctx.rect(x,y,w,h);ctx.clip();
  ctx.drawImage(img,x+(w-iw)/2,y+(h-ih)*(fy==null?.5:fy),iw,ih);ctx.restore()}}
function grad(y0,y1,a0,a1){{const g=ctx.createLinearGradient(0,y0,0,y1);g.addColorStop(0,'rgba(4,5,9,'+a0+')');g.addColorStop(1,'rgba(4,5,9,'+a1+')');ctx.fillStyle=g;ctx.fillRect(0,y0,W,y1-y0)}}
function tag(y){{if(!P.serie)return;ctx.save();ctx.font=font(900,34);const t=P.serie,w=ctx.measureText(t).width+70;RR(540-w/2,y-32,w,64,32);ctx.fillStyle=SC;ctx.fill();
  ctx.fillStyle='#0a0b10';ctx.textAlign='center';ctx.textBaseline='middle';ctx.fillText(t,540,y+2);ctx.restore()}}
function cta(y){{if(!P.cta)return;ctx.save();const t='▶  '+P.cta;ctx.font=font(900,40);const w=ctx.measureText(t).width+90;ctx.shadowColor='rgba(0,0,0,.6)';ctx.shadowBlur=24;
  RR(540-w/2,y-40,w,80,40);ctx.fillStyle=ACC;ctx.fill();ctx.shadowColor='transparent';ctx.fillStyle='#0a0b10';ctx.textAlign='center';ctx.textBaseline='middle';ctx.fillText(t,540,y+2);ctx.restore()}}
function circle(cx,cy,rx,ry,col,lw){{ctx.save();ctx.strokeStyle=col||RED;ctx.lineWidth=lw||12;ctx.shadowColor='rgba(0,0,0,.7)';ctx.shadowBlur=14;ctx.beginPath();ctx.ellipse(cx,cy,rx,ry||rx,-.08,0,Math.PI*2);ctx.stroke();ctx.restore()}}
function arrow(x0,y0,x1,y1,col,lw,bend){{ctx.save();ctx.strokeStyle=col||RED;ctx.fillStyle=col||RED;ctx.lineWidth=lw||14;ctx.lineCap='round';ctx.shadowColor='rgba(0,0,0,.7)';ctx.shadowBlur=14;
  const mx=(x0+x1)/2+(bend||0),my=(y0+y1)/2-(bend||0)*.3;ctx.beginPath();ctx.moveTo(x0,y0);ctx.quadraticCurveTo(mx,my,x1,y1);ctx.stroke();
  const a=Math.atan2(y1-my,x1-mx),L=46;ctx.beginPath();ctx.moveTo(x1+Math.cos(a)*10,y1+Math.sin(a)*10);ctx.lineTo(x1-Math.cos(a-.5)*L,y1-Math.sin(a-.5)*L);ctx.lineTo(x1-Math.cos(a+.5)*L,y1-Math.sin(a+.5)*L);ctx.closePath();ctx.fill();ctx.restore()}}
function candles(x0,y0,w,h,mode){{// gráfico estilizado (no es una captura real)
  const up=[.62,.58,.6,.54,.5,.52,.46,.42,.44,.38,.35,.33,.3,.28],dn=[.30,.33,.28,.36,.32,.38,.35,.42,.40,.46,.44,.5,.88,.97];
  const v=mode==='up'?up:(mode==='flat'?up.map((q,i)=>.5+Math.sin(i)*.05):dn.map((q,i)=>i<12?up[i]:q));const n=v.length,cw=w/n;
  ctx.save();ctx.strokeStyle='rgba(255,255,255,.12)';ctx.lineWidth=2;for(let k=1;k<5;k++){{ctx.beginPath();ctx.moveTo(x0,y0+h*k/5);ctx.lineTo(x0+w,y0+h*k/5);ctx.stroke()}}
  let pts=[];for(let i=0;i<n;i++){{const o=i?v[i-1]:v[0]+.03,c=v[i],hi=Math.min(o,c)-.04,lo=Math.max(o,c)+.04,x=x0+cw*i+cw/2,bull=c<o;
    ctx.strokeStyle=ctx.fillStyle=bull?GREEN:RED;ctx.lineWidth=5;ctx.beginPath();ctx.moveTo(x,y0+hi*h);ctx.lineTo(x,y0+lo*h);ctx.stroke();
    ctx.fillRect(x-cw*.32,y0+Math.min(o,c)*h,cw*.64,Math.max(8,Math.abs(c-o)*h));pts.push([x,y0+lo*h])}}
  ctx.restore();return pts}}
function drawTpl(img,rob){{
  const tp=P.tpl;
  if(tp==='cifra'){{cover(img,0,0,W,H,P.focus_y);grad(0,1080,.9,0);grad(1500,H,0,.6);tag(470);
    T(P.big,540,650,290,ACC,{{blur:44}});T(P.line,540,830,84,'#fff');if(P.small)T(P.small,540,925,44,'#e9edf5',{{w:800,stroke:false,blur:18}});cta(1430)}}
  else if(tp==='objeto'){{cover(img,0,0,W,H,P.focus_y);grad(0,900,.85,0);tag(470);
    T(P.big,540,640,250,ACC,{{f:'Playfair',blur:40}});T(P.line,540,800,70,'#fff',{{w:800}});cta(1430)}}
  else if(tp==='antes_despues'){{cover(img,0,0,W,H,P.focus_y);ctx.fillStyle='rgba(4,5,9,.35)';ctx.fillRect(0,0,W,H);grad(0,1150,.92,.2);tag(450);
    T(P.line,540,548,76,'#fff');
    const card=(y,lab,val,col)=>{{ctx.save();ctx.shadowColor='rgba(0,0,0,.7)';ctx.shadowBlur=30;RR(130,y,820,180,30);ctx.fillStyle='rgba(10,12,18,.88)';ctx.fill();ctx.shadowColor='transparent';
      ctx.fillStyle=col;RR(130,y,22,180,11);ctx.fill();ctx.lineWidth=4;ctx.strokeStyle=col;RR(130,y,820,180,30);ctx.stroke();ctx.restore();
      T(lab,190,y+42,34,'#cfd6e4',{{align:'left',w:800,stroke:false,blur:0,maxW:700}});T(val,190,y+115,104,col,{{align:'left',maxW:730}})}};
    card(620,P.a_label,P.a_val,GREEN);arrow(540,820,540,905,RED,16);card(930,P.b_label,P.b_val,RED);if(P.small)T(P.small,540,1180,44,'#fff',{{w:800}});cta(1430)}}
  else if(tp==='grafico'){{cover(img,0,0,W,H,P.focus_y);ctx.fillStyle='rgba(4,5,9,.45)';ctx.fillRect(0,0,W,H);grad(0,900,.85,0);tag(450);
    T(P.line,540,545,80,'#fff');T(P.big,350,700,200,RED,{{maxW:620}});
    const pts=candles(120,820,840,560,'down');const [lx,ly]=pts[pts.length-1];circle(lx,ly-20,95,80,'#ffe14d',12);arrow(560,760,lx-70,ly-120,'#ffe14d',14,-90);
    T('gráfico ilustrativo',540,1478,26,'rgba(255,255,255,.75)',{{w:700,stroke:false,blur:8}});cta(1600)}}
  else if(tp==='interfaz'){{ctx.save();ctx.filter='blur(10px) brightness(.55)';cover(img,-30,-30,W+60,H+60,P.focus_y);ctx.restore();tag(450);
    const x=110,y=540,w=860,h=520;ctx.save();ctx.shadowColor='rgba(0,0,0,.8)';ctx.shadowBlur=60;RR(x,y,w,h,30);ctx.fillStyle='#f3f5f9';ctx.fill();ctx.restore();
    ctx.save();RR(x,y,w,96,30);ctx.clip();ctx.fillStyle='#1b2130';ctx.fillRect(x,y,w,96);ctx.restore();
    ctx.fillStyle=RED;ctx.beginPath();ctx.arc(x+50,y+48,14,0,7);ctx.fill();T(P.title,x+80,y+50,40,'#fff',{{align:'left',w:800,stroke:false,shadow:false,maxW:740}});
    (P.rows||[]).forEach((r,i)=>{{const yy=y+170+i*140;T(r[0],x+50,yy,36,'#6b7385',{{align:'left',w:700,stroke:false,shadow:false,maxW:330}});
      const sz=T(r[1],x+w-50,yy,72,'#10131a',{{align:'right',w:900,stroke:false,shadow:false,maxW:470}});
      if(r[2]){{ctx.font=font(900,sz);const tw=ctx.measureText(r[1]).width;circle(x+w-50-tw/2,yy,tw/2+70,sz*.95,RED,9)}}}});
    if(P.stamp){{ctx.save();ctx.translate(x+w-200,y+h-70);ctx.rotate(-.12);ctx.strokeStyle=RED;ctx.lineWidth=7;ctx.font=font(900,44);const sw=ctx.measureText(P.stamp).width+50;
      ctx.strokeRect(-sw/2,-36,sw,72);ctx.fillStyle=RED;ctx.textAlign='center';ctx.textBaseline='middle';ctx.fillText(P.stamp,0,2);ctx.restore()}}
    T('recreación',x+60,y+h-40,26,'#8a92a3',{{align:'left',w:700,stroke:false,shadow:false}});
    T(P.line,540,1190,88,'#fff');if(P.small)T(P.small,540,1290,44,ACC,{{w:800}});cta(1430)}}
  else if(tp==='vs'){{cover(img,0,0,540,H,P.focus_y);ctx.fillStyle='#0b1220';ctx.fillRect(540,0,540,H);
    ctx.save();ctx.beginPath();ctx.rect(540,0,540,H);ctx.clip();candles(590,700,440,560,P.chart||'up');ctx.restore();
    grad(0,800,.85,0);ctx.fillStyle=ACC;ctx.fillRect(532,0,16,H);tag(450);
    const lab=(s,cx,col)=>{{ctx.save();ctx.font=font(900,52);const w=Math.min(480,ctx.measureText(s).width+50);RR(cx-w/2,540,w,86,16);ctx.fillStyle=col;ctx.fill();ctx.restore();T(s,cx,585,52,'#0a0b10',{{maxW:440,stroke:false,shadow:false}})}};
    lab(P.left,270,'#ffffff');lab(P.right,810,'#ffffff');
    ctx.save();ctx.shadowColor='rgba(0,0,0,.8)';ctx.shadowBlur=40;ctx.fillStyle=ACC;ctx.beginPath();ctx.arc(540,960,118,0,7);ctx.fill();ctx.restore();
    T('VS',540,966,120,'#0a0b10',{{stroke:false,shadow:false}});T(P.line,540,1280,92,'#fff');cta(1430)}}
  else if(tp==='pregunta'){{cover(img,0,0,W,H,P.focus_y);grad(0,1000,.88,0);tag(450);
    T(P.q1,540,575,104,'#fff',{{f:'Marker',w:400}});T(P.q2,540,715,130,ACC,{{f:'Marker',w:400}});
    if(P.cx){{circle(P.cx,P.cy,P.r||110,(P.r||110)*.85,RED,12);arrow(700,800,P.cx+(P.r||110)*.5,P.cy-(P.r||110)*.9,RED,14,80)}}cta(1430)}}
  else if(tp==='robot'){{ctx.fillStyle='#07070a';ctx.fillRect(0,0,W,H);const g=ctx.createRadialGradient(540,1100,40,540,1100,700);g.addColorStop(0,'rgba(255,190,60,.55)');g.addColorStop(1,'rgba(255,190,60,0)');
    ctx.fillStyle=g;ctx.fillRect(0,0,W,H);const rh=1050,rw=rob.width*rh/rob.height;ctx.drawImage(rob,540-rw/2,820,rw,rh);grad(1500,H,0,.7);tag(450);
    T(P.big,540,640,230,ACC,{{blur:44}});T(P.line,540,800,76,'#fff');cta(1430)}}
  else if(tp==='sello'){{cover(img,0,0,W,H,P.focus_y);ctx.fillStyle='rgba(4,5,9,.3)';ctx.fillRect(0,0,W,H);grad(0,1100,.88,0);tag(450);
    T(P.big,540,630,250,'#fff',{{blur:44}});ctx.save();ctx.translate(540,860);ctx.rotate(-.14);ctx.font=font(900,120);const sw=ctx.measureText(P.stamp).width+90;
    ctx.globalAlpha=.95;ctx.strokeStyle=RED;ctx.lineWidth=14;ctx.strokeRect(-sw/2,-85,sw,170);ctx.fillStyle=RED;ctx.textAlign='center';ctx.textBaseline='middle';ctx.fillText(P.stamp,0,6);ctx.restore();
    T(P.line,540,1060,70,'#fff');cta(1430)}}
  window.__done=true}}
function load(src){{return new Promise(r=>{{if(!src)return r(null);const i=new Image();i.onload=()=>r(i);i.src=src}})}}
(async()=>{{for(const f of ['900 40px Inter','800 40px Inter','700 40px Inter','900 40px Playfair','400 40px Marker','400 40px Typer'])await document.fonts.load(f);
  const img=await load({json.dumps(photo)}),rob=await load({json.dumps(robot)});drawTpl(img,rob)}})();
</script></body></html>"""
tmp = os.path.join(HERE, f'_cover_v2_tmp_{os.getpid()}.html'); open(tmp, 'w', encoding='utf-8').write(html)
with sync_playwright() as p:
    br = p.chromium.launch(); pg = br.new_page(viewport={'width': 1080, 'height': 1920})
    errs = []; pg.on('pageerror', lambda e: errs.append(str(e)))
    pg.goto('file://' + tmp); pg.wait_for_function('window.__done===true', timeout=30000)
    png = base64.b64decode(pg.evaluate("document.getElementById('c').toDataURL('image/png')").split(',', 1)[1]); br.close()
os.remove(tmp)
if errs: print('errores:', errs)
im = Image.open(io.BytesIO(png)).convert('RGB'); im.save(out, quality=90)
if prev:  # vista previa: completa + recorte 3:4 de la cuadrícula + miniatura del tamaño de la cuadrícula del móvil
    full = im.resize((360, 640)); grid = im.crop((0, 240, 1080, 1680)).resize((360, 480)); tiny = im.crop((0, 240, 1080, 1680)).resize((120, 160))
    sh = Image.new('RGB', (360 * 2 + 140, 640), (40, 40, 40)); sh.paste(full, (0, 0)); sh.paste(grid, (370, 80)); sh.paste(tiny, (740, 240))
    d = ImageDraw.Draw(sh); d.rectangle([0, 140, 359, 500], outline=(0, 255, 120), width=2)  # zona segura 1:1
    sh.save(prev, quality=88)
print('ok', out)
