import numpy as np, soundfile as sf, subprocess
from scipy import signal
from kokoro_onnx import Kokoro
SR=44100;DUR=21.0;N=int(SR*DUR)
k=Kokoro('kokoro.onnx','voices.bin')
V=[(0,3.6,'Un grid abre operaciones a distancias fijas.'),(3.6,7.4,'Si el precio baja, compra un nivel más abajo.'),(7.4,11,'Cuando regresa, cierra todo en ganancia.'),(11,15,'Pero si la tendencia sigue en contra, las operaciones se acumulan.'),(15,18.4,'El Securus Apex limita la operativa en los parabólicos.'),(18.4,21,'Securus Apex. Link en bio.')]
def say(text,win):
    s,sr=k.create(text,voice='em_alex',speed=1.0,lang='es');d=len(s)/sr
    if d>win:
        s,sr=k.create(text,voice='em_alex',speed=min(1.4,d/win*1.02),lang='es');d=len(s)/sr
    return signal.resample_poly(s,147,80).astype(np.float32),d
def place(buf,x,t0):
    i=int(t0*SR)
    if i>=len(buf):return
    j=min(len(buf),i+len(x));buf[i:j]+=x[:j-i]
rs=np.random.default_rng(5)
def lp(x,f):return signal.sosfilt(signal.butter(2,f,'low',fs=SR,output='sos'),x)
def hp(x,f):return signal.sosfilt(signal.butter(2,f,'high',fs=SR,output='sos'),x)
def pulse(f,n,duty=.25):t=np.arange(n)/SR;return ((f*t)%1<duty)*2.-1
def tri(f,n):t=np.arange(n)/SR;return 2*np.abs(2*((f*t)%1)-1)-1
def note(f,d,amp=.2,duty=.25,dec=8):n=int(d*SR);t=np.arange(n)/SR;return pulse(f,n,duty)*np.exp(-t*dec)*np.minimum(1,t*400)*amp
def seq(fs,gap=.07,d=.09,amp=.2):
    o=np.zeros(int((len(fs)*gap+d+.1)*SR))
    for i,f in enumerate(fs):place(o,note(f,d,amp),i*gap)
    return o
def noise(d,amp,dec):n=int(d*SR);t=np.arange(n)/SR;return hp(rs.standard_normal(n),5000)*np.exp(-t*dec)*amp
def kick(amp=.5):n=int(.2*SR);t=np.arange(n)/SR;ph=2*np.pi*np.cumsum(140*np.exp(-t*20)+45)/SR;return np.sin(ph)*np.exp(-t*14)*amp
# música chiptune 120 bpm, Am F C G
mus=np.zeros(N);step=.125
ch=[[220,261.63,329.63,440],[174.61,220,261.63,349.23],[261.63,329.63,392,523.25],[196,246.94,293.66,392]]
bass=[110,87.31,130.81,98];pat=[0,1,2,3,2,1,2,3,0,1,2,3,2,1,3,2]
for b in range(int(np.ceil(DUR/2))):
    for s in range(16):
        t0=b*2+s*step
        if t0>=DUR:break
        oct_=2 if 11<=t0<15 else 1
        place(mus,note(ch[b%4][pat[s]]*oct_,.11,.13,.25 if s%2 else .5,14),t0)
    for q in range(4):
        t0=b*2+q*.5
        if t0>=DUR:break
        n=int(.42*SR);place(mus,tri(bass[b%4],n)*np.exp(-np.arange(n)/SR*4)*.3,t0)
        if t0>=2:place(mus,kick(),t0)
        place(mus,noise(.05,.1,70),t0+.25)
g=np.minimum(1,np.arange(N)/SR/.4)*np.minimum(1,(DUR-np.arange(N)/SR)/.8)
mus=mus*g;mus=mus/np.abs(mus).max()*.5
# efectos
sfx=np.zeros(N)
place(sfx,seq([523,784],.08,.1,.22),.05)
for l,s in enumerate([3.8,4.6,5.4,6.2,7.0]):place(sfx,note(500+l*40,.1,.22,.5,10),s)
for l in range(5):place(sfx,seq([880,1320],.06,.08,.2),8.7+l*.18)
place(sfx,seq([660,880,1175],.08,.12,.2),9.0)
for l in range(12):place(sfx,note(420-l*14,.1,.24,.5,10),11+l*.33)
place(sfx,noise(.4,.5,6),14.8)
for l in range(5):place(sfx,note(500+l*40,.1,.22,.5,10),15.3+l*.33)
place(sfx,seq([440,554,659,880,1109],.07,.12,.25),16.8)
place(sfx,seq([659,784,988,1319],.09,.16,.22),18.4)
voice=np.zeros(N)
for a,b,tx in V:
    s,d=say(tx,b-a-.25);place(voice,s,a+.12);print(a,round(d,2),'/',b-a,flush=True)
voice*=.9/np.abs(voice).max()
sf.write('pv.wav',voice,SR);sf.write('pm.wav',np.clip(mus+sfx,-1,1),SR)
