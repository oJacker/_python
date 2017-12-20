'''
检测 QQQ 股价的线性趋势
'''
from matplotlib.finance import quotes_historical_yahoo_ohlc
from datetime import date
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter
from matplotlib.dates import DayLocator
from matplotlib.dates import MonthLocator
# (1) 编写代码获取QQQ的收盘价和对应的日期数据。
today = date.today()
start = (today.year - 1, today.month, today.day)
quotes = quotes_historical_yahoo_ohlc("QQQ", start, today)
quotes = np.array(quotes)
dates = quotes.T[0]
qqq = quotes.T[4]
# (2) 去除信号中的线性趋势
y = signal.detrend(qqq)
# (3) 创建月定位器和日定位器
alldays = DayLocator()
months = MonthLocator()
# (4) 创建一个日期格式化器以格式化x轴上的日期。该格式化器将创建一个字符串，包含简写的月份和年份。
month_formatter = DateFormatter("%b %Y")
# (5) 创建图像和子图。
fig = plt.figure()
ax = fig.add_subplot(111)
plt.plot(dates, qqq, 'o', dates, qqq - y, '-')
# (7) 设置定位器和格式化器。
ax.xaxis.set_minor_locator(alldays)
ax.xaxis.set_major_locator(months)
ax.xaxis.set_major_formatter(month_formatter)
# (8) 将x轴上的标签格式化为日期。
fig.autofmt_xdate()
plt.show()