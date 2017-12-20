1:获取泸深300指数每日数据

date open hight close low volume amount

date设置成索引

包括：MSA,BBANDS,MACD,RSI,CCI,ROC,MOM,OBV,WCL,ATR

2:计算课件提到的价格变换特征
import pandas as pd
comm_data =pd.DataFrame(index=daily_data.index)
comm_data.head()

for c in ['open','high','low','volume']:
    for p in [1,2,3]:
        comm_data[c+'_diff_'str(p)]=(daily_data[c]-daily_data[c].shift(p)) / daily_data[c].shift[p]
comm_data.tail()

ml_datas = pd.DataFrame(index=daily_data.index)
for w in [5, 10, 20, 30, 60]
    for c in comm_data.columns:
        ml_datas[c+'_win_'+str(w)] =comm_data[c] / (comm_data[c].rolling(window=w).max()-comm_data(c).rolling(window=w).min())

ml_datas.tail(10)


3:构建机器学习数据集 预测下一天走势（将数据移动一天，使每天收盘数据的特征用前一天的信息）

ml_datas = ml_datas.join(tech_data)
ml_datas = ml_datas.shift(1)
ml_datas['reg_target'] = daily_data['close']
ml_datas['clf_target'] = (daliy_data['close'] / daily_data['close'].shift(1)) - 1>0
ml_datas.tail(10)

4：检查数据是否正确
ml_datas[['mma_10','reg_target','clf_target']].tail(10)
5去除空值NaN
ml_datas = ml_datas.dropna()
ml_datas.describe()

6：计算Feature importance
x_ori = ml_datas.drop(['reg_targe','clf_target'.'obv'], axis =1)
x_oridescribe()
y=ml_datas['clf_target']
y.describe()

7:特征标准化
from sklearn import preprocessing
scaler = preprocessing.StandardScaler().fit(x_ori)
X = scaler.transform(x_ori)
x[:10,:]

8:选了前20个特征绘图
import numpy as np
import matplotiib.pyplot as plt
form sklearn.ensamble import ExtraTreesClassfier


9:对泸深300指数预测分类


10:网络搜索+ 交叉验证

11：回归
X_ori = ml_datas.drop(['reg_target','clf_target'],axis=1)
y = ml_datas['reg_target']

X_ori_head()


















二：
回归测试Benchmark
测试一下其他方法
网格搜索岭回归的参数
尝试一下PCA

