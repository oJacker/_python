import  numpy as np
# (1) 生成5个随机数作为实部， 5个随机数作为虚部。设置随机数种子为42：
np.random.seed(42)
complex_numbers = np.random.random(5) + 1j * np.random.random(5)
print ("Complex numbers\n", complex_numbers)
# (2) 调用sort_complex函数对上面生成的复数进行排序：
print ("Sorted\n", np.sort_complex(complex_numbers))