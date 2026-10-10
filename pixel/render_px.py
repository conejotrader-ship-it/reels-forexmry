import sys,os
from playwright.sync_api import sync_playwright
a,b=int(sys.argv[1]),int(sys.argv[2]);FPS=30
os.makedirs('frames',exist_ok=True)
with sync_playwright() as p:
    br=p.chromium.launch(args=['--use-gl=angle','--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist'])
    pg=br.new_page(viewport={'width':420,'height':700},device_scale_factor=3)
    pg.on('pageerror',lambda e:print('pageerror:',e,flush=True))
    pg.goto('file:///home/claude/pixel/pixel.html');pg.wait_for_function('window.__ready===true',timeout=20000)
    st=pg.locator('#stage')
    for i in range(a,b):
        pg.evaluate(f'window.__seek({i/FPS})');st.screenshot(path=f'frames/f{i:04d}.jpg',type='jpeg',quality=94)
        if i%60==0:print(i,flush=True)
    br.close()
