#!/usr/bin/env python
# -*- coding:utf-8 -*-

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

exit_flag = False

for i in range(10):
    if i <5:
        continue
    print(i )
    for j in range(10):
        print("layer2",j)
        if j == 6:
            exit_flag = True
            break
    if exit_flag:
        break