
import pandas as pd
import numpy as np

names = ['a', 'b', 'c', 'd', 'message']

df1 = pd.read_csv('../examples/ex2.csv', names=names, index_col='message')
print(df1.columns)
print(df1.index)
print(df1.shape, "\n\n")

parsed = pd.read_csv("../examples/csv_mindex.csv", index_col=['key1', 'key2'])
print(parsed, "\n")


result = pd.read_csv('../examples/ex5.csv')

print(result.isnull().astype(int).replace((0, 1), (50, 10)))