import pygame
import random

pygame.init()

size = width,height = 600,500

white = 255,255,255
red = 255,0,0
green = 0,255,0
blue = 0,0,255
yellow = 255,255,0

colors = [red,green,yellow,blue]

col = random.choice(colors)

screen = pygame.display.set_mode(size)

clock = pygame.time.Clock()
FPS = 30

while True:

    screen.fill(white)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            col = random.choice(colors)

    pos_x, pos_y = pygame.mouse.get_pos()

    pygame.draw.circle(screen, col, [pos_x,pos_y], 50)


    pygame.display.update()
    clock.tick(FPS)
