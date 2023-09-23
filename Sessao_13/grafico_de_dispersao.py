# %% [markdown]
# # Gráfico de dispersão
# ### Ótimo para comparar a relação entre duas váriáveis numéricas

# %%
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# %%
data = pd.read_csv(r'dados/trees.csv')
data.head()

# %% [markdown]
# ### Ver a relação entre os valores girth e volume

# %%
# Gráfico de dispersão com MatPlotLib 

disp_mat = plt.scatter(x=data.Girth, y=data.Volume, facecolors='red', color='blue', marker='o')
# Facecolor: cor de dentro
# Color: cor de fora
# Marler: formato dos pontos
plt.title('Relação Girth x Volume')
plt.xlabel("Circunferência")
plt.ylabel("Volume")


# %%
# Gráfico de linha com MatPlotLib

lin_mat = plt.plot(data.Girth, data.Volume)
plt.title('Relação Girth x Volume')
plt.xlabel("Circunferência")
plt.ylabel("Volume")

# %%
# Gráfico de dispersão com SeaBorn 

disp_sns = sns.regplot(x=data.Girth, y=data.Volume, x_jitter=0.5, fit_reg=False, color='red').set(title='Relação Girth x Volume')
# Fit_reg = régua de tendência dos valores, vem TRUE por padrão
# X_jitter = move os pontos um pouco para o lado em case de sobreposição


