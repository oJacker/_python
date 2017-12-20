import numpy as np
x = np.arange(-9, 9)
y = -x
'''
(1) 第一个小技巧需要用XOR或者^操作符。 XOR操作符又被称为不等运算符，因此当两个操
作数的符号不一致时， XOR操作的结果为负数。在NumPy中， ^操作符对应于bitwise_xor函数，
<操作符对应于less函数。
'''
print ("Sign different?", (x ^ y) < 0)
print ("Sign different?", np.less(np.bitwise_xor(x, y), 0))
'''
(2) 在二进制数中， 2的幂数表示为一个1后面跟一串0的形式，例如10、 100、 1000等。而比
2的幂数小1的数表示为一串二进制的1，例如11、 111、 1111（即十进制里的3、 7、 15）等。如
果我们在2的幂数以及比它小1的数之间执行位与操作AND，那么应该得到0。在NumPy中， &操作
符对应于bitwise_and函数， ==操作符对应于equal函数。
'''
print ("Power of 2?\n", x, "\n", (x & (x - 1)) == 0)
print ("Power of 2?\n", x, "\n", np.equal(np.bitwise_and(x, (x - 1)), 0))
'''
(3) 计算余数的技巧实际上只在模为2的幂数（如4、 8、 16等）时有效。二进制的位左移一位，
则数值翻倍。在前一个小技巧中我们看到，将2的幂数减去1可以得到一串1组成的二进制数，如
11、 111、 1111等。这为我们提供了掩码（mask），与这样的掩码做位与操作AND即可得到以2
的幂数作为模的余数。在NumPy中， <<操作符对应于left_shift函数。
'''
print ("Modulus 4\n", x, "\n", x & ((1 << 2) - 1))
print ("Modulus 4\n", x, "\n", np.bitwise_and(x, np.left_shift(1, 2) - 1))

