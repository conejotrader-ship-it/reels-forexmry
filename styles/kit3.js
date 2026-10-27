// ---- KIT 3: primitivas de gráficos y bloques para reels de 60 s (requiere common.js y kit2.js ya cargados) ----
// La página define ST = {fam,w,txt,mu,acc,pn,c:[4 colores],mono,panel(x,y,w,h,col),bg(t)}
const ST={fam:'Inter',w:900,txt:'#fff',mu:'#aaa',acc:'#fff',pn:'#222',c:['#fff','#fff','#fff','#fff'],mono:false,panel:null};
function fx(s){s=String(s);return ST.mono?s.replace(/≈/g,'~').replace(/−/g,'-').replace(/→/g,'>').replace(/×/g,'x'):s}
function Lb(s,x,y,sz,col,a=1,al='center',w){T(fx(s),x,y,{font:`${w||ST.w} ${sz}px ${ST.fam}`,fill:col||ST.txt,a,align:al})}
function head(t,t0,s,col){Lb(s,540,175,52,col||ST.acc,eout(prog(t,t0,t0+.5)))}
function panel(x,y,w,h,col){if(ST.panel)ST.panel(x,y,w,h,col);else{ctx.save();ctx.fillStyle=ST.pn;RR(x,y,w,h,22);ctx.fill();ctx.lineWidth=6;ctx.strokeStyle=col;ctx.stroke();ctx.restore()}}
// aparece con rebote en (cx,cy); fn dibuja centrado en 0,0
function pop(t,t0,cx,cy,fn){const k=eback(prog(t,t0,t0+.7));if(k<=.02)return;ctx.save();ctx.translate(cx,cy);ctx.scale(k,k);fn();ctx.restore()}
function bigNum(t,t0,cx,cy,txt,sz,col){pop(t,t0,cx,cy,()=>Lb(txt,0,0,sz,col))}
function slide(t,t0,fn,dx=-70){const k=eout(prog(t,t0,t0+.6));if(k<=.02)return;ctx.save();ctx.globalAlpha*=k;ctx.translate(lerp(dx,0,k),0);fn();ctx.restore()}
// tarjeta ancha con 1 o 2 líneas
function card(t,t0,y,h,col,l1,l2,sz=42){slide(t,t0,()=>{panel(60,y,960,h,col);if(l2){Lb(l1,100,y+h*.36,sz,ST.txt,1,'left');Lb(l2,100,y+h*.72,Math.round(sz*.72),col,1,'left')}else Lb(l1,100,y+h/2,sz,ST.txt,1,'left')})}
// polilínea con revelado; pts normalizados [u,v] (v hacia arriba)
function pathPts(pts,x,y,w,h){return pts.map(([u,v])=>[x+u*w,y+h-v*h])}
function lineChart(t,a,b,pts,x,y,w,h,col,lw=9,glow){const P=pathPts(pts,x,y,w,h);const r=eio(prog(t,a,b));if(r<=0)return null;const n=P.length-1;const lim=r*n;
  ctx.save();ctx.lineWidth=lw;ctx.strokeStyle=col;ctx.lineJoin='round';ctx.lineCap='round';if(glow){ctx.shadowColor=col;ctx.shadowBlur=glow}
  ctx.beginPath();ctx.moveTo(P[0][0],P[0][1]);let hx=P[0][0],hy=P[0][1];
  for(let i=1;i<=n;i++){if(i-1>=lim)break;let q=P[i];if(i>lim){const f=lim-(i-1);q=[lerp(P[i-1][0],P[i][0],f),lerp(P[i-1][1],P[i][1],f)]}ctx.lineTo(q[0],q[1]);hx=q[0];hy=q[1]}
  ctx.stroke();ctx.restore();ctx.save();ctx.fillStyle=col;ctx.beginPath();ctx.arc(hx,hy,lw*1.2,0,7);ctx.fill();ctx.restore();return [hx,hy]}
