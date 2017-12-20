import numpy as np
# (1) 生成5个随机数作为现金流的取值。插入-100作为初始值。
cashflows = np.random.randint(100, size=5)
cashflows = np.insert(cashflows, 0, -100)
print ("Cashflows", cashflows)
# (2) 根据上一步生成的现金流数据，调用npv函数计算净现值。利率按3%计算
print ("Net present value", np.npv(0.03, cashflows))