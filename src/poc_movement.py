"Description: This is a sandbox file for testing purposes."

import random 
import math

initial_distance: int = 4500
deviation_angle: float = 0
daily_distance: float = 40
new_distance: int
day: int = 0

def calc_new_distance(daily_distance: float, initial_distance: int, deviation_angle: float) -> int:
	"""Calculates the new distance to the destination based on the deviation angle and two known distances.
	
	The formula is: n = sqrt(a^2 + b^2 - 2ab * cos(theta)), where:
	- n is the new distance to the destination
	- a is the daily distance traveled
	- b is the old distance to the destination
	- theta is the angle of deviation from the direct path
	"""
	new_distance = math.sqrt(math.pow(daily_distance, 2) + math.pow(initial_distance, 2) - 2 * daily_distance * initial_distance * math.cos(math.radians(deviation_angle)))
	return new_distance

def randomize_angle() -> int:
	"Generates a random angle between 0 and 90 degrees, following a normal distribution."
	mu = 0
	sigma = 30
	angle = random.gauss(mu, sigma)
	if -90 <= angle <= 90:
		return angle
	else:
		randomize_angle()

while initial_distance > 30:
	deviation_angle = randomize_angle()
	new_distance = calc_new_distance(daily_distance, initial_distance, deviation_angle)
	initial_distance = new_distance
	day += 1
	print(f"Day {day}: Angle is {deviation_angle}°, new distance is {new_distance} km")