import re,sys
W,H=int(sys.argv[1]),int(sys.argv[2])
src=open('/tmp/claude-0/-home-claude/fa35dd04-da4e-562c-82b7-45a62fe8b377/scratchpad/reels-securus-apex.html',encoding='utf8').read()
src=re.sub(r'<link[^>]*>\n','',src)
src=src.replace('<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>','<script src="three.min.js"></script>')
src=src.replace('renderer.setSize(540,960,false)','renderer.setSize(%d,%d,false)'%(W,H))
ff=''.join('@font-face{font-family:"%s";font-weight:%s;src:url(fonts/%s.woff2) format("woff2")}\n'%x for x in [("Barlow Condensed",600,"barlow-condensed-latin-600-normal"),("Barlow Condensed",700,"barlow-condensed-latin-700-normal"),("Barlow",400,"barlow-latin-400-normal"),("Barlow",500,"barlow-latin-500-normal")])
css='<style>'+ff+'''body{padding:0!important;background:#000!important}
main>header,.tabs,.ctrl,.side,.bar,.bigplay{display:none!important}
main{max-width:none!important;display:block!important}.wrap{display:block!important}
.stage{width:360px!important;max-width:none!important;margin:0!important;border:0!important;border-radius:0!important}</style>'''
src=src.replace('select(0,false);requestAnimationFrame(frame)}','select(0,false)}')
hook='window.__rc={load:function(i){load(i);poster=false;big.hidden=true;playing=false},seek:function(tt){t=tt;upd(tt);camera.position.set(Math.sin(t*.35)*.16,Math.cos(t*.27)*.09,10);camera.lookAt(0,0,0);renderer.render(scene,camera);lastSub=-2;dom()}};\n'
i=src.rindex('})();');src=src[:i]+hook+src[i:]
open('export.html','w',encoding='utf8').write('<!doctype html><meta charset="utf-8">'+css+src)
