import numpy as np
import matplotlib.pyplot as plt

# (1) 创建多项式函数及其导函数。
func = np.poly1d(np.array([1, 2, 3, 4]).astype(float))
x = np.linspace(-10, 10, 30)
y = func(x)
func1 = func.deriv(m=1)
y1 = func1(x)
func2 = func.deriv(m=2)
y2 = func2(x)
# (2) 使用subplot函数创建第一个子图。该函数的第一个参数是子图的行数，第二个参数是子图的列数，第三个参数是一个从1开始的序号。
plt.subplot(311)
plt.plot(x, y, 'r-' )
plt.title("Polynomial")
# (3) 使用subplot函数创建第二个子图。设置子图的标题为First Derivative，使用蓝色三角形绘制。
plt.subplot(312)
plt.plot(x, y1, 'b^')
plt.title("First Derivative")
# (4) 使用subplot函数创建第三个子图。设置子图的标题为Second Derivative，使用绿
# 色圆形绘制。
plt.subplot(313)
plt.plot(x, y2, 'go')
plt.title("Second Derivative")
plt.xlabel('x')
plt.ylabel('y')
plt.show()