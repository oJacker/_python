# -*- coding:utf-8 -*-
'''
数据结构 索引对象
• pandas的索引对象负责管理轴标签和其他元数据（比如轴名称等）。构建
Series或DataFrame时，所用到的任何数组或其他序列的标签都会被转换成一
个Index。
• Index对象是不可修改的（immutable），因此用户不能对其进行修改。不可
修改性非常重要，因为这样才能使Index对象在多个数据结构之间安全共享。
'''

import numpy as np
import pandas as pd
import sys
from pandas import  Series, DataFrame, Index

print('获取index')
obj = Series(range(3), index= ['a','b','c'])
index = obj.index
print(index[1:])
try:
    index[1] = 'd'
except:
    print(sys.exc_info()[0])

print('使用Index对象')
index = Index(np.arange(3))
obj2 = Series([1.5, -2.5, 0], index = index)
print(obj2)
print(obj2.index is index)

print('判断列和索引是否存在')
pop = {'Nevada':{20001:2.4, 2002:2.9},
        'Ohio':{2000:1.5, 2001:1.7, 2002:3.6}
       }
frame3 = DataFrame(pop)
print('Ohio' in frame3.columns)
print('2003' in  frame3.index)
