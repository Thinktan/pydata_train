import pandas as pd

# one-hot encoding
s = pd.Series(['a', 'b', 'c', 'd']*2)
cat_s = s.astype('category')

print(pd.get_dummies(cat_s))