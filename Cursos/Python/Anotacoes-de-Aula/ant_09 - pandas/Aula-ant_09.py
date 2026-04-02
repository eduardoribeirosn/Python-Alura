import pandas as pd

# dt -> data frame
df = pd.read_csv("meu_csv.csv")

print(df)
print("\n")
# se não colocar nd, aparece os 5 primeiros
# head mostra os primeiros
print(df.head(7))
print("\n")
# tail mostra os últimos
print(df.tail())
