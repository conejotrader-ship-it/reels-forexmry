#!/usr/bin/env python3
"""Arma la pista de voz v5_<escena>.wav con locuciones de ElevenLabs (una por subtítulo), en lugar de Kokoro.
Uso: python3 mix_elevenlabs.py <escena> <dir_con_s0..sN.mp3>
- Lee /home/claude/pixel/scene<escena>.json (subs) y coloca sN en el inicio del subtítulo N (+0,12 s).
- Recorta silencios, y si la frase no cabe hasta el siguiente subtítulo la acelera con atempo (máx. 1,25; avisa si pasa de 1,15).
- La música y los efectos (m5_<escena>.wav) se siguen generando con gen_px5.py; ejecutarlo ANTES (sobrescribe v5)."""
import sys, os, json, subprocess, tempfile
import numpy as np, soundfile as sf
SR = 44100
sc, d = int(sys.argv[1]), sys.argv[2]
spec = json.load(open(f'/home/claude/pixel/scene{sc}.json')); subs = spec['subs']; DUR = float(spec.get('dur', 60))
voice = np.zeros(int(SR * DUR)); tmp = tempfile.mkdtemp()
for i, s in enumerate(subs):
    a = s[0]; nxt = subs[i + 1][0] if i + 1 < len(subs) else DUR
    room = nxt - a - 0.12 - 0.15
    src = os.path.join(d, f's{i}.mp3'); w = os.path.join(tmp, f't{i}.wav')
    trim = 'silenceremove=start_periods=1:start_threshold=-45dB,areverse,silenceremove=start_periods=1:start_threshold=-45dB,areverse'
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', src, '-ac', '1', '-ar', str(SR), '-af', trim, w], check=True)
    x, _ = sf.read(w); L = len(x) / SR; tempo = 1.0
    if L > room:
        tempo = min(1.25, L / room)
        w2 = os.path.join(tmp, f'u{i}.wav')
        subprocess.run(['ffmpeg', '-v', 'error', '-y', '-i', w, '-af', f'atempo={tempo:.4f}', w2], check=True)
        x, _ = sf.read(w2)
    p = int((a + 0.12) * SR); n = min(len(x), len(voice) - p); voice[p:p + n] += x[:n]
    print(sc, i, a, f'{L:.2f}s / {room:.2f}', f'tempo {tempo:.2f}' + (' (!)' if tempo > 1.15 else ''), flush=True)
voice *= .9 / np.abs(voice).max()
sf.write(f'/home/claude/audio/v5_{sc}.wav', voice, SR)
print('ok', f'/home/claude/audio/v5_{sc}.wav')
