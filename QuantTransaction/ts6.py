#!/usr/bin/python
import tushare as ts

# 龙虎榜数据
'''
龙虎榜数据接口提供历史龙虎榜上榜股票数据，主要包括以下类别：

    每日龙虎榜列表
    个股上榜统计
    营业部上榜统计
    龙虎榜机构席位追踪
    龙虎榜机构席位成交明细
'''
# 每日龙虎榜列表
'''
按日期获取历史当日上榜的个股数据，如果一个股票有多个上榜原因，则会出现该股票多条数据。

参数说明：

    date：日期，格式YYYY-MM-DD
    retry_count：当网络异常后重试次数，默认为3
    pause:重试时停顿秒数，默认为0

返回值说明：

    code：代码
    name:名称
    pchange:当日涨跌幅
    amount：龙虎榜成交额(万)
    buy：买入额(万)
    bratio：买入占总成交比例
    sell：卖出额(万)
    sratio：卖出占总成交比例
    reason：上榜原因
    date：日期

'''
df = ts.top_list('2017-12-15')
print(df.head(10))

# 个股上榜统计
'''
获取近5、10、30、60日个股上榜统计数据,包括上榜次数、累积购买额、累积卖出额、净额、买入席位数和卖出席位数。

参数说明：

    days：统计周期5、10、30和60日，默认为5日
    retry_count：当网络异常后重试次数，默认为3
    pause:重试时停顿秒数，默认为0

返回值说明：

    code：代码
    name:名称
    count：上榜次数
    bamount：累积购买额(万)
    samount：累积卖出额(万)
    net：净额(万)
    bcount：买入席位数
    scount：卖出席位数

'''

df = ts.cap_tops()

# 营业部上榜统计
'''
获取营业部近5、10、30、60日上榜次数、累积买卖等情况。

参数说明：

    days：统计周期5、10、30和60日，默认为5日
    retry_count：当网络异常后重试次数，默认为3
    pause:重试时停顿秒数，默认为0

返回值说明：

    broker：营业部名称
    count：上榜次数
    bamount：累积购买额(万)
    bcount：买入席位数
    samount：累积卖出额(万)
    scount：卖出席位数
    top3：买入前三股票
'''
ts.broker_tops()
# 机构席位追踪
'''
获取机构近5、10、30、60日累积买卖次数和金额等情况。

参数说明：

    days：统计周期5、10、30和60日，默认为5日
    retry_count：当网络异常后重试次数，默认为3
    pause:重试时停顿秒数，默认为0

返回值说明：

    code:代码
    name:名称
    bamount:累积买入额(万)
    bcount:买入次数
    samount:累积卖出额(万)
    scount:卖出次数
    net:净额(万)

'''
ts.inst_tops()

# 机构成交明细
'''
获取最近一个交易日机构席位成交明细统计数据

参数说明：

    retry_count：当网络异常后重试次数，默认为3
    pause:重试时停顿秒数，默认为0

返回值说明：

    code:代码
    name:名称
    date:交易日期
    bamount:机构席位买入额(万)
    samount:机构席位卖出额(万)
    type:类型

'''

df = ts.inst_detail()