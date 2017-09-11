import pygame

pygame.init()
pygame.mixer.init()

white = 255,255,255
red = 255,0,0
black = 0,0,0

screen = pygame.display.set_mode((500,500))
sound = pygame.mixer.Sound('music_1.ogg')
sound.play(-1)
while True:
    screen.fill(red)
    pygame.display.update()

