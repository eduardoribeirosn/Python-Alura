# Desafio -> Python: Inteligência Artificial Aplicada > 06 > 07

from openai import OpenAI
import json

client_openai = OpenAI(
    base_url="http://127.0.0.1:1234/v1",
    api_key="lm_studio"
)

lista_de_resenhas = []
with open("Resenhas_App_ChatGPT.txt", "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        lista_de_resenhas.append(linha.strip())

# print(lista_de_resenhas)

lista_de_resenhas = lista_de_resenhas[:2]

lista_json_AI = []
lista_text_responses = ""

for item in lista_de_resenhas:
    response = client_openai.chat.completions.create(
        model="google/gemma-3-1b",
        messages = [
            {
                "role": "user",
                "content": f'Retorne um JSON sobre o item que irei te mandar da seguinte maneira, Exemplo: {{"usuario": "Sasuke", "resenha original": "this is very good", "resenha_pt": "isso ficou muito bom", "avaliacao": "algo entre (Positiva, Negativa ou Neutra)"}}. Me envie apenas o JSON. Item: {item}'
            }
        ],
        temperature=1.0
    )

    response_current = response.choices[0].message.content

    print(response_current)

    response_current_formatted = response_current.replace("```json", "").replace("```", "").strip()
    response_current_formatted_json = json.loads(response_current_formatted)

    lista_json_AI.append(response_current_formatted_json)

    for item in response_current_formatted_json.values():
        lista_text_responses += item + "###"

positiva = 0
negativa = 0
neutra = 0
for itemLista in lista_json_AI:
    if itemLista["avaliacao"] == "Positiva":
        positiva += 1
    elif itemLista["avaliacao"] == "Negativa":
        negativa += 1
    elif itemLista["avaliacao"] == "Neutra":
        neutra += 1

# SIMPLESMENTE CANSEI kkk, vou dormir que eu ganho MAIS............

print(lista_json_AI)
print()
print()
print()
print("-----")
print(positiva)
print(neutra)
print(negativa)
print()
print()
print()
print("-----")
print(lista_text_responses)