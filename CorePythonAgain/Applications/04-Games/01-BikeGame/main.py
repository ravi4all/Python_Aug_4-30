import pygame
import random

pygame.init()

size = width,height = 800,600

white = 255,255,255
red = 255,0,0

screen = pygame.display.set_mode(size)

backgroundImage = pygame.image.load('assets/bg_1.jpg')
backgroundImage2 = pygame.image.load('assets/bg_2.jpg')

myCar = pygame.image.load("assets/car_1.png")
myCarRect = myCar.get_rect()
oppCar_1 = pygame.image.load("assets/car_2.png")
oppCar_1Rect = oppCar_1.get_rect()
oppCar_2 = pygame.image.load("assets/car_3.png")
oppCar_2Rect = oppCar_2.get_rect()

mainBg = pygame.image.load("assets/mainBg.jpg")
startGame = pygame.image.load("assets/startGame.png")

clock = pygame.time.Clock()
FPS = 30

def homeScreen():
    while True:
        screen.fill(white)
        posX,posY = pygame.mouse.get_pos()
        startGameRect = pygame.Rect(590, 200, startGame.get_width(), startGame.get_height())
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEMOTION:
                print(posX)
                if posX > 590 or posX < 730:
                    print("True")
                else:
                    print("False")

        screen.blit(mainBg, (0,0))
        screen.blit(startGame, (590, 200))

        pygame.display.update()



def mainGame():
    backgroundY = 0
    backgroundY2 = -height

    moveBackground = 10
    carX = width/2
    carY = height - 140

    moveCarPos = 0

    oppCar_1X = width/2 - 70
    oppCar_1Y = height - 140

    oppCar_2X = width/2 + 70
    oppCar_2Y = height - 140

    moveCar1 = random.randint(-6,-1)
    moveCar2 = random.randint(-6,-1)

    while True:

        screen.fill(white)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    moveBackground += 5
                    moveCarPos += 5
                    moveCar1 = random.randint(-6,-1)
                    moveCar2 = random.randint(-6,-1)
                elif event.key == pygame.K_DOWN:
                    moveBackground -= 5
            if event.type == pygame.KEYUP:
                moveCarPos = 0

        # print(moveBackground)

        screen.blit(backgroundImage, (0,0))
        screen.blit(backgroundImage, (0,backgroundY))
        screen.blit(backgroundImage2, (0,backgroundY2))

        carY -= moveCarPos

        oppCar_1Y += moveCar1
        oppCar_2Y += moveCar2

        if carY > height - 140 or carY < height/2 - 100:
            moveCarPos = 0

        if oppCar_1Y  < -100:
            moveCar1 = random.randint(1,6)
        elif oppCar_1Y > height:
            moveCar1 = random.randint(-6,-1)

        if oppCar_2Y < -100:
            moveCar2 = random.randint(2,7)
        elif oppCar_2Y > height:
            moveCar2 = random.randint(-8,-2)

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


##homeScreen()
mainGame()
