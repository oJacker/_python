
'''
动手实践：使用布莱克曼窗平滑股价数据

'''
import numpy as np
from matplotlib.pyplot import plot, show, legend
from matplotlib.dates import datestr2num
import sys
# (1) 将数据载入NumPy数组。调用blackman函数生成一个平滑窗并用它来平滑股价数据
closes=np.loadtxt('AAPL.csv', delimiter=',', usecols=(6,),
converters={1:datestr2num}, unpack=True)
N = int(sys.argv[1])
window = np.blackman(N)
smoothed = np.convolve(window/window.sum(), closes, mode='same')
# (2) 使用Matplotlib绘制平滑后的股价图。在这个例子中，我们将省略最前面5个和最后面5个数据点。
plot(smoothed[N:-N], lw=2, label="smoothed")
plot(closes[N:-N], label="closes")
legend(loc='best')
show()