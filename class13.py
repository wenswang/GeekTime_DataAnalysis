# -*- coding: UTF-8 -*-
# 数据转换

from sklearn import preprocessing
import numpy as np

x = np.array([[0., -3., 1.],
              [3., 1., 2.],
              [0., 1., -1.]])

# topic1 Mix-max规范化
min_max_scaler = preprocessing.MinMaxScaler()
minmax_x = min_max_scaler.fit_transform(x)
print(minmax_x)

# topic2 Z-Score规范化
scaled_x = preprocessing.scale(x)
print(scaled_x)

# topic3 小数定标规范化
j = np.ceil(np.log10(np.max(abs(x))))
scaled_x = x/(10**j)
print(scaled_x)

# Homework
y = np.array([[5000.], [16000.], [58000.]])
min_max_scaler = preprocessing.MinMaxScaler()
minmax_y = min_max_scaler.fit_transform(y)
print(minmax_y)
