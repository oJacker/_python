
'''
对数正态分布（lognormal distribution） 是自然对数服从正态分布的任意随机变量的概率分
布。 NumPy random模块中的lognormal函数模拟了这个分布。

'''

import numpy as np
import matplotlib.pyplot as plt
# (1) 使用NumPy random模块中的normal函数产生随机数。
N=10000
lognormal_values = np.random.lognormal(size=N)
# (2) 绘制分布直方图和理论上的概率密度函数（均值为0、方差为1）。
dummy, bins, dummy = plt.hist(lognormal_values, np.sqrt(N),normed=True, lw=1)
sigma = 1
mu = 0
x = np.linspace(min(bins), max(bins), len(bins))
pdf = np.exp(-(np.log(x) - mu)**2 / (2 * sigma**2))/ (x * sigma * np.sqrt(2 * np.pi))
plt.plot(x, pdf,lw=3)
plt.show()