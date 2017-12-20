'''
随机数在蒙特卡罗方法（Monto Carlo method）、随机积分等很多方面都有应用。真随机数的
产生很困难，因此在实际应用中我们通常使用伪随机数。
设想你来到了一个17世纪的赌场，正在对一个硬币赌博游戏下8份赌注。每一轮抛9枚硬币，
如果少于5枚硬币正面朝上，你将损失8份赌注中的1份；否则，你将赢得1份赌注。我们来模拟
一下赌博的过程，初始资本为1000份赌注。为此，我们需要使用random模块中的binomial
函数。
'''
import numpy as np
from matplotlib.pyplot import plot, show
# (1) 初始化一个全0的数组来存放剩余资本。以参数10000调用binomial函数，意味着我们
# 将在赌场中玩10 000轮硬币赌博游戏
cash = np.zeros(10000)
cash[0] = 1000
outcome = np.random.binomial(9, 0.5, size=len(cash))
# (2) 模拟每一轮抛硬币的结果并更新cash数组。打印出outcome的最小值和最大值，以检查
# 输出中是否有任何异常值：
for i in range(1, len(cash)):
    if outcome[i] < 5:
        cash[i] = cash[i - 1] - 1
    elif outcome[i] < 10:
        cash[i] = cash[i - 1] + 1
    else:
        raise AssertionError("Unexpected outcome " + outcome)
print (outcome.min(), outcome.max())
# (3) 使用Matplotlib绘制cash数组：
plot(np.arange(len(cash)), cash)
show()