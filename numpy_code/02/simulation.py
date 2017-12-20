import  numpy as np
import  sys
o,h,l,c = np.loadtxt('data.csv', delimiter=',', usecols=(3,4,5,6), unpack=True)

'''
(4) calc_profit函数非常简单。首先，我们尝试以比开盘价稍低一点的价格买入股票。如果
这个价格不在当日的股价范围内，则尝试买入失败，没有获利，也没有亏损，我们均返回0。否则，
我们将以当日收盘价卖出，所获得的利润即买入和卖出的差价。事实上，计算相对利润更为直观：
'''
def calc_profit(open,high, low, close):
    # 在开盘时买入
    buy = open *float(sys.argv[1])
    # 当日股价区间
    if low < buy < high:
        return (close - buy)/buy
    else:
        return 0
# (3) 我们现在可以先把func当做函数来使用。对股价数组使用我们得到的func函数:
func = np.vectorize(calc_profit)
#(2) NumPy中的vectorize函数相当于Python中的map函数。调用vectorize函数并给定calc_profit函数作为参数
profits = func(o,h,l,c)
print("Profits", profits)
#(5) 在所有交易日中有两个零利润日，即没有利润也没有损失。我们选择非零利润的交易日并计算平均值：
real_trades = profits[profits !=0]
print("Number of trades", len(real_trades), round(100.0 * len(real_trades)/len(c),2), "%")
print("Average profit/loss %", round(np.mean(real_trades) * 100, 2))
#(6) 乐观的人们对于正盈利的交易更感兴趣。选择正盈利的交易日并计算平均利润：
winning_trades =profits[profits>0]
print("Number of winning trades", len(winning_trades),round(100.0 * len(winning_trades)/len(c), 2), "%")
print("Average profit %", round(np.mean(winning_trades) * 100, 2))
# (7) 悲观的人们对于负盈利的交易更感兴趣，选择负盈利的交易日并计算平均损失：
losing_trades =profits[profits<0]
print("Number of winning trades", len(losing_trades),round(100.0 * len(losing_trades)/len(c), 2), "%")
print("Average profit %", round(np.mean(losing_trades) * 100, 2))
'''
尽管平均利润为正值，但我们仍需要了解这段过程中是否有长期连续亏损的状况出现。这
一点很重要，因为如果出现了连续亏损，我们可能会面临资本耗尽的情形，那么计算出来的平
均利润就不可信了。
请检查是否出现过这样的连续亏损。如果你乐意，也可以检查是否有长时间的连续盈利。
'''