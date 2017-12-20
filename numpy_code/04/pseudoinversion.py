'''
摩尔·彭罗斯广义逆矩阵（Moore-Penrose pseudoinverse）可以使用numpy.linalg模块中的
pinv函数进行求解（广义逆矩阵的具体定义请访问http://en.wikipedia.org/wiki/Moore%E2%80%-
93Penrose_pseudoinverse）。计算广义逆矩阵需要用到奇异值分解。 inv函数只接受方阵作为输入
矩阵，而pinv函数则没有这个限制

'''
import numpy as np
# (1) 首先，创建一个矩阵：
A = np.mat("4 11 14;8 7 -2")
print ("A\n", A)
# (2) 使用pinv函数计算广义逆矩阵：
pseudoinv = np.linalg.pinv(A)
print ("Pseudo inverse\n", pseudoinv)
# (3) 将原矩阵和得到的广义逆矩阵相乘：
print ("Check", A * pseudoinv)