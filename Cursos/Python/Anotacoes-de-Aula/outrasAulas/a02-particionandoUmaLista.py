# Particionando uma lista

lista_de_nomes = ["Maria Silva", "João Santos", "Ana Oliveira", "Pedro Costa", "Juliana Perereira"]

print(lista_de_nomes[1:3])
print(lista_de_nomes[2:])
print(lista_de_nomes[:2])

lista_de_nomes.append("Fábio Carraro")

print(len(lista_de_nomes))

# Vai dar erro, o apprend espera apenas uma argumento
# lista_de_nomes.append("Joana da Silva", "Paulo Silveira")

lista_de_nomes.extend(["Joana da Silva", "Paulo Silveira"])
print(len(lista_de_nomes))

lista_de_nomes.remove("Paulo Silveira")
lista_de_nomes.pop()
print(lista_de_nomes)
lista_de_nomes.pop(2)
print(lista_de_nomes)
