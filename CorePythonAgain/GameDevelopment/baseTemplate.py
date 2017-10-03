import pygame

pygame.init()

size = width,height = 600,500

white = 255,255,255
red = 255,0,0

screen = pygame.display.set_mode(size)

clock = pygame.time.Clock()
FPS = 30

while True:

    screen.fill(white)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            quit()


    pygame.display.update()
    clock.tick(FPS)
