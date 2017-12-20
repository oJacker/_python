from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
fig = plt.figure()
# (1) 我们需要使用3d关键字来指定图像的三维投影。
ax = fig.add_subplot(111, projection='3d')
# (2) 我们将使用meshgrid函数创建一个二维的坐标网格。这将用于变量x和y的赋值。
u = np.linspace(-1, 1, 100)
x, y = np.meshgrid(u, u)
z = x ** 2 + y ** 2
# (3) 我们将指定行和列的步幅，以及绘制曲面所用的色彩表（color map）。步幅决定曲面上“瓦
# 片”的大小，而色彩表的选择取决于个人喜好
ax.plot_surface(x, y, z, rstride=4, cstride=4, cmap=cm.YlGnBu_r)
plt.show()