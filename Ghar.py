import pygame
pygame.init()
pixel_size = 1

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Bresenham Line - 9 Lines")
screen.fill(BLACK)

def bresenham_line(x1, y1, x2, y2):
    x, y = x1, y1
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    
    sx = 1 if x2 > x1 else -1
    sy = 1 if y2 > y1 else -1

    if dx > dy:
        p = 2 * dy - dx
        for _ in range(dx + 1):
            pygame.draw.rect(screen, WHITE, (x, y, pixel_size, pixel_size))
            if p >= 0:
                y += sy
                p -= 2 * dx
            x += sx
            p += 2 * dy
    else:  # slope > 1
        p = 2 * dx - dy
        for _ in range(dy + 1):
            pygame.draw.rect(screen, WHITE, (x, y, pixel_size, pixel_size))
            if p >= 0:
                x += sx
                p -= 2 * dy
            y += sy
            p += 2 * dx
lines = [
    (200, 300, 600, 300), 
    (600, 300, 600, 500),  
    (600, 500, 200, 500),  
    (200, 500, 200, 300),  
    (200, 300, 400, 150),  
    (400, 150, 600, 300),  
    (350, 500, 350, 400),  
    (350, 400, 450, 400), 
    (450, 400, 450, 500)   
]

for line in lines:
    bresenham_line(*line)

pygame.display.update()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
