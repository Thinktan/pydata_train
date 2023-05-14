
import numpy as np
import pandas as pd
import sys

data = pd.read_csv('../examples/ex5.csv')
data.to_csv(sys.stdout, index=False, header=False)

dates = pd.date_range('1/1/2000', periods=7)
print(dates, "\n-----\n")
ts = pd.Series(np.arange(7), index=dates)
ts.to_csv(sys.stdout)