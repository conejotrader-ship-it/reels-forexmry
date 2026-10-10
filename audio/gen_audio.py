import numpy as np, soundfile as sf, subprocess, sys
from scipy import signal
from kokoro_onnx import Kokoro
SR=44100; DUR=15.0; N=int(SR*DUR)
k=Kokoro('kokoro.onnx','voices.bin')
VOICE='em_alex'
CTA='Securus Apex. Link en bio.'
# (inicio, fin, texto hablado)
V={
1:[(0,3,'El oro puede subir casi en vertical.'),(3,6.5,'Eso es un movimiento parabólico: velas grandes y casi sin retrocesos.'),(6.5,9.5,'Un grid sin protección acumula operaciones en contra.'),(9.5,13,'El Securus Apex lo detecta y limita la operativa.'),(13,15,CTA)],
2:[(0,3,'¿Cómo se detecta un parabólico?'),(3,6,'Mira las E M A veinte, cincuenta y doscientos, en H cuatro.'),(6,9.5,'Sus cruces avisan que el movimiento está acelerando.'),(9.5,13,'El Securus Apex los vigila con I A y limita la operativa.'),(13,15,CTA)],
3:[(0,3,'Mismo movimiento, dos reacciones.'),(3,7,'Un grid sin protección sigue promediando contra el precio.'),(7,11,'Con el Securus Apex, la operativa se limita hasta que cesa.'),(11,13,'Después, el scalping continúa.'),(13,15,CTA)],
4:[(0,3,'¿Cuándo funciona el scalping en oro?'),(3,5.3,'En mercado normal, el robot opera.'),(5.3,8.4,'Si inicia un parabólico, limita la operativa.'),(8.4,13,'Cuando el movimiento cesa, vuelve a hacer scalping.'),(13,15,CTA)],
5:[(0,3,'Tres errores al usar un robot de oro.'),(3,6.5,'Uno: lotaje excesivo para tu capital.'),(6.5,10,'Dos: ignorar las noticias de alto impacto.'),(10,13,'Tres: no tener protección ante parabólicos.'),(13,15,CTA)],
}
BPM={1:92,2:96,3:100,4:96,5:104}
def say(text,win):
    s,sr=k.create(text,voice=VOICE,speed=1.0,lang='es'); d=len(s)/sr
    if d>win:
        sp=min(1.4,d/win*1.02); s,sr=k.create(text,voice=VOICE,speed=sp,lang='es'); d=len(s)/sr
    s=signal.resample_poly(s,147,80).astype(np.float32)
    return s,d
def place(buf,x,t0):
    i=int(t0*SR); j=min(len(buf),i+len(x)); buf[i:j]+=x[:j-i]
def lp(x,f,o=2): return signal.sosfilt(signal.butter(o,f,'low',fs=SR,output='sos'),x)
def hp(x,f,o=2): return signal.sosfilt(signal.butter(o,f,'high',fs=SR,output='sos'),x)
rs=np.random.default_rng(3)
def whoosh(dur=.8,amp=.28):
    n=int(dur*SR); x=rs.standard_normal(n); x=hp(lp(x,5000),400); e=np.sin(np.pi*np.linspace(0,1,n))**2; return x*e*amp
def chime(amp=.28):
    n=int(1.6*SR); t=np.arange(n)/SR; x=sum(np.sin(2*np.pi*f*t)*a for f,a in [(784,1),(1175,.6),(1568,.4),(2093,.2)])*np.exp(-t*3.2); return x*amp/2
def beep(f=880,d=.11,amp=.22):
    n=int(d*SR); t=np.arange(n)/SR; return np.sin(2*np.pi*f*t)*np.minimum(1,t*200)*np.exp(-t*12)*amp
def seq(fs,gap=.13,amp=.22):
    out=np.zeros(int((len(fs)*gap+.2)*SR)); 
    for i,f in enumerate(fs): place(out,beep(f,.12,amp),i*gap)
    return out
def pop(f0=700,amp=.3):
    n=int(.16*SR); t=np.arange(n)/SR; ph=2*np.pi*np.cumsum(f0*np.exp(-t*14)+250)/SR; return np.sin(ph)*np.exp(-t*22)*amp
def riser(dur,amp=.22):
    n=int(dur*SR); t=np.arange(n)/SR; x=rs.standard_normal(n); x=hp(lp(x,7000),600)
    e=np.linspace(0,1,n)**2; ph=2*np.pi*np.cumsum(180+1100*(t/dur)**2)/SR
    return (0.6*x+0.5*np.sin(ph))*e*amp
