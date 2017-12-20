'''
方波也是一种可以在示波器上显示的波形。方波可以近似表示为多个正弦波的叠加。事实上，
任意一个方波信号都可以用无穷傅里叶级数来表示。
'''
import numpy as np

from matplotlib.pyplot import plot
from matplotlib.pyplot import show
import sys
# (1) 我们从初始化t和k开始，并将函数值初始化为0：
t = np.linspace(-np.pi, np.pi, 201)
k = np.arange(1, float(sys.argv[1]))
k = 2 * k - 1
f = np.zeros_like(t)
# (2) 接下来，直接使用sin和sum函数进行计算：
for i in range(len(t)):
    f[i] = np.sum(np.sin(k * t[i])/k)
f = (4 / np.pi) * f
# (3) 绘制波形的代码和前面的教程中几乎一模一样：
plot(t, f)
show()