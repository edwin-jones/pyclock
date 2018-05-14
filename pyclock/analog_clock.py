from pygame.math import Vector2


class AnalogClock:
    """This class is used to calculate the hand positions on an analog stopwatch-like clock"""

    second_hand_end_position = Vector2()
    minute_hand_end_position = Vector2()

    _start_hand_end_position = Vector2(0, -150) #150 will be default length of a hand
    _second_angle = 0
    _minute_angle = 0 
    _angle_per_second = 360 / 60
    _angle_per_minute = (360 / 60) / 60


    def __init__(self, center):
        self.center = center


    def _get_angle(self, angle, angle_increment, delta_time_milliseconds):
        """get the angle we should rotate by based on the time passed in milliseconds"""

        # clamp angle
        if angle >= 360:
            angle = 0

        # calculate the angle, plus the incremement size calculated with the elapsed time
        angle = angle + (angle_increment / 1000 * delta_time_milliseconds)

        return angle


    def update(self, delta_time):
        """Update the analog clock. Takes in the amount of milliseconds that have passed since the last call."""

        # calculate the angles of the hands 
        self._second_angle = self._get_angle(self._second_angle, self._angle_per_second, delta_time)
        self._minute_angle = self._get_angle(self._minute_angle, self._angle_per_minute, delta_time)
        
        # calculate the end positions of the hands.
        # we cheat a little here by dividing the results to make them shorter than the clock's radius.
        self.second_hand_end_position = self._start_hand_end_position.rotate(self._second_angle) / 1.25
        self.minute_hand_end_position = self._start_hand_end_position.rotate(self._minute_angle) / 2

        # We have to add the center of the clock to the results to make sure the hands have the correct origin
        self.second_hand_end_position = self.second_hand_end_position + self.center
        self.minute_hand_end_position = self.minute_hand_end_position + self.center
