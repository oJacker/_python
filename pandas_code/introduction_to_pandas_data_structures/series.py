# -*- coding:utf-8 -*-
# 数据结构Series
'''
Series是一种类似于一维数组的对象，它由一组数据（各种NumPy数据类型）
以及一组与之相关的数据标签（即索引）组成。
• Series的字符串表现形式为：索引在左边，值在右边。
• 创建
• 读写
• 运算
'''
from pandas import Series

print("用数组生成Series")
obj = Series([4,7,-5,3])
print(obj)

print(obj.values)
print(obj.index)

print('指定Series的index')
obj2 = Series ([4,7,-5,3], index=['d', 'b', 'a', 'c'])
print(obj2)
print(obj2.index)

print(obj2['a'])
obj2['d'] = 6
print(obj2[['c','a','d']])
print(obj2[obj2 > 0])  # 找出大于0的元素

print('b' in obj2)
print('e' in obj2)

print('使用字典生成Series')

sdata = {'Ohio':45000, 'Texas':71000, 'Oregon':16000, 'Utah':5000}
obj3 =  Series(sdata)

print(obj3)

print('使用字典生成Series，并额外指定index，不匹配部分为NaN。')
states = ['California', 'Ohio', 'Oregon', 'Texas']
obj4 = Series(sdata, index= states)
print(obj4)

print('Series相加，相同索引部分相加')
print(obj3 + obj4)

print('指定Series及其索引的名字')
obj4.name = 'population'
obj4.index.name = 'state'
print(obj4)
print('替换index')
obj.index = ['Bob', 'Steve', 'Jeff', 'Ryan']
print(obj)










