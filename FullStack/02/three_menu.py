#!/usr/bin/env python
# -*- coding:utf-8 -*-

menu ={
    '北京':{
        '朝阳':{
            '国贸':{
                'CICC':{},
                'HP':{},
                '渣打银行':{},
                'CCTV':{}
            },
            '望京':{
                '陌陌':{},
                '360':{},
                '奔驰':{},
            },
            '三里屯':{
                '优衣库':{},
                'apple':{},
            }
        },
        '昌平':{
            '沙河':{
                'oldboy':{},
                '包子':{}
            },
            '天通苑':{
                '我爱我家':{},
                '链家':{}
            },
            '回龙观':{}
        },
        '海淀':{
            '五道口':{
                '谷歌':{},
                '网易':{},
                'Sohu':{},
                'Sogo':{},
                '快手':{}
            },
            'youku':{},
            'Iqiyi':{},
            '汽车之家':{},
            '新东方':{},
            'QQ':{},
        }

    },
    '上海':{
        '浦东':{
            '陆家嘴':{
                "CICC":{},
                "高盛":{},
                "摩根":{}
            },
            '外滩':{},
        },
        '闵行':{},
        '静安区':{},
    },
    '广东':{
        '济南':{},
        '德州':{
            '乐陵':{
                '丁务镇':{},
                '城区':{}
            },
            '平原':{},
        },
        '青岛':{},
    },
}

menu_main_layer = menu
menu_parent_layers = []
while True:
    for key in menu_main_layer:
        print(key)
    choice = input(">>>:").strip()
    if len(choice) == 0: continue
    if choice in menu_main_layer:
        menu_parent_layers.append(menu_main_layer)
        #下次loop，当前用户选择，就可以直接列表的最后一个值出来就ok了
        menu_main_layer=menu_main_layer[choice]
    elif choice == "b":
        if menu_parent_layers:
            menu_main_layer = menu_parent_layers.pop()
    else:
        print("无此项内容")

