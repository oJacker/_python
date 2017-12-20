'''
移频
numpy.linalg模块中的fftshift函数可以将FFT输出中的直流分量移动到频谱的中央。
ifftshift函数则是其逆操作。
'''
import numpy as np
from matplotlib.pyplot import plot, show
# (1) 创建一个包含30个点的余弦波信号。
x = np.linspace(0, 2 * np.pi, 30)
wave = np.cos(x)
# (2) 使用fft函数对余弦波信号进行傅里叶变换。
transformed = np.fft.fft(wave)

# (3) 使用fftshift函数进行移频操作。
shifted = np.fft.fftshift(transformed)
# (4) 用ifftshift函数进行逆操作，这将还原移频操作前的信号
print (np.all(np.abs(np.fft.ifftshift(shifted) - transformed) < 10 ** -9))
plot(transformed, lw=2)
plot(shifted, lw=3)
show()