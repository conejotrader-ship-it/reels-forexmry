#!/usr/bin/env python3
"""Compone clips de video IA (Higgsfield) debajo de los textos de una página canvas ya renderizada.
Primero se renderizan los frames normales (render_canvas.py <pagina> <escena>); luego:
  python3 render_anim.py <pagina.html> <escena> <spec.json>
spec.json: {"segs": [{"t0": 0, "t1": 6.2, "clip": "hook.mp4"}, ...], "robot": {"t0": 56.0, "clip": "robot.mp4"}}
- En cada segmento la página se dibuja SIN fondo (ST.bg y PRE/POST vacíos), se exporta PNG con transparencia
  y se pone encima del clip (escalado a 1080x1920, oscurecido arriba y abajo para leer los textos).
- Los bordes del segmento se funden 0,3 s con el frame normal.
- "robot": la tarjeta final se dibuja sin fondo ni robot (window.CTA_VIDEO) y el clip del robot va en un recuadro arriba.
Sobrescribe /home/claude/pixel/frames5/s<escena>/fNNNN.jpg."""
import sys, os, json, base64, io, subprocess, tempfile, glob
import numpy as np
from PIL import Image, ImageFilter
from playwright.sync_api import sync_playwright
FPS = 30; W, H = 1080, 1920
html, sc, specf = sys.argv[1], int(sys.argv[2]), sys.argv[3]
spec = json.load(open(specf)); base = os.path.dirname(os.path.abspath(specf))
FD = f'/home/claude/pixel/frames5/s{sc}'
tmp = tempfile.mkdtemp(prefix=f'anim{sc}_')

def clip_frames(path, n, size=(W, H), name='c'):
    """Extrae n frames del clip, estirando la duración al segmento (sin audio)."""
    d = os.path.join(tmp, name + os.path.basename(path)); os.makedirs(d, exist_ok=True)
    dur = float(subprocess.check_output(['ffprobe', '-v', 'error', '-show_entries', 'format=duration', '-of', 'csv=p=0', path]).decode().strip())
    f = max(1.0, (n / FPS) / dur)
    w, h = size
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', path, '-an', '-vf',
                    f'setpts={f:.4f}*PTS,fps={FPS},scale={w}:{h}:force_original_aspect_ratio=increase,crop={w}:{h}',
                    os.path.join(d, 'k%04d.jpg')], check=True)
    fr = sorted(glob.glob(os.path.join(d, 'k*.jpg')))
    return [fr[min(i, len(fr) - 1)] for i in range(n)]

# máscara de oscurecimiento para leer textos sobre el video
y = np.linspace(0, 1, H)[:, None]
dark = 0.72 * np.ones((H, 1))
top = np.clip(1 - y / (1000 / H), 0, 1) ** 1.2 * 0.80
bot = np.clip((y - 1300 / H) / (1 - 1300 / H), 0, 1) * 0.65
mult = (dark * (1 - top) * (1 - bot))[:, :, None]

def b64png(s): return Image.open(io.BytesIO(base64.b64decode(s.split(',', 1)[1]))).convert('RGBA')

with sync_playwright() as p:
    br = p.chromium.launch(); pg = br.new_page(viewport={'width': W, 'height': H})
    pg.on('pageerror', lambda e: print('pageerror:', e, flush=True))
    pg.goto('file://' + os.path.abspath(html)); pg.wait_for_function('window.__ready===true', timeout=30000)
    pg.evaluate("window._bg=ST.bg;ST.bg=()=>{};try{PRE=()=>{};POST=()=>{}}catch(e){}")
    for s in spec.get('segs', []):
        a, b = int(round(s['t0'] * FPS)), int(round(s['t1'] * FPS)); n = b - a
        cf = clip_frames(os.path.join(base, s['clip']), n, name=f'seg{a}_')
        for k in range(n):
            i = a + k; t = i / FPS
            pg.evaluate(f'__seek({t})'); ov = b64png(pg.evaluate('__png()'))
            v = np.asarray(Image.open(cf[k]).convert('RGB'), dtype=np.float32) * mult
            bg = Image.fromarray(np.clip(v, 0, 255).astype(np.uint8)).convert('RGBA')
            out = Image.alpha_composite(bg, ov).convert('RGB')
            e = min(k + 1, n - k) / (0.3 * FPS)  # fundido con el frame normal en los bordes
            if e < 1 and os.path.exists(f'{FD}/f{i:04d}.jpg'):
                out = Image.blend(Image.open(f'{FD}/f{i:04d}.jpg').convert('RGB'), out, max(0.0, e))
            out.save(f'{FD}/f{i:04d}.jpg', quality=92)
        print(sc, 'seg', s['t0'], s['t1'], 'ok', flush=True)
    r = spec.get('robot')
    if r:
        pg.evaluate('window.CTA_VIDEO=true')
        a = int(round(r['t0'] * FPS)); b = int(round(json.loads(pg.evaluate('__load()'))['dur'] * FPS)); n = b - a
        bh = 880; bw = int(bh * 9 / 16) // 2 * 2
        cf = clip_frames(os.path.join(base, r['clip']), n, size=(bw, bh), name='rob_')
        m = Image.new('L', (bw, bh), 0); mm = Image.new('L', (bw - 80, bh - 80), 255); m.paste(mm, (40, 40)); m = m.filter(ImageFilter.GaussianBlur(28))
        dk = pg.evaluate('DK')
        for k in range(n):
            i = a + k; t = i / FPS
            pg.evaluate(f'__seek({t})'); ov = b64png(pg.evaluate('__png()'))
            ov2 = Image.new('RGBA', (W, H), dk); ov2.paste(Image.open(cf[k]).convert('RGB'), ((W - bw) // 2, 40), m)
            out = Image.alpha_composite(ov2, ov).convert('RGB')
            kk = min(1.0, (t - r['t0']) / 0.7); kk = 1 - (1 - kk) ** 3
            if kk < 1: out = Image.blend(Image.open(f'{FD}/f{i:04d}.jpg').convert('RGB'), out, kk)
            out.save(f'{FD}/f{i:04d}.jpg', quality=92)
        print(sc, 'robot ok', flush=True)
    br.close()
