import pygame

pygame.init()

red = 255,0,0

screen = pygame.display.set_mode((600,500))

screen.fill((255,255,255))

pygame.display.update()

while True:

    screen.fill((255,255,255))

    pygame.draw.rect(screen, red, [10,10,100,200])

    pygame.draw.circle(screen, red, [200,200], 150)

    pygame.display.update()
