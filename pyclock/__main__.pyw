import pygame

white = (255, 255, 255)
black = (0, 0, 0)

screen_size = (400, 400)
center = (200, 200)

screen = pygame.display.set_mode(screen_size)


def draw():
    screen.fill(white)
    pygame.draw.circle(screen, black, center, 10)
    pygame.draw.circle(screen, black, center, 150, 1)
    pygame.display.flip()


pygame.display.set_caption("pyclock")
pygame.init()

running = True
while running:

    draw()  

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False