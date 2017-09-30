import pygame
import random
import time

pygame.init()

red = 255,0,0
green = 0,255,0
blue = 0,0,255
yellow = 255,255,0

colors = [red,green,yellow,blue]

screen = pygame.display.set_mode((600,500))

screen.fill((255,255,255))

pygame.display.update()

for event in pygame.event.get():

    if event.type == pygame.QUIT:
        pygame.quit()
        quit()

screen.fill((255,255,255))

for i in range(30):
    circle_x = random.randint(0,550)
    circle_y = random.randint(0,450)
    size = random.randint(20,80)
    col = random.choice(colors)
    pygame.draw.circle(screen, col, [circle_x, circle_y], size)
    circle_x += 5
    circle_y += 5
    pygame.display.update()
    time.sleep(0.5)
