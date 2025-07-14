import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

# Caminho do diretório com seus áudios VOICED
audio_dir = Path("data/audio/raw_wav")

# Verifica se há arquivos .wav
wav_files = list(audio_dir.glob("*.wav"))
if not wav_files:
    raise FileNotFoundError("Nenhum arquivo .wav encontrado em 'data/audio/spectrograms'.")

# Carrega o primeiro arquivo encontrado
audio_path = wav_files[0]
print(f"Arquivo carregado: {audio_path.name}")
y, sr = librosa.load(audio_path, sr=None)

# Extrai MFCCs
mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)

# Mostra informações básicas
print(f"Duração: {librosa.get_duration(y=y, sr=sr):.2f} segundos")
print(f"Taxa de amostragem: {sr} Hz")
print(f"MFCC shape: {mfcc.shape}")

# Plot dos MFCCs
plt.figure(figsize=(10, 4))
librosa.display.specshow(mfcc, x_axis='time')
plt.colorbar()
plt.title(f"MFCC - {audio_path.name}")
plt.tight_layout()
plt.show()
