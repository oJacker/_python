'''
行列式（determinant）是与方阵相关的一个标量值，在数学中得到广泛应用（更详细的介
绍请访问http://en.wikipedia.org/wiki/Determinant）。对于一个n×n的实数矩阵，行列式描述的是
一个线性变换对“有向体积”所造成的影响。行列式的值为正表示保持了空间的定向（顺时针
或逆时针）， 为负则表示颠倒了空间的定向。 numpy.linalg模块中的det函数可以计算矩阵的
行列式。

'''

import numpy as np
A = np.mat("3 4;5 6")
print ("A", A)
print ("Determinant", np.linalg.det(A))