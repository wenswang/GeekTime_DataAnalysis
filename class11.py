# -*- coding: UTF-8 -*-
# 数据清洗

import numpy as np
import pandas as pd
from pandas import DataFrame

# topic1 缺失值
# topic1.1 平均值填充
df['Age'].fillna(df['Age'].mean(), inplace=True)
# topic1.2 高频数据填充
age_maxf = train_features['Age'].value_counts().index[0]
train_features['Age'].fillna(age_maxf, inplace=True)

# topic2 空行
df.dropna(how='all', inplace=True)

# topic3 单位不统一
rows_with_lbs = df['weight'].str.contains('lbs').fillna(False)
print(df[rows_with_lbs])
for i, lbs_row in df[rows_with_lbs].iterrows():
    weight = int(float(lbs_row['weight'][:-3])/2.2)
    df.at[i, 'weight'] = '{}kgs'.format(weight)

# topic4 非ASCII字符
df['first_name'].replace({r'[^\x00-\x7F]+':''}, regex=True, inplace=True)
df['last_name'].replace({r'[^\x00-\x7F]+':''}, regex=True, inplace=True)

# topic5 拆分列
df[['first_name', 'last_name']] = df['name'].str.split(expand=True)
df.drop('name', axis=1, inplace=True)

# topic6 删除重复数据
df.drop_duplicates(['first_name', 'last_name'], inplace=True)

# Homework
df = DataFrame(pd.read_excel('class11_data.xlsx'))
df['food'] = df['food'].str.title()
df['ounces'].fillna(df['ounces'].mean(), inplace=True)
df['ounces'][df['ounces'] < 0] = 0
print(df)


