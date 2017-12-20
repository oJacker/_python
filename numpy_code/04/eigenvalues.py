import numpy as np
A = np.mat("3 -2;1 0")
print ("A\n", A)
# (2) 调用eigvals函数求解特征值：
print ("Eigenvalues", np.linalg.eigvals(A))
# (3) 使用eig函数求解特征值和特征向量。该函数将返回一个元组，按列排放着特征值和对应的特征向量，其中第一列为特征值，第二列为特征向量。
eigenvalues, eigenvectors = np.linalg.eig(A)
print ("First tuple of eig", eigenvalues)
print ("Second tuple of eig\n", eigenvectors)
# (4) 使用dot函数验证求得的解是否正确。分别计算等式 Ax = ax 的左半部分和右半部分，检查是否相等。
for i in range(len(eigenvalues)):
    print ("Left", np.dot(A, eigenvectors[:,i]))
print ("Right", eigenvalues[i] * eigenvectors[:,i])