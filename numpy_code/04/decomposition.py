'''
SVD（Singular Value Decomposition，奇异值分解）是一种因子分解运算，将一个矩阵分解
为3个矩阵的乘积。奇异值分解是前面讨论过的特征值分解的一种推广。在numpy.linalg模块
中的svd函数可以对矩阵进行奇异值分解。该函数返回3个矩阵——U、 Sigma和V，其中U和V是
正交矩阵， Sigma包含输入矩阵的奇异值
'''

import numpy as np
# (1) 首先，创建一个矩阵：
A = np.mat("4 11 14;8 7 -2")
print ("A", A)
# (2) 使用svd函数分解矩阵：
U, Sigma, V = np.linalg.svd(A, full_matrices=False)
print ("U",U)

print ("Sigma",Sigma)

print ("V",V)
# (3) 不过，我们并没有真正得到中间的奇异值矩阵——得到的只是其对角线上的值，而非对角线上的值均为0。
print ("Product\n", U * np.diag(Sigma) * V)