function axes(x,y,w,h,col,lab){ctx.save();ctx.strokeStyle=col;ctx.lineWidth=3;ctx.globalAlpha*=.6;ctx.beginPath();ctx.moveTo(x,y);ctx.lineTo(x,y+h);ctx.lineTo(x+w,y+h);ctx.stroke();ctx.restore();if(lab)Lb(lab,x+w,y+h+36,26,ST.mu,1,'right')}
function hline(y,col,lw=4,x1=60,x2=1020){line(x1,y,x2,y,col,lw,[14,10])}
function ring(t,t0,cx,cy,r,col){const k=eout(prog(t,t0,t0+.8));if(k<=.02)return;ctx.save();ctx.strokeStyle=col;ctx.lineWidth=8;ctx.globalAlpha*=1-k*.5;ctx.beginPath();ctx.arc(cx,cy,r*(.6+k*.8),0,7);ctx.stroke();ctx.restore()}
// barras verticales: items [etiqueta, valor 0..1, color, texto]
function barsV(t,t0,items,x,y,w,h,gap=30,vsz=44){const n=items.length,bw=(w-gap*(n-1))/n;items.forEach(([lab,v,col,tx],i)=>{const k=eout(prog(t,t0+i*.45,t0+i*.45+.9));if(k<=.01)return;const bh=h*v*k,bx=x+i*(bw+gap);
  ctx.save();ctx.fillStyle=col;RR(bx,y+h-bh,bw,bh,10);ctx.fill();ctx.restore();Lb(tx,bx+bw/2,y+h-bh-34,vsz,ST.txt,k);Lb(lab,bx+bw/2,y+h+40,28,ST.mu,k)})}
// barras horizontales: items [etiqueta, fracción 0..1, color, texto]
function barsH(t,t0,items,x,y,w,rowH=130,sz=38){items.forEach(([lab,v,col,tx],i)=>{const k=eout(prog(t,t0+i*.5,t0+i*.5+.9));if(k<=.01)return;const yy=y+i*rowH;Lb(lab,x,yy,sz,ST.txt,k,'left');
  ctx.save();ctx.globalAlpha*=k;ctx.fillStyle=col;RR(x,yy+34,Math.max(20,(w-10)*v*k),50,12);ctx.fill();ctx.restore();Lb(tx,x+Math.max(20,(w-10)*v*k)+16,yy+60,sz,col,k,'left')})}
// bloque final estándar: Para tu robot / Recuerda
function endBlock(t,a,t0,l1,l2,c1,c2){ctx.save();ctx.globalAlpha=a;head(t,t0+.2,'RECUERDA',ST.c[0]);
  [[l1,c1||ST.c[1]],[l2,c2||ST.c[2]]].forEach(([s,c],i)=>{const k=eout(prog(t,t0+1+i*1.1,t0+1.7+i*1.1));if(k<=.02)return;ctx.save();ctx.translate(lerp(-80,0,k),0);ctx.globalAlpha=a*k;panel(60,290+i*140,960,110,c);Lb(s,110,345+i*140,s.length>26?38:44,ST.txt,1,'left');ctx.restore()});
  robot(300,620,780,eout(prog(t,t0+2.8,t0+3.6)));
  Lb('Contenido educativo,',60,1440,34,ST.c[0],eout(prog(t,t0+4.8,t0+5.4)),'left');Lb('no es asesoría financiera',60,1490,34,ST.c[0],eout(prog(t,t0+4.8,t0+5.4)),'left');ctx.restore()}
// motor de bloques: BL = [[a,b,fn(t,a)]...]; hook en 0..6
function drawBlocks(t,BL){ST.bg(t);for(const [a,b,fn,fade0] of BL){let al=fade(t,a,b);if(a==0&&t<.3)al=1;if(al>0)fn(t,al)}
  const al=fade(t,49.8,55.9);if(al>0)outro(t,al)}
