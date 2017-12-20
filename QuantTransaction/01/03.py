#!/usr/bin/python

# -*- coding:utf-8 -*-

import numpy as np
from datetime import  datetime
def datestr_to_num(s):
    return datetime.strptime(s.decode('ascii'), "%Y-%m-%d").date().weekday()


# 读入CSV文件处理数据
# c 表示收盘价,v表示成交量数据

dates,open,high,close,low,volume = np.loadtxt('../CSV/600808_2017.csv',delimiter=',' , skiprows=1,usecols=(0,1,2,3,4,5),converters={0:datestr_to_num},unpack=True)

#print(close,volume)
'''
VWAP （Volume-Weighted Average Price，成交量加权平均价格）是一个非常重要的经济学量，
它代表着金融资产的“平均”价格。某个价格的成交量越高，该价格所占的权重就越大。 VWAP
就是以成交量为权重计算出来的加权平均值，常用于算法交易。
'''
vwap = np.average(close, weights=volume)
print("vwap = ", vwap)
# vwap =  4.25387482732
# 算术平均值函数
print("mean =",np.mean(close))
#mean = 3.89482905983
#时间加权平均价格
'''
建立在真实市场成交量上而不是依赖静态模型而形成交易进度，随后逐渐演化成为采用
更隐藏的路径以达到零市场冲击的最小冲击算法。
时间加权平均价格（TWAP）是一种基于时间变化的加权平均价格，被称为TWAP算法，
其仅以时间分割为基础，考虑指令的设置或指令的执行，而不受市场价格或成交
'''
t = np.arange(len(close))
print('twap = ', np.average(close,weights=t))
# twap =  3.57643703459

# 找到最大值和最小值   每日最高价和最低价
high, low = np.loadtxt('../CSV/600808_2017.csv', delimiter=',',skiprows=1,usecols=(2,4),unpack=True)
hightest = np.max(high)
print('hightest =', hightest)
# hightest = 5.7
lowest = np.min(low)
print('lowest = ', lowest)
# lowest =  2.82
medest = (hightest+lowest)/2
print('madest = ', medest)
# madest =  4.26

'''
NumPy中有一个ptp函数可以计算数组的取值范围。该函数返回的是数组元素的最大值
和最小值之间的差值。也就是说，返回值等于max(array) - min(array)。调用ptp函数：
'''
h = np.ptp(high)
print("Spead high price", h)
#Spead high price 2.83
l = np.ptp(low)
print("Spead low price", l)
#Spead low price 2.47

# 简单统计分析
#(1) 计算收盘价的中位数
median = np.median(close)
print('median = ', median)
# median =  3.585
# 统计量就是方差 方差能够体现变量变化的程度
# 方差是指各个数据与所有数据算术平均数的离差平方和除以数据个数所得到的值
variance = np.var(close)
print('variance =', variance)
# variance = 0.498423261378
vfd = np.mean((close-close.mean()) ** 2)
print('vfd = ', vfd)
# vfd =  0.498423261378

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

returns = np.diff(close) / close[: -1]
# print(returns)
#注意，我们没有用收盘价数组中的最后一个值做除数。接下来，用std函数计算标准差：
deviation = np.std(returns)
print('Standard Deviation =', deviation)
# Standard Deviation = 0.0247844006256

#(2)对数收益率计算起来甚至更简单一些。我们先用log函数得到每一个收盘价的对数，
# 再对结果使用diff函数即可  股价总为正值，
logreturns = np.diff(np.log(close))
print('logreturns = ',logreturns)

'''
(3) 我们很可能对哪些交易日的收益率为正值非常感兴趣。在完成了前面的步骤之后，我们
只需要用where函数就可以做到这一点。 where函数可以根据指定的条件返回所有满足条件的数
组元素的索引值
'''
posretindices = np.where(returns > 0)
print('Indeices with positive returns', posretindices)

# (4) 在投资学中，波动率（volatility）是对价格变动的一种度量历史波动率可以根据历史价格数据计算得出
# 计算历史波动率（如年波动率或月波动率）时，需要用到对数收益率
# 年波动率等于对数收益率的标准差除以其均值 再除以交易日倒数的平方根 通常交易日取252天。我们用std和mean函数来计算
annual_vlatility = np.std(logreturns) / np.mean(logreturns)
year_vlatility = annual_vlatility / np.sqrt(1./252.)
print('year_result= ', year_vlatility)
# year_vlatility=  2200.64810258
#计算月波动率如下
monthly_volatility = annual_vlatility * np.sqrt(1./12.)
print('monthly_volatility = ',monthly_volatility)
# monthly_volatility =  40.0183988414

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
    return datetime.strptime(s.decode('ascii'), '%d-%m-%y').date().weekday()
