# Reels @forexmry — Robot De Oro Mr. Y 10.0 Securus Apex

Sistema para producir y programar reels educativos de Instagram (estilo pixel-art 3D con Three.js, voz en español y música/sfx chiptune).

## Flujo
1. `./setup.sh` — copia el código a `/home/claude`, instala dependencias y descarga el modelo de voz (Kokoro).
2. Definir la escena en `pixel/pixel5.html` (arreglo `SC`: nombre, hook, bpm, progresión, eventos de sonido, subtítulos).
3. `cd /home/claude/pixel && python3 render5.py <escena>:0:630` — genera los frames (SwiftShader, 1080x1920, 30 fps, 21 s). Con 2 procesos en paralelo se divide por rangos de frames.
4. `cd /home/claude/audio && python3 gen_px5.py <escena>` — genera voz (`v5_N.wav`) y música+sfx (`m5_N.wav`) desde `pixel/sceneN.json`.
5. `python3 pixel/build_pixel.py <escena> salida.mp4` — arma el video con audio (sidechain de la voz sobre la música).
6. Subir el MP4 a `videos/` y hacer push. El enlace directo es
   `https://raw.githubusercontent.com/conejotrader-ship-it/reels-forexmry/main/videos/<archivo>.mp4`
7. Programar en Metricool (blogId 7337805, zona America/Bogota) con `createScheduledPost`: tipo REEL, `showReelOnFeed: true`, `isAiGenerated: true`. Metricool copia el video a sus servidores, así que el enlace de GitHub solo se usa al programar.

## Carpetas
- `pixel/` — plantilla pixel-art y scripts de render.
- `audio/` — voz y música (`gen_px5.py` es la versión vigente).
- `three/` — reels Three.js originales y su exportador.
- `scenes/` — JSON de las 5 escenas actuales (referencia).
- `videos/` — MP4 publicados.
- `docs/calendario.md` — temas por día y reglas de hashtags.

## Notas
- Subtítulos siempre en la parte inferior de la pantalla (arriba los tapa la interfaz de Instagram).
- Mantener los temas ligados al trading; no usar los temas ya producidos.
- Los modelos de voz y los frames no se versionan (ver `.gitignore`).

## Estilos canvas 2D (`styles/`)
Motor liviano (`common.js`) para reels de estilos distintos, sin WebGL. Cada página define `SPEC` (subtítulos, bpm, acordes, eventos de sonido), `draw(t)` y `cover()`.
- `v1_spread.html` — velas animadas (spread). `v2_stoploss.html` — infografía. `v3_pip.html` — neón synthwave.
- Frames: `python3 styles/render_canvas.py <pagina.html> <escena>` (escenas 10+). Carátula: `... cover <pagina.html> <salida.png>`. Vista previa: `... sheet <pagina.html> 1,5,9 <salida.jpg>`.
- Audio y ensamble: igual que pixel-art (`audio/gen_px5.py <escena>` y `pixel/build_pixel.py <escena> salida.mp4`).
- Carátulas en `covers/`; se usan como `videoThumbnailUrl` en Metricool. Deben ser llamativas y virales (reglas en `docs/calendario.md`, sección Carátulas).

- Duración y tarjeta final configurables: `SPEC.dur` y `SPEC.cta` en cada página (por defecto 21 s y 17,1 s). En `subs` un 4.º elemento opcional es el texto hablado (por ejemplo números escritos en palabras).
