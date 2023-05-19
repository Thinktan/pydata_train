import re

import numpy as np
import pandas as pd

data = {'Dave': 'dave@google.com', 'Steve': 'steve@gmail.com',
        'Rob': 'rob@gmail.com', 'Wes': np.nan}

data = pd.Series(data)

print(data.isnull(), '\n')

print(data.str.contains('gmail'), '\n')

pattern = r'([A-Z0-9._%+-]+)@([A-Z0-9.-]+)\.([A-Z]{2,4})'
print(data.str.findall(pattern, flags=re.IGNORECASE), '\n')

matches = data.str.match(pattern, flags=re.IGNORECASE)
print(matches, '\n')
print(data.str[0], '\n')
print(data.str.get(1), '\n')