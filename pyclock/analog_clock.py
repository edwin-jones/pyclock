from datetime import datetime
from pygame.math import Vector2


class AnalogClock:
    """This class is used to calculate the hand positions on an analog stopwatch-like clock"""

    second_hand_end_position = Vector2()
    minute_hand_end_position = Vector2()
    hour_hand_end_position = Vector2()

    def __init__(self, center, radius):
        
        #store the location of the center of the clock
        self.center = center

        # negative radius means the vector starts point up/at 12
        self._start_hand_end_position = Vector2(0, -radius)


    def _get_angle(self, total_positions, time_part):
        """get the angle we should rotate by based on the time part (secs/mins/hrs)"""

        # calculate the angle, plus the incremement size calculated with secs/mins/hrs
        angle = 360 / total_positions * time_part

        return angle


    def update(self):
        """Update the analog clock."""

        # get the current local system time
        time = datetime.now().time()

        # calculate the angles of the hands 
        second_angle = self._get_angle(60, time.second)
        minute_angle = self._get_angle(60, time.minute)
        hour_angle = self._get_angle(12, time.hour)
        
        # calculate the end positions of the hands.
        # we cheat a little here by altering the results to make
        # them shorter than the clock's radius.
        self.second_hand_end_position = self._start_hand_end_position.rotate(second_angle) * 0.9
        self.minute_hand_end_position = self._start_hand_end_position.rotate(minute_angle) * 0.75
        self.hour_hand_end_position = self._start_hand_end_position.rotate(hour_angle) * 0.5

        # We have to add the center of the clock to the results to make sure 
        # the hands have the correct origin
        self.second_hand_end_position += self.center
        self.minute_hand_end_position += self.center
        self.hour_hand_end_position += self.center
