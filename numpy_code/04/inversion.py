import numpy as np
A = np.mat("0 1 2; 1 0 3; 4 -3 8")
print("A\n", A)

# (2) 现在，我们使用inv函数计算逆矩阵：
inverse = np.linalg.inv(A)

print("inverse of A\n", inverse)