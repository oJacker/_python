# -*- coding:utf-8 -*-

import  numpy as np
import sys
from matplotlib.pyplot import plot
from matplotlib.pyplot import show

# N = int(sys.argv[1])
# (1) 调用hanning函数计算权重，生成一个长度为N的窗口（在这个示例中N取8）：
N =8
weights = np.hanning(N)
print('Weights', weights)
# (2) 使用convolve函数计算BHP和VALE的股票收益率，以归一化处理后的weights作为参数：
bhp = np.loadtxt('BHP.csv',delimiter=',', usecols=(6,), unpack=True)
bhp_returns= np.diff(bhp)/bhp[: -1]
smooth_bhp = np.convolve(weights/weights.sum(), bhp_returns)[N-1:-N+1]
vale = np.loadtxt('VALE.csv',delimiter=',' , usecols=(6,), unpack=True)
vale_returns= np.diff(vale)/vale[: -1]
smooth_vale = np.convolve(weights/weights.sum(), vale_returns)[N-1:-N+1]
# (4) 使用多项式拟合平滑后的数据：
K = int(sys.argv[1])
t = np.arange(N - 1,len(bhp_returns))
poly_bhp = np.polyfit(t, smooth_bhp, K)
poly_vale = np.polyfit(t, smooth_vale, K)
#(5) 现在，我们需要解出上面的两个多项式何时取值相等，即在哪些地方存在交叉点。这等
# 价于先对两个多项式函数作差，然后对所得的多项式函数求根。使用polysub函数对多项式作差:
poly_sub = np.polysub(poly_bhp,poly_vale)
xpoints = np.roots(poly_sub)
print("Intersection points",xpoints)

reals = np.isreal(xpoints)
print("Real number?", reals)
# 6) 得到的结果为复数，这不利于我们后续处理，除非时间也有实部和虚部。因此，这里需
# 要用isreal函数来判断数组元素是否为实数：
xpoints = np.select([reals],[xpoints])
xpoints = xpoints.real
print("Real intersection points", xpoints)
#(7) 我们需要去掉其中为0的元素。 trim_zeros函数可以去掉一维数组中开头和末尾为0的元素：
print("Sans 0s", np.trim_zeros(xpoints))
# 用Matplotlib绘图：
plot(t, bhp_returns[N-1:],lw =1.0)
plot(t, smooth_bhp, lw=2.0)
plot(t, vale_returns[N-1:], lw=1.0)
plot(t, smooth_vale, lw=2.0)
show()
'''
请尝试使用其他的平滑函数，如hamming、 blackman、 bartlett以及kaiser。它们的
使用方法和hanning函数类似。
'''
