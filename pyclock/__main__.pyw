import pygame
from analog_clock import AnalogClock

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)

(width, height) = (400, 400)
center = (200, 200)

pygame_clock = pygame.time.Clock()
screen = pygame.display.set_mode((width, height))


def draw(second_hand_end_position, minute_hand_end_position):
    screen.fill(white)
    pygame.draw.circle(screen, black, center, 10)
    pygame.draw.circle(screen, black, center, 150, 1)
    pygame.draw.line(screen, red, center, second_hand_end_position, 5)
    pygame.draw.line(screen, red, center, minute_hand_end_position, 5)
    pygame.display.flip()


pygame.init()
pygame.display.set_caption("pyclock")

analog_clock = AnalogClock(center)

running = True
while running:

    delta_time = pygame_clock.tick(60)
    analog_clock.update(delta_time)
    draw(analog_clock.second_hand_end_position, analog_clock.minute_hand_end_position)  

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False