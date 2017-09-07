import pygame

pygame.init()
pygame.mixer.init()

sound = pygame.mixer.Sound('music_1.ogg')
sound.play(1)
