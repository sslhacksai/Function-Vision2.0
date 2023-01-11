import pygame
pygame.init()
from math import sin,cos,tan,sinh,cosh,tanh,asin,acos,atan,log,log2,log10,exp,pow,sqrt,gamma,pi,e,fabs,floor,ceil,gcd,trunc,nan
font=pygame.font.Font(None,50)
BLACK=(0,0,0)
WHITE=(255,255,255)
GREY=(100,100,100)
DARKGREY=(20,20,20)
RED=(255,150,150)
ORANGE=(255,175,139)
YELLOW=(255,234,174)
GREEN=(189,247,182)
CYAN=(118,231,189)
BLUE=(192,252,255)
PURPLE=(209,188,255)

if __name__=='__main__':
    cale=input()
    print(eval(cale))