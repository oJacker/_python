#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 字典的创建
dic ={'name':'ojacker','age':25,'hobby':{'girl_name':'yz','age':23},'is_handsome':True}

print(dic)
# {'is_handsome': True, 'hobby': {'age': 23, 'girl_name': 'yz'}, 'name': 'ojacker', 'age': 25}

# 字典两大特点：无序，键唯一

dic1 = {}
dic2 = dict((('name','ojacker'),))
print(dic2)
# {'name': 'ojacker'}
dic3 =dict([['name','ojacker'],])
print(dic3)
# {'name': 'ojacker'}

dic1 = {'name':'ojacker'}
dic1['age'] =18
print(dic1)
# {'name': 'ojacker', 'age': 18}

# 键存在，不改动，返回字典中相应的键对应的值
ret = dic1.setdefault('age',34)
print(ret)
# 18
#键不存在，在字典中中增加新的键值对，并返回相应的值
ret2 = dic1.setdefault('hobby','girl')
print(dic1)
# {'hobby': 'girl', 'age': 18, 'name': 'ojacker'}
print(ret2)
# girl
#查  通过键去查找
dic3 ={'name':'ojacker','age':25,'hobby':{'girl_name':'yz','age':23},'is_handsome':True}
print(dic3['name'])
# ojacker
print(list(dic3.keys()))
# ['name', 'age', 'is_handsome', 'hobby']
print(list(dic3.values()))
# ['ojacker', True, 25, {'girl_name': 'yz', 'age': 23}]
print(list(dic3.items()))
# [('name', 'ojacker'), ('age', 25), ('is_handsome', True), ('hobby', {'age': 23, 'girl_name': 'yz'})]

# 改
li = [1,2,34,5,7]
li[2]=5
dic3['age']=26
print(dic3)
# {'is_handsome': True, 'hobby': {'girl_name': 'yz', 'age': 23}, 'name': 'ojacker', 'age': 26}

dic4 ={'name':'ojacker','age':25,'hobby':{'girl_name':'yz','age':23},'is_handsome':True}
dic5 ={'1':'111','name':'kk'}

dic4.update(dic5)
print(dic4)
# {'1': '111', 'hobby': {'girl_name': 'yz', 'age': 23}, 'name': 'kk', 'is_handsome': True, 'age': 25}
print(dic5)
#{'1': '111', 'name': 'kk'}

dic5 ={'name':'ojacker','age':25,'hobby':{'girl_name':'yz','age':23},'is_handsome':True}
#dic5.clear()
#print(dic5)
#{}
del dic5['name']  #删除字典中指定键值对，并返回该键值对的值
print(dic5)
# {'hobby': {'girl_name': 'yz', 'age': 23}, 'age': 25, 'is_handsome': True}
a =dic5.popitem() #随机删除某组键值对，并以元组方式返回值
print(a,dic5)
# ('hobby', {'girl_name': 'yz', 'age': 23}) {'age': 25, 'is_handsome': True}
del dic5  #删除整个字典

# 其他操作以及涉及到的方法其他操作以及涉及到的方法
dic6=dict.fromkeys(['host1','host2','host3'],'test')
print(dic6)
# {'host3': 'test', 'host1': 'test', 'host2': 'test'}
dic6=dict.fromkeys(['host1','host2','host3'],['test1','tets2'])
print(dic6)
# {'host3': ['test1', 'tets2'], 'host1': ['test1', 'tets2'], 'host2': ['test1', 'tets2']}
dic6['host3'][1]='t3'
print(dic6)
# {'host3': ['test1', 't3'], 'host2': ['test1', 't3'], 'host1': ['test1', 't3']}

dic ={'2':'222','5':'555','6':'666'}

print(sorted(dic.items()))
# [('2', '222'), ('5', '555'), ('6', '666')]
for i in dic:
    print(i,dic[i])
for i,v in dic.items():
    print(i,v)


# String 操作
a = "Let's go"
print(a)

# 2 [] ,[:] 通过索引获取字符串中字符,这里和列表的切片操作是相同的,具体内容见列表
# print('helloworld'[2:])

#关键字 in
print(123 in [23,45,123])
print('e2l' in 'hello')

# 4 %   格式字符串
print('%s is a good man' % 'ojacker')

a ='1234'
b='abcd'
d ='55'
c = a +b
print(c)
# 1234abcd

c = ' '.join([a,b,d])
print(c)
# 1234abcd55

# String 的内置方法
st = 'hell kitty {name} is {age}'

print(st.count('l')) # 2
print(st.capitalize())
# Hell kitty {name} is {age}
print(st.center(50,'#'))
# ############hell kitty {name} is {age}############
print(st.endswith('tty3')) #  判断是否以某个内容结尾 False
print(st.startswith('he')) #  判断是否以某个内容开头 True
print(st.expandtabs(tabsize=20))
# hell kitty {name} is {age}
print(st.find('t'))        #  查找到第一个元素，并将索引值返回  7
print(st.format(name='alex',age=37))  # 格式化输出的另一种方式   待定：?:{}
# hell kitty alex is 37
print(st.format_map({'name':'alex','age':22})) #hell kitty alex is 22
print(st.index('t')) #7
print('asd'.isalnum()) # True
print('12632178'.isdecimal()) # True
print('1269999.uuuu'.isnumeric()) # False

print('abc'.isidentifier())
# True
print('Abc'.islower())
# False
print('ABC'.isupper())
# True
print('  e'.isspace())
# False
print('My title'.istitle())
# False
print('My tLtle'.lower())
# my tltle
print('My tLtle'.upper())
# MY TLTLE
print('My tLtle'.swapcase())
# mY TlTLE
print('My tLtle'.ljust(50,'*'))
# My tLtle******************************************
print('My tLtle'.rjust(50,'*'))
# ******************************************My tLtle
print('\tMy tLtle\n'.strip())
print('\tMy tLtle\n'.lstrip())
print('\tMy tLtle\n'.rstrip())
#
#	My tLtle
print('My title title'.replace('itle','lesson',1))
# My tlesson title
print('My title title'.rfind('t'))
#11
print('My title title'.split('i',1))
# ['My t', 'tle title']
print('My title title'.title())
# My Title Title