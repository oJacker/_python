# -*- coding:utf-8 -*-
import  numpy as np

# 保存txt文件
i2 = np.eye(2)
# print(2)
np.savetxt("eye.txt",i2)

# 读入CSV文件处理数据
# c 表示收盘价,v表示成交量数据
c,v = np.loadtxt('data.csv', delimiter=',', usecols=(6,7),unpack=True)
# print(c,v)
# 336.1 21144800.0
'''
VWAP （Volume-Weighted Average Price，成交量加权平均价格）是一个非常重要的经济学量，
它代表着金融资产的“平均”价格。某个价格的成交量越高，该价格所占的权重就越大。 VWAP
就是以成交量为权重计算出来的加权平均值，常用于算法交易。
'''
vwap = np.average(c, weights=v)
# print("vwap = ", vwap)
# vwap =  350.589549353
#算术平均值函数
# print ("mean =", np.mean(c))
# mean = 351.037666667
#时间加权平均价格
t = np.arange(len(c))
# print("twap = " , np.average(c, weights=t))
# twap =  352.428321839
# 找到最大值和最小值
#每日最高价和最低价
h,l = np.loadtxt('data.csv',delimiter=',',usecols=(4,5),unpack= True)
#print("hightest =", np.max(h))
# hightest = 364.9
#print("lowest =", np.min((l)))
#lowest = 333.53
# print((np.max(h)+np.min(l)) /2 )
# 349.215
'''
NumPy中有一个ptp函数可以计算数组的取值范围。该函数返回的是数组元素的最大值
和最小值之间的差值。也就是说，返回值等于max(array) - min(array)。调用ptp函数：
'''
# print("Spead high price", np.ptp(h))
high=np.ptp(h)
low = np.ptp(l)
# print("Spead low price", np.ptp(l))
# Spead high price 24.86
# Spead low price 26.97

# 简单统计分析
#(1) 计算收盘价的中位数
c = np.loadtxt('data.csv', delimiter=',', usecols=(6,), unpack= True)
# print("median = ", np.median(c))
#median =  352.055

#  既然这是我们首次使用median函数，我们来检查一下结果是否正确。
sorted_close = np.msort(c)
#print("sorted = ", sorted_close)
'''
sorted =  [ 336.1   338.61  339.32  342.62  342.88  343.44  344.32  345.03  346.5
  346.67  348.16  349.31  350.56  351.88  351.99  352.12  352.47  353.21
  354.54  355.2   355.36  355.76  356.85  358.16  358.3   359.18  359.56
  359.9   360.    363.13]
'''
N = len(c)

print("middle =", sorted_close[int((N-1)/2)])
#middle = 351.99
print("average middle =",(sorted_close[int((N-1)/2)] + sorted_close[int((N)/2)])/2)
#average middle = 352.055

# 统计量就是方差 方差能够体现变量变化的程度  方差是指各个数据与所有数据算术平均数的离差平方和除以数据个数所得到的值

#print("variance =", np.var(c))
#variance = 50.1265178889

print("variance from definition =", np.mean((c-c.mean()) ** 2))
# variance from definition = 50.1265178889

'''
收盘价的分析常常是基于股票收益率和对数收益率的。简单收益率是指相邻
两个价格之间的变化率，而对数收益率是指所有价格取对数后两两之间的差值
“ a”的对数减去“ b”的对数就等于“ a除以b”的对数。因此，对数收益率也可
以用来衡量价格的变化率。
投资者最感兴趣的是收益率的方差或标准差，因为
这代表着投资风险的大小
'''

# 分析股票收益率
# (1) 首先，我们来计算简单收益率
'''
NumPy中的diff函数可以返回一个由相邻数组元素的差
值构成的数组。这有点类似于微积分中的微分。为了计算收益率，我们还需要用差值除以前一天
的价格。
'''
returns = np.diff(c) / c[: -1]
#注意，我们没有用收盘价数组中的最后一个值做除数。接下来，用std函数计算标准差：
deviation = np.std(returns)
#print("Standard deviation =", np.std(returns))
#  Standard deviation = 0.0129221344368
# (2) 对数收益率计算起来甚至更简单一些。我们先用log函数得到每一个收盘价的对数，再对结果使用diff函数即可  股价总为正值，
logreturns = np.diff(np.log(c))

'''
(3) 我们很可能对哪些交易日的收益率为正值非常感兴趣。在完成了前面的步骤之后，我们
只需要用where函数就可以做到这一点。 where函数可以根据指定的条件返回所有满足条件的数
组元素的索引值
'''
posretindices =np.where(returns > 0)
#print("Indeices with positive returns", posretindices)

# (4) 在投资学中，波动率（volatility）是对价格变动的一种度量
# 历史波动率可以根据历史价格数据计算得出  计算历史波动率（如年波动率或月波动率）时，需要用到对数收益率
# 年波动率等于对数收益率的标准差除以其均值 再除以交易日倒数的平方根 通常交易日取252天。我们用std和mean函数来计算
annual_vlatility = np.std(logreturns)/np.mean(logreturns)
annual_vlatility = annual_vlatility / np.sqrt(1./252.)
#print(annual_vlatility)
#年波动率 129.274789911
#计算月波动率如下
monthly_volatility = annual_vlatility * np.sqrt(1./12.)
#print("monthly_volatility = ", monthly_volatility)
#计算月波动率如下  monthly_volatility =  37.3184173773

