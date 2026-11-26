#!/usr/bin/env python3
"""Carátula con foto IA a pantalla completa + gancho (regla del 26 nov 2026).
Uso: python3 make_photo_cover.py <foto.png|jpg> <salida.jpg> "<chip>" "<cifra grande>" "<línea>" "<línea pequeña>" "<botón>" [acento]
Renderiza con Playwright (Chromium) en 1080x1920 usando las fuentes Inter de styles/node_modules."""
import sys, os, base64, io, json
from PIL import Image
from playwright.sync_api import sync_playwright
HERE = os.path.dirname(os.path.abspath(__file__))
src, out, chip, big, mid, small, btn = sys.argv[1:8]
acc = sys.argv[8] if len(sys.argv) > 8 else '#ffc83d'
im = Image.open(src).convert('RGB').resize((1080, 1920), Image.LANCZOS)
b = io.BytesIO(); im.save(b, 'JPEG', quality=88); data = base64.b64encode(b.getvalue()).decode()
T = json.dumps(dict(chip=chip, big=big, mid=mid, small=small, btn=btn, acc=acc), ensure_ascii=False)
html = f"""<!doctype html><html><head><meta charset="utf-8"><style>
@font-face{{font-family:Inter;font-weight:800;src:url(node_modules/@fontsource/inter/files/inter-latin-800-normal.woff2)}}
@font-face{{font-family:Inter;font-weight:900;src:url(node_modules/@fontsource/inter/files/inter-latin-900-normal.woff2)}}
html,body{{margin:0;background:#000}}</style></head><body><canvas id="c" width="1080" height="1920"></canvas><script>
const P={T};const cv=document.getElementById('c'),ctx=cv.getContext('2d'),W=1080,H=1920;
function fz(s,sz,maxW,w=900){{ctx.font=w+' '+sz+'px Inter';const m=ctx.measureText(s).width;return m>maxW?Math.floor(sz*maxW/m):sz}}
function S(s,y,sz,col,maxW=980,blur=26){{sz=fz(s,sz,maxW);ctx.save();ctx.font='900 '+sz+'px Inter';ctx.textAlign='center';ctx.textBaseline='middle';
  ctx.shadowColor='rgba(0,0,0,1)';ctx.shadowBlur=blur;ctx.lineJoin='round';ctx.lineWidth=Math.max(6,sz*.06);ctx.strokeStyle='rgba(0,0,0,.55)';ctx.strokeText(s,540,y);ctx.fillStyle=col;ctx.fillText(s,540,y);ctx.restore()}}
const img=new Image();img.onload=async()=>{{await document.fonts.load('900 40px Inter');await document.fonts.load('800 40px Inter');
  ctx.drawImage(img,0,0,W,H);
  let g=ctx.createLinearGradient(0,0,0,1000);g.addColorStop(0,'rgba(5,6,10,.92)');g.addColorStop(.72,'rgba(5,6,10,.55)');g.addColorStop(1,'rgba(5,6,10,0)');ctx.fillStyle=g;ctx.fillRect(0,0,W,1000);
  g=ctx.createLinearGradient(0,1350,0,H);g.addColorStop(0,'rgba(5,6,10,0)');g.addColorStop(1,'rgba(5,6,10,.7)');ctx.fillStyle=g;ctx.fillRect(0,1350,W,H-1350);
  // chip
  ctx.font='900 36px Inter';const cw=ctx.measureText(P.chip).width+60;ctx.fillStyle='#6fd6ff';ctx.beginPath();ctx.roundRect(540-cw/2,240,cw,64,32);ctx.fill();
  ctx.fillStyle='#0b0d12';ctx.textAlign='center';ctx.textBaseline='middle';ctx.fillText(P.chip,540,273);
  S(P.big,470,250,P.acc,980,40);S(P.mid,650,74,'#ffffff');S(P.small,740,42,'#e8ecf4',980,18);
  ctx.fillStyle=P.acc;ctx.beginPath();ctx.roundRect(170,1560,740,110,55);ctx.fill();ctx.font='900 50px Inter';ctx.fillStyle='#0b0d12';ctx.fillText(P.btn,540,1617);
  window.__done=true}};
img.src='data:image/jpeg;base64,{data}';
</script></body></html>"""
tmp = os.path.join(HERE, '_photo_cover_tmp.html'); open(tmp, 'w').write(html)
with sync_playwright() as p:
    br = p.chromium.launch(); pg = br.new_page(viewport={'width': 1080, 'height': 1920})
    pg.goto('file://' + tmp); pg.wait_for_function('window.__done===true', timeout=20000)
    png = base64.b64decode(pg.evaluate("document.getElementById('c').toDataURL('image/png')").split(',', 1)[1]); br.close()
os.remove(tmp)
Image.open(io.BytesIO(png)).convert('RGB').save(out, quality=90)
print('ok', out)
