# %% [markdown]
# # Gráficos de barras e de setores

# %% [markdown]
# ### Pandas também é capaz de gerar plots, basta usar obj_name."plot".plot_type

# %%
import pandas as pd

# %%
data_base = pd.read_csv(r'dados/insect.csv')
data_base.head()

# %%
# barras (BAR)
contagem = data_base.groupby(['spray'])['count'].sum()
contagem.plot.bar(color=['red', 'gray'])

# %%
# setores (PIE)
contagem.plot.pie(legend=True)
# legend: naturalemnte vem False


