import numpy as np

def ultimate_answer(a):
    # (2)使用zeros_like函数创建一个和a形状相同，并且元素全部为0的数组result：
    result = np.zeros_like(a)
    result.flat = 42
    return result
# (4) 使用frompyfunc创建通用函数。指定输入参数的个数为1，随后的1为输出参数的个数：
ufunc = np.frompyfunc(ultimate_answer, 1, 1)
print ("The answer", ufunc(np.arange(4)))
print ("The answer", ufunc(np.arange(4).reshape(2, 2)))