"""Renderiza un reel de estilo canvas. Uso: python3 render_canvas.py <pagina.html> <escena> [a:b] | cover <pagina.html> <salida.png> | sheet <pagina.html> <t1,t2,...> <salida.jpg>"""
import sys, os, base64, json
from playwright.sync_api import sync_playwright
FPS = 30
def page(br, html):
    pg = br.new_page(viewport={'width':1080,'height':1920}, device_scale_factor=1)
    pg.on('pageerror', lambda e: print('pageerror:', e, flush=True))
    pg.on('console', lambda m: print('console:', m.text, flush=True) if m.type == 'error' else None)
    pg.goto('file://' + os.path.abspath(html)); pg.wait_for_function('window.__ready===true', timeout=20000)
    return pg
def b64(s): return base64.b64decode(s.split(',',1)[1])
with sync_playwright() as p:
    br = p.chromium.launch()
    m = sys.argv[1]
    if m == 'cover':
        pg = page(br, sys.argv[2]); pg.evaluate('__cover()'); open(sys.argv[3],'wb').write(b64(pg.evaluate('__png()')))
    elif m == 'sheet':
        from PIL import Image
        import io
        pg = page(br, sys.argv[2]); ts = [float(x) for x in sys.argv[3].split(',')]; ims = []
        for t in ts:
            pg.evaluate(f'__seek({t})'); ims.append(Image.open(io.BytesIO(b64(pg.evaluate('__frame()')))).resize((360,640)))
        sh = Image.new('RGB', (360*len(ims), 640))
        for i, im in enumerate(ims): sh.paste(im, (360*i, 0))
        sh.save(sys.argv[4], quality=88)
    else:
        html, sc = sys.argv[1], int(sys.argv[2]); a, b = (int(x) for x in sys.argv[3].split(':')) if len(sys.argv) > 3 else (0, 630)
        pg = page(br, html)
        if a == 0: open(f'/home/claude/pixel/scene{sc}.json','w').write(pg.evaluate('__load()'))
        d = f'/home/claude/pixel/frames5/s{sc}'; os.makedirs(d, exist_ok=True)
        for i in range(a, b):
            pg.evaluate(f'__seek({i/FPS})'); open(f'{d}/f{i:04d}.jpg','wb').write(b64(pg.evaluate('__frame()')))
            if i % 90 == 0: print(sc, i, flush=True)
    br.close()
