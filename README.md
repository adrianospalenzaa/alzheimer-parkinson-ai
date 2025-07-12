# 🧠 Alzheimer & Parkinson AI

Este projeto tem como objetivo o desenvolvimento de um sistema de **detecção precoce de Alzheimer e Parkinson** utilizando técnicas de **Inteligência Artificial** aplicadas à **fala** e à **escrita** de pacientes.

A solução combina **NLP (Processamento de Linguagem Natural)** e **processamento de sinais de áudio**, com apoio em bases públicas validadas e bibliotecas modernas de machine learning.

---

## 🎯 Objetivo

Criar um protótipo funcional que:
- Analise gravações de fala e textos digitados
- Classifique sinais indicativos de Alzheimer ou Parkinson
- Sirva como apoio a triagens clínicas automatizadas

---

## 🧰 Tecnologias Utilizadas

- Python 3.10+
- [spaCy](https://spacy.io/) – NLP em português
- [Librosa](https://librosa.org/) – Análise de áudio
- [WFDB](https://github.com/MIT-LCP/wfdb-python) – Conversão de sinais médicos (.dat)
- [scikit-learn](https://scikit-learn.org/)
- [Transformers – Hugging Face](https://huggingface.co/)
- Streamlit (interface web)
- Flask ou FastAPI (API backend)

---

## 🗂 Estrutura do Projeto


---

## 📊 Bases de Dados Utilizadas

- **VOICED (PhysioNet):** áudios reais de pacientes com Parkinson
- **ADReSSo Challenge (TalkBank):** transcrições e áudios de pacientes com Alzheimer
- **Texto Simulado:** gerado para prototipagem de NLP

---

## 🧪 Etapas Desenvolvidas

✅ Estrutura inicial configurada  
✅ Pré-processamento de texto e áudio validado  
✅ Conversão de sinais médicos para `.wav`  
✅ Scripts para extração de MFCC e lematização  
🔜 Próxima etapa: vetorização + modelos de IA

---

## 👨‍⚕️ Aplicação Final

Protótipo com interface web que permite:
- Enviar um texto ou áudio de paciente
- Processar e classificar automaticamente
- Retornar risco estimado de Alzheimer ou Parkinson

---

## 📜 Licença

Este projeto é acadêmico, sem fins comerciais. Para fins clínicos ou institucionais, é necessário validar com comitê de ética e aprovação regulatória.

---



