# -*- coding:utf-8 -*-

import sys

# 导入pygame模块，第8行的作用是简化你的输入，如不用在event前再加上pygame模块名
import pygame
from pygame.locals import *


def hello_world():
    # 任何pygame程序均需要执行此句进行模块初始化
    pygame.init()

    # 设置窗口的模式，（400, 300）表示窗口像素，及（宽度，高度）
    # 此函数返回一个Surface对象，本程序不使用它，故没保存
    screen = pygame.display.set_mode((400, 300))

    # 设置窗口标题
    pygame.display.set_caption('Hello World!')

    # 循环，直到接收到窗口关闭事件
    #(3) 游戏通常会有一个主循环一直运行，直到退出事件的发生。在本例中，我们仅仅在坐标
      # (100, 100)处设置一个Hello World文本标签，文本的字体大小为19，颜色为
    while True:
        sysFont = pygame.font.SysFont("None", 19)
        rendered = sysFont.render('Hello World', 0, (255, 100, 100))
        screen.blit(rendered, (100, 100))
        # 处理事件
        for event in pygame.event.get():
            # 接收到窗口关闭事件
            if event.type == QUIT:
                # 退出
                pygame.quit()
                sys.exit()
                # 将Surface对象上帝绘制在屏幕上
        pygame.display.update()


if __name__ == "__main__":
    hello_world()