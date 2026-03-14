# chat com a IA com histórico
import os
from google import genai

API_test_gemini = "AIzaSyD3ddagxhQEGIPEvub8_Ldea4OF0ghBuT8"

os.environ["GOOGLE_API_KEY"] = API_test_gemini

client = genai.Client()

chat = client.chats.create(model="gemini-2.5-flash")

resposta = chat.send_message("Quando lançou o ChatGPT?")

prompt = input("Digite sua pergunta: ")

while prompt != "fim":
    resposta = chat.send_message(prompt)
    print(resposta.text)
    print("\n")
    prompt = input("Digite sua pergunta: ")