def music(bpm):
    beat=60/bpm; out=np.zeros(N); t=np.arange(N)/SR
    ch=[[110,164.81,220,261.63],[87.31,174.61,220,261.63],[130.81,196,261.63,329.63],[98,196,246.94,293.66]]
    root=[55,43.65,65.41,49]
    bars=int(np.ceil(DUR/(4*beat)))
    pad=np.zeros(N); bass=np.zeros(N)
    for b in range(bars):
        c=ch[b%4]; s0=int(b*4*beat*SR); s1=min(N,int((b+1)*4*beat*SR)+int(.3*SR)); tt=t[s0:s1]
        seg=np.zeros(len(tt))
        for f in c:
            for dt in (-.4,.4):
                ff=f*(1+dt/100); seg+=2*((ff*tt)%1)-1
        seg=lp(seg,1000)/8
        env=np.minimum(1,(tt-tt[0])/.35)*np.minimum(1,(tt[-1]-tt)/.35)
        pad[s0:s1]+=seg*env
    for st in np.arange(0,DUR,beat/2):
        b=int(st/(4*beat)); r=root[b%4]; n=int(.28*SR); tt=np.arange(n)/SR
        x=lp(2*((r*2*tt)%1)-1,380)*np.exp(-tt*9); place(bass,x*.5,st)
    out+=pad*.55+bass*.5
    for i,st in enumerate(np.arange(0,DUR,beat)):
        if st>=4*beat:
            n=int(.22*SR); tt=np.arange(n)/SR; ph=2*np.pi*np.cumsum(130*np.exp(-tt*18)+45)/SR; place(out,np.sin(ph)*np.exp(-tt*14)*.7,st)
        if st>=2*beat:
            n=int(.05*SR); h=hp(rs.standard_normal(n),7000)*np.exp(-np.arange(n)/SR*70)*.12; place(out,h,st+beat/2)
    g=np.minimum(1,t/.6)*np.minimum(1,(DUR-t)/.9)
    return out*g
EV={1:[(0,'w'),(4.2,'r',3.8),(9.5,'alert'),(13,'c')],2:[(0,'w'),(6.52,'ping'),(13,'c')],3:[(0,'w'),(5.1,'r',2.9),(13,'c')],4:[(0,'w'),(5.3,'down'),(8.4,'up'),(13,'c')],5:[(0,'w'),(3,'pop'),(6.5,'pop'),(10,'pop2'),(13,'c')]}
for r in ([int(x) for x in sys.argv[1:]] or [1,2,3,4,5]):
    voice=np.zeros(N,dtype=np.float64)
    for a,b,txt in V[r]:
        s,d=say(txt,b-a-.25); place(voice,s,a+.12); print(r,a,round(d,2),'/',b-a,flush=True)
    voice*=0.9/max(1e-6,np.abs(voice).max())
    mus=music(BPM[r]); sfx=np.zeros(N)
    for e in EV[r]:
        k_=e[1]
        if k_=='w': place(sfx,whoosh(),e[0])
        elif k_=='r': place(sfx,riser(e[2]),e[0])
        elif k_=='c': place(sfx,chime(),e[0])
        elif k_=='alert': place(sfx,seq([880,660,880,660],.14),e[0])
        elif k_=='ping': place(sfx,seq([988,1319],.1),e[0])
        elif k_=='down': place(sfx,seq([700,520],.12),e[0])
        elif k_=='up': place(sfx,seq([520,780],.12),e[0])
        elif k_=='pop': place(sfx,pop(700),e[0])
        elif k_=='pop2': place(sfx,pop(900),e[0]); place(sfx,seq([660,880,1175],.09,.18),e[0]+.1)
    mus=mus/np.abs(mus).max()*.5
    sf.write(f'voice{r}.wav',voice,SR); sf.write(f'music{r}.wav',np.clip(mus+sfx,-1,1),SR)
    f=f'/home/claude/export/reel{r}.mp4'; o=f'/home/claude/export/reel{r}_sonido.mp4'
    fc='[2:a]volume=0.55[m];[m][1:a]sidechaincompress=threshold=0.02:ratio=10:attack=15:release=350[md];[1:a][md]amix=inputs=2:normalize=0:duration=first,alimiter=limit=0.95[a]'
    subprocess.run(['ffmpeg','-y','-loglevel','error','-i',f,'-i',f'voice{r}.wav','-i',f'music{r}.wav','-filter_complex',fc,'-map','0:v','-map','[a]','-c:v','copy','-c:a','aac','-b:a','192k','-t','15',o],check=True)
    print('done',o,flush=True)
