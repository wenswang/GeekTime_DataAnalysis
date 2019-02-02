# -*- coding: UTF-8 -*-
# Python：Numpy

import numpy as np

# topic1 创建数组
a = np.array([1, 2, 3])
b = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
b[1, 1] = 10
print(a.shape)
print(b.shape)
print(a.dtype)
print(b)

# topic2 结构数组
persontype = np.dtype({
    'names': ['name', 'age', 'chinese', 'math', 'english'],
    'formats': ['S32', 'i', 'i', 'i', 'f']})
peoples = np.array([("ZhangFei", 32, 75, 100, 90), ("GuanYu", 24, 85, 96, 88.5),
                    ("ZhaoYun", 28, 85, 92, 96.5), ("HuangZhong", 29, 65, 85, 100)], dtype=persontype)
ages = peoples[:]['age']
chineses = peoples[:]['chinese']
maths = peoples[:]['math']
englishs = peoples[:]['english']
print(ages)
print(np.mean(ages))
print(chineses)
print(np.mean(chineses))
print(maths)
print(np.mean(ages))
print(englishs)
print(np.mean(englishs))

# topic3 创建连续数组 & 算数运算
x1 = np.arange(1, 11, 2)
x2 = np.linspace(1, 9, 5)
print(x1)
print(x2)
print(np.add(x1, x2))
print(np.subtract(x1, x2))
print(np.multiply(x1, x2))
print(np.divide(x1, x2))
print(np.power(x1, x2))
print(np.remainder(x1, x2))
print(np.mod(x1, x2))

# topic4 统计函数：最大值 & 最小值
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(np.amin(a))
print(np.amin(a, 0))
print(np.amin(a, 1))
print(np.amax(a))
print(np.amax(a, 0))
print(np.amax(a, 1))

# topic5 统计函数：最大值最小值之差
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(np.ptp(a))
print(np.ptp(a, 0))
print(np.ptp(a, 1))

# topic6 统计函数：百分位数
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(np.percentile(a, 50))
print(np.percentile(a, 50, axis=0))
print(np.percentile(a, 50, axis=1))
print(np.percentile(a, 85, axis=0))
print(np.percentile(a, 85, axis=1))

# topic7 统计函数：中位数 & 平均数
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(np.median(a))
print(np.median(a, axis=0))
print(np.median(a, axis=1))
print(np.mean(a))
print(np.mean(a, axis=0))
print(np.mean(a, axis=1))

# topic8 统计函数：加权平均值
a = np.array([1, 2, 3, 4])
wts = np.array([1, 2, 3, 4])
print(np.average(a))
print(np.average(a, weights=wts))

# topic9 统计函数：标准差 & 方差
a = np.array([1, 2, 3, 4])
print(np.std(a))
print(np.var(a))

# topic10 排序
a = np.array([[4, 3, 2], [2, 4, 1]])
print(np.sort(a))
print(np.sort(a, axis=None))
print(np.sort(a, axis=0))
print(np.sort(a, axis=1))
print(np.sort(a, axis=-1))
print(np.sort(a, axis=-1, kind='quicksort', order=None))

# Homework
persontype = np.dtype({
    'names': ['name', 'chinese', 'english', 'math', 'total'],
    'formats': ['S32', 'i', 'i', 'i', 'i']})
people = np.array([("ZhangFei", 66, 65, 30,0), ("GuanYu", 95, 85, 98,0), ("ZhaoYun", 93, 92, 96,0),
                   ("HuangZhong", 90, 88, 77,0), ("DianWei", 80, 90, 90,0)], dtype=persontype)
chineses = people[:]['chinese']
englishs = people[:]['english']
maths = people[:]['math']
people[:]['total'] = people[:]['chinese']+people[:]['english']+people[:]['math']
totals = people[:]['total']

result_type = np.dtype({
    'names': ['name', 'chinese', 'english', 'math'],
    'formats': ['S32', 'f', 'f', 'f']})
people_result = np.array([
    ("Mean", np.mean(chineses), np.mean(englishs), np.mean(maths)),
    ("Min", np.amin(chineses), np.amin(englishs), np.amin(maths)),
    ("Max", np.amax(chineses), np.amax(englishs), np.amax(maths)),
    ("Variance", np.var(chineses), np.var(englishs), np.var(maths)),
    ("SD", np.std(chineses), np.std(englishs), np.std(maths))], dtype=result_type)
print(people_result)
print(np.sort(people, order='total'))