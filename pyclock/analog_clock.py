from pygame.math import Vector2


class AnalogClock:
    """This class is used to calculate the hand positions on an analog stopwatch-like clock"""

    second_angle = 0
    minute_angle = 0
    second_hand_end_position = Vector2()
    minute_hand_end_position = Vector2()
    start_hand_end_position = Vector2(0, -150)
    angle_per_second = 360 / 60
    angle_per_minute = (360 / 60) / 60

    def __init__(self, center):
        self.center = center

    def get_angle(self, angle, angle_per_millisecond, delta_time):
        """get the angle we should rotate by based on the time passed"""

        #clamp angle
        if angle >= 360:
            angle = 0

        
        angle = angle + angle_per_millisecond / 1000 * delta_time

        return angle

    def update(self, delta_time):
        """Update the analog clock. Takes in the amount of milliseconds that have passed since the last call."""
        
        self.second_angle = self.get_angle(self.second_angle, self.angle_per_second, delta_time)
        self.minute_angle = self.get_angle(self.minute_angle, self.angle_per_minute, delta_time)
        
        self.second_hand_end_position = self.start_hand_end_position.rotate(self.second_angle) / 1.25
        self.minute_hand_end_position = self.start_hand_end_position.rotate(self.minute_angle) / 2

        self.second_hand_end_position = self.second_hand_end_position + self.center
        self.minute_hand_end_position = self.minute_hand_end_position + self.center
