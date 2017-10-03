import pygame
import random

pygame.init()

red = 255,0,0
green = 0,255,0
blue = 0,0,255
yellow = 255,255,0

colors = [red,green,yellow,blue]

col = random.choice(colors)

width = 800
height = 600

speed = [20,20]

screen = pygame.display.set_mode((width,height))

img_1 = pygame.image.load("images/ball.jpg")

pygame.display.update()

x = 50
y = 50

clock = pygame.time.Clock()
FPS = 30
while True:

    screen.fill((255,255,255))

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    screen.fill((255,255,255))

    # pygame.draw.circle(screen, col, [x,y], 50)
    screen.blit(img_1, [x,y])

    x += speed[0]
    y += speed[1]

    if x >= width - 225 or x <= 0:
        speed[0] = -speed[0]
        col = random.choice(colors)
        img_1 = pygame.transform.rotate(img_1, 90)
    elif y >= height - 225 or y <= 0:
        speed[1] = -speed[1]
        col = random.choice(colors)
        img_1 = pygame.transform.rotate(img_1, 90)

    pygame.display.update()
    clock.tick(FPS)
