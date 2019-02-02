# -*- coding: UTF-8 -*-
# 数据可视化

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
from matplotlib.font_manager import FontProperties

# topic1 散点图
N = 1000
x = np.random.randn(N)
y = np.random.randn(N)
plt.scatter(x, y, marker='x')
plt.show()
df = pd.DataFrame({'x': x, 'y': y})
sns.jointplot(x="x", y="y", data=df, kind='scatter')
plt.show()

# topic2 折线图
x = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]
y = [5, 3, 6, 20, 17, 16, 19, 30, 32, 35]
plt.plot(x, y)
plt.show()
df = pd.DataFrame({'x': x, 'y': y})
sns.lineplot(x="x", y="y", data=df)
plt.show()

# topic3 直方图
a = np.random.randn(100)
s = pd.Series(a)
plt.hist(s)
plt.show()
sns.distplot(s, kde=False)
plt.show()
sns.distplot(s, kde=True)
plt.show()

# topic4 条形图
x = ['Cat1', 'Cat2', 'Cat3', 'Cat4', 'Cat5']
y = [5, 4, 7, 5, 8]
plt.bar(x, y)
plt.show()
sns.barplot(x, y)
plt.show()

# topic5 箱线图
data = np.random.normal(size=(10, 4))
labels = ['A', 'B', 'C', 'D']
plt.boxplot(data, labels=labels)
plt.show()
df = pd.DataFrame(data, columns=labels)
sns.boxplot(data=df)
plt.show()

# topic6 饼图
nums = [25, 37, 33, 27, 5]
labels = ['High-school', 'Bachelor', 'Master', 'Ph.d', 'Others']
plt.pie(x=nums, labels=labels)
plt.show()

# topic7 热力图
flights = pd.read_csv('dataset/flights.csv')
data = flights.pivot('year', 'month', 'passengers')
sns.heatmap(data)
plt.show()

# topic8 蜘蛛图
labels = np.array([u"推进", "KDA", u"生存", u"团战", u"发育", u"输出"])
stats = [83, 61, 95, 67, 76, 88]
angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False)
stats = np.concatenate((stats, [stats[0]]))
angles = np.concatenate((angles, [angles[0]]))
fig = plt.figure()
ax = fig.add_subplot(111, polar=True)
ax.plot(angles, stats, 'o-', linewidth=2)
ax.fill(angles, stats, alpha=0.25)
font = FontProperties(fname='/System/Library/Fonts/PingFang.ttc', size=14)
ax.set_thetagrids(angles * 180 / np.pi, labels, FontProperties=font)
plt.show()

# topic9 二元变量分布
tips = pd.read_csv('dataset/tips.csv')
print(tips.head(10))
sns.jointplot(x="total_bill", y="tip", data=tips, kind='scatter')
sns.jointplot(x="total_bill", y="tip", data=tips, kind='kde')
sns.jointplot(x="total_bill", y="tip", data=tips, kind='hex')
plt.show()

# topic10 成对关系
iris = pd.read_csv('dataset/iris.csv')
sns.pairplot(iris)
plt.show()

# homework
car_crashes = pd.read_csv('dataset/car_crashes.csv')
sns.pairplot(car_crashes)
sns.jointplot(x="total", y="speeding", data=car_crashes, kind='kde')
plt.show()
