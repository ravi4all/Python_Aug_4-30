import pygame

pygame.init()

size = width,height = 600,500

white = 255,255,255
red = 255,0,0

screen = pygame.display.set_mode(size)

clock = pygame.time.Clock()
FPS = 30

rect_x = 0
rect_y = 0

move_x = 0
move_y = 0

while True:

    screen.fill(white)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                move_x = 10
                move_y = 0
            elif event.key == pygame.K_LEFT:
                move_x = -10
                move_y = 0
            elif event.key == pygame.K_DOWN:
                move_y = 10
                move_x = 0
            elif event.key == pygame.K_UP:
                move_y = -10
                move_x = 0


    pygame.draw.rect(screen, red, [rect_x,rect_y,50,50])

    rect_x += move_x
    rect_y += move_y

    if rect_x >= width:
        rect_x = -50
    elif rect_y >= height:
        rect_y = -50
    elif rect_x <= -50:
        rect_x = width
    elif rect_y <= -50:
        rect_y = height

    pygame.display.update()
    clock.tick(FPS)
