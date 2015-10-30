import pygame

pygame.init()

r = (255,0,0)
g = (0,255,0)
b = (0,0,255)
w = (255,255,255)
bl = (0,0,0)

num = 0
c = r

size = (700,500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Sage's flashing screen")

done = False

clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    if num % 5 == 0:
        c = r
    elif num % 4 == 0:
        c = g
    elif num % 3 == 0:
        c = b
    elif num % 2 == 0:
        c = w
    else:
        c = bl

    num+=1
    screen.fill(c)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
