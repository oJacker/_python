'''
除了简单移动平均线，指数移动平均线（exponential moving average）也是一种流行的技术
指标。指数移动平均线使用的权重是指数衰减的。对历史上的数据点赋予的权重以指数速度减小，
但永远不会到达0。我们将在计算权重的过程中学习exp和linspace函数。
'''
import numpy as np
import sys
from  matplotlib.pyplot import plot
from  matplotlib.pyplot import show
# 定一个数组， exp函数可以计算出每个数组元素的指数
x = np.arange(5)
#print("Exp", np.exp(x))
#Exp [  1.           2.71828183   7.3890561   20.08553692  54.59815003]
#linspace函数需要一个起始值和一个终止值参数，以及可选的元素个数的参数，它将返回 一个元素值在指定的范围内均匀分布的数组。

#print("Linspace", np.linspace(-1, 0, 5))
# Linspace [-1.   -0.75 -0.5  -0.25  0.  ]
# (1) 还是回到权重的计算——这次使用exp和linspace函数。
#N = int(sys.argv[1])
N = 5
weights = np.exp(np.linspace(-1. , 0. , N))
# (2) 对权重值做归一化处理。我们将用到ndarray对象的sum方法。
weights /= weights.sum()
print("Weights", weights)

c = np.loadtxt('data.csv', delimiter=',', usecols=(6,), unpack=True)
ema = np.convolve(weights,c)[N-1:-N+1]
t = np.arange(N-1, len(c))
plot(t, c[N-1:],lw = 1.0)
plot(t, ema, lw =2.0)
show()