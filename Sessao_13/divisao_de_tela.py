# %% [markdown]
# # Divisão de tela (SubPlot)
# ### Possibilita mostrar vários elementos (subplots) em uma única figura

# %%
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# %%
data = pd.read_csv(r'dados/trees.csv')
data.head()

# %% [markdown]
# ## Relação entre as variávies

# %%
# Girth <=> Volume
plt.scatter(x=data.Girth, y=data.Volume)

# %%
# Height <=> Volume
plt.scatter(x=data.Height, y=data.Volume)

# %%
# Height <=> Girth
plt.scatter(x=data.Height, y=data.Girth)

# %%
# Frequencia do volume
print(np.histogram(data.Volume))
print('=-'*35)

plt.hist(data.Volume)

# %% [markdown]
# # Unir os elementos em uma única figura

# %%
plt.figure(1)
# Molde: plt.subplot(qtde.linha, qtde.coluna, posição)

plt.subplot(2,2,1)
plt.scatter(x=data.Girth, y=data.Volume)

plt.subplot(2,2,2)
plt.scatter(x=data.Height, y=data.Volume)

plt.subplot(2,2,3)
plt.scatter(x=data.Height, y=data.Girth)

plt.subplot(2,2,4)
plt.hist(data.Volume)


