import pygame

white = (255, 255, 255)

(width, height) = (480, 640)
screen = pygame.display.set_mode((width, height))

screen.fill(white)
pygame.display.flip()


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


