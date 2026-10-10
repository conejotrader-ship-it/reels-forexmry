import sys,json
from playwright.sync_api import sync_playwright
from PIL import Image
jobs=[a.split(':') for a in sys.argv[1:]]  # scene:t1,t2,...
with sync_playwright() as p:
    b=p.chromium.launch(args=['--use-gl=angle','--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist'])
    pg=b.new_page(viewport={'width':420,'height':700},device_scale_factor=2)
    pg.on('console',lambda m:print('console:',m.text));pg.on('pageerror',lambda e:print('pageerror:',e))
    pg.goto('file:///home/claude/pixel/pixel5.html');pg.wait_for_function('window.__ready===true',timeout=20000)
    for sc,ts in jobs:
        pg.evaluate(f'window.__load({sc})')
        ims=[]
        for t in ts.split(','):
            pg.evaluate(f'window.__seek({t})');fn=f's{sc}_{t}.png';pg.locator('#stage').screenshot(path=fn);ims.append(Image.open(fn).resize((360,640)))
        sheet=Image.new('RGB',(360*len(ims),640));[sheet.paste(im,(360*i,0)) for i,im in enumerate(ims)];sheet.save(f'sheet{sc}.jpg',quality=88)
    b.close()
