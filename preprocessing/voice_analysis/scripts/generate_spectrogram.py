import librosa
import matplotlib.pyplot as plt
import librosa.display
import numpy as np
import os

# Caminho para o arquivo real (exemplo)
audio_path = "C:/Users/adria/PycharmProjects/WorkSpace/alzheimer-parkinson-ai/data/audio/raw_wav/voice001.wav"

# Verificação se o arquivo existe
if not os.path.isfile(audio_path):
    raise FileNotFoundError(f"Arquivo de áudio não encontrado em: {audio_path}")

# Carregar áudio
y, sr = librosa.load(audio_path, sr=None)

# Duração e taxa de amostragem
print(f'Duração: {len(y)/sr:.2f} segundos')
print(f'Taxa de amostragem: {sr} Hz')

# Converter para espectrograma de Mel
S = librosa.feature.melspectrogram(y=y, sr=sr, n_mels=128)
S_dB = librosa.power_to_db(S, ref=np.max)

# Plotar
plt.figure(figsize=(10, 4))
librosa.display.specshow(S_dB, sr=sr, x_axis='time', y_axis='mel')
plt.colorbar(format='%+2.0f dB')
plt.title('Espectrograma de Mel')
plt.tight_layout()
plt.savefig('C:/Users/adria/PycharmProjects/WorkSpace/alzheimer-parkinson-ai/data/audio/spectrograms/voice001_melspec.png')
plt.show()
