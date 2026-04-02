# Como printar algo na tela.
print("Olá, mundo!") # Aspas duplas ou simples funciona.

# métodos de String
texto = "     Fabrício CARRaro  da alura   "
print(texto)
print(texto.lower())
print(texto.upper())
print(texto.strip())
print(texto.replace("  ", " "))

print(texto.strip().upper().replace("  ", " "))

texto = texto.strip().upper().replace("  ", " ")

print(texto)

nome = input("Digite o seu nome: ")
print(nome)
idade = input("Digite sua idade: ")
print(idade)