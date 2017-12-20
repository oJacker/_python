import  numpy as np

# (1) 创建矩阵A和数组b：
A = np.mat("1 -2 1;0 2 -8; -4 5 9")
print("A\n", A)

b = np.array([0, 8, -9])
print("b\n", b)

# (2) 调用solve函数求解线性方程组：
x =np.linalg.solve(A, b)
print("Solution", x)
# 3) 使用dot函数检查求得的解是否正确：
print("Check\n", np.dot(A, x))