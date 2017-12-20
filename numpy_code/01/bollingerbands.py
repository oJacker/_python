'''
布林带（Bollinger band）又是一种技术指标。是的，股票市场的确有成千上万种技术指标。
布林带是以发明者约翰·布林格（John Bollinger）的名字命名的，用以刻画价格波动的区间。布
林带的基本型态是由三条轨道线组成的带状通道（中轨和上、下轨各一条）。
 中轨 简单移动平均线。
 上轨 比简单移动平均线高两倍标准差的距离。这里的标准差是指计算简单移动平均线
所用数据的标准差。
 下轨 比简单移动平均线低两倍标准差的距离。
'''
import numpy as np
import  sys
from matplotlib.pyplot import  plot
from matplotlib.pyplot import show
# (1) 我们已经有一个名为sma的数组，包含了简单移动平均线的数据。因此，我们首先要遍
# 历和这些值有关的数据子集。数据子集构建完成后，计算其标准差。



# N =int(sys.argv[1])
N = 5

weights =np.ones(N) / N
print("Weights", weights)
c = np.loadtxt('data.csv', delimiter=',' , usecols=(6,), unpack=True)
sma = np.convolve(weights, c)[N-1:-N+1]
deviation = []
C = len(c)

for i in range(N - 1, C):
    if i + N < C:
        dev = c[i: i+N]
    else:
        dev = c[-N:]
    averages = np.zeros(N)
    averages.fill(sma[i - N - 1])
    dev =dev - averages
    dev =dev ** 2
    dev = np.sqrt(np.mean(dev))
    deviation.append(dev)

deviation = 2* np.array(deviation)
print(len(deviation), len(sma))
upperBB = sma + deviation
lowerBB = sma - deviation

c_slice = c[N-1:]
between_bands = np.where((c_slice < upperBB) & (c_slice > lowerBB))
print(c[between_bands])
print(upperBB[between_bands])
between_bands = len(np.ravel(between_bands))
print("Ratio between bands", float(between_bands)/len(c_slice))
#(2) 使用如下代码绘制布林带
t = np.arange(N -1, C)
plot(t, c_slice, lw =1.0)
plot(t, sma, lw=2.0)
plot(t, upperBB, lw=3.0)
plot(t, lowerBB, lw=4.0)
show()

'''
人们通常将简单移动平均线作为布林带的中轨线。而以指数移动平均线作为中轨线也是一
种流行的做法，因此我们将它留作练习。如果需要提示，你可以在本章中找到合适的示例。
验证一下fill函数的执行速度是否真的比使用array.flat = scalar或者用循环遍历
数组赋值的方法更快。

'''