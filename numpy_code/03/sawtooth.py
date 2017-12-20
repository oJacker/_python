import numpy as np

from  matplotlib.pyplot import plot
from  matplotlib.pyplot import show
import sys
# (1) 将函数值初始化为0：
t = np.linspace(-np.pi, np.pi, 201)
k = np.arange(1, float(sys.argv[1]))
f = np.zeros_like(t)
# (2) 同样，直接使用sin和sum函数进行计算：
for i in range(len(t)):
    f[i] = np.sum(np.sin(2 * np.pi * k * t[i])/k)
f = (-2 / np.pi) * f
# (3) 同时绘制锯齿波和三角波并不难，因为三角波函数的取值恰好是锯齿波函数值的绝对值。
plot(t, f, lw=1.0)
plot(t, np.abs(f), lw=2.0)
show()