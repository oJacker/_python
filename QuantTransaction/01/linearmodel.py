#!/usr/bin/python

import  numpy as np
import sys
# (1) 首先，获取一个包含N个股价的向量b。
N = 5

close = np.loadtxt('../CSV/600808_2017.csv',delimiter=',',skiprows=1,usecols=(3,),unpack=True)
close = close[::-1]
b = close[-N:]
print(b)
# (2) 第二步，初始化一个N×N的二维数组A，元素全部为0。
A = np.zeros((N, N), float)
# (3) 第三步，用b向量中的N个股价值填充数组A。
for i in range(N):
    A[i, ]= close[-N -1 -i: -1 -i]
print("A", A)

#(4) 我们的目标是确定线性模型中的那些系数，以解决最小平方和的问题。我们使用linalg包中的lstsq函数来完成这个任务。
(x,residuals, rank, s) = np.linalg.lstsq(A,b)
print(x, residuals, rank, s)
print(np.dot(b, x))