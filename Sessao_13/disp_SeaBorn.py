# %% [markdown]
# # Gráfico de dispersão
# ### Ótimo para comparar a relação entre duas váriáveis numéricas

# %%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# %% [markdown]
# ## Concentração ed CO2 em plantas

# %%
# base de dados sobre concetraçãoi de co2 em plantas
data_co2 = pd.read_csv(r'dados/co2.csv')
data_co2.head()

# %%
# Concentração de CO2 de acordo com a absorção (destacando por tratamento)
sns.scatterplot(x=data_co2.uptake, y=data_co2.conc, hue=data_co2.Treatment)
# Hue: 'legenda' os pontos de acordo com o parametro

# %%
# Concentração de CO2 de acordo com a absorção, separando por tratamento

ch = data_co2.loc[data_co2['Treatment'] == 'chilled']
Nch = data_co2.loc[data_co2['Treatment'] == 'nonchilled']

plt.figure(1)

plt.subplot(1,2,1)
sns.scatterplot(x=ch.uptake, y=ch.conc, color='blue').set(title='Chilled')

plt.subplot(1,2,2)
sns.scatterplot(x=Nch.uptake, y=Nch.conc, color='red').set(title='Non chilled')

plt.tight_layout()

# %%
# Concentração de CO2 de acordo com a absorção separando por type

q = data_co2.loc[data_co2['Type'] == 'Quebec']
m = data_co2.loc[data_co2['Type'] == 'Mississippi']
# display(q)
# display(m)

plt.figure(1)

plt.subplot(1,2,1)
sns.scatterplot(x=q.uptake, y=q.conc, color='gray', ).set(title='Quebec')

plt.subplot(1,2,2)
sns.scatterplot(x=m.uptake, y=m.conc, color='black').set(title='Mississippi')

plt.tight_layout()

# %% [markdown]
# ## Número de casos de câncer de acordo com idade e hábitos

# %%
# Base dados sobre a ocorrencia de cancer em individuos por idade e habitos

cd = pd.read_csv(r'dados/esoph.csv')
cd.head()

# %%
# Número de casos por consumo de tabaco

sns.catplot(x=cd.tobgp, y=cd.ncases)

# %%
# Número de casos por consumo de tabaco, separando por idade

sns.catplot(x=cd.tobgp, y=cd.ncases, col=cd.agegp, aspect=.6)

# col: separa o elemento em subelementos
# aspect: configura a largura dos subplots

# %%
# Número de casos de acordo com o consumo de alcool, separando por idade
sns.catplot(x=cd.alcgp, y=cd.ncases, col=cd.agegp, aspect=0.6)

# col: separa o elemento em subelementos
# aspect: configura a largura dos subelementos


