import pygame
import random

pygame.init()

red = 255,0,0
green = 0,255,0
blue = 0,0,255
yellow = 255,255,0

colors = [red,green,yellow,blue]

col = random.choice(colors)

width = 600
height = 500

speed = [2,2]

screen = pygame.display.set_mode((width,height))

screen.fill((255,255,255))

pygame.display.update()

x = 50
y = 50

clock = pygame.time.Clock()
FPS = 100
while True:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    screen.fill((255,255,255))

    pygame.draw.circle(screen, col, [x,y], 50)

    x += speed[0]
    y += speed[1]

    if x >= width - 50 or x == 40:
        speed[0] = -speed[0]
        col = random.choice(colors)
    elif y >= height - 50 or y == 40:
        speed[1] = -speed[1]
        col = random.choice(colors)

    pygame.display.update()
    clock.tick(FPS)
