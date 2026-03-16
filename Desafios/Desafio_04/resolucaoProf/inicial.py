from retornaJson import recebe_linha_e_retorna_json
import json

# Etapa 1: Ler o arquivo de resenhas
lista_de_resenhas = []
with open("resenhas-app-gpt.txt", "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        lista_de_resenhas.append(linha.strip())

lista_de_resenhas_json = []

lista_de_resenhas = lista_de_resenhas[:4]

for resenha in lista_de_resenhas:
    resenha_json = recebe_linha_e_retorna_json(resenha)
    print(resenha_json)
    resenha_dict = json.loads(resenha_json)
    lista_de_resenhas_json.append(resenha_dict)

print(lista_de_resenhas_json)

def contador_e_juntador(lista_de_dicionarios):
    contador_positivas = 0
    contador_negativas = 0
    contador_neutras = 0

    for dicionario in lista_de_resenhas_json:
        if dicionario['avaliacao'] == 'Positiva':
            contador_positivas += 1
        elif dicionario['avaliacao'] == 'Negativa':
            contador_negativas += 1
        else:
            contador_neutras += 1

    lista_de_dicionarios_str = [str(dicionario) for dicionario in lista_de_dicionarios]
    textos_unidos = "#####".join(lista_de_dicionarios_str)

    return contador_positivas, contador_negativas, contador_neutras, textos_unidos

pos, neg, neut, textos = contador_e_juntador(lista_de_resenhas_json)

print(f"Positivas: {pos}")
print(f"Negativas: {neg}")
print(f"Neutras: {neut}")
print(textos)