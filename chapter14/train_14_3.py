import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 美国1880~2010年的婴儿名字

# names1880 = pd.read_csv('../datasets/babynames/yob1880.txt',
#                         names=['name', 'sex', 'births'])
# print(names1880, '\n')
# print(names1880.groupby('sex').births.sum(), '\n')

years = range(1880, 2011)
pieces = []
columns = ['name', 'sex', 'births']
for year in years:
    path = '../datasets/babynames/yob%d.txt' % year
    frame = pd.read_csv(path, names=columns)
    frame['year'] = year
    pieces.append(frame)
# 将所有内容粘接进一个DataFrame
names = pd.concat(pieces, ignore_index=True)

total_births = names.pivot_table(values='births', aggfunc=sum, index='year', columns='sex')
print(total_births.tail(), '\n')

# total_births.plot(title='Total births by sex and year')
# plt.show()

def add_prop(group):
    # print(group)
    group['prop'] = group.births / group.births.sum()
    return group

names = names.groupby(['year', 'sex']).apply(add_prop)


# 完整性检查，所有分组prop总计1
print(names.groupby(['year', 'sex']).prop.sum(), '\n')



def get_top1000(group):
    return group.sort_values(by='births', ascending=False)[:1000]

grouped = names.groupby(['year', 'sex'])
top1000 = grouped.apply(get_top1000)
print(top1000, '\n')
# 删除组索引，不需要它
top1000.reset_index(inplace=True, drop=True)
print(top1000, '\n')

# 14.3.1 分析名字数字
boys = top1000[top1000.sex == 'M']
girls = top1000[top1000.sex == 'F']

total_births = top1000.pivot_table(index='year', columns='name', values='births', aggfunc=sum)
print(total_births.info(), '\n')



subset = total_births[['John', 'Harry', 'Mary', 'Marilyn']]
# subset.plot(subplots=True, figsize=(12, 10), grid=False,
#             title="Number of births per year")
# plt.show()

# 14.3.1.1 计量 命名多样性的增加
table = top1000.pivot_table('prop', index='year', columns='sex', aggfunc=sum)
# table.plot(title='Sum of table1000.prop by year and sex', yticks=np.linspace(0, 1.2, 13), xticks=range(1880, 2020, 10))
# plt.show()

df = boys[boys.year == 2010]
print(df)

prop_cumsum = df.sort_values(by='prop', ascending=False).prop.cumsum()
print(prop_cumsum[:10], '\n')

print(prop_cumsum.values.searchsorted(0.5), '\n')

df = boys[boys.year == 1900]
in1900 = df.sort_values(by='prop', ascending=False).prop.cumsum()
print(in1900.values.searchsorted(0.5), '\n')

def get_quantile_count(group, q=0.5):
    group = group.sort_values(by='prop', ascending=False)
    return group.prop.cumsum().values.searchsorted(q) + 1

diversity = top1000.groupby(['year', 'sex']).apply(get_quantile_count)
diversity = diversity.unstack('sex')
# diversity.plot(title="Number of popular names in top 50%")
# plt.show()

# 14.3.1.2 "最后一个字母"革命
# 从name列提取最后一个字母
get_last_letter = lambda x: x[-1]
last_letters = names.name.map(get_last_letter)
last_letters.name = 'last_letter'

table = names.pivot_table('births', index=last_letters, columns=['sex', 'year'], aggfunc=sum)

subtable = table.reindex(columns=[1910, 1960, 2010], level='year')
print(subtable.head(), '\n')

print(subtable.sum(), '\n')
letter_prop = subtable/subtable.sum()
print(letter_prop, '\n')


# fig, axes = plt.subplots(2, 1, figsize=(10, 8))
# letter_prop['M'].plot(kind='bar', rot=0, ax=axes[0], title='Male')
# letter_prop['F'].plot(kind='bar', rot=0, ax=axes[1], title='Female', legend=False)
# plt.show()

letter_prop = table / table.sum()
dny_ts = letter_prop.loc[['d', 'n', 'y'], 'M'].T
# print(dny_ts.head(), '\n')
# print(table, '\n')
# print(table.sum(), '\n')

# dny_ts.plot()
# plt.show()


# 14.3.1.3 男孩名字变成男孩名字(以及反向)
all_names = pd.Series(top1000.name.unique())
lesley_like = all_names[all_names.str.lower().str.contains('lesl')]
print(lesley_like, '\n')

filtered = top1000[top1000.name.isin(lesley_like)]
# print(filtered)
# print(filtered.groupby('name').births.sum(), '\n')
# print(filtered.groupby('name').sum(), '\n')

table = filtered.pivot_table('births', index='year', columns='sex', aggfunc='sum')
print(table, '\n')
table = table.div(table.sum(1), axis=0)
print(table, '\n')

table.plot(style={'M': 'k-', 'F': 'k--'})
plt.show()