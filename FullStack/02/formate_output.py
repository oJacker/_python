#!/usr/bin/env python
# -*- coding:utf-8 -*-

name = input("Please input Name: ")
age = int(input("Please input Age: "))
job = input("Please input Job: ")
salary = input("please input Salary: ")

# Judge whether the salary is an integer

if salary.isdigit():
    salary = int(salary)
else:
    exit("must input digit")

msg = '''
------------- about of %s --------
Name : %s
Age : %d
Job : %s
Salary: %f
You will be retired in %s years
---------------end -----------------
''' % (name,name,age,job,salary,70-age)

print(msg)