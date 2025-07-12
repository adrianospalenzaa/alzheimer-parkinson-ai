import wfdb
import soundfile as sf
from pathlib import Path

input_dir = Path("data/audio/voiced")
output_dir = input_dir / "converted"
output_dir.mkdir(parents=True, exist_ok=True)

# Processa todos os arquivos .dat
for dat_file in input_dir.glob("*.dat"):
    base_name = dat_file.stem
    record_path = input_dir / base_name

    try:
        record = wfdb.rdrecord(str(record_path))
        signal = record.p_signal[:, 0]  # Primeira faixa de áudio
        sr = int(record.fs)

        wav_path = output_dir / f"{base_name}.wav"
        sf.write(wav_path, signal, sr)
        print(f"✅ Convertido: {wav_path.name}")
    except Exception as e:
        print(f"⚠️ Erro ao converter {base_name}: {e}")
