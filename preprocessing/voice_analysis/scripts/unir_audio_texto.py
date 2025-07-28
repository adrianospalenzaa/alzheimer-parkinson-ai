import pandas as pd
import os
from glob import glob

# Pasta com os CSVs de features de áudio
pasta_audio = "C:/Users/adria/PycharmProjects/alzheimer-parkinson-ai/data/audio/features"

# CSV com os textos já processados
caminho_texto = "C:/Users/adria/PycharmProjects/alzheimer-parkinson-ai/data/text/text_com_metrica.csv"
df_texto = pd.read_csv(caminho_texto)

# Criar coluna 'id' no texto
df_texto["id"] = "voice" + df_texto.index.astype(str).str.zfill(3)

# Ler e juntar todos os CSVs de áudio
arquivos_audio = glob(os.path.join(pasta_audio, "*.csv"))
print("[DEBUG] Arquivos de áudio encontrados:", len(arquivos_audio))
df_audio = pd.concat([pd.read_csv(f) for f in arquivos_audio])

# Criar coluna 'id' no áudio
df_audio["id"] = df_audio["arquivo"].str.replace(".wav", "", regex=False)

# Unir os dados
df_final = pd.merge(df_texto, df_audio, on="id")

# Reorganizar colunas
colunas_final = ['id', 'label', 'text_processado'] + \
                [c for c in df_texto.columns if c.startswith("qtd_") or c.startswith("media")] + \
                [c for c in df_audio.columns if c not in ["arquivo", "id"]]

df_final = df_final[colunas_final]

# Salvar dataset final
saida = "C:/Users/adria/PycharmProjects/alzheimer-parkinson-ai/data/dataset final/dataset_final.csv"
df_final.to_csv(saida, index=False)
print(f"[✓] Dataset final salvo: {saida}")
