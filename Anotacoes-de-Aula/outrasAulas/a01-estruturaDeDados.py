# Estruturas de Dados
# Listas
lista_de_nomes = ["Maria Silva", "João Santos", "Ana Oliveira", "Pedro Costa", "Juliana Pereira"]
print(lista_de_nomes[2])
lista_de_medias = [8.9, 7.5, 4.2, 1.4, 9.5]
print(lista_de_medias[2])
n = 0
while n < len(lista_de_nomes):
    if (lista_de_medias[n] + 1 <= 10):
        lista_de_medias[n] = lista_de_medias[n] + 1
    else:
        lista_de_medias[n] = 10
    n += 1

print(lista_de_medias)