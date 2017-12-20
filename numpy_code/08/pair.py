from matplotlib.finance import quotes_historical_yahoo_ohlc
from datetime import date
import numpy as np
from scipy import stats
from statsmodels.stats.stattools import jarque_bera
import matplotlib.pyplot as plt
def get_close(symbol):
    today = date.today()
    start = (today.year - 1, today.month, today.day)
    quotes = quotes_historical_yahoo_ohlc(symbol, start, today)
    quotes = np.array(quotes)
    return quotes.T[4]
#(2) 计算DIA和SPY的对数收益率。先对收盘价取自然对数，然后计算连续值之间的差值，即得到对数收益率。
spy = np.diff(np.log(get_close("SPY")))
dia = np.diff(np.log(get_close("DIA")))
#(3) 均值检验可以检查两组不同的样本是否有相同的均值。返回值有两个，其中第二个为p-value，取值范围为0~1。
print ("Means comparison", stats.ttest_ind(spy, dia))
# (4) Kolmogorov-Smirnov检验可以判断两组样本同分布的可能性
print ("Kolmogorov smirnov test", stats.ks_2samp(spy, dia))
# (5) 在两只股票对数收益率的差值上应用Jarque-Bera正态性检验。
print ("Jarque Bera test", jarque_bera(spy - dia)[1])
# (6) 使用Matplotlib绘制对数收益率以及其差值的直方图。
plt.hist(spy, histtype="step", lw=1, label="SPY")
plt.hist(dia, histtype="step", lw=2, label="DIA")
plt.hist(spy - dia, histtype="step", lw=3, label="Delta")
plt.legend()
plt.show()