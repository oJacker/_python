import  numpy as np
a = np.arange(-4, 4)

print(a)
# (1) remainder函数逐个返回两个数组中元素相除后的余数。如果第二个数字为0，则直接返回0：
print("Remainder", np.remainder(a, 2))
# (2) mod函数与remainder函数的功能完全一致：
print("Mod", np.mod(a, 2))
# (3) %操作符仅仅是remainder函数的简写：
print("% operator", a % 2)
# (4) fmod函数处理负数的方式与remainder、 mod和%不同。所得余数的正负由被除数决定，
# 与除数的正负无关：
print("Fmod", np.fmod(a, 2))