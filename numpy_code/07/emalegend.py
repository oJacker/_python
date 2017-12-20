'''
对于高质量的绘图，图例和注释是至关重要的。我们可以用legend函数创建透明的图例，
并由Matplotlib自动确定其摆放位置。 同时， 我们可以用annotate函数在图像上精确地添加注释，
并有很多可选的注释和箭头风格。

'''
from matplotlib.finance import quotes_historical_yahoo_ohlc
from matplotlib.dates import DateFormatter
from matplotlib.dates import DayLocator
from matplotlib.dates import MonthLocator
import sys
from datetime import date
import matplotlib.pyplot as plt
import numpy as np
today = date.today()
start = (today.year - 1, today.month, today.day)
symbol = 'DISH'
if len(sys.argv) == 2:
    symbol = sys.argv[1]
quotes = quotes_historical_yahoo_ohlc(symbol, start, today)
quotes = np.array(quotes)
dates = quotes.T[0]
close = quotes.T[4]
fig = plt.figure()
ax = fig.add_subplot(111)
# (1) 计算并绘制指数移动平均线：如果需要，请回到第3章中复习一下指数移动平均线的计算
#方法。分别使用9、 12和15作为周期数计算和绘制指数移动平均线
emas = []
for i in range(9, 18, 3):
    weights = np.exp(np.linspace(-1., 0., i))
    weights /= weights.sum()
    ema = np.convolve(weights, close)[i-1:-i+1]
    idx = (i - 6)/3
    ax.plot(dates[i-1:], ema, lw=idx, label="EMA(%s)" % (i))
    data = np.column_stack((dates[i-1:], ema))
    emas.append(np.rec.fromrecords(data, names=["dates", "ema"]))
# (2) 我们来找到两条指数移动平均曲线的交点。
first = emas[0]["ema"].flatten()
second = emas[1]["ema"].flatten()
bools = np.abs(first[-len(second):] - second)/second < 0.0001
xpoints = np.compress(bools, emas[1])
# (3) 我们将找到的交点用注释和箭头标注出来，并确保注释文本在交点的不远处。
for xpoint in xpoints:
    ax.annotate('x', xy=xpoint, textcoords='offset points',
            xytext=(-50, 30),
            arrowprops=dict(arrowstyle="->"))
# (4) 添加一个图例并由Matplotlib自动确定其摆放位置
leg = ax.legend(loc='best', fancybox=True)
# (5) 设置alpha通道值，将图例透明化
leg.get_frame().set_alpha(0.5)
alldays = DayLocator()
months = MonthLocator()
month_formatter = DateFormatter("%b %Y")
ax.plot(dates, close, lw=1.0, label="Close")
ax.xaxis.set_major_locator(months)
ax.xaxis.set_minor_locator(alldays)
ax.xaxis.set_major_formatter(month_formatter)
ax.grid(True)
fig.autofmt_xdate()
plt.show()