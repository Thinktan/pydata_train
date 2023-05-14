
import pandas as pd
import numpy as np

frame = pd.DataFrame({'a': np.random.rand(100)})
store = pd.HDFStore('mydata.h5')

