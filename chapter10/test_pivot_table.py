import pandas as pd

data = {'City': ['New York', 'London', 'London', 'Paris', 'Paris'],
        'Year': [2020, 2020, 2021, 2021, 2022],
        'Sales': [1000, 1500, 1200, 1800, 2000]}
df = pd.DataFrame(data)
pivot_df = pd.pivot_table(df, values='Sales', index='City', columns='Year', aggfunc='sum')
print(df, '\n')
print(pivot_df, '\n')