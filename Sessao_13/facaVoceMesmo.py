# %% [markdown]
# # Faça Você Mesmo
# ## Análise Exploratória

# %%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# %%
db = pd.read_csv(r'dados/dados.csv', sep=';')
db.head()

# %%
# Frequência de PIB
print(db.PIB.describe())

sns.histplot(db.PIB, bins=6, kde=True).set(title='Frequência por PIB')
# Conclusão: Faixa de PIB ais frequente: ~8000 - ~480000

# %%
# Fequência de empenho:
sns.histplot(db.VALOREMPENHO/1000000, bins=6, kde=True).set(title='Frequência por empenho\n Em milhão')

# Conclusão: Faixa de empenho mais frequente: 0 - ~200,000

# %%
oPIB = db.sort_values('PIB', ascending=True)

# Cidades com maiores PIBs
oPIB.iloc[-5:,:].plot.bar(x='MUNICIPIO', y='PIB', color='red')

# Cidades com menores PIBs
oPIB.iloc[:5,:].plot.bar(x='MUNICIPIO', y='PIB', color='blue')


