'''
拟合正弦波
'''
from matplotlib.finance import quotes_historical_yahoo_ohlc
import numpy as np
import matplotlib.pyplot as plt
from scipy import fftpack
from scipy import signal
from matplotlib.dates import DateFormatter
from matplotlib.dates import DayLocator
from matplotlib.dates import MonthLocator
from scipy import optimize
start = (2010, 7, 25)
end = (2011, 7, 25)
quotes = quotes_historical_yahoo_ohlc("QQQ", start, end)
quotes = np.array(quotes)
dates = quotes.T[0]
qqq = quotes.T[4]
y = signal.detrend(qqq)
alldays = DayLocator()
months = MonthLocator()
month_formatter = DateFormatter("%b %Y")
fig = plt.figure()
fig.subplots_adjust(hspace=.3)
ax = fig.add_subplot(211)
ax.xaxis.set_minor_locator(alldays)
ax.xaxis.set_major_locator(months)
ax.xaxis.set_major_formatter(month_formatter)
ax.tick_params(axis='both', which='major', labelsize='x-large')
amps = np.abs(fftpack.fftshift(fftpack.rfft(y)))
amps[amps < amps.max()] = 0
# (1) 根据正弦波模型，定义residuals函数：
def residuals(p, y, x):
    A,k,theta,b = p
    err = y-A * np.sin(2* np.pi* k * x + theta) + b
    return err
# (2) 将滤波后的信号变换回时域：
filtered = -fftpack.irfft(fftpack.ifftshift(amps))
 # (3) 猜测参数的值，尝试估计从时域到频域的变换函数：
N = len(qqq)
f = np.linspace(-N/2, N/2, N)
p0 = [filtered.max(), f[amps.argmax()]/(2*N), 0, 0]
print ("P0", p0)
# 4) 调用leastsq函数：
plsq = optimize.leastsq(residuals, p0, args=(filtered, dates))
p = plsq[0]
print ("P", p)
# (5) 在第一个子图中绘制去除趋势后的数据、滤波后的数据及其拟合曲线。
plt.plot(dates, y, 'o', label="detrended")
plt.plot(dates, filtered, label="filtered")
plt.plot(dates, p[0] * np.sin(2 * np.pi * dates * p[1] + p[2]) + p[3], '^', label="fit")
fig.autofmt_xdate()
plt.legend(prop={'size':'x-large'})
# (6) 添加第二个子图，绘制主频率部分的频谱图和图例。
ax2 = fig.add_subplot(212)
ax2.tick_params(axis='both', which='major', labelsize='x-large')
plt.plot(f, amps, label="transformed")
plt.legend(prop={'size':'x-large'})
plt.show()