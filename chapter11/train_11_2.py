import pandas as pd

s1 = pd.Series([11, 22, 33, 44], index=[1, 2, 3, 4])
s2 = pd.Series([22, 44], index=[2, 4])

print(s1)
print(s2)
print(s1+s2)
