#!/usr/bin/python

import tushare as ts

# 新闻事件数据
'''
新闻事件接口主要提供国内财经、证券、港股和期货方面的滚动新闻，以及个股的信息地雷数据。目前主要包括以下类别：

    即时财经新闻
    个股信息地雷
    新浪股吧新闻

'''

# 即时新闻
'''
获取即时财经新闻，类型包括国内财经、证券、外汇、期货、港股和美股等新闻信息。数据更新较快，使用过程中可用定时任务来获取。

参数说明：

    top:int，显示最新消息的条数，默认为80条
    show_content:boolean,是否显示新闻内容，默认False

返回值说明：

    classify :新闻类别
    title :新闻标题
    time :发布时间
    url :新闻链接
    content:新闻内容（在show_content为True的情况下出现）
如果需要单独获取新闻内容，可以调用latest_content(url)方法，将上一步获取到的新闻链接传递进来。
'''

# df = ts.get_latest_news() #默认获取最近80条新闻数据，只提供新闻类型、链接和标题

df = ts.get_latest_news(top=5, show_content= True)
print(df)

# 信息地雷
'''
获取个股信息地雷数据。
参数说明：
    code:股票代码
    date:信息公布日期

返回值说明：

    title:信息标题
    type:信息类型
    date:公告日期
    url:信息内容URL
    如果获取信息内容，请调用notice_content(url)接口，把url地址作为参数传入即可。
     
'''
df= ts.get_notices('600808','2017-12-01')
print(df)

# 新浪股吧
'''
获取sina财经股吧首页的重点消息。股吧数据目前获取大概17条重点数据，可根据参数设置是否显示消息内容，默认情况是不显示。

参数说明：

    show_content:boolean,是否显示内容，默认False

返回值说明：

    title, 消息标题
    content, 消息内容（show_content=True的情况下）
    ptime, 发布时间
    rcounts,阅读次数
调用方法：
'''
ts.guba_sina()

df = ts.guba_sina(True)
print(df.ix[3]['content'])