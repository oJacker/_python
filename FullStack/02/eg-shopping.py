#!/usr/bin/env python
# -*- coding:utf-8 -*-

product_list=[
    ('Mac', 18000),
    ('tsla',10000),
    ('python book',120),
    ('bke',2000)
]

print(product_list[0])
print(product_list[0][1])
exit()
saving = input("Please input your money: ")
shopping_list = []

if saving.isdigit():
    saving= int(saving)
    while True:
        # 打印商品信息
        for i,v in enumerate(product_list,1):
            print(i,'>>>>',v)
        # 选择商品
        choice = input("选择购买商品编号【退出： q】: ")

        #验证输入是否合法
        if choice.isdigit():
            choice = int(choice)
            if choice >0 and choice <= len(product_list):

                p_item = product_list[choice-1]

                if p_item[1] < saving:
                    saving -= p_item[1]

                    shopping_list.append(p_item)
                else:
                    print('余额不足，还剩%s' % saving)
                print(p_item)
            else:
                print("编码不存在")
        elif choice == 'q':
            print('----------------您已经购买如下商品-------------')
            # 循环遍历购物车里的商品，购物车存放的是已买商品
            for i in shopping_list:
                print(i)
            print('您还剩%s元钱'%saving)
            break
        else:
            print("invalid input")