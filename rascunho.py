import pandas as pd


df = pd.read_csv('produtos/estoque.csv')
df.to_excel('estoque.xlsx', index=False)