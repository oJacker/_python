import numpy as np

# (1) 在创建矩阵的专用字符串中，矩阵的行与行之间用分号隔开，行内的元素之间用空格隔
# 开。使用如下的字符串调用mat函数创建矩阵：
A = np.mat('1 2 3; 4 5 6; 7 8 9')
print("Creation from string", A)

# (2) 用T属性获取转置矩阵：
print("Transpose A", A.T)
# 3) 用I属性获取逆矩阵： 求得的逆矩阵如下（注意：计算复杂度为O(n3)）
print("Inverse A", A.I)

print("Check Inverse", A * A.I)

# (4) 除了使用字符串创建矩阵以外，我们还可以使用NumPy数组进行创建：
print("Creation from array", np.mat(np.arange(9).reshape(3,3)))