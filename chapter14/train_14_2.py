import pandas as pd

# MovieLens 1M数据集
import pandas as pd
# 让展示内容少一点
pd.options.display.max_rows = 10

unames = ['user_id', 'gender', 'age', 'occupation', 'zip']
users = pd.read_table('../datasets/movielens/users.dat', sep='::', header=None, names=unames)

rnames = ['user_id', 'movie_id', 'rating', 'timestamp']
ratings = pd.read_table('../datasets/movielens/ratings.dat', sep='::', header=None, names=rnames)

mnames = ['movie_id', 'title', 'genres']
movies = pd.read_table('../datasets/movielens/movies.dat', sep='::', header=None, names=mnames)

print('user:\n', users.columns)
print('rating:\n', ratings.columns)
print('movies:\n', movies.columns)

data = pd.merge(pd.merge(ratings, users), movies)
print('data:\n', data.columns, '\n')


mean_ratings = data.pivot_table(values='rating', index='title', columns='gender', aggfunc='mean')
print(mean_ratings[:5], '\n')

ratings_by_title = data.groupby('title').size()
print(ratings_by_title[:10], '\n')

active_titles = ratings_by_title.index[ratings_by_title >= 250]
print(active_titles, '\n')

mean_ratings = mean_ratings.loc[active_titles]
print(mean_ratings, '\n')

top_female_ratings = mean_ratings.sort_values(by='F', ascending=False)
print(top_female_ratings[:10], '\n')


# 14.2.1 测量评价分歧
# 男女差别
mean_ratings['diff'] = mean_ratings['M'] - mean_ratings['F']
sorted_by_diff = mean_ratings.sort_values(by='diff')
print(sorted_by_diff[:10], '\n')

# 不依赖性别标识
# Standard deviation of rating grouped by title
rating_std_by_title = data.groupby('title')['rating'].std()
# Filter down to active_titles
rating_std_by_title = rating_std_by_title.loc[active_titles]
# Order Series by value in descending order
print(rating_std_by_title.sort_values(ascending=False)[:10], '\n')














