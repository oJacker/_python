'''
趋势线，是根据股价走势图上很多所谓的枢轴点绘成的曲线。顾名思义，趋势线描绘的是价
格变化的趋势。
'''

import  numpy as np
from  matplotlib.pyplot import plot
from  matplotlib.pyplot import show

def fit_line(t, y):
   A = np.vstack([t, np.ones_like(t)]).T
   return np.linalg.lstsq(A, y)[0]
# (1) 首先，我们需要确定枢轴点的位置。这里，我们假设它们等于最高价、最低价和收盘价的算术平均值。
h, l, c = np.loadtxt('data.csv', delimiter=',', usecols=(4, 5, 6), unpack=True)
'''
(2) 定义一个函数用直线y= at + b来拟合数据，该函数应返回系数a和b。这里需要再次用
到linalg包中的lstsq函数。将直线方程重写为y = Ax的形式，其中A = [t 1]， x = [a b]。
使用ones_like和vstack函数来构造数组A。
'''
pivots = (h + l + c) / 3
print("Pivots", pivots)
# (3) 假设支撑位在枢轴点下方一个当日股价区间的位置，而阻力位在枢轴点上方一个当日股
# 价区间的位置，据此拟合支撑位和阻力位的趋势线。
t = np.arange(len(c))
sa, sb = fit_line(t, pivots - (h - l))
ra, rb = fit_line(t, pivots + (h - l))

support = sa * t + sb
resistance = ra * t + rb

'''
(4) 到这里我们已经获得了绘制趋势线所需要的全部数据。但是，我们最好检查一下有多少
个数据点落在支撑位和阻力位之间。显然，如果只有一小部分数据在这两条趋势线之间，这样的
设定就没有意义。设置一个判断数据点是否位于趋势线之间的条件，作为where函数的参数。
'''
condition = (c > support) & (c < resistance)

print("Condition", condition)

between_bands = np.where(condition)

print( support[between_bands])
print(c[between_bands])
print(resistance[between_bands])
between_bands = len(np.ravel(between_bands))

print("Number points betwwen bands", between_bands)
print("Ratio between bands ", float(between_bands)/len(c))
# 我们可以用这个模型来预测下一个交易日的阻力位和支撑位。
print("Tomorows support", sa * (t[-1] + 1) + sb)
print("Tomorrows resistance", ra * (t[-1] + 1) + rb)
'''
此外，还有另外一种计算支撑位和阻力位之间数据点个数的方法：使用[]和intersect1d
函数。在[]操作符里面定义选取条件，然后用intersect1d函数计算两者相交的结果。
'''
a1 = c[c > support]
a2 = c[c < resistance]
print("Number of points between bands and approach", len(np.intersect1d(a1, a2)))

plot(t, c)
plot(t, support)
plot(t, resistance)
show()