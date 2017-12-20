from scipy import stats
import matplotlib.pyplot as plt
# (1) 使用scipy.stats包按正态分布生成随机数。
generated = stats.norm.rvs(size=900)
# (2) 用正态分布去拟合生成的数据，得到其均值和标准差：
print ("Mean", "Std", stats.norm.fit(generated))
# (3) 偏度（skewness）描述的是概率分布的偏斜（非对称）程度。
print ("Skewtest", "pvalue", stats.skewtest(generated))
# (4) 峰度（kurtosis）描述的是概率分布曲线的陡峭程度。
print ("Kurtosistest", "pvalue", stats.kurtosistest(generated))
# (5) 正态性检验（normality test）可以检查数据集服从正态分布的程度。我们来做一个正态性检验
print ("Normaltest", "pvalue", stats.normaltest(generated))
# (6) 使用SciPy我们可以很方便地得到数据所在的区段中某一百分比处的数值：
print ("95 percentile", stats.scoreatpercentile(generated, 95))
# (7) 将前一步反过来，我们也可以从数值1出发找到对应的百分比：
print ("Percentile at 1", stats.percentileofscore(generated, 1))
# (8) 使用Matplotlib绘制生成数据的分布直方图。
plt.hist(generated)
plt.show()