import sys
import pygame
from os import path
import math
def resurce_path(relative_path):
    base_path=getattr(sys,'_MEIPASS',path.dirname(path.abspath(__file__)))
    return path.join(base_path,relative_path)
pygame.init()
font2=pygame.font.Font(resurce_path("air_mitalic.ttf"),70)
MYEVENT1=pygame.USEREVENT+1
def InputFunction(screen,font,color,position):
    screen.fill((0,0,0))
    while True:
        run=True
        a=[]
        flag=True
        while run:
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    sys.exit()
                if event.type==MYEVENT1:
                    flag=True
                    pygame.time.set_timer(MYEVENT1, 0)
                key = pygame.key.get_pressed()
                if key[pygame.K_BACKSPACE]:
                    if len(a) and flag:
                        del a[len(a) - 1]
                        flag=False
                        pygame.time.set_timer(MYEVENT1,200)
                if event.type==pygame.KEYDOWN:
                    if key[pygame.K_LSHIFT] or key[pygame.K_RSHIFT]:
                        if event.key==pygame.K_8:
                            a.append('*')
                        if event.key==pygame.K_9:
                            a.append('(')
                        if event.key==pygame.K_0:
                            a.append(')')
                        if event.key==pygame.K_EQUALS:
                            a.append('+')
                        if event.key==pygame.K_x:
                            a.append('X')
                        if event.key==pygame.K_MINUS:
                            a.append('_')
                    else:
                        if (event.key>=pygame.K_0 and event.key<=pygame.K_9) or event.key==pygame.K_MINUS or event.key==pygame.K_PERIOD or event.key==pygame.K_SLASH:
                            a.append(pygame.key.name(event.key))
                        if event.key >= 97 and event.key <= 122:
                            a.append(pygame.key.name(event.key))
                        if event.key==pygame.K_COMMA:
                            a.append(',')
                        if event.key==pygame.K_QUOTE:
                            a.append('\'')
                    if event.key==pygame.K_RETURN:
                        run=False
            screen.fill((0,0,0))
            rectimage=pygame.draw.rect(screen,(10,10,10),(50,360,700,80),0)
            text=font.render(str("".join(a)),True,color)
            rect=text.get_rect()
            rect.center=screen.get_rect().center
            screen.blit(text,rect)
            pygame.display.flip()
        f=str("".join(a))
        if f=='elpsycongroo':
            screen.fill((0,0,0))
            text = font2.render("El Psy Congroo", True, (255,255,255))
            screen.blit(text, (200, 300))
            pygame.display.flip()
            elpsycongroo=True
            while elpsycongroo:
                for event in pygame.event.get():
                    if event.type==pygame.QUIT:
                        sys.exit()
                    if event.type==pygame.KEYDOWN:
                        elpsycongroo=False
            continue
        return f

if __name__=='__main__':
    screen=pygame.display.set_mode((600,400))
    cale=InputFunction(screen,pygame.font.Font(None,40),(255,255,255),(20,20))
    screen.fill((0,0,0))
    text=pygame.font.Font(None,50).render(str(eval(cale)),True,(255,255,255))
    screen.blit(text,(20,20))
    pygame.display.flip()
    pygame.time.wait(2000)
    pygame.quit()
