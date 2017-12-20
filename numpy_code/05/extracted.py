

import numpy as np
# (1) 使用arange函数创建数组：
a = np.arange(7)
# (2) 生成选择偶数元素的条件变量：
condition = (a % 2) == 0
# (3) 使用extract函数基于生成的条件从数组中抽取元素：
print ("Even numbers", np.extract(condition, a))
# (4) 使用nonzero函数抽取数组中的非零元素：
print ("Non zero", np.nonzero(a))