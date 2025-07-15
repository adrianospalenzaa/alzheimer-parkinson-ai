import os
from extrair_features import extrair_features  # importa a função que você criou

# Caminho da pasta com os áudios
pasta_wavs = "C:/Users/adria/PycharmProjects/WorkSpace/alzheimer-parkinson-ai/data/audio/raw_wav"
pasta_saida = "C:/Users/adria/PycharmProjects/WorkSpace/alzheimer-parkinson-ai/data/audio/features"

# Listar todos os arquivos .wav
arquivos = [f for f in os.listdir(pasta_wavs) if f.endswith(".wav")]

# Processar cada arquivo
for arquivo in arquivos:
    caminho_completo = os.path.join(pasta_wavs, arquivo)

    # Nome do arquivo de saída esperado
    nome_saida = arquivo.replace('.wav', '_features.csv')
    caminho_saida = os.path.join(pasta_saida, nome_saida)

    # Verificar se já foi processado
    if os.path.exists(caminho_saida):
        print(f"[↪] Pulando (já processado): {arquivo}")
        continue

    try:
        # Chama a função para extrair e salvar os dados
        extrair_features(caminho_completo, pasta_saida)
    except Exception as e:
        print(f"[✗] Erro ao processar {arquivo}: {e}")
