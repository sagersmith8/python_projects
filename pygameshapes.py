import pygame
import random
import time

pygame.init()

r = (255,0,0)
g = (0,255,0)
b = (0,0,255)
w = (255,255,255)
bl = (0,0,0)
shape = 2
c = w

size = (700,500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Sage's fun shapes: c to cycle, r to reset")

done = False

clock = pygame.time.Clock()
screen.fill(c)
clock.tick(60)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type== pygame.KEYDOWN:
            if event.key == pygame.K_r:
                screen.fill(c)
            if event.key == pygame.K_c:
                if shape == 2:
                    shape = 3
                elif shape == 3:
                    shape = 6
                else:
                    shape = 2
                screen.fill(c)
    
    if shape%2 == 0:
        pygame.draw.rect(screen, (random.randrange(255),random.randrange(255),random.randrange(255)), (random.randrange(700),random.randrange(600),random.randrange(200),random.randrange(200)), 0)
    if shape % 3 == 0:
        pygame.draw.circle(screen,(random.randrange(255),random.randrange(255),random.randrange(255)),(random.randrange(700),random.randrange(600)), random.randrange(200),0)
    pygame.display.update()
    time.sleep(.1)
pygame.quit()
