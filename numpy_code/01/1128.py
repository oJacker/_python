# -*- coding:utf-8 -*-

#向量相加-Python
#  python2.x range(n)
# python3.5 加list(range(n))
def pythonsum(n):
    a = list(range(n))
    b = list(range(n))
    c = []
    print(a)
    for i in list(range(len(a))):
        a[i] = i ** 2
        b[i] = i ** 3
        c.append(a[i] + b [i])
    return   #[ 0  2 12]

# 向量相加-Numpy
import  numpy as np
def numpysum(n):
    a = np.arange(n) ** 2
    b = np.arange(n) ** 3
    c =a + b
    return  c   #[ 0  2 12]
# 效率比较
import  sys
from datetime import  datetime
import  numpy as np
'''
size = 1000
start = datetime.now()
c = pythonsum(size)
delta = datetime.now() - start
print("The last 2 elements of the sum", c)
print("PythonSum elapsed time in microseconds", delta.microseconds)

 
start = datetime.now()
c = numpysum(size)
delta = datetime.now() -start
print("The last 2 elements of the sum", c[-2:])
print("NumPySum elapsed time in microseconds", delta.microseconds)
'''

# numpy 数组
a = np.arange(5)
print(a.dtype)
print(a)
print(a.shape)

#创建多维数组
m = np.array([np.arange(2),np.arange(2)])

print(m)
print(m.shape)
print(m.dtype)


print(np.zeros(10))
print(np.zeros((3,6)))

print(np.empty((2, 3, 2)))
print(np.arange(15))

#选取数组元素
a = np.array([[1,2],[3,4]])
print(a)
print(a[0,0])
print(a[0,1])
print(a[1,0])
print(a[1,1])

print(np.arange(7, dtype=np.uint16))

try:
    print(np.int(42.0 + 1.j))
except:
    print("TypeError")

print(float(42.0 + 1.j))
