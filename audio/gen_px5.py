import numpy as np, soundfile as sf, subprocess, json, sys
from scipy import signal
from kokoro_onnx import Kokoro
SR=44100;DUR=21.0;N=int(SR*DUR)
k=Kokoro('/home/claude/audio/kokoro.onnx','/home/claude/audio/voices.bin')
rs=np.random.default_rng(11)
def say(text,win):
    s,sr=k.create(text,voice='em_alex',speed=1.0,lang='es');d=len(s)/sr
    if d>win:
        s,sr=k.create(text,voice='em_alex',speed=min(1.4,d/win*1.02),lang='es');d=len(s)/sr
    return signal.resample_poly(s,147,80).astype(np.float32),d
def place(buf,x,t0):
    i=int(t0*SR)
    if i>=len(buf) or i<0:return
    j=min(len(buf),i+len(x));buf[i:j]+=x[:j-i]
def hp(x,f):return signal.sosfilt(signal.butter(2,f,'high',fs=SR,output='sos'),x)
def lp(x,f):return signal.sosfilt(signal.butter(2,f,'low',fs=SR,output='sos'),x)
def pulse(f,n,duty=.25):t=np.arange(n)/SR;return ((f*t)%1<duty)*2.-1
def tri(f,n):t=np.arange(n)/SR;return 2*np.abs(2*((f*t)%1)-1)-1
def note(f,d,amp=.2,duty=.25,dec=8):n=int(d*SR);t=np.arange(n)/SR;return pulse(f,n,duty)*np.exp(-t*dec)*np.minimum(1,t*400)*amp
def seq(fs,gap=.07,d=.09,amp=.2):
    o=np.zeros(int((len(fs)*gap+d+.1)*SR))
    for i,f in enumerate(fs):place(o,note(f,d,amp),i*gap)
    return o
def noise(d,amp,dec):n=int(d*SR);t=np.arange(n)/SR;return hp(rs.standard_normal(n),5000)*np.exp(-t*dec)*amp
def kick(amp=.5):n=int(.2*SR);t=np.arange(n)/SR;ph=2*np.pi*np.cumsum(140*np.exp(-t*20)+45)/SR;return np.sin(ph)*np.exp(-t*14)*amp
def sweep(f0,f1,d,amp=.22):n=int(d*SR);t=np.arange(n)/SR;f=f0+(f1-f0)*(t/d)**1.5;ph=np.cumsum(f)/SR;return (((ph%1)<.5)*2.-1)*np.minimum(1,t*200)*np.minimum(1,(d-t)*30)*amp
mf=lambda m:440*2**((m-69)/12)
def music(bpm,prog):
    beat=60/bpm;step=beat/4;bar=4*beat;mus=np.zeros(N)
    ch=[[mf(r+iv+12) for iv in ([0,3,7,12] if q=='m' else [0,4,7,12])] for r,q in prog];bass=[mf(r-12) for r,q in prog]
    pat=[0,1,2,3,2,1,2,3,0,1,2,3,2,1,3,2]
    for b in range(int(np.ceil(DUR/bar))+1):
        for s in range(16):
            t0=b*bar+s*step
            if t0>=DUR:break
            o=2 if 11<=t0<15 else 1
            place(mus,note(ch[b%4][pat[s]]*o,.11,.13,.25 if s%2 else .5,14),t0)
        for q in range(4):
            t0=b*bar+q*beat
            if t0>=DUR:break
            n=int(.42*SR);place(mus,tri(bass[b%4],n)*np.exp(-np.arange(n)/SR*4)*.3,t0)
            if t0>=bar:place(mus,kick(),t0)
            place(mus,noise(.05,.1,70),t0+beat/2)
    tt=np.arange(N)/SR;g=np.minimum(1,tt/.4)*np.minimum(1,(DUR-tt)/.8)
    mus=mus*g;return mus/np.abs(mus).max()*.5
