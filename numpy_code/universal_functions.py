# -*- coding:utf-8 -*-
import numpy as np
import numpy.random as np_random

# 求平方根
arr = np.arange(10)
print(np.sqrt(arr))


print('数组比较')
x = np_random.rand(8)
y = np_random.rand(8)

#print(x)
#print(y)

print(np.maximum(x, y))

# 使用modf函数把浮点数分解成整数和小数部分

arr =np_random.rand(7) * 5  # 统一乘5
print(arr)
print(np.modf(arr))