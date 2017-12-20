# -*- coding: utf-8 -*-
'''
基本功能 丢弃指定轴上的项
• 丢弃某条轴上的一个或多个项很简单，只要有一个索引数组或列表即可。由于
需要执行一些数据整理和集合逻辑，所以drop方法返回的是一个在指定轴上删
除了指定值的新对象
'''
import  numpy as np
from  pandas import  Series, DataFrame

print('Series根据索引删除元素')
obj = Series(np.arange(5.), index=['a', 'b', 'c', 'd', 'e'])
new_obj = obj.drop('c')
print(new_obj)
print(obj.drop(['d','c']))

print('DataFrame删除元素，可指定索引或列。')
data = DataFrame(np.arange(16).reshape((4,4)),
                 index=['Ohio', 'Colorado', 'Utah', 'New York'],
                 columns=['one', 'two', 'three', 'four'])
print(data)
print(data.drop(['Colorado', 'Ohio']))
print(data.drop('two',axis=1))
print(data.drop(['two','four'], axis= 1))