# Coisas diferentes do meu...


## Fazer a pergunta para IA e guardar em um dicionario com (pergunta e resposta)
# for pergunta in lista_desafio:
#     resposta = client.models.generate_content(
#         model="gemini-2.5-flash",
#         contents=f"Gere uma resposta muito sucinta para a pergunta: {pergunta}"
#     )
#     lista_de_dicionarios_de_respostas.append({"pergunta": pergunta, "resposta": resposta.text})
#

## Escrever um csv utilizando (with open) com o objeto criado
# with open("respostas1.csv", "w", encoding="utf-8") as arquivo:
#     arquivo.write("pergunta,resposta\n")
#     for pergunta_dict in lista_de_dicionarios_de_respostas:
#         arquivo.write(f"{pergunta_dict['pergunta']},{pergunta_dict['resposta']}\n")
#


## Escrever um csv utilizando a biblioteca pandas com o (DataFrame) passando um objeto
# df_perguntas_e_respostas = pd.DataFrame(lista_de_dicionarios_de_respostas)
#


## Criar um arquivo apartir da variável anterior (criada com DataFrame)
# df_perguntas_e_respostas.to_csv("resposta2.csv", index=False, encoding="utf-8")
#


## Ler o arquivo csv com a biblioteca Pandas
# print(pd.read_csv("resposta2.csv"))