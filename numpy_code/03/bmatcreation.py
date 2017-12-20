import  numpy as np

#(1) 首先，创建一个2×2的单位矩阵：
A = np.eye(2)

print("A", A)
B = 2* A
print("B", B)

#2) 使用字符串创建复合矩阵，该字符串的格式与mat函数中一致，只是在这里你可以用矩阵变量名代替数字：
print("Compound matrix\n", np.bmat("A B; A B"))