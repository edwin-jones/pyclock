import pygame

from analog_clock import AnalogClock

# create some tuples to represent RGB colors, positions and sizes.
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

screen_size = (400, 400)
center = (200, 200)

# create an instance of our helper class.
analog_clock = AnalogClock(center, 150)

# create a pygame clock for calculating how much time has passed etc.
pygame_clock = pygame.time.Clock()

# create a window based on the desired screen size.
screen = pygame.display.set_mode(screen_size)


def draw_graduations(analog_clock):
    """this function will draw all the graduations around the edge of the clock"""

    for position in analog_clock.graduation_positions:
        pygame.draw.line(screen, black, position.start, position.end, 1)


def draw(analog_clock):
    """this function draws the clock on the screen"""

    # pygame always draws back to front so what we do here is:
    
    # draw a white screen
    screen.fill(white)

    # draw the graduations
    draw_graduations(analog_clock)

    # draw the second hand
    pygame.draw.line(screen, red, center, analog_clock.second_hand_end_position, 1)

    # draw the minute hand
    pygame.draw.line(screen, black, center, analog_clock.minute_hand_end_position, 5)

    # draw the hour hand
    pygame.draw.line(screen, black, center, analog_clock.hour_hand_end_position, 5)

    # draw the center 'dot' of the clock'
    pygame.draw.circle(screen, black, center, 10)

    # draw the outer line of the clock.
    pygame.draw.circle(screen, black, center, 151, 1)

    # we have to call this for the display to update.
    pygame.display.flip()


# set the title of the window and initialize pygame
pygame.display.set_caption("pyclock")
pygame.init()

running = True
while running:

    # .tick will make this loop run at a maximum speed of the passed in seconds value.    
    pygame_clock.tick(30)

    # update the analog clock
    analog_clock.update()

    # draw the hands with the calculated end positions.
    draw(analog_clock)  

    # check for any exit button presses and quit the program if any are found.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False