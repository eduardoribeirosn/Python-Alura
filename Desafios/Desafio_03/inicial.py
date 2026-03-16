# Desafio -> Python: Inteligência Artificial Aplicada > 05 > 05

import pandas as pd
from groq import Groq
from dotenv import load_dotenv
import os
import json

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

feedbacks_client = pd.DataFrame(pd.read_csv("reviews.csv"))

reviewerText = feedbacks_client["reviewText"]

# print(feedbacks_client)

# print(reviewerText)

lista_de_reviewText = []
for test in reviewerText:
    lista_de_reviewText.append(test)

lista_de_reviewText = lista_de_reviewText[:5]

# print(lista_de_reviewText)

response = client.chat.completions.create(
    model="openai/gpt-oss-20b",
    messages=[
        {
            "role": "user",
            "content": f'Classifique o sentimento de cada feedback com uma dessas 3 opções (Positivo, Negativo, Neutro), a lista é essa: {lista_de_reviewText}. -> Devolva no formato JSON, "Feedbacks": ["Positivo", "Negativo", "Positivo", "Neutro", ...] um feedback para cada item da lista.'
        }
    ]
)

feedbacks_client_classifieds = response.choices[0].message.content
feedbacks_client_classifieds = feedbacks_client_classifieds.replace("```json", "").replace("```", "").strip()
feedbacks_client_classifieds = json.loads(feedbacks_client_classifieds)

# df = pd.DataFrame(lista_de_reviewText)

part_feedbacks_client = feedbacks_client[:5].copy() # Utilizando o .copy(), porque posteriormente se eu modificar o pedaço cortado, pode gerar algum erro, o .copy() tira o erro

part_feedbacks_client["Classificação"] = feedbacks_client_classifieds["Feedbacks"]

print(part_feedbacks_client)