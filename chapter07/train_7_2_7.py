
import numpy as np
import pandas as pd

df = pd.DataFrame(np.arange(5*4).reshape((5, 4)))

sampler = np.random.permutation(5)
print(sampler)

print(df, '\n')
print(df.take(sampler), '\n')

print(df.sample(n=3), '\n')

choices = pd.Series([5, 7, -1, 6, 4])
draws = choices.sample(n=10, replace=True)
print(draws)

