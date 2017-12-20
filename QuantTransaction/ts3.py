#!/usr/bin/python

import tushare as ts

# 基本面数据
'''
基本面类数据提供所有股票的基本面情况，包括股本情况、业绩预告和业绩报告等。主要包括以下类别：
    沪深股票列表
    业绩预告
    业绩报告（主表）
    盈利能力数据
    营运能力数据
    成长能力数据
    偿债能力数据
    现金流量数据
'''

#股票列表
'''
code,代码
name,名称
industry,所属行业
area,地区
pe,市盈率
outstanding,流通股本(亿)
totals,总股本(亿)
totalAssets,总资产(万)
liquidAssets,流动资产
fixedAssets,固定资产
reserved,公积金
reservedPerShare,每股公积金
esp,每股收益
bvps,每股净资
pb,市净率
timeToMarket,上市日期
undp,未分利润
perundp, 每股未分配
rev,收入同比(%)
profit,利润同比(%)
gpr,毛利率(%)
npr,净利润率(%)
holders,股东人数

'''

df = ts.get_stock_basics()
print(df.head(10))

# 业绩报告（主表）
'''
code,代码
name,名称
esp,每股收益
eps_yoy,每股收益同比(%)
bvps,每股净资产
roe,净资产收益率(%)
epcf,每股现金流量(元)
net_profits,净利润(万元)
profits_yoy,净利润同比(%)
distrib,分配方案
report_date,发布日期
'''

ts.get_report_data(2017, 3)

# 营运能力
'''
按年度、季度获取营运能力数据，结果返回的数据属性说明如下：
code,代码
name,名称
arturnover,应收账款周转率(次)
arturndays,应收账款周转天数(天)
inventory_turnover,存货周转率(次)
inventory_days,存货周转天数(天)
currentasset_turnover,流动资产周转率(次)
currentasset_days,流动资产周转天数(天)
'''
ts.get_operation_data(2017, 3)

# 成长能力

'''
code,代码
name,名称
mbrg,主营业务收入增长率(%)
nprg,净利润增长率(%)
nav,净资产增长率
targ,总资产增长率
epsg,每股收益增长率
seg,股东权益增长率
'''
ts.get_growth_data(2017, 3)

# 偿债能力
'''
code,代码
name,名称
currentratio,流动比率
quickratio,速动比率
cashratio,现金比率
icratio,利息支付倍数
sheqratio,股东权益比率
adratio,股东权益增长率
'''

ts.get_debtpaying_data(2017, 3)

# 现金流量
'''
code,代码
name,名称
cf_sales,经营现金净流量对销售收入比率
rateofreturn,资产的经营现金流量回报率
cf_nm,经营现金净流量与净利润的比率
cf_liabilities,经营现金净流量对负债比率
cashflowratio,现金流量比率
'''

ts.get_cashflow_data(2017, 3)