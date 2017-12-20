# -*- coding: utf-8 -*-
# 汉诺塔(hanoi)


'''
def move (n, source, target, helper):
    if n == 1:
        print (source + ' -> ' + target
    else:
        move(n -1, source ,helper, target)
        print (source + ' -> ' + target )
        move(n -1, helper, target, source)



move(4, 'A', 'B', 'C')
'''

i = 1
def move(n, mfrom, mto) :
  global i
  print ("第%d步:将%d号盘子从%s -> %s" %(i, n, mfrom, mto))
  i += 1

def hanoi(n, source, target, helper) :
  if n == 1 :
    move(1, source, helper)
  else :
    hanoi(n - 1, source, helper, target) 
    move(n, source, helper)    
    hanoi(n - 1, target, source, helper)



hanoi(4, 'A', 'B', 'C')
