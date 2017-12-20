# -*- coding:utf-8 -*-

import re


# 正则表达式
m = re.match(r'\d{3}\-\d{3,8}','010-12345')

print(dir(m))
print(m.string)

print(m.pos,m.endpos)
'''
010-12345
0 9
('010', '12345')
010-12345
010
12345

'''

#分组
m = re.match(r'^(\d{3})-(\d{3,8})$','010-12345')
print(m.groups())
print(m.group(0))
print(m.group(1))
print(m.group(2))

'''
010-12345
0 9
('010', '12345')
010-12345
010
12345
'''

# 分割

p = re.compile(r'\d+')
print(dir(p))
'''
['__class__', '__copy__', '__deepcopy__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__le__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'findall', 'finditer', 'flags', 'fullmatch', 'groupindex', 'groups', 'match', 'pattern', 'scanner', 'search', 'split', 'sub', 'subn']

'''
print(type(p))
 
print(p.split('one1two3three3four4'))  #['one', 'two', 'three', 'four', '']
print(m.group(2))  #12345

t = '20:15:45'

re.match(r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$', t)

print(m.groups())

























