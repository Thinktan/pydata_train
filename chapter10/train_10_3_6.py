
import numpy as np
import pandas as pd
import statsmodels.api as sm

# 逐组线性回归

close_px = pd.read_csv('../examples/stock_px.csv', parse_dates=True, index_col=0)
# print(close_px.info(), '\n')

spx_corr = lambda x: x.corrwith(x['SPX'])
rets = close_px.pct_change().dropna()

get_year = lambda x: x.year
by_year = rets.groupby(get_year)

for k, g in by_year:
    # print(k)
    # print(g.head(), '\n')

    yvar = 'AAPL'
    xvars = ['SPX']
    Y = g[yvar]
    X = g[xvars]
    X['intercept'] = 1.

    result = sm.OLS(Y, X).fit()

    print(X)
    print('-------------')
    print(Y.head())
    print('-------------')
    print(result.params)
    print('=============')

def regress(data, yvar, xvars):
    Y = data[yvar]
    X = data[xvars]
    X['intercept'] = 1.
    result = sm.OLS(Y, X).fit()
    return result.params

print(by_year.apply(regress, 'AAPL', ['SPX']), '\n')

states = ['Ohio', 'New York', "Vermont", 'Florida',
          'Oregon', 'Nevada', 'California', 'Idaho']


# 测试返回为Series的情况
index = ['A', 'B', 'C']
# data = pd.Series(['x', 'y', 'z'], index=index)
data = pd.Series(['x', 'y', 'z'])
print(data, '\n')

cvrt_func = lambda g: data

print(by_year.apply(cvrt_func), '\n')

# 测试返回为DataFrame的情况
data2 = {'Value': [10, 20, 30, 40, 50, 60],
        'Category': ['A', 'B', 'A', 'B', 'A', 'B'],
        'Year': [2020, 2020, 2021, 2021, 2022, 2022]}

# 创建一个包含多维索引的DataFrame
index2 = pd.MultiIndex.from_tuples([('Group 1', 'Person 1'),
                                   ('Group 1', 'Person 2'),
                                   ('Group 2', 'Person 1'),
                                   ('Group 2', 'Person 2'),
                                   ('Group 3', 'Person 1'),
                                   ('Group 3', 'Person 2')], names=['Group', 'Person'])

df2 = pd.DataFrame(data2, index=index2)
cvrt_func2 = lambda g: df2

print(by_year.apply(cvrt_func2), '\n')

# 测试返回为单列DataFrame的情况
index3 = ['A', 'B', 'C']
data3 = {'City': ['New York', 'London', 'Pairs']}
df3 = pd.DataFrame(data3, index=index3)
print(df3, '\n')

cvrt_func = lambda g: df3

print(by_year.apply(cvrt_func), '\n')