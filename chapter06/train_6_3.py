import pandas as pd
import requests
url = 'https://api.github.com/repos/pandas-dev/pandas/issues'
resp = requests.get(url)
print(resp)
data = resp.json()
print(data)
print(len(data[0]))
print(data[0]['title'])
print('-------')

issues = pd.DataFrame(data, columns=['number', 'title', 'labels', 'state'])
print(issues)
print(issues.columns)