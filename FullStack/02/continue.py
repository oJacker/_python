#!/usr/bin/env python
# -*- coding:utf-8 -*-

flag = False

for i in range(10):
    if i < 5:
        continue
    print(i)
    for j in range(10):
        print("layer2", j)
        if j == 6:
            flag = True
            break
    if flag:
        break