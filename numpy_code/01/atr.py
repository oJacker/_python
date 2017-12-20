import numpy as np
import sys

# 真实波动幅度均值
h, l, c = np.loadtxt('data.csv', delimiter=',', usecols=(4, 5, 6), unpack=True)

# (1) ATR是基于N个交易日的最高价和最低价进行计算的，通常取最近20个交易日
# N = int(sys.argv[1])
N = 20
h = h[-N:]
l = l[-N:]
print("len(h)", len(h), "len(l)", len(l))
print("Close:", c)
# (2) 我们还需要知道前一个交易日的收盘价。
previousclose = c[-N -1: -1]
print ("len(previousclose)", len(previousclose))
print ("Previous close", previousclose)

'''
对于每一个交易日，计算以下各项。
h – l 当日股价范围，即当日最高价和最低价之差。
h – previousclose 当日最高价和前一个交易日收盘价之差。
previousclose – l 前一个交易日收盘价和当日最低价之差
'''
#(3) max函数返回数组中的最大值。基于上面计算的3个数值，我们来计算所谓的真实波动幅度，也就是这三者的最大值。
print ("len(previousclose)", len(previousclose))
print ("Previous close", previousclose)
truerange = np.maximum(h - l, h - previousclose, previousclose - l)
print ("True range", truerange)
# (4) 创建一个长度为N的数组atr，并初始化数组元素为0。
atr = np.zeros(N)
# (5) 这个数组的首个元素就是truerange数组元素的平均值。
atr[0] = np.mean(truerange)

# PATR表示前一个交易日的ATR值， TR即当日的真实波动幅度。
for i in range(1, N):
    atr[i] = (N - 1) * atr[i - 1] + truerange[i]
    atr[i] /= N
print ("ATR", atr)
'''
生成了3个数组，分别表示3种范围——当日股价范围，当日最高价和前一个交易日收盘
价之差，以及前一个交易日收盘价和当日最低价之差
'''