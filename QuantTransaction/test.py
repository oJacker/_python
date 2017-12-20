#!/usr/bin/python

from __future__ import print_function

import tushare as ts

# print(ts.__version__)

data= ts.get_hist_data('600808',start='2015-01-01',end='2017-12-18')
#print(data)
'''
ts.get_hist_data('600808', ktype='W') #获取周k线数据
ts.get_hist_data('600808', ktype='M') #获取月k线数据
ts.get_hist_data('600808', ktype='5') #获取5分钟k线数据
ts.get_hist_data('600808', ktype='15') #获取15分钟k线数据
ts.get_hist_data('600808', ktype='30') #获取30分钟k线数据
ts.get_hist_data('600808', ktype='60') #获取60分钟k线数据
ts.get_hist_data('sh')#获取上证指数k线数据，其它参数与个股一致，下同
ts.get_hist_data('sz')#获取深圳成指k线数据
ts.get_hist_data('hs300')#获取沪深300指数k线数据
ts.get_hist_data('sz50')#获取上证50指数k线数据
ts.get_hist_data('zxb')#获取中小板指数k线数据
ts.get_hist_data('cyb')#获取创业板指数k线数据
'''
df = ts.get_tick_data('600808',date='2017-12-15')
# print(df.head(10))

'''
0：name，股票名字
1：open，今日开盘价
2：pre_close，昨日收盘价
3：price，当前价格
4：high，今日最高价
5：low，今日最低价
6：bid，竞买价，即“买一”报价
7：ask，竞卖价，即“卖一”报价
8：volume，成交量 maybe you need do volume/100
9：amount，成交金额（元 CNY）
10：b1_v，委买一（笔数 bid volume）
11：b1_p，委买一（价格 bid price）
12：b2_v，“买二”
13：b2_p，“买二”
14：b3_v，“买三”
15：b3_p，“买三”
16：b4_v，“买四”
17：b4_p，“买四”
18：b5_v，“买五”
19：b5_p，“买五”
20：a1_v，委卖一（笔数 ask volume）
21：a1_p，委卖一（价格 ask price）
...
30：date，日期；
31：time，时间；
'''
df =ts.get_realtime_quotes('600808') # single stock symbol
print(df[['code','name','price','bid','ask','volume','amount','date','time']])

'''
    参数说明
    code：股票代码，即6位数字代码
    retry_count : int, 默认3,如遇网络等问题重复执行的次数
    pause : int, 默认 0,重复请求数据过程中暂停的秒数，防止请求间隔时间太短出现的问题
    返回值说明：
    time：时间
    price：当前价格
    pchange:涨跌幅
    change：价格变动
    volume：成交手
    amount：成交金额(元)
    type：买卖类型【买盘、卖盘、中性盘】

'''
df =ts.get_today_ticks('600808')
print(df.head(10))

# 大盘指数行情列表
'''

    code:指数代码
    name:指数名称
    change:涨跌幅
    open:开盘点位
    preclose:昨日收盘点位
    close:收盘点位
    high:最高点位
    low:最低点位
    volume:成交量(手)
    amount:成交金额（亿元）

'''
df = ts.get_index()
print(df.head(10))


# 大单交易数据
'''
参数说明：

    code：股票代码，即6位数字代码
    date:日期，格式YYYY-MM-DD
    vol:手数，默认为400手，输入数值型参数
    retry_count : int, 默认3,如遇网络等问题重复执行的次数
    pause : int, 默认 0,重复请求数据过程中暂停的秒数，防止请求间隔时间太短出现的问题

返回值说明：

    code：代码
    name：名称
    time：时间
    price：当前价格
    volume：成交手
    preprice ：上一笔价格
    type：买卖类型【买盘、卖盘、中性盘】

'''

df = ts.get_sina_dd('600808',date='2017-12-08')  #默认400手