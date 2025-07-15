def extrair_features(audio_path, pasta_saida='"C:/Users/adria/PycharmProjects/WorkSpace/alzheimer-parkinson-ai/data/audio/features"'):
    import librosa
    import numpy as np
    import pandas as pd
    import os

    if not os.path.isfile(audio_path):
        raise FileNotFoundError(f"Arquivo de áudio não encontrado em: {audio_path}")

    # Carregar áudio
    y, sr = librosa.load(audio_path, sr=None)

    # MFCCs
    mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)
    mfcc_means = np.mean(mfccs, axis=1)

    # Pitch
    f0 = librosa.yin(y, fmin=50, fmax=300, sr=sr)
    f0_valid = f0[~np.isnan(f0)]
    pitch_mean = np.mean(f0_valid)
    pitch_std = np.std(f0_valid)

    # Jitter
    diff_f0 = np.abs(np.diff(f0_valid))
    jitter = np.mean(diff_f0)

    # Montar o dicionário
    features_dict = {
        'arquivo': os.path.basename(audio_path),
        'jitter': jitter,
        'pitch_medio': pitch_mean,
        'pitch_std': pitch_std
    }

    for i, val in enumerate(mfcc_means):
        features_dict[f'mfcc{i+1}_medio'] = val

    df = pd.DataFrame([features_dict])

    # Nome do arquivo de saída
    nome_csv = os.path.basename(audio_path).replace('.wav', '_features.csv')
    caminho_csv = os.path.join(pasta_saida, nome_csv)

    # Salvar
    df.to_csv(caminho_csv, index=False)

    print(f"[✓] Features salvas: {caminho_csv}")
    return features_dict


# Teste unitário
if __name__ == "__main__":
    caminho = "C:/Users/adria/PycharmProjects/WorkSpace/alzheimer-parkinson-ai/data/audio/raw_wav/voice002.wav"
    extrair_features(caminho, pasta_saida="C:/Users/adria/PycharmProjects/WorkSpace/alzheimer-parkinson-ai/data/audio/features")

