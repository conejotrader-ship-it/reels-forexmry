"""Ensambla un video pixel-art: frames -> mp4 mudo, mezcla de audio y mux final.
Uso: python3 build_pixel.py <escena 0-4> <nombre_salida.mp4>
Requiere haber corrido antes: render5.py (frames) y audio/gen_px5.py (v5_N.wav, m5_N.wav)."""
import subprocess, sys
sc, out = int(sys.argv[1]), sys.argv[2]
P = '/home/claude/pixel'; A = '/home/claude/audio'
sil = f'{P}/sil_{sc}.mp4'
subprocess.run(['ffmpeg','-y','-framerate','30','-i',f'{P}/frames5/s{sc}/f%04d.jpg','-c:v','libx264','-pix_fmt','yuv420p','-crf','18',sil],check=True)
fc = ('[1:a]asplit=2[v1][v2];[2:a][v1]sidechaincompress=threshold=0.03:ratio=8:attack=5:release=250[mduck];'
      '[v2][mduck]amix=inputs=2:normalize=0,alimiter=limit=0.95[a]')
subprocess.run(['ffmpeg','-y','-i',sil,'-i',f'{A}/v5_{sc}.wav','-i',f'{A}/m5_{sc}.wav','-filter_complex',fc,
                '-map','0:v','-map','[a]','-c:v','copy','-c:a','aac','-b:a','192k','-shortest',out],check=True)
