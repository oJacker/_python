import numpy as np
from matplotlib.pyplot import plot, show

# 用正确的参数调用fv函数，计算终值：
print ("Future value", np.fv(0.03/4, 5 * 4, -10, -1000))
fvals = []
for i in range(1, 10):
    fvals.append(np.fv(.03/4, i * 4, -10, -1000))
plot(fvals, 'bo')
show()