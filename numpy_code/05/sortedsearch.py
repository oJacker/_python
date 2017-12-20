import numpy as np
# (1) 我们需要一个排序后的数组。使用arange函数创建一个升序排列的数组
a = np.arange(5)
# (2) 现在，我们来调用searchsorted函数：
indices = np.searchsorted(a, [-2, 7])
print ("Indices", indices)
# (3) 使用insert函数构建完整的数组：
print ("The full array", np.insert(a, indices, [-2, 7]))