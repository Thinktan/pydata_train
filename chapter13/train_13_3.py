import pandas as pd
import numpy as np
import statsmodels.api as sm
import statsmodels.formula.api as smf


# statsmodels介绍
print('-------------13.3.1-------------')
# 13.3.1 评估线性模型
def dnorm(mean, variance, size=1):
    if isinstance(size, int):
        size = size,
    return mean + np.sqrt(variance) * np.random.randn(*size)
# 用于复现
np.random.seed(12345)
N = 100
X = np.c_[dnorm(0, 0.4, size=N),
          dnorm(0, 0.6, size=N),
          dnorm(0, 0.2, size=N)]

print('X.shape:\n', X.shape, '\n')

eps = dnorm(0, 0.1, size=N)
beta = [0.1, 0.3, 0.5]
y = np.dot(X, beta) + eps

# 添加截距项目
X_model = sm.add_constant(X)

model = sm.OLS(y, X)
results = model.fit()
print(results.params, '\n')
print(results.summary(), '\n')





data = pd.DataFrame(X, columns=['col0', 'col1', 'col2'])
data['y'] = y
print(data[:5], '\n')

results = smf.ols('y~col0+col1+col2', data=data).fit()
print(results.params, '\n')
print(results.tvalues, '\n')


print(results.predict(data[:5]), '\n')


# '-------------13.3.2-------------'
# 评估时间序列处理
init_x = 4
import random
values = [init_x, init_x]
N = 1000
b0 = 0.8
b1 = -0.4
noise = dnorm(0, 0.1, N)
for i in range(N):
    new_x = values[-1] * b0 + values[-2] * b1 + noise[i]
    values.append(new_x)

# MAXLAGS = 5
# model = sm.tsa.AR(values)
# results = model.fit(MAXLAGS)
# print(results.params)

# NotImplementedError: AR has been removed from statsmodels
# and replaced with statsmodels.tsa.ar_model.AutoReg.







