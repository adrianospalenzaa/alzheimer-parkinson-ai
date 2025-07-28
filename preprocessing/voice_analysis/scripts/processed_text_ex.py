import pandas as pd
import spacy

# Carregar o modelo SpaCy em português
nlp = spacy.load("pt_core_news_sm")

# Caminho do CSV
caminho_csv = "C:/Users/adria/PycharmProjects/alzheimer-parkinson-ai/data/text/text_adresso_fake.csv"

# Ler o CSV
df = pd.read_csv(caminho_csv)

# Selecionar o primeiro texto
texto_original = df.loc[0, "text"]
print("Texto original:\n", texto_original)

# Processar com SpaCy
doc = nlp(texto_original)

# Obter tokens lematizados, ignorando pontuação e stopwords
tokens_limpos = [token.lemma_.lower() for token in doc if not token.is_stop and not token.is_punct]

print("\nTexto lematizado e limpo:")
print(" ".join(tokens_limpos))
