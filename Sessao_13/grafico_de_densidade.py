# %% [markdown]
# # GRÁFICO DE DENSIDADE
# ### Mostra a frequência de valores em forma de linha e não em barras. Pode ser um elemento independente ou um complemento do histograma 

# %%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# %%
data_base = pd.read_csv(r'dados/trees.csv')
data_base.head()

# %%
hist_data_height = np.histogram(data_base.iloc[:, 1], bins=10)
print(hist_data_height)

# %%
# Histograma sem linha de densidade
# kde = linha de densidade
hist_plt_kdeOFF = sns.histplot(data_base['Height'], kde=False, bins=6).set(title='Alturas') 
hist_plt_kdeOFF

# %%
# Histograma com linha de densidade
# kde = linha de densidade
hist_plt_kdeON = sns.histplot(data_base['Height'], kde=True, bins=6).set(title='Alturas')
hist_plt_kdeON


