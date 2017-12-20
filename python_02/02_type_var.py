# -*- coding: utf-8 -*-

import string


#  base type
print(type(None))
print(type(True))
print(type(123456))
print(type(123.45))
print(type(1234.))
print(type('abc'))
'''
<class 'NoneType'>
<class 'bool'>
<class 'int'>
<class 'float'>
<class 'float'>
<class 'str'>

'''

# container type

print(type([1, 2, 3, 'a', 'bc']))
print(type((1, 2, 3, 'abc')))
values = ['abc', 1, 2, 3.]
print((type(values[3])))
print(type(set(['a', 1, 2.])))
print(type({'a':123, 4:'bcd', 5:'efg'}))

'''
<class 'list'>
<class 'tuple'>
<class 'float'>
<class 'set'>
<class 'dict'>

'''

#function
def func(): print(100)
print(type(func))

# modules
print(type(string))

# defined type and type instance

class Cls: pass
print(type(Cls))
cls = Cls()
print(type(cls))



#  variable assignment

try:
    print(x)
except NameError:
    print("NameError: name 'x' is not defined")

x = 100
x = 'abcd'

'''
<class 'function'>
<class 'module'>
<class 'type'>
<class '__main__.Cls'>
NameError: name 'x' is not defined
'''
