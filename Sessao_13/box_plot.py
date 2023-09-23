# %% [markdown]
# # BoxPlot
# ### Usado para ver o intervalo de um valor 

# %%
import pandas as pd
import matplotlib.pyplot as plt

# %%
data = pd.read_csv(r'dados/trees.csv')
data.head()

# %%
plt.boxplot(data.Volume, vert=False, showfliers=False, notch=True, patch_artist=True)
# vert: padrão True
# Showfliers (mostrar voadores/fora do padrão) padrão True
# Notch(?) intervalo de confiança entorno da mediana. padrão False
# patch_artist: preeenche a forma geométrica formada. padrão False

# %%
# Dados por coluna
plt.boxplot(data, vert=False, patch_artist=True)
print(data.describe().iloc[[3,-1],:])
#Mostra o intervalo de valores de cada linha

# %%
#dados por linha

# plt.box(data) <== assim, as colunas vão para o eixo X ao invés das linhas
plt.boxplot(data.transpose(), patch_artist=True) # Transpondo, as linhas vão para o eixo X

data.transpose().describe().iloc[[3,-1],:12]
# Represente o intervalo dos valores de cada linha
# Ex.: na linha 1, os valores vão de 8.3 (Girth) a 70 (Height)


