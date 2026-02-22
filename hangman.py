import pygame,sys
pygame.init()
WIDTH,HEIGHT=800,600
screen=pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Hangman Mid-point Circle & DDA")
RED=(255,0,0)
BLUE=(0,0,128)
def dda_line(x0,y0,x1,y1,color=RED):
 dx=x1-x0
 dy=y1-y0
 steps=max(abs(dx),abs(dy))
 Xinc=dx/steps
 Yinc=dy/steps
 x,y=x0,y0
 for _ in range(int(steps)+1):
  screen.set_at((round(x),round(y)),color)
  x+=Xinc
  y+=Yinc
def draw_circle_algorithm(x,y,r,color=RED):
 X=0
 Y=r
 d=1-r
 while X<=Y:
  screen.set_at((round(X+x),round(Y+y)),color)
  screen.set_at((round(-X+x),round(Y+y)),color)
  screen.set_at((round(X+x),round(-Y+y)),color)
  screen.set_at((round(-X+x),round(-Y+y)),color)
  screen.set_at((round(Y+x),round(X+y)),color)
  screen.set_at((round(-Y+x),round(X+y)),color)
  screen.set_at((round(Y+x),round(-X+y)),color)
  screen.set_at((round(-Y+x),round(-X+y)),color)
  if d<0:d+=2*X+3
  else:d+=2*(X-Y)+5;Y-=1
  X+=1
def draw_hangman():
 draw_circle_algorithm(400,150,30)
 dda_line(400,180,400,300)
 dda_line(400,220,360,260)
 dda_line(400,220,440,260)
 dda_line(400,300,360,360)
 dda_line(400,300,440,360)
def main():
 while True:
  for event in pygame.event.get():
   if event.type==pygame.QUIT:pygame.quit();sys.exit()
  screen.fill(BLUE)
  draw_hangman()
  pygame.display.flip()
if __name__=="__main__":
 main()
