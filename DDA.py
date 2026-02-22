import pygame
import sys
def dda(x1,y1,x2,y2,screen,color):
    dx=x2-x1
    dy=y2-y1
    steps=int(max(abs(dx),abs(dy)))
    xinc=dx/steps
    yinc=dy/steps
    x=x1
    y=y1
    for _ in range(steps+1):
        screen.set_at((round(x),round(y)),color)
        x+=xinc
        y+=yinc
def main():
    pygame.init()
    w,h=600,600
    screen=pygame.display.set_mode((w,h))
    pygame.display.set_caption("DDA")
    WHITE=(255,255,255)
    BLACK=(0,0,0)
    x1,y1=100,200
    x2,y2=200,400
    running=True
    while running:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
        screen.fill(BLACK)
        dda(x1,y1,x2,y2,screen,WHITE)
        pygame.display.update()
    pygame.quit()
    sys.exit()
if __name__=="__main__":
    main()
