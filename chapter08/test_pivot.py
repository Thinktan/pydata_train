
import pandas as pd

df = pd.DataFrame({
    'date': ['2023-05-01', '2023-05-01', '2023-05-02', '2023-05-02'],
    'city': ['City A', 'City B', 'City A', 'City B'],
    'temperature': [25, 28, 24, 26],
    'humidity': [80, 85, 82, 83]
})
print(df, '\n')

pivot_df1 = df.pivot(index='date', columns='city', values='temperature')
print(pivot_df1, '\n')

pivot_df2 = df.pivot(index='date', columns='city')
print(pivot_df2, '\n')