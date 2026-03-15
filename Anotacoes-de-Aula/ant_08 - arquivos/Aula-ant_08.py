# Mexer com arquivos

texto_fic = ["abc", "def", "ghi"]

# modificar / criar
# Se arquivo não existe, ele cria. - "w" se tiver algo escrito apaga e começa do 0 - "a" continua com o que estava e adiciona mais
with open("nome_arquivo.txt", "w", encoding="utf-8") as arquivo:
    for elemento in texto_fic:
        arquivo.write(elemento + "\n")

    # OR arquivo.writeline(texto_fic)

# ler
nova_lista_de_leitura = []
with open("nome_arquivo.txt", "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        nova_lista_de_leitura.append(linha.strip())

    # OR arquivo.read()

    # OR arquivo.readlines()

print(nova_lista_de_leitura)
