#  -*- coding:utf-8 -*-
import numpy as np
import sys
from matplotlib.pyplot import plot
from matplotlib.pyplot import  show
'''
简单移动平均线（simple moving average）通常用于分析时间序列上的数据。为了计算它，
我们需要定义一个N个周期的移动窗口，在我们的例子中即N个交易日。我们按照时间序列滑动
这个窗口，并计算窗口内数据的均值
'''
# 卷积是分析数学中一种重要的运算，定义为一个函数与经过翻转和平移的另一个函数的乘积的积分。

#(1) 使用ones函数创建一个长度为N的元素均初始化为1的数组，然后对整个数组除以N，即可得到权重。

# N = (list(sys.argv[1]))
#简单移动平均线
N = 5
weights = np.ones(N) / N

print("Weights", weights)
# (2) 使用这些权重值，调用convolve函数：
c = np.loadtxt('data.csv', delimiter=',' , usecols=(6,), unpack=True)
sma =np.convolve(weights, c)[N-1:-N+1]

#(3) 我们从convolve函数返回的数组中，取出中间的长度为N的部分①。下面的代码将创建一个存储时间值的数组，并使用Matplotlib进行绘图。
t = np.arange(N - 1,len(c))
plot(t, c[N-1:], lw = 1.0)
plot(t, sma, lw=2.0)
show()


