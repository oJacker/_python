#!/usr/bin/env python
#-*- coding:utf-8 -*-

user = 'ojacker'
passwd = '123456'

counter = 0
while counter < 3:
    username = input("Please input Username: ")
    password = input("Please input Password: ")
    if username == user and password ==  passwd :
        print("Welcome %s login ..." % user)
        break
    else:
        print("Invalid Username or Password !")
    counter += 1
    if counter == 3:
        keep_go_chice = input("Do you want this game?[y/n]")
        if keep_go_chice.upper() == 'Y' :
            counter = 0
else:
    print("system busy！")