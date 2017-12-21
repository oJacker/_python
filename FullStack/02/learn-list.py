#!/usr/bin/env python
#-*- coding:utf-8 -*-

names = 'a b c d e f g'
a = ['a','b','c','d','e','f','g',['a','g']]

#增删改查
print(a[1:]) #从1 取到最后
# ['b', 'c', 'd', 'e', 'f', 'g', ['a', 'g']]
print(a[1:-1]) #从1 取到倒数第二值
# ['b', 'c', 'd', 'e', 'f', 'g']
print(a[0:-1:1]) #从左到右一个一个去取
# ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(a[1::2]) #从左到右隔一个去取
# ['b', 'd', 'f', ['a', 'g']]
print(a[3::-1])
# ['d', 'c', 'b', 'a']
print(a[-2::-1])
# ['g', 'f', 'e', 'd', 'c', 'b', 'a']
print(a[1:-1:-2])
#[]

# 添加 append insert
a.append('aa')  #默认插到最后一个位置
print(a)
# ['a', 'b', 'c', 'd', 'e', 'f', 'g', ['a', 'g'], 'aa']
a.insert(1, 'bb')  #将数据插入到任意一个位置
print(a)
# ['a', 'bb', 'b', 'c', 'd', 'e', 'f', 'g', ['a', 'g'], 'aa']
# 修改
a[1] = 'ab'
print(a)
# ['a', 'ab', 'b', 'c', 'd', 'e', 'f', 'g', ['a', 'g'], 'aa']
a[1:2]=['a','b']
print(a)
# ['a', 'a', 'b', 'b', 'c', 'd', 'e', 'f', 'g', ['a', 'g'], 'aa']

#删除 remove pop del
a.remove(a[0])
print(a)
# ['a', 'b', 'b', 'c', 'd', 'e', 'f', 'g', ['a', 'g'], 'aa']
b = a.pop(1)
print(a)
# ['a', 'b', 'c', 'd', 'e', 'f', 'g', ['a', 'g'], 'aa']
print(b)
# b

del a[0]
print(a)
# ['b', 'c', 'd', 'e', 'f', 'g', ['a', 'g'], 'aa']


#count:计算某元素出现次数
t = ['to','be','or','not','to','be'].count('to')
print(t)
# 2
# extend

a = [1,2,3]
b = [4,5,6]
a.extend(b)
print(a)
# [1, 2, 3, 4, 5, 6]
print(b)
# [4, 5, 6]

# index 根据内容找位置
a = ['a','b','c','d','e','f','g',['a','g']]
find_d_index= a.index('d')
print('find_d_index: ',find_d_index)
little_list = a[find_d_index+1:]
print(little_list)

find_newd_index = little_list.index('f')
print("find_newd_index",find_newd_index)

second_lg_index_in_big_list=find_d_index + find_newd_index +1
print("second lg:",a[second_lg_index_in_big_list])

# reverse
a = ['a','b','c','d','e','f','g',['a','g']]
a.reverse()
print(a)

x = [4, 6, 2, 1, 7, 9]
x.reverse()
print(x)
# [9, 7, 1, 2, 6, 4]
x.sort(reverse=True)
print(x)
# [9, 7, 6, 4, 2, 1]