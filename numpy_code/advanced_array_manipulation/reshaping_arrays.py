# -*- coding: utf-8 -*-
import numpy as np
print('将一维数组转换为二维数组')
arr = np.arange(8)
arr.reshape((4, 2))
print(arr)
print(arr.reshape((4, 2)).reshape((2, 4)))

print('维度大小自动推导')
arr = np.arange(15)
print(arr.reshape(5, -1))

print('获取维度信息并应用')
other_arr =np.ones((3, 5))
print(other_arr.shape)
print(arr.reshape(other_arr.shape))

print('高维数组拉平')
arr = np.arange(15).reshape((5, 3))
print(arr.ravel())