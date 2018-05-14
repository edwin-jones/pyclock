import pygame

white = (255, 255, 255)
black = (0, 0, 0)

(width, height) = (640, 480)
center = (320, 240)
screen = pygame.display.set_mode((width, height))

screen.fill(white)

pygame.draw.circle(screen, black, center, 3)

pygame.draw.circle(screen, black, center, 200, 1)

pygame.display.flip()


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
