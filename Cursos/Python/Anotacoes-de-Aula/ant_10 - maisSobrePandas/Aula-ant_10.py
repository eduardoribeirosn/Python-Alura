import pandas as pd
import numpy as np

# Definindo os dados para as colunas
nomes_produtos = [f"Produto {i+1}" for i in range(50)]
categorias_produtos = np.random.choice(["Eletrônicos", "Livros", "Roupas", "Alimentos", "Brinquedos"], 50)
precos_produtos = np.random.uniform(10.0, 500.0, 50).round(2)
itens_vendidos = np.random.randint(1, 1000, 50)
avaliacoes_produtos = np.random.uniform(1.0, 5.0, 50).round(1)

# Criando o DataFrame
df_produtos = pd.DataFrame({
    "Nome do produto": nomes_produtos,
    "Categoria do produto": categorias_produtos,
    "Preço do produto": precos_produtos,
    "Itens vendidos": itens_vendidos,
    "Avaliação do produto": avaliacoes_produtos
})

# Exibir toda a lista
# print(df_produtos)

# Exibir os 5 primeiros
# print(df_produtos.head())

# Exibir apenas uma coluna
# print(df_produtos["Categoria do produto"])

# Exibir as 5 primeiras categoria
# print(df_produtos.head()["Categoria do produto"])

# Exibir todas as categorias possíveis
# print(df_produtos["Categoria do produto"].unique()) # Devolve uma lista
# OR
# print(set(df_produtos["Categoria do produto"])) # Devolve um dicionário


# FILTRAR ELEMENTOS

# Exibir apenas aqueles que é igual a alguma coisa (Apenas os que são de categoria "Eletrônicos")
# print(df_produtos[df_produtos["Categoria do produto"] == "Eletrônicos"])

# Exibir o tamanho do DataFrame -> (linhas, colunas) não tem parenteses
# print(df_produtos.shape)

# Exibir algo com 2 filtros, utilize o &, e coloque parenteses em cada verificação
# print(df_produtos[(df_produtos["Categoria do produto"] == "Eletrônicos") & (df_produtos["Preço do produto"] >= 350.0)])

# Exibir algo de acordo com seu índice
# print(df_produtos.iloc[15])

# Exibir um conjunto de itens baseado no índice
# print(df_produtos.iloc[0:16])

# Para alterar o índice e colocar um nome no local, aqui colocamos o nome de uma coluna
df_produtos_com_indice = df_produtos.set_index("Nome do produto")
# print(df_produtos_com_indice)

# Exibir algo de acordo com o índice, agora como o índice é um texto, utilizamos o "loc" invés do "iloc"
# print(df_produtos_com_indice.loc["Produto 12"])

# Exibir um conjunto de itens baseado no índice com nomes
# print(df_produtos_com_indice.loc["Produto 2":"Produto 18"])

# Exibir apenas uma célula
# print(df_produtos_com_indice.loc["Produto 23", "Itens vendidos"])

# Exibir um conjunto de itens com um conjunto de filtros
# print(df_produtos_com_indice.loc[["Produto 11", "Produto 33", "Produto 44"], ["Categoria do produto", "Itens vendidos"]])

# Alterar tudo que está de um jeito (toda categoria "Brinquedo" para "Brinquedo e Jogos")
brinquedos = df_produtos_com_indice[df_produtos_com_indice["Categoria do produto"] == "Brinquedos"]
df_produtos_com_indice.loc[brinquedos.index, "Categoria do produto"] = "Brinquedos e Jogos"
print(df_produtos_com_indice)