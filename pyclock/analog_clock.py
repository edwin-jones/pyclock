import collections

from datetime import datetime
from pygame.math import Vector2

class AnalogClock:
    """This class is used to calculate the hand positions on an analog stopwatch-like clock"""

    # this tuple is used to store graduation position information for the analog clock face
    GraduationPosition = collections.namedtuple('GraduationPosition', 'start, end')
    
    second_hand_end_position = Vector2()
    minute_hand_end_position = Vector2()
    hour_hand_end_position = Vector2()

    def __init__(self, center, radius):
        
        # store the location of the center of the clock
        self.center = center

        # store radius of the clock
        self.radius = radius

        # figure out how thick the hour hand should be based on radius
        self.hour_hand_width = max(int(radius * 0.05), 1)

         # figure out how thick the minute hand should be based on radius
        self.minute_hand_width = max(int(radius * 0.05), 1)

        # figure out how thick the second hand should be based on radius
        self.second_hand_width = max(int(radius * 0.01), 1)

        # figure out how large the center dot of the clock face should be
        self.center_dot_radius = int(radius * 0.075)

        # negative radius means the vector starts point up/at 12
        self._start_hand_end_position = Vector2(0, -radius)

        # a list of all the graduation positions on the clock face
        self.graduation_positions = list(self._get_graduation_positions())


    def _get_angle(self, total_positions, time_part):
        """gets the angle we should rotate by based on the time part (secs/mins/hrs)"""

        # calculate the angle, plus the incremement size calculated with secs/mins/hrs
        angle = 360 / total_positions * time_part

        return angle


    def _get_graduation_positions(self):
        """gets all the graduation start and end positions for the analog clock.

        returns:
            A generator that iterates over GraduationPositions       
        """

        for i in range(1, 13):

            # get the angle for the current graduation
            angle = self._get_angle(12, i)

            # get the end position for the current graduation
            end = self.center + self._start_hand_end_position.rotate(angle)

            # get the direction from the end to the center (not normalized)
            direction = self.center - end

            # set the end point to be a scaled proportion of the direction
            # away from the start towards the center
            start = end + direction * 0.1

            # return this position of the sequence (this is a generator)
            yield self.GraduationPosition(start, end)


    def update(self):
        """update the analog clock"""

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