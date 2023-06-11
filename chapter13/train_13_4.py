import pandas as pd

# scikit-learn
train = pd.read_csv('../datasets/titanic/train.csv')
test = pd.read_csv('../datasets/titanic/test.csv')
print(train[:4], '\n')
print(train.isnull().sum())

impute_value = train['Age'].median()
train['Age'] = train['Age'].fillna(impute_value)
test['Age'] = test['Age'].fillna(impute_value)

train['IsFemale'] = (train['Sex'] == 'female').astype(int)
test['IsFemale'] = (test['Sex'] == 'female').astype(int)

print(train.columns, '\n')
print(test.columns, '\n')

predictors = ['Pclass', 'IsFemale', 'Age']
X_train = train[predictors].values
X_test = test[predictors].values
y_train = train['Survived'].values
print(X_train[:5], '\n')
print(y_train[:5], '\n')

from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
model.fit(X_train, y_train)

y_predict = model.predict(X_test)
print(y_predict[:10], '\n')

# 交叉验证

# from sklearn.linear_model import LogisticRegressionCV
# model_cv = LogisticRegressionCV(10)
# model_cv.fit(X_train, y_train)

#LogisticRegression和LogisticRegressionCV的主要区别是LogisticRegressionCV使用了交叉验证来选择正则化系数C
#手动交叉验证
from sklearn.model_selection import cross_val_score
model = LogisticRegression(C=10)
scores = cross_val_score(model, X_train, y_train, cv=4)
print(scores)