import pandas as pd

tables = pd.read_html('../examples/fdic_failed_bank_list.html')
print(len(tables))
failures = tables[0]
print(failures.head(), '\n')
print(failures.columns)

close_timestamps = pd.to_datetime(failures['Closing Date'])
print(close_timestamps.dt.year.value_counts(), '\n------\n')

from lxml import objectify
path = '../datasets/mta_perf/Performance_MNR.xml'
parsed = objectify.parse(open(path))
root = parsed.getroot()

print('xxx')

data = []
skip_fields = ['PARENT_SEQ', 'INDICATOR_SEQ', 'DESIRED_CHANGE', 'DECIMAL_PLACES']

for elt in root.INDICATOR:
    el_data = {}
    for child in elt.getchildren():
        if child.tag in skip_fields:
            print('continue', child.tag)
            continue
        el_data[child.tag] = child.pyval
    data.append(el_data)

perf = pd.DataFrame(data)
print(perf.head())
print(perf.columns)


from io import StringIO
tag = '<a href="http://www.google.com">Google</a>'
root = objectify.parse(StringIO(tag)).getroot()

print(root.get('href'))
print(root.text)