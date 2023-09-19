# %%
import pandas as pd
import seaborn as sns
import statistics as stts

# %% [markdown]
# ## Previous Analysis

# %%
data = pd.read_csv('tempo.csv', sep=';')
data

# %%
# NaN values
print(data.isna().sum())

# %%
# Aparencia data
print(data.groupby('Aparencia').size())

# %%
# Temperatura data
print(data['Temperatura'].describe())
# sns.boxplot(data['Temperatura'])
sns.histplot(data['Temperatura'])

# %%
# Umidade data
print(data['Umidade'].describe())
# sns.boxplot(data['Umidade'])
sns.histplot(data['Umidade'])

# %%
# Vento data
print(data.groupby('Vento').size())

# %%
# Jogar data
print(data.groupby('Jogar').size())

# %% [markdown]
# ## Data processing
# 

# %%
# NaN values

# Umidade
data.loc[data['Umidade'].isna(), 'Umidade'] = stts.median(data['Umidade'])
sns.histplot(data['Umidade'])

# Vento
data.loc[data['Vento'].isna(), 'Vento'] = 'FALSO'
data.groupby('Vento').size()

# %%
# Aparencia data

data.loc[data['Aparencia'] == 'menos', 'Aparencia'] = 'chuva'
data.groupby('Aparencia').size()

# %%
# Temperatura data

data.loc[data['Temperatura'] > 135, 'Temperatura'] = stts.median(data['Temperatura'])
data['Temperatura'].describe()

# %%
# Umidade data
data.loc[data['Umidade'] > 100, 'Umidade'] = stts.median(data['Umidade'])
data['Umidade'].describe()
