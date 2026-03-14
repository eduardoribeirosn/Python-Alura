# Dicionário

lista_de_nomes = ["Maria Silva", "João Santos", "Ana Oliveira", "Pedro Costa", "Juliana Perereira"]
lista_de_medias = [8.9, 7.5, 4.2, 1.4, 9.5]

dict_de_nomes_e_media = {
    "Maria Silva": 8.9,
    "João Santos": 7.5,
    "Pedro Costa": 4.2,
    "Juliana Perereira": 1.4,
    "Ana Oliveira": 4.2
}

dict_de_nomes_e_media["Maria Silva"]
dict_de_nomes_e_media.get("Maria Silva")
dict_de_nomes_e_media.pop("Maria Silva")
print(dict_de_nomes_e_media)
print(dict_de_nomes_e_media.items())
print(dict_de_nomes_e_media.keys())
print(dict_de_nomes_e_media.values())

lista_desafio = [
    {
        "nome": "Maria Silva",
        "media": 8.9
    },
    {
        "nome": "João Santos",
        "media": 7.5
    },
    {
        "nome": "Ana Oliveira",
        "media": 4.2
    },
    {
        "nome": "Pedro Costa",
        "media": 1.4
    },
    {
        "nome": "Juliana Pereira",
        "media": 9.5
    }
]

print("\n")
print(lista_desafio)
print(lista_desafio[0]["media"])