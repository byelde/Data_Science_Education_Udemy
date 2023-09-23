# %% [markdown]
# # HISTOGRAMA:
# ### Usado para ver a distribuição e frequência de valores separados em intervalos (bins)

# %%
# Imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# %%
# Import data base
data_base = pd.read_csv(r'dados/trees.csv')
print(data_base.head())
print(data_base.shape)

# %%
# Distribuição histograma
hist = np.histogram(data_base.iloc[:,1], bins=10) #1ª lista: eixo y, 2ª lista: eixo x
print('Distribuição histograma')
print(hist)
print('='*80)

# Dados da coluna Height
print('Dados da coluna Height')
print(data_base['Height'].describe())
print('='*80)

# Frequencia da coluna Height
print('Frequencia da coluna Height')
print(data_base.groupby('Height').size())

# %%
# Plot
histPlt = plt.hist(data_base.iloc[:,1])
plt.title('Frequência de alturas')
plt.ylabel('Frequência')
print(hist)


