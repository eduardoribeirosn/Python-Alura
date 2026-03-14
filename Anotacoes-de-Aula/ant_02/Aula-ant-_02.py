# Tipagem
nome = input("Digite seu nome: ")
print(nome)
idade = input("Digite sua idade: ")
print(idade)
print("---- Tipagem ----")
print(type(nome))
print(type(idade))
print("---- ------- ----")
idade = int(idade)
print(type(idade))

print("A pessoa se chama " + nome + " e tem " + str(idade) + " anos de idade")

print(f"A pessoa se chama {nome} e tem {idade} anos de idade")