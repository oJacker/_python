from numpy.testing.decorators import  setastest, skipif, knownfailureif
from numpy.testing import decorate_methods
@setastest(False)
def test_false():
    pass
@setastest(True)
@skipif(True)
def test_skip():
    pass
@knownfailureif(True)
def test_alwaysfail():
    pass
class TestClass():
    def test_true2(self):
        pass
class TestClass2():
    def test_false2(self):
        pass
decorate_methods(TestClass2, setastest(False), 'test_false2')