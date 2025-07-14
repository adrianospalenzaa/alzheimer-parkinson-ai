import spacy
import pandas as pd

# Carrega o modelo em português
nlp = spacy.load("pt_core_news_sm")

# Exemplo de frase com padrão de Alzheimer
texto = "O... o livro, ele... li... ou alguém leu pra mim?"

# Processamento NLP
doc = nlp(texto)

# Extrai token, lema e classe gramatical
tokens_info = [(token.text, token.lemma_, token.pos_) for token in doc]
df = pd.DataFrame(tokens_info, columns=["Token", "Lema", "Classe Gramatical"])

print(df)

