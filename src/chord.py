'''
Sandbox to calculate chord values.
They are 2sin(theta/2) in the unit circle.
'''

import math

angle: float = 45

distance: float = 0.0

distance = 2 * math.sin(math.radians(angle) / 2)

print(distance)