print('dates = ',dates)
#  我们来创建一个包含5个元素的数组，分别代表一周的5个工作日。数组元素将初始化为0。
averages = np.zeros(5)
# 我们将遍历0到4的日期标识，或者说是遍历星期一到星期五，然后用where函数得到各工作日的索引值并存储在indices数组中。
for i in range(5):
    indices = np.where(dates == i)
    prices = np.take(close,indices)
    avg = np.mean(prices)
    print("Day ", i, "Prices", prices, "Average", avg)
    averages[i] = avg

# 找出哪个工作日的平均收盘价是最高的，哪个是最低的
top = np.max(averages)
print("Hightest average", top)
# Hightest average 3.92659090909
print("Top day of the week", np.argmax(averages))
# Top day of the week 0
bottom = np.min(averages)
print("Lowest average", bottom)
# Lowest average 3.86395833333

print("Bottom day of the week", np.argmin(averages))
# Bottom day of the week 4


 # 动手实践：汇总数据
dec_close = close[:11]
dec_dates = dates[:11]

# get first Monday 找到第一个星期一
first_monday = np.ravel(np.where(dec_dates == 0))[0]
print("The first Monday index is ", first_monday)
# The first Monday index is  4
# get last friday
last_friday= np.ravel(np.where(dec_dates == 4))[-1]
print("This last Friday index is ", last_friday)
#(3) 创建一个数组，用于存储三周内每一天的索引值。
weeks_indices = np.arange(first_monday,last_friday +1)
print("weeks indices after split", weeks_indices)

# (4) 按照每个子数组5个元素，用split函数切分数组：
weeks_indices = np.split(weeks_indices, 7)
print("Weeks indices after split", weeks_indices)
#(5) 在NumPy中，数组的维度也被称作轴  apply_along_axis
# (6) 编写summarize函数。该函数将为每一周的数据返回一个元组，包含这一周的开盘价、最高价、最低价和收盘价，类似于每天的盘后数据。
def summarize(a,o,h,l,c):
    monday_open = o[a[0]]
    week_high = np.max(np.take(h,a))
    week_low = np.min(np.take(l,a))
    firday_close = c[a[-1]]
    return("600808",monday_open,week_high,week_low,firday_close)
weeksumary = np.apply_along_axis(summarize,1,weeks_indices, open, high, low, close)
print("Week summary", weeksumary)

# 真实波动幅度均值
# (1) ATR是基于N个交易日的最高价和最低价进行计算的，通常取最近20个交易日
N = 20
twenty_high = high[:20]
twenty_low = low[:20]
print("len(twenty_high)" , len(twenty_high),"len(twenty_low)", len(twenty_low))
# (2) 我们还需要知道前一个交易日的收盘价。
previousclose = close[-N -1: -1]
'''
对于每一个交易日，计算以下各项。
h – l 当日股价范围，即当日最高价和最低价之差。
h – previousclose 当日最高价和前一个交易日收盘价之差。
previousclose – l 前一个交易日收盘价和当日最低价之差
'''
#(3) max函数返回数组中的最大值。基于上面计算的3个数值，我们来计算所谓的真实波动幅度，也就是这三者的最大值。
print("len(previousclose)",len(previousclose))
truerange = np.maximum(twenty_high-twenty_low,twenty_high-previousclose,previousclose-1)
print("truerange = ", truerange)
# (4) 创建一个长度为N的数组atr，并初始化数组元素为0。

atr = np.zeros(N)
# (5) 这个数组的首个元素就是truerange数组元素的平均值。
atr[0] = np.mean(truerange)
# PATR表示前一个交易日的ATR值， ATR即当日的真实波动幅度。
for i in range(1, N):
    atr[i] = (N - 1) * atr[i -1] + truerange[i]
    atr[i] /= N
print("ATR = ", atr)
'''
生成了3个数组，分别表示3种范围——当日股价范围，当日最高价和前一个交易日收盘
价之差，以及前一个交易日收盘价和当日最低价之差
'''