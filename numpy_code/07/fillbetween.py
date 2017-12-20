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
alldays = DayLocator()
months = MonthLocator()
month_formatter = DateFormatter("%b %Y")
# (1) 创建一个Matplotlib的figure对象
fig = plt.figure()
# (2) 在图像中添加一个子图
ax = fig.add_subplot(111)
# (3) 绘制收盘价数据。
ax.plot(dates, close)
# (4) 对收盘价下方的区域进行着色，依据低于或高于平均收盘价使用不同的颜色填充
plt.fill_between(dates, close.min(), close, where=close>close.mean(), facecolor="green",
alpha=0.4)
plt.fill_between(dates, close.min(), close, where=close<close.mean(),
facecolor="red", alpha=0.4)
ax.xaxis.set_major_locator(months)
ax.xaxis.set_minor_locator(alldays)
ax.xaxis.set_major_formatter(month_formatter)
ax.grid(True)
fig.autofmt_xdate()
plt.show()