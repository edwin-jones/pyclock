import pygame

# create some tuples to represent RGB colors, positions and sizes.
white = (255, 255, 255)
black = (0, 0, 0)

screen_size = (400, 400)
center = (200, 200)

# create a window based on the desired screen size.
screen = pygame.display.set_mode(screen_size)


# this is a small helper function we use to keep the code tidy
def draw():

    # pygame always draws back to front so what we do here is:
    
    # draw a white screen
    screen.fill(white)

    # draw the center 'dot' of the clock'
    pygame.draw.circle(screen, black, center, 10)

    # draw the outer line of the clock.
    pygame.draw.circle(screen, black, center, 150, 1)

    # we have to call this for the display to update.
    pygame.display.flip()


# set the title of the window and initialize pygame
pygame.display.set_caption("pyclock")
pygame.init()

running = True
while running:

    # draw the hands with the calculated end positions.
    draw()  

    # check for any exit button presses and quit the program if any are found.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False