#!/usr/bin/python

import  tushare as ts
# 数据存储
'''
    保存为csv格式
    保存为Excel格式
    保存为HDF5文件格式
    保存为JSON格式
    存入MySQL等关系型数据库
    存入NoSQL数据库
'''

# CSV文件

'''
pandas的DataFrame和Series对象提供了直接保存csv文件格式的方法，通过参数设定，轻松将数据内容保存在本地磁盘。

常用参数说明：

    path_or_buf: csv文件存放路径或者StringIO对象
    sep : 文件内容分隔符，默认为,逗号
    na_rep: 在遇到NaN值时保存为某字符，默认为’‘空字符
    float_format: float类型的格式
    columns: 需要保存的列，默认为None
    header: 是否保存columns名，默认为True
    index: 是否保存index，默认为True
    mode : 创建新文件还是追加到现有文件，默认为新建
    encoding: 文件编码格式
    date_format: 日期格式

注：在设定path时，如果目录不存在，程序会提示IOError，请先确保目录已经存在于磁盘中。
'''

#df = ts.get_hist_data('600808',start='2017-01-01',end='2017-12-15')

#df.to_csv('./CSV/600808.csv')

# 选择保存
# df.to_csv('./600808.csv',columns=['open', 'high','low','close'])
import os
paths ='./CSV/'
codes = ['600808','002361','002610']
for code in codes:
    filename = paths+code+'_2017.csv'
    # print(paths+code+'.csv')
    df =ts.get_hist_data(code,start='2017-01-01',end='2017-12-31')
    if os.path.exists(filename):
         df.to_csv(filename,mode='a',header=None)
    else:
         df.to_csv(filename)

# Excel文件
'''
pandas将数据保存为MicroSoft Excel文件格式。

常用参数说明：

    excel_writer: 文件路径或者ExcelWriter对象
    sheet_name:sheet名称，默认为Sheet1
    sep : 文件内容分隔符，默认为,逗号
    na_rep: 在遇到NaN值时保存为某字符，默认为’‘空字符
    float_format: float类型的格式
    columns: 需要保存的列，默认为None
    header: 是否保存columns名，默认为True
    index: 是否保存index，默认为True
    encoding: 文件编码格式
    startrow: 在数据的头部留出startrow行空行
    startcol :在数据的左边留出startcol列空列
'''
'''
df = ts.get_hist_data('600808')
#直接保存
df.to_excel('./EXCEL/600808.xlsx')
#设定数据位置（从第3行，第6列开始插入数据）
df.to_excel('./EXCEL/600808.xlsx',startrow=2,startcol=5)
'''

# JSON文件
'''
pandas生成Json格式的文件或字符串。

常用参数说明：

    path_or_buf: json文件存放路径
    orient:json格式顺序，包括columns，records，index，split，values，默认为columns
    force_ascii: 将字符转ASCII，默认为True

'''
'''
df = ts.get_hist_data('600808')
df.to_json('./JSON/600808',orient= 'records')
print(df.to_json(orient='records'))
'''

# MySQL数据库
'''
pandas提供了将数据便捷存入关系型数据库的方法，在新版的pandas中，主要是已sqlalchemy方式与数据建立连接，支持MySQL、Postgresql、Oracle、MS SQLServer、SQLite等主流数据库。本例以MySQL数据库为代表，展示将获取到的股票数据存入数据库的方法,其他类型数据库请参考sqlalchemy官网文档的create_engine部分。

常用参数说明：

    name:表名，pandas会自动创建表结构
    con：数据库连接，最好是用sqlalchemy创建engine的方式来替代con
    flavor:数据库类型 {‘sqlite’, ‘mysql’}, 默认‘sqlite’，如果是engine此项可忽略
    schema:指定数据库的schema，默认即可
    if_exists:如果表名已存在的处理方式 {‘fail’, ‘replace’, ‘append’},默认‘fail’
    index:将pandas的Index作为一列存入数据库，默认是True
    index_label:Index的列名
    chunksize:分批存入数据库，默认是None，即一次性全部写人数据库
    dtype:设定columns在数据库里的数据类型，默认是None

'''
'''
from sqlalchemy import create_engine

df = ts.get_hist_data('600808', date='2017-12-15')
engine = create_engine('mysql://user:passwd@127.0.0.1/db_name?charset=utf8')

#存入数据库
df.to_sql('tick_data',engine)

#追加数据到现有表
#df.to_sql('tick_data',engine,if_exists='append')
'''