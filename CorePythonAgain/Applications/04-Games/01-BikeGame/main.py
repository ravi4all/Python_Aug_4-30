import pygame

pygame.init()

size = width,height = 800,600

white = 255,255,255
red = 255,0,0

screen = pygame.display.set_mode(size)

backgroundImage = pygame.image.load('assets/bg_1.jpg')
backgroundImage2 = pygame.image.load('assets/bg_2.jpg')

backgroundY = 0
backgroundY2 = -height

moveBackground = 10

clock = pygame.time.Clock()
FPS = 30

while True:

    screen.fill(white)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    screen.blit(backgroundImage, (0,backgroundY))
    screen.blit(backgroundImage2, (0,backgroundY2))

    backgroundY += moveBackground
    backgroundY2 += moveBackground

    if backgroundY > height:
        backgroundY = -height + 10
    elif backgroundY2 > height:
        backgroundY2 = -height + 10

    pygame.display.update()
    clock.tick(FPS)
