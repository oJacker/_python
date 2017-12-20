# -*- coding: utf-8 -*-
import numpy as np
from pandas import Series, DataFrame

print('重复的索引')
obj = Series(range(5), index=['a', 'a', 'b', 'b', 'c'])
print(obj.index.is_unique)   # 判断是非有重复索引

print(obj['a'])
df =DataFrame(np.random.randn(4,3), index= ['a', 'a', 'b', 'b'])
print(df.ix['b'].ix[0])
print(df.ix['b'].ix[1])
