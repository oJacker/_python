import numpy as np
import unittest
# (1) 首先，我们编写一个阶乘函数：
def factorial(n):
    if n ==0:
        return 1
    if n < 0:
        raise (ValueError, "Unexpected negative value")
    return np.arange(1, n+1).cumprod()
#(2) 现在我们来编写单元测试。编写一个包含单元测试的类，继承Python标准库unittest模
# 块中的TestCase类
class FactorialTest(unittest.TestCase):
    def test_factorial(self):
        # # 计算3的阶乘，测试通过
        self.assertEqual(6, factorial(3)[-1])
        np.testing.assert_equal(np.array([1, 2, 6]), factorial(3))
    def test_zero(self):
        # # 计算0的阶乘，测试通过
        self.assertEqual(1, factorial(0))
    def test_negative(self):
        # 计算负数的阶乘，测试不通过
        # 这里应抛出ValueError异常，但我们断言其抛出IndexError异常
        self.assertRaises(IndexError, factorial(-10))

if __name__ == '__main__':
    unittest.main()