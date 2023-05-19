import numpy as np
import pandas as pd

df = pd.DataFrame({'key': ['b', 'b', 'a', 'c', 'a', 'b'],
                   'data1': range(6)})

print(df, '\n')

print(pd.get_dummies(df['key']))

dummies = pd.get_dummies(df['key'], prefix='key')
df_with_dummy = df[['data1']].join(dummies)
print(df_with_dummy, '\n')

mnames = ['movie_id', 'title', 'genres']
movies = pd.read_table('../datasets/movielens/movies.dat', sep='::', header=None, names=mnames)
print(movies[:10], '\n')

# 提取不同流派的列表
all_genres = []
for x in movies.genres:
    all_genres.extend(x.split('|'))
genres = pd.unique(all_genres)
print(genres, '\n')

# 全0 matrix
zero_matrix = np.zeros((len(movies), len(genres)))
dummies = pd.DataFrame(zero_matrix, columns=genres)

for i, gen in enumerate(movies.genres):
    indices = dummies.columns.get_indexer(gen.split('|'))
    dummies.iloc[i, indices] = 1

movies_windic = movies.join(dummies.add_prefix('Genre_'))
print(movies_windic.iloc[0], '\n')


# 将get_dummies与cut等离散化函数结合
np.random.seed(12345)
values = np.random.rand(10)
bins = [0, 0.2, 0.4, 0.6, 0.8, 1]
cutans = pd.cut(values, bins)
print(cutans, '\n')
print(pd.get_dummies(cutans), '\n')



