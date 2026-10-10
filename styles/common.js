// Motor 2D común para los reels de estilo canvas (1080x1920)
const W=1080,H=1920,cv=document.getElementById('c');cv.width=W;cv.height=H;
const ctx=cv.getContext('2d');
const clamp=(x,a=0,b=1)=>Math.min(b,Math.max(a,x));
const lerp=(a,b,t)=>a+(b-a)*t;
const prog=(t,a,b)=>clamp((t-a)/(b-a));
const eio=x=>{x=clamp(x);return x<.5?4*x*x*x:1-Math.pow(-2*x+2,3)/2};
const eout=x=>1-Math.pow(1-clamp(x),3);
const eback=x=>{x=clamp(x);const c1=1.70158,c3=c1+1;return 1+c3*Math.pow(x-1,3)+c1*Math.pow(x-1,2)};
function rng(seed){let s=seed;return()=>{s=(s*1664525+1013904223)%4294967296;return s/4294967296}}
function T(s,x,y,o={}){ctx.save();ctx.globalAlpha*=o.a==null?1:o.a;ctx.font=o.font||'700 48px Inter';
  ctx.textAlign=o.align||'center';ctx.textBaseline=o.base||'middle';
  if(o.scale){ctx.translate(x,y);ctx.scale(o.scale,o.scale);x=0;y=0}
  if(o.glow){ctx.shadowColor=o.glow;ctx.shadowBlur=o.gb||20}
  if(o.stroke){ctx.lineWidth=o.lw||8;ctx.strokeStyle=o.stroke;ctx.lineJoin='round';ctx.strokeText(s,x,y)}
  ctx.fillStyle=o.fill||'#fff';ctx.fillText(s,x,y);ctx.restore()}
function wrapLines(s,maxW,font){ctx.save();ctx.font=font;const w=s.split(' ');const L=[];let c='';
  for(const x of w){const t=c?c+' '+x:x;if(ctx.measureText(t).width>maxW&&c){L.push(c);c=x}else c=t}
  if(c)L.push(c);ctx.restore();return L}
function RR(x,y,w,h,r){ctx.beginPath();ctx.roundRect(x,y,w,h,r)}
function line(x1,y1,x2,y2,col,lw,dash){ctx.save();ctx.strokeStyle=col;ctx.lineWidth=lw||2;if(dash)ctx.setLineDash(dash);
  ctx.beginPath();ctx.moveTo(x1,y1);ctx.lineTo(x2,y2);ctx.stroke();ctx.restore()}
// Subtítulos en la parte inferior (arriba los tapa la interfaz de Instagram)
function subs(t,st){const s=SPEC.subs.find(([a,b])=>t>=a&&t<b);if(!s)return;const [a,b,tx]=s;
  const al=Math.min(prog(t,a,a+.15),prog(t,b,b-.15));const font=st.subFont||'800 46px Inter';
  const L=wrapLines(tx,880,font);const lh=62,bh=L.length*lh+36,cy=1545;
  ctx.save();ctx.globalAlpha=al;RR(80,cy-bh/2,920,bh,26);ctx.fillStyle=st.subBg||'rgba(0,0,0,.72)';ctx.fill();
  if(st.subStroke){ctx.strokeStyle=st.subStroke;ctx.lineWidth=3;ctx.stroke()}ctx.restore();
  L.forEach((l,i)=>T(l,540,cy-bh/2+18+lh/2+i*lh,{font,fill:st.subFill||'#fff',a:al}))}
// Tarjeta final: producto + CTA
function ctaCard(t,st){const CT=SPEC.cta||17.1;const k=eout(prog(t,CT,CT+.7));if(k<=0)return;ctx.save();ctx.globalAlpha=k;
  ctx.fillStyle=st.ctaBg;ctx.fillRect(0,0,W,H);ctx.restore();
  const y=lerp(40,0,k);
  T('ROBOT DE ORO',540,640+y,{font:st.ctaFontS,fill:st.ctaSub,a:k,glow:st.ctaGlow,gb:18});
  T('MR. Y 10.0',540,770+y,{font:st.ctaFontL,fill:st.ctaMain||'#fff',a:k,glow:st.ctaGlow,gb:22});
  T('SECURUS APEX',540,920+y,{font:st.ctaFontL,fill:st.ctaAccent,a:k,glow:st.ctaGlow,gb:26});
  ctx.save();ctx.globalAlpha=k;RR(240,1060+y,600,110,55);ctx.fillStyle=st.ctaAccent;ctx.fill();ctx.restore();
  T('LINK EN BIO',540,1115+y,{font:st.ctaFontS,fill:st.ctaBtnText,a:k});
  T('@forexmry',540,1230+y,{font:st.ctaFontS,fill:st.ctaMain||'#fff',a:k})}
window.__ready=false;
function boot(fonts){Promise.all(fonts.map(f=>document.fonts.load(f))).then(()=>{window.__ready=true})}
window.__load=()=>JSON.stringify(Object.assign({dur:21},SPEC));
window.__seek=t=>{ctx.clearRect(0,0,W,H);draw(t);ctaCard(t,STY);subs(t,STY)};
window.__cover=()=>{ctx.clearRect(0,0,W,H);cover()};
window.__frame=()=>cv.toDataURL('image/jpeg',.92);
window.__png=()=>cv.toDataURL('image/png');
