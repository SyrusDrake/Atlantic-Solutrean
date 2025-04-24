'''
Example of generating random numbers using Gaussian distribution'''

import random 
import matplotlib.pyplot as plt 

max_deviation: int = 90
	
# store the random numbers in a list 
nums = [] 
mu = 0
sigma = max_deviation / 3.0
	
for i in range(10000): 
	temp = random.gauss(mu, sigma)
	# This limits the deviation to a maximum specified above. Note that this is technically not a normal distribution.
	if -max_deviation <= temp <= max_deviation:
		nums.append(temp) 
		
# plotting a graph 
plt.hist(nums, bins = 200) 
plt.show() 
