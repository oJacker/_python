import  pygame, sys
from pygame.locals import *
import numpy as np
pygame.init()

# (1) 创建一个Pygame的Clock对象，如下所示
clock = pygame.time.Clock()
screen = pygame.display.set_mode((400, 400))

pygame.display.set_caption('Animating Objects')
'''
(2) 和本书配套的源代码文件一起，有一张头部的图片。
'''
img = pygame.image.load('head.jpg')
'''
(3) 我们将定义一些数组来储存动画中图片的位置坐标。既然对象可以被移动，那么应该有
四个方向——上、下、左、右。每一个方向上都有40个等距的步长。我们将各方向上的值全部初
始化为0。
'''
steps = np.linspace(20, 260, 40).astype(int)
right = np.zeros((2, len(steps)))
down = np.zeros((2, len(steps)))
left = np.zeros((2, len(steps)))
up =  np.zeros((2, len(steps)))
# (4) 设置图片的位置坐标是一件很烦琐的事情。不过，有一个小技巧可以用上——[::-1]可以获得倒序的数组元素。
right[0] = steps
right[1] = 20

down[0] = 360
down[1] = steps
left[0] = steps[::-1]
left[1] = 360

up[0] = 20
up[1] =steps[::-1]
# (5) 四个方向的路径可以连接在一起，但需要先用T操作符对数组进行转置操作，使得它们以正确的方式对齐。
pos = np.concatenate((right.T, down.T, left.T, up.T))
i = 0

while  True:

    screen.fill((255, 255, 255))
    if i >= len(pos):
        i = 0
    screen.blit(img.pos[i])
    i += 1
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    # (6) 在主循环中，我们设置时钟周期为每秒30帧：
    clock.tick(30)
