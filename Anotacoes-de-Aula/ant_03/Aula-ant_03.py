# Estrutura Condiciona
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))

if idade >= 18:
    print(f"O {nome} pode entrar na festa porque ele é maior de idade")
    print(f"Ele tem {idade} anos de idade")
else:
    print(f"O {nome} NÃO pode entrar na festa porque ele é maior de idade")
    print(f"Ele tem {idade} anos de idade")