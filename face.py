import pygame, sys
pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mid-point Circle Algorithm")
RED = (255, 0, 0)
BLUE = (0, 0, 128)
def draw_circle_algorithm(x, y, r, color=RED):
    X = 0
    Y = r
    d = 1 - r
    while X <= Y:
        screen.set_at((round(X + x), round(Y + y)), color)
        screen.set_at((round(-X + x), round(Y + y)), color)
        screen.set_at((round(X + x), round(-Y + y)), color)
        screen.set_at((round(-X + x), round(-Y + y)), color)
        screen.set_at((round(Y + x), round(X + y)), color)
        screen.set_at((round(-Y + x), round(X + y)), color)
        screen.set_at((round(Y + x), round(-X + y)), color)
        screen.set_at((round(-Y + x), round(-X + y)), color)
        if d < 0:
            d = d + 2 * X + 1
        else:
            d = d + 2 * (X - Y) + 1
            Y -= 1
        X += 1
def draw_smile(x, y, r):
    X = 0
    Y = r
    d = 1 - r
    while X <= Y:
        screen.set_at((x + X, y + Y), RED)
        screen.set_at((x - X, y + Y), RED)
        screen.set_at((x + Y, y + X), RED)
        screen.set_at((x - Y, y + X), RED)
        if d < 0:
            d = d + 2 * X + 3
            X += 1
            Y=Y
        else:
            d = d + 2 * (X - Y) + 5
            Y -= 1
            X += 1      
def face(x, y, r):
    draw_circle_algorithm(x, y, r)
    draw_circle_algorithm(x - 40, y - 40, 10)
    draw_circle_algorithm(x + 40, y - 40, 10)
    draw_smile(x, y + 30, 40)
def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.fill(BLUE)
        face(400, 300, 100)
        pygame.display.flip()
if __name__ == "__main__":
    main()