import numpy as np

'''
(1) 沿着指定的轴，在连续的数组元素之间递归调用通用函数，即可得到输入数组的规约
（reduce）计算结果。对于add函数，其对数组的reduce计算结果等价于对数组元素求和。调用
reduce方法
'''
a = np.arange(9)
print(a)
print("Reduce", np.add.reduce(a))
'''
(2) accumulate方法同样可以递归作用于输入数组。但是与reduce方法不同的是，它将存
储运算的中间结果并返回。因此在add函数上调用accumulate方法，等价于直接调用cumsum函
数。在add函数上调用accumulate方法：
'''
print ("Accumulate", np.add.accumulate(a))
'''
(3) reduceat方法解释起来有点复杂，我们先运行一次，再一步一步来看它的算法。
reduceat方法需要输入一个数组以及一个索引值列表作为参数。
'''
print ("Reduceat", np.add.reduceat(a, [0, 5, 2, 7]))
print ("Reduceat step I", np.add.reduce(a[0:5]))
print ("Reduceat step II", a[5])
print ("Reduceat step III", np.add.reduce(a[2:7]))
print ("Reduceat step IV", np.add.reduce(a[7:]))
print ("Outer", np.add.outer(np.arange(3), a))