'''
超几何分布（hypergeometric distribution）是一种离散概率分布，它描述的是一个罐子里有
两种物件，无放回地从中抽取指定数量的物件后，抽出指定种类物件的数量。 NumPy random模
块中的hypergeometric函数可以模拟这种分布
设想有这样一个游戏秀节目，每当参赛者回答对一个问题，他们可以从一个罐子里摸出3个
球并放回。罐子里有一个“倒霉球”，一旦这个球被摸出，参赛者会被扣去6分。而如果他们摸出
的3个球全部来自其余的25个普通球，那么可以得到1分。因此，如果一共有100道问题被正确回
答，得分情况会是怎样的呢？为了解决这个问题，请完成如下步骤
'''
import numpy as np
from matplotlib.pyplot import plot, show
'''
(1) 使用hypergeometric函数初始化游戏的结果矩阵。该函数的第一个参数为罐中普通球
的数量，第二个参数为“倒霉球”的数量，第三个参数为每次采样（摸球）的数量。
'''
points = np.zeros(100)
outcomes = np.random.hypergeometric(25, 1, 3, size=len(points))
#(2) 根据上一步产生的游戏结果计算相应的得分。
for i in range(len(points)):
    if outcomes[i] == 3:
        points[i] = points[i - 1] + 1
    elif outcomes[i] == 2:
        points[i] = points[i - 1] - 6
    else:
        print (outcomes[i])
# (3) 使用Matplotlib绘制points数组。
plot(np.arange(len(points)), points)
show()