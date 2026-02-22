#Read values x1,y1,x2,y2
#Calculate dx=x2-x1;dy=y2-y1
#If (x2>x1) lx=1 else lx=-1
#If (y2>y1) ly=1 else ly=-1
#If dx>dy(i.e m<1)
    #Pk= 2dy-dx
    #if (Pk<0)
        #xk+1=xk+lx
        #yk+1=yk
        #Pk+1=Px+2dy
    #else
        #xk+1=xk+1
        #yk+1=yk+1
        #Pk+1=Px+2dy-2dx



import pygame as py
import sys as sy
py.init()
w,h=600,600
screen=py.display.set_mode((w,h))
py.display.set_caption("DDA")
WHITE=(255,255,255)
BLACK=(0,0,0)

def bla(x1,y1,x2,y2):

    dx=abs(x2-x1)
    dy=abs(y2-y1)
    if dx>=0:
        lx=1
    else:
        lx=-1
    if dy>=0:
        ly=1
    else:
        ly=-1
    xk=x1
    yk=y1
    if dx>=dy:
        pk=2*dy-dx
        for i in range (dx+1):
            print(f"\n({xk},{yk}),{pk}")
            xk+=lx
            
            if pk<0:
                yk=yk
                pk+=2*dy
            else:
                yk+=ly
                pk+=2*dy-2*dx
            screen.set_at((round(xk),round(yk)),WHITE)

        
    else:
        pk=2*dx-dy
        for i in range (dy+1):
            print(f"\n({xk},{yk}),{pk}")
            yk+=ly
            if pk<=0:
                xk=xk
                pk+=2*dx
            else:
                xk+=lx
                pk+=2*dx-2*dy
            screen.set_at((round(xk),round(yk)),WHITE)


def main():
   
 
    while True:
        for event in py.event.get():
            if event.type==py.QUIT:
                py.quit()
                sy.exit()
        screen.fill(BLACK)

        bla(10,10,150,160)
        py.display.update()
   
if __name__=="__main__":
    main()