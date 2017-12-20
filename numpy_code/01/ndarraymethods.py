import  numpy as np

# (1) clip方法返回一个修剪过的数组，也就是将所有比给定最大值还大的元素全部设为给定
# 的最大值，而所有比给定最小值还小的元素全部设为给定的最小值。
a = np.arange(5)
print("a = ", a)
print("Clipped", a.clip(1, 2))
# (2) compress方法返回一个根据给定条件筛选后的数组。
a = np.arange(4)
print(a)

print("Compressed", a.compress(a >2 ))

# (1) 计算8的阶乘。为此，先生成一个1~8的整数数组，并调用prod方法
b= np.arange(1, 9)
print("b =", b)
print("Factorial", b.prod())
#(2) 没问题！调用cumprod方法，计算数组元素的累积乘积。
print("Factorials", b.cumprod())