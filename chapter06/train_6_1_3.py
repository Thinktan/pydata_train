import pandas as pd
import csv

f = open('../examples/ex7.csv')
reader = csv.reader(f)

for line in reader:
    print(line)

print('============')

with open('../examples/ex7.csv') as f:
    lines = list(csv.reader(f))
    header, values = lines[0], lines[1:]
    # print(header, "\n-----")
    # print(values, '\n')
    data_dict = {h: v for h, v in zip(header, zip(*values))}
    # print(data_dict)