def scribble(d,amp=.11):
    n=int(d*SR);t=np.arange(n)/SR;x=lp(hp(rs.standard_normal(n),1800),7000)
    env=(0.55+0.45*np.sin(2*np.pi*(7+rs.random()*4)*t+rs.random()*6))*np.minimum(1,t*60)*np.minimum(1,(d-t)*60)
    return x*env*amp
def wipe(d=.5,amp=.35):
    n=int(d*SR);t=np.arange(n)/SR;return lp(rs.standard_normal(n),2200)*np.sin(np.pi*t/d)*amp
def pluck(f,d,amp):
    n=int(d*SR);t=np.arange(n)/SR
    return (np.sin(2*np.pi*f*t)+.35*np.sin(4*np.pi*f*t)*np.exp(-t*10)+.15*np.sin(6*np.pi*f*t)*np.exp(-t*20))*np.exp(-t*6)*np.minimum(1,t*300)*amp
def music_soft(bpm,prog):
    beat=60/bpm;step=beat/2;bar=4*beat;mus=np.zeros(N);pat=[0,2,1,3,2,1,3,2]
    for b in range(int(np.ceil(DUR/bar))+1):
        r,q=prog[b%4];ch=[mf(r+iv+12) for iv in ([0,3,7,12] if q=='m' else [0,4,7,12])]
        for s in range(8):
            t0=b*bar+s*step
            if t0<DUR:place(mus,pluck(ch[pat[s]],.5,.2),t0)
        for q4 in range(2):
            t0=b*bar+q4*2*beat
            if t0<DUR:place(mus,pluck(mf(r-12),1.2,.35),t0)
        for q5 in range(4):
            t0=b*bar+q5*beat+beat/2
            if t0<DUR:place(mus,noise(.04,.05,90),t0)
    tt=np.arange(N)/SR;g=np.minimum(1,tt/.4)*np.minimum(1,(DUR-tt)/.8)
    mus=mus*g;return mus/np.abs(mus).max()*.4
def sfx_events(evs):
    sfx=np.zeros(N)
    for e in evs:
        t0,kind=e[0],e[1];arg=e[2] if len(e)>2 else None
        if kind=='blip':place(sfx,note(arg,.1,.2,.5,10),t0)
        elif kind=='seq':place(sfx,seq(arg,.08,.12,.22),t0)
        elif kind=='chime':place(sfx,seq([784,1175,1568],.09,.3,.2),t0)
        elif kind=='hit':
            place(sfx,noise(.35,.55,8),t0);place(sfx,kick(.7),t0)
        elif kind=='alert':place(sfx,seq([880,660,880,660],.12,.1,.24),t0)
        elif kind=='rise':place(sfx,sweep(200,1400,arg),t0)
        elif kind=='down':place(sfx,seq([700,520,380],.1,.12,.22),t0)
        elif kind=='power':place(sfx,sweep(900,120,.7,.25),t0)
        elif kind=='ding':place(sfx,note(1320,.5,.25,.5,6),t0)
        elif kind=='tick':place(sfx,note(1500,.03,.15,.5,40),t0)
        elif kind=='scribble':place(sfx,scribble(arg),t0)
        elif kind=='wipe':place(sfx,wipe(),t0)
        elif kind=='cta':place(sfx,seq([659,784,988,1319],.09,.16,.22),t0)
    return sfx
for sc in ([int(x) for x in sys.argv[1:]] or range(5)):
    d=json.load(open(f'/home/claude/pixel/scene{sc}.json'));DUR=float(d.get('dur',21.0));N=int(SR*DUR)
    voice=np.zeros(N)
    for a,b,tx,*sp in d['subs']:
        s,dd=say(sp[0] if sp else tx,b-a-.25);place(voice,s,a+.12);print(sc,a,round(dd,2),'/',round(b-a,2),flush=True)
    voice*=.9/np.abs(voice).max()
    mus=(music_soft if d.get('mus')=='soft' else music)(d['bpm'],d['prog']);sfx=sfx_events(d['ev'])
    sf.write(f'/home/claude/audio/v5_{sc}.wav',voice,SR);sf.write(f'/home/claude/audio/m5_{sc}.wav',np.clip(mus+sfx,-1,1),SR)
