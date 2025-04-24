'''
Calculates the new distance to the destination based on the deviation angle and two known distances.
The formula is: n = sqrt(a^2 + b^2 - 2ab * cos(theta)), where:
- n is the new distance to the destination
- a is the daily distance traveled
- b is the old distance to the destination
- theta is the angle of deviation from the direct path
'''

import math

daily_distance: float = 1
angle: float = 90
old_distance: float = 2
new_distance: float

new_distance = math.sqrt(math.pow(daily_distance, 2) + math.pow(old_distance, 2) - 2 * daily_distance * old_distance * math.cos(math.radians(angle)))
print(new_distance)