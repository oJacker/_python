import numpy as np
import matplotlib.pyplot as plt
# 1) 以自然数序列作为多项式的系数，使用poly1d函数创建多项式
func = np.poly1d(np.array([1,2,3,4]).astype(float))
# (2) 使用NumPy的linspace函数创建x轴的数值，在-10和10之间产生30个均匀分布的值。
x = np.linspace(-10, 10, 30)
# (3) 计算我们在第一步中创建的多项式的值。
y =func(x)
# (4) 调用plot函数，这并不会立刻显示函数图像。
plt.plot(x,y)
# (5) 使用xlabel函数添加x轴标签
plt.xlabel('x')
# (6) 使用ylabel函数添加y轴标签。
plt.ylabel('y(x)')
# (7) 调用show函数显示函数图像
plt.show()