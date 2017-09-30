import pygame

pygame.init()

screen = pygame.display.set_mode((600,500))

# print(pygame.event.get())

screen.fill((255,255,255))

pygame.display.update()

while True:

    for event in pygame.event.get():
        print(event)

    screen.fill((255,255,255))

    pygame.display.update()
