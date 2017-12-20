'''
连续分布可以用PDF（Probability Density Function，概率密度函数）来描述。随机变量落在某
一区间内的概率等于概率密度函数在该区间的曲线下方的面积。 NumPy的random模块中有一系列
连续分布的函数——beta、chisquare、exponential、f、gamma、gumbel、laplace、lognormal、
logistic、 multivariate_normal、 noncentral_chisquare、 noncentral_f、 normal等
随机数可以从正态分布中产生，它们的直方图能够直观地刻画正态分布。按照如下步骤绘制
正态分布。
'''
import numpy as np
import matplotlib.pyplot as plt
# (1) 使用NumPy random模块中的normal函数产生指定数量的随机数
N = 10000
normal_values = np.random.normal(size=N)
# 2) 绘制分布直方图和理论上的概率密度函数（均值为0、方差为1的正态分布）曲线。我们
# 将使用Matplotlib进行绘图。
dummy, bins, dummy = plt.hist(normal_values, np.sqrt(N), normed=True, lw=1.0)

sigma = 1
mu = 0
plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) * np.exp( - (bins -mu)**2 / (2 * sigma**2) ),lw=2)
plt.show()