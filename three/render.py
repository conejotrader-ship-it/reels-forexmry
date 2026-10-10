import sys,time,os,subprocess
from playwright.sync_api import sync_playwright
FPS=30;DUR=15
reels=[int(x) for x in sys.argv[1:]] or [0,1,2,3,4]
with sync_playwright() as p:
    b=p.chromium.launch(args=['--use-gl=angle','--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist'])
    pg=b.new_page(viewport={'width':420,'height':700},device_scale_factor=3)
    pg.on('console',lambda m:print('console:',m.text,flush=True))
    pg.on('pageerror',lambda e:print('pageerror:',e,flush=True))
    pg.goto('file:///home/claude/export/export.html')
    pg.wait_for_function('window.__rc!==undefined',timeout=20000)
    pg.evaluate('document.fonts.ready')
    st=pg.locator('#stage')
    for r in reels:
        d=f'frames/r{r+1}';os.makedirs(d,exist_ok=True)
        pg.evaluate(f'window.__rc.load({r})')
        t0=time.time()
        for i in range(FPS*DUR):
            pg.evaluate(f'window.__rc.seek({i/FPS})')
            st.screenshot(path=f'{d}/f{i:04d}.jpg',type='jpeg',quality=95)
            if i%30==0:print(f'reel{r+1} {i}/{FPS*DUR} {time.time()-t0:.0f}s',flush=True)
        out=f'reel{r+1}.mp4'
        subprocess.run(['ffmpeg','-y','-loglevel','error','-framerate',str(FPS),'-i',f'{d}/f%04d.jpg','-c:v','libx264','-pix_fmt','yuv420p','-crf','18','-preset','medium','-movflags','+faststart',out],check=True)
        print('done',out,flush=True)
    b.close()
