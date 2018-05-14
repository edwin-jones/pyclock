import pygame
from pygame.math import Vector2

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)

(width, height) = (400, 400)
center = (200, 200)

start_hand_end_position = Vector2(0, -150)
second_hand_end_position = Vector2()
minute_hand_end_position = Vector2()

second_angle = 0
minute_angle = 0

clock = pygame.time.Clock()
screen = pygame.display.set_mode((width, height))


def update():
    global second_angle
    global minute_angle
    global minute_hand_end_position
    global second_hand_end_position

    #clamp angles
    if second_angle >= 360:
        second_angle = 0
    
    if minute_angle >= 360:
        minute_angle = 0
    

    angle_per_second = 360 / 60
    second_angle = second_angle + angle_per_second
    
    angle_per_minute = (360 / 60) / 60
    minute_angle = minute_angle + angle_per_minute

    second_hand_end_position = start_hand_end_position.rotate(second_angle) / 1.25
    minute_hand_end_position = start_hand_end_position.rotate(minute_angle) / 2

    # The current endpoint is the startpoint vector + the
    # rotated original endpoint vector.
    second_hand_end_position = second_hand_end_position + center
    minute_hand_end_position = minute_hand_end_position + center

def draw():
    screen.fill(white)
    pygame.draw.circle(screen, black, center, 10)
    pygame.draw.circle(screen, black, center, 150, 1)
    pygame.draw.line(screen, red, center, second_hand_end_position, 5)
    pygame.draw.line(screen, red, center, minute_hand_end_position, 5)
    pygame.display.flip()


pygame.init()

running = True
while running:

    update()
    draw()
    clock.tick(1)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False