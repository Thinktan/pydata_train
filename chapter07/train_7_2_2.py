
import numpy as np
import pandas as pd
from numpy import nan as NA

data = pd.DataFrame(
    {'food': ['bacon', 'pulled pork', 'bacon', 'Pastrami', 'corned beef', 'Bacon', 'pastrami',
              'honey ham', 'nova lox'],
     'ounces': [4, 3, 12, 6, 7.5, 8, 3, 5, 6]
     }
)

meat_to_animal = {'bacon': 'pig',
                  'pulled pork': 'pig',
                  'pastrami': 'cow',
                  'corned beef': 'cow',
                  'honey ham': 'pig',
                  'nova lox': 'salmon'}

lowercased = data['food'].str.lower()

data['animal'] = lowercased.map(meat_to_animal)
print(data, '\n')