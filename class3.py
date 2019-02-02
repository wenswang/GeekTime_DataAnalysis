# -*- coding: UTF-8 -*-
# Python基础语法

# topic1
name = input("What's your name?")
sum = 100+100
print('hello, %s' %name)
print('sum = %d' %sum)

# topic2 if...else...
if score >= 90:
    print('Excellent')
else:
    if score < 60:
        print('Fail')
    else:
        print('Good Job')

# topic3 for
sum = 0
for number in range(11):
    sum = sum + number
print (sum)

# topic4 while
sum = 0
number = 1
while number < 11:
    sum = sum + number
    number = number + 1
print (sum)

# topic5 list
lists = ['a', 'b', 'c']
lists.append('d')
print (lists)
print (len(lists))
lists.insert(0, 'mm')
lists.pop()
print (lists)

# topic6 tuple
tuples = ('tupleA', 'tupleB')
print (tuples[0])

# topic7 dictionary
# 定义一个 dictionary
score = {'guanyu':95, 'zhangfei':96}
# 添加一个元素
score['zhaoyun'] = 98
print (score)
# 删除一个元素
score.pop('zhangfei')
# 查看key是否存在
print ('guanyu') in score
# 产看一个 key 对应的值
print (score.get('guanyu'))
print (score.get('yase', 99))

# topic8 set
s = set(['a', 'b', 'c'])
s.add('d')
s.remove('b')
print (s)
print ('c' in s)

# topic9 import
import module_name
import module_name1, module_name2
from package_name import module_name
from package_name import *

# topic 10 def
def addone(score):
    return score + 1
print addone(99)

# Online Judge P1
while True:
	try:
		line = raw_input()
		a = line.split()
		print (int(a[0]) + int(a[1]))
	except:
		break

# Homework1
import sklearn

# topic3 for
sum = 0
for number in range(11):
    sum = sum + number
print (sum)

# Homework2
# 方法1
sum = 0
for number in range(1, 100, 2):
    sum += number
print (sum)
# 方法2
sum = 0
number = 1
while number < 100:
    sum += number
    number += 2
print (sum)