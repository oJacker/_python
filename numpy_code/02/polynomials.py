import  numpy as np
import  sys
from matplotlib.pyplot import plot
from matplotlib.pyplot import show
#(1) 我们继续使用BHP和VALE的股票价格数据。用一个三次多项式去拟合两只股票收盘价的差价：
bhp = np.loadtxt()
vale = np.loadtxt()
t = np.arange(len(bhp))
poly = np.polyfit(t, bhp - vale, int(sys.argv[1]))
print("Polynomial fit", poly)
#(2) 上面看到的那些数字就是多项式的系数。用我们刚刚得到的多项式对象以及polyval函
#数，就可以推断下一个值：
print("Next value", np.polyval(poly, t[-1] + 1))
'''
(3) 理想情况下， BHP和VALE股票收盘价的差价越小越好。在极限情况下，差值可以在某个
点为0。使用roots函数找出我们拟合的多项式函数什么时候到达0值：
'''
print("Roots", np.roots(poly))
# (4) 我们在微积分课程中还学习过求极值的知识——极值可能是函数的最大值或最小值。
der = np.polyder(poly)
print("Derivative", der)
# (5) 求出导数函数的根，即找出原多项式函数的极值点：
print("Extremas", np.roots(der))
# (6) 现在，使用argmax和argmin找出最大值点和最小值点
vals = np.polyval(poly, t)
print(np.argmax(vals))
print(np.argmin(vals))
# (7) 绘制源数据和拟合函数如下：
plot(t, bhp -vale)
plot(t, vals)

'''
本节中的拟合函数有很多可以改进的地方。尝试使用三次方之外的不同指数，或者考虑在
拟合前对数据进行平滑处理。使用移动平均线就是一种数据平滑的方法。计算简单移动平均线
和指数移动平均线的示例可参阅前面的章节
'''