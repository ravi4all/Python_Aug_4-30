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

x = 5
y = height/2 - 25

x1 = width - 55

clock = pygame.time.Clock()
FPS = 100
while True:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    screen.fill((255,255,255))

    rect_1 = pygame.draw.rect(screen, red, (x,y,50,50))
    rect_2 = pygame.draw.rect(screen, red, (x1,y,50,50))

    x += speed[0]
    x1 -= speed[0]

    if rect_1.colliderect(rect_2):
        speed[0] -= speed[0]

    if x > width - 50 or x1 < 0:
        speed[0] = -speed[0]

    pygame.display.update()
    clock.tick(FPS)
