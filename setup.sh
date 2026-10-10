#!/usr/bin/env bash
# Prepara una sesión nueva: copia el código a /home/claude, instala dependencias y descarga el modelo de voz.
set -e
R="$(cd "$(dirname "$0")" && pwd)"
mkdir -p /home/claude/pixel /home/claude/audio /home/claude/export
cp -r "$R"/pixel/. /home/claude/pixel/
cp -r "$R"/audio/. /home/claude/audio/
cp -r "$R"/three/. /home/claude/export/
cp "$R"/scenes/*.json /home/claude/pixel/
pip install --break-system-packages kokoro-onnx soundfile scipy numpy playwright
(cd /home/claude/pixel && npm install)
(cd /home/claude/export && npm install)
B=https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0
[ -f /home/claude/audio/kokoro.onnx ] || curl -L -o /home/claude/audio/kokoro.onnx $B/kokoro-v1.0.onnx
[ -f /home/claude/audio/voices.bin ]  || curl -L -o /home/claude/audio/voices.bin  $B/voices-v1.0.bin
echo OK
