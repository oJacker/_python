#!/usr/bin/env python
# -*- coding:utf-8 -*-

for i in range(1,101):
    if i % 2 == 1:
        print("loop: ", i)
for i in range(100):
    if i <50 or i>70:
        print(i)

for i in range (1, 100, 2):
    print("loop: " ,i)

user = 'ojacker'
passwd = '123456'
passed_authentication = False
for i in range(3):
    username = input("Please input Username: ")
    password = input("Please input Password: ")
    if username == user  and password== password:
        print("Welcome %s login ..." % user)
        passed_authentication = True
        break
    else:
        print("Invalid username or password !")
if  not passed_authentication:
    print("System is buys")