#!/usr/bin/python
import  numpy as np
import sys
from matplotlib.pyplot import plot,show

'''
除了简单移动平均线，指数移动平均线（exponential moving average）也是一种流行的技术
指标。指数移动平均线使用的权重是指数衰减的。对历史上的数据点赋予的权重以指数速度减小，
但永远不会到达0。我们将在计算权重的过程中学习exp和linspace函数。
'''
# (1) 还是回到权重的计算——这次使用exp和linspace函数。
N =5
weights = np.exp(np.linspace(-1, 0., N))
# (2) 对权重值做归一化处理。我们将用到ndarray对象的sum方法。
weights /= weights.sum()
print("Weights", weights)

close = np.loadtxt('../CSV/002361_2017.csv',delimiter=',',skiprows=1,usecols=(3,),unpack=True)
close = close[::-1]
ema = np.convolve(weights,close)[N-1:-N+1]
t = np.arange(N-1, len(close))
plot(t, close[N-1:],lw = 1.0)
plot(t, ema, lw =2.0)
show()