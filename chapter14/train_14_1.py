import json

path = '../datasets/bitly_usagov/example.txt'
# print(open(path).readline())

records = [json.loads(line) for line in open(path, encoding='utf-8')]

print(records[0], '\n')

# 14.1.1 纯Python时区计数
time_zones = [rec['tz'] for rec in records if 'tz' in rec]
print(time_zones[:10], '\n')

def get_counts(sequence):
    counts = {}
    for x in sequence:
        if x in counts:
              counts[x] += 1
        else:
              counts[x] = 1
    return counts

from collections import defaultdict
def get_counts2(sequence):
    counts = defaultdict(int) # 值将会初始化为0
    for x in sequence:
        counts[x] += 1
    return counts

counts = get_counts(time_zones)
print(counts, '\n')

def top_counts(count_dict, n=10):
    value_key_pairs = [(count, tz) for tz, count in count_dict.items()]
    value_key_pairs.sort()
    return value_key_pairs[-n:]

print(top_counts(counts), '\n')

# 使用Python标准库
from collections import Counter
counts = Counter(time_zones)
print(counts.most_common(10), '\n')


# 14.1.2 使用pandas进行时区计数
import pandas as pd
frame = pd.DataFrame(records)
print(frame.info(), '\n')
print(frame['tz'][:10], '\n')

tz_counts = frame['tz'].value_counts()
print(tz_counts[:10], '\n')

clean_tz = frame['tz'].fillna('Missing')
clean_tz[clean_tz == ''] = 'Unknown'
tz_counts = clean_tz.value_counts()
print(tz_counts[:10], '\n')


import seaborn as sns
import matplotlib.pyplot as plt
# subset = tz_counts[:10]
# sns.barplot(y=subset.index, x=subset.values)
# plt.show()

results = pd.Series([x.split()[0] for x in frame.a.dropna()])
print(results[:5], '\n')
print(results.value_counts()[:8], '\n')

import numpy as np

cframe = frame[frame.a.notnull()]
cframe['os'] = np.where(cframe['a'].str.contains('Windows'), 'Windows', 'Not Windows')
print(cframe['os'][:5], '\n')

by_tz_os = cframe.groupby(['tz', 'os'])
# for k, v in by_tz_os:
#     print(k)
#     print(v, '\n')
agg_counts = by_tz_os.size().unstack().fillna(0)
print(agg_counts[:10], '\n')

indexer = agg_counts.sum(1).argsort()
print(indexer[:10], '\n')


count_subset = agg_counts.take(indexer[-10:])
print(count_subset, '\n')



# 对绘图数据重新排列
count_subset = count_subset.stack()
count_subset.name = 'total'
count_subset = count_subset.reset_index()
count_subset[:10]
# sns.barplot(x='total', y='tz', hue='os',  data=count_subset)
# plt.show()

def norm_total(group):
    group['normed_total'] = group.total / group.total.sum()
    return group
results = count_subset.groupby('tz').apply(norm_total)

g = count_subset.groupby('tz')

print('count_subset.groupby(\'tz\')=\n', count_subset.groupby('tz'), '\n')
for k, v in g:
    print(k)
    print(v, '\n')

print(g.total)
# print(g.total.transform('sum'))


# sns.barplot(x='normed_total', y='tz', hue='os', data=results)
# plt.show()




