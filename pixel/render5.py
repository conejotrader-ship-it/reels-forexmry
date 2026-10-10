import sys,os,json
from playwright.sync_api import sync_playwright
FPS=30
jobs=[tuple(int(x) for x in a.split(':')) for a in sys.argv[1:]]  # scene:a:b
with sync_playwright() as p:
    br=p.chromium.launch(args=['--use-gl=angle','--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist'])
    pg=br.new_page(viewport={'width':420,'height':700},device_scale_factor=3)
    pg.on('pageerror',lambda e:print('pageerror:',e,flush=True))
    pg.goto('file:///home/claude/pixel/pixel5.html');pg.wait_for_function('window.__ready===true',timeout=20000)
    st=pg.locator('#stage')
    for sc,a,b in jobs:
        info=pg.evaluate(f'window.__load({sc})')
        open(f'scene{sc}.json','w').write(info)
        d=f'frames5/s{sc}';os.makedirs(d,exist_ok=True)
        for i in range(a,b):
            pg.evaluate(f'window.__seek({i/FPS})');st.screenshot(path=f'{d}/f{i:04d}.jpg',type='jpeg',quality=94)
            if i%90==0:print(sc,i,flush=True)
    br.close()
