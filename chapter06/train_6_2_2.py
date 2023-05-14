
import pandas as pd

xlsx = pd.ExcelFile('../examples/ex1.xlsx')
frame = pd.read_excel(xlsx, "Sheet1")

print(frame)