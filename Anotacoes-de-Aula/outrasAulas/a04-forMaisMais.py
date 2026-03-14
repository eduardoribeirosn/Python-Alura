# Mais coisas sobre for

# do 0 ao 4
for n in range(5):
    print(n)

print("-\n")
# do 2 ao 6
for n in range(2, 7):
    print(n)

print("-\n")
# do 3 ao 10, de 2 em 2
for n in range(3, 11, 2):
    print(n)

pessoa = {
        "nome": "Eduardo",
        "idade": 20,
        "altura": 1.75
    }

print("\n\n")
for chave, valor in pessoa.items():
    print(f"A chave é {chave} e o valor é {valor}")