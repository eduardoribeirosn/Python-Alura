# Desafio Python: Inteligência Artificial Aplicada > 04 > 05

import pandas as pd
import os
from groq import Groq
from dotenv import load_dotenv
import json

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

lista_de_perguntas = [
    "O que é velocidade?",
    "Qual é a unidade de força no Sistema Internacional (SI)?",
    "O que acontece com um objeto quando nenhuma força resultante atua sobre ele?",
    "Qual é a fórmula da velocidade média?",
    "O que é energia cinética?"
]

with open("lista_de_perguntas.txt", "w", encoding="utf-8") as arquivo:
    for pergunta in lista_de_perguntas:
        arquivo.write(pergunta + "\n")

nova_lista_de_perguntas = []
with open("lista_de_perguntas.txt", "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        nova_lista_de_perguntas.append(linha.strip())

response = client.chat.completions.create(
    model="openai/gpt-oss-20b",
    messages=[
        {
            "role": "user",
            "content": f"""Responda as seguintes perguntas: {' Pergunta: '.join(nova_lista_de_perguntas)} . No formato JSON como 'Respostas': ['Resp1', 'Resp2', 'Resp3', 'Resp4', 'Resp5']"""
        }
    ]
)

lista_de_respostas = response.choices[0].message.content
lista_de_respostas = lista_de_respostas.replace("```json", "").replace("```", "".strip())
lista_de_respostas = json.loads(lista_de_respostas)

with open("arquivo.csv", "w", encoding="utf-8") as arquivo:
    arquivo.write("pergunta,resposta\n")
    for i, pergunta in enumerate(nova_lista_de_perguntas):
        arquivo.write(f'"{pergunta.strip()}","{lista_de_respostas["Respostas"][i].strip()}"\n')

df = pd.read_csv("arquivo.csv")

print(df)