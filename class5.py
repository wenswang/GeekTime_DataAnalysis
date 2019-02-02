# -*- coding: UTF-8 -*-
# Python：Pandas

import numpy as np
import pandas as pd
from pandas import Series, DataFrame
from pandasql import sqldf, load_meat, load_births

# topic1 Series
x1 = Series([1, 2, 3, 4])
x2 = Series(data=[1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
print(x1)
print(x2)

# topic2 DataFrame
data = {'Chinese': [66, 95, 93, 90, 80], 'English': [65, 85, 92, 88, 90], 'Math': [30, 98, 96, 77, 90]}
df1 = DataFrame(data)
df2 = DataFrame(data, index=['Zhangfei', 'GuanYu', 'ZhaoYun', 'HuangZhong', 'DianWei'], columns=['English', 'Math', 'Chinese'])
print(df1)
print(df2)

# topic3 读取/存储 xlsx and csv
score = DataFrame(pd.read_excel('data1.xlsx'))
score.to_excel('data2.xlsx')
print(score)

# topic4 数据清洗
data = {'Chinese': ['66', ' 95', ' 93', ' 90', ' 80'], 'English': ['65',' 85',' 92',' 88',' 90'], 'Math': ['30',' 98',' 96',' 77',' 90']}
df2 = DataFrame(data, index=['ZhangFei', 'GuanYu', 'ZhaoYun', 'HuangZhong', 'DianWei'], columns=['English', 'Math', 'Chinese'])
# 删除
df2 = df2.drop(columns=['Chinese'])
df2 = df2.drop(index=['Zhangfei'])
print(df2)
# 重命名列名
df2.rename(columns={'Chinese': 'Yuwen', 'English': 'Yinyu'}, inplace=True)
print(df2)
# 去除重复值
df2 = df2.drop_duplicates()
print(df2)
# 更改数据格式
df2['Chinese'].astype('str')
df2['Chinese'].astype(np.int64)
print(df2)
# 删除空格
df2['Chinese'] = df2['Chinese'].map(str.strip)
df2['Chinese'] = df2['Chinese'].map(str.lstrip)
df2['Chinese'] = df2['Chinese'].map(str.rstrip)
print(df2)
# 大小写转换
df2.columns = df2.columns.str.upper()
df2.columns = df2.columns.str.lower()
df2.columns = df2.columns.str.title()
print(df2)
# 查找空值
data1 = {'Name': ['ZhangFei', 'GuanYu', 'ZhaoYun', 'HuangZhong', 'DianWei'],
        'Chinese': [66, 95, 93, 90, 80],
        'English': [65, 85, 92, 88, 90],
        'Math': [np.nan, 98, 96, 77, 90]}
df1 = DataFrame(data1,  columns=['Name', 'English', 'Math', 'Chinese'])
# print(df1)
# print(df1.isnull())
# print(df1.isnull().any())
# 使用apply函数清洗
df1['Name'] = df1['Name'].apply(str.upper)
print(df1)
def double_df(x):
    return 2*x
df1['Chinese'] = df1['Chinese'].apply(double_df)
print(df1)
def plus(df, n, m):
    df['new1'] = (df['Chinese'] + df['English']) * m
    df['new2'] = (df['Chinese'] + df['English']) * n
    return df
df1 = df1.apply(plus,axis=1, args=(2, 3,))
print(df1)

# topic5 数据统计
df1 = DataFrame({'name': ['ZhangFei', 'GuanYu', 'a', 'b', 'c'], 'data1': range(5)})
print(df1)
print(df1.describe())

# topic6 数据表合并
df1 = DataFrame({'name': ['ZhangFei', 'GuanYu', 'a', 'b', 'c'], 'data1': range(5)})
df2 = DataFrame({'name': ['ZhangFei', 'GuanYu', 'A', 'B', 'C'], 'data2': range(5)})
df3 = pd.merge(df1, df2, on='name')
print(df3)
df3 = pd.merge(df1, df2, how='inner')
print(df3)
df3 = pd.merge(df1, df2, how='left')
print(df3)
df3 = pd.merge(df1, df2, how='right')
print(df3)
df3 = pd.merge(df1, df2, how='outer')
print(df3)

# topic7 SQL方式打开Pandas
df1 = DataFrame({'name': ['ZhangFei', 'GuanYu', 'a', 'b', 'c'], 'data1': range(5)})
print(df1)
pysqldf = lambda sql: sqldf(sql, globals())
sql = "select * from df1 where name = 'ZhangFei'"
print(pysqldf(sql))

# Homework
data1 = {'Name': ['ZhangFei', 'GuanYu', 'ZhaoYun', 'HuangZhong', 'DianWei', 'DianWei'],
        'Chinese': [66, 95, 93, 90, 80, 80],
        'English': [65, 85, 92, 88, 90, 90],
        'Math': [None, 98, 96, 77, 90, 90]}
df1 = DataFrame(data1,  columns=['Name', 'Chinese', 'English', 'Math'])
df1 = df1.drop_duplicates()
df1.rename(columns={'Name': '名字', 'English': '英语', 'Chinese': '语文', 'Math': '数学'}, inplace=True)
df1['数学'].fillna(np.mean(df1['数学']), inplace=True)
df1['总成绩'] = df1.sum(axis=1)
print(df1.sort_values(by='总成绩', ascending=False))