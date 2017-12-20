#!/usr/bin/python

from __future__ import print_function

import tushare as ts

# 投资参考数据
"""

    分配预案
    业绩预告
    限售股解禁
    基金持股
    新股上市
    融资融券（沪市）
    融资融券（深市）

"""
#分配预案
'''
参数说明：

    year : 预案公布的年份，默认为2014
    top :取最新n条数据，默认取最近公布的25条
    retry_count：当网络异常后重试次数，默认为3
    pause:重试时停顿秒数，默认为0

返回值说明：

    code:股票代码
    name:股票名称
    year:分配年份
    report_date:公布日期
    divi:分红金额（每10股）
    shares:转增和送股数（每10股）
'''

#df = ts.profit_data(top=60)
#df.sort('shares', ascending=False)
# 选择每10股送转在10以上的：  print df[df.shares>=10]

# 业绩报告
'''
参数说明：

    year:int 年度 e.g:2014
    quarter:int 季度 :1、2、3、4，只能输入这4个季度
结果返回的数据属性说明如下：

code,代码
name,名称
type,业绩变动类型【预增、预亏等】
report_date,发布日期
pre_eps,上年同期每股收益
range,业绩变动范围
'''
df= ts.forecast_data(2017,3)
print(df)

# 限售股解禁
'''
参数说明：

    year:年份,默认为当前年
    month:解禁月份，默认为当前月
    retry_count：当网络异常后重试次数，默认为3
    pause:重试时停顿秒数，默认为0

返回值说明：

    code：股票代码
    name：股票名称
    date:解禁日期
    count:解禁数量（万股）
    ratio:占总盘比率
'''
ts.xsg_data()

# 基金持股
'''
参数说明：

    year:年份,默认为当前年
    quarter:季度（只能输入1，2，3，4这个四个数字）
    retry_count：当网络异常后重试次数，默认为3
    pause:重试时停顿秒数，默认为0

返回值说明：

    code：股票代码
    name：股票名称
    date:报告日期
    nums:基金家数
    nlast:与上期相比（增加或减少了）
    count:基金持股数（万股）
    clast:与上期相比
    amount:基金持股市值
    ratio:占流通盘比率

'''

ts.fund_holdings(2017,3)
#新股数据
'''
 参数说明：

    retry_count：当网络异常后重试次数，默认为3
    pause:重试时停顿秒数，默认为0

返回值说明：

    code：股票代码
    name：股票名称
    ipo_date:上网发行日期
    issue_date:上市日期
    amount:发行数量(万股)
    markets:上网发行数量(万股)
    price:发行价格(元)
    pe:发行市盈率
    limit:个人申购上限(万股)
    funds：募集资金(亿元)
    ballot:网上中签率(%)

'''

ts.new_stocks()

# 融资融券（沪市）
'''

    本日融资融券余额＝本日融资余额＋本日融券余量金额
    本日融资余额＝前日融资余额＋本日融资买入额－本日融资偿还额；
    本日融资偿还额＝本日直接还款额＋本日卖券还款额＋本日融资强制平仓额＋本日融资正权益调整－本日融资负权益调整；
    本日融券余量=前日融券余量+本日融券卖出数量-本日融券偿还量；
    本日融券偿还量＝本日买券还券量＋本日直接还券量＋本日融券强制平仓量＋本日融券正权益调整－本日融券负权益调整－本日余券应划转量；
    融券单位：股（标的证券为股票）/份（标的证券为基金）/手（标的证券为债券）。
    明细信息中仅包含当前融资融券标的证券的相关数据，汇总信息中包含被调出标的证券范围的证券的余额余量相关数据。

    参数说明：

    start:开始日期 format：YYYY-MM-DD 为空时取去年今日
    end:结束日期 format：YYYY-MM-DD 为空时取当前日期
    retry_count：当网络异常后重试次数，默认为3
    pause:重试时停顿秒数，默认为0

返回值说明：

    opDate:信用交易日期
    rzye:本日融资余额(元)
    rzmre: 本日融资买入额(元)
    rqyl: 本日融券余量
    rqylje: 本日融券余量金额(元)
    rqmcl: 本日融券卖出量
    rzrqjyzl:本日融资融券余额(元)

'''

ts.sh_margins(start='2017-01-01', end='2017-12-15')
'''
沪市融资融券明细数据

参数说明：

    date:日期 format：YYYY-MM-DD 默认为空’‘,数据返回最近交易日明细数据
    symbol：标的代码，6位数字e.g.600848，默认为空’‘
    start:开始日期 format：YYYY-MM-DD 默认为空’‘
    end:结束日期 format：YYYY-MM-DD 默认为空’‘
    retry_count：当网络异常后重试次数，默认为3
    pause:重试时停顿秒数，默认为0

返回值说明：

    opDate:信用交易日期
    stockCode:标的证券代码
    securityAbbr:标的证券简称
    rzye:本日融资余额(元)
    rzmre: 本日融资买入额(元)
    rzche:本日融资偿还额(元)
    rqyl: 本日融券余量
    rqmcl: 本日融券卖出量
    rqchl: 本日融券偿还量

'''
ts.sh_margin_details(start='2015-01-01', end='2015-04-19', symbol='601989')

# 融资融券（深市）
'''
本日融资余额(元)=前日融资余额＋本日融资买入-本日融资偿还额
本日融券余量(股)=前日融券余量＋本日融券卖出量-本日融券买入量-本日现券偿还量
本日融券余额(元)=本日融券余量×本日收盘价
本日融资融券余额(元)=本日融资余额＋本日融券余额；

深市融资融券汇总数据

参数说明：

    start:开始日期 format：YYYY-MM-DD 为空时取去年今日
    end:结束日期 format：YYYY-MM-DD 为空时取当前日期
    retry_count：当网络异常后重试次数，默认为3
    pause:重试时停顿秒数，默认为0

返回值说明：

    opDate:信用交易日期(index)
    rzmre: 融资买入额(元)
    rzye:融资余额(元)
    rqmcl: 融券卖出量
    rqyl: 融券余量
    rqye: 融券余量(元)
    rzrqye:融资融券余额(元)

'''
ts.sz_margins(start='2015-01-01', end='2015-04-19')
'''
深市融资融券明细数据

参数说明：

    date:日期 format：YYYY-MM-DD 默认为空’‘,数据返回最近交易日明细数据
    retry_count：当网络异常后重试次数，默认为3
    pause:重试时停顿秒数，默认为0

返回值说明：

    stockCode:标的证券代码
    securityAbbr:标的证券简称
    rzmre: 融资买入额(元)
    rzye:融资余额(元)
    rqmcl: 融券卖出量
    rqyl: 融券余量
    rqye: 融券余量(元)
    rzrqye:融资融券余额(元)
    opDate:信用交易日期

'''
ts.sz_margin_details('2015-04-20')