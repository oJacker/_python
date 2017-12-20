import  numpy as np
#(1) 创建斐波那契矩阵：
F = np.matrix([[1, 1],[1, 0]])
print("F", F)
# (2) 计算斐波那契数列中的第8个数，即矩阵的幂为8减去1。计算出的斐波那契数位于矩阵的对角线上：
print("8th Fibonacci", (F ** 7)[0, 0])
# (3) 利用黄金分割公式或通常所说的比奈公式（Binet’ s Formula），加上取整函数，就可以直
# 接计算斐波那契数。计算前8个斐波那契数：
n =np.arange(1, 9)
sqrt5 = np.sqrt(5)
phi = (1+ sqrt5) /2
fibonacci = np.rint((phi ** n -(-1/phi)**n)/sqrt5)
print("Fibonacci", fibonacci)