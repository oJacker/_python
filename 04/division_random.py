# -*- coding: utf-8 -*-

from __future__ import division
from numpy.random import randn
import numpy as np



# 通用函数

arr = np.array(10)
np.sqrt(arr)
np.exp(arr)

x = randn(8)
y = randn(8)

# print(x)
# print(y)

np.maximum(x, y)

arr =  randn(7) * 5
# print(arr)
np.modf(arr)


# 向量化

points  = np.arange(-5, 5, 0.01)

xs, ys = np.meshgrid(points,points)

# print(ys)

import matplotlib.pyplot as plt
z = np.sqrt(xs ** 2 + ys ** 2)
# print(z)

plt.imshow(z, cmap=plt.cm.gray) ; plt.colorbar()

plt.title("Image plot of $\sqrt{x^2 + y^2}$ for a grid of values")

plt.draw()


# 将条件逻辑表达为数组运算

xarr = np.array([1.1, 1.2, 1.3, 1.4, 1.5])
yarr = np.array([2.1, 2.2, 2.3, 2.4, 2.5])
cond = np.array([True, False, True, True, False])

result = [(x if c else y)
            for x, y, c in zip(xarr, yarr, cond)
          ]

# print(result)


arr = randn(4, 4)
# print(arr)

np.where(arr > 0, 2, -2)
np.where(arr > 0, 2, arr)

'''
result = []
for i in range(n):
    if cond1[i] and cond2[i]:
        result.append(0)
    elif cond1[i]:
        result.append(1)
    elif cond2[i]:
        result.append(2)
    else:
        result.append(3)




np.where(cond1 & cond2, 0,
         np.where(cond1, 1,
                  np.where(cond2, 2, 3)))



result = 1 * cond1 + 2 * cond2 + 3 * -(cond1 | cond2)

print(result
'''

'''
#数学与统计方法

arr = np.random.randn(5, 4)
arr.mean()
np.mean(arr)
arr.sum

arr.mean(axis=1)
arr.sum(0)


arr = np.array([[0,1,2],[3,4,5],[6,7,8]])
arr.cumsum(0)
arr.cumprod(1)
'''
'''

#用于布尔型数组的方法
arr = randn(100)
(arr > 0).sum() # 正值的数量

bools = np.array([False, False, True, False])
bools.any()
bools.all()
'''
'''
# 范例：随机漫步
import random
position = 0
walk = [position]
steps = 1000
for i in range(steps):
    step = 1 if random.randint(0, 1) else -1
    position += step
    walk.append(position)

np.random.seed(12345)

nsteps = 1000
draws = np.random.randint(0, 2, size=nsteps)
steps = np.where(draws > 0, 1, -1)
walk = steps.cumsum()

walk.min()
walk.max()

(np.abs(walk) >= 10).argmax() 


'''









# 统计分析

c = np.loadtxt('data.csv', delimiter=',' , usecols=(6,), unpack = True)
print("median =", np.median(c))

sorted =  np.msort(c)

print("sorted =",sorted)

N = len(c)
print("middle =", sorted[(N-1)/2])
 
# print ("average middle =", (sorted[N /2] + sorted[(N - 1) / 2]) / 2)




















