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
print(root)