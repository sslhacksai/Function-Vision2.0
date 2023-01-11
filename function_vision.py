import sys
import pygame
import math
from os import path
from input_function import *
from init_function import *
from extend_funciton import *
def resurce_path(relative_path):
    base_path=getattr(sys,'_MEIPASS',path.dirname(path.abspath(__file__)))
    return path.join(base_path,relative_path)
pygame.init()

#  创建窗口
screen=pygame.display.set_mode((800,800))
logo=pygame.image.load(resurce_path("logo.png"))
logo=pygame.transform.scale(logo,(64,64))
pygame.display.set_caption("function vision")
pygame.display.set_icon(logo)
func=[]  # 存储正在显示的所有函数表达式
color=[RED,ORANGE,YELLOW,GREEN,CYAN,BLUE,PURPLE,WHITE]
#  距离函数，求两个像素的欧氏距离
def dis(a,b):
    try:
        return math.sqrt(math.pow(a[0]-b[0],2)+math.pow(a[1]-b[1],2))
    except: # 当距离过大时会溢出，此时使用一个很大的数作为结果
        return math.inf
#   函数求值 func函数表达式 x自变量值
def f(func,x):
    try:
        return [eval(func),False]  #  系统内置函数，将字符串作为有效表达式执行
    except:
        return [nan,True]  #解释错误原因是分母为0的情况出现了，将其表达式值用某个数代替即可

# 读入一个函数到当前函数列表
def add_function():
    func.append(InputFunction(screen, pygame.font.Font(None, 40),WHITE, (200, 300)))    # 输入函数表达式

# 绘制所有函数
def draw_function(sx,sy,watch):
    count=0
    for now in func:  # 绘制所有函数
        #   取点绘制单个函数图像
        pointx=[]
        pointy=[]
        exist=[]
        # 取点步长，视窗放大时步长减小提高精确度，视窗缩小时步长增大提高效率
        # 无论坐标轴上每单位代表多上像素，取点步长总是一像素
        dx = 1 / watch
        for i in range(0, 801):
            # 按照步长每像素取一次点
            pointx.append(float(-sx / watch + dx * i))
            num=f(now,pointx[i])
            pointy.append(num[0])
            exist.append(num[1])

        # 用连线的方式近视该视窗位置的函数图像
        st = [(0, 0)]
        en = [(0, 0)]
        for i in range(1, 801):
            if isinstance(pointy[i-1],tuple)==False:
                st.append((pointx[i - 1] * watch + sx, -pointy[i - 1] * watch + sy))
            else:   #  如果输入是一个元组，启用描点功能
                st.append((pointy[i-1][0]*watch + sx, -pointy[i-1][1]*watch + sy))
            if isinstance(pointy[i],tuple)==False:
                en.append((pointx[i] * watch + sx, -pointy[i] * watch + sy))
            else:
                en.append((pointy[i][0]*watch + sx, -pointy[i][1]*watch + sy))
            if exist[i-1] or exist[i]:  # 若该点不存在，则不连线
                continue
            if now.count("floor") or now.count("ceil"):
                if dis(st[i], en[i]) > dis(st[i - 1], en[i - 1]) + 10:
                    continue
            elif dis(st[i], en[i]) > dis(st[i - 1], en[i - 1]) + 200:
                continue
            # 根据坐标轴的缩放大小，将点按照比例对应到像素后连线
            try:
                #  描点和函数绘制区分开来操作
                if isinstance(pointy[i],tuple):
                    pygame.draw.circle(screen,WHITE,en[i],4)
                else:
                    pygame.draw.aaline(screen, color[count],st[i],en[i],2)  # 通过线段来拟合函数曲线
            except:
                pass
        count+=1
        count%=len(color)

# 坐标系绘制
def coordinate(sx,sy,watch):
    # 横纵辅助线绘制
    for i in range(sx, 800, watch):
        pygame.draw.line(screen, DARKGREY, (i, -1e9), (i, 1e9))
    for i in range(sx, 0, -watch):
        pygame.draw.line(screen, DARKGREY, (i, -1e9), (i, 1e9))
    for i in range(sy, 0, -watch):
        pygame.draw.line(screen, DARKGREY, (-1e9, i), (1e9, i))
    for i in range(sy, 800, watch):
        pygame.draw.line(screen, DARKGREY, (-1e9, i), (1e9, i))
    # 横纵坐标上的单位点绘制
    font1 = pygame.font.Font(None, 20)
    count = 0
    for i in range(sy, 800, watch):
        pygame.draw.circle(screen, GREY, (sx, i), 4)
        text = font1.render(str(-count), True, GREY)  # 加上下标
        if watch >= 16 and count:
            screen.blit(text, (sx + 7, i - 7))
        count += 1
    count = 0
    for i in range(sy, 0, -watch):
        pygame.draw.circle(screen, GREY, (sx, i), 4)
        text = font1.render(str(-count), True, GREY)
        if watch >= 16 and count:
            screen.blit(text, (sx + 7, i - 7))
        count -= 1
    count = 0
    for i in range(sx, 0, -watch):
        pygame.draw.circle(screen, GREY, (i, sy), 4)
        text = font1.render(str(count), True, GREY)
        if watch >= 16 and count:
            screen.blit(text, (i - 7, sy + 7))
        count -= 1
    count = 0
    for i in range(sx, 800, watch):
        pygame.draw.circle(screen, GREY, (i, sy), 4)
        text = font1.render(str(count), True, GREY)
        if watch >= 16 and count:
            screen.blit(text, (i - 3, sy + 7))
        count += 1
    # 横纵坐标和原点绘制
    pygame.draw.circle(screen, GREY, (sx, sy), 6)  # 原点
    pygame.draw.line(screen, GREY, (-1e9, sy), (1e9, sy))  # x轴
    pygame.draw.line(screen, GREY, (sx, -1e9), (sx, 1e9))  # y轴

#  主函数
def main(speedlr,speedwa):
    run=True
    watch = 100  # 坐标轴缩放倍数 （每单位多少个像素）
    sx = screen.get_rect().centerx  # 原点横坐标像素位置
    sy = screen.get_rect().centery  # 原点纵坐标像素位置
    clock = pygame.time.Clock()
    while run:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
            key_pressed=pygame.key.get_pressed()
            # 按下ESC退出当前函数绘制
            if key_pressed[pygame.K_ESCAPE]:
                func.clear()
                run=False
            # 视窗上下移动
            if key_pressed[pygame.K_s]:
                sy-=speedlr
            if key_pressed[pygame.K_w]:
                sy+=speedlr
            # 视窗左右移动
            if key_pressed[pygame.K_a]:
                sx+=speedlr
            if key_pressed[pygame.K_d]:
                sx-=speedlr
            # 坐标轴缩放倍数控制
            if key_pressed[pygame.K_j]:
                watch+=speedwa
            if key_pressed[pygame.K_k]:
                watch-=speedwa
                watch=max(watch,1)  #  缩放极限，一单位一像素
            if key_pressed[pygame.K_LSHIFT] or key_pressed[pygame.K_RSHIFT]:
                if key_pressed[pygame.K_EQUALS]:
                    add_function()
        screen.fill(BLACK)
        # 绘制直角坐标系
        coordinate(sx,sy,watch)
        # 绘制所有函数
        draw_function(sx,sy,watch)
        pygame.display.flip()
while True:
    add_function()
    main(7,1)