# 分析日期数据   收盘价 ，日期
# 星期一 0
# 星期二 1
# 星期三 2
# 星期四 3
# 星期五 4
# 星期六 5
# 星期日 6
#日期转换：在处理日期世需要用到参数converters,它是本数据和转换函数之间进行映射的字典 0到6的整数， 0代表星期一， 6代表星期天
from datetime import  datetime
def datestr_to_num(s):
    return datetime.strptime(s.decode('ascii'), "%d-%m-%Y").date().weekday()
dates, close=np.loadtxt('data.csv', delimiter=',', usecols=(1,6), converters={1: datestr_to_num}, unpack=True)
print(dates)

#  我们来创建一个包含5个元素的数组，分别代表一周的5个工作日。数组元素将初始化为0。
averages = np.zeros(5)
#我们将遍历0到4的日期标识，或者说是遍历星期一到星期五，然后用where函数得到各工作日的索引值并存储在indices数组中。

for i in range(5):
    indices = np.where(dates == i)
    prices =np.take(close,indices)
    avg = np.mean(prices)
    print("Day", i, "prices",prices,"Average",avg)
    averages[i]= avg

# 找出哪个工作日的平均收盘价是最高的，哪个是最低的
top = np.max(averages)
print("Highest average", top)
print("Top day of the week", np.argmax(averages))
bottom = np.min(averages)
print("Lowest average", bottom)
print("Bottom day of the week", np.argmin(averages))
'''
Highest average 352.136666667
Top day of the week 2
Lowest average 350.022857143
Bottom day of the week 4
'''

# 动手实践：汇总数据


dates, open, high, low, close = np.loadtxt('data.csv', delimiter=',',usecols=(1,3,4,5,6),converters={1:datestr_to_num},unpack= True)
close = close[:16]
dates = dates[:16]

# get first Monday
first_monday = np.ravel(np.where(dates == 0))[0]
print("The first Monday index is ", first_monday)
# The first Monday index is  1
# 找到最后一个星期五
#print(np.where(dates == 0))
#print(np.where(dates == 4))
# get last Friday
last_friday = np.ravel(np.where(dates == 4))[-1]
print("The last Friday index is ", last_friday)
#(3) 创建一个数组，用于存储三周内每一天的索引值。
weeks_indices = np.arange(first_monday, last_friday + 1)
print("weeks indices after split", weeks_indices)
# weeks indices after split [ 1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24]

# (4) 按照每个子数组5个元素，用split函数切分数组：
weeks_indices = np.split(weeks_indices, 3)
print("Weeks indices after split", weeks_indices)

#(5) 在NumPy中，数组的维度也被称作轴  apply_along_axis

# (6) 编写summarize函数。该函数将为每一周的数据返回一个元组，包含这一周的开盘价、最高价、最低价和收盘价，类似于每天的盘后数据。
def summarize(a, o, h, l, c):
    monday_open = o[a[0]]
    week_high = np.max(np.take(h, a))
    week_low = np.min(np.take(l,a))
    firday_close = c[a[-1]]
    return("APPL", monday_open, week_high,week_low,firday_close)
weeksumary = np.apply_along_axis(summarize, 1, weeks_indices, open, high, low, close)
print("Week summary", weeksumary)

# 使用NumPy中的savetxt函数，将数据保存至文件。
np.savetxt("weeksumary.csv", weeksumary, delimiter=",", fmt="%s")

# 真实波动幅度均值
h, l, c =np.loadtxt('data.csv', delimiter=',',usecols=(4,5,6),unpack=True)

# (1) ATR是基于N个交易日的最高价和最低价进行计算的，通常取最近20个交易日
N = 20
h = h[-N:]
l = l[-N:]
print("len(h)", len(h), "len(l)", len(l))
print("Close:", c)
# (2) 我们还需要知道前一个交易日的收盘价。
previousclose = c [-N -1: -1]
'''
对于每一个交易日，计算以下各项。
h – l 当日股价范围，即当日最高价和最低价之差。
h – previousclose 当日最高价和前一个交易日收盘价之差。
previousclose – l 前一个交易日收盘价和当日最低价之差
'''
#(3) max函数返回数组中的最大值。基于上面计算的3个数值，我们来计算所谓的真实波动幅度，也就是这三者的最大值。
print ("len(previousclose)", len(previousclose))
print ("Previous close", previousclose)
truerange = np.maximum(h - l, h - previousclose, previousclose - l)
# (4) 创建一个长度为N的数组atr，并初始化数组元素为0。
atr = np.zeros(N)
# (5) 这个数组的首个元素就是truerange数组元素的平均值。
atr[0] = np.mean(truerange)
# PATR表示前一个交易日的ATR值， TR即当日的真实波动幅度。

for i in range(1, N):
    atr[i] = (N - 1) * atr[i -1] + truerange[i]
    atr[i] /= N

print("ATR", atr)
'''
生成了3个数组，分别表示3种范围——当日股价范围，当日最高价和前一个交易日收盘
价之差，以及前一个交易日收盘价和当日最低价之差
'''







