
import pandas as pd
import numpy as np

frame = pd.DataFrame({'a': range(7),
                      'b': range(7, 0, -1),
                      'c': ['one', 'one', 'one', 'two', 'two', 'two', 'two'],
                      'd': [0, 1, 2, 0, 1, 2, 3]})

print(frame, '\n')

frame2 = frame.set_index(['c', 'd'])
print(frame2, '\n')

print(frame.set_index(['c', 'd'], drop=False), '\n')

print(frame2.reset_index(), '\n')