# -*- coding: utf-8 -*-

d = {'a':1, 'b':2, 1:'one', 2:'two', 3: [1,2,3]}

print(type(dict))
print(type(d))



print(d['a'])
print(d[1])
print(d[3])



print('two' in d)
print(3 in d)
del(d[3])


print(len(d))


d[3] = [1, 2, 3, 4]
d[3] = '1234'

 



for key in d:
    print(d[key])
print('......')
for k, v in d.items():
    print(k, v)
keys=d.keys();
print(type(keys))
print(keys)
