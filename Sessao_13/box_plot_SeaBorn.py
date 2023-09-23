# %% [markdown]
# # BoxPlot
# ### Usado para ver o intervalo de um valor 

# %%
import pandas as pd
import seaborn as sns

# %%
data_base = pd.read_csv(r'dados/trees.csv')
data_base.head()

# %%
# Visualizar frequência de uma coluna
sns.boxplot(data_base.Volume, orient='v').set(title='Frequência volumes')
# Orient vem 'v'(vertical) por padrão, mas poed ser alterado para h (horizontal)

# %%
# Visualizar frequencia de todas as colunas
sns.boxplot(data_base, orient='h')
# Orient vem 'v'(vertical) por padrão, mas poed ser alterado para h (horizontal)


