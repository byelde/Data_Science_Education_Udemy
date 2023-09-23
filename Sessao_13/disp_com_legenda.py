# %% [markdown]
# # Gráfico de dispersão
# ### Ótimo para comparar a relação entre duas váriáveis numéricas
# ### A legenda mostra a separa os valores em categorias

# %%
import pandas as pd
import matplotlib.pyplot as plt

# %%
data_base = pd.read_csv(r'dados/co2.csv')
print(data_base.head())

# %%
# listando as legendas
# "set" pega os todos os valores que aparecem na coluna
condicao = list(set(data_base.Treatment))
print(condicao)
'''chilled, nonchilled'''

# %%
# Atribuição em varíavel curta apenas para organização

y = data_base.uptake
x = data_base.conc
# print(x,y)

# %%
# Cada 'ponto' recebe legenda de forma independente, um por vez
for i in range(len(condicao)): #enumera as condições: 0-chilled, 1-nonchilled
    indice = (data_base.Treatment == condicao[i]) #indice recebe V ou F (que vêm 'enumerados') dependendo de ter a condição ou não
    plt.scatter(x=x[indice], y=y[indice], label=condicao[i]) # x e y que tem a condição recebem a condição como legenda
plt.legend(loc='lower right')


