# -*- coding: UTF-8 -*-
# 决策树：Cart算法

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import DecisionTreeRegressor
from sklearn.datasets import load_iris
from sklearn.datasets import load_boston
from sklearn.datasets import load_digits

# 分类树
iris = load_iris()
features = iris.data
labels = iris.target
train_features, test_features, train_labels, test_labels = train_test_split(features, labels, test_size=0.33, random_state=0)
clf = DecisionTreeClassifier(criterion='gini')
clf = clf.fit(train_features, train_labels)
test_predict = clf.predict(test_features)
score = accuracy_score(test_labels, test_predict)
print("CART 分类树准确率 %.4lf" % score)

# 回归树
boston = load_boston()
print(boston.feature_names)
features = boston.data
prices = boston.target
train_features, test_features, train_prices, test_prices = train_test_split(features, prices, test_size=0.33)
dtr = DecisionTreeRegressor()
dtr.fit(train_features, train_prices)
predict_prices = dtr.predict(test_features)
print('回归树二乘偏差均值:', mean_squared_error(test_prices, predict_prices))
print('回归树绝对值偏差均值:', mean_absolute_error(test_prices, predict_prices))

# homework
digits = load_digits()
features = digits.data
labels = digits.target
train_features, test_features, train_labels, test_labels = train_test_split(features, labels, test_size=0.33, random_state=0)
clf = DecisionTreeClassifier(criterion='gini')
clf = clf.fit(train_features, train_labels)
test_predict = clf.predict(test_features)
score = accuracy_score(test_labels, test_predict)
print("分类：", score)

