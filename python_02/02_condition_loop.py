# -*- coding: utf-8 -*-

a = 100
b = 200
c = 300
if c == a :
    print(a)
elif c == b:
    print(b)
else:
    print(c)

x = None
if x is None:
    print ('x is None')
if not x:
    print('x is None')



s = 0
for i in range(0, 101):
    s += 1
print(s)

s = 0
i = 0
while i<= 100:
    s += i
    i += 1
print(s)


for i in range(0, 100):
    if i< 10:
        pass
    elif i< 30:
        continue
    elif i< 35:
        print(i)
    else:
        break
        
