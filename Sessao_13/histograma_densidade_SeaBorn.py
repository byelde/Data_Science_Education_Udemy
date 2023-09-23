# %% [markdown]
# # HISTOGRAMA:
# ### Usado para ver a distribuição e frequência de valores separados em intervalos (bins)

# %%
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# %%
c_data = pd.read_csv(r'dados/chicken.csv')
c_data.head()

# %%
# Soma do wieight de todas as feeds

total = c_data.groupby(['feed'])['weight'].sum()
print(total.reset_index())

# %%
# Valor max e min de cada feed

feeds = list(set(c_data.feed))

for feed in feeds:
    current_feed = c_data.loc[c_data['feed'] == feed]
    print(feed)
    print(current_feed.describe().iloc[[3,-1],:])

# %%
# Histograma com densidade (kde) de cada feed
feeds = list(set(c_data.feed))
plt.figure(1)
for nF, feed in enumerate(feeds):
    plt.subplot(3,2,nF+1)
    sns.histplot(c_data.loc[c_data['feed'] == feed], kde=True, bins=10).set(title=feed)
plt.tight_layout() # Retira sobreposições


