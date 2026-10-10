from playwright.sync_api import sync_playwright
with sync_playwright() as p:
    br=p.chromium.launch(args=['--use-gl=angle','--use-angle=swiftshader','--enable-unsafe-swiftshader'])
    pg=br.new_page(viewport={'width':420,'height':700})
    pg.goto('file:///home/claude/pixel/pixel5.html');pg.wait_for_function('window.__ready===true',timeout=20000)
    for sc in range(5):open(f'scene{sc}.json','w').write(pg.evaluate(f'window.__load({sc})'))
    br.close()
