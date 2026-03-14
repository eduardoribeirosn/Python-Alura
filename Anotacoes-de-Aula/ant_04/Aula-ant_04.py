# Rodando a sua IA no Google Colab

import os
from google import genai

API_teste_gemini = "AIzaSyD3ddagxhQEGIPEvub8_Ldea4OF0ghBuT8"

os.environ["GOOGLE_API_KEY"] = API_teste_gemini

client = genai.Client()

resposta = client.models.generate_content(model="gemini-2.5-flash", contents="O que é a Inteligência Artificial?")
print(resposta.text)
