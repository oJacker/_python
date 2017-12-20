'''
FFT（Fast Fourier Transform，快速傅里叶变换）是一种高效的计算DFT（Discrete Fourier
Transform，离散傅里叶变换）的算法。 FFT算法比根据定义直接计算更快，计算复杂度为
O(NlogN) 。 DFT在信号处理、图像处理、求解偏微分方程等方面都有应用。在NumPy中，有一
个名为fft的模块提供了快速傅里叶变换的功能。在这个模块中，许多函数都是成对存在的，也
就是说许多函数存在对应的逆操作函数。例如， fft和ifft函数就是其中的一对。

'''
import numpy as np
from matplotlib.pyplot import plot, show
# (1) 创建一个包含30个点的余弦波信号，如下所示：
x = np.linspace(0, 2 * np.pi, 30)
wave = np.cos(x)
# (2) 使用fft函数对余弦波信号进行傅里叶变换。
transformed = np.fft.fft(wave)
# (3) 对变换后的结果应用ifft函数，应该可以近似地还原初始信号
print (np.all(np.abs(np.fft.ifft(transformed) - wave) < 10 ** -9))
# (4) 使用Matplotlib绘制变换后的信号。
plot(transformed)
show()