import  numpy as np
import  datetime

def datestra2num(s):
    return  datetime.datetime.strptime(s.decode('ascii'), "%d-%m-%Y").toordinal()

dates, closes = np.loadtxt('data.csv', delimiter=',' , usecols=(1, 6), converters={1: datestra2num}, unpack=True)
#(2) 使用lexsort函数排序。数据本身已经按照日期排序，不过我们现在优先按照收盘价排序：
indices = np.lexsort((dates, closes))
print("Indeices", indices)

print(["%s %s" % (datetime.date.fromordinal(int(dates[i])),closes[i]) for i in indices])