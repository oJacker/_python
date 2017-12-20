import  numpy as np
from matplotlib.pyplot import plot
from matplotlib.pyplot import show

# (1) 首先，从CSV文件（本章示例代码文件夹中）中读入两只股票的收盘价数据
bhp = np.loadtxt('BHP.csv', delimiter=',', usecols=(6,), unpack=True)
bhp_returns = np.diff(bhp) / bhp[:-1]
vale =np.loadtxt('VALE.csv', delimiter=',' , usecols=(6,), unpack=True)
vale_returns = np.diff(vale) / vale[:-1]

'''
(2) 协方差描述的是两个变量共同变化的趋势，其实就是归一化前的相关系数。使用cov函
数计算股票收益率的协方差矩阵（并非必须这样做，但我们可以据此展示一些矩阵操作的方法）。
'''
convariance =np.cov(bhp_returns,vale_returns)
print("Convariance", convariance)
#(3) 使用diagonal函数查看对角线上的元素
print("Convariance diagonal", convariance.diagonal())
#(4) 使用trace函数计算矩阵的迹，即对角线上元素之和：
print("Convariance trace", convariance.trace())
# (5) 两个向量的相关系数被定义为协方差除以各自标准差的乘积。
print(convariance/(bhp_returns.std() * vale_returns.std()))
'''
(6) 我们将用相关系数来度量这两只股票的相关程度。相关系数的取值范围在-1到1之间。
根据定义，一组数值与自身的相关系数等于1。这是严格线性关系的理想值，实际上如果得到稍
小一些的值，我们仍然会很高兴。使用corrcoef函数计算相关系数（或者更精确地，相关系数
矩阵）：
'''
print("Correlation coneffiecient", np.corrcoef(bhp_returns,vale_returns))
#(7) 另外一个要点是判断两只股票的价格走势是否同步。如果它们的差值偏离了平均差值2
#  倍于标准差的距离，则认为这两只股票走势不同步。
difference = bhp -vale
avg = np.mean(difference)
dev = np.std(difference)

print("Out of sync", np.abs(difference[-1] - avg ) > 2 * dev)
# (8) 绘图需要Matplotlib库
t =np.arange(len(bhp_returns))
plot(t,bhp_returns, lw=1)
plot(t,vale_returns, lw=2)
show()
