import pygame
import random

pygame.init()

pygame.mixer.init()

red = 255,0,0
green = 0,255,0
blue = 0,0,255
yellow = 255,255,0

colors = [red,green,yellow,blue]

col = random.choice(colors)

width = 800
height = 600

speed = [2,2]

screen = pygame.display.set_mode((width,height))

img_1 = pygame.image.load("images/ball.jpg")
img_rect = img_1.get_rect()
sound = pygame.mixer.Sound('sounds/gunShot.wav')

while True:

    screen.fill((255,255,255))

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    img_rect = img_rect.move(speed)

    if img_rect.left < 0 or img_rect.right > width:
        speed[0] = -speed[0]
        sound.play()
    elif img_rect.top < 0 or img_rect.bottom > height:
        speed[1] = -speed[1]
        sound.play()

    screen.fill((255,255,255))

    # pygame.draw.circle(screen, col, [x,y], 50)
    screen.blit(img_1, img_rect)

    pygame.display.update()
