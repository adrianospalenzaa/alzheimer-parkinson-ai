import pandas as pd
import spacy
import os

# Carregar o modelo SpaCy para português
nlp = spacy.load("pt_core_news_sm")

# Caminho do CSV original
caminho_csv = "C:/Users/adria/PycharmProjects/alzheimer-parkinson-ai/data/text/text_adresso_fake.csv"

# Carregar os dados
df = pd.read_csv(caminho_csv)

# Função de limpeza e lematização
def limpar_texto(texto):
    doc = nlp(str(texto))
    tokens = [token.lemma_.lower() for token in doc if not token.is_stop and not token.is_punct]
    return " ".join(tokens)

# Aplicar função em todos os textos
df["text_processado"] = df["text"].apply(limpar_texto)


print(df[["text", "text_processado"]].head())

# Salvar novo CSV com coluna tratada
saida = "C:/Users/adria/PycharmProjects/alzheimer-parkinson-ai/data/text/text_processado.csv"
df.to_csv(saida, index=False)
print(f"[✓] Texto pré-processado salvo em: {saida}")



def extrair_metrica_gramatical(texto):
    doc = nlp(str(texto))

    pronomes = sum(1 for token in doc if token.pos_ == "PRON")
    verbos = sum(1 for token in doc if token.pos_ == "VERB")
    verbos_passado = sum(1 for token in doc if token.tag_ == "VMI")  # Verbo, modo indicativo passado

    frases = list(doc.sents)
    qtd_frases = len(frases)
    total_tokens = len([t for t in doc if not t.is_punct])
    media_tokens_por_frase = total_tokens / qtd_frases if qtd_frases > 0 else 0

    return pd.Series([pronomes, verbos, verbos_passado, qtd_frases, media_tokens_por_frase])

# Aplicar em todos os textos
df[["qtd_pronomes", "qtd_verbos", "qtd_verbos_passado", "qtd_frases", "media_tokens_por_frase"]] = df["text"].apply(extrair_metrica_gramatical)

# Salvar CSV com métricas linguísticas
saida_final = "C:/Users/adria/PycharmProjects/alzheimer-parkinson-ai/data/text/text_com_metrica.csv"
df.to_csv(saida_final, index=False)
print(f"[✓] Métricas linguísticas salvas: {saida_final}")

