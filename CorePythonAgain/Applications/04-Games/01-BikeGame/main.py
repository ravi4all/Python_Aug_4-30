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

myCar = pygame.image.load("assets/car_1.png")
myCarRect = myCar.get_rect()
oppCar_1 = pygame.image.load("assets/car_2.png")
oppCar_1Rect = oppCar_1.get_rect()
oppCar_2 = pygame.image.load("assets/car_3.png")
oppCar_2Rect = oppCar_2.get_rect()

carX = width/2
carY = height - 140

oppCar_1X = width/2 - 70
oppCar_1Y = height - 140

oppCar_2X = width/2 + 70
oppCar_2Y = height - 140

clock = pygame.time.Clock()
FPS = 30

while True:

    screen.fill(white)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                moveBackground += 5
            elif event.key == pygame.K_DOWN:
                moveBackground -= 5
        # if event.type == pygame.KEYUP:
        #     moveBackground -= 10

    screen.blit(backgroundImage, (0,0))
    screen.blit(backgroundImage, (0,backgroundY))
    screen.blit(backgroundImage2, (0,backgroundY2))

    screen.blit(myCar, (carX, carY))
    screen.blit(oppCar_1, (oppCar_1X, oppCar_1Y))
    screen.blit(oppCar_2, (oppCar_2X, oppCar_2Y))

    backgroundY += moveBackground
    backgroundY2 += moveBackground

    if backgroundY > height:
        backgroundY = -height + 10
    elif backgroundY2 > height:
        backgroundY2 = -height + 10

    pygame.display.update()
    clock.tick(FPS)
