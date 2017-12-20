import numpy as np

# (1) 把data数据分别加载到收盘价和成交量的数组中
c, v =np.loadtxt('data.csv',delimiter=',', usecols=(6,7), unpack= True)
# 收盘价差值的计算结果如下：
change = np.diff(c)
print("Change", change)
# (2) NumPy中的sign函数可以返回数组中每个元素的正负符号，数组元素为负时返回-1，为
#正时返回1，否则返回0。对change数组使用sign函数：
signs =np.sign(change)
print("Signs", signs)

pieces = np.piecewise(change, [change < 0 , change > 0],[-1, 1])

print("Arrags equal? ", np.array_equal(signs,pieces))
#(3) OBV值的计算依赖于前一日的收盘价，所以在我们的例子中无法计算首日的OBV值：
print("on balance volume", v[1:] * signs)