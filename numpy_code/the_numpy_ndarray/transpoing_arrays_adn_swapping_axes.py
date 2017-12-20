# -*- coding:utf-8 -*-

import numpy as np
import numpy.random as np_random

# 转置矩阵
arr = np.arange(15).reshape((3, 5))
print(arr)

print(arr.T)

# 转置矩阵做点积
arr = np_random.rand(6, 3)
print(arr)
print('-------------')
print(np.dot(arr.T, arr))
print('-------------')
# 高维矩阵转换
arr = np.arange(16).reshape((2, 2, 4))
print(arr)
print('-------------')
print(arr[0][1])
print('-------------')
print(arr.transpose((1, 0, 2)))
print('-------------')
print(arr.swapaxes(1, 2)) # 直接交换第1和第2个坐标