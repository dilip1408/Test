# import pandas as pd
#
# df = pd.read_csv("C:/Users/dvoruga/Downloads/clickstream-enwiki-2018-12/clickstream-enwiki-2018-12.tsv",  delimiter='\t',
#     names=['coming_from', 'article', 'referrer_type', 'n'],
#     dtype={'referrer_type': 'category','n': 'uint32'} )
# #
# # # df.iloc[:10000]
# # # print(df.shape)
# # # print(df.describe())
# #
# # # print(df['coming_from'].sum())
# # top_links = df.loc[df['referrer_type'].isin(['link']),['coming_from','article','n']].groupby(['coming_from', 'article']).sum().sort_values(by='n', ascending=False)
# #
# # print(top_links)
#
# from dask import dataframe as dd
# #
# dfd = dd.read_csv(
#     'C:/Users/dvoruga/Downloads/clickstream-enwiki-2018-12/clickstream-enwiki-2018-12.tsv',
#     delimiter='\t',
#     names=['coming_from', 'article', 'referrer_type', 'n'],
#     dtype={
#         'referrer_type': 'category',
#         'n': 'uint32'},
#     blocksize=64000000 # = 64 Mb chunks
# )
# #
# # top_links_grouped_dask = dfd.loc[
# #     dfd['referrer_type'].isin(['link']),
# #     ['coming_from','article', 'n']].groupby(['coming_from', 'article'])
# #
# # store = pd.HDFStore('./data/clickstream_store.h5')
# #
# # top_links_dask = top_links_grouped_dask.sum().nlargest(20, 'n')
#
# # store.put('top_links_dask',
# #            top_links_dask.compute(),
# #            format='table',
# #            data_columns=True)
#
# # external_searches = df.loc[
# #  (df['referrer_type'].isin(['external'])) &
# #  (df['coming_from'].isin(['other-search'])),
# #  ['article', 'n']
# # ]
#
# # most_popular_articles = external_searches.sort_values(by='n', ascending=False).head(40)
# # print(most_popular_articles)
#
# external_searches_dask = dfd.loc[
#     (dfd['referrer_type'].isin(['external'])) &
#     (dfd['coming_from'].isin(['other-search'])),
#     ['article', 'n']
# ]
#
# external_searches_dask = external_searches_dask.nlargest(40, 'n').compute()
#
# import seaborn as sns
# from matplotlib import pyplot as plt
# sns.barplot(data=external_searches_dask, y='article', x='n')
# plt.gca().set_ylabel('')

##########################
#https://towardsdatascience.com/a-data-scientists-intro-to-parallel-computing-with-dask-4c1b4a464579

import dask
from dask.distributed import Client, progress
from dask.distributed import Client

if __name__ == '__main__':
    client = Client(processes=False)
# try:
#     client.close()
#     client = Client(threads_per_worker=1,
#                     n_workers=5,
#                     memory_limit='2GB')
# except:
#     client = Client(threads_per_worker=1,
#                     n_workers=5,
#                     memory_limit='2GB')
# print(client)
#
import numpy as np
import pandas as pd

def simulate_dataset(i):
    g = 10
    k = 100000

    categories = np.random.choice(a=np.arange(g), size=k)
    values = [(j + 1) * np.random.random(k // g) for j in range(g)]
    values = np.concatenate(values)

    data = pd.DataFrame({'category': categories,
                         'values': values})
    data_out = data.groupby('category').apply(lambda df: [
        df.loc[:, 'values'].mean(),
        df.loc[:, 'values'].std()
    ])
    return (data_out)

import timeit

results = {}
for i in range(1000000):
    results[i] = simulate_dataset(i)
print(results)