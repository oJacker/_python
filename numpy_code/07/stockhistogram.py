from matplotlib.finance import quotes_historical_yahoo_ohlc
import sys
from datetime import date
import matplotlib.pyplot as plt
import numpy as np
# (1) 下载一年以来的数据：
today = date.today()
start = (today.year - 1, today.month, today.day)
symbol = 'DISH'
if len(sys.argv) == 2:
    symbol = sys.argv[1]
quotes = quotes_historical_yahoo_ohlc(symbol, start, today)
# (2) 上一步得到的股价数据存储在Python列表中。将其转化为NumPy数组并提取出收盘价数据：
quotes = np.array(quotes)
close = quotes.T[4]
# (3) 指定合理数量的柱形，绘制分布直方图：
plt.hist(close, np.sqrt(len(close)))
plt.show()