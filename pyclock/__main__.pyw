import pygame

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

(width, height) = (640, 480)
center = (320, 240)
top = (320, 40)
screen = pygame.display.set_mode((width, height))

screen.fill(white)

pygame.draw.circle(screen, black, center, 3)

pygame.draw.circle(screen, black, center, 200, 1)

pygame.draw.line(screen, red, center, top)

pygame.display.flip()


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False