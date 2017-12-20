import numpy as np
import matplotlib.pyplot as plt
# (1) 创建多项式函数及其导函数。
func = np.poly1d(np.array([1,2,3,4]).astype(float))
func1 = func.deriv(m =1)
x =np.linspace(-10,10,30)
y = func(x)
y1 = func1(x)
# (2)以两种不同风格绘制多项式函数及其导函数：红色圆形和绿色虚线。你可能无法在本书
# 的印刷版中看到彩色图像，因此只能自行尝试绘制图像。
plt.plot(x,y, 'ro', x, y1, 'g--')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
