# -*- coding: utf-8 -*-

import  numpy as np
import numpy.random as np_random

# 一维数组排序
arr = np_random.randn(8)
arr.sort()  # 升序
print(arr)

# 二维数组排序
arr = np_random.randn(5, 3)
print(arr)
arr.sort(1)  # 对每一行元素做排序
arr.sort(0)  # 对每一列元素做排序
print(arr)

# 找位置在5%的数字

large_arr = np_random.randn(10000)
large_arr.sort()
print(large_arr[int(0.05) * len(large_arr)])

