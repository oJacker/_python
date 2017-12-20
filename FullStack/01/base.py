#!/usr/bin/env python
# -*- coding:utf-8 -*-


# print（） 用来输出指定的内容
print("Hello World")

# 别名变量
name ="hello world"
print(name)
# Hello World

name,age ="ojacker",12
print(name,age)
#ojacker 12


#赋值
name1 = "Super"
name2 = name1
name1 = "Ben"
print(name1,name2)
# Ben Super


#变量的命名规则


from keyword import kwlist
print(kwlist)
'''
['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise',
'return', 'try', 'while', 'with', 'yield']
'''
# 约定俗成的一些规则：  变量名称应该有意义、不要用中文做变量名、不要使用拼音

#表达式和运算符
# 算术运算符 ： + - * / //(取整除) %（取余） **
print("2+3=",2+3)
print("3-2=",3-2)
print("2*3=",2*3)
print("5/2+",5/2)
print("5//2=",5//2)
print("5%2=",5%2)
print("2**3=",2**3)
'''
2+3= 5
3-2= 1
2*3= 6
5/2+ 2.5
5//2= 2
5%2= 1
2**3= 8
'''
# 赋值运算符： = 、+= -= *= /= %= //= **=
num =2
#num += 1     等价于 num = num + 1
#num -= 1    # 等价于 num = num - 1 
#num *= 1    # 等价于 num = num * 1
#num /= 1    # 等价于 num = num / 1
#num //= 1    # 等价于 num = num // 1
#num %= 1)  # 等价于 num = num % 1
#num **= 2    # 等价于 num = num ** 2
# 比较运算符：>、 <、 >=、 <=、 ==、!= True False简单讲一下

'''
>>> a = 5
>>> b = 3
>>> a > b  # 检查左操作数的值是否大于右操作数的值，如果是，则条件成立。 
True
>>> a < b  # 检查左操作数的值是否小于右操作数的值，如果是，则条件成立。
False
>>> a <= b  # 检查左操作数的值是否小于或等于右操作数的值，如果是，则条件成立。
False
>>> a >= b  # 检查左操作数的值是否大于或等于右操作数的值，如果是，则条件成立。
True
>>> a == b  # 检查，两个操作数的值是否相等，如果是则条件变为真。
False
>>> a != b  # 检查两个操作数的值是否相等，如果值不相等，则条件变为真。
True

'''

# 逻辑运算符： not 、and、 or

'''
>>> a > b and  a < b  # 如果两个操作数都是True，那么结果为True，否则结果为False。
False
>>> a > b or  a < b  # 如果有两个操作数至少有一个为True, 那么条件变为True，否则为False。
True
>>> not a > b  # 反转操作的状态，操作数为True，则结果为False，反之则为True
False

'''

# 成员运算符： not in 、in （判断某个单词里是不是有某个字母）


'''
>>> "h" in "hello"  # 这里的意思是 “h” 在“Hello” 中，判断后结果为True
True 
>>> "h" not in "hello"  # 这里的意思是 “h” 不在“Hello” 中，判断后结果为False
False
'''

# 身份运算符： is、is not（讲数据类型时讲解，一般用来判断变量的数据类型）
'''
>>> a = 123456
>>> b = a
>>> b is a   #判断  a 和 b 是不是同一个 123456
True
>>> c = 123456

>>> c is a  #判断  c 和 a 是不是同一个 123456
False
>>> c is not a   #判断  c 和 a 是不是不是同一个 123456
True

'''

# 获取用户的输入

var = input()
print(var)

var = input("请输入：")

# 流程控制 之if语句

'''
if 判断条件:
    执行语句...
elif 判断条件:
    执行语句...
else:
    执行语句
    
'''
var=input("Enter:")
if var == 'A':
    print("True")
else:
    print("False")

# 流程控制——while循环

'''
while 判断条件：  # 只有条件不成立时退出循环，如果条件为真，则循环就没有停止的时候，成为一个死循环
    执行语句……

'''
init_num = 12
num = int(input("please (int)number :"))
while init_num != num:
    if num >  init_num:
        print("数字过大")
    else:
        print("数字过小")
    num = int(input("Enter:"))

print("猜对了")
# 循环输出1-10所有整数
num = 1
while num <11:
    print(num)
    num = num +1

# 使用break语句，break语句会终端当前循环
# 循环输出1-10所有整数
num = 1
while num <11:
    print("当前数字是",num)
    if num == 5 :
        break
    num = num +1
    print("现在数字变成了：",num)

# break的作用： 结束循环，在死循环中，也可以通过设置一定的条件来结束循环。
# 输出1-100之间的所有奇数。
num = 0
while num<100:
    num = num + 1
    if num%2 ==0:
        continue
    print(num)


# while循环中的else：
'''
while 判断条件： 
    执行语句……
else:
    执行语句……
'''
# 循环没有被中断
num = 0
while num<10:
    num = num + 1
    if num%2 ==0:
        continue
    print(num)
else:
    print("else-----")

# 循环被中断
num = 0
while num<10:
    num = num + 1
    if num%2 ==0:
        break
    print(num)
else:
    print("else-----")
# 嵌套循环：循环套循环
num1 = 0
while num1 <3:
    print(num1,end="++" )
    num1 += 1
    num2 = 0
    while num2<3:
        print(num2,end="  ")
        num2 +=1
    print()

i=1
while i<10:
    j = 1
    while j< i+1:
        print('{}x{}={}\t'.format(i, j, i * j), end='')
        j += 1
    print()
    i += 1

for i in range(1,10):
    for j in range(1,i+1):
        print('{}x{}={}\t'.format(i,j,i*j),end='')
    print()


# 序列
arr = range(10)
#[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
arr = range(1,10,2)
# [1, 3, 5, 7, 9]
'''
range(start, stop[, step]) 
    #start表示起始数字,stop表示结束数字，stop表示每两个相邻数字之间的差，也叫步长
    #列出从start开始，到stop之前所有的数字

'''

# 流程控制——for循环
'''
for var in sequence:
        statements(s)

'''

for i in range(10):
    print(i)


