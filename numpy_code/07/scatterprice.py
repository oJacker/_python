from matplotlib.finance import quotes_historical_yahoo_ohlc
import sys
from datetime import date
import matplotlib.pyplot as plt
import numpy as np
#(1) 得到的quotes数据存储在Python列表中。将其转化为NumPy数组并提取出收盘价和成交
#量数据。
today = date.today()
start = (today.year - 1, today.month, today.day)
symbol = 'DISH'
if len(sys.argv) == 2:
    symbol = sys.argv[1]
quotes = quotes_historical_yahoo_ohlc(symbol, start, today)
quotes = np.array(quotes)
close = quotes.T[4]
volume = quotes.T[5]
# (2) 计算股票收益率和成交量的变化值
ret = np.diff(close)/close[:-1]
volchange = np.diff(volume)/volume[:-1]
# (3) 创建一个Matplotlib的figure对象。
fig = plt.figure()
# (4) 在图像中添加一个子图。
ax = fig.add_subplot(111)
# (5) 创建散点图，并使得数据点的颜色与股票收益率相关联，数据点的大小与成交量的变化相关联。
ax.scatter(ret, volchange, c=ret * 100, s=volchange * 100, alpha=0.5)
# (6) 设置图像的标题并添加网格线。
ax.set_title('Close and volume returns')
ax.grid(True)
plt.show()