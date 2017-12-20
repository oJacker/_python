#!/usr/bin/python

import tushare as ts
'''
股票分类数据
分类数据提供股票的分类信息数据，从股票类型的不同角度进行数据分类，在一些统计套利方法的应用中，时常会以股票的分类来做切入，比如对某些行业或概念进行阶段统计来决定近期的交易策略等。TuShare提供的分类数据主要包括以下类别：
    行业分类
    概念分类
    地域分类
    中小板分类
    创业板分类
    风险警示板分类
    沪深300成份股及权重
    上证50成份股
    中证500成份股
    终止上市股票列表
    暂停上市股票列表
'''
ts.get_industry_classified()
# 概念分类
'''
返回股票概念的分类数据，现实的二级市场交易中，经常会以”概念”来炒作，在数据分析过程中，可根据概念分类监测资金等信息的变动情况。本接口是一次性在线获取数据，调用接口时会有一定的延时，请在数据返回后自行将数据进行及时存储。sina财经提供的概念分类信息大致
返回值说明：

    code：股票代码
    name：股票名称
    c_name：概念名称

'''
ts.get_concept_classified()

# 地域分类
'''
参数说明：

    file_path:文件路径，默认为None即由TuShare提供，可以设定自己的股票文件路径。

返回值说明：

    code：股票代码
    name：股票名称
    area：地域名称

'''
ts.get_area_classified()

#中小板分类
'''
参数说明：

    file_path:文件路径，默认为None即由TuShare提供，可以设定自己的股票文件路径。

返回值说明：

    code：股票代码
    name：股票名称

'''
ts.get_sme_classified()

# 创业板分类
'''
参数说明：

    file_path:文件路径，默认为None即由TuShare提供，可以设定自己的股票文件路径。

返回值说明：

    code：股票代码
    name：股票名称

'''
ts.get_gem_classified()

# 风险警示板分类
'''
参数说明：

    file_path:文件路径，默认为None即由TuShare提供，可以设定自己的股票文件路径。

返回值说明：

    code：股票代码
    name：股票名称

'''
ts.get_st_classified()
# 沪深300成份及权重
'''
返回值说明：

    code :股票代码
    name :股票名称
    date :日期
    weight:权重

'''
ts.get_hs300s()

# 上证50成份股
'''
返回值说明：

    code：股票代码
    name：股票名称

'''
ts.get_sz50s()
# 中证500成份股
'''
返回值说明：

    code：股票代码
    name：股票名称

'''
ts.get_zz500s()

# 终止上市股票列表
'''
获取已经被终止上市的股票列表，数据从上交所获取，目前只有在上海证券交易所交易被终止的股票。

返回值说明：

    code：股票代码
    name：股票名称
    oDate:上市日期
    tDate:终止上市日期

'''
ts.get_terminated()

# 暂停上市股票列表

'''

    code：股票代码
    name：股票名称
    oDate:上市日期
    tDate:暂停上市日期

'''
ts.get_suspended()


