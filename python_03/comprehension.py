# -*- coding: utf-8 -*-
li = []

for i in range(20):
    if(i % 2) == 0:
        li.append(i)

print(li)


li = [1] * 10
print(li)
li[3] = 3
print(li)



li_2d = [[0]*3 ] * 3
print(li_2d)

li_2d[0][0] = 1
print(li_2d)


 
li_3d = [[0] * 3 for i in range(3) ]
print (li_3d)

li_3d[0][0] = 100

print(li_3d)


s = {x for x in range(10) if x %2 == 0}
print(s)

d = {x: x % 2 == 0 for x in range(10)}
print(d)
 
